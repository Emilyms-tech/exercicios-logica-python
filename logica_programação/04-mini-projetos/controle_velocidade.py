velocidade=int(input("Digite a velocidade que seu veículo estava na via: "))
vel_Max = 80

if velocidade <= vel_Max:
    print("Não houve multa")
elif velocidade > 80 and velocidade <= 90:
    print("Levou multa leve")
elif velocidade > 90 and velocidade <= 100:
    print("Levou multa grave!")
else:
    print("Levou multa gravíssima!")