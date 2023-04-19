from tkinter import *
import datetime
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    date=time.strftime('%d')
    mon=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    lable_hr.config(text=hr)
    lable_min.config(text=min)
    lable_sec.config(text=sec)
    lable_am.config(text=am)
    lable_date.config(text=date)
    lable_mon.config(text=mon)
    lable_year.config(text=year)
    lable_day.config(text=day)


    lable_hr.after(200,date_time)


clock=Tk()
clock.title("Digital Clock")
clock.geometry('900x505')
clock.config(bg='#d8f2f2')

lable_hr=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='#cbedc5',fg='#4f594e')
lable_hr.place(x=75,y=75,height=100,width=150)

lable_min=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='#cbedc5',fg='#4f594e')
lable_min.place(x=275,y=75,height=100,width=150)

lable_sec=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='#cbedc5',fg='#4f594e')
lable_sec.place(x=475,y=75,height=100,width=150)

lable_am=Label(clock,text="00",font=('Time New Roman',50,"bold"),bg='#cbedc5',fg='#4f594e')
lable_am.place(x=675,y=75,height=100,width=150)

#templates

lable_ht=Label(clock,text="hours",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_ht.place(x=75,y=200,height=30,width=150)

lable_mt=Label(clock,text="minutes",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_mt.place(x=275,y=200,height=30,width=150)

lable_st=Label(clock,text="seconds",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_st.place(x=475,y=200,height=30,width=150)

lable_at=Label(clock,text="AM/PM",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_at.place(x=675,y=200,height=30,width=150)

#date month year day

lable_date=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='#cbedc5',fg='#4f594e')
lable_date.place(x=75,y=273,height=100,width=150)

lable_mon=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='#cbedc5',fg='#4f594e')
lable_mon.place(x=275,y=273,height=100,width=150)

lable_year=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='#cbedc5',fg='#4f594e')
lable_year.place(x=475,y=273,height=100,width=150)

lable_day=Label(clock,text="00",font=('Time New Roman',48,"bold"),bg='#cbedc5',fg='#4f594e')
lable_day.place(x=675,y=273,height=100,width=150)

#templates

lable_datet=Label(clock,text="DATE",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_datet.place(x=75,y=398,height=30,width=150)

lable_mont=Label(clock,text="MONTH",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_mont.place(x=275,y=398,height=30,width=150)

lable_yet=Label(clock,text="YEAR",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_yet.place(x=475,y=398,height=30,width=150)

lable_dayt=Label(clock,text="DAY",font=('Time New Roman',15),bg='#cbedc5',fg='#4f594e')
lable_dayt.place(x=675,y=398,height=30,width=150)



date_time()
clock.mainloop()