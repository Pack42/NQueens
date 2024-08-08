from NQueens import NQueens
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Visualization for nqueens puzzle")

# Define initial variables
cell_width = 5
cell_height = 2
n = 4


# Function to change the grid size and redraw
def increaseN():
    global n
    n += 1  # Increase grid size by 1
    create_grid(n, getBoard())  # Recreate grid

def create_grid(n, queens):
    for widget in root.winfo_children():
        widget.destroy()
    button = tk.Button(root, text="Increase N", command=increaseN)
    button.pack()

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
            cell = tk.Label(frame, width=cell_width, height=cell_height, bg=color, borderwidth=1, relief="solid")
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