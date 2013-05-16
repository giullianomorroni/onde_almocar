# -*- coding: utf-8 -*-

class PrecoMedio():

    def minimizar(self, valores, perfilCliente):

        if not perfilCliente.ordenar_preco_medio:
            return valores      

            resultado = []
        for v in valores:
            if (v.perfil_restaurante.preco_medio == perfilCliente.preco_medio):
                v.pontuacao += 1
            if ((v.perfil_restaurante.preco_medio + 3.0) == perfilCliente.preco_medio):
                v.pontuacao += 0.5
            if ((v.perfil_restaurante.preco_medio - 3.0) == perfilCliente.preco_medio):
                v.pontuacao += 0.5
                resultado.append(v);	
        return resultado;
