from tkinter import *
def myFunction():
	print(s.get())
	print(sh.get())
window=Tk()
window.title("My App")
window.geometry("500x500")
s=Scale(window, from_=0, to=100)
s.pack()
sh=Scale(window, from_=100, to=200, orient=HORIZONTAL)
sh.pack()

btn=Button(window, text='Click Me', command=myFunction)
btn.pack()
window.mainloop()
