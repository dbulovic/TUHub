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

won = 0
lost = 0
draw = 0
abort = 0

# Query your userToken to be able to start a new match
# def getUserToken(matr_number, secret):
#     auth = AuthPacket()
#     auth.matr_number = matr_number
#     auth.secret = secret
#     response = stub.GetUserToken(auth)
#     return response.user_token


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
    leng = state.board_length

    for y in range(leng):
        offset = leng - y
        for i in range(offset): print(" ", end='')
        for x in range(y + 1):
            slot = state.board_data[int(x + (y * (y + 1) / 2))]
            if slot == 255: print("X", end=' ')
            else: print (slot, end=' ')
        print()
    print()
    print("____________")
    print("Stone | left")
    print("------------")
    for i in range(len(state.remaining_stones)):
        print("  ", i, " | ", state.remaining_stones[i])
        print("------------")
    print("============")
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
        #print(queryGameState().game_status)
        #exit(0)
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
    state, status = showGameState()

    leng = state.board_length

    win_triangles = findTriangles(leng)

    client_data = [[198 for i in range(leng)] for i in range(leng)]

    while(not(isMatchOver(status))):
        state, status = showGameState()
        time.sleep(1)
        if isTurnPlayable(status):
            for y in range(leng):
                for x in range(y+1):
                    client_data[y][x] = state.board_data[int(x + (y * (y + 1) / 2))]

            turn_x = turn_y = turn_color = 0

            xy_found = False
            for y in range(leng):
                for x in range(y + 1):
                    if client_data[y][x] != 255:
                        for y1 in range(leng):
                            for x1 in range(y1 + 1):
                                if x1 == x and y1 == y:
                                        continue
                                if client_data[y1][x1] == client_data[y][x]:
                                    index_candid = client_data[y][x]
                                    for y2 in range(leng):
                                        for x2 in range(y2 + 1):
                                            if (x1 == x2 and y1 == y2) or (x == x2 and y == y2):
                                                continue
                                            if client_data[y2][x2] == 255:
                                                if ([[x,y],[x1,y1],[x2,y2]] in win_triangles) and state.remaining_stones[index_candid] > 0:
                                                    turn_x = x2
                                                    turn_y = y2
                                                    turn_color = client_data[y][x]
                                                    xy_found = True
                                                    print("off")
                                            if(xy_found): break
                                        if(xy_found): break
                                    if(xy_found): break
                                if(xy_found): break
                            if(xy_found): break
                        if(xy_found): break
                    if(xy_found): break
                if(xy_found): break
            
            not_these = []
            not_these_c = []
            if(not(xy_found)):
                for y in range(leng):
                    for x in range(y + 1):
                        if client_data[y][x] != 255:
                            for y1 in range(leng):
                                for x1 in range(y1 + 1):
                                    if x1 == x and y1 == y:
                                        continue
                                    if client_data[y1][x1] == 255:                                    
                                        for y2 in range(leng):
                                            for x2 in range(y2 + 1):
                                                if client_data[y2][x2] == 255 and [[x,y],[x1,y1],[x2,y2]] in win_triangles:
                                                    not_these.append([x2, y2])
                                                    not_these_c.append(client_data[y][x])

                for y in range(leng):
                    for x in range(y + 1):
                        if client_data[y][x] != 255: continue 
                        indices = []
                        for inc in range(len(not_these)):
                            if not_these[inc] == [x,y]:
                                indices.append(inc)

                        for i in range(state.number_of_colors):
                            if state.remaining_stones[i] > 0:
                                cnt = 0
                                if indices == []:
                                    turn_x = x
                                    turn_y = y
                                    turn_color = i
                                    xy_found = True
                                    print("def")
                                    break

                                for j in indices:
                                    if not_these_c[j] == i:
                                        break
                                    cnt += 1

                                    if cnt == len(indices):
                                        turn_x = x
                                        turn_y = y
                                        turn_color = i
                                        xy_found = True
                                        print("def")
                                        break
                                if(xy_found): break
                            if(xy_found): break
                        if(xy_found): break
                    if(xy_found): break
                
            if (not(xy_found)):
                for i in range(state.number_of_colors):
                    if state.remaining_stones[i] > 0:
                        turn_color = i
                        break

                i = 0
                xy_found = False
                for y in range(leng):
                    for x in range(y + 1):
                        if state.board_data[i] == 255:
                            turn_x = x
                            turn_y = y
                            xy_found = True
                            break
                        i = i+1
                    if(xy_found): break
                                                    
            print(turn_x, turn_y, turn_color)
            turn = GameTurn(x=turn_x, y=turn_y, color=turn_color)
            state = submitTurn(turn)
    
    showGameState()
    
    if status == GameStatus.MATCH_WON: 
        print("Won.") 
        global won
        won += 1
    if status == GameStatus.MATCH_LOST: 
        print("Lost.") 
        global lost
        lost +=1
    if status == GameStatus.DRAW: 
        print("Draw.") 
        global draw
        draw += 1
    if status == GameStatus.MATCH_ABORTED: 
        print("Abort.") 
        global abort
        abort += 1

    pass

def findTriangles(leng):

    cor = [i for i in range(leng**2)]

    per = list(permutations(cor, 3))

    eql = []

    for p in per:
        tril = list(p)
        y1 = tril[0] // leng
        x1 = tril[0] % leng
        y2 = tril[1] // leng
        x2 = tril[1] % leng
        y3 = tril[2] // leng
        x3 = tril[2] % leng

        if x1 > y1 or x2 > y2 or x3 > y3:
            continue

        x1_s = x1 + (leng - 1 - y1)/2
        x2_s = x2 + (leng - 1 - y2)/2
        x3_s = x3 + (leng - 1 - y3)/2

        y1_s = y1 - 0.1339760000001133*y1
        y2_s = y2 - 0.1339760000001133*y2
        y3_s = y3 - 0.1339760000001133*y3

        side1 = sqrt((x1_s - x2_s)**2 + (y1_s-y2_s)**2)
        side2 = sqrt((x2_s - x3_s)**2 + (y2_s-y3_s)**2)
        side3 = sqrt((x3_s - x1_s)**2 + (y3_s-y1_s)**2)

        if abs(side1 - side2) < 0.00001 and abs(side1 - side3) < 0.00001 and abs(side3 - side2) < 0.00001:
            eql.append([[x1, y1],[x2, y2],[x3, y3]])
    return eql


def main():
    print("UserToken:", userToken)
    size = 3
    n_colors = 1
    n_games = 3 # change to how many games you want to play
    played = 0
    global won
    global lost
    global draw
    global abort
    while(played < n_games):
        newMatch(size, n_colors)
        waitMatchStarted()
        print("Opponent found.")
        queryOpponentInfo()
        queryTimeout()
        autoPlay()

        played += 1
        print("Played: ",played, "/", n_games)
        print("Won: ", won, " Draw: ", draw, " Lost: ", lost, " Abort: ", abort)


if __name__ == "__main__":
    main()
