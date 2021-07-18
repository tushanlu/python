class Calculator(object):
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b


print(Calculator.add(2, 3))
print(Calculator.minus(2, 3))
print(Calculator.mul(2, 3))