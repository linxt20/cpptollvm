lexer grammar cpp14Lexer;

LT: '<';
GT: '>';
DQUOTE: '"';
SQUOTE: '\'';
LBRACE: '{';
RBRACE: '}';
LSQUARE: '[';
RSQUARE: ']';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
SEMI: ';';
DOT: '.';
COLON: ':';

// operators
ASSIGN: '=';
ADD: '+';
ADD_ASSIGN: '+=';
AND: '&&';
BITAND: '&';
BITOR: '|';
SUB: '-';
SUB_ASSIGN: '-=';
MULT: '*';
MULT_ASSIGN: '*=';
DIV: '/';
DIV_ASSIGN: '/=';
MOD: '%';
MOD_ASSIGN: '%=';
LSHIFT: '<<';
LSHIFT_ASSIGN: '<<=';
RSHIFT: '>>';
RSHIFT_ASSIGN: '>>=';
EQ: '==';
DOTS: '...';
LEQ: '<=';
GEQ: '>=';
ARROW: '->';
PLUS_PLUS: '++';
MINUS_MINUS: '--';
COMPL: '~';
NOT: '!';
NOT_EQ: '!=';
OR: '||';
XOR: '^';

// keywords
BOOL: 'bool';
BREAK: 'break';
CASE: 'case';
CHAR: 'char';
CLASS: 'class';
CONST: 'const';
CONTINUE: 'continue';
DEFAULT: 'default';
DELETE: 'delete';
DO: 'do';
DOUBLE: 'double';
ELSE: 'else';
FALSE_: 'false';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
LONG: 'long';
NEW: 'new';
NULLPTR: 'nullptr';
PRIVATE: 'private';
PROTECTED: 'protected';
PUBLIC: 'public';
RETURN: 'return';
SHORT: 'short';
SIGNED: 'signed';
SIZEOF: 'sizeof';
STRUCT: 'struct';
SWITCH: 'switch';
THIS: 'this';
TRUE_: 'true';
TYPEDEF: 'typedef';
UNSIGNED: 'unsigned';
VOID: 'void';
WHILE: 'while';

// identifier
fragment DIGIT: '0' ..'9';
fragment OCTALDIGIT: '0' ..'7';
fragment HEXDIGIT: '0' ..'9' | 'A' ..'F' | 'a' ..'f';
fragment NONDIGIT: '_' | 'a' ..'z' | 'A' ..'Z';
fragment HEXQUAD: HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT;
WHITESPACE: (' ' | '\t' | '\f') -> skip;
NEWLINE: ('\r' | '\n') -> skip;
LINE_COMMENT:	'//' (~('\n' | '\r'))* ('\r'? '\n') -> channel(HIDDEN);
COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
Identifier: NONDIGIT (DIGIT | NONDIGIT)*;
StringLiteral:DQUOTE SChar* DQUOTE;
CharacterLiteral: SQUOTE CChar SQUOTE;
DecimalLiteral: '0' | (('1' ..'9') ('0' ..'9')*);
FloatingLiteral:	 (DigitSequence DecimalExponent )
	| (DigitSequence DOT DecimalExponent)
        | (DigitSequence DOT DigitSequence DecimalExponent?);
DigitSequence: ('0' ..'9')+;
DecimalExponent: ('e' | 'E') (ADD | SUB)? DigitSequence;

// Character literals
SChar: ~["\\\r\n] | Escapesequence | Universalcharactername;
CChar: ~ ['\\\r\n] | Escapesequence | Universalcharactername;
Escapesequence:	Simpleescapesequence
	| Octalescapesequence
	| Hexadecimalescapesequence;
Simpleescapesequence:
	'\\\''
	| '\\"'
	| '\\?'
	| '\\\\'
	| '\\a'
	| '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| ('\\' ('\r' '\n'? | '\n'))
	| '\\t'
	| '\\v';
Octalescapesequence:	'\\' OCTALDIGIT
	| '\\' OCTALDIGIT OCTALDIGIT
	| '\\' OCTALDIGIT OCTALDIGIT OCTALDIGIT;
Hexadecimalescapesequence: '\\x' HEXDIGIT+;
Universalcharactername: '\\u' HEXQUAD | '\\U' HEXQUAD HEXQUAD;
