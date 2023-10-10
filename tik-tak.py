board = list(range(1, 10))

pobeda = [(1,2,3),(4,5,6),(7,8,9),(3,6,9),(2,5,8),(1,4,7),(1,5,9),(3,5,7)] #Выигрышные комбинации

def f():
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3],'|')

def who(X_or_O):
    while True:
        value = input('Выберите место для постановки'+X_or_O)
        if value not in '123456789':
            print('Ошибка.Повторите ввод.')
            continue
        value = int(value)
        if str(board[value-1]) in 'XO': #так как индексы начинаются с 0,мы наше число (от 1 до 9) уменьшаем на один.
            print('Вы выбрали занятуюю ячейку')
            continue
        board[value-1] = X_or_O
        break

def check_Winner():
    for j in pobeda:
        if (board[j[0]-1]) == (board[j[1]-1]) == (board[j[2]-1]):
            return (board[j[1]-1])
    else:
        return False
    
def main():
    while True:
        f()
        if count%2 == 0:
            who("X") #Это фунция которую я вызову позже
        else:
            who("O")
