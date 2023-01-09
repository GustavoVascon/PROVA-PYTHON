#Frases malucas - Em algumas situações é preciso gerar textos aleatórios para teste (por exemplo para preencher o design de um site em construção) Para este fim, escreva um programa que gere 5 textos aleatórios baseado nas listas de palavras abaixo:
#artigos = ["o", "a", "um", "uma"]
#sujeitos = ["gato", "cachorro", "homem", "mulher"]
#verbos = ["cantar", "correr", "pular", "nadar"]
#adverbios = ["vagarosamente", "silenciosamente", "bem", "mal"]

#Para escolha aleatória da palavra de cada lista utilize a função random.choice(lista). Não esqueça de importar o módulo random ( import. random)

#exemplo de saída:

#a cachorro cantar mal
#o gato nadar mal
#um homem correr silenciosamente
#a homem pular bem
#o homem correr mal

#(opcional) Incremente o programa utilizando 2 estruturas de frases: (1) artigo, sujeito, verbo, adverbio ou (2) artigo, sujeito, verbo. Utilize a função random.randint() para escolher aleatoriamente entre as 2 estruturas.

#exemplo de saída:

#uma gato pular vagarosamente
#o mulher cantar 
#o gato pular 
#um homem correr 
#um gato cantar bem


import random
artigos = ["o", "a", "um", "uma"]
sujeitos = ["gato", "cachorro", "homem", "mulher"]
verbos = ["cantar", "correr", "pular", "nadar"]
adverbios = ["vagarosamente", "silenciosamente", "bem", "mal"]

for i in range(5):
    frase = ''
    num = random.randint(1, 2)
    if num == 1:
        frase += random.choice(artigos) + ' '
        frase += random.choice(sujeitos) + ' '
        frase += random.choice(verbos) + ' '
        frase += random.choice(adverbios)
    else:
        frase += random.choice(artigos) + ' '
        frase += random.choice(sujeitos) + ' '
        frase += random.choice(verbos)
    print(frase)