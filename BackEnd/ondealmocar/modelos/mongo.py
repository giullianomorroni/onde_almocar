# -*- coding: utf-8 -*-

from pymongo import MongoClient, GEO2D
from filtro import Filtro
from perfil_cliente import PerfilCliente

class Mongo():

    global base

    def __init__(self):
        conexao = MongoClient('localhost', 27017)
        self.base = conexao.onde_almocar
        self.base.restaurante.ensure_index([("loc", "2d")])

    def inserir_restaurante(self, json_data):
        colecao = self.base.restaurante
        r = colecao.insert(json_data)
        return r

    def inserir_cliente(self, json_data):
        colecao = self.base.cliente
        r = colecao.insert(json_data)
        return r

    def inserir_favorito(self, json_data):
        colecao = self.base.favorito
        r = colecao.insert(json_data)
        return r

    def pesquisar_restaurante(self, filtro):
        CIRCUNFERENCIA_TERRA = 6371
        METROS = 1000
        r = self.base.command(
    	([
    	  ('geoNear', 'restaurante'),
    	  ('near', [filtro.longitude, filtro.latitude]),
    	  ('maxDistance', 1000 / CIRCUNFERENCIA_TERRA),
    	  ('distanceMultiplier', CIRCUNFERENCIA_TERRA * METROS),
              ('spherical', True),
              ('sort', 'dis')
    	]))
        return r