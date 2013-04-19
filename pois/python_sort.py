#! /usr/bin/env python
# -*- coding: utf-8 -*-

class p_sort:
  
  '''
  Recebe o arquivo original e o arquivo onde será gravado o resultado da ordenação
  '''
  def ordenar(self, arq_original, arq_ordenado):
    lista = []

    for linha in arq_original:
      lista.append(linha)

    '''
    Ordena a lista baseando-se somente no nome do POI
    '''
    lista_final = sorted(lista, key=lambda nome : str(nome.split("#")[0]).lower())
    for poi in lista_final:
      arq_ordenado.write(poi)
