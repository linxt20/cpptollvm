from antlr4 import *
import llvmlite.ir as ir


def is_int(llvm_num):
    if llvm_num['type'] == ir.IntType(64) or llvm_num['type'] == ir.IntType(32) or llvm_num['type'] == ir.IntType(16) \
            or llvm_num['type'] == ir.IntType(8) or llvm_num['type'] == ir.IntType(1):
        return True
    return False


def int_convert(src, target, builder):
    if target['type'].width >= src['type'].width:  # 往大扩展
        if src['type'].width == 1:
            return_value = builder.zext(src['value'], target['type'])
            return {
                'type': target['type'],
                'signed': src['signed'],
                'value': return_value
            }
        else:
            if src['signed']:
                return_value = builder.sext(src['value'], target['type'])
            else:
                return_value = builder.zext(src['value'], target['type'])
            return {
                'type': target['type'],
                'signed': src['signed'],
                'value': return_value
            }
    else:
        return_value = builder.trunc(src['value'], target['type'])
        expression = {
            'type': target['type'],
            'signed': src['signed'],
            'value': return_value
        }
        return expression


def int_to_double(llvm_num, builder):
    if llvm_num['signed']:
        return_value = builder.sitofp(llvm_num['value'], ir.DoubleType())
    else:
        return_value = builder.uitofp(llvm_num['value'], ir.DoubleType())
    return {
        'type': ir.DoubleType(),
        'value': return_value
    }


def double_to_int(llvm_num, target, builder):
    if llvm_num['signed']:
        return_value = builder.fptosi(llvm_num['value'], target['type'])
    else:
        return_value = builder.fptoui(llvm_num['value'], target['type'])
    return {
        'type': target['type'],
        'value': return_value
    }


def to_bool(llvm_num, builder):
    if llvm_num['type'] == ir.DoubleType():
        return_value = builder.fcmp_ordered('!=', llvm_num['value'], ir.Constant(ir.IntType(1), 0))
    else:
        return_value = builder.icmp_signed('!=', llvm_num['value'], ir.Constant(ir.IntType(1), 0))
    expression = {
        'type': ir.IntType(1),
        'signed': True,
        'value': return_value
    }
    return expression


def assign_type_convert(left, right, builder):
    # 赋值语句中用的类型转换
    # 强制把右侧的类型转换为左侧的类型
    # 右侧的读进来，
    if left['type'] != right['type']:
        if is_int(left) and is_int(right):
            right = int_convert(right, left, builder)
        elif is_int(left) and is_int(right) == False:
            right = double_to_int(right, left, builder)
        elif is_int(left) == False and is_int(right):
            right = int_to_double(right, builder)
        else:
            pass
    return right


def expr_type_convert(left, right, builder):
    # left和right的符号类型不一致时，类型转换为一致，向大的类型转换
    # left,right可能的类型: int1,int8,int16,int32,int64,double...（暂时支持这几种）
    if left['type'] == right['type']:
        return left, right
    elif is_int(left) and is_int(right):
        if left['type'].width < right['type'].width:
            left = int_convert(left, right, builder)
        else:
            right = int_convert(right, left, builder)
    elif is_int(left) and right['type'] == ir.DoubleType():
        left = int_to_double(left, builder)
    elif left['type'] == ir.DoubleType() and is_int(right):
        right = int_to_double(right, builder)
    return left, right

