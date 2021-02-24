#calculator code
#https://github.com/SyedUmaidAhmed/Python-Course-Mathematics-Department/blob/master/Week%205_GUI%20Development%20Tkinter%20Python/gui_seven.py

from tkinter import *
def btnclick(numbers):
    global oprt
    oprt = oprt + str(numbers)
    text_input.set(oprt)
def btnclearnum():
    global oprt
    oprt=""
    text_input.set("")
def btnequal():
    global oprt
    sumup=str(eval(oprt))
    text_input.set(sumup)
    oprt=""
cal = Tk()
cal.title("CALCULATOR")
#cal.attributes("-alpha",0.5)
oprt = ""
text_input = StringVar()
txtdisplay = Entry(cal,font=('Helvetica',20),textvariable=text_input,bd=20,insertwidth=4,bg="#DDDCFC",justify='right')
txtdisplay.grid(columnspan=4)

# clear button
txtclear = Button(cal,padx=16,font=('Helvetica',20),bd=6,text="C",command=btnclearnum)
txtclear.grid(row=1,column=3)

# button 7/8/9/+
btn7= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="7",command=lambda:btnclick(7))
btn7.grid(row=2,column=0)

btn8= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="8",command=lambda:btnclick(8))
btn8.grid(row=2,column=1)

btn9= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="9",command=lambda:btnclick(9))
btn9.grid(row=2,column=2)

add= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="+",command=lambda:btnclick("+"))
add.grid(row=2,column=3)

# button 4/5/6/-
btn4= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="4",command=lambda:btnclick(4))
btn4.grid(row=3,column=0)

btn5= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="5",command=lambda:btnclick(5))
btn5.grid(row=3,column=1)

btn6= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="6",command=lambda:btnclick(6))
btn6.grid(row=3,column=2)

sub= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="-",command=lambda:btnclick("-"))
sub.grid(row=3,column=3)

# button 1/2/3/*
btn1= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="1",command=lambda:btnclick(1))
btn1.grid(row=4,column=0)

btn2= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="2",command=lambda:btnclick(2))
btn2.grid(row=4,column=1)

btn3= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="3",command=lambda:btnclick(3))
btn3.grid(row=4,column=2)

mul= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="*",command=lambda:btnclick("*"))
mul.grid(row=4,column=3)

# button 0/=/(/)/.
btn0= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="0",command=lambda:btnclick(0))
btn0.grid(row=5,column=0)

btneq= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="=",command=btnequal)
btneq.grid(row=5,column=1)

btnpoint= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text=".",command=lambda:btnclick("."))
btnpoint.grid(row=5,column=2)

div= Button(cal,padx=16,bd=6,fg="black",font=('Helvetica',20),text="/",command=lambda:btnclick("/"))
div.grid(row=5,column=3)

cal.mainloop()
