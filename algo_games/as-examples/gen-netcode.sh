#!/bin/bash
##################################
# Author: Martin Wistauder
# Date: 12.12.2019
# Version: 1.0
##################################
set -e

usage='Usage: ./gen-netcode.sh {protobuf source dir} {output dir}
Example usage: ./gen-netcode.sh $PWD/protobuf $PWD/netcode
Note: Use absolute paths'

# check params
[ -z $1 ] && echo -e "Error: First parameter missing.\n$usage" && exit 1 || protodir="$1"
[ -z $2 ] && echo -e "Error: Second parameter missing.\n$usage" && exit 1 || gendir="$2"
libname="libnetcode.a"
cxx="g++"
idFileName="IDfile_gen-netcode"
set -u

# check deps
which protoc &> /dev/null || (echo "Missing dependency \"protoc\"" && exit 1)
which grpc_cpp_plugin &> /dev/null || (echo "Missing dependency \"grpc_cpp_plugin\"" && exit 1)
which "$cxx" &> /dev/null || (echo "Missing dependency \"$cxx\"" && exit 1)
which ar &> /dev/null || (echo "Missing dependency \"ar\"" && exit 1)

###############################################################################
# Setup
[ -d "$gendir" ] && [ -e "$gendir/$idFileName" ] && rm -rf "$gendir" && echo "> Cleaned $gendir"
echo "> Creating $gendir"
mkdir -p "$gendir"/cpp
touch "$gendir/$idFileName"

###############################################################################
# Compile proto files
cd "$protodir"
echo "> .proto files from $protodir"
abs=$(pwd)
tmp=$(find "$protodir" -name "*.proto" -printf "%P ")
for fname in $tmp; do
	echo "$fname"
done
echo "> Generating proto code..."
protoc --proto_path="$protodir" --cpp_out="$gendir"/cpp --grpc_out="$gendir"/cpp --plugin=protoc-gen-grpc=$(which grpc_cpp_plugin) $(echo "$tmp")
cd - &> /dev/null

###############################################################################
# Create C++ lib
cd "$gendir"/cpp

echo "> .cc files"
tmp=$(find . -name "*.cc")
echo "$tmp"
echo "> Compiling..."
$cxx -c $(echo "$tmp")

echo "> .o files"
tmp=$(find . -name "*.o")
echo "$tmp"

echo "> Creating lib"
ar rvs "$libname" $(echo "$tmp")

###############################################################################
# Cleanup
echo "> Cleaning up..."
rm $(echo "$tmp")
cd - &> /dev/null

echo "Done"