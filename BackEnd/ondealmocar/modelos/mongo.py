# -*- coding: utf-8 -*-

from pymongo import MongoClient, GEO2D
from perfil_cliente import PerfilCliente
import json

class Mongo():

    global base

    def __init__(self):
        conexao = MongoClient('localhost', 48019)
        self.base = conexao.onde_almocar
        self.base.restaurante.ensure_index([("loc", "2d")])

    def inserir_local(self, json_data):
        colecao = self.base.restaurante
        r = colecao.insert(json_data)
        return r

    def inserir_cliente(self, json_data):
        colecao = self.base.cliente
        r = colecao.insert(json_data)
        return r

    def inserir_perfil_cliente(self, json_data):
        colecao = self.base.perfil_cliente
        r = colecao.insert(json_data)
        return r

    def pesquisar_cliente_por_email(self, emailParam):
        colecao = self.base.cliente
        r = colecao.find_one( {"email" : emailParam} )
        if r == None:
            return '{"code":204, "message":"nothing"}'
        _id = r["_id"]
        r["_id"] = None
        r["id"] = str(_id)
        return r

    def inserir_favorito(self, json_data):
        colecao = self.base.favorito
        r = colecao.insert(json_data)
        return r

    def pesquisar_locais(self, filtro):
        CIRCUNFERENCIA_TERRA = 6371
        METROS = 1000

        r = self.base.command(
    	[  ('geoNear', 'restaurante'),
    	   ('near', [ filtro['latitude'], filtro['longitude'] ]),
    	   ('maxDistance', (1000 / CIRCUNFERENCIA_TERRA)) ,
    	   ('distanceMultiplier', (CIRCUNFERENCIA_TERRA * METROS)),
           ('spherical', 'true'),
           ('sort', 'dis')
    	])

        return r
