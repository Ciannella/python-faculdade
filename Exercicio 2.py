from time import sleep #função para fazer uma epera no programa
from styles.estilo import bordas #modulo feito para fazer estilos no programa


#funções

""" A função captura o numero da RU o nome e o sobrenome,
 primeiro ela captura o penúltimo e o ultimo número da RU
 tranforma em string e ao final concatena todos os elementos """

def concatena(nome,sobrenome,num):
    ru = str(num)[-2]
    ru_2 = str(num)[-1]
    concat = nome[0] + sobrenome + ru + ru_2 + '@algoritimos.com.br'
    print(concat)


#programa principal


bordas('sistema de concatenação de e-mail')

sleep(1.5)

nome = input('Digite o seu nome: ')
sob = input('Digite o seu sobrenome: ')
ru = int(input('Digite o seu RU: '))

bordas('Finalizando. . . .')
sleep(1.5)

concatena(nome,sob,ru)

