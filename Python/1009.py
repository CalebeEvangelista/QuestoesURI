nome = input()
salario = float(input())
vendas = float(input())
comissao = vendas * 0.15
salariofinal = comissao + salario

print("TOTAL = R$ {:.2f}" .format(salariofinal))