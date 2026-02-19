soma=0
for i in range(5):
     n=int(input("Digite um número inteiro: "))
     soma+=n

     if i==0:
       menor = maior = n

     else:
        if menor > n:
                menor = n
        if maior < n:
                maior = n                       
print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")
print(f"A soma dos números digitados é: {soma}")


