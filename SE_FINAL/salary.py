
def wages():
    
    Hoursworkedinweek = float(hoursworked.get())
    wageperhour = float(hourlyrate.get())
    pay = wageperhour * Hoursworkedinweek
    paydue = "$" ,str('%.2f' %(pay))
    payable.set(paydue)
    
    taxa = pay*0.2
    Taxable = "$" ,str('%.2f' %(taxa))
    tax.set(Taxable)
    
    netpaya = pay - taxa
    Netpays = "$" ,str('%.2f' %(netpaya))
    netpay.set(Netpays)
    
    if Hoursworkedinweek> 40:
        overtimehours = (Hoursworkedinweek - 40) + wageperhour *1.5
        overtimeh = "$" ,str('%.2f' %(overtimehours))
        overtime.set(overtimeh)
        
    elif Hoursworkedinweek<40:
        overtimepay = (Hoursworkedinweek-40) + wageperhour *1.5
        overtimeh = "$", str('%.2f' %(overtimepay))
        overtime.set(overtimeh)
    return

def exit():
    qexit = messagebox.askyesno("Salary management system", "Do you want to exit?")
    if qexit > 0:
        root.destroy()
    return

def Reset():
    Name.set("")
    Address.set("")
    Employer.set("")
    Ninumber.set("")
    hoursworked.set("")
    hourlyrate.set("")
    tax.set("")
    overtime.set("")
    netpay.set("")
    payable.set("")
    txtsalary.delete("1.0",END)
    return
    
def info():
    txtsalary.insert(END,"\t\tSalary\n\n")
    txtsalary.insert(END,"Name: \t\t" + Name.get() + "\n\n")
    txtsalary.insert(END,"Address: \t\t" + Address.get() + "\n\n")
    txtsalary.insert(END,"Employer: \t\t" + Employer.get() + "\n\n")
    txtsalary.insert(END,"Ninumber: \t\t" + Ninumber.get() + "\n\n")
    txtsalary.insert(END,"Hours Worked: \t\t" + hoursworked.get() + "\n\n")
    txtsalary.insert(END,"NET PAY\t\t" + netpay.get() + "\n\n")
    txtsalary.insert(END,"Hourly Rate\t\t" + hourlyrate.get() +"\n\n")
    txtsalary.insert(END,"Tax Payable: \t\t" + tax.get() + "\n\n")
    txtsalary.insert(END,"Payable \t\t" + payable.get() + "\n\n")
    return


import datetime
from tkinter import *
import time
from tkinter import messagebox
import os
#import functions

"""Setting up the geometry and the title"""
root = Tk()
root.title("Salary management system")
root.geometry('1350x650+0+0')
"""set"""


Topframe = Frame(root, width = 1350, height = 50, bd = 8, relief ="raise")
Topframe.pack(side = TOP)

frameone = Frame(root, width = 600, height = 600, bd = 8, relief = "raise")
frameone.pack(side = LEFT)

frametwo = Frame(root, width = 300, height = 700, bd = 8, relief = "raise")
frametwo.pack(side = RIGHT)

fla = Frame(frameone,width = 600, height = 200, bd = 20, relief = "raise")
fla.pack(side = TOP)

flb = Frame(frameone,width = 600, height = 600, bd = 20, relief = "raise")
flb.pack(side = TOP)

lblinfo = Label(Topframe, font =('arial', 60, 'bold'), bg = "lightblue",fg = "Red", text = "    Salary management system     ", bd = 10,)
lblinfo.grid(row = 0, column = 0)

lblmin = Label(Topframe, font = ('arial',15), text = "Minimum 40 hours to avoid pay cut")
lblmin.grid(row = 1,column = 0)

Name = StringVar()
Address = StringVar()
Employer = StringVar()
Ninumber = StringVar()
hoursworked = StringVar()
hourlyrate = StringVar()
tax = StringVar()
overtime = StringVar()
netpay = StringVar()
dateoforder = StringVar()
timeoforder = StringVar()
payable = StringVar()

dateoforder.set(time.strftime("%d/%m/%Y"))

