# -*- coding: utf-8 -*-

import xml.etree.ElementTree as xml
from collections import deque
import os
import urllib
import nltk

'''
Baseado no arquivo de categorias/subcategorias que interessam, separa todos os 
estabelecimentos em dois arquivos (os que interessam e os que não interessam)
'''
class Limpeza():

  global categorias

  def __init__(self):
    self.categorias = deque()
    revisadas = open('/home/giulliano/Documents/Estabelecimentos/scripts_apontador/categorias_revisadas.txt','r')
    for linha in revisadas:
      c = linha.replace('\n','')
      if c in self.categorias:
	print 'ja existe'
      else:
	self.categorias.append(c);
    print 'Total de categorias %d' %len(self.categorias)

  def read(self):
    ei = open('/home/giulliano/Documents/Estabelecimentos/estabelecimentos_interessantes.txt','w')
    eni = open('/home/giulliano/Documents/Estabelecimentos/estabelecimentos_nao_interessantes.txt','w')

    for arquivo in os.listdir('/home/giulliano/Documents/Estabelecimentos/apontador/'):
      tree = xml.parse('/home/giulliano/Documents/Estabelecimentos/apontador/'+arquivo)
      rootElement = tree.getroot()
      documentos = rootElement.findall("document")
      for documento in documentos:
	cat = documento.findtext('category-base');
	sub = documento.findtext('subcategory-base');
	if sub == None or cat == None: continue;
	aux = cat+"#"+sub;

	nome = documento.findtext('name')
	endereco = documento.findtext('address')
	cidade = documento.findtext('city')
	estado = documento.findtext('state')
	telefone = documento.findtext('phone')
	categoria = documento.findtext('category-base')
	subcategoria = documento.findtext('subcategory-base')
	site = documento.findtext('site')
	if site != None:
	  site = site.replace('http://www.apontador.com.br/local/redirect/?url=','')

	if nome == None: continue
	if endereco == None: continue
	if categoria == None: continue

	if aux in self.categorias:
	  if nome != None:ei.write(nome.encode('utf-8'))
	  ei.write('#')
	  if endereco != None:ei.write(endereco.encode('utf-8'))
	  ei.write('#')
	  if cidade != None:ei.write(cidade.encode('utf-8'))
	  ei.write('#')
	  if estado != None:ei.write(estado.encode('utf-8'))
	  ei.write('#')
	  if telefone != None:ei.write(telefone.encode('utf-8'))
	  ei.write('#')
	  if categoria != None:ei.write(categoria.encode('utf-8'))
	  ei.write('#')
	  if subcategoria != None:ei.write(subcategoria.encode('utf-8'))
	  ei.write('#')
	  if site != None:ei.write(urllib.unquote(site.encode('utf-8')))
	  ei.write('#')
	  ei.write(arquivo)
	  ei.write('#')
	  ei.write('\n')
	else:
	  cat = None;
	  for aux in self.categorias:
	    if nltk.metrics.distance.edit_distance(aux, categoria.encode('utf-8')) < 4:
	      cat = categoria.encode('utf-8')

	  if cat != None:
	    if nome != None:ei.write(nome.encode('utf-8'))
	    ei.write('#')
	    if endereco != None:ei.write(endereco.encode('utf-8'))
	    ei.write('#')
	    if cidade != None:ei.write(cidade.encode('utf-8'))
	    ei.write('#')
	    if estado != None:ei.write(estado.encode('utf-8'))
	    ei.write('#')
	    if telefone != None:ei.write(telefone.encode('utf-8'))
	    ei.write('#')
	    if categoria != None:ei.write(categoria.encode('utf-8'))
	    ei.write('#')
	    if subcategoria != None:ei.write(subcategoria.encode('utf-8'))
	    ei.write('#')
	    if site != None:ei.write(urllib.unquote(site.encode('utf-8')))
	    ei.write('#')
	    ei.write(arquivo)
	    ei.write('#')
	    ei.write('\n')	      
	  else:
	    if nome != None:eni.write(nome.encode('utf-8'))
	    eni.write('#')
	    if endereco != None:eni.write(endereco.encode('utf-8'))
	    eni.write('#')
	    if cidade != None:eni.write(cidade.encode('utf-8'))
	    eni.write('#')
	    if estado != None:eni.write(estado.encode('utf-8'))
	    eni.write('#')
	    if telefone != None:eni.write(telefone.encode('utf-8'))
	    eni.write('#')
	    categoria = 'Outros';
	    if categoria != None:eni.write(categoria.encode('utf-8'))
	    eni.write('#')
	    subcategoria = None;
	    if subcategoria != None:eni.write(subcategoria.encode('utf-8'))
	    eni.write('#')
	    if site != None:eni.write(site.encode('utf-8'))
	    eni.write('#')
	    eni.write(arquivo)
	    eni.write('#')
	    eni.write('\n')

    ei.close()
    eni.close()
  