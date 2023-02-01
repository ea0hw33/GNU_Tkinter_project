import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk

from calculation import *

class Disks:
    def __init__(self, frame, img_of_disks, weight=0, base_weight=0):
        self.img = img_of_disks
        self.frame = frame
        self.weight = weight
        self.base_weight = base_weight
        self.discs_var = {'1.25': 0, '2.5': 0, '5': 0, '10': 0, '15': 0, '20': 0, '25': 0}

    def set_discs_var(self, weight, base_weight):
        if error_handler(weight, base_weight) is None:
            messagebox.showerror(title='Ошибка',
                                 message= 'Введите число или дробное число, '
                                          'входящее в рабочий диапазон чисел. Пример:\n72.5; 25')
        else:
            self.weight = weight
            self.base_weight = base_weight
            self.discs_var = error_handler(self.weight, self.base_weight)

    def display_discs_var(self):
        columns = 0

        #to clear frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        for i in self.discs_var.keys():
            if self.discs_var[i] != 0:
                for _ in range(self.discs_var[i]):
                    img_lb = Label(self.frame, image=self.img[i])
                    img_lb.grid(row=0,column=columns)
                    columns+=1

    def button_command(self,weight,base_weight):
        self.set_discs_var(weight,base_weight)
        self.display_discs_var()

    def clear_dict_of_disks(self):
        self.discs_var = {'1.25': 0, '2.5': 0, '5': 0, '10': 0, '15': 0, '20': 0, '25': 0}

def clear_handler(weight_ent, base_weight_ent, frame,disks):
    for widget in frame.winfo_children():
        widget.destroy()
    base_weight_ent.delete(0,'end')
    weight_ent.delete(0, 'end')
    disks.clear_dict_of_disks()


def main():
    root = Tk()
    root.resizable(False,False)
    root.title("Калькулятор набора штангового веса")
    icon = tk.PhotoImage(file='img/icon.png')
    root.iconphoto(False,icon)

    content = ttk.Frame(root)
    frame = Frame(root, borderwidth=5,height=80,width=400)
    img = {'1.25':ImageTk.PhotoImage(Image.open('img/1.25.png')),
           '2.5':ImageTk.PhotoImage(Image.open('img/2.5.png')),
           '5':ImageTk.PhotoImage(Image.open('img/5.png')),
           '10':ImageTk.PhotoImage(Image.open('img/10.png')),
           '15':ImageTk.PhotoImage(Image.open('img/15.png')),
           '20':ImageTk.PhotoImage(Image.open('img/20.png')),
           '25':ImageTk.PhotoImage(Image.open('img/25.png'))}
    weight_lb = Label(content,text="Общий вес грифа с дисками:")
    base_weight_lb = Label(content,text="Базовый вес(вес грифа и замков):")
    weight_ent = Entry(content)
    base_weight_ent = Entry(content)
    disks = Disks(frame,img)
    button_input = Button(content, text='Рассчитать',
                    command=(lambda: disks.button_command(weight_ent.get(),base_weight_ent.get())))
    button_clear = Button(content, text='Очистить',
                    command=(lambda: clear_handler(weight_ent,base_weight_ent,frame,disks)))

    content.pack(expand=True)
    frame.pack(anchor='n')
    weight_lb.grid(row=1)
    weight_ent.grid(row=1, column=1)
    base_weight_lb.grid(row=2)
    base_weight_ent.grid(row=2, column=1)
    button_input.grid(row=1, column=3, padx=10, pady=10)
    button_clear.grid(row=2,column=3)

    root.mainloop()

main()