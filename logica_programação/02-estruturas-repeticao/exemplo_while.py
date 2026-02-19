soma=0 #variável para armazenar a soma dos números digitados
qnt=0 #contador de números digitados
while True:
    i= (int(input("Digite um número (Digite 0 para sair): ")))
        
    if i==0:
        break
    soma+=i
    qnt+=1

    if qnt > 0: 
        media=soma/qnt

    else:
        print("A média dos números digitados é: 0")

print(f"A quantidade de números digitados é: {qnt}")
print(f"A soma dos números digitados é: {soma}")
print(f"A média dos números digitados é: {media}")