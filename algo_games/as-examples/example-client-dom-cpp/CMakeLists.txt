##################################
# Author: Martin Wistauder
# Date: 12.10.2020
# Version: 1.0
##################################
cmake_minimum_required(VERSION 3.10)

add_executable(dom-example
        main-example-client-dom.cpp GameClient.cpp GameClient.h Helper.h)
target_include_directories(dom-example
        PUBLIC ../netcode/cpp)
target_link_directories(dom-example
        PUBLIC ../netcode/cpp)
target_link_libraries(dom-example
        PUBLIC -pthread -lprotobuf -lgrpc -lgrpc++ -lgpr libnetcode.a)