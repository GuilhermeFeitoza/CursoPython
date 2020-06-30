"""
Exercicio 1)
a = [1, 0, 5, -2, -5, 7]
soma = a[0] + a[1] + a[5]
print(soma)
a[4] = 100
print(a)

for var in a:
    print(var)
"""

'''
##Exercicio 2
lista = []
i = 0
while i < 6:
    lista.append(int(input('Digite um valor')))
    i = i + 1
else:
    for item in lista:
        print(item)
'''
"""
##Exercicio 3
lista = []
i=0
while i < 10:
    lista.append(int(input('Digite um numero')))
    i += 1
else:
    listaquadrado = []
    for item in lista:
        listaquadrado.append(item**2)
    else:
        print(listaquadrado)
"""
"""
##Exercicio4
vetor = [1, 2, 3, 4, 5, 6, 7, 8]
x = vetor[1]
y = vetor[5]
soma = x + y

print(soma)

"""
"""
##Exercicio 5
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(vetor))

numeros_pares = 0
for num in vetor:
    if num%2 == 0:
        numeros_pares +=1
print(numeros_pares)
"""
"""
##Exercicio6
vetor = []
i=0
while i < 11:
    vetor.append(int(input('Digite um numero')))
    i += 1

print(min(vetor))
print(max(vetor))
"""
"""
##Exercicio07
vetor = []
i = 0
while i < 11:
        vetor.append(int(input('Digite um numero')))
        i = i + 1
print(vetor)
print(max(vetor))
print(vetor.index(max(vetor)))
"""
"""

##Exercicio08
vetor = [1,2,3,4,5,6]
vetor.reverse()
print(vetor)
"""
"""
##Exercicio09
vetor = []
i = 0
while i < 6:
    numero = int(input('Digite um numero'))
    if numero % 2 == 0:
        vetor.append(numero)
    else:
        print('Somente numeros pares')
    i += 1
else:
    vetor.reverse();
    print(vetor)
"""
"""
##Exercicio10
notas = []
i = 1
while i < 16:
    notas.append(float(input(f'Digite a nota do aluno{i}')))
    i+=1
else:
    media = sum(notas)/15
    print(media)
"""


