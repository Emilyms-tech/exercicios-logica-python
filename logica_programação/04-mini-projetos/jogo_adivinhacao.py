import random

numero_de_chute = random.randint(1,10)

print("Bem-vindo ao jogo de adivinhar o número!")

acerto = False

while not acerto:
    chute = int(input("Digite um número entre 1 e 10: "))
    if chute == numero_de_chute:
        print("Parabéns! Você acertou o número!")
    elif chute < numero_de_chute:
        print("O número é maior do que o seu chute. Tente novamente.")
    else:
        print("O número é menor do que o seu chute. Tente novamente.")
