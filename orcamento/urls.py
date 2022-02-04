from django.urls import path

from orcamento.views import SumarioViewSet

urlpatterns = [
    path('<int:year>/<int:month>', SumarioViewSet.as_view(), name='sumario'),
]