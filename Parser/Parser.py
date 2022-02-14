#!/usr/bin/python3

import sys

GAME_MANAGER = 2
GAME_PLAYER = 1

class Parser:
    def __init__(self) -> None:
        self.gameBoard = []

    def __start(self, value) -> None:
        size = int(value)
        if (size < 5):
            print('ERROR unvalid_size', flush=True, end='\n')
            return
        for i in range(0, size):
            line = [0] * size
            self.gameBoard.append(line)
        print('OK', flush=True, end='\n')

    def __debug(self) -> None:
        print(self.gameBoard)

    def __turn(self, position, ai) -> None:
        x, y = list(map(int, position.split(','))) # "3, 2" -> 3, 2
        self.gameBoard[y][x] = GAME_MANAGER
        x, y = ai.play(self.gameBoard)
        self.gameBoard[y][x] = GAME_PLAYER
        self.__print(x, y)

    def __begin(self, ai) -> None:
        x, y = ai.play(self.gameBoard)
        self.gameBoard[y][x] =  GAME_PLAYER
        self.__print(x, y)
        pass
    def __board(self, ai) -> None:
        for line in sys.stdin:
            if (line.rstrip() != "DONE"):
                x, y, owner = list(map(int, line.split(',')))
                self.gameBoard[y][x] = owner
            else:
                x, y = ai.play(self.gameBoard)
                self.gameBoard[y][x] = GAME_PLAYER
                self.__print(x, y)
                break
    def __end(self) -> None:
        sys.exit(0)
    def __print(self, x, y) -> None:
        print(str(x) + "," + str(y), flush=True, end='\n')
    def __about(self) -> None:
        print("name=\"SLGBrain\", version=\"1.0\", author=\"SLG\", country=\"USA\"", flush=True, end='\n')
    def __parseCmd(self, cmd, args, ai) -> None:
        if (cmd == "START"):
            self.__start(args[1])
        elif (cmd == "TURN"):
            self.__turn(args[1], ai)
        elif (cmd == "BEGIN"):
            self.__begin(ai)
        elif (cmd == "BOARD"):
            self.__board(ai)
        elif (cmd == "END"):
            self.__end()
        elif (cmd == "ABOUT"):
            self.__about()
        elif (cmd == "DEBUG"):
            self.__debug()
        

    def run(self, ai) -> None:
        while True:
            line = input().split(' ')
            self.__parseCmd(line[0].upper(), line, ai)
