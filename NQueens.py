# TITLE: NQueens solver
# AUTHOR: Pack
# CREATION DATE: 2023
# LAST UPDATE: 8/7/2024
# SUMMARY: Run file and follow prompts.  
#   Solves the nqueens puzzle for any board of n size
#   Prints N that its solved followed by the completed board
#   Prompts ask for starting and ending number so it can solve multiple N's in a single run

import sys

# Create list for possible failed boards
failed = []
class NQueens():
    # Function that checks that a board was completed successfully
    # Params: First is the board to check, Second is the number of rows/columns
    # Called by: run()
    def check(self, board, n):
        # Create set for queens and diagonals
        queens = set()
        diag = set()
        # Return false if board is not the correct size
        if len(board) != n:
            print("Board not correct size")
            return False
        # Loop through board
        for x in range(len(board)):
            y = board[x]
            # If y is outside 0-n return false
            if(y >= n or y < 0):
                return False
            # Add y value to queens set
            queens.add(y)
            # Add y-x to diagonal set
            diag.add(y - x)
        # If either of the sets are not equal in length to n then return false
        if len(diag) != n or len(queens) != n:
            return False
        # Return true otherwise
        return True

    # Function for solving a board of n % 6 = 2
    # Params: Number representing number of rows/columns
    # Called by: run()
    def runTwo(self, n):
        # Initialize variables (i =increment, y = next queen's y value, board = list of y values)
        i = 2
        y = n // 2 - 1
        board = []
        # While y is in bounds
        while y < n:
            # Add y to board and increase by increment
            board.append(y)
            y += i
        # If y is one value out of bounds set y to 1
        if (y == n + 1):
            y = 1
        # Else (y = n) set y to 0
        else:
            y = 0
        # Add y to board and increase by increment
        board.append(y)
        y += i
        # While y is not in board add y to board and increase by increment
        while y not in board:
            board.append(y)
            y += i
        # Set y to n // 2 + 2
        y = n // 2 + 2
        # While y is in bounds add y to board and increase by increment
        while y <= n - 1:
            board.append(y)
            y += i
        # If y has been 0 set y to one, otherwise set y to 0
        if 0 in board:
            y = 1
        else:
            y = 0
        # While board is not complete add y to board and increase by increment
        while len(board) < n:
            board.append(y)
            y += i
        # Return board
        return board

    # Function for solving a board of n % 6 = 3
    # Params: Number representing number of rows/columns
    # Called by: run()
    def runThree(self, n):
        # Initialize variables (i =increment, y = next queen's y value, board = list of y values)
        i = 2
        y = 3
        board = []
        # While y is in bounds add y to board and increase by increment
        while(y < n):
            board.append(y)
            y+= i
        # Set y to 1 add to board then set y to 4
        y = 1
        board.append(y)
        y = 4
        # While y is in bounds add y to board and increase by increment
        while(y < n):
            board.append(y)
            y+= i
        # Set y to 0
        y = 0
        # While board is not full add y to board and increase by increment
        while (len(board) < n):
            board.append(y)
            y +=i
        # Return board
        return board

    # Function for solving a board where n % 6 != 2 or 3 
    # Params: Number representing number of rows/columns
    # Called by: run()
    def runOther(self, n):
        # Initialize variables (i =increment, y = next queen's y value, board = list of y values)
        i = 2
        y = 1
        board = []
        # If n is odd set y to 0 instead of 1
        if n % 2 == 1:
            y = 0
        # While y is in bounds add y to board and increase by increment
        while y < n:
            board.append(y)
            y += i
        # If n is even set y to 0 and if n is odd set y to 1
        if (n % 2 == 0):
            y = 0
        else:
            y = 1
        # If n % 6 does not equal 0 or 5 enter while loop
        if n % 6 != 5 and n % 6 != 0:
            # While y is in bounds add y to board and increase by increment
            while y < len(board):
                board.append(y)
                y += 2
        else:
            # If n % 6 = 0 set y to 0
            if n % 6 == 0:
                y = 0
            # If n % 6 = 5 set y to 1
            else:
                y = 1
            # While y is in bounds add y to board and increase by increment
            while y < n:
                board.append(y)
                y += i
        # Set y to 0
        y = 0
        # While board is not full add y to board and increase by increment
        while len(board) < n:
            board.append(y)
            y += i
        # Return board
        return board

    # Function for solving boards from start (Inclusive) to end (Exclusive)
    # Params: First is starting number, Second is ending number
    # Called by: main 
    #  Calls: check(), runTwo(), runThree(), runOther()    
    def run(self, start, end):
        # Set n to starting number
        n = start
        # While n is not equal to end
        while n != end:
            # If n % 6 = 2 then call runTwo with param n
            if (n % 6 == 2):
                board = self.runTwo(n)
            # If n % 6 = 3 then call runThree with param n
            elif (n % 6 == 3):
                board = self.runThree(n)
            # Otherwise call runOther with param n
            else:
                board = self.runOther(n)
            # Print n
            print(n)
            # If board failed add to failed list and print failed
            if not self.check(board, n):
                failed.append([n, board])
                print("FAILED")
            # Print completed board and increment n
            print(board)
            n += 1

if __name__ == "__main__":
    # While loop to get user input
    while True:
        # Get input
        user = input("Choose starting number (inclusive): ")
        # Try to convert to number
        try:
            start = int(user)
            # If successful but number is less than 4, print error and ask again
            if start < 4:
                print("Error starting number must be at least 4")
            # If successful and number is greater than 4, break out of loop
            else:
                break
        # If unsuccessful, print error and ask again
        except ValueError:
            print("Error unrecognized input")

    # While loop to get user input
    while True:
        # Get input
        user = input("Choose ending number (exclusive): ")
        # Try to convert to number
        try:
            end = int(user)
            # If successful but number is less than start, print error and ask again
            if end < start:
                print("Error end must be bigger than start")
            else:
                # If successful and number is greater than start, break out of loop
                break
        # If unsuccessful, print error and ask again
        except ValueError:
            print("Error unrecognized input")

    nqueen = NQueens()
    # Call run function with params for starting and ending numbers
    nqueen.run(start, end)
    # If at least one failed print failed list (n, board) *Should never see this, only used for refactoring*
    if len(failed) > 0:
        print("Failed:", failed)
    # Otherwise print success
    else:
        print("Success")