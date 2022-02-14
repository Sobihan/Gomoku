#!/usr/bin/python3
from math import ceil
from operator import ne

GAME_MANAGER = 2
GAME_PLAYER = 1

WIN_PATTERN_1 = [0, 1, 1, 1, 1]
WIN_PATTERN_2 = [1, 1, 1, 1, 0]

WIN_PATTERN_3 = [0, 1, 1, 1, 0]
WIN_PATTERN_4 = [0, 1, 0, 1, 1]
WIN_PATTERN_5 = [1, 0, 1, 1, 0]

WIN_PATTERN_6 = [1, 1, 1, 0, 1]
WIN_PATTERN_7 = [1, 1, 0, 1, 1]
WIN_PATTERN_8 = [1, 0, 1, 1, 1]

LOOSE_PATTERN_1 = [0, 2, 2, 2, 2]
LOOSE_PATTERN_2 = [2, 2, 2, 2, 0]

LOOSE_PATTERN_3 = [0, 2, 2, 2, 0]
LOOSE_PATTERN_4 = [0, 2, 0, 2, 2]
LOOSE_PATTERN_5 = [2, 0, 2, 2, 0]

LOOSE_PATTERN_6 = [2, 2, 2, 0, 2]
LOOSE_PATTERN_7 = [2, 2, 0, 2, 2]
LOOSE_PATTERN_8 = [2, 0, 2, 2, 2]

LOOSE_PATTERN_9 = [2, 0, 2, 2]

