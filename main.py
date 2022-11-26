from antlr4 import *
import sys,os
import ast

from src.cpplexer import cpplexer

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py (input_filename)")
        exit(0)
    else:
        filename = sys.argv[1]
        output_filename = filename.split(".")[0]+"lexer.txt"
        input_stream = FileStream(filename)
        print(input_stream)
        # lexer
        lexer = cpplexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()
        tokennum = stream.getNumberOfOnChannelTokens()
        tokens = stream.getTokens(0,tokennum)
        for token in tokens:
            print(token)