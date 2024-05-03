#O desafio é inverter os valores das variáveis sem usar funções ou mais do que 2 variáveis.

num1 = int(input())
num2 = int(input())

num1 += num2
num2 = num1 - num2
num1 -= num2

print(num1, num2)
