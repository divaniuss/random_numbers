from tkinter import *
import random

def generate_random():
    random_number = random.randint(1, 100)
    result_label.config(text=f"{random_number}")

root = Tk()
root.title("Number")
root.geometry('750x500')


button = Button(text='Число', padx=20, command=generate_random)
button.pack()

result_label = Label(text='', font=('Times New Roman', 15))
result_label.pack()

root.mainloop()