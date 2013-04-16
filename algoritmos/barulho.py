# -*- coding: utf-8 -*-

class Barulho():

  def minimizar(self, valores, perfilCliente):
    resultado = []
    for v in valores:
      if (v.perfil_restaurante.barulho == perfilCliente.barulho):
	resultado.append(v);
      elif ( (v.perfil_restaurante.barulho+2) == perfilCliente.barulho):
	resultado.append(v);
      elif ( (v.perfil_restaurante.barulho-2) == perfilCliente.barulho):
	resultado.append(v);
    return resultado;
