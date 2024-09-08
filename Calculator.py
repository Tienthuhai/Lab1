class Calculator:
    def __init__(self,*args):
        self.args = args
    
    @staticmethod
    def add(*args):
        return sum(args)
    
    @staticmethod
    def multiply(*args):
        value = args[0]
        for num in args:
            value *= num
        return value
    @staticmethod
    def divide(*args):
        value = args[0]
        for num in args[1:]:
            value /= num
        return value
    @staticmethod
    def subtract(*args):
        value = args[0]
        for num in args[1:]:
            value = value - num
        return value
    
print(Calculator.add(5, 10, 4)) 
print(Calculator.multiply(1, 2, 3, 5)) 
print(Calculator.divide(100, 2)) 
print(Calculator.subtract(90, 20, -50, 43, 7)) 
