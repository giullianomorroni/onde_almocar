# -*- coding: utf-8 -*-

import sys

sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/modelos/')
sys.path.append('/run/media/giulliano/Desenvolvimento/workspace/python/onde_almocar/BackEnd/ondealmocar/')
sys.path.append('/run/media/giulliano/Desenvolvimento/workspace/python/onde_almocar/BackEnd/ondealmocar/modelos/')

#configuracao de paths
from cliente import Cliente
from perfil_cliente import PerfilCliente
from mongo import Mongo

#inicio da carga
mongo = Mongo();

p = PerfilCliente()
p.preco_medio = 30.0
p.conforto = 2
p.barulho = 5
c = Cliente()
c.nome = 'Giulliano'
c.email = 'giulliano@gmail.com'
c.perfil_cliente = p;
c.almocos = [1,2,3];
c.amigos = [1,2,3];
c.favoritos = [1,2,3];
json_data = c.extrair_json()
mongo.inserir_cliente(json_data);


p = PerfilCliente()
p.preco_medio = 15.0
p.conforto = 7
p.barulho = 5
c = Cliente()
c.nome = 'Pauline'
c.email = 'pauline@gmail.com'
c.perfil_cliente = p;
c.almocos = [1,2,3];
c.amigos = [1,2,3];
c.favoritos = [1,2,3];
json_data = c.extrair_json()
mongo.inserir_cliente(json_data);


p = PerfilCliente()
p.preco_medio = 20.0
p.conforto = 2
p.barulho = 5
c = Cliente()
c.nome = 'Joyce'
c.email = 'joyce@gmail.com'
c.perfil_cliente = p;
c.almocos = [1,2,3];
c.amigos = [];
c.favoritos = [];
json_data = c.extrair_json()
mongo.inserir_cliente(json_data);


p = PerfilCliente()
p.preco_medio = 10.0
p.conforto = 2
p.barulho = 5
c = Cliente()
c.nome = 'Soraya'
c.email = 'soraya@gmail.com'
c.perfil_cliente = p;
c.almocos = [1,2];
c.amigos = [];
c.favoritos = [1];
json_data = c.extrair_json()
mongo.inserir_cliente(json_data);


p = PerfilCliente()
p.preco_medio = 10.0
p.conforto = 2
p.barulho = 5
c = Cliente()
c.nome = 'Eduardo'
c.email = 'eduardo@gmail.com'
c.perfil_cliente = p;
c.almocos = [3];
c.amigos = [1];
c.favoritos = [1,2,3];
json_data = c.extrair_json()
mongo.inserir_cliente(json_data);
