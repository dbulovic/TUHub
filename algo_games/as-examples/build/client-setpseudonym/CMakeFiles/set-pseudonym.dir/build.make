# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/david/Documents/TUG/TUhub/algo_games/as-examples

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/david/Documents/TUG/TUhub/algo_games/as-examples/build

# Include any dependencies generated for this target.
include client-setpseudonym/CMakeFiles/set-pseudonym.dir/depend.make

# Include the progress variables for this target.
include client-setpseudonym/CMakeFiles/set-pseudonym.dir/progress.make

# Include the compile flags for this target's objects.
include client-setpseudonym/CMakeFiles/set-pseudonym.dir/flags.make

client-setpseudonym/CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.o: client-setpseudonym/CMakeFiles/set-pseudonym.dir/flags.make
client-setpseudonym/CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.o: ../client-setpseudonym/main-client-setpseudonym.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/david/Documents/TUG/TUhub/algo_games/as-examples/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object client-setpseudonym/CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.o"
	cd /home/david/Documents/TUG/TUhub/algo_games/as-examples/build/client-setpseudonym && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.o -c /home/david/Documents/TUG/TUhub/algo_games/as-examples/client-setpseudonym/main-client-setpseudonym.cpp

client-setpseudonym/CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.i"
	cd /home/david/Documents/TUG/TUhub/algo_games/as-examples/build/client-setpseudonym && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/david/Documents/TUG/TUhub/algo_games/as-examples/client-setpseudonym/main-client-setpseudonym.cpp > CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.i

client-setpseudonym/CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.s"
	cd /home/david/Documents/TUG/TUhub/algo_games/as-examples/build/client-setpseudonym && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/david/Documents/TUG/TUhub/algo_games/as-examples/client-setpseudonym/main-client-setpseudonym.cpp -o CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.s

# Object files for target set-pseudonym
set__pseudonym_OBJECTS = \
"CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.o"

# External object files for target set-pseudonym
set__pseudonym_EXTERNAL_OBJECTS =

client-setpseudonym/set-pseudonym: client-setpseudonym/CMakeFiles/set-pseudonym.dir/main-client-setpseudonym.cpp.o
client-setpseudonym/set-pseudonym: client-setpseudonym/CMakeFiles/set-pseudonym.dir/build.make
client-setpseudonym/set-pseudonym: client-setpseudonym/CMakeFiles/set-pseudonym.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/david/Documents/TUG/TUhub/algo_games/as-examples/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable set-pseudonym"
	cd /home/david/Documents/TUG/TUhub/algo_games/as-examples/build/client-setpseudonym && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/set-pseudonym.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
client-setpseudonym/CMakeFiles/set-pseudonym.dir/build: client-setpseudonym/set-pseudonym

.PHONY : client-setpseudonym/CMakeFiles/set-pseudonym.dir/build

client-setpseudonym/CMakeFiles/set-pseudonym.dir/clean:
	cd /home/david/Documents/TUG/TUhub/algo_games/as-examples/build/client-setpseudonym && $(CMAKE_COMMAND) -P CMakeFiles/set-pseudonym.dir/cmake_clean.cmake
.PHONY : client-setpseudonym/CMakeFiles/set-pseudonym.dir/clean

client-setpseudonym/CMakeFiles/set-pseudonym.dir/depend:
	cd /home/david/Documents/TUG/TUhub/algo_games/as-examples/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/david/Documents/TUG/TUhub/algo_games/as-examples /home/david/Documents/TUG/TUhub/algo_games/as-examples/client-setpseudonym /home/david/Documents/TUG/TUhub/algo_games/as-examples/build /home/david/Documents/TUG/TUhub/algo_games/as-examples/build/client-setpseudonym /home/david/Documents/TUG/TUhub/algo_games/as-examples/build/client-setpseudonym/CMakeFiles/set-pseudonym.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : client-setpseudonym/CMakeFiles/set-pseudonym.dir/depend

