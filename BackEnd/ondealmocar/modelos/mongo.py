# -*- coding: utf-8 -*-

from pymongo import MongoClient, GEO2D
from controladores.filtro import Filtro
from perfil_cliente import PerfilCliente
import json

class Mongo():

    global base

    def __init__(self):
        conexao = MongoClient('localhost', 48019)
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

    def pesquisar_cliente_por_email(self, emailParam):
        colecao = self.base.cliente
        r = colecao.find_one( {"email" : emailParam} )
        print r
        _id = r["_id"]
        r["_id"] = None
        r["id"] = str(_id)
        return r

    def pesquisar_locais(self, filtro):
        colecao = self.base.cliente
        results = colecao.find( filtro )
        return results

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