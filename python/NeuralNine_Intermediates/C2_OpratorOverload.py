class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __str__(self):
        return f"(x={self.x},y={self.y})"
    
v1 = Vector(1,2)
v2 = Vector(2,3)

v3 = v1+v2
print(v3)