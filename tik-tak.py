board = list(range(1, 10))

def f():
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3],'|')
def main():
    while True:
        f()
        if count%2 == 0:
            who("X") 
        else:
            who("O")