# -*- coding: utf-8 -*-

#configuracao de paths
import os
import sys
import json
from restaurante import Restaurante
from endereco import Endereco
from perfil_restaurante import PerfilRestaurante
from caracteristica import Caracteristica

sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/modelos/')

restaurantes = []

def carga():
  #inicio da carga
  r = Restaurante()
  r.nome = 'Restaurante 1'
  r.site = 'www.site.com.br'
  r.telefone = '11 99994444'
  r.horario = '8h - 22h'
  r.descricao = 'Descrição....'

  e = Endereco()
  e.logradouro = 'Av. Brg. Luís Antônio'
  e.numero = '2250'
  e.complemento = ''
  e.cep = '01418100'
  e.latitude = -23.568206
  e.longitude = -46.649441
  e.bairro = 'Jardim Paulista'
  e.cidade = 'São Paulo'
  e.estado = 'São Paulo'
  r.endereco = e;

  pf = PerfilRestaurante()
  pf.preco_medio = 20.0
  pf.conforto = 5
  pf.barulho = 5
  pf.categoria = 'diversos'
  pf.tipo = 'padaria'
  pf.espaco_proprio = True
  r.perfil_restaurante = pf
  
  c = Caracteristica()
  c.distancia = 150.00
  c.primeira_vez = False
  c.favorito = True
  r.caracteristica = c
  restaurantes.append(r)





  r = Restaurante()
  r.nome = 'Restaurante 2'
  r.site = 'www.site.com.br'
  r.telefone = '11 99994444'
  r.horario = '8h - 22h'
  r.descricao = 'Descrição....'

  e = Endereco()
  e.logradouro = 'Alameda Santos'
  e.numero = '760'
  e.complemento = ''
  e.cep = '01418100'
  e.latitude = -23.567606
  e.longitude = -46.650985
  e.bairro = 'Jardim Paulista'
  e.cidade = 'São Paulo'
  e.estado = 'São Paulo'
  r.endereco = e;

  pf = PerfilRestaurante()
  pf.preco_medio = 30.0
  pf.conforto = 10
  pf.barulho = 7
  pf.categoria = 'self-service'
  pf.tipo = 'restaurante'
  pf.espaco_proprio = True
  r.perfil_restaurante = pf

  c = Caracteristica()
  c.distancia = 50.00
  c.primeira_vez = True
  c.favorito = False
  r.caracteristica = c
  restaurantes.append(r)










  r = Restaurante()
  r.nome = 'Restaurante 3'
  r.site = 'www.site.com.br'
  r.telefone = '11 99994444'
  r.horario = '8h - 22h'
  r.descricao = 'Descrição....'

  e = Endereco()
  e.logradouro = 'R. Cincinato Braga'
  e.numero = '388'
  e.complemento = ''
  e.cep = '01333010'
  e.latitude = -23.567144
  e.longitude = -46.647348
  e.bairro = 'Bela Vista'
  e.cidade = 'São Paulo'
  e.estado = 'São Paulo'
  r.endereco = e;

  pf = PerfilRestaurante()
  pf.preco_medio = 15.0
  pf.conforto = 2
  pf.barulho = 2
  pf.categoria = 'self-service'
  pf.tipo = 'restaurante'
  pf.espaco_proprio = True
  r.perfil_restaurante = pf

  c = Caracteristica()
  c.distancia = 601.20
  c.primeira_vez = True
  c.favorito = False
  r.caracteristica = c
  restaurantes.append(r)





  r = Restaurante()
  r.nome = 'Restaurante 4'
  r.site = 'www.site.com.br'
  r.telefone = '11 99994444'
  r.horario = '8h - 22h'
  r.descricao = 'Descrição....'

  e = Endereco()
  e.logradouro = 'Av Paulista'
  e.numero = '615'
  e.complemento = ''
  e.cep = '01311000'
  e.latitude = -23.567360
  e.longitude = -46.649408
  e.bairro = 'Bela Vista'
  e.cidade = 'São Paulo'
  e.estado = 'São Paulo'
  r.endereco = e;

  pf = PerfilRestaurante()
  pf.preco_medio = 25.0
  pf.conforto = 5
  pf.barulho = 5
  pf.categoria = 'típica'
  pf.tipo = 'restaurante'
  pf.espaco_proprio = False
  r.perfil_restaurante = pf

  c = Caracteristica()
  c.distancia = 400.00
  c.primeira_vez = True
  c.favorito = True
  r.caracteristica = c
  restaurantes.append(r)









  r = Restaurante()
  r.nome = 'Lanchonete 1'
  r.site = 'www.site.com.br'
  r.telefone = '11 99994444'
  r.horario = '8h - 22h'
  r.descricao = 'Descrição....'

  e = Endereco()
  e.logradouro = 'Av Paulista'
  e.numero = '1000'
  e.complemento = ''
  e.cep = '01311000'
  e.latitude = -23.565118
  e.longitude = -46.652069
  e.bairro = 'Bela Vista'
  e.cidade = 'São Paulo'
  e.estado = 'São Paulo'
  r.endereco = e;

  pf = PerfilRestaurante()
  pf.preco_medio = 10.0
  pf.conforto = 2
  pf.barulho = 10
  pf.categoria = 'diversos'
  pf.tipo = 'lanchonete'
  pf.espaco_proprio = False
  r.perfil_restaurante = pf
  
  c = Caracteristica()
  c.distancia = 700.00
  c.primeira_vez = True
  c.favorito = False
  r.caracteristica = c
  restaurantes.append(r)







  r = Restaurante()
  r.nome = 'Restaurante 5'
  r.site = 'www.site.com.br'
  r.telefone = '11 99994444'
  r.horario = '8h - 22h'
  r.descricao = 'Descrição....'

  e = Endereco()
  e.logradouro = 'Av. Brg. Luís Antônio'
  e.numero = '2300'
  e.complemento = ''
  e.cep = '01418100'
  e.latitude = -23.568206
  e.longitude = -46.649441
  e.bairro = 'Jardim Paulista'
  e.cidade = 'São Paulo'
  e.estado = 'São Paulo'
  r.endereco = e;

  pf = PerfilRestaurante()
  pf.preco_medio = 25.0
  pf.conforto = 5
  pf.barulho = 7
  pf.categoria = 'prato-feito'
  pf.tipo = 'restaurante'
  pf.espaco_proprio = True
  r.perfil_restaurante = pf
  
  c = Caracteristica()
  c.distancia = 70.00
  c.primeira_vez = True
  c.favorito = False
  r.caracteristica = c
  restaurantes.append(r)


  return restaurantes