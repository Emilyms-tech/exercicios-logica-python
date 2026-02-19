usuario = " "
senha = " "
tentativas=0

print("Faça seu login abaixo!")

while (usuario != "Emily" and senha != "Genia456") and tentativas < 3:
    usuario = input("Digite o nome cadastrado: ")
    senha = input("Digite sua senha: ")
    tentativas += 1
    
if usuario=="Emily" and senha == "Genia456":
    print("Login realizado com sucesso!")
else:
    print("Tente novamente + tarde!")

