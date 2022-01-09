import tkinter as tk

count = 0
grid = []

def if_clicked(btn):
    global count
    if btn["text"] == " " and count%2 == 0:
        btn["text"] = "X"
        count += 1
        grid[btn.grid_info()['row']][btn.grid_info()['column']] = 0
        print(grid)
    elif btn["text"] == " " and count%2 == 1:
        btn["text"] = "O"
        count += 1
        grid[btn.grid_info()['row']][btn.grid_info()['column']] = 1
        print(grid)
    else:
        print("Try again sweetie")
    check_for_winner()

def check_for_winner():
    win = False
    # Le grid logic
    if grid [0][0] == grid [0][1] == grid [0][2] and grid [0][0] != -1:
        print("We have a winner!")
    elif grid [1][0] == grid [1][1] == grid [1][2] and grid [1][0] != -1:
        print("We have a winner!")
    elif grid [2][0] == grid [2][1] == grid [2][2] and grid [2][0] != -1:
        print("We have a winner!")
    elif grid [0][0] == grid [1][0] == grid [2][0] and grid [0][0] != -1:
        print("We have a winner!")
    elif grid [0][1] == grid [1][1] == grid [2][1] and grid [0][1] != -1:
        print("We have a winner!")
    elif grid [0][2] == grid [1][2] == grid [2][2] and grid [0][2] != -1:
        print("We have a winner!")
    elif grid [0][0] == grid [1][1] == grid [2][2] and grid [0][0] != -1:
        print("We have a winner!")
    elif grid [0][2] == grid [1][1] == grid [2][0] and grid [0][2] != -1:
        print("We have a winner!")
    else:
        return

def create_grid(root):
    btn1 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn1))
    btn1.grid(row = 0, column = 0)
    
    btn2 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn2))
    btn2.grid(row = 0, column = 1)

    btn3 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn3))
    btn3.grid(row = 0, column = 2)

    btn4 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn4))
    btn4.grid(row = 1, column = 0)

    btn5 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn5))
    btn5.grid(row = 1, column = 1)

    btn6 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn6))
    btn6.grid(row = 1, column = 2)

    btn7 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn7))
    btn7.grid(row = 2, column = 0)

    btn8 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn8))
    btn8.grid(row = 2, column = 1)

    btn9 = tk.Button(root, text = " ", height = 5, width = 10, command = lambda: if_clicked(btn9))
    btn9.grid(row = 2, column = 2)

    grid.append([-1, -1, -1])
    grid.append([-1, -1, -1])
    grid.append([-1, -1, -1])

def main():
    root = tk.Tk()
    root.geometry("350x275")
    create_grid(root)
    root.mainloop()

main()
