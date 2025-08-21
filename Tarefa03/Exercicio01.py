def media (lista, i, soma):
    soma = soma + lista[i]
    if i > 0: return media(lista, i-1, soma)
    else: return soma/len(lista)

def main():
    lista = [1,2,3,4]
    val = media(lista, len(lista)-1, 0)
    print(val)

main()