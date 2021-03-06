# Copyright 2020 StrongDM Inc
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='accounts.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\020AccountsPlumbing',
  serialized_pb=b'\n\x0e\x61\x63\x63ounts.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\roptions.proto\x1a\nspec.proto\"i\n\x14\x41\x63\x63ountCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd5\x01\n\x15\x41\x63\x63ountCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x19\n\x05token\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x04 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"Q\n\x11\x41\x63\x63ountGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb4\x01\n\x12\x41\x63\x63ountGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"u\n\x14\x41\x63\x63ountUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12(\n\x07\x61\x63\x63ount\x18\x03 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xba\x01\n\x15\x41\x63\x63ountUpdateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"W\n\x14\x41\x63\x63ountDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x90\x01\n\x15\x41\x63\x63ountDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"W\n\x12\x41\x63\x63ountListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x9f\x01\n\x13\x41\x63\x63ountListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12)\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd4\x01\n\x07\x41\x63\x63ount\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\x08.v1.UserH\x00\x12\x1e\n\x07service\x18\x02 \x01(\x0b\x32\x0b.v1.ServiceH\x00:a\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07R\xc2\xf3\xb3\x07M\xa2\xf3\xb3\x07 tf_examples/account_resource.txt\xaa\xf3\xb3\x07#tf_examples/account_data_source.txtB,\n\x07\x61\x63\x63ount\x12!\xaa\xf8\xb3\x07\t\xa2\xf8\xb3\x07\x04User\xaa\xf8\xb3\x07\x0e\xaa\xf8\xb3\x07\tsuspended\"\xf5\x01\n\x04User\x12&\n\x02id\x18\x01 \x01(\tB\x1a\xf2\xf8\xb3\x07\x15\xa2\xf3\xb3\x07\x02ID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x04User\x12(\n\x05\x65mail\x18\x02 \x01(\tB\x19\xf2\xf8\xb3\x07\x14\xa2\xf3\xb3\x07\x05\x45mail\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\x31\n\nfirst_name\x18\x03 \x01(\tB\x1d\xf2\xf8\xb3\x07\x18\xa2\xf3\xb3\x07\tFirstName\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12/\n\tlast_name\x18\x04 \x01(\tB\x1c\xf2\xf8\xb3\x07\x17\xa2\xf3\xb3\x07\x08LastName\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\"\n\tsuspended\x18\x05 \x01(\x08\x42\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf3\xb3\x07\x01:\x13\xfa\xf8\xb3\x07\x0e\xa2\xf3\xb3\x07\x04User\xa8\xf3\xb3\x07\x01\"\x96\x01\n\x07Service\x12&\n\x02id\x18\x01 \x01(\tB\x1a\xf2\xf8\xb3\x07\x15\xa2\xf3\xb3\x07\x02ID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x04User\x12*\n\x04name\x18\x02 \x01(\tB\x1c\xf2\xf8\xb3\x07\x17\xa2\xf3\xb3\x07\x08LastName\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\"\n\tsuspended\x18\x03 \x01(\x08\x42\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf3\xb3\x07\x01:\x13\xfa\xf8\xb3\x07\x0e\xa2\xf3\xb3\x07\x04User\xa8\xf3\xb3\x07\x01\x32\xab\x04\n\x08\x41\x63\x63ounts\x12\xb4\x01\n\x06\x43reate\x12\x18.v1.AccountCreateRequest\x1a\x19.v1.AccountCreateResponse\"u\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/accounts:\x01*\x92\x41[\"Y\n\x1bLearn how to make a Account\x12:https://www.strongdm.com/docs/api/services/Accounts#Create\x12O\n\x03Get\x12\x15.v1.AccountGetRequest\x1a\x16.v1.AccountGetResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/accounts/{id}\x12[\n\x06Update\x12\x18.v1.AccountUpdateRequest\x1a\x19.v1.AccountUpdateResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x1a\x11/v1/accounts/{id}:\x01*\x12X\n\x06\x44\x65lete\x12\x18.v1.AccountDeleteRequest\x1a\x19.v1.AccountDeleteResponse\"\x19\x82\xd3\xe4\x93\x02\x13*\x11/v1/accounts/{id}\x12M\n\x04List\x12\x16.v1.AccountListRequest\x1a\x17.v1.AccountListResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/accounts\x1a\x11\xca\xf9\xb3\x07\x0c\xc2\xf9\xb3\x07\x07\x41\x63\x63ountB0\n\x1c\x63om.strongdm.api.v1.plumbingB\x10\x41\x63\x63ountsPlumbingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_ACCOUNTCREATEREQUEST = _descriptor.Descriptor(
  name='AccountCreateRequest',
  full_name='v1.AccountCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='v1.AccountCreateRequest.account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=230,
)


