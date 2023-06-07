
all: proto/ved_pb2.py

proto/ved_pb2.py:proto/ved.proto
	protoc -I. --python_out=pyi_out:. proto/ved.proto
