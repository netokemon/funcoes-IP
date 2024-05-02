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


#2. questão TENTATIVA DE AUTOMATIZAR MAS N SEI SE FICOU BOM (erro se colocar 64x64)

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


