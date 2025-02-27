import operator

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    def construct_tree(self, postfix):
        stack = []
        for token in postfix:
            if token.isdigit():
                stack.append(Node(int(token)))
            else:
                node = Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack[0]

    def evaluate(self, root):
        if root.value in self.operators:
            left_val = self.evaluate(root.left)
            right_val = self.evaluate(root.right)
            return self.operators[root.value](left_val, right_val)
        return root.value

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    
    while stack:
        output.append(stack.pop())

    return output

# Función principal para evaluar expresiones
def evaluate_expression(expression):
    postfix = infix_to_postfix(expression)
    tree = ExpressionTree()
    root = tree.construct_tree(postfix)
    return tree.evaluate(root)

# Ejemplo de uso
expression = "3 + 5 * (2 - 8)"
result = evaluate_expression(expression)
print(f"Resultado de '{expression}': {result}")
