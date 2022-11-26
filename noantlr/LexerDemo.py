import sys


white_char = [' ', '\t', '\n']
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
ALPHAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
normal_symbol = ['[', '{', '(', ',', ';', '}', ')', ']', '.', '&']
operators = ['+', '-', '*', '/', '%', '!', '=', '<', '>']
reserve_words = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
                 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'return', 'short', 'signed', 'sizeof', 'static',
                 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']


class Token:
    def __init__(self, token_name, attribute_value=None):
        # 所有的token name：'reserve_words', 'ID', 'integer', 'float', 'string', 'char', 'EOF',
        #                 '[', '{', '(', ',', ';', '}', ')', ']', '.', '&', '+', '-', '*', '/', '%', '!', '=', '<', '>',
        #                 '++', '--', '+=', '-=', '*=', '/=', '%=', '!=', '==', '<=', '>='
        self.token_name = token_name
        self.attribute_value = attribute_value


class StringStream:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.i = 0
        self.txt = self.file.read()
        self.txt_len = len(self.txt)

    def next_char(self):
        if self.i == self.txt_len:
            return ''
        self.i += 1
        return self.txt[self.i - 1]

    def back_char(self):
        self.i -= 1


def next_token(s):
    state = '0'  # 自动机所有状态：0, alpha, integer, float, error, normal_symbol, operator, string, char（部分状态简化了）
    token = ''  # 这个token似乎跟一个系统库token重名了，不知道会不会有影响..?

    while state != 'error':
        current = s.next_char()
        if current == '':
            if state in ['0', 'alpha', 'integer', 'float', 'operator', 'logic_op']:
                break
            elif state in ['string', 'char']:
                state = 'error'
                break

        if state == '0':
            if current in white_char:
                continue
            elif current in alphas + ALPHAS + ['_']:
                state = 'alpha'
                token += current
            elif current in integers:
                state = 'integer'
                token += current
            elif current in normal_symbol:
                state = 'normal_symbol'
                token += current
                break
            elif current in operators:
                state = 'operator'
                token += current
            elif current == '"':
                state = 'string'
                token += '"'
            elif current == "'":
                state = 'char'
                token += "'"
            else:
                state = 'error'
                token += current

        elif state == 'alpha':
            if current in alphas + ALPHAS + ['_'] + integers:
                token += current
            else:
                s.back_char()
                break

        elif state == 'integer':
            if current in integers:
                token += current
            elif current == '.':
                state = 'float'
                token += current
            elif current in alphas + ALPHAS + ['_', '[', '{', "'", '"', '&']:
                state = 'error'
                token += current
            else:
                s.back_char()
                break

        elif state == 'float':
            if current in integers:
                token += current
            elif current in alphas + ALPHAS + ['_', '[', '{', "'", '"', '&', '.']:
                state = 'error'
                token += current
            else:
                s.back_char()
                break

        elif state == 'operator':
            if token == '+' and current == '+':
                token = '++'
                break
            if token == '-' and current == '-':
                token = '--'
                break

            if current != '=':
                s.back_char()
                break
            else:
                token += '='
                break

        elif state == 'string':
            if current != '"':
                token += current
            else:
                token += current
                break

        elif state == 'char':
            if current != "'":
                token += current
            else:
                token += current
                break

    if state == 'error':
        print('Lexer:未识别的标识符：' + str(token))
        exit(1)

    elif state == '0':
        print('Lexer work done')
        return Token('EOF')
    elif state == 'alpha':
        if token in reserve_words:
            return Token('reserve_words', token)
        return Token('ID', token)
    elif state == 'integer':
        return Token('integer', token)
    elif state == 'float':
        return Token('float', token)
    elif state in ['normal_symbol', 'operator', 'logic_op']:
        return Token(token)
    elif state == 'string':
        return Token('string', token)
    elif state == 'char':
        return Token('char', token)
    else:
        print('Lexer bug!')  # 词法分析器存在bug
        print('state == ' + str(state))
        exit(1)


if __name__ == '__main__':
    S = StringStream(sys.argv[1])
    output = sys.argv[2]
    output_file = open(output, "w")

    while 1:
        t = next_token(S)
        if t.token_name == 'EOF':
            exit(0)
        if t.attribute_value is not None:
            output_file.write('<' + t.token_name + ',' + t.attribute_value + '>\n')
        else:
            output_file.write('<' + t.token_name + ',>\n')
