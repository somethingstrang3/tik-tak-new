board = list(range(1, 10))

def f():
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3],'|')
print('Выбор ячейки')
a = input()
print('Выбрали ',a ' ячейку')