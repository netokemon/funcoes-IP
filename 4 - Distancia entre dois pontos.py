inputCoordenadas = input("Insira as Coordenadas X1,Y1,X2,Y2\n ").split(",")
x1User = int(inputCoordenadas[0])
y1User = int(inputCoordenadas[1])
x2User = int(inputCoordenadas[2])
y2User = int(inputCoordenadas[3])

def distanciaPontos(X1, Y1, X2, Y2):
    print(((X2 - X1)**2 + (Y2-Y1)**2)** 0.5)

distanciaPontos(x1User, y1User, x2User, y2User)
