"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-19 13:39:07
Author  : Younth Yang (8593009@qq.com)
"""
import tkinter
import tkinter.messagebox


def main():
    flag = True

    def change_lable_text():
        nonlocal flag
        flag = not flag

        color, msg = ('red', 'hello world') if flag else (
            'blue', 'goodbye world')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    top = tkinter.Tk()
    top.geometry('240x160')
    top.title = '小游戏'
    label = tkinter.Label(top, text='hello world', font='宋体', fg='red')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    btn1 = tkinter.Button(panel, text='修改', command=change_lable_text)
    btn1.pack(side='left')
    btn2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)

    btn2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()

if __name__ == '__main__':
    main()
