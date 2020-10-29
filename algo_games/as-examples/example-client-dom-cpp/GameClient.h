/**
 * @file GameClient.h
 * @author Martin Wistauder
 * @date 12 Oct 2020
 * @version 1.0
 */
#pragma once

#include <string>
#include <vector>
#include <sstream>
#include <memory>
#include <iostream>
#include <netcode.grpc.pb.h>
#include <iomanip>
#include <cassert>
#include "Helper.h"

namespace example::dom
{
	class GameClient
	{
		private:
			std::string _userToken;
			std::string _matchToken;

			netcode::MatchIDPacket* createMatchID();

		public:
			bool _beginningPlayer;
			::dom::GameState _currentState;
			::netcode::GameStatus _currentStatus;

		public:
			explicit GameClient(const std::string& userToken);
			void newMatch(uint32_t width, uint32_t height);
			bool hasMatchStarted();
			void submitTurn(::dom::GameTurn* turn);
			void printGameStatus();
			void showGameState();
			void queryGameState();
			bool isMatchOver();
			bool isTurnPlayable();
			void queryTimeout();
			void queryOpponentInfo();
	};
}