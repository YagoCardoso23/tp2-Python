def operacoes_aritmeticas(num1, num2):
  
    soma = num1 + num2

   
    subtracao = num1 - num2

    
    multiplicacao = num1 * num2

  
    if num2 != 0:
      
        divisao = num1 / num2
       
        resto = num1 % num2
    else:
      
        divisao = None
        resto = None

    
    return soma, subtracao, multiplicacao, divisao, resto


num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

resultados = operacoes_aritmeticas(num1, num2)


print("Soma:", resultados[0])
print("Subtração:", resultados[1])
print("Multiplicação:", resultados[2])
print("Divisão:", resultados[3])
print("Resto da divisão:", resultados[4])
