import math

def circle_stats(radious):
    area = round(math.pi* (radious**2),3)
    circumferance = round(math.pi*2*radious,3)
    return area,circumferance
a,c = circle_stats(4)
print(a,c)
print(circle_stats(5))