# -*- coding: utf-8 -*-

#configuracao de paths
import sys
sys.path.append('/home/giulliano/Desktop/onde_almocar/onde_almocar/modelos/')


#inicio do teste
from cliente import Cliente
from perfil_cliente import PerfilCliente

p = PerfilCliente()
p.preco_medio = 10.0
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
print 'json_data:'
print json_data

clazz = c.extrair_classe(json_data)
print 'classe#nome:'
print clazz.nome