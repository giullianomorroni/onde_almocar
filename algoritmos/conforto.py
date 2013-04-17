# -*- coding: utf-8 -*-

class Conforto():

  def minimizar(self, valores, perfilCliente):
    
    if not perfilCliente.ordenar_conforto:
      return valores
    
    resultado = []
    for v in valores:
      if (v.perfil_restaurante.conforto == perfilCliente.conforto):
	v.pontuacao += 1
      elif ( (v.perfil_restaurante.conforto +2) == perfilCliente.conforto):
	v.pontuacao += 0.5
      elif ( (v.perfil_restaurante.conforto -2) == perfilCliente.conforto):
	v.pontuacao += 0.5
      resultado.append(v);
    return resultado;
