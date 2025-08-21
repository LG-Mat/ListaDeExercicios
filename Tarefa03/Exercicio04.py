def primo(num, den, aux):
    if den == 0:
        return aux
    if num % den == 0:
        return primo(num, den-1, aux+1)
    else:
        return primo(num, den-1, aux)

def main():
    num = int(input('Digite um valor: '))
    resultado = primo(num, num, 0)
    if resultado == 2:
        print('O valor inserido é primo')
    else: print('O valor inserido não é primo')

main()
