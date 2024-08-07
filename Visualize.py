from NQueens import NQueens
import tkinter as tk

def create_grid(n, queens):
    # Create the main window
    root = tk.Tk()
    root.title("Visualization for nqueens puzzle")

    # Create a frame to hold the grid
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Define colors for the chessboard pattern
    colors = ["#F0D9B5", "#B58863"]  # Light and dark squares

    # Create the grid
    for i in range(n):
        for j in range(n):
            if queens[i] == j:
                color = "#000000"
            else:
                color = colors[(i + j) % 2]  # Alternate colors
            cell = tk.Label(frame, width=5, height=2, bg=color, borderwidth=1, relief="solid")
            cell.grid(row=i, column=j, padx=1, pady=1)

    # Start the Tkinter event loop
    root.mainloop()

# While loop to get user input
while True:
    # Get input
    user = input("Choose size: ")
    # Try to convert to number
    try:
        n = int(user)
        # If successful but number is less than 4, print error and ask again
        if n < 4:
            print("Error size must be at least 4")
        # If successful and number is greater than 4, break out of loop
        else:
            break
    # If unsuccessful, print error and ask again
    except ValueError:
        print("Error unrecognized input")
nq = NQueens()
# If n % 6 = 2 then call runTwo with param n
if (n % 6 == 2):
    board = nq.runTwo(n)
# If n % 6 = 3 then call runThree with param n
elif (n % 6 == 3):
    board = nq.runThree(n)
# Otherwise call runOther with param n
else:
    board = nq.runOther(n)
# Call create grid
create_grid(n, board)