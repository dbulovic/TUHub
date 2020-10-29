##################################
# Author: Martin Wistauder
# Date: 12.10.2020
# Version: 1.1
##################################
cmake_minimum_required(VERSION 3.10)

add_executable(set-pseudonym
        main-client-setpseudonym.cpp)
target_include_directories(set-pseudonym
        PUBLIC ../netcode/cpp)
target_link_directories(set-pseudonym
        PUBLIC ../netcode/cpp)
target_link_libraries(set-pseudonym
        PUBLIC -pthread -lprotobuf -lgrpc -lgrpc++ -lgpr libnetcode.a)