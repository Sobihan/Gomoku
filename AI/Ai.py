#!/usr/bin/python3
from math import ceil

GAME_MANAGER = 2
GAME_PLAYER = 1

class AI:
    def findBestMove(self, board):
        cpy = board
        maximum = 0
        bstMove = []
        for x in range(len(cpy)):
            for y in range(len(cpy[x])):
                maximum = max(maximum, cpy[x][y])
                if maximum == cpy[x][y]:
                    bstMove = [x, y]
        if not bstMove:
           return [-1, -1]
        return bstMove

    def boardIsEmpty(self, board):
        if self.findBestMove(board) == [-1, -1]:
            return True
        return False

    def copy(self, board):
        newBoard = []
        for line in board:
            tmp = []
            tmp = line.copy()
            newBoard.append(tmp)
        return newBoard

    def rows(self, board):
        return [[c for c in r] for r in board]

    def cols(self, board):
        return zip(*board)

    def vertical(self, board):
        verticalBoard = []
        for x in range(len(board)):
            tmp = []
            for y in range(len(board)):
                tmp.append(board[y][x])
            verticalBoard.append(tmp)
        return verticalBoard

    def diagonal(self, board, isReverse):
        newBoard = [None] * (len(board) - 1)
        if isReverse:
            board = [newBoard[:i] + r + newBoard[i:] for i, r in enumerate(self.rows(board))]
        else:
            board = [newBoard[i:] + r + newBoard[:i] for i, r in enumerate(self.rows(board))]
        return [[c for c in r if c is not None] for r in self.cols(board)]

    def getAllCopy(self, board):
        newBoard = self.copy(board)
        verticalBoard = self.vertical(board)
        diagonalBoard = self.diagonal(board, False)
        reverseDiagonal = self.diagonal(board, True)
        return [newBoard, verticalBoard, diagonalBoard, reverseDiagonal]

    def play(self, board):
        if self.boardIsEmpty(board):
            middle = ceil(len(board)/2)
            return [middle, middle]
        newBoard, verticalBoard, diagonalBoard, reverseDiagonal = self.getAllCopy(board)
        return [0]