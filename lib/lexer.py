from antlr4 import Lexer

class GambitLexer(Lexer):
    def __init__(self, input):
        super().__init__(input)
        self._interp = None
        self._state = None
        self._errHandler = None
        self._ctx = None

    def nextToken(self):
        while True:
            self._interp = self.interpreter
            self._state = self.getState()
            self._errHandler = self.errorHandler

            tok = super().nextToken()

            if tok.type == GambitParser.EOF:
                break

            self._interp = None
            self._state = None
            self._errHandler = None

            return tok
