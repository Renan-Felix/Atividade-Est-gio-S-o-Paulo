# Dicionário com o faturamento mensal por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Cálculo do faturamento total
faturamento_total = 0  # Inicializando com 0

# Soma os valores de faturamento de cada estado
for valor in faturamento_por_estado.values():
    faturamento_total += valor

# Exibe o faturamento total
print(f"Faturamento total: R$ {faturamento_total:.2f}\n")

# Cálculo e exibição do percentual de representação de cada estado
print("Percentual de representação por estado:")
for estado, valor in faturamento_por_estado.items():
    percentual = (valor / faturamento_total) * 100  # Calcula o percentual
    print(f"{estado}: {percentual:.2f}%")  # Exibe o percentual formatado