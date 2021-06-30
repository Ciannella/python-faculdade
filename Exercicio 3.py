from random import choice, shuffle
from time import sleep
from styles.estilo import bordas


#programa principal


lista =[]

bordas('Programa solidario')

#crio um loop infinito para o programa não parar

while True:
   nome = input('Digite o seu nome:')
   valor = int(input('Insira o valor doado:R$ '))

#Uma validação para o valor doado, impedindo de doar menos de 10 reais

   while valor < 10:
      print('\033[1;91m Para participar é preciso doar um valor a partir de R$10,00 reais\033[m')
      valor = int(input('favor inserir novo valor: R$ '))

#logica, para cada 10 reais doado o nome é adicionado na lista

   if valor >= 10:
      div = int(valor / 10)

      for valor in range(0,div):
         lista.append(nome)

#Pergunta para finalizar o programa + validação de entrada do usuário
   resp = input('Deseja adicionar mais participantes?[S / N]')
   print('-' * 18)
   while resp not in 'SsNn':
      resp = input('Por favor digite apenas [S ou N]  ')
   if resp == 'N':
      break
   else:
      continue


bordas(' sorteando ganhador!')

shuffle(lista)
sorteado = choice(lista)
sleep(1.5)

print(f'\033[1;30;102mE o vencedor foi: {sorteado}!\033[m')
print(f'\033[1;30;102mPARABÉNS\033[m')

