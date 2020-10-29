##################################
# Author: Martin Wistauder
# Date: 12.10.2020
# Version: 1.1
##################################
cmake_minimum_required(VERSION 3.10)

add_executable(user-registration
        main-client-userregistration.cpp)
target_include_directories(user-registration
        PUBLIC ../netcode/cpp)
target_link_directories(user-registration
        PUBLIC ../netcode/cpp)
target_link_libraries(user-registration
        PUBLIC -pthread -lprotobuf -lgrpc -lgrpc++ -lgpr libnetcode.a)