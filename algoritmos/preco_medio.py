# -*- coding: utf-8 -*-

class PrecoMedio():

  def minimizar(self, valores, perfilCliente):
    resultado = []
    for v in valores:
      if (v.perfil_restaurante.preco_medio == perfilCliente.preco_medio):
	resultado.append(v);
      if ( (v.perfil_restaurante.preco_medio+3.0) == perfilCliente.preco_medio):
	resultado.append(v);
      if ( (v.perfil_restaurante.preco_medio-3.0) == perfilCliente.preco_medio):
	resultado.append(v);	
    return resultado;
