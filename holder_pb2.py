# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: holder.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='holder.proto',
  package='holder',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0cholder.proto\x12\x06holder\"z\n\nCardHolder\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03job\x18\x02 \x02(\t\x12\x14\n\x0cphone_number\x18\x03 \x02(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x02(\t\x12\x13\n\x0b\x63\x61rd_number\x18\x05 \x02(\t\x12\x15\n\rcard_provider\x18\x06 \x02(\t')
)




_CARDHOLDER = _descriptor.Descriptor(
  name='CardHolder',
  full_name='holder.CardHolder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='holder.CardHolder.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job', full_name='holder.CardHolder.job', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='holder.CardHolder.phone_number', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='holder.CardHolder.address', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_number', full_name='holder.CardHolder.card_number', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_provider', full_name='holder.CardHolder.card_provider', index=5,
      number=6, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['CardHolder'] = _CARDHOLDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CardHolder = _reflection.GeneratedProtocolMessageType('CardHolder', (_message.Message,), dict(
  DESCRIPTOR = _CARDHOLDER,
  __module__ = 'holder_pb2'
  # @@protoc_insertion_point(class_scope:holder.CardHolder)
  ))
_sym_db.RegisterMessage(CardHolder)


# @@protoc_insertion_point(module_scope)
