# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/predict.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/predict.proto\x12\x07predict\"\x07\n\x05\x45mpty\"W\n\x07Predict\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\x03\x12\x15\n\rcurrent_price\x18\x03 \x01(\x02\x12\x17\n\x0fpredicted_price\x18\x04 \x01(\x02\"4\n\x0fPredictResponse\x12!\n\x07predict\x18\x01 \x03(\x0b\x32\x10.predict.Predict\"!\n\x0cTimeStampReq\x12\x11\n\ttimeStamp\x18\x01 \x01(\x03\x32\x90\x02\n\x0ePredictService\x12\x35\n\x07predict\x12\x0e.predict.Empty\x1a\x18.predict.PredictResponse\"\x00\x12\x34\n\tdeleteall\x12\x15.predict.TimeStampReq\x1a\x0e.predict.Empty\"\x00\x12\x31\n\x06update\x12\x15.predict.TimeStampReq\x1a\x0e.predict.Empty\"\x00\x12(\n\x04plot\x12\x0e.predict.Empty\x1a\x0e.predict.Empty\"\x00\x12\x34\n\x07getData\x12\x15.predict.TimeStampReq\x1a\x10.predict.Predict\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.predict_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=32
  _globals['_EMPTY']._serialized_end=39
  _globals['_PREDICT']._serialized_start=41
  _globals['_PREDICT']._serialized_end=128
  _globals['_PREDICTRESPONSE']._serialized_start=130
  _globals['_PREDICTRESPONSE']._serialized_end=182
  _globals['_TIMESTAMPREQ']._serialized_start=184
  _globals['_TIMESTAMPREQ']._serialized_end=217
  _globals['_PREDICTSERVICE']._serialized_start=220
  _globals['_PREDICTSERVICE']._serialized_end=492
# @@protoc_insertion_point(module_scope)
