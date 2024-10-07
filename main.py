class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, other: float) -> float:
        return self.number + other

    def sub(self, other: float) -> float:
        return self.number - other

    def div(self, other: float) -> float:
        if other == 0:
            raise ValueError("error.")
        return self.number / other

    def mul(self, other: float) -> float:
        return self.number * other

    def calculate(self, other: float) -> float:
        if self.symbol == "+":
            return self.add(other)
        elif self.symbol == "-":
            return self.sub(other)
        elif self.symbol == "/":
            return self.div(other)
        elif self.symbol == "*":
            return self.mul(other)
        else:
            raise ValueError("error: " + self.symbol)
    
    
 