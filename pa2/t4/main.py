
import tkinter

form = tkinter.Tk()
form.geometry("500x400")

inputNumber = tkinter.Entry(form)
inputNumber.pack()

def defcompose():
    result = ""
    for n in range(0, len(inputNumber.get())):
        op = int(inputNumber.get()) // 10**n % 10;
        result += str(op) + ("0"*n) + "\n"

    result = tkinter.Label(form, text= result)
    result.pack()

print()

btn = tkinter.Button(form, text="Descomponer", command = defcompose)
btn.pack()


form.mainloop()
