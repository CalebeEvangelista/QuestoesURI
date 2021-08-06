import math

p1 = input() .split()
p2 = input() .split()

x1 = float(p1[0])
x2 = float(p2[0])
y1 = float(p1[1])
y2 = float(p2[1])

c1 = math.pow(x2-x1 ,2)
c2 = math.pow(y2-y1 ,2)
c3 = c1 + c2
c4 = math.sqrt(c3)

print("{:.4f}" .format(c4))