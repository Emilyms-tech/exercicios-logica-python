print("Realize seu cadastro com uma senha de no mínimo 6 dígitos!")
valide = input("Digite suas senhas para validação aqui: ")
senhas = valide.split()

for senha in senhas:
    if len(senha)>=6:
        print("senhas aceitas : ", senha , end= " ")

    else:
        print("\nCaracteres insuficientes em:", senha)
