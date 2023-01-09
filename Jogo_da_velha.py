#lista da Velha esquisito – faça um programa que leia 9 números inteiros e imprime-os no formado de lista da velha. 
# Imprima também a soma da dagonal principal:
#exemplo de saída: 1,2,3,4,5,6,7,8,9

#1 | 2 | 3
#4 | 5 | 6
#7 | 8 | 9
#Soma da diagonal principal = 15

#(opcional) – incremente o programa imprimindo o formato invertido 

#exemplo de saída: 1,2,3,4,5,6,7,8,9
#9 | 8 | 7
#6 | 5 | 4
#3 | 2 | 1
#Soma da diagonal principal = 15
print('')
print('lista da Velha esquisito')
print('')
print('Colunas e linhas de 0 a 3')
print('')
print('[0,0] [0,1] [0,2]\n[1,0] [1,1] [1,2]\n[2,0] [2,1] [2,2]')
print('')

matriz = [['']*3,['']*3, ['']*3]

for i in range(3):
    print(f" {matriz[i][0]:3} | {matriz[i][1]:3} | {matriz[i][2]:3}")
    if i < 2:
        print(f"-----+-----+-----")

for j in range (9):
    # jogador entra com jogada
    if j%1==0:
        while True:
            print("Entre com sua jogada:")
            while True:
                linha = int(input("insira a linha: "))
                if linha in [0,1,2]:
                    break
            while True:
                coluna = int(input("insira a coluna: "))
                if 0<= coluna <=2:
                    break

            #testa se a jogada foi valida
            if matriz[linha][coluna] == '':
                matriz[linha][coluna] = user_input = int(input('Digite seu número: '))
                break
            else:
                print("jogada invalida")
    #imprimo o tabuleiro
    for i in range(3):
        print(f" {matriz[i][0]:3} | {matriz[i][1]:3} | {matriz[i][2]:3}")
        if i < 2:
            print(f"-----+-----+-----")

soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
print('Soma da diagonal principal =',soma)

print('Imprimindo programa de forma inversa')
print('   {} |   {} |   {}'.format(matriz[2][2],matriz[2][1],matriz[2][0]))
print(f"-----+-----+-----")
print('   {} |   {} |   {}'.format(matriz[1][2],matriz[1][1],matriz[1][0]))
print(f"-----+-----+-----")
print('   {} |   {} |   {}'.format(matriz[0][2],matriz[0][1],matriz[0][0]))
print('Soma da diagonal inversa principal =',soma)