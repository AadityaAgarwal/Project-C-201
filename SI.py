from tkinter import *

window=Tk()
window.geometry("400x400")
window.title("SI Calculator")
def calc_SI():
    name=name_entry_label.get()
    p=float(p_entry_label.get())
    r=float(r_entry_label.get())
    t=float(t_entry_label.get())

    SI=round(((p*r*t)/100),2)

    result_label.destroy()
   

    print(SI)
    output_msg=Label(result_frame,text=name+"'s SI: "+str(SI)+" \n",font=("calibri",12),width=40,fg='white')
    output_msg.place(x=20,y=20)
    output_msg.pack()

window.configure(bg="black")
heading_label=Label(window,text="SI Calculator",fg='white',font=('calibri',20),bd=5)
heading_label.place(x=100,y=20)

name_label=Label(window,text="Enter name: ",fg='yellow',font=('calibri',12),bd=1)
name_label.place(x=20,y=80)

name_entry_label=Entry(window,text="",fg='white',bd=2,width=20)
name_entry_label.place(x=200,y=80)

p_label=Label(window,text="Enter principal(in rupees): ",fg='yellow',font=('calibri',12),bd=1)
p_label.place(x=20,y=120)

p_entry_label=Entry(window,text="",fg='white',bd=2,width=20)
p_entry_label.place(x=200,y=120)

r_label=Label(window,text="Enter rate of interest: ",fg='yellow',font=('calibri',12),bd=1)
r_label.place(x=20,y=160)

r_entry_label=Entry(window,text="",fg='white',bd=2,width=20)
r_entry_label.place(x=200,y=160)

t_label=Label(window,text="Enter time period: ",fg='yellow',font=('calibri',12),bd=1)
t_label.place(x=20,y=200)

t_entry_label=Entry(window,text="",fg='white',bd=2,width=20)
t_entry_label.place(x=200,y=200)

calculate_button=Button(window,text="Calculate",fg='red',bd=3,command=calc_SI)
calculate_button.place(x=100,y=240)

result_frame=LabelFrame(window,text="result",font=("Calibri",15))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text="",fg='white',bd=2,width=40,font=('calibri',12))
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()

