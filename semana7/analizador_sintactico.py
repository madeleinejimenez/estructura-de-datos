class SyntaxAnalyzer:
    def __init__(self, expression):
        self.expression = expression
    
    def is_balanced(self):
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        for char in self.expression:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack or stack.pop() != matching[char]:
                    return False
        return len(stack) == 0

    def is_valid_expression(self):
        tokens = self.tokenize(self.expression)
        previous = None
        for token in tokens:
            if token in "+-*/":
                if not previous or previous in "+-*/({[":
                    return False
            elif token not in "({[":
                if previous and previous not in "+-*/({[":
                    return False
            previous = token
        return previous not in "+-*/"

    def tokenize(self, expression):
        import re
        return re.findall(r'\d+|[a-zA-Z]+|[()+\-*/{}[\]]', expression)

    def validate(self):
        if not self.is_balanced():
            return "Error: La expresión tiene un balanceo incorrecto de paréntesis, corchetes o llaves."
        if not self.is_valid_expression():
            return "Error: La expresión tiene operadores o operandos en una disposición incorrecta."
        return "La expresión es válida."

# Ejemplo de uso
expression = "5 * (3 + 2)"
analyzer = SyntaxAnalyzer(expression)
print(analyzer.validate())
