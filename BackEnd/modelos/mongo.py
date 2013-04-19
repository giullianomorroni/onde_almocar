# -*- coding: utf-8 -*-

from pymongo import MongoClient
from filtro import Filtro
from perfil_cliente import PerfilCliente

class Mongo():

  def __init__(self):
    conexao = MongoClient('localhost', 27017)
    base = client.onde_almocar

  def inserir_restaurante(self, json_data):
    colecao = base.restaurante
    colecao.ensureIndex( { {'endereco':'loc'} : "2d"} )
    r = colecao.insert(json_data)
    return r

  def inserir_cliente(self, json_data):
    colecao = base.cliente
    r = colecao.insert(json_data)
    return r

  def inserir_favorito(self, json_data):
    colecao = base.favorito
    r = colecao.insert(json_data)
    return r

  def pesquisar_restaurante(self, filtro):
    CIRCUNFERENCIA_TERRA = 6371
    METROS = 1000
    r = base.runCommand(
	{ 
	  'geoNear' : 'restaurante',
	  'near' : {[ filtro.longitude, filtro.latitude ]} ,
	  'maxDistance': 1000 / CIRCUNFERENCIA_TERRA,
	  'distanceMultiplier': CIRCUNFERENCIA_TERRA * METROS,
          'spherical': True,
          'sort': 'dis'
	})
    return r