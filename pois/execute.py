#! /usr/bin/env python
# -*- coding: utf-8 -*-

from python_sort import p_sort
from python_match import p_match
import time

'''
print 'Iniciando ordenação dos POIs'
arq_original = open('/home/giulliano/Documents/Estabelecimentos/scripts_unificacao/estabelecimentos.txt','r')
arq_ordenado = open('/home/giulliano/Documents/Estabelecimentos/scripts_unificacao/estabelecimentos_ordenados.txt','w')
pst = p_sort()
pst.ordenar(arq_original, arq_ordenado)
print 'Ordenação concluída'
'''

print 'Iniciando comparação por range'
pmatch = p_match()
arq_unificado = open('/home/giulliano/Documents/Estabelecimentos/scripts_unificacao/estabelecimentos_unificados.txt','w')
arq_ordenado = open('/home/giulliano/Documents/Estabelecimentos/scripts_unificacao/estabelecimentos_ordenados.txt','r')


lista = []
#count = 0;
for linha in arq_ordenado:
  #count += 1;
  #if (count < inicio): continue;
  #if (count > fim): break;
  lista.append(linha)


pmatch.removerDuplicados(arq_ordenado, arq_unificado, 0 , 30000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 30000 , 60000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 60000 , 90000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 90000 , 120000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 120000 , 150000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 150000 , 180000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 180000 , 210000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 210000 , 240000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 240000 , 270000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 270000 , 300000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 300000 , 330000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 330000 , 360000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 360000 , 390000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 390000 , 420000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 420000 , 450000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 450000 , 480000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 480000 , 510000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 510000 , 540000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 540000 , 570000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 570000 , 600000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 600000 , 630000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 630000 , 660000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 660000 , 690000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 690000 , 720000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 720000 , 750000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 750000 , 780000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 780000 , 810000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 810000 , 840000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 840000 , 870000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 870000 , 900000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 900000 , 930000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 930000 , 960000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 960000 , 990000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 990000 , 1020000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1020000 , 1050000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1050000 , 1080000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1080000 , 1110000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1110000 , 1140000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1140000 , 1170000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1170000 , 1200000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1200000 , 1230000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1230000 , 1260000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1260000 , 1290000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1290000 , 1320000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1320000 , 1350000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1350000 , 1380000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1380000 , 1410000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1410000 , 1440000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1440000 , 1470000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1470000 , 1500000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1500000 , 1530000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1530000 , 1560000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1560000 , 1590000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1590000 , 1620000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1620000 , 1650000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1650000 , 1680000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1680000 , 1710000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1710000 , 1740000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1740000 , 1770000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1770000 , 1800000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1800000 , 1830000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1830000 , 1860000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1860000 , 1890000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1890000 , 1920000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1920000 , 1950000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1950000 , 1980000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 1980000 , 2010000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2010000 , 2040000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2040000 , 2070000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2070000 , 2100000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2100000 , 2130000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2130000 , 2160000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2160000 , 2190000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2190000 , 2220000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2220000 , 2250000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2250000 , 2280000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2280000 , 2310000, lista)
pmatch.removerDuplicados(arq_ordenado, arq_unificado, 2310000 , 2340000, lista)

arq_unificado.close()
#arq_original.close()
arq_ordenado.close()
