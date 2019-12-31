import collections


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port:
# certificate_authority:
# client_certificate:
# client_key:
class Kubernetes:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'hostname', 'port',
        'certificate_authority', 'client_certificate', 'client_key'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.hostname = None
        self.port = None
        self.certificate_authority = None
        self.client_certificate = None
        self.client_key = None

    def __repr__(self):
        return '<sdm.Kubernetes id: {0} name: {1} port_override: {2} healthy: {3} hostname: {4} port: {5} certificate_authority: {6} client_certificate: {7} client_key: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.hostname), repr(self.port),
            repr(self.certificate_authority), repr(self.client_certificate),
            repr(self.client_key))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# endpoint:
# access_key:
# secret_access_key:
# certificate_authority:
# region:
# cluster_name:
class AmazonEKS:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'endpoint', 'access_key',
        'secret_access_key', 'certificate_authority', 'region', 'cluster_name'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.endpoint = None
        self.access_key = None
        self.secret_access_key = None
        self.certificate_authority = None
        self.region = None
        self.cluster_name = None

    def __repr__(self):
        return '<sdm.AmazonEKS id: {0} name: {1} port_override: {2} healthy: {3} endpoint: {4} access_key: {5} secret_access_key: {6} certificate_authority: {7} region: {8} cluster_name: {9}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.endpoint), repr(self.access_key),
            repr(self.secret_access_key), repr(self.certificate_authority),
            repr(self.region), repr(self.cluster_name))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# endpoint:
# certificate_authority:
# service_account_key:
class GoogleGKE:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'endpoint',
        'certificate_authority', 'service_account_key'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.endpoint = None
        self.certificate_authority = None
        self.service_account_key = None

    def __repr__(self):
        return '<sdm.GoogleGKE id: {0} name: {1} port_override: {2} healthy: {3} endpoint: {4} certificate_authority: {5} service_account_key: {6}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.endpoint),
            repr(self.certificate_authority), repr(self.service_account_key))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# port:
# public_key:
class SSH:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'hostname', 'username',
        'port', 'public_key'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.port = None
        self.public_key = None

    def __repr__(self):
        return '<sdm.SSH id: {0} name: {1} port_override: {2} healthy: {3} hostname: {4} username: {5} port: {6} public_key: {7}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.hostname), repr(self.username),
            repr(self.port), repr(self.public_key))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# url:
# healthcheck_path:
# username:
# password:
# headers_blacklist:
# default_path:
# subdomain:
class HTTPBasicAuth:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'url', 'healthcheck_path',
        'username', 'password', 'headers_blacklist', 'default_path',
        'subdomain'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.url = None
        self.healthcheck_path = None
        self.username = None
        self.password = None
        self.headers_blacklist = None
        self.default_path = None
        self.subdomain = None

    def __repr__(self):
        return '<sdm.HTTPBasicAuth id: {0} name: {1} port_override: {2} healthy: {3} url: {4} healthcheck_path: {5} username: {6} password: {7} headers_blacklist: {8} default_path: {9} subdomain: {10}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.url), repr(self.healthcheck_path),
            repr(self.username), repr(self.password),
            repr(self.headers_blacklist), repr(self.default_path),
            repr(self.subdomain))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# url:
# healthcheck_path:
# headers_blacklist:
# default_path:
# subdomain:
class HTTPNoAuth:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'url', 'healthcheck_path',
        'headers_blacklist', 'default_path', 'subdomain'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.url = None
        self.healthcheck_path = None
        self.headers_blacklist = None
        self.default_path = None
        self.subdomain = None

    def __repr__(self):
        return '<sdm.HTTPNoAuth id: {0} name: {1} port_override: {2} healthy: {3} url: {4} healthcheck_path: {5} headers_blacklist: {6} default_path: {7} subdomain: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.url), repr(self.healthcheck_path),
            repr(self.headers_blacklist), repr(self.default_path),
            repr(self.subdomain))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# url:
# healthcheck_path:
# auth_header:
# headers_blacklist:
# default_path:
# subdomain:
class HTTPAuth:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'url', 'healthcheck_path',
        'auth_header', 'headers_blacklist', 'default_path', 'subdomain'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.url = None
        self.healthcheck_path = None
        self.auth_header = None
        self.headers_blacklist = None
        self.default_path = None
        self.subdomain = None

    def __repr__(self):
        return '<sdm.HTTPAuth id: {0} name: {1} port_override: {2} healthy: {3} url: {4} healthcheck_path: {5} auth_header: {6} headers_blacklist: {7} default_path: {8} subdomain: {9}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.url), repr(self.healthcheck_path),
            repr(self.auth_header), repr(self.headers_blacklist),
            repr(self.default_path), repr(self.subdomain))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port:
class Mysql:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'hostname', 'username',
        'password', 'database', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port = None

    def __repr__(self):
        return '<sdm.Mysql id: {0} name: {1} port_override: {2} healthy: {3} hostname: {4} username: {5} password: {6} database: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.hostname), repr(self.username),
            repr(self.password), repr(self.database), repr(self.port))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port:
