# -*- coding: utf-8 -*-

from barulho import Barulho
from conforto import Conforto
from preco_medio import PrecoMedio

class Minimizar():

  def executar(self, valores, perfilCliente):
    barulho = Barulho()
    conforto = Conforto()
    preco_medio = PrecoMedio()

    valores = barulho.minimizar(valores, perfilCliente)
    valores = conforto.minimizar(valores, perfilCliente)
    valores = preco_medio.minimizar(valores, perfilCliente)
    return valores
