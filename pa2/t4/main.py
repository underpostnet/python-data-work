





import tkinter


form = tkinter.Tk()
form.geometry("500x400")

def defcompose():
    result = "test"
    result = tkinter.Label(form, text= result)
    result.pack()

inputNumber = tkinter.Entry(form)
inputNumber.pack()


btn = tkinter.Button(form, text="Descomponer", command = defcompose)
btn.pack()


form.mainloop()
