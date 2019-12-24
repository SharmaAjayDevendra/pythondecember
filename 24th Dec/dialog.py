from tkinter import *
from tkinter import messagebox
def myFunction():
	ans=messagebox.askretrycancel("Sawal", "Kunal party dega?")
	lbl.config(text=str("Retry Cancel: "+str(ans)))
	ans=messagebox.askyesno("Sawal", "Kunal party dega?")
	lbl.config(text=str("Yes No: "+str(ans)))
	ans=messagebox.askyesnocancel("Sawal", "Kunal party dega?")
	lbl.config(text=str("Yes No Cancel: "+str(ans)))
	ans=messagebox.askokcancel("Sawal", "Kunal party dega?")
	lbl.config(text=str("OK Cancel: "+str(ans)))

window=Tk()
window.title("My App")
window.geometry("500x500")
btn=Button(window, text='Click Me', command=myFunction)
btn.pack()
lbl=Label(window)
lbl.pack()
window.mainloop()
