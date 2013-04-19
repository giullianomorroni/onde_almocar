#!/usr/bin/env python
#-*-coding:utf-8-*-

import os

def execute():
  origem =  open('estabelecimentos_unificados.txt','r')
  destino =  open('destino.txt','w')
  x = []
  for linha in origem:
    r = linha.split('#')
    categoria 	= r[7]
    if categoria != 'Gastronomia':
      continue;
    destino.write(str(r)+'\n')

  destino.close()
  origem.close()