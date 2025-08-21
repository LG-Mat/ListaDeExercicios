def divisivel (a, b):
    if a % b == 0:
        return True
    else:
        return False

def main():
    valor1 = input("Digite o primeiro valor: ")
    valor1 = float(valor1)
    valor2 = input("Digite o segundo valor: ")
    valor2 = float(valor2)

    resultado = divisivel(valor1, valor2)

    print(resultado)

main()