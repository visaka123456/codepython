print('ยินดีต้อนรับสู่โปรแกรม')
from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมของฉัน') # ชื่อโปรแกรม
GUI.geometry('500x300')   # ปรับขนาดหน้าจอ

def Show():
    messagebox.showinfo('Show Box','สวัสดีครับ!')

B1 = ttk.Button(GUI,text='กรุณาคลิกปุ่มนี้',command=Show)
B1.pack(ipadx=50,ipady=30,pady=50) # แปะปุ่มไว้กับโปรแกรมหลัก

'''
B1 = ttk.Button(GUI,text='กรุณาคลิกปุ่มนี้',command=Show)
B1.pack(ipadx=50,ipady=30)

B1 = ttk.Button(GUI,text='กรุณาคลิกปุ่มนี้',command=Show)
B1.pack(ipadx=50)

B1 = ttk.Button(GUI,text='กรุณาคลิกปุ่มนี้',command=Show)
B1.pack()
'''

GUI.mainloop()

