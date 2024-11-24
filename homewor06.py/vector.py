import math

class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __bool__(self):
        return any(self.components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, index, value):
        self.components[index] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be of the same length for multiplication.")
            return Vector(*(a * b for a, b in zip(self.components, other.components)))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Unsupported operation for multiplication.")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return Vector(*(a / scalar for a in self.components))
        else:
            raise TypeError("Division only supports scalars (int or float).")

    def __eq__(self, other):
        return self.components == other.components

    def __neg__(self):
        return Vector(*(-a for a in self.components))

    def __abs__(self):
        return math.sqrt(sum(a ** 2 for a in self.components))



vector1 = Vector(1, 4, 6)
print(vector1)              
print(bool(vector1))        
print(len(vector1))        
print(vector1[1])          
vector1[1] = 10
print(vector1)            

vector2 = Vector(3, 7, 2)
print(vector1 + vector2)          
print(vector1 - vector2)        
print(vector1 * vector2)          
print(vector1 * 3)          
print(vector1 / 2)           
print(abs(v1))          
print(vector1 == Vector(1, 10, 6)) 
print(-vector1)              