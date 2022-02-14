#!/usr/bin/python3
from math import ceil
from nis import match
from operator import ne

GAME_MANAGER = 2
GAME_PLAYER = 1

class AI:
    def createPatterns(self):
        self.winnerPatterns = [
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 0, 1, 1, 0],

        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1]
        ]

        self.looserPatterns = [
        [0, 2, 2, 2, 2],
        [2, 2, 2, 2, 0],
        [0, 2, 2, 2, 0]
        [0, 2, 0, 2, 2],
        [2, 0, 2, 2, 0],
        [2, 2, 2, 0, 2],
        [2, 2, 0, 2, 2],
        [2, 0, 2, 2, 2],
        [2, 0, 2, 2]
        ]
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

    def unDiagonal(self, board, lenght):
        un_b = []
        y = 0
        l = []
        while (y < lenght):
            l.append(board[y][y])
            y += 1
        y = 1
        un_b.append(l)
        rem = 1
        while(y < lenght):
            l = []
            tmp = 0
            while (y < lenght):
                l.append(board[y][y - rem])
                y += 1
                tmp += 1
            while (len(l) < lenght):
                l.append(board[y][tmp - 1])
                y += 1
            un_b.append(l)
            rem += 1
            y = rem
        un_b = self.vertical(un_b)
        return un_b
    def unreverseDiagnoal(self, board, lenght):
        board.reverse()
        board = self.unDiagonal(board, lenght)
        for i in board:
            i.reverse()
        return board
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

    def unvertical(self, board):
        return self.vertical(board)

    def getAllCopy(self, board):
        newBoard = self.copy(board)
        verticalBoard = self.vertical(board)
        diagonalBoard = self.diagonal(board, False)
        reverseDiagonal = self.diagonal(board, True)
        return [newBoard, verticalBoard, diagonalBoard, reverseDiagonal]

    def match(board, pattern):
        for x in range(len(board)):
            if board[x] == pattern[0] and board[x:x+len(pattern)] == pattern:
                return True
        return False

    def getCritcalMove(self, board, who):
        if who == GAME_PLAYER:
            for b in board:
                for i in self.winnerPatterns:
                    if match(b, i):
                        return board.index(b)
        else:
            for b in board:
                for i in self.looserPatterns:
                    if match(b, i):
                        return board.index(b)
        if who == GAME_PLAYER:
            for b in board:
                for i in self.winnerPatterns:
                    if match(b, i):
                        return board.index(b)
        else:
            for b in board:
                for i in self.looserPatterns:
                    if match(b, i):
                        return board.index(b)
        return -1
    
    def getValue(board, pattern):
        for x in range(len(board)):
            if board[x] == pattern[0] and board[x:x+len(pattern)] == pattern:
                return x
        return -1
    def getPatern(self, board, values, who):
        if (who == GAME_PLAYER):
            value = self.getValue(board[values], self.winnerPatterns[0])
            if value != -1:
                board[values][value] = 8
                return board
            value = self.getValue(board[values], self.winnerPatterns[1])
            if value != -1:
                board[values][value + 4] = 8
                return board
            value = self.getValue(board[values], self.winnerPatterns[2])
            if value != -1:
                board[values][value] = 8
                return board
            value = self.getValue(board[values], self.winnerPatterns[3])
            if (value != -1):
                board[values][value] = 8
                return board        
            value = self.getValue(board[values], self.winnerPatterns[4])
            if (value != -1):
                board[values][value + 4] = 8
                return board
            value = self.getValue(board[values], self.winnerPatterns[5])
            if (value != -1):
                board[values][value + 3] = 8
                return board
            value = self.getValue(board[values], self.winnerPatterns[6])
            if (value != -1):
                board[values][value + 2] = 8
                return board
            value = self.getValue(board[values], self.winnerPatterns[7])
            if (value != -1):
                board[values][value + 1] = 8
                return board
        else:
            value = self.getValue(board[values], self.looserPatterns[0])
            if (value != -1):
                board[values][value] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[1])
            if (value != -1):
                board[values][value + 4] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[2])
            if (value != -1):
                board[values][value] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[3])
            if (value != -1):
                board[values][value + 2] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[4])
            if (value != -1):
                board[values][value + 1] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[5])
            if (value != -1):
                board[values][value + 3] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[6])
            if (value != -1):
                board[values][value + 2] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[7])
            if (value != -1):
                board[values][value + 1] = 8
                return board
            value = self.getValue(board[values], self.looserPatterns[8])
            if (value != -1):
                board[values][value + 1] = 8
                return board
        return board
    
    def importantMove(self, who, newBoard, diagonalBoard, reverseDiagonalBoard, verticalBoard):
        result = self.getCritcalMove(newBoard, who)
        if result != -1:
            returnValue = self.getPatern(newBoard, result, who)
            return self.findBestMove(returnValue)
        result = self.getCritcalMove(verticalBoard, who)
        if result != -1:
            returnValue = self.getPatern(verticalBoard, result, who)
            returnValue = self.unvertical(verticalBoard)
            return self.findBestMove(returnValue)
        result = self.getCritcalMove(diagonalBoard, who)
        if result != -1:
            returnValue = self.getPatern(diagonalBoard)
            returnValue = self.unDiagonal(diagonalBoard, len(newBoard))
            return self.findBestMove(returnValue)
        result = self.getCritcalMove(reverseDiagonalBoard, who)
        if result != -1:
            returnValue = self.getPatern(reverseDiagonalBoard)
            returnValue = self.unreverseDiagnoal(reverseDiagonalBoard, len(newBoard))
            return self.findBestMove(returnValue)
        return -1, -1

    def evaluationFromZero(self, line):
        if line[0] == 0:
            if line[1] == GAME_PLAYER:
                return 20
            elif line[1] == GAME_MANAGER:
                return 10
    def evaluationFromLast(self, line, val):
        if line[val] == 0:
            if line[val - 1] == GAME_PLAYER:
                return 20
            elif line[val -1] == GAME_MANAGER:
                return 10
    def evaluationFromOther(self, line, val):
        result = 0
        if line[val] == 0:
            if line[val - 1] == GAME_PLAYER:
                result += 20
            elif line[val - 1] == GAME_MANAGER:
                result += 10
            if line[val + 1] == GAME_PLAYER:
                result += 20
            elif line[val + 1] == GAME_MANAGER:
                result += 10
        return result

    def evaluationDirection(self, board):
        for i in board:
            val = 0
            if len(i) > 1:
                while val < len(i):
                    if val == 0:
                        i[val] += self.evaluationFromZero(i)
                    elif val == len(i) - 1:
                        i[val] += self.evaluationFromLast(i, val)
                    else:
                        i[val] += self.evaluationFromOther(i, val)
                    val += 1

    def mergeList(self, src, cpy):
        return [x + y for x, y in zip(src, cpy)]

    def merge(self, newBoard, verticalBoard, diagonalBoard, reverseDiagonalBoard):
        result = []
        for i in range(len(newBoard)):
            line = []
            line = self.mergeList(newBoard[i], verticalBoard[i])
            line = self.mergeList(newBoard[i], diagonalBoard[i])
            line = self.mergeList(newBoard[i], reverseDiagonalBoard[i])
            result.append(line)
        return result

    def evaluation(self, newBoard, verticalBoard, diagonalBoard, reverseDiagonalBoard):
        newBoard = self.evaluationDirection(newBoard)
        verticalBoard = self.evaluationDirection(verticalBoard)
        verticalBoard = self.unvertical(verticalBoard)
        diagonalBoard = self.evaluationDirection(diagonalBoard)
        diagonalBoard = self.unDiagonal(diagonalBoard)
        reverseDiagonalBoard = self.evaluationDirection(reverseDiagonalBoard)
        reverseDiagonalBoard = self.unreverseDiagnoal(reverseDiagonalBoard)
        resultBoard = self.merge(newBoard, verticalBoard, diagonalBoard, reverseDiagonalBoard)
        return self.findBestMove(resultBoard)

    def play(self, board):
        if self.boardIsEmpty(board):
            middle = ceil(len(board)/2)
            return [middle, middle]
        newBoard, verticalBoard, diagonalBoard, reverseDiagonal = self.getAllCopy(board)
        self.createPatterns()
        x, y = self.importantMove(GAME_PLAYER, newBoard, diagonalBoard, reverseDiagonal, verticalBoard)
        if x != -1 and y != -1:
            return x, y
        x, y = self.importantMove(GAME_MANAGER, newBoard, diagonalBoard, reverseDiagonal, verticalBoard)
        if x != -1 and y != -1:
            return x, y
        return self.evaluation(newBoard, verticalBoard, diagonalBoard, reverseDiagonal)