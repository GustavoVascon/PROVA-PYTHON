#Vetores estranhos – criei um programa que solicite até 20 números inteiros positivos, 
#e os armazene em um vetor. A entrada dos números termina ao chegar a 20 ou se o usuário digitar um valor negativo. 
#Ao termina a entrada de dados imprima os números, a soma dos números, a quantidade entrada e a média. 

#exemplo de saída:

#vetor [1, 2, 3, 4, 5, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
#soma = 15
#Quantidade entrada = 5
#Media = 3

#(opcional) – incremente o programa imprimindo também o maior e menor valor entrado
#exemplo de saída:

#exemplo de saída:

#vetor [1, 2, 3, 4, 5, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
#soma = 15
#Quantidade entrada = 5
#Media = 3
#Maior = 5
#Menor = 1


import statistics

lista = []

while len(lista) + 1 <= 20:
    numero = (int(input('Digite um número: ')))
    if numero <= 0:
        break
    else:
        lista.append(numero)

print('lista: {} '.format(lista))
print('Soma: ',sum(lista))
print('Quantidade de entradas: ',len(lista))
print('Média: ', statistics.mean(lista))
print('Maior: ',max(lista))
print('Menor: ',min(lista))




