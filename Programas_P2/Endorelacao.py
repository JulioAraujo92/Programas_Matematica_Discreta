def verifica_reflexividade(conjunto, relacao):

    for elemento in conjunto:
        if (elemento, elemento) not in relacao:
            return False
    return True


conjunto_exemplo = {1, 2, 3}
relacao_exemplo = [(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)]

if verifica_reflexividade(conjunto_exemplo, relacao_exemplo):
    print("A relação é reflexiva.")
else:
    print("A relação não é reflexiva.")
