# salario com bonus

vendedor = input()
salario = float(input())
vendas = float(input())

comissao = (vendas * 15) / 100

total = salario + comissao

print("TOTAL = R$ {:.2F}".format(total))
