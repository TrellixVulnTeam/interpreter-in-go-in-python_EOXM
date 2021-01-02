from tokenType import TokenType, Token, lookup_identifier_token_type


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self._read_char()

    def next_token(self):
        self._skip_whitespace()

        if self.ch == '=':
            token = Token(TokenType.Assign, self.ch)
        elif self.ch == ';':
            token = Token(TokenType.Semicolon, self.ch)
        elif self.ch == '(':
            token = Token(TokenType.LeftParen, self.ch)
        elif self.ch == ')':
            token = Token(TokenType.RightParen, self.ch)
        elif self.ch == ',':
            token = Token(TokenType.Comma, self.ch)
        elif self.ch == '+':
            token = Token(TokenType.Plus, self.ch)
        elif self.ch == '{':
            token = Token(TokenType.LeftBrace, self.ch)
        elif self.ch == '}':
            token = Token(TokenType.RightBrace, self.ch)
        elif self.ch == '\0':
            token = Token(TokenType.EOF, "")
        else:
            if self._is_letter(self.ch):
                literal = self._read_identifier()
                return Token(lookup_identifier_token_type(literal), literal)
            elif self._is_digit(self.ch):
                return Token(TokenType.Int, self._read_number())
            else:
                token = Token(TokenType.Illegal, self.ch)

        self._read_char()
        return token

    def _skip_whitespace(self):
        while str.isspace(self.ch):
            self._read_char()

    def _read_char(self):
        if self.readPosition >= len(self.input):
            self.ch = "\0"
        else:
            self.ch = self.input[self.readPosition]

        self.position = self.readPosition
        self.readPosition += 1

    def _read_identifier(self):
        starting_position = self.position
        while self._is_letter(self.ch):
            self._read_char()
        return self.input[starting_position:self.position]

    def _read_number(self):
        starting_position = self.position
        while self._is_digit(self.ch):
            self._read_char()
        return self.input[starting_position:self.position]

    @staticmethod
    def _is_letter(ch):
        return "a" <= ch <= "z" or "A" <= ch <= "Z" or ch == "_"

    @staticmethod
    def _is_digit(ch):
        return "0" <= ch <= "9"
