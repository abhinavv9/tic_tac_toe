board = [' ' for x in range(10)]


def forletter(letter, pos):
    board[pos] = letter


def userturn():
    run = True
    while run:
        move = input('Please Enter Your Position in (1-9).')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isposempty(move):
                    run = False
                    forletter('X', move)
                else:
                    print('Sorry, this space is filled!')
            else:
                print('Please type a number within range!')
        except:
            print('Please type a number!')


def compturn():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if iswinner(boardCopy, let):
                move = i
                return move

    if 5 in possibleMoves:
        move = 5
        return move

    forcorner = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            forcorner.append((i))

    if len(forcorner) > 0:
        move = selectrandom(forcorner)
        return  move

    foredge = []
    for i in possibleMoves:
        if i != [2, 4, 6, 8]:
            foredge.append((i))

    if len(foredge) > 0:
        move = selectrandom(foredge)

    return move


def printgrid(board):
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])


def isposempty(pos):
    return board[pos] == ' '


def isgridfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def iswinner(b, le):
    return (b[1] == le and b[2] == le and b[3] == le) or (b[4] == le and b[5] == le and b[6] == le) or (b[7] == le and b[8] == le and b[9] == le) or (b[1] == le and b[4] == le and b[7] == le) or (b[2] == le and b[5] == le and b[8] == le) or (b[3] == le and b[6] == le and b[9] == le) or (b[1] == le and b[5] == le and b[9] == le) or (b[3] == le and b[5] == le and b[7] == le)


def selectrandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print('----Welcome! Can you beat me?----')
    printgrid(board)

    while not(isgridfull(board)):
        if not iswinner(board, 'O'):
            userturn()
            printgrid(board)
        else:
            print('Sorry O\'s won this match!')
            break

        if not iswinner(board, 'X'):
            move = compturn()
            if move == 0:
                print('Tie game!')
            else:
                forletter('O', move)
                print('Computer placed \'O\' at position', move, ';')
                printgrid(board)
        else:
            print('You won this match!')
            break


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('---------------------------------')
        main()
    else:
        break
