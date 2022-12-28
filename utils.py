from antlr4 import *
import llvmlite.ir as ir


def isInt(llvmNum):
    if llvmNum['type'] == ir.IntType(64) or llvmNum['type'] == ir.IntType(32) or llvmNum['type'] == ir.IntType(16)\
            or llvmNum['type'] == ir.IntType(8) or llvmNum['type'] == ir.IntType(1):
        return True
    return False


def intConvert(src, target, Builder):
    if target['type'].width >= src['type'].width:  # 往大扩展
        if src['type'].width == 1:
            ValueToReturn = Builder.zext(src['value'], target['type'])
            return {
                'type': target['type'],
                'signed': src['signed'],
                'value': ValueToReturn
            }
        else:
            if src['signed']:
                ValueToReturn = Builder.sext(src['value'], target['type'])
            else:
                ValueToReturn = Builder.zext(src['value'], target['type'])
            return {
                'type': target['type'],
                'signed': src['signed'],
                'value': ValueToReturn
            }
    else:  # 往小了转换，其实是 undefined 行为
        ValueToReturn = Builder.trunc(src['value'], target['type'])
        return {
            'type': target['type'],
            'signed': src['signed'],
            'value': ValueToReturn
        }


def intToDouble(llvmNum, Builder):
    if llvmNum['signed']:
        ValueToReturn = Builder.sitofp(llvmNum['value'], ir.DoubleType())
    else:
        ValueToReturn = Builder.uitofp(llvmNum['value'], ir.DoubleType())
    return {
        'type': ir.DoubleType(),
        'value': ValueToReturn
    }


def doubleToInt(llvmNum, target, Builder):
    if llvmNum['signed']:
        ValueToReturn = Builder.fptosi(llvmNum['value'], target['type'])
    else:
        ValueToReturn = Builder.fptoui(llvmNum['value'], target['type'])
    return {
        'type': target['type'],
        'value': ValueToReturn
    }


def toBool(llvmNum, Builder):
    if llvmNum['type'] == ir.DoubleType():
        ValueToReturn = Builder.fcmp_ordered('!=', llvmNum['value'], ir.Constant(ir.IntType(1), 0))
    else:
        ValueToReturn = Builder.icmp_signed('!=', llvmNum['value'], ir.Constant(ir.IntType(1), 0))
    return {
        'type': ir.IntType(1),
        'signed': True,
        'value': ValueToReturn
    }


def exprTypeConvert(left, right, Builder):
    # left和right的符号类型不一致时，类型转换为一致，向大的类型转换
    # left,right可能的类型: int1,int8,int16,int32,int64,double...（暂时支持这几种）
    if left['type'] == right['type']:
        return left, right
    elif isInt(left) and isInt(right):
        if left['type'].width < right['type'].width:
            left = intConvert(left, right, Builder)
        else:
            right = intConvert(right, left, Builder)
    elif isInt(left) and right['type'] == ir.DoubleType():
        left = intToDouble(left, Builder)
    elif left['type'] == ir.DoubleType() and isInt(right):
        right = intToDouble(right, Builder)
    return left, right


def getTypeFromText(name: str):
    if name == "int":
        return ir.IntType(32)
    elif name == "int16":
        return ir.IntType(32)
