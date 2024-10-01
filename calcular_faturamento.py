import json

# Função para analisar o faturamento
def analisar_faturamento(faturamento):
    # Filtra os valores que não são nulos
    faturamento_validos = [valor for valor in faturamento if valor is not None]
    
    if not faturamento_validos:
        return None, None, 0  # Caso não haja faturamento válido

    # Cálculo do menor e maior faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    # Cálculo da média mensal
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    # Contagem de dias com faturamento superior à média
    dias_superior_media = sum(1 for dia in faturamento_validos if dia > media_mensal)

    return menor_faturamento, maior_faturamento, media_mensal, dias_superior_media

# Lendo o arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

# Extraindo o faturamento diário
faturamento_diario = [registro['valor'] for registro in dados['faturamento']]

# Analisando o faturamento
menor, maior, media, dias_superior = analisar_faturamento(faturamento_diario)

# Exibindo os resultados
if menor is not None:
    print(f"Menor faturamento: R$ {menor}")
    print(f"Maior faturamento: R$ {maior}")
    print(f"Média mensal: R$ {media:.2f}")
    print(f"Número de dias com faturamento superior à média: {dias_superior}")
else:
    print("Não há faturamento válido para análise.")