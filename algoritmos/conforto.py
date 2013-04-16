# -*- coding: utf-8 -*-

class Conforto():

  def minimizar(self, valores, perfilCliente):
    resultado = []
    for v in valores:
      if (v.perfil_restaurante.conforto == perfilCliente.conforto):
	resultado.append(v);
      elif ( (v.perfil_restaurante.conforto +2) == perfilCliente.conforto):
	resultado.append(v);
      elif ( (v.perfil_restaurante.conforto -2) == perfilCliente.conforto):
	resultado.append(v);	
    return resultado;
