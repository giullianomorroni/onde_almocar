# -*- coding: utf-8 -*-

class Filtro():

  global preco_medio
  global tipos
  global salao_proprio
  global quant_pessoas
  global nivel_silencio
  global nivel_conforto
  global favoritos
  global busca_exata

  def __init__(self):
    self.preco_medio = None
    self.tipos = []
    self.salao_proprio = None
    self.quant_pessoas = None
    self.nivel_silencio = None
    self.nivel_conforto = None
    self.favoritos = []
    self.busca_exata = None

  def montarFiltro(self, json_data)
    self.preco_medio = json_data['preco_medio']
    self.tipos = json_data['tipos']
    self.salao_proprio = json_data['salao_proprio']
    self.quant_pessoas = json_data['quant_pessoas']
    self.nivel_silencio = json_data['nivel_silencio']
    self.nivel_conforto = json_data['nivel_conforto']
    self.favoritos = json_data['favoritos']
    self.busca_exata = json_data['busca_exata']
