import grpc
import time
import sys
from itertools import permutations
from math import sqrt

sys.path.append('./netcode')

from netcode.netcode_pb2_grpc import GameComStub
from netcode.netcode_pb2 import *
from netcode.dozo_pb2 import *

# settings
userToken = "daeda48c89c09150a68fc5ac290db5dabd6cb2cc53fd5bc6468982efb8d4eaba"  # Your user token

# vars
matchToken = ""

# setup comms
channel = grpc.insecure_channel('gameserver.ist.tugraz.at:80')
stub = GameComStub(channel)


# Query your userToken to be able to start a new match
def getUserToken(matr_number, secret):
    auth = AuthPacket()
    auth.matr_number = matr_number
    auth.secret = secret
    response = stub.GetUserToken(auth)
    return response.user_token


# Request a new match for Dozo
def newMatch(length, colors):
    params = GameParameter(board_length=length,
                           number_of_colors=colors)
    request = MatchRequest(user_token=userToken,
                           game_token='dzo',
                           dzo_game_parameters=params)
    response = stub.NewMatch(request)

    print("New Match:", response.match_token)
    print("First player?", response.beginning_player)

    global matchToken
    matchToken = response.match_token


# Helper to create the MatchIDPacket
def createMatchId():
    return MatchIDPacket(user_token=userToken,
                         match_token=matchToken)


# Let's get started
def queryGameState():
    response = stub.GetGameState(createMatchId())
    return response.dzo_game_state, response.game_status


# Sleepy time
def waitMatchStarted():
    while queryGameState()[1] == GameStatus.MATCH_NOT_STARTED:
        time.sleep(1)


# Identify yourself!
def queryOpponentInfo():
    response = stub.GetOpponentInfo(createMatchId())
    print("Opponent:", response.user_pseudonym, "(" + str(response.elo.user_elo) + "),",
          "from group:", response.group_pseudonym, "(" + str(response.elo.group_elo) + ")")
    pass


# What did we agree on? 2 Timeout, keine mehr?
def queryTimeout():
    response = stub.GetTimeout(createMatchId())
    print("Negotiated timeout:", response.timeout_seconds, "sec")
    pass


# I did implement this, but I deleted it because it was not fancy enough.
def showGameState():
    state, status = queryGameState()
    len = state.board_length
    i = 0
    for y in range(len):
        for x in range(y + 1):
            print(state.board_data[i], end=' ')
            i = i+1
        print()
    print()
    return state, status


# Submit a turn and evaluate the turn status info. Also returns the Dozo board state.
def submitTurn(turn):
    request = TurnRequest(match_id=createMatchId(),
                          dzo_game_turn=turn)
    response = stub.SubmitTurn(request)
    if response.turn_status == TurnStatus.INVALID_TURN:
        print("Error: Invalid turn submitted.")
        exit(1)
    if response.turn_status == TurnStatus.MATCH_OVER:
        print("Match is over.")
        print(queryGameState().game_status)
        exit(0)
    if response.turn_status == TurnStatus.NOT_YOUR_TURN:
        print("This isn't the time to use that!")
    return response.dzo_game_state


# Helper
def isMatchOver(game_status):
    return game_status in [GameStatus.MATCH_WON,
                           GameStatus.MATCH_LOST,
                           GameStatus.DRAW,
                           GameStatus.MATCH_ABORTED]


# Helper
def isTurnPlayable(game_status):
    return game_status == YOUR_TURN


# Query, calculate, submit, repeat, query, calculate, submit, repeat
def autoPlay():
    print("TODO: implement autoPlay()")
    state, status = showGameState()

    len = state.board_length

    win_triangles = findTriangles(len)

    client_data = [[198 for i in range(len)] for i in range(len)]

    while(not(isMatchOver(status))):
        state, status = showGameState()
        time.sleep(1)
        if isTurnPlayable(status):
            for y in range(len):
                for x in range(y+1):
                    print(int(x + (y * (y + 1) / 2)))
                    client_data[y][x] = state.board_data[int(x + (y * (y + 1) / 2))]

            turn_x = turn_y = turn_color = 0

            for i in range(state.number_of_colors):
                if state.remaining_stones[i] > 0:
                    turn_color = i
                    break

            xy_found = False
            for y in range(len):
                for x in range(y + 1):
                    if client_data[x][y] != 255:
                        for y1 in range(len):
                            for x1 in range(y + 1):
                                if x1 == x and y1 == y:
                                        continue
                                if client_data[x1][y1] == client_data[x][y]:
                                    for y2 in range(len):
                                        for x2 in range(y + 1):
                                            pass
                                            #check permutation
            

            if(not(xy_found)):
                for y in range(len):
                    for x in range(y + 1):
                        if client_data[x][y] == 255:
                            for y1 in range(len):
                                for x1 in range(y + 1):
                                    if x1 == x and y1 == y:
                                        continue
                                    
                                    for y2 in range(len):
                                        for x2 in range(y + 1):
                                            pass
                                            #check permutation for defence
            print(turn_x, turn_y, turn_color)
            turn = GameTurn(x=turn_x, y=turn_y, color=turn_color)
            state = submitTurn(turn)

    pass

def findTriangles(leng):

    cor = [i for i in range(leng**2)]

    per = list(permutations(cor, 3))

    eql = []

    for p in per:
        tril = list(p)
        x1 = tril[0] // leng
        y1 = tril[0] % leng
        x2 = tril[1] // leng
        y2 = tril[1] % leng
        x3 = tril[2] // leng
        y3 = tril[2] % leng

        if x1 > y1 or x2 > y2 or x3 > y3:
            continue

        side1 = sqrt((x1 - x2)**2 + (y1-y2)**2)
        side2 = sqrt((x2 - x3)**2 + (y2-y3)**2)
        side3 = sqrt((x3 - x1)**2 + (y3-y1)**2)

        tri= [side1, side2, side3]
        tri.sort()

        if tri[0] < tri[1]+tri[2]:
            if tri[0] == tri[2]:
                continue
            elif tri[1] == tri[2] or tri[1] == tri[0]:
                if abs(tri[2]**2 - tri[1]**2 - tri[0]**2) < 0.0001:
                    eql.append([[x1, y1],[x2, y2],[x3, y3]]) 
    return eql


def main():
    # getUserToken("INSERT MATR#", "INSERT SECRET") # Please only do this once (ever) and save your userToken somewhere
    print("UserToken:", userToken)
    newMatch(7, 4)
    waitMatchStarted()
    print("Opponent found.")
    queryOpponentInfo()
    queryTimeout()
    autoPlay()


if __name__ == "__main__":
    main()
