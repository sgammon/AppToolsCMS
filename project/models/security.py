from apptools import ndb


## == Content-oriented Security == #
class ContentPrivacy(ndb.Model):

    ''' Specifies privacy/seucurity options on a piece of content. '''

    pass


class PageSecurity(ndb.Model):

    ''' Specifies security options on an entire site page. '''

    pass


## === User-oriented Security === #
class Role(ndb.Model):

    ''' Represents a security role that can be applied to a user. '''

    pass


class Privilege(ndb.Model):

    ''' Represents a security privilege that can be applied to a user. '''

    pass
