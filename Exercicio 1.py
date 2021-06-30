from styles.estilo import bordas

#programa principal

bordas('Bem vindo ao sistema UNINTER')
#laço de repetição em loop
while True:
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
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
    print('-' * 28)
    print(f'''nome do aluno: {nome}  
    Nota final: {nota} 
    O aluno se encontra com conceito {situacao}''')
    print('-' * 28)

#variável para continuar ou não o programa
    res = int(input('Para finalizar o programa digite 0 ou qualquer dígito para continuar:'))
    if res == 0:
        break
    else:
        continue
print('fim do programa')





