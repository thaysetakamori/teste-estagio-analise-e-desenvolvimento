# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def load_json(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados

def calcular_faturamento(dados):
    faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len([dia for dia in dados])
    dias_acima_da_media = len([dia for dia in faturamento_diario if dia > media_mensal])
    return menor_faturamento, maior_faturamento, dias_acima_da_media

arquivo = 'dados.json'

dados_faturamento = load_json(arquivo)
menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)

print("Menor valor de faturamento ocorrido em um dia do mês: R$", menor)
print("Maior valor de faturamento ocorrido em um dia do mês: R$", maior)
print("Número de dias com faturamento superior à média mensal:", dias_acima_media)