from tkinter import *


def various_elements(vvod):
    d, g = {n1.get().split(' ')[0]: [int(i) for i in n1.get().split(' ')[1:6]]}, {n1.get().split(' ')[6]: [int(i) for i in n1.get().split(' ')[7:]]}
    c['text'] = 'апельсины', max(d['апельсины'])
    e['text'] = 'яблоки', max(g['яблоки'])


root = Tk()
root.title('Нахождение средних значений')
root.geometry("600x120")
Label(text='Ввод, через пробел:').grid(row=1, column=0)
n1 = Entry(width=50)
n1.grid(row=1, column=1)
button1 = Button(text="Поиск")
button1.grid(row=4, column=1)
c = Label(font='arial 12')
c.grid(row=5, column=1)
e = Label(font='arial 12')
e.grid(row=6, column=1)
button1.bind('<Button-1>', various_elements)
root.mainloop()