# Em relação a Matemática Discreta, podemos visualizar em um simples jogo de Jo-Ken-Po. 
# Relações Binárias distintas a partir do possíveis resultados:
# Conjuto = (Pedra, Papel e Tesoura)
# (Pedra, Papel); (Pedra, Tesoura); (Pedra, Pedra)
# (Papel, Papel); (Papel, Tesoura); (Papel, Pedra)
# (Tesoura, Papel); (Tesoura, Tesoura); (Tesoura, Pedra)

import random

#Escolhas possíveis:
opcoes = ["pedra", "papel", "tesoura"]

#Jogadores:
jogada_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
jogada_computador = random.choice(opcoes)

print("Você jogou " + jogada_jogador)
print("Computador jogou " + jogada_computador)

#Resultados possíveis:
if jogada_jogador not in opcoes:
    print("Jogada inválida.")
elif jogada_jogador == jogada_computador:
    print("Empate!")
elif jogada_jogador == "pedra":
    if jogada_computador == "papel":
        print("Você perdeu!")
    else:
        print("Você venceu!")
elif jogada_jogador == "papel":
    if jogada_computador == "tesoura":
        print("Você perdeu!")
    else:
        print("Você venceu!")
elif jogada_jogador == "tesoura":
    if jogada_computador == "pedra":
        print("Você perdeu!")
    else:
        print("Você venceu!")

