/**
 * @file Helper.h
 * @author Martin Wistauder
 * @date 12 Oct 2020
 * @version 1.0
 */
#pragma once

#include <iostream>
#include <memory>
#include <netcode.grpc.pb.h>

#define INFO(msg) std::cout << "\e[7;1mClient>\e[0m " << msg << std::endl
#define ERROR(msg) std::cout << "\e[7;1;91mClient> Error:\e[0m " << msg << std::endl
#define PROMPT std::cout << "\e[7;1;94mClient $>\e[0m "

namespace example::dom
{
	typedef std::unique_ptr<netcode::GameCom::Stub> StubPtr;
}

extern example::dom::StubPtr stub;