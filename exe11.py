#calculo com valores na mesma linha .split

codigo_peca1, numero_peca1, valor_unitario_peca1 = map(float, input().split())

codigo_peca2, numero_peca2, valor_unitario_peca2 = map(float, input().split())

total_a_pagar = (numero_peca1 * valor_unitario_peca1) + (numero_peca2 * valor_unitario_peca2)

print("VALOR A PAGAR: R$ {:.2f}".format(total_a_pagar))


##########################################################

#calculo de peças opcional 

# peca1 = int(input())
# qtd_peca1 = int(input())
# valor_peca1 = float(input())

# peca2 = int(input())
# qtd_peca2 = int(input())
# valor_peca2 = float(input())

# soma1 = valor_peca1 * qtd_peca1
# soma2 = valor_peca2 * qtd_peca2

# total = soma1 + soma2

# print("VALOR A PAGAR: R$ {:.2F}".format(total))