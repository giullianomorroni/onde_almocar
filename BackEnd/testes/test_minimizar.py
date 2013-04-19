# -*- coding: utf-8 -*-

#configuracao de paths
import os
import sys
import django.core.handlers.wsgi
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/modelos/')
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/algoritmos/')
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/carga_dados/')


#inicio do teste
from minimizar import Minimizar
from perfil_cliente import PerfilCliente

import carga_restaurante as cr

print '\nTodos os restaurantes:'
restaurantes = cr.carga()
for r in restaurantes:
  print r.nome

minimizar = Minimizar();

perfil_cliente = PerfilCliente();
perfil_cliente.barulho = 7
perfil_cliente.preco_medio = 10.0
perfil_cliente.conforto = 5

perfil_cliente.ordenar_barulho = True
perfil_cliente.ordenar_conforto = True
perfil_cliente.ordenar_preco_medio = True

perfil_cliente.ordenar_distancia = False
perfil_cliente.latitude = -23.567360
perfil_cliente.longitude = -46.649408

perfil_cliente.somente_favorito = False
perfil_cliente.somente_espaco_proprio = False

print '\nRestaurantes filtrados:'
restaurantes = minimizar.executar(restaurantes, perfil_cliente)
restaurantes = sorted(restaurantes, key=lambda r: r.pontuacao, reverse=True)
for r in restaurantes:
  print r.nome + ' [pontuacao: '+ str(r.pontuacao)+']' + ' [distancia: '+ str(r.caracteristica.distancia)+']'
