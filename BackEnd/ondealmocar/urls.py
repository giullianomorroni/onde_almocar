from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^autenticar/$', 'services.autenticar', name='autenticar'),
    url(r'^pesquisar/locais/$', 'services.pesquisar_locais', name='pesquisar_locais'),
    url(r'^cliente/inserir_perfil/$', 'services.inserir_perfil_cliente', name='inserir_perfil_cliente'),
    url(r'^local/inserir/$', 'services.inserir_local', name='inserir_local'),
    url(r'^local/favoritar/$', 'services.favoritar', name='favoritar'),
    url(r'^teste/$', 'services.teste', name='teste'),

)