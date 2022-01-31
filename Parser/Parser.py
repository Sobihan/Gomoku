#!/usr/bin/python3

import sys

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
    def __turn(self, position) -> None:
        pass
    def __begin(self) -> None:
        pass
    def __end(self) -> None:
        sys.exit(0)
    def __about(self) -> None:
        print("name=\"SLGBrain\", version=\"1.0\", author=\"SLG\", country=\"USA\"", flush=True, end='\n')
    def __parseCmd(self, cmd, args) -> None:
        if (cmd == "START"):
            self.__start(args[1])
        elif (cmd == "TURN"):
            self.__turn(args[1])
        elif (cmd == "BEGIN"):
            self.__begin()
        elif (cmd == "END"):
            self.__end()
        elif (cmd == "ABOUT"):
            self.__about()
        elif (cmd == "DEBUG"):
            self.__debug()
        

    def run(self) -> None:
        while True:
            line = input().split(' ')
            self.__parseCmd(line[0].upper(), line)
