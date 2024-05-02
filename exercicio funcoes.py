#1. questão

def borda():
    print("+ - - - - + - - - - +")

def linhas():
    for x in range(4):
        print("|         |         |")

def montar():
    
   borda()
   linhas()
   borda()
   linhas()
   borda()

montar()

print("FIM DA PRIMEIRA QUESTÃO")

#2. questão

def borda():
    print("+ - - - - + - - - - " * 2 + "+")


def linhas():
    for x in range(4):
        print("|         |         " * 2 + "|")

def montar():
    borda()
    linhas()
    borda()
    linhas()
    borda()
    linhas()
    borda()
    linhas()
    borda()

montar()

print("FIM DA SEGUNDA QUESTÃO")


#2. questão TENTATIVA DE AUTOMATIZAR MAS N SEI SE FICOU BOM (bug se colocar 64x64)

coluna = ""
quantidadeLinhas = int(input("QUANTIDADE DE LINHAS?"))
quantidadeColunas = int(input("QUANTIDADE DE COLUNAS?"))

def borda(quantidadeColunas):
    global coluna
    coluna = "+ - - - - "
    print(coluna * quantidadeColunas + "+")


def linha(quantidadeColunas):
    for x in range(4):
        print("|         " * quantidadeColunas + "|")

def montar():
    for x in range(quantidadeLinhas):
        borda(quantidadeColunas)
        linha(quantidadeColunas)
        #borda(quantidadeColunas)
    print(coluna * quantidadeColunas + "+")

montar()

print("FIM DA SEGUNDA QUESTÃO AUTOMATIZADA")


#3. Questão

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
print("FIM DA TERCEIRA QUESTAO")

#4. Questão

inputCoordenadas = input("Insira as Coordenadas: ").split(" ")
xUser = int(inputCoordenadas[0])
yUser = int(inputCoordenadas[1])

def distanciaPontos(X, Y):
    print((X**2 + Y**2) ** 0.5)

distanciaPontos(xUser, yUser)

print("FIM DA QUARTA QUESTÃo")

#5. Questão

saldo = 0.0

print("Empresa VEM onibus de neto")

print("INSIRA O VALOR DA SUA PRIMEIRA RECARGA")

def mostrarSaldo():
    global saldo
    print("Seu saldo atual é {:.2f}".format(saldo))

def adicionarSaldo(valorAdicionado):
    global saldo
    saldo += valorAdicionado
    mostrarSaldo()

def usarCartao():
    global saldo
    saldo -= 4.10
    mostrarSaldo()

adicionarSaldo(float(input()))
usarCartao()

print("FIM DA QUINTA QUESTÃO")




    

