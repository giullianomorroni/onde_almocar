# -*- coding: utf-8 -*-

class Distancia():

  def minimizar(self, valores, perfilCliente):

    if not perfilCliente.ordenar_distancia:
      return valores    

    resultado = []
    for v in valores:
      if (v.caracteristica.distancia < 100):
	v.pontuacao += 3
      elif (v.caracteristica.distancia > 100 and v.caracteristica.distancia < 500):
	v.pontuacao += 2
      elif (v.caracteristica.distancia > 500):
	v.pontuacao += 1
      resultado.append(v);
    return resultado;
