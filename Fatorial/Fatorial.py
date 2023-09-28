def calc_fatorial():
    print("OBS: Valores altos resultarão em números negativos ou 0, pois o resultado sera maior que a capacidade da variavel.")
    
    x = int(input("Digite um numero: "))
    num = x

    if x == 0:
        print(f"{num}! = 1")
    else:
        calc = str(x)
        y = x - 1
        resultado = x

        while y != 0:
            calc = calc + " * " + str(y)
            resultado = resultado * y
            y -= 1

        print("\nFatorial")
        print(f"{num}! = {calc} = {resultado}")


if __name__ == "__main__":
    calc_fatorial()