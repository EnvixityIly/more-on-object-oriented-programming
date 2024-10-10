class Circle:

    def __init__(self):
        print('working')
        
    def area(self,r):
        ar = 3.14 * r
        return ar
    def perimeter(self,r):
        p = 2 * 3.14 * r
        return p
# sir i did it a bit differently bc init functione r diye parchilam na
radius = float(input("Enter the float number: "))

obj = Circle()
print(obj.area(radius))
print(obj.perimeter(radius))


