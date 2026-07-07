class Lexer:
    def tokenize(self,text):
        return [l.rstrip() for l in text.splitlines()]
