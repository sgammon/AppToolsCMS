from apptools import ndb


### === Basic user account stuff === ###
class UserAccount(ndb.Model):

    ''' Represents a user account on this system. '''

    pass


### === Basic permissions/security stuff === ###
class Role(ndb.Model):

    ''' Represents a security role that can be applied to a user. '''

    pass


class Privilege(ndb.Model):

    ''' Represents a security privilege that can be applied to a user. '''

    pass


class AuditRecord(ndb.Model):

    ''' Represents a record of an admin's action, for audit purposes. '''

    pass
