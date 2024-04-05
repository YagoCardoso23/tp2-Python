entrada = input("Digite uma sequência de números inteiros separados por vírgulas: ")


numeros_str = entrada.split(',')


numeros = [int(numero) for numero in numeros_str]


print("A saída será:", numeros)
