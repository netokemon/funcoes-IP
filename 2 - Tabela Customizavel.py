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

coluna = ""
quantidadeLinhas = int(input("QUANTIDADE DE LINHAS? "))
quantidadeColunas = int(input("QUANTIDADE DE COLUNAS? "))

def borda(quantidadeColunas):
    global coluna
    coluna = "+ - - - - "
    print(coluna * quantidadeColunas + "+")


def linha(quantidadeColunas):
    for x in range(4):
        print("|         " * quantidadeColunas + "|")

def montar():
    for x in range(max(quantidadeLinhas, quantidadeColunas)):
        borda(quantidadeColunas)
        linha(quantidadeColunas)
        #borda(quantidadeColunas)
    print(coluna * quantidadeColunas + "+")

montar()
