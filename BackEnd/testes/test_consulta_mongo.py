# -*- coding: utf-8 -*-

#configuracao de paths
import os
import sys
import django.core.handlers.wsgi
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/BackEnd/modelos')
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/BackEnd/algoritmos/')
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/BackEnd/controladores/')

#inicio do teste
from mongo import Mongo
from filtro import Filtro

f = Filtro()
f.latitude = -23.565118
f.longitude = -46.652069

m = Mongo()
resultado = m.pesquisar_restaurante(f)

print resultado