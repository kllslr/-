from easy import *
from medium import *
from hard import *
from tkinter import *
BACKGROUND_COLOR = 'white'
FOREGROUND_COLOR = '#262A53'
BUTTON_COLOR = '#262A53'
BUTTON_FOREGROUND = '#FFE3E3'


def easy_window():
    easy_obj = Easy()


def medium_window():
    med_obj = Medium()


def hard_window():
    hard_obj = Hard()







root = Tk()
root.title("Keyboard trainer")
root.config(padx=100, pady=70, bg=BACKGROUND_COLOR)
root.resizable(width=False, height=False)

title_label = Label(text="клавиатурный тренажер", font=('Arial', 15), bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
title_label.grid(row=1, column=2, pady=7)

level_title = Label(text="Выбери уровень: ", font=("Arial", 15), bg=BACKGROUND_COLOR
                    , fg=FOREGROUND_COLOR)
level_title.grid(row=2, column=2, pady=20)

easy_button = Button(text="Лёгкий",  command=easy_window, bg=BUTTON_COLOR
                     , fg=BUTTON_FOREGROUND)
easy_button.grid(row=3, column=1)

medium_button = Button(text="Средний",  command=medium_window, bg=BUTTON_COLOR,
                       fg=BUTTON_FOREGROUND)
medium_button.grid(row=3, column=2)

hard_button = Button(text="Сложный", command=hard_window, bg=BUTTON_COLOR,
                     fg=BUTTON_FOREGROUND)
hard_button.grid(row=3, column=3)

mainmenu = Menu(root)
root.config(menu=mainmenu)


root.mainloop()