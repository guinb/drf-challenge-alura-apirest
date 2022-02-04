from rest_framework import serializers
from orcamento.models import Receita, Despesa
from orcamento.validators import receita_existe, despesa_existe

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'data']

    def validate(self, attrs):
        if receita_existe(attrs['descricao'], attrs['data'], attrs['valor']):
            raise serializers.ValidationError('Receita já existe neste mês')
        return attrs

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'data', 'categoria']

    def validate(self, attrs):
        if despesa_existe(attrs['descricao'], attrs['data'], attrs['valor']):
            raise serializers.ValidationError('Despesa já existe neste mês')
        return attrs