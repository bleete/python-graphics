import pygame, sys
from reversiboard import *
from reversimoves import *
import random
import time

# Window parameters
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

# Colors
DARK_GREEN = (0, 128, 0)
DARK_GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Board size (number of squares on each side)
BOARD_SIZE = 8

HUMAN = 'human'
COMPUTER = 'computer'

# Players: computer is 'W', human is 'B'
# Pick random starting player
sides = [ HUMAN, COMPUTER ]
colors = { HUMAN : WHITE , COMPUTER : BLACK }

playerIndex = random.randrange(2)
board = ReversiBoard(BOARD_SIZE, sides)

pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

drawer = ReversiBoardDrawer(board,
                            surface,
                            WINDOW_WIDTH,
                            WINDOW_HEIGHT,
                            DARK_GREY,
                            DARK_GREEN,
                            GREEN,
                            sides, colors)



try:
    playing = True
    missedMoves = 0
    winner = None

    while playing:
        opponentIndex = 1 - playerIndex
        player = sides[playerIndex]
        opponent = sides[opponentIndex]

        drawer.drawBoard()

        if board.noLegalMoves(player, opponent):
            print(player + " has no legal move.")
            move = None
            time.sleep(3)
        elif player == HUMAN:
            move = getPlayerMove(drawer)
        else:
            move = getComputerMove(board, COMPUTER, HUMAN)

        if move is None:
            missedMoves += 1

        if missedMoves == 2:
            winner = board.determineWinner()

        moveResult = board.resultOfMove(move, player, opponent)
        board.apply(move, moveResult, player)
        drawer.drawMove(move, player)

        if board.isFull():
            winner = board.determineWinner()
            playing = False

        playerIndex = 1 - playerIndex

except PlayerQuitException:
    pass

print("The winner is the " + winner)