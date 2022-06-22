print('funcionou')

array = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
arrayBola = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
arrayX = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def scanBola():
    print('digite a posicao do valor que voce quer inserir a bola O')
    n1 = int(input())
    n2 = int(input())
    if array[n1][n2] == '#':
        array[n1][n2] = 'O'
        arrayBola[n1][n2] = 1
    else:
        print('esse lugar ja tem elemento')
        scanBola()
    

def scanX():
    print('digite a posicao do valor que voce quer inserir a bola X')
    n1 = int(input())
    n2 = int(input())
    if array[n1][n2] == '#':
        array[n1][n2] = 'X'
        arrayX[n1][n2] = 1
    else:
        print('esse lugar ja tem elemento')
        scanX()
    
    
def printar():
    for fileira in array:
        print(fileira[0], '|', fileira[1], '|', fileira[2])

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

for i in range(9):
    scanBola()
    printar()
    if verificar(arrayBola):
        print('BOLA GANHOU')
        break
    scanX()
    printar()
    if verificar(arrayX):
        print('X GANHOU')
        break


