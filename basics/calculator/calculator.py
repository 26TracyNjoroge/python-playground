"""Calculator program"""

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self):
        number = int(input("Pick a number to add! "))
        self.result = self.result + number

    def subtract(self):
        number = int(input("Pick a number to subtract! "))
        self.result = self.result - number

    def get_result(self):
        return self.result

c = Calculator()
c.add()
c.subtract()
print(c.get_result())

    