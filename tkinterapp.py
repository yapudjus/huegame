# cette version est actuellement abandonée
# tghis version is abandoned for now


from tkinter import *
import random

def rgbToHex(rgb):
    return '#%02x%02x%02x' % rgb

# x= random.randint(0,20)
# y= random.randint(0,20)

x = 25
y = 25

center = Tk()
center.geometry(f'{y*25}x{x*25}')
center.title(f"{x}x{y} grid")
center.resizable(width=False, height=False)

cells = {}
for row in range(x):
    for column in range(y):
        cell = Frame(center, bg=rgbToHex((row*column % 255, int((row*column)/2) % 255, column % 255)), highlightbackground="black",
                    width=25, height=25, padx=3, pady=3)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell


def color_cell(cells, i, j, color="red"):
    cells[(i, j)].configure(background="red")

# center.after(5000, color_cell, cells, 3, 4)

center.mainloop()