class AuroraMysql:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'hostname', 'username',
        'password', 'database', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port = None

    def __repr__(self):
        return '<sdm.AuroraMysql id: {0} name: {1} port_override: {2} healthy: {3} hostname: {4} username: {5} password: {6} database: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.hostname), repr(self.username),
            repr(self.password), repr(self.database), repr(self.port))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port:
class Clustrix:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'hostname', 'username',
        'password', 'database', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port = None

    def __repr__(self):
        return '<sdm.Clustrix id: {0} name: {1} port_override: {2} healthy: {3} hostname: {4} username: {5} password: {6} database: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.hostname), repr(self.username),
            repr(self.password), repr(self.database), repr(self.port))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port:
class Maria:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'hostname', 'username',
        'password', 'database', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port = None

    def __repr__(self):
        return '<sdm.Maria id: {0} name: {1} port_override: {2} healthy: {3} hostname: {4} username: {5} password: {6} database: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.hostname), repr(self.username),
            repr(self.password), repr(self.database), repr(self.port))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port:
class Memsql:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'hostname', 'username',
        'password', 'database', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port = None

    def __repr__(self):
        return '<sdm.Memsql id: {0} name: {1} port_override: {2} healthy: {3} hostname: {4} username: {5} password: {6} database: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.hostname), repr(self.username),
            repr(self.password), repr(self.database), repr(self.port))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# port_override: Port number override.
# healthy: True if the datasource is reachable and the credentials are valid.
# access_key:
# secret_access_key:
# region:
# output:
class Athena:
    __slots__ = [
        'id', 'name', 'port_override', 'healthy', 'access_key',
        'secret_access_key', 'region', 'output'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.port_override = None
        self.healthy = None
        self.access_key = None
        self.secret_access_key = None
        self.region = None
        self.output = None

    def __repr__(self):
        return '<sdm.Athena id: {0} name: {1} port_override: {2} healthy: {3} access_key: {4} secret_access_key: {5} region: {6} output: {7}>'.format(
            repr(self.id), repr(self.name), repr(self.port_override),
            repr(self.healthy), repr(self.access_key),
            repr(self.secret_access_key), repr(self.region), repr(self.output))


# CreateResponseMetadata is reserved for future use.
class CreateResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.CreateResponseMetadata>'.format()


# GetResponseMetadata is reserved for future use.
class GetResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.GetResponseMetadata>'.format()


# UpdateResponseMetadata is reserved for future use.
class UpdateResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.UpdateResponseMetadata>'.format()


# DeleteResponseMetadata is reserved for future use.
class DeleteResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.DeleteResponseMetadata>'.format()


# RateLimitMetadata contains information about remaining requests avaialable
# to the user over some timeframe.
# limit: How many total requests the user/token is authorized to make before being
# rate limited.
# remaining: How many remaining requests out of the limit are still avaialable.
# reset_at: The time when remaining will be reset to limit.
# bucket: The bucket this user/token is associated with, which may be shared between
# multiple users/tokens.
class RateLimitMetadata:
    __slots__ = ['limit', 'remaining', 'reset_at', 'bucket']

    def __init__(self):
        self.limit = None
        self.remaining = None
        self.reset_at = None
        self.bucket = None

    def __repr__(self):
        return '<sdm.RateLimitMetadata limit: {0} remaining: {1} reset_at: {2} bucket: {3}>'.format(
            repr(self.limit), repr(self.remaining), repr(self.reset_at),
            repr(self.bucket))


# NodeCreateResponse reports how the Nodes were created in the system.
# meta: Reserved for future use.
# node: The created Node.
# token: The auth token generated for the Node. The Node will use this token to
# authenticate with the strongDM API.
# rate_limit: Rate limit information.
class NodeCreateResponse:
    __slots__ = ['meta', 'node', 'token', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.node = None
        self.token = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeCreateResponse meta: {0} node: {1} token: {2} rate_limit: {3}>'.format(
            repr(self.meta), repr(self.node), repr(self.token),
            repr(self.rate_limit))


# NodeGetResponse returns a requested Node.
# meta: Reserved for future use.
# node: The requested Node.
# rate_limit: Rate limit information.
class NodeGetResponse:
    __slots__ = ['meta', 'node', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeGetResponse meta: {0} node: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.node), repr(self.rate_limit))


# NodeUpdateResponse returns the fields of a Node after it has been updated by
# a NodeUpdateRequest.
# meta: Reserved for future use.
# node: The updated Node.
# rate_limit: Rate limit information.
class NodeUpdateResponse:
    __slots__ = ['meta', 'node', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeUpdateResponse meta: {0} node: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.node), repr(self.rate_limit))


# NodeDeleteResponse returns information about a Node that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class NodeDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# Relay represents a StrongDM CLI installation running in relay mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the relay. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
class Relay:
    __slots__ = ['id', 'name', 'state']

    def __init__(self):
        self.id = None
        self.name = None
        self.state = None

    def __repr__(self):
        return '<sdm.Relay id: {0} name: {1} state: {2}>'.format(
            repr(self.id), repr(self.name), repr(self.state))


