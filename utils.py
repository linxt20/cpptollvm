from antlr4 import *
import llvmlite.ir as ir


def is_int(llvm_num):
    return llvm_num['type'] in [ir.IntType(64), ir.IntType(32), ir.IntType(16), ir.IntType(8), ir.IntType(1)]


def int_convert(src, target, builder):
    if target['type'].width >= src['type'].width:
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
    if left['type'] == right['type']:
        pass
    else:
        if is_int(left) and is_int(right):
            right = int_convert(right, left, builder)
        elif is_int(left) and is_int(right) is False:
            right = double_to_int(right, left, builder)
        elif is_int(left) is False and is_int(right):
            right = int_to_double(right, builder)
        else:
            pass
    return right


def expr_type_convert(left, right, builder):
    if left['type'] == right['type']:
        pass
    else:
        if is_int(left) and is_int(right):
            if left['type'].width < right['type'].width:
                left = int_convert(left, right, builder)
            else:
                right = int_convert(right, left, builder)
        elif is_int(left) and right['type'] == ir.DoubleType():
            left = int_to_double(left, builder)
        elif left['type'] == ir.DoubleType() and is_int(right):
            right = int_to_double(right, builder)
        else:
            pass
    return left, right
