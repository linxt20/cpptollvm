CPPS = $(wildcard ./test/*.cpp)
OBJS = $(CPPS:.cpp=.ll)
CPPS2 = $(wildcard ./test/other_test/*.cpp)
OBJS2 = $(CPPS2:.cpp=.ll)

antlr: grammar/cpp14Lexer.g4 grammar/cpp14Parser.g4
	antlr4 -Dlanguage=Python3 grammar/cpp14Lexer.g4 grammar/cpp14Parser.g4 -visitor -o src

test: $(OBJS) $(OBJS2)

$(OBJS):%.ll: %.cpp
	@echo "TEST $^"
	python main.py $^

$(OBJS2):%.ll: %.cpp
	@echo "TEST $^"
	python main.py $^

clean:
	del test\*.ll test\other_test\*.ll