from tkinter import *
window=Tk()
window.title("AutoDice")
window.geometry("1000x1000")
f=('arial', 20, 'bold')

lbl=Label(window, text='Enter Your Name', font=f)
inp=Entry(window, font=f)
btn=Button(window, text='Submit', font=f, fg='#ffffff', bg='#006699')

lbl.place(x=100, y=50, width=230, height=50)
inp.place(x=350, y=50, width=300, height=50)
btn.place(x=350, y=120, width=300, height=50)
window.state('zoomed')
window.mainloop()
