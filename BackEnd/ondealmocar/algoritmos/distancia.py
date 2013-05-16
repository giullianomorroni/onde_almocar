# -*- coding: utf-8 -*-

import math

class Distancia():

    def minimizar(self, valores, perfilCliente):
    
        if not perfilCliente.ordenar_distancia:
            return valores    
        
        resultado = []
        for v in valores:
            distancia = self.calculoDistancia(v.endereco.latitude, v.endereco.longitude, perfilCliente.latitude, perfilCliente.longitude)
            v.caracteristica.distancia = distancia
            if (v.caracteristica.distancia < 100):
                v.pontuacao += 3
            elif (v.caracteristica.distancia > 100 and v.caracteristica.distancia < 500):
                v.pontuacao += 2
            elif (v.caracteristica.distancia > 500):
                v.pontuacao += 1
            resultado.append(v);
        return resultado;


    def calculoDistancia(self, latitude, longitude, latitudeCliente, longitudeCliente):
        if latitude == None or longitude == None or latitudeCliente == None or longitudeCliente == None:
            return 0;
        
        EARTH_RADIUS_KM = 6371;
        EARTH_RADIUS_M = EARTH_RADIUS_KM * 1000;
        
        #Conversão de graus pra radianos das latitudes
        latitudeEmDecimal_1 = math.radians(latitude);
        latitudeEmDecimal_2 = math.radians(latitudeCliente);
        
        #Diferença das longitudes
        diferenciaLongitudes = math.radians(longitude - longitudeCliente);
        
        #aqui usei como padrão a unidade de metros
        medida = EARTH_RADIUS_M; 
        
        #Cálcula da distância entre os pontos
        distancia = math.acos(math.cos(latitudeEmDecimal_1) 
          * math.cos(latitudeEmDecimal_2) 
          * math.cos(diferenciaLongitudes) + math.sin(latitudeEmDecimal_1)
          * math.sin(latitudeEmDecimal_2)) * medida
        
        #int lastIndexOf = distancia.toString().lastIndexOf(".");
        #String fmt = distancia.toString().substring(0, lastIndexOf);
        distancia = round(distancia, 2)
        return distancia;
