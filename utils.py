from antlr4 import *
import llvmlite.ir as ir


def getTypeFromText(name: str):
    if name == "int":
        return ir.IntType(32)
    elif name == "int16":
        return ir.IntType(32)
