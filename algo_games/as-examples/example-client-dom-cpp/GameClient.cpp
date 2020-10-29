/**
 * @file GameClient.cpp
 * @author Martin Wistauder
 * @date 12 Oct 2020
 * @version 1.0
 */
#include "GameClient.h"

example::dom::GameClient::GameClient(const std::string& userToken) : _userToken(userToken)
{
}

void example::dom::GameClient::newMatch(uint32_t width, uint32_t height)
{
	// needed variables
	netcode::MatchRequest matchRequest;
	netcode::MatchResponse matchResponse;
	grpc::ClientContext context; // NOTE: after a rpc uses the client context, it gets invalidated and cannot be reused
	grpc::Status status;

	// create new game parameters
	auto gameParameters = new ::dom::GameParameter();
	gameParameters->set_board_width(width);
	gameParameters->set_board_height(height);

	// set request parameters
	matchRequest.set_user_token(_userToken);
	matchRequest.set_game_token("dom");
	matchRequest.set_allocated_dom_game_parameters(gameParameters);

	// do the remote procedure call
	status = stub->NewMatch(&context, matchRequest, &matchResponse);
	assert(status.ok());

	// handle response
	_matchToken = matchResponse.match_token();
	_beginningPlayer = matchResponse.beginning_player();

	INFO("New Match: " << _matchToken);
	INFO("First player? " << (_beginningPlayer ? "yes" : "no"));
}

void example::dom::GameClient::submitTurn(::dom::GameTurn* turn)
{
	// create the request
	netcode::TurnRequest turnRequest;
	turnRequest.set_allocated_match_id(createMatchID());
	turnRequest.set_allocated_dom_game_turn(turn);

	// do the rpc
	netcode::TurnResponse turnResponse;
	grpc::ClientContext context;
	grpc::Status status = stub->SubmitTurn(&context, turnRequest, &turnResponse);

	// check the status
	assert(status.ok());

	// handle the response
	switch (turnResponse.turn_status())
	{
		case netcode::OK:
			std::cout << "Turn was ok\n";
			break;
		case netcode::INVALID_TURN:
			std::cout << "Turn was invalid\n";
			showGameState();
			break;
		case netcode::NOT_YOUR_TURN:
			std::cout << "Not your turn\n";
			break;
		case netcode::MATCH_OVER:
			std::cout << "Match over\n";
			printGameStatus();
			break;
		default:
			assert(false);
	}
}

void example::dom::GameClient::printGameStatus()
{
	switch (_currentStatus)
	{
		case netcode::MATCH_NOT_STARTED:
			std::cout << "Game has not yet started. No one dares to approach you!\n";
			return;
		case netcode::YOUR_TURN:
			std::cout << "It's your turn \\(°°)/\n";
			return;
		case netcode::OPPONENTS_TURN:
			std::cout << "It's not your turn (>°°<)\n";
			return;
		case netcode::MATCH_WON:
			std::cout << "Game over, match won! :)\n";
			return;
		case netcode::MATCH_LOST:
			std::cout << "Game over, match lost! :(\n";
			return;
		case netcode::DRAW:
			std::cout << "Game over, it's a draw! :|\n";
			return;
		case netcode::MATCH_ABORTED:
			std::cout << "The match has been aborted.\n";
			return;
		default:
			assert(false);
	}
}

void example::dom::GameClient::showGameState()
{
	queryGameState();

	uint32_t width = _currentState.board_width();
	uint32_t height = _currentState.board_height();
	const char* data = _currentState.board_data().c_str();

	std::cout << "-------------------------------\n";
	for (int y = 0; y < height; ++y)
	{
		for (int x = 0; x < width; ++x)
		{
			std::cout << data[x + y * width];
		}
		std::cout << "\n";
	}
	std::cout << "-------------------------------\n";

	printGameStatus();
}

void example::dom::GameClient::queryGameState()
{
	// needed variables
	std::unique_ptr<netcode::MatchIDPacket> matchIDPacket(createMatchID());
	netcode::GameStateResponse gameStateResponse;
	grpc::ClientContext context;
	grpc::Status status;

	// rpc
	status = stub->GetGameState(&context, *matchIDPacket, &gameStateResponse);
	assert(status.ok() && "Error: querying game state failed.");

	// handle response
	_currentState = gameStateResponse.dom_game_state();
	_currentStatus = gameStateResponse.game_status();
}

bool example::dom::GameClient::isMatchOver()
{
	return _currentStatus == netcode::MATCH_WON ||
		   _currentStatus == netcode::MATCH_LOST ||
		   _currentStatus == netcode::DRAW ||
		   _currentStatus == netcode::MATCH_ABORTED;
}

bool example::dom::GameClient::isTurnPlayable()
{
	switch (_currentStatus)
	{
		case netcode::YOUR_TURN:
			return true;
		case netcode::OPPONENTS_TURN:
			return false;
		case netcode::MATCH_WON:
		case netcode::MATCH_LOST:
		case netcode::DRAW:
		case netcode::MATCH_NOT_STARTED:
		case netcode::MATCH_ABORTED:
		default:
			assert(false);
	}
}

netcode::MatchIDPacket* example::dom::GameClient::createMatchID()
{
	auto matchIdPacket = new netcode::MatchIDPacket();
	matchIdPacket->set_user_token(_userToken);
	matchIdPacket->set_match_token(_matchToken);
	return matchIdPacket;
}

void example::dom::GameClient::queryTimeout()
{
	// needed variables
	std::unique_ptr<netcode::MatchIDPacket> matchIDPacket(createMatchID());
	netcode::GetTimeoutResponse timeoutResponse;
	grpc::ClientContext context;
	grpc::Status status;

	// rpc
	status = stub->GetTimeout(&context, *matchIDPacket, &timeoutResponse);
	assert(status.ok() && "Error: querying timeout failed.");

	// handle response
	INFO("Negotiated timeout: " << timeoutResponse.timeout_seconds());
}

void example::dom::GameClient::queryOpponentInfo()
{
	// needed variables
	std::unique_ptr<netcode::MatchIDPacket> matchIDPacket(createMatchID());
	netcode::OpponentInfoResponse opponentInfoResponse;
	grpc::ClientContext context;
	grpc::Status status;

	// rpc
	status = stub->GetOpponentInfo(&context, *matchIDPacket, &opponentInfoResponse);
	assert(status.ok() && "Error: querying opponent info failed.");

	// handle response
	INFO("Opponent: " << opponentInfoResponse.user_pseudonym() << ", from group: "
					  << opponentInfoResponse.group_pseudonym());
}

bool example::dom::GameClient::hasMatchStarted()
{
	queryGameState();
	return _currentStatus != netcode::MATCH_NOT_STARTED;
}
