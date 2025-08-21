def valor(num, den):

    if den == 0: return 0

    if num % den == 0:
        print(num, 'é divisivel por:', den)
    return valor(num, den-1)

def main():
    v1 = int(input('Digite um valor: '))
    v1 = float(v1)

    v2 = v1

    valor(v1, v2)

main()