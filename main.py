from antlr4 import *
import sys, os
import ast

from src.cpplexer import cpplexer
from src.cppparser import cppparser
from src.cppparserListener import cppparserListener as cpp20Listener
from src.cppparserVisitor import cppparserVisitor as cpp20Visitor

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py (input_filename)")
        exit(0)
    else:
        filename = sys.argv[1]
        output_filename = filename.split(".")[0]+"lexer.txt"
        input_stream = FileStream(filename)
        # print(input_stream)
        # lexer
        lexer = cpplexer(input_stream)
        stream = CommonTokenStream(lexer)
        # stream.fill()
        # tokennum = stream.getNumberOfOnChannelTokens()
        # tokens = stream.getTokens(0,tokennum)

        # if(output_filename):
        #     with open(output_filename, 'w') as f:
        #         for token in tokens:
        #             f.write(str(token)+'\n')
        # parser
        parser = cppparser(stream)
        tree = parser.translationUnit()
        # print(tree.toStringTree(recog=parser))
        if(output_filename):
            with open(output_filename, 'w') as f:
                f.write(str(tree.toStringTree(recog=parser)))
        exit(0)