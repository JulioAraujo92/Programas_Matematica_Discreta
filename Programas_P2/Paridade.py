def verifica_paridade(numero):

    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número para verificar paridade: "))

resultado = verifica_paridade(numero)
print(f"O número {numero} é {resultado}.")
