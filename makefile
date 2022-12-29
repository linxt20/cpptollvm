CPPS = $(wildcard ./test/*.cpp)
OBJS = $(CPPS:.cpp=.ll)
antlr: grammar/cpp14Lexer.g4 grammar/cpp14Parser.g4
	antlr4 -Dlanguage=Python3 grammar/cpp14Lexer.g4 grammar/cpp14Parser.g4 -visitor -o src

test: $(OBJS)

$(OBJS):%.ll: %.cpp
	@echo "TEST $^"
	python main.py $^

clean:
	del test\*.ll