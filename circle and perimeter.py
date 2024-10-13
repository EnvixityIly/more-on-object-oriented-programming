class Circle:

    def __init__(self,r):
        self.r = r
        
    def area(self):
        ar = 3.14 * self.r
        return ar
    def perimeter(self):
        p = 2 * 3.14 * self.r
        return p
# sir i did it a bit differently bc init functione r diye parchilam na
radius = float(input("Enter the float number: "))

obj = Circle(radius)
print(obj.area())
print(obj.perimeter())






