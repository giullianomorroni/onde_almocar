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
from restaurante import Restaurante
from endereco import Endereco
from perfil_restaurante import PerfilRestaurante
from caracteristica import Caracteristica

m = Mongo()

r = Restaurante()
r.nome = 'Lanchonete 1'
r.site = 'www.site.com.br'
r.telefone = '11 99994444'
r.horario = '8h - 22h'
r.descricao = 'Descrição....'

e = Endereco()
e.logradouro = 'Av Paulista'
e.numero = '1000'
e.complemento = ''
e.cep = '01311000'
e.latitude = -23.565118
e.longitude = -46.652069
e.bairro = 'Bela Vista'
e.cidade = 'São Paulo'
e.estado = 'São Paulo'
r.endereco = e;

pf = PerfilRestaurante()
pf.preco_medio = 10.0
pf.conforto = 2
pf.barulho = 10
pf.categoria = 'diversos'
pf.tipo = 'lanchonete'
pf.espaco_proprio = False
r.perfil_restaurante = pf

c = Caracteristica()
c.distancia = 700.00
c.primeira_vez = True
c.favorito = False
r.caracteristica = c
json_data = r.extrair_json()

print json_data

m.inserir_restaurante(json_data)