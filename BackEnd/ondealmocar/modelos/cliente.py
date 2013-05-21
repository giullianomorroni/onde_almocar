# -*- coding: utf-8 -*-

import json
from perfil_cliente import PerfilCliente
from restaurante import Restaurante

class Cliente():

    global nome;
    global email;
    global perfil_cliente;
    global almocos;
    global amigos;
    global favoritos;

    def __init__(self):
        self.nome = '';
        self.email = '';
        self.perfil_cliente = None;
        self.almocos = [];
        self.amigos = [];
        self.favoritos = []; 

    def extrair_classe(self, json_data):
        aux = json.loads(json_data)
        self.nome = aux['nome'];
        self.email = aux['email'];
        self.perfil_cliente = aux['perfil_cliente'];
        self.almocos = aux['almocos'];
        self.amigos = aux['amigos'];
        self.favoritos = aux['favoritos'];
        return self

    def extrair_json(self):
        perfil = None;
        if (self.perfil_cliente != None):
            perfil = self.perfil_cliente.extrair_json();
    
        js_dt = json.dumps(
        {
        	"nome":self.nome, 
        	"email":self.email, 
        	"perfil_cliente": perfil,
        	"almocos": self.almocos,
        	"amigos": self.amigos,
        	"favoritos": self.favoritos
        }, ensure_ascii=False
        )
        return json.loads(js_dt)
