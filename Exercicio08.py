# As notas de um aluno estão armazenadas em uma lista. Calcular a média dessas notas.

notas = []
soma = 0

n1 = input('Digite o valor da primeira nota: ')
notas.append(float(n1))

n2 = input('Digite o valor da segunda nota: ')
notas.append(float(n2))

n3 = input('Digite o valor da terceira nota: ')
notas.append(float(n3))

for i in range(len(notas)):
    soma = soma + notas[i]

media = soma/len(notas)

print(media)
