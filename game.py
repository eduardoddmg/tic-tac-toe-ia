contadorJogadas = 0

array = [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]]
arrayBola = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
arrayX = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

possibilidadesX = []
possibilidadesO = []

pertoGanharX = []
pertoGanharO = []

posicoes = []
jogadas = ['11', '00', '02', '22', '20']

def scanBola():
    print("digite a posicao do valor que voce quer inserir a bola O")
    n1 = int(input())
    n2 = int(input())
    if array[n1][n2] == "#":
        array[n1][n2] = "O"
        arrayBola[n1][n2] = 1
    else:
        print("esse lugar ja tem elemento")
        scanBola()
    

def scanX():
    n1 = int(jogadas[0][0])
    n2 = int(jogadas[0][1])
    array[n1][n2] = 'X'
    jogadas.pop(0)
    arrayX[n1][n2] = 1

def verificarJogadas():
    for i in jogadas:
        if array[int(i[0])][int(i[1])] != '#':
            jogadas.remove(i)

def prestesGanharX():
    pertoGanharX.clear()
    for i in posicoes:
        hashtag = 0
        for j in i:
            if j == '#':
                hashtag = 1
        if hashtag == 1:
            index = i.index('#')
        contador = 0
        for j in i:
            if j == 'X':
                contador+=1
        if contador == 2 and hashtag == 1:
            value = i[index+3]
            pertoGanharX.append([i[0], i[1], i[2], array[int(value[0])][int(value[1])]])
            jogadas.insert(0, value)

def prestesGanharO():
    pertoGanharO.clear()
    for i in posicoes:
        hashtag = 0 
        for j in i:
            if j == '#':
                hashtag = 1
        if hashtag == 1:
            index = i.index('#')
        contador = 0
        for j in i:
            if j == 'O':
                contador+=1
        if contador == 2 and hashtag == 1:
            value = i[index+3]
            pertoGanharO.append([i[0], i[1], i[2], array[int(value[0])][int(value[1])]])
            jogadas.insert(0, value)

def colocarPosicao():
    posicoes.clear()
    posicoes.append([array[0][0], array[1][0], array[2][0], '00', '10', '20'])
    posicoes.append([array[0][1], array[1][1], array[2][1], '01', '11', '21'])
    posicoes.append([array[0][2], array[1][2], array[2][2], '02', '12', '22'])

    posicoes.append([array[0][0], array[0][1], array[0][2], '00', '01', '02'])
    posicoes.append([array[1][0], array[1][1], array[1][2], '10', '11', '12'])
    posicoes.append([array[2][0], array[2][1], array[2][2], '20', '21', '22'])

    posicoes.append([array[0][0], array[1][1], array[2][2], '00', '11', '22'])
    posicoes.append([array[0][2], array[1][1], array[2][0], '02', '11', '20'])

def printar():
    for fileira in array:
        print(fileira[0], "|", fileira[1], "|", fileira[2])

def verificar(list):
    if list[0][0] and list[1][0] and list[2][0]:
        return True
    elif list[0][1] and list[1][1] and list[2][1]:
        return True
    elif list[0][2] and list[1][2] and list[2][2]:
        return True
    elif list[0][0] and list[0][1] and list[0][2]:
        return True
    elif list[1][0] and list[1][1] and list[1][2]:
        return True
    elif list[2][0] and list[2][1] and list[2][2]:
        return True
    elif list[0][0] and list[1][1] and list[2][2]:
        return True
    elif list[0][2] and list[1][1] and list[2][0]:
        return True
    return False

def computadorComeca(jogadas):
    contadorJogadas = 0
    while contadorJogadas < 9:
        scanX()
        if contadorJogadas == 0:
            printar()
        contadorJogadas = contadorJogadas + 1
        colocarPosicao()
        if verificar(arrayX):
            printar()
            print("X GANHOU")
            break
        scanBola()
        contadorJogadas = contadorJogadas + 1
        if (contadorJogadas == 9):
            if verificar(arrayX) is False and verificar(arrayBola) is False:
                print('deu velha')
            printar()
            break
        colocarPosicao()
        verificarJogadas()
        prestesGanharO()
        prestesGanharX()
        if verificar(arrayBola):
            printar()
            print("BOLA GANHOU")
            break
        printar()
        jogadas = list(set(jogadas))
        verificarJogadas()

def jogadorComeca(jogadas):
    contadorJogadas = 0
    while contadorJogadas < 9:
        scanBola()
        contadorJogadas = contadorJogadas + 1
        if (contadorJogadas == 9):
            if verificar(arrayX) is False and verificar(arrayBola) is False:
                print('deu velha')
            printar()
            break
        colocarPosicao()
        verificarJogadas()
        prestesGanharO()
        prestesGanharX()
        if verificar(arrayBola):
            print("BOLA GANHOU")
            printar()
            break
        scanX()
        contadorJogadas = contadorJogadas + 1
        printar()
        colocarPosicao()
        if verificar(arrayX):
            print("X GANHOU")
            printar()
            break
        jogadas = list(set(jogadas))
        verificarJogadas()

def menu(jogadas):
    print('[1]: Jogador comeca\n[2]: Computador comeca')
    val = int(input())
    if val == 1:
        jogadorComeca(jogadas)
    elif val == 2:
        computadorComeca(jogadas)

menu(jogadas)