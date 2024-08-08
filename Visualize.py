from NQueens import NQueens
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Visualization for nqueens puzzle")

# Define initial variables
cell_width = 5
cell_height = 2
size = 1
n = 4


# Function to change the grid size and redraw
# Called by: User pressing button
# Calls: create_grid() and getBoard()
def increaseN():
    global n
    n += 1  # Increase grid size by 1
    create_grid(n, getBoard())  # Recreate grid

# Function to change the grid size and redraw
# Called by: User pressing button
# Calls: create_grid() and getBoard()
def decreaseN():
    global n
    n -= 1  # Decrease grid size by 1
    create_grid(n, getBoard())  # Recreate grid

# Function that creates grid
def create_grid(n, queens):
    # Destroy grid
    for widget in root.winfo_children():
        widget.destroy()
    # Create increase button
    incButton = tk.Button(root, text="Increase N", command=increaseN)
    incButton.pack()
    # Only allow decrease if n is greater than 4
    if n > 4:
        # Create decrease button
        decButton = tk.Button(root, text="Decrease N", command=decreaseN)
        decButton.pack()

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
            cell = tk.Label(frame, width=cell_width * size, height=cell_height * size, bg=color, borderwidth=1, relief="solid")
            cell.grid(row=i, column=j, padx=1, pady=1)


def getBoard():
    # If n % 6 = 2 then call runTwo with param n
    if (n % 6 == 2):
        board = nq.runTwo(n)
    # If n % 6 = 3 then call runThree with param n
    elif (n % 6 == 3):
        board = nq.runThree(n)
    # Otherwise call runOther with param n
    else:
        board = nq.runOther(n)
    return board

# Create nqueens variable to get board
nq = NQueens()
# Call create grid
create_grid(n, getBoard())
# Start the Tkinter event loop
root.mainloop()