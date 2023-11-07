# Lê os três valores inteiros
a, b, c = map(int, input().split())

# Calcula o maior entre a e b
maior_ab = (a + b + abs(a - b)) // 2

# Calcula o maior entre o valor anterior e c
maior = (maior_ab + c + abs(maior_ab - c)) // 2

# Imprime o resultado
print(maior, "eh o maior")
