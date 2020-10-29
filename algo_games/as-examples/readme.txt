### INTRODUCTION ###

The c++ examples should give you a quick look at how to use our given network protocol based on the grpc framework.
Note, that you have to edit the examples first (in code), before you can properly use them.

The network protocol is defined in the '.proto' files.
The main file is the 'netcode.proto', which houses all available remote procedure calls.
The other files are game-specific implementations, which are used inside the 'netcode.proto'.

Use the 'gen-netcode.sh' script to generate a library for c++ (called 'libnetcode.a').
Use cmake to initialize the build system.
To build all examples the 'libnetcode.a' is required, additionally to the general requirements listed in 'dependencies.txt'.

Keep in mind, that you don't have to use these examples or c++ for the practical, they exist to give you an introduction of the client structure.

### HOW TO BUILD ###

1. Check dependencies
2. run './gen-netcode.sh $PWD/protobuf $PWD/netcode'
3. 'mkdir build'
4. 'cd build'
5. 'cmake ..'
6. 'make -j'
