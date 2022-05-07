pares = 0
impares = 0
for numero in range(1, 101):
    inteiro = int(input())
    if inteiro % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(pares)
print(impares)

