num = int(input("Digite um número inteiro: "))

for i in range(1, num + 1): # O loop for itera de 1 até o número digitado (inclusive), calculando o fatorial de cada número
    fatorial = 1
    for j in range(1, i + 1):
        fatorial *= j
print(f"O fatorial de {num} é: {fatorial}")
