carlos = input() .split()
c1 = int(carlos[0])
n1 = int(carlos[1])
v1 = float(carlos[2])
total1 = n1 * v1

alberto = input() .split()
c2 = int(alberto[0])
n2 = int(alberto[1])
v2 = float(alberto[2])
total2 = n2 * v2

totaltotal = total1 + total2

print("VALOR A PAGAR: R$ {:.2f}" .format(totaltotal))