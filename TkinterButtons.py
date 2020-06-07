from tkinter import *

root = Tk()
root.title("Python GUI")
root.geometry("200x200")
btn = Button(root, text="Hello",                            # Конструктор кнопки
             bg="#555",                                     # Фоновый цвет кнопки (background)
             fg="#ccc",                                     # Цвет текста (foreground)
             padx="20",                                     # Дополнительный отступ от границ до текста по X
             pady="10",                                     # Дополнительный отступ от границ до текста по Y
             font="Arial 16",                               # Стиль и размер текста
             activebackground="#ccc",                       # Фоновый цвет при нажатии
             activeforeground="#555",                       # Цвет текста при нажатии
             bd="5",                                        # Толщина границы (default=2)
             height="3",                                    # Высота кнопки
             highlightcolor="#ccc",                         # Цвет кнопки, когда она в фокусе
             justify="center",                              # Выравнивание текста(left, right, center)
             relief="sunken",                               # Тип границы (sunken, raised, groove, ridge)
             state="normal",                                # Состояние кнопки (active, disabled, normal)
             underline="1",                                 # Подчеркивание определенного символа текста
             width="5",                                     # Ширина кнопки
             wraplength="-1")                               # Перенос текста кнопки при положительном значении
btn.pack()                                                  # Отображение кнопки
root.mainloop()



