import math
from functionModule import function
print(math.pi)
print(math.degrees(math.pi))
print(math.atan(math.pi))


def toDegrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

print(toDegrees(math.pi))

def toRadians(degrees):
    radians = (degrees * math.pi) / 180
    return radians

print(toRadians(180))

def toSin(radians):
    seno = 0
    for x in range(50):
        seno += ((-1)**x * radians**(2*x + 1)) / math.factorial(2*x + 1)
    return seno

degree = input("Choose degrees: ")
radians = toRadians(int(degree))
print(toRadians(int(degree)))
print(f"Sine of {degree} degrees = {toSin(radians)}")

# moduling
print(function.addTwo(2))