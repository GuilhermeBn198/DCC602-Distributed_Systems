# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# Importa os módulos necessários

_sym_db = _symbol_database.Default()

# Cria um descritor para o arquivo de protótipo

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x63ommands.proto\x12\x07\x63ommand\"!\n\x0e\x43ommandRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\"!\n\x0f\x43ommandResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2W\n\x0e\x43ommandService\x12\x45\n\x0e\x45xecuteCommand\x12\x17.command.CommandRequest\x1a\x18.command.CommandResponse\"\x00\x62\x06proto3')

# Constrói os descritores de mensagens e enumerações

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())

# Constrói os descritores e mensagens principais

_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'commands_pb2', globals())

if _descriptor._USE_C_DESCRIPTORS == False:
    # Define as opções como nulas e configura as posições de serialização
    DESCRIPTOR._options = None
    _COMMANDREQUEST._serialized_start = 27
    _COMMANDREQUEST._serialized_end = 60
    _COMMANDRESPONSE._serialized_start = 62
    _COMMANDRESPONSE._serialized_end = 95
    _COMMANDSERVICE._serialized_start = 97
    _COMMANDSERVICE._serialized_end = 184