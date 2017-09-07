class operators():
    op = {}
    def init(self):
        self.op = {"+": self.sum, "-": self.sub, "*": self.mul, "/": self.div}
    def sum(self, a, b):
        a = int(a)
        b = int(b)
        return a+b
    def sub(self, a, b):
        a = int(a)
        b = int(b)
        return a-b
    def mul(self, a, b):
        a = int(a)
        b = int(b)
        return a*b
    def div(self, a, b):
        a = int(a)
        b = int(b)
        return a/b

operator = operators()
operator.init()

for i in range(3):
    str = input("Введите выражение: ")
    stack = []
    s = str.split(" ")
    for token in s:
        if token in operator.op:
            operand1, operand2 = int(stack.pop()), int(stack.pop())
            res = operator.op[token](operand2, operand1)
            stack.append(res)
        elif token:
            stack.append(int(token))
    print(stack.pop())