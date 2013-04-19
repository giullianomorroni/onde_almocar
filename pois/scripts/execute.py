#! /usr/bin/env python
# -*- coding: utf-8 -*-

#from limpeza_base import Limpeza
#from unificacao_estabelecimentos import Limpeza
#from criacao_estabelecimentos import Criacao
from normalizacao_endereco import NormalizacaoEndereco
#from limpeza_base_endereco import LimpezaEndereco

#l = Limpeza()
#l.read()

#c = Criacao()
#c.execute()

e = NormalizacaoEndereco()
e.read()

#le = LimpezaEndereco()
#le.read()
