from antlr4 import *
import sys, os
import ast
import json

from src.cpp14Lexer import cpp14Lexer
from src.cpp14Parser import cpp14Parser
from src.cpp14ParserListener import cpp14ParserListener as cpp14Listener
from src.cpp14ParserVisitor import cpp14ParserVisitor as cpp14Visitor

jsonString = ""
# global lasttype
def translate(text:str):
    text = text.replace("\\","\\\\")
    text = text.replace("\"","\\\"")
    if(len(text)>50):
        text = text[0:49]+"...(too long)"
    return text

def printTree(tree,k):
    global jsonString
    content = translate(tree.getText())
    if tree.getChildCount() == 0 :
        jsonString += ("{ \"" + f"type\": \"{content}\",  \"content\": \"{content}\", \"children\": []" + "},")
        return
    jsonString += ("{ \"" + f"type\": \"{str(type(tree))[36:-9]}\",  \"content\": \"{content}\",  \"children\": [")
    for i in range(tree.getChildCount()):
        printTree(tree.getChild(i), k + 1)
    jsonString += ("]},")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py (input_filename)")
        exit(0)
    else:
        filename = sys.argv[1]
        output_filename = filename.split(".")[0]+"parser.json"
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
        #             f.write(str(token)+' ')
        # parser
        parser = cpp14Parser(stream)
        tree = parser.translationUnit()
        printTree(tree,0)
        # print(output_filename)
        # print(jsonString)

        # print(tree)
        # print(tree.toStringTree(recog=parser))
        # if(output_filename):
        #     with open(output_filename, 'w') as f:
        #         f.write(str(tree.toStringTree(recog=parser)))
        jsonString = jsonString.replace(",]","]")
        jsonString = jsonString[0:len(jsonString)-1]

        final_json = json.loads(jsonString)

        final_string=json.dumps(final_json,indent=4)
        if(output_filename):
            with open(output_filename, 'w') as f:
                f.write(final_string)
        exit(0)