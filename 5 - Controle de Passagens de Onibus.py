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

def usarCartao(valorPassagem, qntPassagens):
    global saldo

    if saldo >= valorPassagem * qntPassagens:
        saldo -= valorPassagem * qntPassagens
    else:
        print("Saldo insuficiente para esta operação.")
    
    mostrarSaldo()

adicionarSaldo(float(input()))
usarCartao(float(input("Insira o Valor da Passagem: ")), float(input("\nInsira a quantidade de passagens utilizadas: ")))
