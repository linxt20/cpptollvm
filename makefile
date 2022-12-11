CPPS = $(wildcard ./test/*.cpp)
OBJS = $(CPPS:.cpp=.txt)
antlr: grammar/cpp14Lexer.g4 grammar/cpp14Parser.g4
	antlr4 -Dlanguage=Python3 grammar/cpp14Lexer.g4 grammar/cpp14Parser.g4 -visitor -o src

test: $(OBJS)

$(OBJS):%.txt: %.cpp
	@echo "TEST $^"
	python main.py $^

cleantxt:
	del test\*.json