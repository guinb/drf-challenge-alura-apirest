from orcamento.models import Receita, Despesa

def receita_existe(descricao, data, valor):
    is_receita = Receita.objects.filter(descricao = descricao, valor = valor, 
                        data__month = data.month, data__year = data.year).exists()
    
    return is_receita

def despesa_existe(descricao, data, valor):
    is_despesa = Despesa.objects.filter(descricao = descricao, valor = valor,
                        data__month = data.month, data__year = data.year).exists()

    return is_despesa