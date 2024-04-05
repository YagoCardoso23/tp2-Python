
lista_numeros = []
for i in range(10):
    numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
    lista_numeros.append(numero)


soma_quadrados = sum(numero ** 2 for numero in lista_numeros)


print("A soma dos quadrados dos elementos da lista é:", soma_quadrados)
