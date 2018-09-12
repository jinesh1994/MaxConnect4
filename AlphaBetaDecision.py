from MaxConnect4Game import *
from copy import deepcopy

# minusInfinite = -2147483647
# infinite = 2147483648

def AlphaBetaDecision(state):
    lstGames = []
    # print minusInfinite, infinite
    for a,s in Successors(state):
        v = MinValue(s, -2147483647, 2147483648, deepcopy(state.depthLimt))
        lstGames.append((a, v))
    # print lstGames
    finalSelection = []
    i = 0
    for game in lstGames:
        # print('i: ',i,'a: ',game[0],'v: ',game[1])
        if i == 0:
            finalSelection = game
            i += 1
            continue
        if game[1] > finalSelection[1]:
            finalSelection = game
        i += 1
    
    return finalSelection[0], finalSelection[1]

def MaxValue(state, alpha, beta, depth):
    if state.checkPieceCount() == 41 or depth == 1:
        state.countScore()
        # print state.scoreWithEval()
        return state.scoreWithEval()
    v = -2147483647
    # print 'Max:\n','alpha: ', alpha, 'beta: ', beta, 'v: ', v
    for a,s in Successors(state):
        v = max(v, MinValue(s, alpha, beta, deepcopy(depth - 1)))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def MinValue(state, alpha, beta, depth):
    if state.checkPieceCount() == 41 or depth == 1:
        state.countScore()
        # print state.scoreWithEval()
        return state.scoreWithEval()
    v = 2147483648
    # print 'Min:\n','alpha: ', alpha, 'beta: ', beta, 'v: ', v
    for a,s in Successors(state):
        v = min(v, MaxValue(s, alpha, beta, deepcopy(depth - 1)))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def Successors(state):
    lstGames = []
    if state.currentTurn == 1:
        ct = 2
    else:
        ct = 1
    for j in range(7):
        newGame = maxConnect4Game()
        newGame.gameBoard = deepcopy(state.gameBoard)
        newGame.currentTurn = ct
        if newGame.playPiece(j):
            lstGames.append((j, newGame))
    return lstGames