# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import nodes_pb2 as nodes__pb2


class NodesStub(object):
  """Nodes service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/v1.Nodes/Create',
        request_serializer=nodes__pb2.NodeCreateRequest.SerializeToString,
        response_deserializer=nodes__pb2.NodeCreateResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/v1.Nodes/Get',
        request_serializer=nodes__pb2.NodeGetRequest.SerializeToString,
        response_deserializer=nodes__pb2.NodeGetResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/v1.Nodes/Update',
        request_serializer=nodes__pb2.NodeUpdateRequest.SerializeToString,
        response_deserializer=nodes__pb2.NodeUpdateResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/v1.Nodes/Delete',
        request_serializer=nodes__pb2.NodeDeleteRequest.SerializeToString,
        response_deserializer=nodes__pb2.NodeDeleteResponse.FromString,
        )
    self.List = channel.unary_unary(
        '/v1.Nodes/List',
        request_serializer=nodes__pb2.NodeListRequest.SerializeToString,
        response_deserializer=nodes__pb2.NodeListResponse.FromString,
        )
    self.BatchUpdate = channel.unary_unary(
        '/v1.Nodes/BatchUpdate',
        request_serializer=nodes__pb2.NodeBatchUpdateRequest.SerializeToString,
        response_deserializer=nodes__pb2.NodeBatchUpdateResponse.FromString,
        )
    self.BatchDelete = channel.unary_unary(
        '/v1.Nodes/BatchDelete',
        request_serializer=nodes__pb2.NodeBatchDeleteRequest.SerializeToString,
        response_deserializer=nodes__pb2.NodeBatchDeleteResponse.FromString,
        )


class NodesServicer(object):
  """Nodes service
  """

  def Create(self, request, context):
    """Create creates new nodes and returns them.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get reads one node by ID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update patches a node by ID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete removes a node by ID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List is a batched Get call
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchUpdate(self, request, context):
    """BatchUpdate is a batched Update call
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchDelete(self, request, context):
    """BatchDelete is a batched Delete call
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NodesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=nodes__pb2.NodeCreateRequest.FromString,
          response_serializer=nodes__pb2.NodeCreateResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=nodes__pb2.NodeGetRequest.FromString,
          response_serializer=nodes__pb2.NodeGetResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=nodes__pb2.NodeUpdateRequest.FromString,
          response_serializer=nodes__pb2.NodeUpdateResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=nodes__pb2.NodeDeleteRequest.FromString,
          response_serializer=nodes__pb2.NodeDeleteResponse.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=nodes__pb2.NodeListRequest.FromString,
          response_serializer=nodes__pb2.NodeListResponse.SerializeToString,
      ),
      'BatchUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.BatchUpdate,
          request_deserializer=nodes__pb2.NodeBatchUpdateRequest.FromString,
          response_serializer=nodes__pb2.NodeBatchUpdateResponse.SerializeToString,
      ),
      'BatchDelete': grpc.unary_unary_rpc_method_handler(
          servicer.BatchDelete,
          request_deserializer=nodes__pb2.NodeBatchDeleteRequest.FromString,
          response_serializer=nodes__pb2.NodeBatchDeleteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.Nodes', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))