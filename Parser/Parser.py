#!/usr/bin/python3

import sys

class Parser:
    def __init__(self) -> None:
        self.gameBoard = []
    def __start(self, size) -> None:
        pass
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
        

    def run(self) -> None:
        while True:
            line = input().split(' ')
            self.__parseCmd(line[0].upper(), line)
