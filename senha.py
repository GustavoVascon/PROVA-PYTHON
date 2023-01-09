#Senhas Criticadas- Faça um programa em Python que leia uma senha aleatória e forneça seu tamanho, 
#e imprima uma versão maiúscula e uma minúscula da senha. 
#exemplo de saída: (senha:”AbCd123”)
#tamanho da senha: 7
#versão maiúscula: ABCD123
#versão minúscula: abcd123

#(opcional) – incremente o programa e valide uma senha segundo os seguintes critérios:
#Tamanho – de 6 a 8 caracteres; 
#Pelo menos 1 número; 
#Não pode começar por número;
#Pelo menos 1 letra maiúscula;
#(dica: utilize as funções isalpha() para verificar se um caractere é um alfabético, 
#e isdigit() para verificar se um caractere é um dígito.
#Exemplo: s=”abc123”
#S[0].isalpha() => true
#S[0].isdigit() => false
#S[3].isalpha() => false
#S[3].isdigit() => true
#exemplo de saída: 
#Qwerty123abc -> senha inválida
#Qwerty12 -> senha válida
#123abcD -> senha inválida
#q123abcD -> senha válida

print('A senha deve conter de 6 a 8 caracteres')
print('Pelo menos 1 número')
print('Não pode começar por número')
print('Pelo menos 1 letra maiúscula')
print()
while True:
    senha_usuario = input('Digite uma senha válida: ')
    tamanho_senha = len(senha_usuario)
    maiuscula = senha_usuario.upper()
    minuscula = senha_usuario.lower()

    if senha_usuario[0].isdigit():
        print('A senha não pode começar por número')
        print('A senha digitada "{}" é Inválida'.format(senha_usuario))
        break
    elif not any(x.isupper() for x in senha_usuario):
        print('A senha deve conter pelo menos 1 letra maiúscula')
        print('A senha digitada "{}" é Inválida'.format(senha_usuario))
        break
    elif not any(x.isdigit() for x in senha_usuario):
        print('A senha deve conter pelo menos 1 um número')
        print('A senha digitada "{}" é Inválida'.format(senha_usuario))
        break
    elif tamanho_senha < 6 or tamanho_senha > 8:
        print('A senha deve conter de 6 a 8 caracteres')
        print('A senha digitada "{}" é Inválida'.format(senha_usuario))
        break

    print('Senha: {}'.format(senha_usuario))
    print('A senha contém {} caracteres'.format(tamanho_senha))
    print('Versão maiúscula: {}'.format(maiuscula))
    print('Versão minúscula: {}'.format(minuscula))
    break