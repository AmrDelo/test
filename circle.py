class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(rad):
        area = 3.14 * rad.radius * rad.radius
        print("Area of circle "+str(area))
    def perimeter(rad):
        peri = 2 * 3.14 * rad.radius
        print("Perimeter of circle "+str(peri))

r = float(input("Enter radius of circle "))
c = circle(r)
c.area()
c.perimeter()