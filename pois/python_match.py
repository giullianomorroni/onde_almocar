#! /usr/bin/env python
# -*- coding: utf-8 -*-

from nltk import metrics, stem, tokenize
import time

class p_match:

  #Esta função contempla o que será considerado na comparação  
  global _lambda

  def __init__(self):
    self._lambda = lambda nome : str(nome.split("#")[0:3])
  
  def removerDuplicados(self, arq_original, arq_unificado, inicio, fim, lista):
    print 'Range ' + str(inicio) + ' - ' + str(fim)
    print time.strftime('%H : %M : %S')

    for i in range(inicio, fim):
      j = (i+1)
      poi_1 = lista[i]
      duplicado = False
      '''
      A lista que está sendo comparada foi ordenada pelo mesmo
      campo de comparação, logo os itens idênticos estão próximos uns aos outros
      bastando percorrer apenas alguns próximos itens 
      '''
      for j in range(j, 20):
	poi_2 = lista[j]
	duplicado = self.fuzzy_match(poi_1, poi_2, 1) #TRUE
	if duplicado:
	  break;
      if not duplicado:
	arq_unificado.write(poi_1)
    #pausa para o PC respirar um pouco
    time.sleep(5)

  def normalize(self, s):
    stemmer = stem.PorterStemmer()
    words = tokenize.wordpunct_tokenize(s.lower().strip())
    return ' '.join([stemmer.stem(w) for w in words])

  def fuzzy_match(self, s1, s2, max_dist=3):
    return metrics.edit_distance(self.normalize(self._lambda(s1)), self.normalize(self._lambda(s2))) <= max_dist
