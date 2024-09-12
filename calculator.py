from tkinter import *
import math


def click(value):
    global answer
    ex = field.get()

    if value == 'C':
        ex = ex[0:len(ex)-1]
        field.delete(0, END)
        field.insert(0, ex)

    elif value == 'CE':
        field.delete(0, END)

    elif value == '√':
        answer = math.sqrt(int(ex))

    field.delete(0, END)
    field.insert(0, answer)


root = Tk()
root.title('Smart Scientific Calculator')
root.geometry('610x500+10+10')
root.configure(bg='steelblue')

logo = PhotoImage(file='image/logo.png')
logo_label = Label(root, image=logo, bg='steelblue')
logo_label.grid(row=0, column=0)

field = Entry(font=('bold', 20), bg='steelblue', fg='aliceblue', bd=10, relief=SUNKEN, width=20)
field.grid(row=0, column=0, columnspan=8)

audio = PhotoImage(file='image/a.png')
audio_lab = Button(root, image=audio, bd=0, bg='steelblue')
audio_lab.grid(row=0, column=7)


button_text_list = ['C', 'CE', '√', '+', 'π', 'cos', 'tan', 'sin',
                    '1', '2', '3', '-', '2π', 'cosh', 'tanh', 'sinh',
                    '4', '5', '6', '*', chr(8731), 'x\u02b8', 'x\u00B3',
                    'ln', '7', '8', '9', chr(247), 'deg', 'rad', 'e',
                    ',', '0', '. ', '%', '=', 'log(x)', '(', ')', 'x!']
row_value = 1
column_value = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, relief=SUNKEN, text=i, bg='skyblue', fg='black',
                    font=('arial', 16, 'bold'), activebackground='steelblue', command=lambda button=i:click(button))
    button.grid(row=row_value, column=column_value, pady=1)
    column_value += 1
    if column_value > 7:
        row_value += 1
        column_value = 0

root.mainloop()
