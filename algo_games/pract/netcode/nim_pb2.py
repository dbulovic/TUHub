# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nim.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nim.proto',
  package='nim',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tnim.proto\x12\x03nim\"D\n\rGameParameter\x12\x19\n\x11number_of_columns\x18\x01 \x01(\r\x12\x18\n\x10number_of_stones\x18\x02 \x01(\r\"9\n\x08GameTurn\x12\x15\n\rtarget_column\x18\x01 \x01(\r\x12\x16\n\x0enumber_to_take\x18\x02 \x01(\r\"\x1c\n\tGameState\x12\x0f\n\x07\x63olumns\x18\x01 \x01(\tb\x06proto3'
)




_GAMEPARAMETER = _descriptor.Descriptor(
  name='GameParameter',
  full_name='nim.GameParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_of_columns', full_name='nim.GameParameter.number_of_columns', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_of_stones', full_name='nim.GameParameter.number_of_stones', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=86,
)


_GAMETURN = _descriptor.Descriptor(
  name='GameTurn',
  full_name='nim.GameTurn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_column', full_name='nim.GameTurn.target_column', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_to_take', full_name='nim.GameTurn.number_to_take', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=88,
  serialized_end=145,
)


_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='nim.GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='nim.GameState.columns', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=147,
  serialized_end=175,
)

DESCRIPTOR.message_types_by_name['GameParameter'] = _GAMEPARAMETER
DESCRIPTOR.message_types_by_name['GameTurn'] = _GAMETURN
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameParameter = _reflection.GeneratedProtocolMessageType('GameParameter', (_message.Message,), {
  'DESCRIPTOR' : _GAMEPARAMETER,
  '__module__' : 'nim_pb2'
  # @@protoc_insertion_point(class_scope:nim.GameParameter)
  })
_sym_db.RegisterMessage(GameParameter)

GameTurn = _reflection.GeneratedProtocolMessageType('GameTurn', (_message.Message,), {
  'DESCRIPTOR' : _GAMETURN,
  '__module__' : 'nim_pb2'
  # @@protoc_insertion_point(class_scope:nim.GameTurn)
  })
_sym_db.RegisterMessage(GameTurn)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
  'DESCRIPTOR' : _GAMESTATE,
  '__module__' : 'nim_pb2'
  # @@protoc_insertion_point(class_scope:nim.GameState)
  })
_sym_db.RegisterMessage(GameState)


# @@protoc_insertion_point(module_scope)