# Gateway represents a StrongDM CLI installation running in gateway mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the gateway. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
# listen_address: The public hostname/port tuple at which the gateway will be accessible to clients.
# bind_address: The hostname/port tuple which the gateway daemon will bind to.
class Gateway:
    __slots__ = ['id', 'name', 'state', 'listen_address', 'bind_address']

    def __init__(self):
        self.id = None
        self.name = None
        self.state = None
        self.listen_address = None
        self.bind_address = None

    def __repr__(self):
        return '<sdm.Gateway id: {0} name: {1} state: {2} listen_address: {3} bind_address: {4}>'.format(
            repr(self.id), repr(self.name), repr(self.state),
            repr(self.listen_address), repr(self.bind_address))


# ResourceCreateResponse reports how the Resources were created in the system.
# meta: Reserved for future use.
# resource: The created Resource.
# rate_limit: Rate limit information.
class ResourceCreateResponse:
    __slots__ = ['meta', 'resource', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceCreateResponse meta: {0} resource: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.resource), repr(self.rate_limit))


# ResourceGetResponse returns a requested Resource.
# meta: Reserved for future use.
# resource: The requested Resource.
# rate_limit: Rate limit information.
class ResourceGetResponse:
    __slots__ = ['meta', 'resource', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceGetResponse meta: {0} resource: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.resource), repr(self.rate_limit))


# ResourceUpdateResponse returns the fields of a Resource after it has been updated by
# a ResourceUpdateRequest.
# meta: Reserved for future use.
# resource: The updated Resource.
# rate_limit: Rate limit information.
class ResourceUpdateResponse:
    __slots__ = ['meta', 'resource', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceUpdateResponse meta: {0} resource: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.resource), repr(self.rate_limit))


# ResourceDeleteResponse returns information about a Resource that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class ResourceDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# RoleAttachmentCreateResponse reports how the RoleAttachments were created in the system.
# meta: Reserved for future use.
# role_attachment: The created RoleAttachment.
# rate_limit: Rate limit information.
class RoleAttachmentCreateResponse:
    __slots__ = ['meta', 'role_attachment', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role_attachment = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentCreateResponse meta: {0} role_attachment: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role_attachment), repr(self.rate_limit))


# RoleAttachmentGetResponse returns a requested RoleAttachment.
# meta: Reserved for future use.
# role_attachment: The requested RoleAttachment.
# rate_limit: Rate limit information.
class RoleAttachmentGetResponse:
    __slots__ = ['meta', 'role_attachment', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role_attachment = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentGetResponse meta: {0} role_attachment: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role_attachment), repr(self.rate_limit))


# RoleAttachmentDeleteResponse returns information about a RoleAttachment that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleAttachmentDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# A RoleAttachment connects a composite role to another role, granting members
# of the composite role the permissions granted to the attached role.
# id: Unique identifier of the RoleAttachment.
# composite_role_id: The id of the composite role of this RoleAttachment.
# attached_role_id: The id of the attached role of this RoleAttachment.
class RoleAttachment:
    __slots__ = ['id', 'composite_role_id', 'attached_role_id']

    def __init__(self):
        self.id = None
        self.composite_role_id = None
        self.attached_role_id = None

    def __repr__(self):
        return '<sdm.RoleAttachment id: {0} composite_role_id: {1} attached_role_id: {2}>'.format(
            repr(self.id), repr(self.composite_role_id),
            repr(self.attached_role_id))


# RoleCreateResponse reports how the Roles were created in the system. It can
# communicate partial successes or failures.
# meta: Reserved for future use.
# role: The created Role.
# rate_limit: Rate limit information.
class RoleCreateResponse:
    __slots__ = ['meta', 'role', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleCreateResponse meta: {0} role: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role), repr(self.rate_limit))


# RoleGetResponse returns a requested Role.
# meta: Reserved for future use.
# role: The requested Role.
# rate_limit: Rate limit information.
class RoleGetResponse:
    __slots__ = ['meta', 'role', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleGetResponse meta: {0} role: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role), repr(self.rate_limit))


# RoleUpdateResponse returns the fields of a Role after it has been updated by
# a RoleUpdateRequest.
# meta: Reserved for future use.
# role: The updated Role.
# rate_limit: Rate limit information.
class RoleUpdateResponse:
    __slots__ = ['meta', 'role', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleUpdateResponse meta: {0} role: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role), repr(self.rate_limit))


# RoleDeleteResponse returns information about a Role that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# A Role grants users access to a set of resources. Composite roles have no
# resource associations of their own, but instead grant access to the combined
# resources of their child roles.
# id: Unique identifier of the Role.
# name: Unique human-readable name of the Role.
# composite: True if the Role is a composite role.
class Role:
    __slots__ = ['id', 'name', 'composite']

    def __init__(self):
        self.id = None
        self.name = None
        self.composite = None

    def __repr__(self):
        return '<sdm.Role id: {0} name: {1} composite: {2}>'.format(
            repr(self.id), repr(self.name), repr(self.composite))
