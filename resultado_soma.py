#Declaração das variáveis para a inicialiação do laço.
indice = 13
soma = 0
k = 0

#Processamento do laço de repetição

while k < indice:
    k = k + 1
    soma = soma + k


#Impressão do resultado da soma
def resultado_soma():
    print(f'O valor da variável soma foi de {soma}')

def main():
    resultado_soma()


if __name__ == '__main__':
    main()
