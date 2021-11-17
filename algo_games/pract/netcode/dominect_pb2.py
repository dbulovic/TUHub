# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dominect.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dominect.proto',
  package='dom',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64ominect.proto\x12\x03\x64om\":\n\rGameParameter\x12\x13\n\x0b\x62oard_width\x18\x01 \x01(\r\x12\x14\n\x0c\x62oard_height\x18\x02 \x01(\r\":\n\x08GameTurn\x12\n\n\x02x1\x18\x01 \x01(\r\x12\n\n\x02y1\x18\x02 \x01(\r\x12\n\n\x02x2\x18\x03 \x01(\r\x12\n\n\x02y2\x18\x04 \x01(\r\"J\n\tGameState\x12\x13\n\x0b\x62oard_width\x18\x01 \x01(\r\x12\x14\n\x0c\x62oard_height\x18\x02 \x01(\r\x12\x12\n\nboard_data\x18\x03 \x01(\x0c\x62\x06proto3'
)




_GAMEPARAMETER = _descriptor.Descriptor(
  name='GameParameter',
  full_name='dom.GameParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='board_width', full_name='dom.GameParameter.board_width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='board_height', full_name='dom.GameParameter.board_height', index=1,
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
  serialized_start=23,
  serialized_end=81,
)


_GAMETURN = _descriptor.Descriptor(
  name='GameTurn',
  full_name='dom.GameTurn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x1', full_name='dom.GameTurn.x1', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y1', full_name='dom.GameTurn.y1', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x2', full_name='dom.GameTurn.x2', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y2', full_name='dom.GameTurn.y2', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=83,
  serialized_end=141,
)


_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='dom.GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='board_width', full_name='dom.GameState.board_width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='board_height', full_name='dom.GameState.board_height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='board_data', full_name='dom.GameState.board_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=143,
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['GameParameter'] = _GAMEPARAMETER
DESCRIPTOR.message_types_by_name['GameTurn'] = _GAMETURN
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameParameter = _reflection.GeneratedProtocolMessageType('GameParameter', (_message.Message,), {
  'DESCRIPTOR' : _GAMEPARAMETER,
  '__module__' : 'dominect_pb2'
  # @@protoc_insertion_point(class_scope:dom.GameParameter)
  })
_sym_db.RegisterMessage(GameParameter)

GameTurn = _reflection.GeneratedProtocolMessageType('GameTurn', (_message.Message,), {
  'DESCRIPTOR' : _GAMETURN,
  '__module__' : 'dominect_pb2'
  # @@protoc_insertion_point(class_scope:dom.GameTurn)
  })
_sym_db.RegisterMessage(GameTurn)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
  'DESCRIPTOR' : _GAMESTATE,
  '__module__' : 'dominect_pb2'
  # @@protoc_insertion_point(class_scope:dom.GameState)
  })
_sym_db.RegisterMessage(GameState)


# @@protoc_insertion_point(module_scope)
