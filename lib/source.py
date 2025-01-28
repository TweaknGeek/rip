# source.py
from antlr4 import FileStream, CommonTokenStream
import parser
import lexer
import visitor

class Source(object):

    def __init__(self, input_file):
        input_stream = FileStream(input_file)
        lexer = lexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = parser(tokens)
        tree = parser.program()
        self.visitor = visitor()
        self.visitor.visit(tree)

