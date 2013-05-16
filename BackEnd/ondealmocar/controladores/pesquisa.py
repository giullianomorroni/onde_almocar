# -*- coding: utf-8 -*-

from algoritmos.minimizar import Minimizar as minimizar 
from mongo import Mongo

class Pesquisa():

    def pesquisar(self, filtro, perfilCliente):
        m = Mongo()
        valores = m.pesquisar_restaurante(filtro, perfilCliente)
        valores  = minimizar.executar(valores, perfilCliente)
        return valores
