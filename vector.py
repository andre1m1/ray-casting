import math

class Vector2:

    def __init__(self, x : float = 0.0, y : float = 0.0) -> None:
        self.x : float = x
        self.y : float = y


    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"
    
    def sub(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def add(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def mul(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def mod(self) -> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def abs(self):
        return Vector2(math.fabs(self.x), math.fabs(self.y))
    
    def square_dist(self, other) -> float:
        return (other.x - self.x) ** 2 + (other.y - self.y) ** 2
