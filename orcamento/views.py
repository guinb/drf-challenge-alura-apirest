from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer


class ReceitasViewSet(viewsets.ModelViewSet):
    """Listagem de receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['data']
    search_fields = ['descricao']

    @action(detail=False, methods=['get'], url_path=r'(?P<year>\d{4})/(?P<month>\d{1,2})')
    def receita_por_mes(self, request, year, month):
        """Pegando receitas por mês"""
        receitas = Receita.objects.filter(data__year = year, data__month = month)
        if not receitas:
            return Response(status = status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(receitas)

        if page is not None:
            serializer = self.get_serializer(page, many = True, context = {'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(receitas, many = True, context = {'request': request})
        return Response(serializer.data)


class DespesasViewSet(viewsets.ModelViewSet):
    """Listagem de despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['data']
    search_fields = ['descricao']

    @action(detail=False, methods=['get'], url_path=r'(?P<year>\d{4})/(?P<month>\d{1,2})')
    def despesa_por_mes(self, request, year, month):
        """Pegando despesas por mês"""
        despesas = Despesa.objects.filter(data__year=year, data__month=month)
        if not despesas:
            return Response(status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(despesas)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(despesas, many=True, context={'request': request})
        return Response(serializer.data)


class SumarioViewSet(APIView):
    """Sumário do mês"""
    queryset = Receita.objects.none()

    def get(self, request, year, month):
        despesas_valor_total = Despesa.objects.filter(data__year = year, 
                data__month = month).aggregate(Sum('valor'))['valor__sum'] or 0
        receitas_valor_total = Receita.objects.filter(data__year = year,
                data__month = month).aggregate(Sum('valor'))['valor__sum'] or 0
        despesas_por_categoria = Despesa.objects.filter(data__year = year, 
                data__month = month).values('categoria').annotate(Sum('valor'))
        balanco = receitas_valor_total - despesas_valor_total

        for despesa_c in despesas_por_categoria:
            despesa_c['valor'] = despesa_c['valor__sum']
            del despesa_c['valor__sum']

        return Response({
            'despesas_totais': despesas_valor_total,
            'receitas_totais': receitas_valor_total,
            'balanco': balanco,
            'despesa_por_categoria': despesas_por_categoria
        })