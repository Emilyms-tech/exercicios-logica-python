salario=[]
soma = 0
for i in range(5): #o i funciona como índice para controlar o número de vezes que o loop será executado
    valor = float(input("Digite o salario aqui: "))
    salario.append(valor) #append é para adicionar o valor do salário à lista salario
    soma+=valor
print(f"A soma dos salarios é: {soma}")