def media (lista):
    soma = 0
    for i in range(1, len(lista), 1):
        soma = soma + lista[i]
    md = soma/len(lista)
    return md

def main():
    lista = [1,2,3,4]
    val = media(lista)
    print(val)

main()