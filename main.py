#!/usr/bin/python3

from Parser.Parser import Parser
from Ai.Ai import Ai

if __name__ == '__main__':
    ai = Ai()
    parser = Parser()
    parser.run(ai)
