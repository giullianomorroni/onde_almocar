# -*- coding: utf-8 -*-

#configuracao de paths
import os
import sys
import django.core.handlers.wsgi
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/modelos/')


#inicio do teste
from endereco import Endereco

e = Endereco()
e.logradouro = 'Av Paulista'
e.numero = '615'
e.complemento = '16 andar'
e.cep = '01311000'
e.latitude = -23.6045
e.longitude = -46.6045
e.bairro = 'Bela Vista'
e.cidade = 'São Paulo'
e.estado = 'São Paulo'

json_data = e.extrair_json()
print 'json_data:'
print json_data

clazz = e.extrair_classe(json_data)
print 'classe#logradouro:'
print clazz.logradouro