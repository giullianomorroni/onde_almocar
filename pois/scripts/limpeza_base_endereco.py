# -*- coding: utf-8 -*-

from collections import deque
import os

class LimpezaEndereco():

  def read(self):
    original = open('/home/giulliano/Documentos/Estabelecimentos/estabelecimentos_3.txt','r')
    normalizado = open('/home/giulliano/Documentos/Estabelecimentos/estabelecimentos_4.txt','w')
    for linha in original:
      linha = linha.split('#')
      nome 		= linha[0]
      logradouro 	= linha[1]
      numero		= linha[2]
      bairro 		= linha[3]
      cidade 		= linha[4]
      estado 		= linha[5]
      telefone 		= linha[6]
      categoria 	= linha[7]
      subcategoria 	= linha[8]
      site 		= linha[9]

      if len(logradouro.strip()) == 0:continue
      if len(numero.strip()) == 0:continue

      normalizado.write(nome)
      normalizado.write('#')
      normalizado.write(logradouro)
      normalizado.write('#')
      normalizado.write(numero)
      normalizado.write('#')
      normalizado.write(bairro)
      normalizado.write('#')
      normalizado.write(cidade)
      normalizado.write('#')
      normalizado.write(estado)
      normalizado.write('#')
      normalizado.write(telefone)
      normalizado.write('#')
      normalizado.write(categoria)
      normalizado.write('#')
      normalizado.write(subcategoria)
      normalizado.write('#')
      normalizado.write(site)
      normalizado.write('#')
      normalizado.write('\n')

    original.close()
    normalizado.close()
  