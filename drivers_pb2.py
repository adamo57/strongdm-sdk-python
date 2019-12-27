# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drivers.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from . import options_pb2 as options__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='drivers.proto',
    package='v1',
    syntax='proto3',
    serialized_options=_b(
        '\n\034com.strongdm.api.v1.plumbingB\017DriversPlumbing'),
    serialized_pb=_b(
        '\n\rdrivers.proto\x12\x02v1\x1a\roptions.proto\"X\n\x06\x44river\x12\x1a\n\x05mysql\x18\x01 \x01(\x0b\x32\t.v1.MysqlH\x00\x12\x1c\n\x06\x61thena\x18\x02 \x01(\x0b\x32\n.v1.AthenaH\x00:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x42\x08\n\x06\x64river\"\x87\x01\n\x05Mysql\x12\x1c\n\x08username\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1c\n\x08password\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1c\n\x08\x64\x61tabase\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x18\n\x04port\x18\x04 \x01(\x05\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x91\x01\n\x06\x41thena\x12\x1e\n\naccess_key\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12#\n\x0fsecretAccessKey\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1a\n\x06region\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1a\n\x06output\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x42/\n\x1c\x63om.strongdm.api.v1.plumbingB\x0f\x44riversPlumbingb\x06proto3'
    ),
    dependencies=[
        options__pb2.DESCRIPTOR,
    ])

_DRIVER = _descriptor.Descriptor(
    name='Driver',
    full_name='v1.Driver',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='mysql',
                                    full_name='v1.Driver.mysql',
                                    index=0,
                                    number=1,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='athena',
                                    full_name='v1.Driver.athena',
                                    index=1,
                                    number=2,
                                    type=11,
                                    cpp_type=10,
                                    label=1,
                                    has_default_value=False,
                                    default_value=None,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(name='driver',
                                    full_name='v1.Driver.driver',
                                    index=0,
                                    containing_type=None,
                                    fields=[]),
    ],
    serialized_start=36,
    serialized_end=124,
)

_MYSQL = _descriptor.Descriptor(
    name='Mysql',
    full_name='v1.Mysql',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='username',
            full_name='v1.Mysql.username',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='password',
            full_name='v1.Mysql.password',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='database',
            full_name='v1.Mysql.database',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='port',
            full_name='v1.Mysql.port',
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=127,
    serialized_end=262,
)

_ATHENA = _descriptor.Descriptor(
    name='Athena',
    full_name='v1.Athena',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='access_key',
            full_name='v1.Athena.access_key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='secretAccessKey',
            full_name='v1.Athena.secretAccessKey',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='region',
            full_name='v1.Athena.region',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='output',
            full_name='v1.Athena.output',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'),
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=265,
    serialized_end=410,
)

_DRIVER.fields_by_name['mysql'].message_type = _MYSQL
_DRIVER.fields_by_name['athena'].message_type = _ATHENA
_DRIVER.oneofs_by_name['driver'].fields.append(_DRIVER.fields_by_name['mysql'])
_DRIVER.fields_by_name['mysql'].containing_oneof = _DRIVER.oneofs_by_name[
    'driver']
_DRIVER.oneofs_by_name['driver'].fields.append(
    _DRIVER.fields_by_name['athena'])
_DRIVER.fields_by_name['athena'].containing_oneof = _DRIVER.oneofs_by_name[
    'driver']
DESCRIPTOR.message_types_by_name['Driver'] = _DRIVER
DESCRIPTOR.message_types_by_name['Mysql'] = _MYSQL
DESCRIPTOR.message_types_by_name['Athena'] = _ATHENA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Driver = _reflection.GeneratedProtocolMessageType(
    'Driver',
    (_message.Message, ),
    {
        'DESCRIPTOR': _DRIVER,
        '__module__': 'drivers_pb2'
        # @@protoc_insertion_point(class_scope:v1.Driver)
    })
_sym_db.RegisterMessage(Driver)

Mysql = _reflection.GeneratedProtocolMessageType(
    'Mysql',
    (_message.Message, ),
    {
        'DESCRIPTOR': _MYSQL,
        '__module__': 'drivers_pb2'
        # @@protoc_insertion_point(class_scope:v1.Mysql)
    })
_sym_db.RegisterMessage(Mysql)

Athena = _reflection.GeneratedProtocolMessageType(
    'Athena',
    (_message.Message, ),
    {
        'DESCRIPTOR': _ATHENA,
        '__module__': 'drivers_pb2'
        # @@protoc_insertion_point(class_scope:v1.Athena)
    })
_sym_db.RegisterMessage(Athena)

DESCRIPTOR._options = None
_DRIVER._options = None
_MYSQL.fields_by_name['username']._options = None
_MYSQL.fields_by_name['password']._options = None
_MYSQL.fields_by_name['database']._options = None
_MYSQL.fields_by_name['port']._options = None
_MYSQL._options = None
_ATHENA.fields_by_name['access_key']._options = None
_ATHENA.fields_by_name['secretAccessKey']._options = None
_ATHENA.fields_by_name['region']._options = None
_ATHENA.fields_by_name['output']._options = None
_ATHENA._options = None
# @@protoc_insertion_point(module_scope)
