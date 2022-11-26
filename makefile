antlr:
	antlr4 -Dlanguage=Python3 grammar/cpplexer.g4 -o src

cleantxt:
	del test\*.txt