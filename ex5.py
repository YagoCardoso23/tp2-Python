def calcular_quadrado_e_raiz(numero):
   
    quadrado = numero ** 2

    
    raiz_quadrada = numero ** 0.5

   
    return numero, quadrado, raiz_quadrada


numero_inteiro = int(input("Digite um número inteiro: "))


resultado = calcular_quadrado_e_raiz(numero_inteiro)


print("Número:", resultado[0])
print("Quadrado:", resultado[1])
print("Raiz quadrada:", resultado[2])
