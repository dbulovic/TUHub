#!/bin/bash
## @file build-examples.sh
## @author Martin Wistauder
## @date 12 Dec 2019
## @version 1.0
## @brief Generate netcode and build examples.
set -u
set -e

# vars
wd="./build"
idFileName="IDfile_build"

# check deps
which cmake &> /dev/null || (echo "Missing dependency \"cmake\"" && exit 1)

# gen netcode
./gen-netcode.sh "$PWD/protobuf" "$PWD/netcode"

# create build dir
[ -d "$wd" ] && [ -e "$wd/$idFileName" ] && rm -rf "$wd" && echo "Cleaned build dir"
echo "Creating build dir"
mkdir -p "$wd"
touch "$wd/$idFileName"

# compile sources
echo "Compiling"
cd "$wd"
cmake ..
make -j

echo "Done"