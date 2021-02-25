valores = input().split() #.split() = Separa os valores do input para mexer separadamente
A = float(valores[0]) #0 = 1º posição dos valores
B = float(valores[1]) #1 = 2º posição dos valores
C = float(valores[2]) #2 = 3º posição dos valores

tri = (A * C) / 2 #Formula da area do triangulo retangulo
cir = (3.14159 * C**2) #Formula da area do circulo
tra = ((A + B) * C) /2 #Formula da area do trapezio
qua = B**2 #Formula da area do quadrado
ret = A * B #Formula da area do retangulo

print('TRIANGULO: {:.3f}' .format(tri))
print('CIRCULO: {:.3f}' .format(cir))
print('TRAPEZIO: {:.3f}' .format(tra))
print('QUADRADO: {:.3f}' .format(qua))
print('RETANGULO: {:.3f}' .format(ret))