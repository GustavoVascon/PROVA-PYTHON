#Senhas Criticadas com funções – rescreva o programa do exercício anterior, 
#criando e utilizando as seguintes funções:

#tamanhovalido(s, tamanho) – retorna “true” se o tamanho da string “s” é menor ou igual ao número “tamanho”; 
#caso contrário “false”

#senhamaiuscula(s) – retorna a versão maiúscula de s

#senhaminuscula(s) - retorna a versão minúscula de s

#valida1dig(s) – retorna “true” se a string “s” tem pelo menos 1 dígito (numero); caso contrário “false”

#no1number(s) – retorna “true” se a string “s” não começa com 1 dígito; caso contrário “false”

#pelomenos1maisc() - retorna “true” se a string “s” tem pelo menos 1 letra maiúscula;

print('A senha deve conter de 6 a 8 caracteres')
print('Pelo menos 1 número')
print('Não pode começar por número')
print('Pelo menos 1 letra maiúscula')
print()
while True:

    def no1number(s):
        if s[0].isdigit():
            print('A senha não pode começar por número')
            print('A senha digitada "{}" é Inválida'.format(s))
            return False
        else:
            return True

    def senhamaiuscula(s):
        maiuscula = s.upper()
        return maiuscula

    def senhaminuscula(s):
        minuscula = s.lower()
        return minuscula

    def pelomenos1maisc(s):
        if any(x.isupper() for x in s):
            return True
        else:
            print('A senha deve conter pelo menos 1 letra maiúscula')
            print('A senha digitada "{}" é Inválida'.format(s))
            return False

    def valida1dig(s):
        if any(x.isdigit() for x in s):
            return True
        else:
            print('A senha deve conter pelo menos 1 um número')
            print('A senha digitada "{}" é Inválida'.format(s))
            return False

    def tamanhovalido(s, tamanho):
        if len(s) == tamanho:
            return True
        else:
            print('A senha deve conter {} caracteres'.format(tamanho))
            print('A senha digitada "{}" contém {}, portanto, é inválida'.format(s,len(s)))
            return False

    tamanho = 7        
    s = str(input('Digite uma senha válida: '))

    valido_tamanho = tamanhovalido(s, tamanho)
    if valido_tamanho == False:
        break
    
    um_maisculo = pelomenos1maisc(s)
    if um_maisculo == False:
        break

    valido_numero = valida1dig(s)
    if valido_numero == False:
        break
    
    numero_primeiro = no1number(s)
    if numero_primeiro == False:
        break

    print('Senha: {}'.format(s))

    maiuscula = senhamaiuscula(s)
    print('Versão maiúscula: {}'.format(maiuscula))

    minuscula = senhaminuscula(s)
    print('Versão minúscula: {}'.format(minuscula))

    break

def tamanhovalido(password, tamanho):
    if len(password) == tamanho:
        return True
    else:
        return False