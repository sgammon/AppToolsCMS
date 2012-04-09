# -*- coding: utf-8 -*-
from apptools import BaseService

from google.appengine.ext import ndb
from apptools.services import remote
from apptools.services import message_types

from project.models import blog as models
from project.messages import blog as messages


class BlogServiceError(remote.ApplicationError):

    ''' Abstract exception ancestor for BlogService-related exceptions. '''

    pass


class BlogNotFound(BlogServiceError):

    ''' Thrown when a blog cannot be found at a given key. '''

    pass


class PostNotFound(BlogServiceError):

    ''' Thrown when a blog post cannot be found at a given key. '''

    pass


class BlogService(BaseService):

    ''' API for managing blogs and blog posts. '''

    @remote.method(messages.Blog, messages.Blog)
    def put_blog(self, request):

        ''' Create a blog, which can contain posts. '''

        ## Resolve blog
        if request.key is not None:
            blog = ndb.Key(urlsafe=request.key).get()
            if blog is None:
                raise BlogNotFound("The specified blog does not exist.")
        else:
            blog = models.Blog(key=ndb.Key(models.Blog, request.slug))

        ## Add basic params
        blog.name = request.name
        blog.shortname = request.slug
        blog.byline = request.byline
        blog.creator = self.api.users.User(request.creator)
        blog.urlbase = request.urlbase
        blog.commenting = request.privacy.commenting
        if len(request.authors) > 0:
            blog.authors = [self.api.users.User(u) for u in request.authors]

        ## Add privacy settings
        blog.visibility = request.privacy.visibility
        if len(request.privacy.acl) > 0:
            blog.visible_acl = [self.api.users.User(u) for u in request.privacy.acl]
        if len(request.privacy.admin_acl) > 0:
            blog.admin_acl = [self.api.users.User(u) for u in request.privacy.admin_acl]
        if len(request.privacy.editor_acl) > 0:
            blog.editor_acl = [self.api.users.User(u) for u in request.privacy.editor_acl]

        ## Put blog and return
        bk = blog.put()
        return messages.Blog(

            key=bk.urlsafe(),
            name=blog.name,
            byline=blog.byline,
            authors=[str(u.nickname()) for u in blog.authors],
            urlbase=blog.urlbase,
            creator=str(blog.creator.nickname()),
            created=str(blog.created),
            touched=str(blog.touched),
            privacy=messages.PrivacyOptions(

                acl=[str(u.nickname()) for u in blog.visible_acl],
                visibility=blog.visibility,
                admin_acl=[str(u.nickname()) for u in blog.admin_acl],
                editor_acl=[str(u.nickname()) for u in blog.editor_acl],
                commenting=blog.commenting

            )
        )

    @remote.method(messages.BlogPost, messages.BlogPost)
    def put_post(self, request):

        ''' Create a post in a blog. '''

        ## Resolve blog
        try:
            blog = ndb.Key(urlsafe=request.blog).get()
            if blog is None:
                raise BlogNotFound("Could not save post because the specified blog could not be found.")
        except BlogNotFound:
            raise
        except Exception:
            raise BlogNotFound("Could not save post because the specified blog key was malformed or could not be found.")
        else:
            ## Resolve post (if we're editing)
            if request.key is not None:
                post = ndb.Key(urlsafe=request.key).get()
                if post is None:
                    raise PostNotFound("The specified post does not exist.")

            ## There won't be a key if it's a new post...
            else:
                post = models.BlogPost(id=request.slug, parent=blog.key)

            ## Set post properties
            post.title = request.title
            post.author = self.api.users.User(request.author)
            post.status = request.status
            post.byline = request.byline
            post.body = ndb.Text(request.body)
            post.excerpt = request.excerpt
            post.published = request.published
            post.visibility = request.privacy.visibility
            post.commenting = request.privacy.commenting
            post.tags = request.tags
            if len(request.privacy.acl) > 0:
                post.visible_acl = [self.api.users.User(u) for u in request.privacy.acl]
            if len(request.privacy.admin_acl) > 0:
                post.admin_acl = [self.api.users.User(u) for u in request.privacy.admin_acl]
            if len(request.privacy.editor_acl) > 0:
                post.editor_acl = [self.api.users.User(u) for u in request.privacy.editor_acl]

            ## Put post and return
            pk = post.put()
            return messages.BlogPost(

                key=pk.urlsafe(),
                slug=post.shortname,
                blog=pk.parent().urlsafe(),
                title=post.title,
                author=str(post.author.nickname()),
                status=post.status,
                byline=post.byline,
                body=post.body,
                excerpt=post.excerpt,
                published=post.published,
                prviacy=messages.PrivacyOptions(

                    acl=[str(u.nickname()) for u in post.visible_acl],
                    visibility=post.visibility,
                    admin_acl=[str(u.nickname()) for u in post.admin_acl],
                    editor_acl=[str(u.nickname()) for u in post.editor_acl],
                    commenting=post.commenting

                )
            )

    @remote.method(message_types.VoidMessage, messages.Blogs)
    def list_blogs(self, request):

        ''' List available blogs. '''

        bq = models.Blog.query().order(models.Blog.name)
        blogs = bq.fetch(bq.count())
        return messages.Blogs(

            keys=[b.key.urlsafe() for b in blogs],
            count=len(blogs),
            blogs=[messages.Blog(

                key=b.key.urlsafe(),
                name=b.name,
                byline=b.byline,
                authors=[str(u.nickname()) for u in b.authors],
                urlbase=b.urlbase,
                creator=str(b.creator.nickname()),
                created=str(b.created),
                touched=str(b.touched),
                privacy=messages.PrivacyOptions(

                    acl=[str(u.nickname()) for u in b.visible_acl],
                    visibility=b.visibility,
                    admin_acl=[str(u.nickname()) for u in b.admin_acl],
                    editor_acl=[str(u.nickname()) for u in b.editor_acl],
                    commenting=b.commenting

                )

            ) for b in blogs],

        )

    @remote.method(messages.Blog, messages.BlogPosts)
    def list_posts(self, request):

        ''' List available posts, optionally scoped to a blog. '''

        try:
            if request.blog is not None:
                blog = ndb.Key(urlsafe=request.blog)
                if blog is None:
                    raise BlogNotFound("Could not list posts for the specified blog because it could not be found.")
                else:
                    pq = models.BlogPost.query(ancestor=blog.key).order(-models.BlogPost.created)
            else:
                pq = models.BlogPost.query().order(-models.BlogPost.created)

        except BlogNotFound:
            raise

        except Exception:
            raise BlogNotFound("Could not list posts for the specified blog because the blog key was malformed or could not be found.")

        else:

            posts = pq.fetch(pq.count())
            blogs = []
            for post in posts:
                if post.parent() not in blogs:
                    blogs.append(post.parent())
            blogs = ndb.get_multi(blogs, use_cache=True, use_memcache=True)

            return messages.BlogPosts(

                keys=[p.key.urlsafe() for p in posts],
                count=len(posts),
                blogs=[messages.Blog(

                    key=b.key.urlsafe(),
                    name=b.name,
                    byline=b.byline,
                    authors=[str(u.nickname()) for u in b.authors],
                    urlbase=b.urlbase,
                    creator=str(b.creator.nickname()),
                    created=str(b.created),
                    touched=str(b.touched),
                    privacy=messages.PrivacyOptions(

                        acl=[str(u.nickname()) for u in b.visible_acl],
                        visibility=b.visibility,
                        admin_acl=[str(u.nickname()) for u in b.admin_acl],
                        editor_acl=[str(u.nickname()) for u in b.editor_acl],
                        commenting=b.commenting

                    )

                ) for b in blogs],

                posts=[messages.BlogPost(

                    key=p.key.urlsafe(),
                    author=str(p.author.nickname()),
                    slug=p.shortname,
                    title=p.title,
                    byline=p.byline,
                    body=p.body,
                    excerpt=p.excerpt,
                    published=p.published,
                    tags=p.tags,
                    privacy=messages.PrivacyOptions(

                        acl=[str(u.nickname()) for u in p.visible_acl],
                        visibility=b.visibility,
                        admin_acl=[str(u.nickname()) for u in p.admin_acl],
                        editor_acl=[str(u.nickname()) for u in p.editor_acl],
                        commenting=p.commenting

                    )

                ) for p in posts]

            )

    @remote.method(messages.Blog, message_types.VoidMessage)
    def delete_blog(self, request):

        ''' Delete an entire blog. '''

        try:
            if request.key is not None:
                blog = models.Blog.get(urlsafe=request.key)
                if blog is None:
                    raise BlogNotFound("The specified blog could not be found.")
                else:
                    blog.key.delete()
                    return message_types.VoidMessage()
            else:
                raise BlogNotFound("You must specify a blog to delete.")

        except BlogNotFound:
            raise

        except Exception:
            raise BlogNotFound("The specified blog could not be found, either because the key was malformed or it does not exist.")

    @remote.method(messages.BlogPost, message_types.VoidMessage)
    def delete_post(self, request):

        ''' Delete a post from a blog. '''

        try:
            if request.key is not None:
                post = models.BlogPost.get(urlsafe=request.key)
                if post is None:
                    raise PostNotFound("The specified post could not be found.")
                else:
                    post.key.delete()
                    return message_types.VoidMessage()
            else:
                raise PostNotFound("You must specify a post to delete.")

        except PostNotFound:
            raise

        except Exception:
            raise PostNotFound("The specified post could not be found, either because the key was malformed or it does not exist.")
