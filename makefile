CPPS = $(wildcard ./test/*.cpp)
OBJS = $(CPPS:.cpp=.txt)
antlr: grammar/cpplexer.g4
	antlr4 -Dlanguage=Python3 grammar/cpplexer.g4 -o src

test: $(OBJS)

$(OBJS):%.txt: %.cpp
	@echo "TEST $^"
	python main.py $^

cleantxt:
	del test\*.txt