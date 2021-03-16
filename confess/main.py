#!/usr/bin/python3
import sys
from os import path
from random import randint
from tkinter import Tk, Button, Label

from PIL import Image, ImageTk

top = Tk()
top.title('来自一位喜欢你的小哥哥')
# 本地运行用这里
# top.iconbitmap(path.join('res/heart.ico'))
# 打包用这里
top.iconbitmap(path.join(sys._MEIPASS, 'res/heart.ico'))
top.geometry("650x350")

top.protocol('WM_DELETE_WINDOW', lambda: 0)


def close_window():
    top.destroy()


# 本地运行用这里
# photo = ImageTk.PhotoImage(Image.open(path.join('res/heart.png')).resize((150, 150)))
# 打包用这里
photo = ImageTk.PhotoImage(Image.open(path.join(sys._MEIPASS, 'res/heart.png')).resize((150, 150)))
# 汉字可以替换
a_label = Label(top, **{'text': '小姐姐，相识是缘，相知是份', 'font': ('', 19)})
b_label = Label(top, **{'text': '每天要开开心心的，好不好？', 'font': ("Arial Bold", 20)})
a_button = Button(top, **{'text': '好呀', 'width': 13, 'height': 1}, command=close_window)
b_button = Button(top, **{'text': '算了吧', 'width': 13, 'height': 1})
label_img = Label(top, image=photo)

a_label.place(x=50, y=80)
b_label.place(x=50, y=130)
a_button.place(x=130, y=250)
label_img.place(x=420, y=40)

x = 330
y = 250
b_button.place(x=x, y=y)


def change(event):
    global x, y
    x = randint(0, 650)
    y = randint(0, 350)
    b_button.place(x=x, y=y)


b_button.tkraise()
b_button.bind("<Enter>", change)

# 进入消息循环
top.mainloop()
