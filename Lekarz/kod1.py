from tkinter import *
import tkinter
import socket
import json
import ast


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("34.105.186.206", 20001))

root = Tk()
root.title("Logowanie")
lista = []


def rejstracja(label):

    def show_text():
        login = a.get()
        password = b.get()
        post = str({'type':"logindoktor", 'login': str(login), 'password': str(password)})
        s.send(bytes((post).encode('UTF-8')))


        data = s.recv(2048)
        msg = data.decode('UTF-8')
        msg = ast.literal_eval(msg)


        if msg["error"] == "653": #loguje doktora

            label.config(text="Zalogowano pomyślnie")
            root.destroy()

            okno = tkinter.Tk()
            def wyszukaj():
                imie = c.get()
                nazwisko = d.get()
                if imie == "andrzej" and nazwisko == "kowalski": # wyszukuje pacjenta
                    okno.destroy()
                    okno2 = tkinter.Tk()
                    def leki(): #pozwala wpisać leki przypisane
                        entry3 = tkinter.Entry(okno2,textvariable=c)
                        entry3.place(rely=0.2, relwidth=0.6, relheight=0.1)


                    canvas = tkinter.Canvas(okno2, width=300, height=400, bg='pink')
                    canvas.grid()
                    label1 = tkinter.Label(okno2, text="Pacjent: andrzej kowalski")
                    label1.place(relwidth=0.6, relheight=0.1)
                    b4 = tkinter.Button(okno2, text="Leki", command=leki)
                    b4.place(rely=0.12, relwidth=0.6, relheight=0.1)

                    okno2.mainloop()
                else:
                    label.config(text="nie ma takiego pacjenta")



            canvas = tkinter.Canvas(okno, width=300, height=400)
            canvas.grid()
            c = StringVar()
            d = StringVar()
            label1 = tkinter.Label(okno, text="wpisz imie i nazwisko pacjenta:")
            label1.place(relwidth=0.6, relheight=0.1)
            entry1 = tkinter.Entry(okno,textvariable=c)
            entry1.place(rely=0.1, relwidth=0.5, relheight=0.1)
            entry2 = tkinter.Entry(okno, textvariable=d)
            entry2.place(relx=0.52, rely=0.1, relwidth=0.5, relheight=0.1)

            b3 = tkinter.Button(okno, text="wyszukaj", command=wyszukaj)
            b3.place(relx=0.5, rely=0.23, relwidth=0.3, relheight=0.075)

            okno.mainloop()



        else:
            label.config(text="Logowanie się nie powiodło. spróbuj ponownie.")

    return show_text


a = StringVar()
b = StringVar()

Label(text="login :").grid(row=0, column=0)
Entry(textvariable=a).grid(row=0, column=1)
Label(text="Hasło :").grid(row=1, column=0)
Entry(textvariable=b).grid(row=1, column=1)

result_label = Label(root, text="")
result_label.grid(row=4, column=0)

button_command = rejstracja(result_label)
Button(text="rejstracja", command=button_command).grid(row=3, column=1)


root.mainloop()







