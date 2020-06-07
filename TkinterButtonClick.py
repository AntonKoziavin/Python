from tkinter import *


root = Tk()
root.title("Click button")
root.geometry("300x150")
clicks = 0                                                              # Начальное значение кликов


def click_button():                                                     # Функия для подсчета и записи кликов
    global clicks                                                       # Область видимости переменной
    clicks += 1
    root.title("Number of clicks {}".format(clicks))                    # Изменение названия окна


btn = Button(text="Click me", background="#555", foreground="#ccc",     # command - реакция на нажатие и привязка...
             padx="20", pady="8", font="16", height="5",                # ...к функции click_button
             command=click_button)


btn.pack()
root.mainloop()


