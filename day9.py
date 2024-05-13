class Circle:
    def __init__(self,r):
        self.r= r

    def getArea(self):
        area = self.r * self.r * 3.141592
        return area

    def getPerimeter(self):
        perimeter = 2 * self.r * 3.141592
        return perimeter


c = Circle(10)

print(f"원의 면적 {c. getArea()}")
print(f"원의 둘레 {c.getPerimeter()}")