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
# source: options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='options.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.strongdm.api.v1.plumbing'),
  serialized_pb=_b('\n\roptions.proto\x12\x02v1\x1a google/protobuf/descriptor.proto\"\xde\x02\n\x0c\x46ieldOptions\x12\x0e\n\x04name\x18\xb4\xbev \x01(\t\x12\x16\n\x0csql_nullable\x18\xb5\xbev \x01(\x08\x12\x1d\n\x13\x65xpose_as_porcelain\x18\xb6\xbev \x01(\x08\x12\x12\n\x08iterable\x18\xb7\xbev \x01(\x08\x12\x12\n\x08required\x18\xb8\xbev \x01(\x08\x12\x11\n\x07id_type\x18\xb9\xbev \x01(\t\x12\x12\n\x08sdk_only\x18\xba\xbev \x01(\x08\x12\x12\n\x08\x63omputed\x18\xbb\xbev \x01(\x08\x12\x13\n\tforce_new\x18\xbc\xbev \x01(\x08\x12\x1a\n\x10\x63ustom_converter\x18\xbd\xbev \x01(\t\x12\"\n\x18\x63ustom_go_porcelain_type\x18\xbe\xbev \x01(\t\x12$\n\x1a\x63ustom_java_porcelain_type\x18\xbf\xbev \x01(\t\x12)\n\x1f\x63ustom_terraform_porcelain_type\x18\xc0\xbev \x01(\t\"\x92\x01\n\x0eMessageOptions\x12\x14\n\nmodel_name\x18\xb4\xbev \x01(\t\x12\x13\n\tporcelain\x18\xb5\xbev \x01(\x08\x12\x0f\n\x05\x65rror\x18\xb6\xbev \x01(\x05\x12\x17\n\roptions_field\x18\xb7\xbev \x01(\t\x12+\n\x0eterraform_docs\x18\xb8\xbev \x01(\x0b\x32\x11.v1.TerraformDocs\"T\n\rTerraformDocs\x12\x1f\n\x15resource_example_path\x18\xb4\xbev \x01(\t\x12\"\n\x18\x64\x61ta_source_example_path\x18\xb5\xbev \x01(\t\"=\n\x0cOneofOptions\x12\x14\n\nmodel_name\x18\x84\xbfv \x01(\t\x12\x17\n\rcommon_fields\x18\x85\xbfv \x03(\t\"%\n\x0eServiceOptions\x12\x13\n\tmain_noun\x18\x98\xbfv \x01(\t:H\n\rfield_options\x12\x1d.google.protobuf.FieldOptions\x18\x8e\xbfv \x01(\x0b\x32\x10.v1.FieldOptions:N\n\x0fmessage_options\x12\x1f.google.protobuf.MessageOptions\x18\x8f\xbfv \x01(\x0b\x32\x12.v1.MessageOptions:H\n\roneof_options\x12\x1d.google.protobuf.OneofOptions\x18\x85\xbfv \x01(\x0b\x32\x10.v1.OneofOptions:N\n\x0fservice_options\x12\x1f.google.protobuf.ServiceOptions\x18\x99\xbfv \x01(\x0b\x32\x12.v1.ServiceOptionsB\x1e\n\x1c\x63om.strongdm.api.v1.plumbingb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


FIELD_OPTIONS_FIELD_NUMBER = 1941390
field_options = _descriptor.FieldDescriptor(
  name='field_options', full_name='v1.field_options', index=0,
  number=1941390, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MESSAGE_OPTIONS_FIELD_NUMBER = 1941391
message_options = _descriptor.FieldDescriptor(
  name='message_options', full_name='v1.message_options', index=1,
  number=1941391, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ONEOF_OPTIONS_FIELD_NUMBER = 1941381
oneof_options = _descriptor.FieldDescriptor(
  name='oneof_options', full_name='v1.oneof_options', index=2,
  number=1941381, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
SERVICE_OPTIONS_FIELD_NUMBER = 1941401
service_options = _descriptor.FieldDescriptor(
  name='service_options', full_name='v1.service_options', index=3,
  number=1941401, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_FIELDOPTIONS = _descriptor.Descriptor(
  name='FieldOptions',
  full_name='v1.FieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.FieldOptions.name', index=0,
      number=1941300, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sql_nullable', full_name='v1.FieldOptions.sql_nullable', index=1,
      number=1941301, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expose_as_porcelain', full_name='v1.FieldOptions.expose_as_porcelain', index=2,
      number=1941302, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iterable', full_name='v1.FieldOptions.iterable', index=3,
      number=1941303, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required', full_name='v1.FieldOptions.required', index=4,
      number=1941304, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_type', full_name='v1.FieldOptions.id_type', index=5,
      number=1941305, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sdk_only', full_name='v1.FieldOptions.sdk_only', index=6,
      number=1941306, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='computed', full_name='v1.FieldOptions.computed', index=7,
      number=1941307, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force_new', full_name='v1.FieldOptions.force_new', index=8,
      number=1941308, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_converter', full_name='v1.FieldOptions.custom_converter', index=9,
      number=1941309, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_go_porcelain_type', full_name='v1.FieldOptions.custom_go_porcelain_type', index=10,
      number=1941310, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_java_porcelain_type', full_name='v1.FieldOptions.custom_java_porcelain_type', index=11,
      number=1941311, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_terraform_porcelain_type', full_name='v1.FieldOptions.custom_terraform_porcelain_type', index=12,
      number=1941312, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=56,
  serialized_end=406,
)


_MESSAGEOPTIONS = _descriptor.Descriptor(
  name='MessageOptions',
  full_name='v1.MessageOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_name', full_name='v1.MessageOptions.model_name', index=0,
      number=1941300, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='porcelain', full_name='v1.MessageOptions.porcelain', index=1,
      number=1941301, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='v1.MessageOptions.error', index=2,
      number=1941302, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options_field', full_name='v1.MessageOptions.options_field', index=3,
      number=1941303, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terraform_docs', full_name='v1.MessageOptions.terraform_docs', index=4,
      number=1941304, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=555,
)


_TERRAFORMDOCS = _descriptor.Descriptor(
  name='TerraformDocs',
  full_name='v1.TerraformDocs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_example_path', full_name='v1.TerraformDocs.resource_example_path', index=0,
      number=1941300, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_source_example_path', full_name='v1.TerraformDocs.data_source_example_path', index=1,
      number=1941301, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=557,
  serialized_end=641,
)


_ONEOFOPTIONS = _descriptor.Descriptor(
  name='OneofOptions',
  full_name='v1.OneofOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_name', full_name='v1.OneofOptions.model_name', index=0,
      number=1941380, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='common_fields', full_name='v1.OneofOptions.common_fields', index=1,
      number=1941381, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=643,
  serialized_end=704,
)


_SERVICEOPTIONS = _descriptor.Descriptor(
  name='ServiceOptions',
  full_name='v1.ServiceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='main_noun', full_name='v1.ServiceOptions.main_noun', index=0,
      number=1941400, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=706,
  serialized_end=743,
)

_MESSAGEOPTIONS.fields_by_name['terraform_docs'].message_type = _TERRAFORMDOCS
DESCRIPTOR.message_types_by_name['FieldOptions'] = _FIELDOPTIONS
DESCRIPTOR.message_types_by_name['MessageOptions'] = _MESSAGEOPTIONS
DESCRIPTOR.message_types_by_name['TerraformDocs'] = _TERRAFORMDOCS
DESCRIPTOR.message_types_by_name['OneofOptions'] = _ONEOFOPTIONS
DESCRIPTOR.message_types_by_name['ServiceOptions'] = _SERVICEOPTIONS
DESCRIPTOR.extensions_by_name['field_options'] = field_options
DESCRIPTOR.extensions_by_name['message_options'] = message_options
DESCRIPTOR.extensions_by_name['oneof_options'] = oneof_options
DESCRIPTOR.extensions_by_name['service_options'] = service_options
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FieldOptions = _reflection.GeneratedProtocolMessageType('FieldOptions', (_message.Message,), {
  'DESCRIPTOR' : _FIELDOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.FieldOptions)
  })
_sym_db.RegisterMessage(FieldOptions)

MessageOptions = _reflection.GeneratedProtocolMessageType('MessageOptions', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.MessageOptions)
  })
_sym_db.RegisterMessage(MessageOptions)

TerraformDocs = _reflection.GeneratedProtocolMessageType('TerraformDocs', (_message.Message,), {
  'DESCRIPTOR' : _TERRAFORMDOCS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.TerraformDocs)
  })
_sym_db.RegisterMessage(TerraformDocs)

OneofOptions = _reflection.GeneratedProtocolMessageType('OneofOptions', (_message.Message,), {
  'DESCRIPTOR' : _ONEOFOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.OneofOptions)
  })
_sym_db.RegisterMessage(OneofOptions)

ServiceOptions = _reflection.GeneratedProtocolMessageType('ServiceOptions', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.ServiceOptions)
  })
_sym_db.RegisterMessage(ServiceOptions)

field_options.message_type = _FIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_options)
message_options.message_type = _MESSAGEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_options)
oneof_options.message_type = _ONEOFOPTIONS
google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(oneof_options)
service_options.message_type = _SERVICEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_options)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
