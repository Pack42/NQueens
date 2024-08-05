import sys
failed = []
p = 1
def check(board, n):
    queens = set()
    diag = set()
    if len(board) != n:
        print("Board not correct size")
        return False
    for x in range(len(board)):
        y = board[x]
        if(y >= n):
            return False
        queens.add(y)
        diag.add(y - x)
    if len(diag) != n or len(queens) != n:
        return False
    return True

def runTwo(n):
    i = 2
    y = n // 2 - 1
    board = []
    c = 0
    while y < n:
        board.append(y)
        y += i
    if (y == n + 1):
        y = 1
        z = n - 2
    else:
        y = 0
        z = n - 1
    board.append(y)
    while z > n // 2:
        z -= i
    y += i
    while y not in board:
        board.append(y)
        y += i
    z += i
    while z <= n - 1:
        board.append(z)
        z += i
    if 0 in board:
        y = 1
    else:
        y = 0
    while len(board) < n:
        board.append(y)
        y += i
    if not check(board, n):
        print("FAILED")
    return board

def runThree(n):
    i = 2
    board = []
    mid = n // 2
    y = 3
    while(y < n):
        board.append(y)
        y+= i
    y = 1
    i = 2
    board.append(y)
    y = 4
    while(y < n):
        board.append(y)
        y+= i
    y = 0
    while (len(board) < n):
        board.append(y)
        y +=i
    if (not check(board, n)):
        failed.append(n)
    return board

def run(start, end):
    while start != end:
        boo = True
        i = 2
        n = start
        if (n % 6 == 2):
            board = runTwo(n)
            boo = False
        elif (n % 6 == 3):
            board = runThree(n)
            boo = False

        while (boo):
            n = start
            board = []
            y = 1
            if n % 2 != 0:
                y = 0
            while y < n:
                board.append(y)
                y += i
            if (i == 2) and (n % 2 == 0):
                y = 0
            elif (i == 2):
                y = 1
            elif (y == n-1):
                y = n - i + 1
            else:
                y = n - i
            while y >= 0 and (n % 6 != 5 and n % 6 != 0) and i != 2:
                board.append(y)
                y -= i
            while i == 2 and y < len(board) and n % 6 != 5 and n % 6 != 0:
                board.append(y)
                y += 2
            if y == 0:
                y = 2
            elif n % 2 != 0:
                y = 1
            else:
                y = 0
            if (n % 6 == 5):
                y = 1
            elif n % 6 == 0:
                y = 0
            while y < n and (n % 6 == 5 or n % 6 == 0):
                board.append(y)
                y += i
            if n % 6 == 5 or n % 6 == 0:
                y = 2
            while len(board) < n:
                board.append(y)
                y += i
            if(not check(board, n)):
                i += 1
                if i > n:
                    print("GAVEUPGAVEUPGAVEUPGAVEUPGAVEUP")
                    failed.append(n)
                    boo = False
            else:
                boo = False
        print(n)
        print(board)
        start += 1

while True:
    user = input("Choose starting number (inclusive): ")
    try:
        start = int(user)
        break
    except ValueError:
        pass

while True:
    user = input("Choose ending number (exclusive): ")
    try:
        end = int(user)
        break
    except ValueError:
        pass

if start >= end:
    n = start
    run(n, n + 1)
else:
    run(start, end)
    if len(failed) > 0:
        print("Failed at n:", failed)
    else:
        print("Success")