##################################
# Author: Martin Wistauder
# Date: 12.10.2020
# Version: 1.1
##################################
cmake_minimum_required(VERSION 3.10)

add_executable(group-registration
        main-client-groupregistration.cpp)
target_include_directories(group-registration
        PUBLIC ../netcode/cpp)
target_link_directories(group-registration
        PUBLIC ../netcode/cpp)
target_link_libraries(group-registration
        PUBLIC -pthread -lprotobuf -lgrpc -lgrpc++ -lgpr libnetcode.a)