inputNumero1 = float(input("Bem vindo a calculadora do Neto, favor inserir seu primeiro número "))
inputNumero2 = float(input("Agora o segundo número, princesx: "))

def adicao(num1, num2):
    return(num1 + num2)

def subtracao(num1, num2):
    return(num1 - num2)

def divisao(num1, num2):
    return(num1 / num2)
def multiplicacao(num1, num2):
    return(num1 * num2)
def exponenciacao(num1, num2):
    return(num1 ** num2)

print("ADIÇÃO:", adicao(inputNumero1, inputNumero2), "SUBTRAÇÃO:", subtracao(inputNumero1, inputNumero2), "DIVISÃO:", divisao(inputNumero1, inputNumero2), "MULTIPLICAÇÃO:", multiplicacao(inputNumero1, inputNumero2), "EXPONENCIAÇÃO:", exponenciacao(inputNumero1, inputNumero2))