class Ai:
    def __init__(self) -> None:
         self.createPatterns()
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
        [0, 2, 2, 2, 0],
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
                if maximum < cpy[x][y]:
                    maximum = cpy[x][y]
                    bstMove = [x, y]
        if not bstMove:
           return -1, -1
        return bstMove[1], bstMove[0]

    def boardIsEmpty(self, board):
        x, y = self.findBestMove(board)
        if x == -1 and y == -1:
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
            board = [newBoard[i:] + r + newBoard[:i] for i, r in enumerate(self.rows(board))]
        else:
            board = [newBoard[:i] + r + newBoard[i:] for i, r in enumerate(self.rows(board))]

        return [[c for c in r if c is not None] for r in self.cols(board)]

    def unvertical(self, board):
        return self.vertical(board)

    def getAllCopy(self, board):
        newBoard = self.copy(board)
        verticalBoard = self.vertical(board)
        diagonalBoard = self.diagonal(board, False)
        reverseDiagonal = self.diagonal(board, True)
        return [newBoard, verticalBoard, diagonalBoard, reverseDiagonal]

    def match(self, board, pattern):
        for x in range(len(board)):
            if board[x] == pattern[0] and board[x:x+len(pattern)] == pattern:
                return True
        return False

    def getCritcalMove(self, b, player):
        for it in b:
            if (player == 1):
                if (self.match(it, WIN_PATTERN_1)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_2)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_3)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_4)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_5)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_6)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_7)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_8)):
                    return b.index(it)
            else:
                if (self.match(it, LOOSE_PATTERN_1)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_3)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_4)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_5)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_6)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_7)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_8)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_9)):
                    return b.index(it)
        for it in b:
            if (player == 1):
                if (self.match(it, WIN_PATTERN_1)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_2)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_3)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_4)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_5)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_6)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_7)):
                    return b.index(it)
                if (self.match(it, WIN_PATTERN_8)):
                    return b.index(it)
            else:
                if (self.match(it, LOOSE_PATTERN_2)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_3)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_4)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_5)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_6)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_7)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_8)):
                    return b.index(it)
                if (self.match(it, LOOSE_PATTERN_9)):
                    return b.index(it)
        return -1
        # if who == GAME_PLAYER:
        #     for b in board:
        #         for i in self.winnerPatterns:
        #             if self.match(b, i):
        #                 return board.index(b)
        # else:
        #     for b in board:
        #         for i in self.looserPatterns:
        #             if self.match(b, i):
        #                 return board.index(b)
        # if who == GAME_PLAYER:
        #     for b in board:
        #         for i in self.winnerPatterns:
        #             if self.match(b, i):
        #                 return board.index(b)
        # else:
        #     for b in board:
        #         for i in self.looserPatterns:
        #             if self.match(b, i):
        #                 return board.index(b)
        # return -1
    
    def getValue(self, board, pattern):
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
    
    # def importantMove(self, who, newBoard, diagonalBoard, reverseDiagonalBoard, verticalBoard):
    def importantMove(self,cpy, vert, diag, back_diag, player):
        tmp = self.getCritcalMove(cpy, player)
        if (tmp != -1):
            b = self.getPatern(cpy, tmp, player)
            return self.findBestMove(b)
        tmp = self.getCritcalMove(vert, player)
        if (tmp != -1):
            b = self.getPatern(vert, tmp, player)
            b = self.unvertical(b)
            return self.findBestMove(b)
        tmp = self.getCritcalMove(diag, player)
        if (tmp != -1):
            b = self.getPatern(diag, tmp, player)
            b = self.unDiagonal(diag, len(cpy))
            return self.findBestMove(b)
        tmp = self.getCritcalMove(back_diag, player)
        if (tmp != -1):
            b = self.getPatern(back_diag, tmp, player)
            b = self.unreverseDiagnoal(back_diag, len(cpy))
            return self.findBestMove(b)
        return -1, -1

    def evaluationFromZero(self, line):
        if line[0] == 0:
            if line[1] == GAME_PLAYER:
                return 20
            if line[1] == GAME_MANAGER:
                return 10
        return 0
    def evaluationFromLast(self, line, val):
        if line[val] == 0:
            if line[val - 1] == GAME_PLAYER:
                return 20
            if line[val -1] == GAME_MANAGER:
                return 10
        return 0
    def evaluationFromOther(self, line, val):
        result = 0
        if line[val] == 0:
            if line[val - 1] == GAME_PLAYER:
                result += 20
            if line[val - 1] == GAME_MANAGER:
                result += 10
            if line[val + 1] == GAME_PLAYER:
                result += 20
            if line[val + 1] == GAME_MANAGER:
                result += 10
        return result

    def evaluationDirection(self, b):
        for it in b:
            tmp = 0
            if (len(it) > 1):
                while (tmp < len(it)):
                    if (tmp == 0):
                        it[tmp] += self.evaluationFromZero(it)
                    elif (tmp == len(it) - 1):
                        it[tmp] += self.evaluationFromLast(it, tmp)
                    else:
                        it[tmp] += self.evaluationFromOther(it, tmp)
                    tmp += 1
        return b

    def sum_list(self, src, cpy):
        return [x + y for x, y in zip(src, cpy)]

    def sum(self, newBoard, verticalBoard, diagonalBoard, reverseDiagonalBoard):
        result = []
        for i in range(len(newBoard)):
            line = []
            line = self.mergeList(newBoard[i], verticalBoard[i])
            line = self.mergeList(newBoard[i], diagonalBoard[i])
            line = self.mergeList(newBoard[i], reverseDiagonalBoard[i])
            result.append(line)
        return result

    def sum_axis(self,cpy, vert, diag, back_diag):
        r = []
        tmp = 0
        while (tmp < len(cpy)):
            l = []
            l = self.sum_list(cpy[tmp], vert[tmp])
            l = self.sum_list(l, diag[tmp])
            l = self.sum_list(l, back_diag[tmp])
            r.append(l)
            tmp += 1
        return r

    def evaluation(self, newBoard, verticalBoard, diagonalBoard, reverseDiagonalBoard):
        newBoard = self.evaluationDirection(newBoard)
        verticalBoard = self.evaluationDirection(verticalBoard)
        verticalBoard = self.unvertical(verticalBoard)
        diagonalBoard = self.evaluationDirection(diagonalBoard)
        diagonalBoard = self.unDiagonal(diagonalBoard, len(newBoard))
        
        reverseDiagonalBoard = self.evaluationDirection(reverseDiagonalBoard)
        reverseDiagonalBoard = self.unreverseDiagnoal(reverseDiagonalBoard, len(newBoard))
        
        #resultBoard = self.merge(newBoard, verticalBoard, diagonalBoard, reverseDiagonalBoard)
        resultBoard = self.sum_axis(newBoard, verticalBoard, diagonalBoard, reverseDiagonalBoard)

        return self.findBestMove(resultBoard)

    def play(self, board):
        if self.boardIsEmpty(board):
            middle = ceil(len(board)/2)
            return [middle, middle]
        newBoard, verticalBoard, diagonalBoard, reverseDiagonal = self.getAllCopy(board)
        x, y = self.importantMove(newBoard, verticalBoard, diagonalBoard, reverseDiagonal, GAME_PLAYER)
        if x != -1 and y != -1:
            return x, y
        x, y = self.importantMove(newBoard, verticalBoard, diagonalBoard, reverseDiagonal, GAME_MANAGER)
        if x != -1 and y != -1:
            return x, y        
        return self.evaluation(newBoard, verticalBoard, diagonalBoard, reverseDiagonal)