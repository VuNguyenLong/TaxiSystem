# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0emessages.proto\"9\n\x0cRestResponse\x12\x11\n\thashed_id\x18\x01 \x01(\t\x12\x16\n\x0e\x62roker_address\x18\x04 \x03(\t\"=\n\x06\x44river\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04long\x18\x02 \x01(\x02\x12\x0b\n\x03lat\x18\x03 \x01(\x02\x12\x0c\n\x04hash\x18\x04 \x03(\x05\"\"\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04hash\x18\x04 \x03(\x05\"\x84\x01\n\x07Message\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.Message.Type\x12\x19\n\x06\x63lient\x18\x02 \x01(\x0b\x32\x07.ClientH\x00\x12\x19\n\x06\x64river\x18\x03 \x01(\x0b\x32\x07.DriverH\x00\"\x1e\n\x04Type\x12\n\n\x06SELECT\x10\x00\x12\n\n\x06UPDATE\x10\x01\x42\x06\n\x04\x64\x61ta\"G\n\x07\x43ommand\x12\x19\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x07.ClientH\x00\x12\x19\n\x06\x64river\x18\x02 \x01(\x0b\x32\x07.DriverH\x00\x42\x06\n\x04\x64\x61ta\"b\n\x07Request\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.Request.Type\x12\x1a\n\x08\x63ommands\x18\x02 \x03(\x0b\x32\x08.Command\"\x1e\n\x04Type\x12\n\n\x06SELECT\x10\x00\x12\n\n\x06UPDATE\x10\x01\"%\n\tLocations\x12\x18\n\x07\x64rivers\x18\x01 \x03(\x0b\x32\x07.Driver\";\n\x08Response\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x1c\n\x08response\x18\x02 \x01(\x0b\x32\n.Locationsb\x06proto3'
)



_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Message.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SELECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=271,
  serialized_end=301,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)

_REQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Request.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SELECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=271,
  serialized_end=301,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_TYPE)


_RESTRESPONSE = _descriptor.Descriptor(
  name='RestResponse',
  full_name='RestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashed_id', full_name='RestResponse.hashed_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='broker_address', full_name='RestResponse.broker_address', index=1,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=18,
  serialized_end=75,
)


_DRIVER = _descriptor.Descriptor(
  name='Driver',
  full_name='Driver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Driver.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='long', full_name='Driver.long', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lat', full_name='Driver.lat', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Driver.hash', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=77,
  serialized_end=138,
)


_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Client.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Client.hash', index=1,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=140,
  serialized_end=174,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client', full_name='Message.client', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='driver', full_name='Message.driver', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='Message.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=177,
  serialized_end=309,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='Command.client', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='driver', full_name='Command.driver', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='data', full_name='Command.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=311,
  serialized_end=382,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Request.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='Request.commands', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=482,
)


_LOCATIONS = _descriptor.Descriptor(
  name='Locations',
  full_name='Locations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drivers', full_name='Locations.drivers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=484,
  serialized_end=521,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='Response.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='Response.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=523,
  serialized_end=582,
)

_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE.fields_by_name['client'].message_type = _CLIENT
_MESSAGE.fields_by_name['driver'].message_type = _DRIVER
_MESSAGE_TYPE.containing_type = _MESSAGE
_MESSAGE.oneofs_by_name['data'].fields.append(
  _MESSAGE.fields_by_name['client'])
_MESSAGE.fields_by_name['client'].containing_oneof = _MESSAGE.oneofs_by_name['data']
_MESSAGE.oneofs_by_name['data'].fields.append(
  _MESSAGE.fields_by_name['driver'])
_MESSAGE.fields_by_name['driver'].containing_oneof = _MESSAGE.oneofs_by_name['data']
_COMMAND.fields_by_name['client'].message_type = _CLIENT
_COMMAND.fields_by_name['driver'].message_type = _DRIVER
_COMMAND.oneofs_by_name['data'].fields.append(
  _COMMAND.fields_by_name['client'])
_COMMAND.fields_by_name['client'].containing_oneof = _COMMAND.oneofs_by_name['data']
_COMMAND.oneofs_by_name['data'].fields.append(
  _COMMAND.fields_by_name['driver'])
_COMMAND.fields_by_name['driver'].containing_oneof = _COMMAND.oneofs_by_name['data']
_REQUEST.fields_by_name['type'].enum_type = _REQUEST_TYPE
_REQUEST.fields_by_name['commands'].message_type = _COMMAND
_REQUEST_TYPE.containing_type = _REQUEST
_LOCATIONS.fields_by_name['drivers'].message_type = _DRIVER
_RESPONSE.fields_by_name['response'].message_type = _LOCATIONS
DESCRIPTOR.message_types_by_name['RestResponse'] = _RESTRESPONSE
DESCRIPTOR.message_types_by_name['Driver'] = _DRIVER
DESCRIPTOR.message_types_by_name['Client'] = _CLIENT
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Locations'] = _LOCATIONS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RestResponse = _reflection.GeneratedProtocolMessageType('RestResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESTRESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:RestResponse)
  })
_sym_db.RegisterMessage(RestResponse)

Driver = _reflection.GeneratedProtocolMessageType('Driver', (_message.Message,), {
  'DESCRIPTOR' : _DRIVER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Driver)
  })
_sym_db.RegisterMessage(Driver)

Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), {
  'DESCRIPTOR' : _CLIENT,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Client)
  })
_sym_db.RegisterMessage(Client)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Command)
  })
_sym_db.RegisterMessage(Command)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Locations = _reflection.GeneratedProtocolMessageType('Locations', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Locations)
  })
_sym_db.RegisterMessage(Locations)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
