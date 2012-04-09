# -*- coding: utf-8 -*-
from webapp2 import Redirect
from apptools import BaseHandler
from apptools.util import json
from apptools.core import _apibridge
from apptools.models.builtin import StoredAsset
from apptools.models.builtin import UploadSession

from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers


class UploadPassthrough(blobstore_handlers.BlobstoreUploadHandler):

    ''' Receives the callback from the blobstore and stores a corresponding StoredAsset record, then redirects to UploadCallback to print. '''

    api = _apibridge

    def get(self, session):
        return self.handle(session)

    def post(self, session):
        return self.handle(session)

    def handle(self, session):

        ''' Update the UploadSession, save a StoredAsset and redirect to the callback. '''

        ## Get upload session
        us = UploadSession.get_by_id(session)
        us.status = 'success'

        ## Make assets
        assets = []
        uploads = self.get_uploads()
        for upload in uploads:
            cdn = None

            ## If CDN is enabled and it's an image, get a fast serving URL
            if us.enable_cdn:
                if upload.content_type.startswith('image/'):
                    cdn = self.api.images.get_serving_url(upload.key())

            assets.append(StoredAsset(id=str(upload.key()), filename=upload.filename, blobkey=upload.key(), serve_url=self.url_for('dynamic-asset', blobkey=str(upload.key())), cdn_url=cdn, content_type=upload.content_type))

        ## Store the assets, update the session
        assets = ndb.put_multi(assets, use_cache=True, use_memcache=True, use_datastore=True)
        us.assets = assets
        us.put()

        ## Generate a redirect to the callback, with instructions to print the first blob of the set
        redirect = Redirect(self.url_for('upload-callback', session=session, blobkey=str(assets[0].blobkey)))
        redirect.body = ''

        return redirect


class UploadCallback(BaseHandler):

    ''' Prints details about an uploaded blob in JSON for the uploading page to read. '''

    def get(self, session):
        return self.handle(session)

    def post(self, session):
        return self.handle(session)

    def handle(self, session):

        ''' Retrieve a session, convert it (and each blobinfo) to a JSON structure and print it. '''

        us = UploadSession.get_by_id(session)
        assets = ndb.get_multi(us.assets, use_cache=True, use_memcache=True, use_datastore=True)

        blobs = []
        for asset in assets:
            blobs.append({

                'asset': str(asset.key.urlsafe()),
                'blobkey': str(asset.blobkey),
                'filename': asset.filename,
                'content_type': asset.content_type,
                'serve_url': asset.serve_url,
                'cdn_url': asset.cdn_url

            })

        self.respone.write(json.dumps({'session': session, 'count': len(blobs), 'blobs': blobs}))
        return
