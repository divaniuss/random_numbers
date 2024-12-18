from tkinter import *
from tkinter import ttk,messagebox
import random

def generate_random():
    number_from = int(combo_from.get())
    number_to = int(combo_to.get())
    if number_from > number_to:

        messagebox.showinfo("Ошибка","Начальное число не может быть больше конечного")
    else:
        selected_exception = list_exception.curselection()
        exception = ''
        if selected_exception:
            exception = int(list_exception.get(selected_exception))
        while True:
            random_number = random.randint(number_from, number_to)
            if random_number != exception:
                break
        result_label.config(text=f"Случайное число: {random_number}")


        


root = Tk()
root.title("Number")
root.geometry('750x500')


list = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10]
list_exception = Listbox(root, selectmode=SINGLE)
list_exception.pack()

for i in list:
    list_exception.insert(END, i)



combo_from = ttk.Combobox(root, values=[1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10])
combo_from.pack(pady = 10)
combo_to = ttk.Combobox(root, values=[1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10])
combo_to.pack(pady = 10)


button = Button(text='Число', padx=20, command=generate_random)
button.pack()

result_label = Label(text='', font=('Times New Roman', 15))
result_label.pack()

root.mainloop()