from operator import itemgetter
import pandas as pd
from styles.estilo import bordas


#Lista, dicionário e apresentação criadas fora do laço
dicionario = {}
lista = []

bordas('Programa de Estoque')
print('Para encerrar o programa digite\nno campo "Código" o número 0')
print('-'*38)

#laço em loop para garantir a continuidade do programa
while True:
# condicional de finalização do programa
    cod = int(input('Digite o código do produto: '))
    if cod == 0:
        break
    else:
        est = int(input('Insira a quantidade no estoque: '))
        minimum = int(input('insira o estoque mínimo: '))
        print('-'*38)
        dicionario["codigo"] = cod
        dicionario["estoque"] = est
        dicionario["minimo"] = minimum
        lista.append(dicionario.copy())

listaordenada = sorted(lista, key=itemgetter("codigo"))
print(listaordenada)
print('-' * 38)
#tabela de apresentação com o pandas
dataframe = pd.DataFrame(listaordenada)
print(dataframe)
