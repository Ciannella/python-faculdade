#laço do programa
while True:
    res = input('Quer adicionar dados? [Sim ou Não ?]').upper()[0]


    if res == 'S':
        print('-' * 30)
        print('Bem vindo ao sistema UNINTER')
        print( '-' * 30)

        nome = input('Digite o nome do aluno: ')
        nota = float(input('Digite a nota do aluno: '))

    else:
        break

#validação da nota

if nota <= 2.9:
    situacao = 'E'
elif nota <= 4.9:
    situacao = 'D'
elif nota <= 5.9:
    situacao = 'C'
elif nota <= 8.9:
    situacao = 'B'
else:
    situacao = 'A'

print(f'''nome do aluno: {nome} 
Nota final: {nota}
O aluno se encontra com conceito {situacao}''')

print('-' * 30)



