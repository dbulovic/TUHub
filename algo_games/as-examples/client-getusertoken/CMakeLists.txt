##################################
# Author: Martin Wistauder
# Date: 12.10.2020
# Version: 1.1
##################################
cmake_minimum_required(VERSION 3.10)

add_executable(get-usertoken
        main-client-getusertoken.cpp)
target_include_directories(get-usertoken
        PUBLIC ../netcode/cpp)
target_link_directories(get-usertoken
        PUBLIC ../netcode/cpp)
target_link_libraries(get-usertoken
        PUBLIC -pthread -lprotobuf -lgrpc -lgrpc++ -lgpr libnetcode.a)