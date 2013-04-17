# -*- coding: utf-8 -*-

#configuracao de paths
import os
import sys
import django.core.handlers.wsgi
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/modelos/')
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/algoritmos/')


#inicio do teste
from distancia import Distancia

calculo = Distancia()
d = calculo.calculoDistancia(-19.919978, -43.975654, -19.920008, -43.974699)
print d