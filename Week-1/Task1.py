import math

def toCartesian(r, theta):
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x,y

def toPolar(x, y):
    r = (x ** 2 + y ** 2) ** .5
    theta = math.degrees(math.atan2(y,x))
    return r, theta


print("Choose your option:")
print("1. Polar to Cartesian")
print("2. Cartesian to Polar")
choice = input()
if(choice==1):
    print("Enter r:")
    r = input()
    print("Enter theta:")
    theta=input()
    x,y = toCartesian(r,theta)
    print("x: " + str(x) + ", y: " + str(y))

else:
    print("Enter x:")
    x = input()
    print("Enter y:")
    y = input()
    r,theta = toPolar(x,y)
    print("r: " + str(r) + ", theta: " + str(theta))
