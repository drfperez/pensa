from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
import sys

with open(sys.argv[1],encoding='utf-8') as f:
    text=f.read()
program=Parser().parse(Lexer().tokenize(text))
Interpreter().block(program.lines)