_ACCOUNTCREATERESPONSE = _descriptor.Descriptor(
  name='AccountCreateResponse',
  full_name='v1.AccountCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='v1.AccountCreateResponse.account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='v1.AccountCreateResponse.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountCreateResponse.rate_limit', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=446,
)


_ACCOUNTGETREQUEST = _descriptor.Descriptor(
  name='AccountGetRequest',
  full_name='v1.AccountGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountGetRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=529,
)


_ACCOUNTGETRESPONSE = _descriptor.Descriptor(
  name='AccountGetResponse',
  full_name='v1.AccountGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='v1.AccountGetResponse.account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountGetResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=712,
)


_ACCOUNTUPDATEREQUEST = _descriptor.Descriptor(
  name='AccountUpdateRequest',
  full_name='v1.AccountUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountUpdateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountUpdateRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='v1.AccountUpdateRequest.account', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=714,
  serialized_end=831,
)


_ACCOUNTUPDATERESPONSE = _descriptor.Descriptor(
  name='AccountUpdateResponse',
  full_name='v1.AccountUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountUpdateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='v1.AccountUpdateResponse.account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountUpdateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=1020,
)


_ACCOUNTDELETEREQUEST = _descriptor.Descriptor(
  name='AccountDeleteRequest',
  full_name='v1.AccountDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountDeleteRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1022,
  serialized_end=1109,
)


_ACCOUNTDELETERESPONSE = _descriptor.Descriptor(
  name='AccountDeleteResponse',
  full_name='v1.AccountDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountDeleteResponse.rate_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1112,
  serialized_end=1256,
)


_ACCOUNTLISTREQUEST = _descriptor.Descriptor(
  name='AccountListRequest',
  full_name='v1.AccountListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.AccountListRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1258,
  serialized_end=1345,
)


_ACCOUNTLISTRESPONSE = _descriptor.Descriptor(
  name='AccountListResponse',
  full_name='v1.AccountListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='v1.AccountListResponse.accounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\270\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountListResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1348,
  serialized_end=1507,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='v1.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='v1.Account.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='v1.Account.service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007R\302\363\263\007M\242\363\263\007 tf_examples/account_resource.txt\252\363\263\007#tf_examples/account_data_source.txt',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='account', full_name='v1.Account.account',
      index=0, containing_type=None, fields=[], serialized_options=b'\252\370\263\007\t\242\370\263\007\004User\252\370\263\007\016\252\370\263\007\tsuspended'),
  ],
  serialized_start=1510,
  serialized_end=1722,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='v1.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\025\242\363\263\007\002ID\260\363\263\007\001\312\363\263\007\004User', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='v1.User.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\024\242\363\263\007\005Email\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='v1.User.first_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\030\242\363\263\007\tFirstName\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='v1.User.last_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\027\242\363\263\007\010LastName\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspended', full_name='v1.User.suspended', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\320\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\016\242\363\263\007\004User\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1725,
  serialized_end=1970,
)


_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='v1.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.Service.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\025\242\363\263\007\002ID\260\363\263\007\001\312\363\263\007\004User', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.Service.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\027\242\363\263\007\010LastName\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspended', full_name='v1.Service.suspended', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\320\363\263\007\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\016\242\363\263\007\004User\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1973,
  serialized_end=2123,
)

_ACCOUNTCREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_ACCOUNTCREATEREQUEST.fields_by_name['account'].message_type = _ACCOUNT
_ACCOUNTCREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_ACCOUNTCREATERESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_ACCOUNTCREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_ACCOUNTGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_ACCOUNTGETRESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_ACCOUNTGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTUPDATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._UPDATEREQUESTMETADATA
_ACCOUNTUPDATEREQUEST.fields_by_name['account'].message_type = _ACCOUNT
_ACCOUNTUPDATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._UPDATERESPONSEMETADATA
_ACCOUNTUPDATERESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_ACCOUNTUPDATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_ACCOUNTDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_ACCOUNTDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTLISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_ACCOUNTLISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_ACCOUNTLISTRESPONSE.fields_by_name['accounts'].message_type = _ACCOUNT
_ACCOUNTLISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNT.fields_by_name['user'].message_type = _USER
_ACCOUNT.fields_by_name['service'].message_type = _SERVICE
_ACCOUNT.oneofs_by_name['account'].fields.append(
  _ACCOUNT.fields_by_name['user'])
_ACCOUNT.fields_by_name['user'].containing_oneof = _ACCOUNT.oneofs_by_name['account']
_ACCOUNT.oneofs_by_name['account'].fields.append(
  _ACCOUNT.fields_by_name['service'])
_ACCOUNT.fields_by_name['service'].containing_oneof = _ACCOUNT.oneofs_by_name['account']
DESCRIPTOR.message_types_by_name['AccountCreateRequest'] = _ACCOUNTCREATEREQUEST
DESCRIPTOR.message_types_by_name['AccountCreateResponse'] = _ACCOUNTCREATERESPONSE
DESCRIPTOR.message_types_by_name['AccountGetRequest'] = _ACCOUNTGETREQUEST
DESCRIPTOR.message_types_by_name['AccountGetResponse'] = _ACCOUNTGETRESPONSE
DESCRIPTOR.message_types_by_name['AccountUpdateRequest'] = _ACCOUNTUPDATEREQUEST
DESCRIPTOR.message_types_by_name['AccountUpdateResponse'] = _ACCOUNTUPDATERESPONSE
DESCRIPTOR.message_types_by_name['AccountDeleteRequest'] = _ACCOUNTDELETEREQUEST
DESCRIPTOR.message_types_by_name['AccountDeleteResponse'] = _ACCOUNTDELETERESPONSE
DESCRIPTOR.message_types_by_name['AccountListRequest'] = _ACCOUNTLISTREQUEST
DESCRIPTOR.message_types_by_name['AccountListResponse'] = _ACCOUNTLISTRESPONSE
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountCreateRequest = _reflection.GeneratedProtocolMessageType('AccountCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTCREATEREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountCreateRequest)
  })
_sym_db.RegisterMessage(AccountCreateRequest)

AccountCreateResponse = _reflection.GeneratedProtocolMessageType('AccountCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTCREATERESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountCreateResponse)
  })
_sym_db.RegisterMessage(AccountCreateResponse)

AccountGetRequest = _reflection.GeneratedProtocolMessageType('AccountGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGETREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGetRequest)
  })
_sym_db.RegisterMessage(AccountGetRequest)

AccountGetResponse = _reflection.GeneratedProtocolMessageType('AccountGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGETRESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGetResponse)
  })
_sym_db.RegisterMessage(AccountGetResponse)

AccountUpdateRequest = _reflection.GeneratedProtocolMessageType('AccountUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTUPDATEREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountUpdateRequest)
  })
_sym_db.RegisterMessage(AccountUpdateRequest)

AccountUpdateResponse = _reflection.GeneratedProtocolMessageType('AccountUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTUPDATERESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountUpdateResponse)
  })
_sym_db.RegisterMessage(AccountUpdateResponse)

AccountDeleteRequest = _reflection.GeneratedProtocolMessageType('AccountDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDELETEREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountDeleteRequest)
  })
_sym_db.RegisterMessage(AccountDeleteRequest)

AccountDeleteResponse = _reflection.GeneratedProtocolMessageType('AccountDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDELETERESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountDeleteResponse)
  })
_sym_db.RegisterMessage(AccountDeleteResponse)

AccountListRequest = _reflection.GeneratedProtocolMessageType('AccountListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTLISTREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountListRequest)
  })
