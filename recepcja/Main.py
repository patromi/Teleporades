import tkinter as tk
import Panel
import Client

HOST = '34.105.186.206' #'34.105.186.206'
PORT = 20001

LOGINRECEPTION = "loginreception" #type logowania
REGISTERRECEPTION = "registerreception" #type rejestracji
REGISTERDOCTOR = "registerdoctor" #type rejestacji lekarza
GETDOCTORS = "idlek" #type otrzymywania lekarzy

root = tk.Tk()
root.title("Logowanie")
root.geometry("800x640")
root.configure(background="white")

#łączenie z serverem
client = Client.Client(HOST, PORT, LOGINRECEPTION, REGISTERRECEPTION, REGISTERDOCTOR, GETDOCTORS)
# print(client.getDoctors(0))
# print(client.getMsg())

#Logowanie
Login1 = tk.Label(root, text="Login:", bg="white").place(x = 10, y = 10)
login1 = tk.Entry(root, width=50)
login1.pack()
login1.place(x = 10, y = 40)

Pas1 = tk.Label(root, text="Hasło:", bg="white").place(x = 10, y = 80)
pas1 = tk.Entry(root, width=50, show="*")
pas1.pack()
pas1.place(x = 10, y = 110)

def search():
    if client.isConnect(HOST, PORT):
        client.sendLoginReception(login1.get(), pas1.get())
        re = client.isSucces()
        if re:
            root.destroy()
            Panel.Panel.__init__(Panel, client, HOST, PORT)
        else:
            Again = tk.Label(root, text="Błędne dane logowania", bg="white", fg="red").place(x=10, y=140)
    else:
        Again = tk.Label(root, text="Nie można połączyć z serverem", bg="white", fg="red").place(x=10, y=140)


Log = tk.Button(root, text="Zaloguj", command=search).place(width = 100, height = 30, x = 10, y = 170)

#Rejestracja
Login2 = tk.Label(root, text="Login:", bg="white").place(x = 400, y = 10)
login2 = tk.Entry(root, width=50)
login2.pack()
login2.place(x = 400, y = 40)

Pas2 = tk.Label(root, text="Hasło:", bg="white").place(x = 400, y = 80)
pas2 = tk.Entry(root, width=50, show="*")
pas2.pack()
pas2.place(x = 400, y = 110)

Pas2p = tk.Label(root, text="Powtórz Hasło:", bg="white").place(x = 400, y = 150)
pas2p = tk.Entry(root, width=50, show="*")
pas2p.pack()
pas2p.place(x = 400, y = 180)

Email = tk.Label(root, text="Email:", bg="white").place(x = 400, y = 210)
email = tk.Entry(root, width=50)
email.pack()
email.place(x = 400, y = 240)

City = tk.Label(root, text="Miasto:", bg="white").place(x = 400, y = 270)
city = tk.Entry(root, width=50)
city.pack()
city.place(x = 400, y = 300)

Street = tk.Label(root, text="Ulica:", bg="white").place(x = 400, y = 330)
street = tk.Entry(root, width=30)
street.pack()
street.place(x = 400, y = 360)

Number = tk.Label(root, text="Numer placówki:", bg="white").place(x = 600, y = 330)
number = tk.Entry(root, width=16)
number.pack()
number.place(x = 600, y = 360)

Name2 = tk.Label(root, text="Nazwa kliniki:", bg="white").place(x = 400, y = 390)
name2 = tk.Entry(root, width=50)
name2.pack()
name2.place(x = 400, y = 420)

Phone = tk.Label(root, text="Numer telefonu:", bg="white").place(x = 400, y = 450)
phone = tk.Entry(root, width=50)
phone.pack()
phone.place(x = 400, y = 480)

var = tk.StringVar()
Info = tk.Label(root, textvariable=var, bg="white", fg="red").place(x=400, y=510)

def isNumber(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

def register():
    if client.isConnect(HOST, PORT): #sprawdzenie dostepnosci servera
        if pas2.get() == pas2p.get(): #potwierdzenie hasla prawidlowe
            if len(pas2.get()) > 5: #conajmniej 6 znaków hasła
                if len(phone.get()) > 0 and len(login2.get()) > 0 and len(email.get()) > 0 and len(city.get()) > 0 and len(street.get()) > 0 and len(number.get()) > 0 and len(phone.get()) > 0 and len(name2.get()) > 0: #uzupelnione wszystkie pola
                    try:
                        str(email.get()).index("@") #sprawdzić czy email poprowny
                        client.sendRegisterReception(login2.get(), pas2.get(), email.get(), city.get(), street.get(), number.get(),phone.get(), name2.get())
                        re = client.isSucces()
                        if re: #odpowiedz servera
                            var.set("Rejestracja powiodła się")
                            login2.delete(0, len(login2.get()))
                            pas2.delete(0, len(pas2.get()))
                            pas2p.delete(0, len(pas2p.get()))
                            email.delete(0, len(email.get()))
                            city.delete(0, len(city.get()))
                            street.delete(0, len(street.get()))
                            phone.delete(0, len(phone.get()))
                            name2.delete(0, len(name2.get()))
                        else: #wybrany użytkownik już istnieje
                            var.set("Wybrana klinika już istnieje")
                            pas2.delete(0, len(pas2.get()))
                            pas2p.delete(0, len(pas2p.get()))
                    except ValueError:
                        var.set("Napisz poprwanie email")
                        pas2.delete(0, len(pas2.get()))
                        pas2p.delete(0, len(pas2p.get()))
                else:
                    var.set("Uzupełnij wszystkie pola formularza")
                    pas2.delete(0, len(pas2.get()))
                    pas2p.delete(0, len(pas2p.get()))
            else:
                var.set("Hasło musi mieć conajmniej 6 znaków")
                pas2.delete(0, len(pas2.get()))
                pas2p.delete(0, len(pas2p.get()))
        else:
            var.set("Przepisz poprawnie hasło")
            pas2.delete(0, len(pas2.get()))
            pas2p.delete(0, len(pas2p.get()))
    else:
        var.set("Nie można połączyć z serverem")
        pas2.delete(0, len(pas2.get()))
        pas2p.delete(0, len(pas2p.get()))

Reg = tk.Button(root, text="Zarejestruj", command=register).place(width = 100, height = 30, x = 400, y = 540)

def clickEnter(event):
    if repr(event.char) == repr('\r'):
        if str(root.focus_get()) == ".!entry":
            pas1.focus_set()
        if str(root.focus_get()) == ".!entry2" and len(pas1.get()) > 0:
            search()

root.bind("<Key>", clickEnter)

root.mainloop()