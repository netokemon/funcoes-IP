inputCoordenadas = input("Insira as Coordenadas X e Y como: X,Y\n ").split(",")
xUser = int(inputCoordenadas[0])
yUser = int(inputCoordenadas[1])

def distanciaPontos(X, Y):
    print((X**2 + Y**2) ** 0.5)

distanciaPontos(xUser, yUser)
