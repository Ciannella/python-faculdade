from time import sleep
"""Faça uma função que receba o nome e sobrenome de uma pessoa e retorne a
primeira letra de seu nome e seu sobrenome concatenando com a string
@algoritmos.com.br. No algoritmo principal deverá ser apresentada a mensagem
ao usuário contendo seu nome completo e seu email.
Imprima na tela um teste do seu programa utilizando o seu nome e sobrenome
concatenado com os dois últimos dígitos do seu RU. 3617126 """
def concatena(nome,sobrenome,num):
    ru = str(num)[-2]
    ru_2 = str(num) [-1]
    concatenado = nome[0] + sobrenome + ru + ru_2 + '@algoritimos.com.br'
    print(concatenado)




print('-' * 35)
print('sistema de concatenação de e-mail')
print('-' * 35)
sleep(1.5)

nome = input('Digite o seu nome: ')
sob = input('Digite o seu sobrenome: ')
ru = int(input('Digite o seu RU: '))

print('-' * 35)
print('Finalizando. . . .')
print('-' * 35)
sleep(1.5)

concatena(nome,sob,ru)