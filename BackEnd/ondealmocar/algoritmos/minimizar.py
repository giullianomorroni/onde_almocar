# -*- coding: utf-8 -*-

from barulho import Barulho
from conforto import Conforto
from preco_medio import PrecoMedio
from distancia import Distancia
from perfil_cliente import PerfilCliente

class Minimizar():

    def executar(self, valores, perfilCliente):
        if (perfilCliente == None):
            perfilCliente = PerfilCliente()
        
        barulho = Barulho()
        conforto = Conforto()
        preco_medio = PrecoMedio()
        distancia = Distancia()

        valores = barulho.minimizar(valores, perfilCliente)
        valores = conforto.minimizar(valores, perfilCliente)
        valores = preco_medio.minimizar(valores, perfilCliente)
        valores = distancia.minimizar(valores, perfilCliente)
        valores = self.exclusividade(valores, perfilCliente)
        return valores

    def exclusividade(self, valores, perfilCliente):
        '''
        Passa adiante a lista contendo somente valores
        exclusivos caso o cliente solicite preferencia
        de exclusividade.
        '''
        opcao_exclusividade = (perfilCliente.somente_favorito or perfilCliente.somente_primeira_vez or perfilCliente.somente_espaco_proprio);

        resultado = []
        for v in valores:
            if perfilCliente.somente_favorito:
                if not v.caracteristica.favorito:
                    continue

            if perfilCliente.somente_primeira_vez:
                if not v.caracteristica.primeira_vez:
                    continue

            if perfilCliente.somente_espaco_proprio:
                if not v.perfil_restaurante.espaco_proprio:
                    continue
            resultado.append(v)

            # Se o cliente selecionou ao menos um tipo de exclusividade retorna o resultado, 
            # caso contrário retorna a lista original
            if opcao_exclusividade:
                return resultado
            else:
                return valores
