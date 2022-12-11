from antlr4 import *
import sys, os
import ast

from src.cpp14Lexer import cpp14Lexer
from src.cpp14Parser import cpp14Parser
from src.cpp14ParserListener import cpp14ParserListener as cpp14Listener
from src.cpp14ParserVisitor import cpp14ParserVisitor as cpp14Visitor

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py (input_filename)")
        exit(0)
    else:
        filename = sys.argv[1]
        output_filename = filename.split(".")[0]+"parser.txt"
        input_stream = FileStream(filename)
        # print(input_stream)
        # lexer
        lexer = cpp14Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        # stream.fill()
        # tokennum = stream.getNumberOfOnChannelTokens()
        # tokens = stream.getTokens(0,tokennum)

        # if(output_filename):
        #     with open(output_filename, 'w') as f:
        #         for token in tokens:
        #             f.write(str(token)+'\n')
        # parser
        parser = cpp14Parser(stream)
        tree = parser.translationUnit()
        # print(tree)
        # print(tree.toStringTree(recog=parser))
        if(output_filename):
            with open(output_filename, 'w') as f:
                f.write(str(tree.toStringTree(recog=parser)))
        exit(0)