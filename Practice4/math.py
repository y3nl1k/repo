#1 degree to radian
import math
deg=int(input("Input degree: "))
print("Output radian: ", math.radians(deg))

#2 area of Trapezoid
h = float(input())
b1 = float(input())
b2 = float(input())
print((b1 + b2) / 2 * h)

#area of regular polygon
import math
n = int(input())
l = float(input())
a = (n * l**2) / (4 * math.tan(math.pi / n))
print(f"{a:.0f}")

#area of a parallelogram
b = float(input())
h = float(input())
print(float(b * h))