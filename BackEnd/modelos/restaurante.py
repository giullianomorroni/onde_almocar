# -*- coding: utf-8 -*-
import json
from endereco import Endereco
from perfil_restaurante import PerfilRestaurante
from caracteristica import Caracteristica

class Restaurante():

  global nome
  global site
  global email
  global telefone
  global horario
  global descricao
  global endereco
  global perfil_restaurante
  global caracteristica
  global pontuacao

  def __init__(self):
    self.nome = ''
    self.site = ''
    self.email = ''
    self.telefone = ''
    self.horario = ''
    self.descricao = ''
    self.endereco = None
    self.perfil_restaurante = None
    self.caracteristica = None
    self.pontuacao = 0

  def extrair_classe(self, json_data):
    aux = json.loads(json_data)
    self.nome = aux['nome']
    self.site = aux['site']
    self.telefone = aux['telefone']
    self.horario = aux['horario']
    self.descricao = aux['descricao']
    _endereco = aux['endereco']
    self.endereco = Endereco().extrair_classe(_endereco)
    _pf = aux['perfil_restaurante']
    self.perfil_restaurante = PerfilRestaurante().extrair_classe(_pf)
    _caract = aux['caracteristica']
    self.caracteristica = Caracteristica().extrair_classe(_caract)
    return self

  def extrair_json(self):
    _end = None
    _pf = None
    _caract = None

    if (self.endereco != None):
      _end = self.endereco.extrair_json()

    if (self.perfil_restaurante != None):
      _pf = self.perfil_restaurante.extrair_json()

    if (self.caracteristica != None):
      _caract = self.caracteristica.extrair_json()

    js_dt = json.dumps(
      {
	"nome" : self.nome,
	"site" : self.site,
	"telefone" : self.telefone,
	"horario" : self.horario,
	"descricao" : self.descricao,
	"endereco" : _end,
	"perfil_restaurante" : _pf,
	"caracteristica" : _caract
      },
      ensure_ascii=False
    )
    return json.loads(js_dt)