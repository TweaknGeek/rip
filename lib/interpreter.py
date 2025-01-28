import sys

from parser import program
import lexer

def interpret(file):
    with open(file) as f:
        data = f.read()
    tokens = lexer.lex(data)
    tree = program.parse(tokens)
    env = {}
    return eval(tree, env)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 interpreter.py <file>")
        sys.exit(1)
    interpret(sys.argv[1])
