#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import json

def execute():
  origem =  open('estabelecimentos_unificados.txt','r')
  destino =  open('destino.txt','w')
  x = []
  for linha in origem:
    r = linha.split('#')
    print r
    nome 	= r[0]
    endereco 	= r[1]
    numero 	= r[2]
    bairro 	= r[3]
    cidade 	= r[4]
    estado 	= r[5]
    telefone 	= r[6]
    categoria 	= r[7]
    if categoria != 'Gastronomia':
      continue;
    subcategoria= r[8]
    site 	= r[9]
    latitude 	= None
    longitude 	= None
    if len(r) >= 11:
      latitude 	= r[10]
    if len(r) >= 12:
      longitude	= r[11]

    aux = json.dumps({'nome':nome, 'endereco':endereco, 'numero':numero, 'bairro':bairro, 'cidade':cidade, 'estado':estado,
	  'telefone':telefone, 'categoria':categoria, 'subcategoria':subcategoria, 'site':site,
	  'latitude':latitude, 'longitude':longitude }, ensure_ascii=False)
    x.append(aux)
    destino.write(nome + '\n')
    destino.write(aux)

  for v in x:
    print '\n' 
    print v

  destino.close()
  origem.close()