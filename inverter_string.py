# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""  # Inicializa a string invertida como vazia
    for i in range(len(s) - 1, -1, -1):  # Itera sobre a string de trás para frente
        string_invertida += s[i]  # Adiciona cada caractere à nova string
    return string_invertida

# Entrada do usuário
entrada_usuario = input("Informe uma string para inverter: ")

# Se o usuário não informar nada, pediremos para informar uma string válida
if entrada_usuario == "":
    print('Informe uma string válida')

# Invertendo a string
resultado = inverter_string(entrada_usuario)

# Exibindo o resultado
print(f"String original: {entrada_usuario}")
print(f"String invertida: {resultado}")