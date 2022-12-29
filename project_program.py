from tkinter import *
from tkinter.filedialog import *
from csv import *
from tkinter.font import Font
from tkinter.ttk import Treeview
from tkcalendar import *
import csv
from tkinter import filedialog
from datetime import datetime

# สร้างหน้าต่างที่ เเสดงผลหาค่าเฉลี่ย ค่าสูงสุดตำสุด


def sigma():

    # ทำลายหน้าจอเดิมย้อนกลับไปยังหน้าจอ input
    def back_to_main():
        window.destroy()
        main_window()

    # อ่านข้อมูลในไฟล์ทุกบรรทัดเเละส่งข้อมูลเเต่ละบรรทัด เป็น list
    def readall_text():
        with open(namefile, "r", encoding="utf-8") as infile:
            readallitem = csv.reader(infile)
            readall = list(readallitem)    
        return readall

    # หาค่าเฉลี่ยรายจ่ายต่อวัน ค่าสูงสุดค่าต่ำสุด หาค่าเฉลี่ยรายจ่ายต่อวัน ค่าสูงสุดค่าต่ำสุดที่จายในวัน
    def find_sigma_expenses_income():
        readall = readall_text()
        list_income = []
        list_expenses = []
        list_day = []
        for item in (readall):
            if item[0] not in list_day:
                list_day.append(item[0])
            if item[1] == "รายจ่าย":
                list_expenses.append(float(item[4]))
            else:
                list_income.append(float(item[3]))
        if list_day == [] or (sum(list_expenses) == 0):
            expenses_sigma.set(0.0)
            max_expenses.set(0.0)
            min_expenses.set(0.0)
        else:
            expenses_sigma.set("%6.2f" % ((sum(list_expenses)/len(list_day))))
            max_expenses.set(max(list_expenses))
            min_expenses.set(min(list_expenses))

        if list_day == [] or (sum(list_income) == 0):
            income_sigma.set(0.0)
            max_income.set(0.0)
            min_income.set(0.0)
        else:
            income_sigma.set("%6.2f" % ((sum(list_income)/len(list_day))))
            max_income.set(max(list_income))
            min_income.set(min(list_income))

    # หน้าต่างแสดง max, min, etc.
    window = Tk()
    window.title("โปรแกรมรายรับรายจ่าย")
    window.minsize(450, 150)
    window.config(bg="#CED8E1")
    main_frame = Frame(window)
    main_frame.config(bg="#CED8E1")
    main_frame.grid(row=0, column=0, padx=10, pady=10)
    income_sigma = DoubleVar(window)
    expenses_sigma = DoubleVar(window)
    max_income = DoubleVar(window)
    min_income = DoubleVar(window)
    max_expenses = DoubleVar(window)
    min_expenses = DoubleVar(window)

    find_sigma_expenses_income()

    # ตกแต่งfont label
    label_font = Font(size=10,)

    # row 0 in fram
    blank_frame00 = Frame(main_frame, width=115, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#102B3E")
    blank_frame00.grid(row=0, column=0, )

    blank_frame01 = Frame(main_frame, width=93,  height=26,
                          highlightbackground="black", highlightthickness=2, bg="#1CC8A0")
    blank_frame01.grid(row=0, column=1,)

    blank_frame02 = Frame(main_frame, width=115, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#102B3E")
    blank_frame02.grid(row=0, column=3,)

    blank_frame03 = Frame(main_frame, width=93, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#1CC8A0")
    blank_frame03.grid(row=0, column=4,)

    addlabel1 = Label(main_frame, text="รายได้เฉลี่ย",
                      bg="#102B3E", fg="#ffffff", font=label_font)
    addlabel1.grid(row=0, column=0)
    label1 = Label(main_frame, textvariable=income_sigma,
                   bg="#1CC8A0", font=label_font)
    label1.grid(row=0, column=1)

    # 2 บรรทัดนี้ แทรกระหว่าง รายจ่ายกับรายได้
    ins_column0 = Label(main_frame, text=" ", bg="#CED8E1")
    ins_column0.grid(row=0, column=2, padx=10)

    addlabel2 = Label(main_frame, text="รายจ่ายเฉลี่ย",
                      bg="#102B3E", fg="#ffffff", font=label_font)
    addlabel2.grid(row=0, column=3)
    label2 = Label(main_frame, textvariable=expenses_sigma,
                   bg="#1CC8A0", font=label_font)
    label2.grid(row=0, column=4)

    # row 1 in frame
    blank_frame10 = Frame(main_frame, width=115, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#102B3E")
    blank_frame10.grid(row=1, column=0,)

    blank_frame11 = Frame(main_frame, width=93,  height=26,
                          highlightbackground="black", highlightthickness=2, bg="#1CC8A0")
    blank_frame11.grid(row=1, column=1,)

    blank_frame12 = Frame(main_frame, width=115, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#102B3E")
    blank_frame12.grid(row=1, column=3)

    blank_frame13 = Frame(main_frame, width=93,  height=26,
                          highlightbackground="black", highlightthickness=2, bg="#1CC8A0")
    blank_frame13.grid(row=1, column=4)

    addlabel3 = Label(main_frame, text="รายได้สูงสุด",
                      bg="#102B3E", fg="#ffffff", font=label_font)
    addlabel3.grid(row=1, column=0)
    label3 = Label(main_frame, textvariable=max_income,
                   bg="#1CC8A0", font=label_font)
    label3.grid(row=1, column=1)

    addlabel5 = Label(main_frame, text="รายจ่ายสูงสุด",
                      bg="#102B3E", fg="#ffffff", font=label_font)
    addlabel5.grid(row=1, column=3)
    label5 = Label(main_frame, textvariable=max_expenses,
                   bg="#1CC8A0", font=label_font)
    label5.grid(row=1, column=4)

    # row 2 in frame
    blank_frame20 = Frame(main_frame, width=115, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#102B3E")
    blank_frame20.grid(row=2, column=0, )

    blank_frame21 = Frame(main_frame, width=93,  height=26,
                          highlightbackground="black", highlightthickness=2, bg="#1CC8A0")
    blank_frame21.grid(row=2, column=1,)

    blank_frame22 = Frame(main_frame, width=115, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#102B3E")
    blank_frame22.grid(row=2, column=3,)

    blank_frame23 = Frame(main_frame, width=93, height=26,
                          highlightbackground="black", highlightthickness=2, bg="#1CC8A0")
    blank_frame23.grid(row=2, column=4,)

    addlabel4 = Label(main_frame, text="รายได้ต่ำสุด",
                      bg="#102B3E", fg="#ffffff", font=label_font)
    addlabel4.grid(row=2, column=0)
    label4 = Label(main_frame, textvariable=min_income,
                   bg="#1CC8A0", font=label_font)
    label4.grid(row=2, column=1)

    addlabel6 = Label(main_frame, text="รายจ่ายต่ำสุด",
                      bg="#102B3E", fg="#ffffff", font=label_font)
    addlabel6.grid(row=2, column=3)
    label6 = Label(main_frame, textvariable=min_expenses,
                   bg="#1CC8A0", font=label_font)
    label6.grid(row=2, column=4)

    # row 1 window
    back = Button(window, text="BACK", command=back_to_main,
                  width=20, bg="#40cbb6")
    back.grid(row=1, column=0, columnspan=4, sticky=W, padx=10, pady=10)
    back = Button(window, text="CLOSE",
                  command=window.destroy, width=20, bg="red")
    back.grid(row=1, column=0, columnspan=4, sticky=E, padx=10, pady=10)
    window.mainloop()

# หน้าต่างหลัก


def main_window():
    window = Tk()
    window.minsize(725, 500)
    window.title("โปรแกรมรายรับรายจ่าย")
    window.config(bg="#CED8E1")
    window.register(False, False)

    # destroy หน้าต่าง เดิมเเละเปิดหน้าใหม่

    def open_new2():
        window.destroy()
        sigma()

    # อ่านข้อมูลในไฟล์ทุกบรรทัดเเละส่งข้อมูลเเต่ละบรรทัด เป็น list
    def readall_text():
        with open(namefile, "r", encoding="utf-8") as infile:
            readallitem = csv.reader(infile)
            readall = list(readallitem)
        return readall

    # เพิ่มข้อมูลใน file  เเละ treeview เเละ set  balance_money

    def add():
        day_m = a.get_date()
        day_m = day_m.strftime("%d/%m/%Y")
        type_m = type_money.get()
        list_m = list_money.get()
        balance_m = balance_money.get()
        if list_m == "":
            list_m = "-"

        # chack Error หากเกิดError ให้เเจ้งเตือน
        try:
            amount_m = amount_money.get()
        except:
            label_test.config(
                text="Error : โปรดใส่จำนวนเงินเป็นตัวเลข", foreground="red", font=label_font)
            return
        if chack_integer(amount_m) == True:
            return

        balance_m += find_type_money(type_m, amount_m)
        with open(namefile, "a", encoding="utf-8")as outfile:
            if type_m == "รายได้":
                line = [day_m, type_m, list_m, amount_m, "-", balance_m]
            else:
                line = [day_m, type_m, list_m, "-", amount_m, balance_m]
            writercsv = csv.writer(outfile, lineterminator="\n")
            writercsv.writerow(line)

        label_test.config(text="บันทึกเรียบร้อย",
                          foreground="green", font=label_font)

        balance_money.set(balance_m)
        treeview_main.insert(parent="", index="end", iid=len(readall_text(
        )), text="", values=(line[0], line[1], line[2], line[3], line[4], line[5]))

    # หาค่า balance_money()

    def set_balance_money():
        readall = readall_text()
        if len(readall) != 0:
            readall = readall_text()
            balance = (float(readall[-1][-1]))
        else:
            balance = 0.0
        balance_money.set(balance)


    # check ว่าเป็นรายรับหรือรายจ่าย
    def find_type_money(typemoney, amount_money_int):
        if typemoney == "รายได้":
            amount = amount_money_int
        else:
            amount = -amount_money_int
        return amount

    # ฟังก์ชั่น check ว่าเป็นจำนวนเต็มบวกหรือไม่
    def chack_integer(amount):
        if amount <= 0.0:
            setbool = True
            label_test.config(
                text="Error : โปรดกรอกข้อมูลในช่องจํานวนเงิน", foreground="red", font=label_font)
        else:
            setbool = False
        return setbool

    # ฟังก์ชั้นตรวจสอบว่ามีจำนวนline ใน text อยู่เท่าไร

    # ลบข้อมูลทั้งหมดใน treeview

    def remove_all_treeview():
        for recond in treeview_main.get_children():
            print(recond)
            treeview_main.delete(recond)

    # เพิ่มข้อมูลจาก list ลงใน treeview
    def add_allform_file():
        readall = readall_text()
        for number, line in enumerate(readall):
            treeview_main.insert(parent="", index="end", iid=number, text="", values=(
                line[0], line[1], line[2], line[3], line[4], line[5]))

    # เลือกข้อมูลใน treeview เเละลบเเละบันทึกข้อมูลลงไปในfile ใหม่
    def delete():
        try:
            deleteitme = int(list(treeview_main.selection()).pop(0))
        except IndexError:
            label_test.config(text="โปรดเลือกรายการที่ต้องการลบ", foreground="red")
            return
        new_list = []
        for i, item in enumerate(readall_text()):
            if deleteitme > i:
                new_list.append(item)
            elif deleteitme < i:
                if item[1] == "รายได้":
                    addint = float(item[3])
                else:
                    addint = -float(item[4])
                if deleteitme != 0 and i != 1:
                    new_blance = float(new_list[-1][-1])+addint
                else:
                    new_blance = 0+addint
                item.pop(-1)
                item.insert(5, new_blance)
                new_list.append(item)

        with open(namefile, "w", encoding="utf-8") as outfile:
            writerfile = csv.writer(outfile, lineterminator="\n")
            writerfile.writerows(new_list)
        remove_all_treeview()
        add_allform_file()
        set_balance_money()

    type_money_dicts = {
        "รายได้": 1,
        "รายจ่าย": 2,
    }
    type_money = StringVar(window, "รายได้")
    list_money = StringVar()
    amount_money = DoubleVar()
    balance_money = DoubleVar()
    set_balance_money()

    # สร้างกรอบ row = 1
    blank_frame1 = Frame(window, width=120, height=50, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=1, column=1,)
    blank_frame2 = Frame(window, width=93,  height=50, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=1, column=2,)
    blank_frame3 = Frame(window, width=341, height=50, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=1, column=3,)
    blank_frame5 = Frame(window, width=127, height=50, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=1, column=4,)
    blank_frame6 = Frame(window, width=128, height=50, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=1, column=5,)

    # สร้างกรอบ row = 2
    blank_frame7 = Frame(window, width=120, height=33, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=2, column=1,)
    blank_frame8 = Frame(window, width=93,  height=33, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=2, column=2,)
    blank_frame9 = Frame(window, width=341, height=33, highlightbackground="black",
                         highlightthickness=2, bg="#00ff7f").grid(row=2, column=3,)
    blank_frame10 = Frame(window, width=127, height=33, highlightbackground="black",
                          highlightthickness=2, bg="#00ff7f").grid(row=2, column=4,)
    blank_frame11 = Frame(window, width=128, height=33, highlightbackground="black",
                          highlightthickness=2, bg="#00ff7f").grid(row=2, column=5,)

    # ตกแต่งfont header
    head_font = Font(size=10,
                     weight="bold")

    # ตกแต่งfont label
    label_font = Font(size=10,)

    # row1
    blank1 = Label(window, text="วัน/เดือน/ปี", bg="#102B3E", fg="#ffffff",
                   font=head_font).grid(row=1, column=1, ipadx=24.5, ipady=12.5)
    blank2 = Label(window, text="ประเภท", bg="#102B3E", fg="#ffffff",
                   font=head_font).grid(row=1, column=2, ipadx=21, ipady=12.5)
    blank3 = Label(window, text="รายการ", bg="#102B3E", fg="#ffffff",
                   font=head_font).grid(row=1, column=3, ipadx=143.5, ipady=12.5)
    blank5 = Label(window, text="จำนวนเงิน", bg="#102B3E", fg="#ffffff",
                   font=head_font).grid(row=1, column=4, ipadx=29, ipady=12.5)
    blank6 = Label(window, text="เงินคงเหลือ", bg="#102B3E", fg="#ffffff",
                   font=head_font).grid(row=1, column=5, ipadx=29, ipady=12.5)

    # row2
    a = DateEntry(window, select="day",  width=16,)
    a.grid(row=2, column=1, ipady=5)

    # row2 listbox
    b = OptionMenu(window, type_money, *list(type_money_dicts.keys()),)
    b.grid(row=2, column=2, ipadx=8)
    c = Entry(window, textvariable=list_money,      bg="#1CC8A0")   .grid(
        row=2, column=3, ipadx=108, ipady=5)
    e = Entry(window, textvariable=amount_money,    bg="#1CC8A0")   .grid(
        row=2, column=4, ipadx=1.3, ipady=5)
    f = Label(window, textvariable=balance_money,   bg="#1CC8A0",
              width=6)   .grid(row=2, column=5, ipadx=40,  ipady=4)

    # row 3
    label_test = Label(window, bg="#CED8E1")
    label_test.grid(row=3, column=3, pady=10)

    # row 4
    ok_test = Button(window, text="SAVE", command=add,
                     width=10, height=2, bg="#40cbb6")
    ok_test.grid(row=4, column=2)
    button_delete = Button(window, text="DELETE", width=10,
                           height=2, command=delete, bg="#40cbb6")
    button_delete.grid(row=4, column=4)

    # row 5
    treeview_main = Treeview(window)
    treeview_main.grid(row=5, columnspan=6, pady=10)

    treeview_main['columns'] = (
        "day", "type", "list", "income", "expaness", "sum")

    treeview_main.column("#0", width=20, minwidth=25)
    treeview_main.column("day", width=80)
    treeview_main.column("type", width=60)
    treeview_main.column("list", width=200)
    treeview_main.column("income", width=80)
    treeview_main.column("expaness", width=80)
    treeview_main.column("sum", width=80)

    treeview_main.heading("day", text="วัน/เดือน/ปี")
    treeview_main.heading("type", text="ประเภท")
    treeview_main.heading("list", text="รายการ")
    treeview_main.heading("income", text="รายรับ")
    treeview_main.heading("expaness", text="รายจ่าย")
    treeview_main.heading("sum", text="เงินคงเหลือ")

    add_allform_file()
    # row 5 สุดท้าย

    # row 6
    buttontest = Button(window, text="SHOW", command=open_new2,
                        width=10, height=2, bg="yellow")
    buttontest.grid(column=2, row=6)
    buttonclose = Button(window, text="CLOSE",
                         command=window.destroy, width=10, height=2, bg="red")
    buttonclose.grid(column=4, row=6,)
    window.mainloop()


if __name__ == "__main__":

    # เลือก file csv เพื่อใช้งานเเละเปิดหน้าหน้าต่อไป
    def browseFiles():
        global namefile
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Csv files",
                                                          "*.csv*"),
                                                         ("all files",
                                                          "*.*")))
        namefile = str(filename)
        print(namefile)
        if namefile != "":
            window_login.destroy()
            name_string.set(namefile)
            main_window()

    # หน้าต่างเลือก file
    window_login = Tk()
    window_login.title("โปรแกรมรายรับรายจ่าย")
    window_login.minsize(385, 100)
    window_login.config(bg="#CED8E1")
    name_string = StringVar()

    # ตกแต่งfont label
    label_font = Font(size=10,)

    Labletest = Label(window_login, text="โปรดเลือกไฟล์ CSV :",
                      bg="#CED8E1", font=label_font)
    Labletest.grid(column=0, row=0, columnspan=3, pady=5)
    Buttontest = Button(window_login, text="SELECT FILE",
                        command=browseFiles, width=50, height=2, bg="#40cbb6")
    Buttontest.grid(column=0, row=1, padx=20, pady=5)
    Buttonclose = Button(window_login, text="CLOSE",
                         command=window_login.destroy, width=10, bg="red")
    Buttonclose.grid(column=0, row=2, pady=5)
    window_login.mainloop()
