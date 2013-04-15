# -*- coding: utf-8 -*-

#configuracao de paths
import os
import sys
import django.core.handlers.wsgi
from cliente import Cliente
from perfil_cliente import PerfilCliente

sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/modelos/')

#inicio da carga

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
#TODO conectar no mongo e persistir
json_data;


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
#TODO conectar no mongo e persistir
json_data;


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
#TODO conectar no mongo e persistir
json_data;


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
#TODO conectar no mongo e persistir
json_data;


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
#TODO conectar no mongo e persistir
json_data;