# GUI-Wikipedia.py

from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime
import wikipedia
import webbrowser

# ----------------------------CSV----------------------------------------------
def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)


# ----------------------------GUI----------------------------------------------
GUI = Tk()
GUI.title('โปรแกรมจัดการ layout')
GUI.geometry('1200x600')

# -----------------------tab setting---------------------------------------
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_tab1 = PhotoImage(file='Tab1.png')
icon_tab2 = PhotoImage(file='Tab2.png')
icon_tab3 = PhotoImage(file='Coffee.png')


Tab.add(T1, text ='กุ้ง',image=icon_tab1,compound='top')
Tab.add(T2, text ='wiki',image=icon_tab2,compound='top' )
Tab.add(T3, text ='CAFE',image=icon_tab3,compound='top' )

# ---------------- tab 1 กุ้ง ----------------------
L1 = ttk.Label(T1,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar() #ตัวแปรพิเศษเอาไว้เก็บค่า


E1 = ttk.Entry(T1,textvariable=v_kilo,width=10,justify='right',font=('impact',30))
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

B1 = ttk.Button(T1,text='คำนวณราคา',command=Calc)
B1.pack(ipadx=40,ipady=30)

E1.bind('<Return>',Calc) #ต้องใส่คำว่า event = None ไว้ในฟังชั่นด้วย

# ---------------- tab 2 Wiki ----------------------

FONT1 = ('Angsana New',25)

L2 = Label(T2,text='ค้นหาข้อมูล wikipedia',font=('Angsana New',25))
L2.pack()

v_search = StringVar()  # .get() = ดึงข้อมูล .set('hello') set ให้โชว์ข้อความ

E2 = ttk.Entry(T2, textvariable=v_search, font=FONT1)
E2.pack(pady=10)

wikipedia.set_lang('th') #ทำให้เป็นภาษาไทย

v_link = StringVar()

def Search():
    try:
        search = v_search.get() #ดึงข้อความจากช่องที่กรอกมา
        # text = wikipedia.summary(search) # wikipedia.summary คือการสรุปผลที่ได้จากการค้นหา
        text = wikipedia.page(search)
        print(text)
        # v_result.set(text)    #  v_result.set(text[:500]) แสดงไม่เกิน 500 ตัวอักษร
        v_result.set(text.content[:1500])
        print('LINK:',text.url)
        v_link.set(text.url)

    except:
        v_result.set('ไม่มีข้อมูล กรุณาค้าหาใหม่')

B2 = ttk.Button(T2,text='Search',image=icon_tab2,compound='left',command=Search)
B2.pack()

def readmore():
    webbrowser.open(v_link.get())


B3 = ttk.Button(T2,text='อ่านต่อ',command=readmore)
B3.place(x=600,y=50)

v_result = StringVar()
v_result.set('----------Result---------')
result = Label(T2,textvariable=v_result,wraplength=500)
result.pack()

# ---------------- tab 3 CAFE ----------------------

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New',20))

CF1 = Frame(T3)
CF1.place(x=50,y=100)

# header = ['No.','title','quantity','price','total']
#ROW 0
def Menu1():
    table.insert('','end',value=[1,'ลาเต้',1,30,30])

B = ttk.Button(CF1,text='ลาเต้',image=icon_tab3,compound='top',command=Menu1)
B.grid(row=0,column=0,ipadx=20,ipady=10) 
B = ttk.Button(CF1,text='คาปูชิโน่',image=icon_tab3,compound='top')
B.grid(row=0,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='เอสเปรสโซ่',image=icon_tab3,compound='top')
B.grid(row=0,column=2,ipadx=20,ipady=10)

#ROW 1
B = ttk.Button(CF1,text='ชาเขียว',image=icon_tab3,compound='top')
B.grid(row=1,column=0,ipadx=20,ipady=10) 
B = ttk.Button(CF1,text='ชาเย็น',image=icon_tab3,compound='top')
B.grid(row=1,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาร้อน',image=icon_tab3,compound='top')
B.grid(row=1,column=2,ipadx=20,ipady=10)

# -----------------TABLE--------------------------
CF2 = Frame(T3)
CF2.place(x=500,y=100)

header = ['No.','title','quantity','price','total']
hwidth=[50,200,100,100]

table = ttk.Treeview(CF2,columns=header,show='headings',height=15) # height=10 โชว์แค่ 10 รายการ
table.pack()
# for hd in header:
#     table.heading(hd,text=hd)

for hd,hw in zip(header,hwidth):  #คำสั่ง zip คือการเชื่อม list 2 ตัวเข้าด้วยกัน
    table.column(hd,width=hw)  # กำหนดค่าหัวตาราง
    table.heading(hd,text=hd)  # กำหนดค่าความกว้าง




GUI.mainloop()


# EP5 2:13:00
