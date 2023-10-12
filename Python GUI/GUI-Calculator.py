# GUI-Calculator.py

from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# ----------------------------CSV----------------------------------------------
def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = filw writer
        fw.writerow(data)
# --------------------------------------------------------------------------

GUI = Tk()
GUI.title('โปรแกรมจัดการ layout')
GUI.geometry('500x300')

L1 = ttk.Label(GUI,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar() #ตัวแปรพิเศษเอาไว้เก็บค่า


E1 = ttk.Entry(GUI,textvariable=v_kilo,width=10,justify='right',font=('impact',30))
E1.pack(pady=20)

def Calc(event = None):
    print('กำลังคำนวณ...กรุณารอสักครู่')
    kilo = float(v_kilo.get()) # .get()ดึงข้อมูลจากตัวแปรที่เป็น StringVar
    print(kilo * 299)
    calc_result = kilo * 299
    date = datetime.now()
    year = date.year + 543
    stamp = date.strftime('{}-%m-%d %H:%M:%S'.format(year))
    data = [date,'กุ้ง','{:,.2f}'.format(calc_result)]
    writetocsv(data)
    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายตังค์ทั้งหมด: {:,.3f} บาท (กิโลกรัมละ 299)'.format(calc_result))

B1 = ttk.Button(GUI,text='คำนวณราคา',command=Calc)
B1.pack(ipadx=40,ipady=30)

E1.bind('<Return>',Calc) #ต้องใส่คำว่า event = None ไว้ในฟังชั่นด้วย

GUI.mainloop()


