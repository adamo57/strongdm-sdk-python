class Error(Exception):
    pass

# AlreadyExistsError is used when an entity already exists in the system
class AlreadyExistsError(Error):
    def __init__(self, msg, entities):
        self.msg = msg
        self.entities = entities

# NotFoundError is used when an entity does not exist in the system
class NotFoundError(Error):
    def __init__(self, msg, entities):
        self.msg = msg
        self.entities = entities

# BadRequestError identifies a bad request sent by the client
class BadRequestError(Error):
    def __init__(self, msg):
        self.msg = msg

# AuthenticationError is used to specify an authentication failure condition
class AuthenticationError(Error):
    def __init__(self, msg):
        self.msg = msg

# PermissionError is used to specify a permissions violation
class PermissionError(Error):
    def __init__(self, msg, permission, entities):
        self.msg = msg
        self.permission = permission
        self.entities = entities

# InternalError is used to specify an internal system error
class InternalError(Error):
    def __init__(self, msg):
        self.msg = msg

# RateLimitError is used for rate limit excess condition
class RateLimitError(Error):
    def __init__(self, msg):
        self.msg = msg

# RPCError is a generic RPC error
class RPCError(Error):
    def __init__(msg, code):
        self.msg = msg
        self.code = code