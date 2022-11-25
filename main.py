from antlr4 import *
import sys,os
import ast

from src.cpplexer import cpplexer

if __name__ == "__main__":
    # if(len(sys.argv) < 3):
    #     print("too few arguments.",flush=True)
    #     print("usage: python3 main.py <inputfilename> <outputfilename>",flush=True)
    #     exit(1)
    # else:
        # filename = sys.argv[1]
    #     outputfilename = sys.argv[2] 
    # print(filename)      
    filename = sys.argv[1]
    print(filename)
    input_stream = FileStream(filename)
    print(input_stream)
    # lexer
    lexer = cpplexer(input_stream)
    print(lexer)
    stream = CommonTokenStream(lexer)
    print(stream)