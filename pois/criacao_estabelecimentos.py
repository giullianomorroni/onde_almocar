# -*- coding: utf-8 -*-

import os

'''
Com base no arquivo de estabelecimentos interessantes realiza o 'de x para' 
de categorias e subcategorias
'''
class Criacao():

  global categorias
  global subcategorias 

  def __init__(self):
    de_para += [('hoteis-e-pousadas','Serviços')]
    de_para += [('Outros','Outros')]
    self.categorias = dict(de_para)
    
    de_para += [('escolas--geral-','Universidade')]
    de_para += [('vegetarianos','Vegetariana')]
    self.subcategorias = dict(de_para)

  def execute(self):
    origem =  open('/home/giulliano/Documents/Estabelecimentos/scripts_apontador/estabelecimentos_interessantes.txt','r')
    destino = open('/home/giulliano/Documents/Estabelecimentos/scripts_apontador/estabelecimentos.txt','w')
    for linha in origem:
      r = linha.split('#')
      nome = r[0]
      endereco = r[1]
      cidade = r[2]
      estado = r[3]
      telefone = r[4]
      categoria = r[5]
      subcategoria = r[6]
      site = ''
      if len(r) == 8:
	site = r[7]

      if categoria not in self.categorias:
	categoria = 'Outros';
      
      destino.write(nome)
      destino.write('#')
      destino.write(endereco)
      destino.write('#')
      destino.write(cidade)
      destino.write('#')
      destino.write(estado)
      destino.write('#')
      destino.write(telefone)
      destino.write('#')
      categoria = self.categorias[categoria]
      destino.write(categoria)
      destino.write('#')
      if subcategoria in self.subcategorias:
	subcategoria = self.subcategorias[subcategoria]
	destino.write(subcategoria)
      destino.write('#')
      destino.write(site)
      destino.write('#')
      destino.write('\n')

    origem.close()
    destino.close()