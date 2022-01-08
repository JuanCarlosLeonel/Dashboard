from django.urls import path
from minha_dashboard.views import home, retorna_total_vendido, relatorio_faturamento, relatorio_produtos, relatorio_funcionario


urlpatterns = [
    path('', home, name="home"),
    path('retorna_total_vendido', retorna_total_vendido, name="retorna_total_vendido"),
    path('relatorio_faturamento', relatorio_faturamento, name="relatorio_faturamento"),
    path('relatorio_produtos', relatorio_produtos, name="relatorio_produtos"),
    path('relatorio_funcionario', relatorio_funcionario, name="relatorio_funcionario"),
]