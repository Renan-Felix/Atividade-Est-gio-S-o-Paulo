# Função para calcular a sequência de Fibonacci até um número específico
def calcular_fibonacci(n):
    comeco_sequencia = [0, 1]  # Começo da sequência

    while True:
        proximo_valor = comeco_sequencia[-1] + comeco_sequencia[-2]  # Próximo valor é a soma dos dois anteriores
        if proximo_valor > n:  # Se o próximo valor ultrapassar n, paramos
            break
        comeco_sequencia.append(proximo_valor)  # Adiciona o próximo valor à sequência

    return comeco_sequencia

# Função para verificar se um número está na sequência de Fibonacci
def verificar_numero_fibonacci(num):
    gera_sequencia = calcular_fibonacci(num)  # Gera a sequência até o número informado
    return num in gera_sequencia # Retorna True se o número está na sequência

# Entrada do usuário
try:
    numero_informado = int(input("Informe um número: "))  
    if verificar_numero_fibonacci(numero_informado):  
        print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número válido.")  # Trata entradas inválidas


