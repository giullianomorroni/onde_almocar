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
perfil_cliente.barulho = 5
perfil_cliente.preco_medio = 20.0
perfil_cliente.conforto = 5

print '\nRestaurantes filtrados:'
restaurantes = minimizar.executar(restaurantes, perfil_cliente)
for r in restaurantes:
  print r.nome