_sym_db.RegisterMessage(AccountListRequest)

AccountListResponse = _reflection.GeneratedProtocolMessageType('AccountListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTLISTRESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountListResponse)
  })
_sym_db.RegisterMessage(AccountListResponse)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.Account)
  })
_sym_db.RegisterMessage(Account)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.User)
  })
_sym_db.RegisterMessage(User)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.Service)
  })
_sym_db.RegisterMessage(Service)


DESCRIPTOR._options = None
_ACCOUNTCREATEREQUEST.fields_by_name['account']._options = None
_ACCOUNTCREATERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTCREATERESPONSE.fields_by_name['account']._options = None
_ACCOUNTCREATERESPONSE.fields_by_name['token']._options = None
_ACCOUNTCREATERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTCREATERESPONSE._options = None
_ACCOUNTGETREQUEST.fields_by_name['id']._options = None
_ACCOUNTGETRESPONSE.fields_by_name['meta']._options = None
_ACCOUNTGETRESPONSE.fields_by_name['account']._options = None
_ACCOUNTGETRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTGETRESPONSE._options = None
_ACCOUNTUPDATEREQUEST.fields_by_name['account']._options = None
_ACCOUNTUPDATERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTUPDATERESPONSE.fields_by_name['account']._options = None
_ACCOUNTUPDATERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTUPDATERESPONSE._options = None
_ACCOUNTDELETEREQUEST.fields_by_name['id']._options = None
_ACCOUNTDELETERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTDELETERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTDELETERESPONSE._options = None
_ACCOUNTLISTREQUEST.fields_by_name['filter']._options = None
_ACCOUNTLISTRESPONSE.fields_by_name['accounts']._options = None
_ACCOUNTLISTRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNT.oneofs_by_name['account']._options = None
_ACCOUNT._options = None
_USER.fields_by_name['id']._options = None
_USER.fields_by_name['email']._options = None
_USER.fields_by_name['first_name']._options = None
_USER.fields_by_name['last_name']._options = None
_USER.fields_by_name['suspended']._options = None
_USER._options = None
_SERVICE.fields_by_name['id']._options = None
_SERVICE.fields_by_name['name']._options = None
_SERVICE.fields_by_name['suspended']._options = None
_SERVICE._options = None

_ACCOUNTS = _descriptor.ServiceDescriptor(
  name='Accounts',
  full_name='v1.Accounts',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312\371\263\007\014\302\371\263\007\007Account',
  serialized_start=2126,
  serialized_end=2681,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.Accounts.Create',
    index=0,
    containing_service=None,
    input_type=_ACCOUNTCREATEREQUEST,
    output_type=_ACCOUNTCREATERESPONSE,
    serialized_options=b'\202\323\344\223\002\021\"\014/v1/accounts:\001*\222A[\"Y\n\033Learn how to make a Account\022:https://www.strongdm.com/docs/api/services/Accounts#Create',
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.Accounts.Get',
    index=1,
    containing_service=None,
    input_type=_ACCOUNTGETREQUEST,
    output_type=_ACCOUNTGETRESPONSE,
    serialized_options=b'\202\323\344\223\002\023\022\021/v1/accounts/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='v1.Accounts.Update',
    index=2,
    containing_service=None,
    input_type=_ACCOUNTUPDATEREQUEST,
    output_type=_ACCOUNTUPDATERESPONSE,
    serialized_options=b'\202\323\344\223\002\026\032\021/v1/accounts/{id}:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.Accounts.Delete',
    index=3,
    containing_service=None,
    input_type=_ACCOUNTDELETEREQUEST,
    output_type=_ACCOUNTDELETERESPONSE,
    serialized_options=b'\202\323\344\223\002\023*\021/v1/accounts/{id}',
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.Accounts.List',
    index=4,
    containing_service=None,
    input_type=_ACCOUNTLISTREQUEST,
    output_type=_ACCOUNTLISTRESPONSE,
    serialized_options=b'\202\323\344\223\002\016\022\014/v1/accounts',
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTS)

DESCRIPTOR.services_by_name['Accounts'] = _ACCOUNTS

# @@protoc_insertion_point(module_scope)
