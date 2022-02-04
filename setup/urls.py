from django.contrib import admin
from django.urls import path, include
from orcamento.views import ReceitasViewSet, DespesasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('resumo/', include('orcamento.urls'))
]
