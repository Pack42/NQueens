# TITLE: NQueens solver visualization
# AUTHOR: Pack
# CREATION DATE: 2023
# LAST UPDATE: 8/9/2024
# SUMMARY: Run file and press buttons to change board or tile size.
#   Creates a visualization of an algorithm I made to solve the nqueens puzzle 

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
# Create nqueens variable to get board
nq = NQueens()


# Function to change the cell size and redraw
# Called by: User pressing button
# Calls: create_grid() and getBoard()
def increaseSize():
    global size
    size += 1  # Increase grid size by 1
    create_grid(n, getBoard())  # Recreate grid

def decreaseSize():
    global size
    size -= 1  # Decrease grid size by 1
    create_grid(n, getBoard())  # Recreate grid

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
# Called by buttons and MAIN
def create_grid(n, queens):
    # Destroy grid
    for widget in root.winfo_children():
        widget.destroy()
    # Create button frame for increase and decrease N
    buttonNFrame = tk.Frame(root)
    buttonNFrame.pack()
    # Only allow decrease if n is greater than 4
    if n > 4:
        # Create decrease N button
        decNButton = tk.Button(buttonNFrame, text="Decrease N", command=decreaseN)
        decNButton.pack(side="left", padx=5, pady=5)
    # Create increase N button
    incNButton = tk.Button(buttonNFrame, text="Increase N", command=increaseN)
    incNButton.pack(side="left", padx=5, pady=5)

    # Create frame for increase size button
    buttonSizeFrame = tk.Frame(root)
    buttonSizeFrame.pack()
    # Only allow decrease if size is greater than 1
    if size > 1:
        # Create decrease N button
        decSizeButton = tk.Button(buttonSizeFrame, text="Decrease Size", command=decreaseSize)
        decSizeButton.pack(side="left", padx=5)
    # Create increase size button
    incSizeButton = tk.Button(buttonSizeFrame, text="Increase Size", command=increaseSize)
    incSizeButton.pack(side="left", padx=5)

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

# Function to call functions from nqueens to get board
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

if __name__ == "__main__":
    # Call create grid
    create_grid(n, getBoard())
    # Start the Tkinter event loop
    root.mainloop()