lblName = Label(fla, text = "Name",fg = "green", font = ('arial',16,'bold'),bd = 20)
lblName.grid(row = 0, column = 0)

lbladdress = Label(fla, text = "Address",fg = "green", font = ('arial',16,'bold'),bd = 20)
lbladdress.grid(row = 0, column = 2)

lblEmployer = Label(fla, text = "Employer",fg = "blue", font = ('arial',16,'bold'),bd = 20)
lblEmployer.grid(row = 1, column = 0)

lblNinumber = Label(fla, text = "NI Number",fg = "blue", font = ('arial',16,'bold'),bd = 20)
lblNinumber.grid(row = 1, column = 2)

lblhoursworked = Label(fla, text = "Hours Worked",fg = "red", font = ('arial',16,'bold'),bd = 20)
lblhoursworked.grid(row = 2, column = 0)

lblhourlyrate = Label(fla, text = "Hourly Rate",fg = "red", font = ('arial',16,'bold'),bd = 20)
lblhourlyrate.grid(row = 2, column = 2)

lbltax = Label(fla, text = "Tax payable",fg = "orange", font = ('arial',16,'bold'),bd = 20)
lbltax.grid(row = 3, column = 0)

lblovertime = Label(fla, text = "Extra Bonus",fg = "orange", font = ('arial',16,'bold'),bd = 20)
lblovertime.grid(row = 3, column = 2)

lblgrosspay = Label(fla, text = "Grosspay", font = ('arial',16,'bold'),bd = 20)
lblgrosspay.grid(row = 4, column = 0)

lblNetpay = Label(fla, text = "Net Pay", font = ('arial',16,'bold'),bd = 20)
lblNetpay.grid(row = 4, column = 2)




etxtname = Entry(fla, textvariable = Name, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxtname.grid(row = 0, column = 1)

etxtadd = Entry(fla, textvariable = Address, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxtadd.grid(row = 0, column = 3)

etxtemployer = Entry(fla, textvariable = Employer, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxtemployer.grid(row = 1, column = 1)

etxtnumber = Entry(fla, textvariable = Ninumber, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxtnumber.grid(row = 1, column = 3)

etxthoursw = Entry(fla, textvariable = hoursworked, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxthoursw.grid(row = 2, column = 1)

etxthourlyr = Entry(fla, textvariable = hourlyrate, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxthourlyr.grid(row = 2, column = 3)

etxttax = Entry(fla, textvariable = tax, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxttax.grid(row = 3, column = 1)

etxtovertime = Entry(fla, textvariable = overtime, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxtovertime.grid(row = 3, column = 3)

etxtnetpay = Entry(fla, textvariable = netpay, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxtnetpay.grid(row = 4, column = 3)

etxtpayable = Entry(fla, textvariable = payable, font = ('arial',16,'bold'),bd = 16,width = 22, justify = 'left')
etxtpayable.grid(row = 4, column = 1)


lblsalary = Label(frametwo,textvariable = dateoforder, font = ('arial',21,'bold')).grid(row = 0, column = 0)
txtsalary = Text(frametwo, height = 22, width = 34, bd = 16, font=('arial',12,'bold'))
txtsalary.grid(row = 1, column = 0)



btnsalary = Button(flb,text = 'Weekly Salary', padx = 16, pady = 16, bd =8, fg = "black",bg = "yellow", font = ('arial',16,'bold'), width = 14, height = 1,command = wages).grid(row = 0, column = 0)

btnreset = Button(flb,text = 'Reset', padx = 16, pady = 16, bd =8, fg = "black",bg = "pink", font = ('arial',16,'bold'), width = 14, height = 1, command = Reset).grid(row = 0, column = 1)

btnpayslip = Button(flb,text = 'View Payslip', padx = 16, pady = 16, bd =8, fg = "black",bg = "orange", font = ('arial',16,'bold'), width = 14, height = 1,command = info).grid(row = 0, column = 2)

btnexit = Button(flb,text = 'Exit System', padx = 16, pady = 16, bd =8, fg = "black",bg = "white", font = ('arial',16,'bold'), width = 14, height = 1, command = exit).grid(row = 0, column = 3)


root.mainloop()