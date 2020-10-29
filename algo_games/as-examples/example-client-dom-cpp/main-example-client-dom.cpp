/**
 * @file main-example-client-dom.cpp
 * @author Martin Wistauder
 * @date 12 Oct 2020
 * @version 1.0
 */
#include <string>
#include <iostream>
#include <netcode.grpc.pb.h>
#include <grpcpp/create_channel.h>
#include <grpcpp/security/credentials.h>
#include "GameClient.h"
#include "Helper.h"

void autoPlay(example::dom::GameClient& client);

example::dom::StubPtr stub;

int main()
{
	std::string userToken = ""; // TODO: insert your UserToken
	uint32_t boardWidth = 8;
	uint32_t boardHeight = 8;

	// connect to the server
	std::string host = "gameserver.ist.tugraz.at:80";
	INFO("Trying to connect to " << host);
	auto creds = grpc::InsecureChannelCredentials();
	auto channel = grpc::CreateChannel(host, creds);

	// wait till we connect or timeout after 5 seconds
	if (!channel->WaitForConnected(gpr_time_add(
			gpr_now(GPR_CLOCK_REALTIME),
			gpr_time_from_seconds(5, GPR_TIMESPAN))))
	{
		std::cout << "Error: Connection Timeout.\n";
		return 1;
	}

	// create the stub
	stub = netcode::GameCom::NewStub(channel);

	// create the game client
	example::dom::GameClient client(userToken);

	// play the game
	INFO("Requesting new match.");
	client.newMatch(boardWidth, boardHeight);

	// wait for an opponent
	std::cout << "Waiting for opponent" << std::flush;
	while (!client.hasMatchStarted())
	{
		gpr_sleep_until(gpr_time_add(
				gpr_now(GPR_CLOCK_REALTIME),
				gpr_time_from_seconds(2, GPR_TIMESPAN)));
		std::cout << "." << std::flush;
	}
	std::cout << "\n";
	INFO("Opponent found.");

	// let's fight :D
	client.queryOpponentInfo();
	client.queryTimeout();
	autoPlay(client);

	return 0;
}

void autoPlay(example::dom::GameClient& client)
{
	client.showGameState();
	ERROR("Maybe let's think about a strategy first :P");
}