

letra_conjunto1 = input("Digite a letra do primeiro conjunto: ")
letra_conjunto2 = input("Digite a letra do segundo conjunto: ")


conjunto1 = input("Digite os elementos do primeiro conjunto (use , para separar): ")
conjunto2 = input("Digite os elementos do segundo conjunto (use , para separar): ")

conjunto1 = conjunto1.split(",")
conjunto2 = conjunto2.split(",")

produto = []
for elemento1 in conjunto1:
    for elemento2 in conjunto2:
        produto.append((elemento1, elemento2))
        
produto = (str(produto)).replace("[", "{")
produto = produto.replace("]", "}")


print(f"O produto cartesiano dos conjuntos fornecidos sao:\n {letra_conjunto1.upper()}x{letra_conjunto2.upper()} = {produto}")