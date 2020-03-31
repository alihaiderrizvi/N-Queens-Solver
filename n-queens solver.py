import tkinter as tk
import time
import random
import copy



def generate_board(n):
    board = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        board.append(a)
    return board



def validity(board, row, col):
    # checking row
    if 1 in board[row]:
        return False
    #checking col
    for i in range(len(board)):
        if board[i][col] != 0:
            return False
    #checking diagonal
    row_copy = row
    col_copy = col
    if row <= col:
        col -= row
        row -= row
    else:
        row -= col
        col -= col
    #checking right diagonal
    while row < len(board) and col < len(board):
        if board[row][col] != 0:
            return False
        row += 1
        col += 1
    # checking left diagonal
    while row_copy != 0 and col_copy != len(board)-1:
        row_copy -= 1
        col_copy += 1
    while row_copy < len(board) and col_copy >=0:
        if board[row_copy][col_copy] != 0:
            return False
        row_copy += 1
        col_copy -= 1
    return True



def show(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()



def find_space(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)
    return False



def check_finish(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                count += 1

    if count == len(board):
        return True
    return False


def solve(board, n, strt = 0):
    global solution
    if check_finish(board):
        show(board)
        return True

    for i in range(strt, n):
        for j in range(n):
            if board[i][j] == 0 and validity(board,i,j):
                board[i][j] = 1
                a = copy.deepcopy(board)
                solution.append(a)
                if solve(board, n, i+1):
                    return True
                board[i][j] = 0
                a = copy.deepcopy(board)
                solution.append(a)
    return False


def show_sol():
    global solution
    global solution_instance
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            for k in range(len(solution[i][j])):
                m.update()

                if solution[i][j][k] == 1:
                    canvas.itemconfig(solution_instance[j][k], text='Q')
                else:
                    canvas.itemconfig(solution_instance[j][k], text='')



m = tk.Tk()
m.title("n-queens solver")
m.geometry("670x670")
canvas = tk.Canvas(m, width = 670, height = 620)
canvas.pack()

def retrieve_input():
    # print(textBox)
    size = textBox.get("1.0","end-1c")
    size = int(size)
    board = generate_board(size)
    global solution
    global solution_instance
    solution = []
    solution.append(copy.deepcopy(board))
    # drawing boxes, and making a list of text objects
    solution_instance = []
    for i in range(size):
        a = []
        for j in range(size):
            a.append("")
        solution_instance.append(a)

    for i in range(size):
        for j in range(size):
            canvas.create_rectangle(10+(50*j), 10+(50*i), 60+(50*j), 60+(50*i))
            solution_instance[i][j] = canvas.create_text(35 + (50 * j), 35 + (50 * i), text='', font=("calibri", 30))
            m.update()
    print('length of solution instance: ', len(solution_instance))

    solve(board, size)
    show_sol()


# Creating Button
button = tk.Button(m, text="Solve", width = 10, height = 2, command = lambda: retrieve_input()).place(x=315, y=620, in_= m)

#Creating text entry field
textBox = tk.Text(m, height=1, width=10)
textBox.pack()
textBox.place(x = 220, y=630, in_ = m)
tk.Label(m, text="Enter size of grid: ").place(x = 120, y=630, in_ = m)


m.mainloop()