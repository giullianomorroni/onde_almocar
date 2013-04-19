# -*- coding: utf-8 -*-

from collections import deque
import os
import re

class NormalizacaoEndereco():

  def read(self):
    original = open('/home/giulliano/Documents/Estabelecimentos/scripts_apontador/estabelecimentos.txt','r')
    normalizado = open('/home/giulliano/Documents/Estabelecimentos/scripts_apontador/estabelecimentos_final.txt','w')
    for linha in original:
      linha = linha.split('#')
      nome 		= linha[0]
      endereco 		= linha[1]
      #numero 		= linha[2]
      #bairro 		= linha[3]
      cidade 		= linha[2]
      estado 		= linha[3]
      telefone 		= linha[4]
      categoria 	= linha[5]
      subcategoria 	= linha[6]
      site = '';
      if (len(linha) == 7):
	site 		= linha[8]

      #Extrai o nome da rua do endereco
      end_aux = endereco.split(',')
      logradouro = end_aux[0]

      #Separa em um array o número e o bairro
      numero_bairro = ''
      if len(end_aux) > 1:
	numero_bairro = end_aux[1]

      #Extrai o número do endereco
      _regex = re.compile('[0-9]+')
      numero_array = _regex.findall(numero_bairro)
      numero = ''
      if len(numero_array) > 0:
	numero = numero_array[0]

      #Extrai o bairro do endereco
      _regex = re.compile('[a-zA-Z]+')
      bairro_array = _regex.findall(numero_bairro)
      bairro = ''
      if len(bairro_array) > 0:
	bairro = bairro_array[0]

      normalizado.write(nome.strip())
      normalizado.write('#')
      normalizado.write(logradouro.strip())
      normalizado.write('#')
      normalizado.write(numero.strip())
      normalizado.write('#')
      normalizado.write(bairro.strip())
      normalizado.write('#')
      normalizado.write(cidade.strip())
      normalizado.write('#')
      normalizado.write(estado.strip())
      normalizado.write('#')
      normalizado.write(telefone.strip())
      normalizado.write('#')
      normalizado.write(categoria.strip())
      normalizado.write('#')
      normalizado.write(subcategoria.strip())
      normalizado.write('#')
      normalizado.write(site.strip())
      normalizado.write('#')
      normalizado.write('\n')

    original.close()
    normalizado.close()
