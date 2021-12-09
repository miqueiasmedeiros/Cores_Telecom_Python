# -*- coding: utf-8 -*-
import os

numfibra = int(input('Digite o número da fibra: '))

if ((numfibra < 1) or (numfibra > 288)): 
    print("## Número inválido")
    os.system("pause")
    exit()

corfibra = [
    'verde', 'amarela', 'branca', 'azul', 
    'vermelha','violeta', 'marrom', 'rosa', 
    'preta', 'cinza', 'lanranja', 'aqua'
]
n = numfibra % 12
grupo = numfibra * 24 / 288

if n == 0:
    print('cor:', corfibra[11], '\ngrupo: ', int(grupo))
else :
    print('cor:', corfibra[n-1], '\ngrupo: ', int(grupo) + 1)

os.system("pause")