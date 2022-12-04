# Создайте программу для игры в ""Крестики-нолики"".
from tkinter import *
import tkinter.messagebox as mb
import random
import sys

root = Tk()
root.title('Крестики-нолики')
field = []
count = 0
who_move = random.choice(['X', '0'])


def check_win():
    global count
    if field[0][0]['text'] == field[0][1]['text'] == field[0][2]['text'] == 'X' or field[1][0]['text'] == field[1][1][
        'text'] == field[1][2]['text'] == 'X' or field[2][0]['text'] == field[2][1]['text'] == field[2][2][
        'text'] == 'X' or field[0][0]['text'] == field[1][0]['text'] == field[2][0]['text'] == 'X' or field[0][1][
        'text'] == field[1][1]['text'] == field[2][1]['text'] == 'X' or field[0][2]['text'] == field[1][2]['text'] == \
            field[2][2]['text'] == 'X' or field[0][0]['text'] == field[1][1]['text'] == field[2][2]['text'] == 'X' or \
            field[0][2]['text'] == field[1][1]['text'] == field[2][0]['text'] == 'X':
        mb.showinfo("Информация", 'Победили крестики!')
        sys.exit()

    if field[0][0]['text'] == field[0][1]['text'] == field[0][2]['text'] == '0' or field[1][0]['text'] == field[1][1][
        'text'] == field[1][2]['text'] == '0' or field[2][0]['text'] == field[2][1]['text'] == field[2][2][
        'text'] == '0' or field[0][0]['text'] == field[1][0]['text'] == field[2][0]['text'] == '0' or field[0][1][
        'text'] == field[1][1]['text'] == field[2][1]['text'] == '0' or field[0][2]['text'] == field[1][2]['text'] == \
            field[2][2]['text'] == '0' or field[0][0]['text'] == field[1][1]['text'] == field[2][2]['text'] == '0' or \
            field[0][2]['text'] == field[1][1]['text'] == field[2][0]['text'] == '0':
        mb.showinfo("Информация", 'Победили нолики!')
        sys.exit()

    if count == 9:
        mb.showinfo("Информация", 'Победила дружба!')
        sys.exit()


def click(row, col):
    global who_move
    global count
    if field[row][col]['text'] == ' ' and who_move == 'X':
        field[row][col]['text'] = 'X'
        count += 1
        check_win()
        who_move = '0'

    if field[row][col]['text'] == ' ' and who_move == '0':
        field[row][col]['text'] = '0'
        count += 1
        check_win()
        who_move = 'X'


for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=3, height=3, font=('Arial', 20, 'bold'),
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
mb.showinfo("Информация", f'Первые ходят {who_move}')
root.mainloop()
