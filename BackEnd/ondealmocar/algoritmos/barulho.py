# -*- coding: utf-8 -*-

class Barulho():

    def minimizar(self, valores, perfilCliente):
    
        if not perfilCliente.ordenar_barulho:
            return valores
        
        resultado = []
        for v in valores:
            if (v.perfil_restaurante.barulho == perfilCliente.barulho):
                v.pontuacao += 1
            elif ( (v.perfil_restaurante.barulho+2) == perfilCliente.barulho):
                v.pontuacao += 0.5
            elif ( (v.perfil_restaurante.barulho-2) == perfilCliente.barulho):
                v.pontuacao += 0.5
        resultado.append(v);
        return resultado;
