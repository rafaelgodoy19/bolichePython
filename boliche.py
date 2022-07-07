def mostraPista(pinos):
    for i in pinos:
        print(i, end='')
    print()
       
pista = [
    'I',' ','I',' ','I',' ','I','\n',
    ' ','I',' ','I',' ','I',' ','\n',
    ' ',' ','I',' ','I',' ',' ','\n',
    ' ',' ',' ','I',
]

posicaoPinos = {
    '1': 27,
    '2': 18,
    '3': 20,
    '4': 9,
    '5': 11,
    '6': 13,
    '7': 0,
    '8': 2,
    '9': 4,
    '10': 6,
}

mostraPista(pista)

jogada = ['3','5','9']

for pino in jogada:
    posicao = posicaoPinos[pino]
    pista[posicao] = ' '
print()

print("Depois da jogada\n")
mostraPista(pista)