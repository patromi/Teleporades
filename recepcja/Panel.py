import tkinter as tk
import Doctor, Data
import CalendarGraph
import calendar
import datetime

class Panel:
    def __init__(self, client, HOST, PORT):
        global msg, doctor, data0
        root = tk.Tk()
        root.title("Recepcja")
        root.geometry("1280x800+0+0")
        root.configure(background="white")
        doctor = []
        data0 = []

        msg = client.getMessageRec()

        def guit():
            cal.closeThread()

        root.protocol("WM_DELETE_WINDOW", quit)

        DocList = tk.Label(root, text="Lista Lekarzy:", bg="white").place(x=10, y=10)
        docList = tk.Listbox(root, width=50, height=4)
        docList.pack()
        docList.place(x=10, y=40)

        scrl = tk.Scrollbar(root)

        doctor.append(Doctor.Doctor(0, "Wszyscy", "Lekarze", "0", "-"))
        def addDoctors():
            list = client.getDoctors(msg['id'])
            for i in range(len(list)):
                d = list[i]
                doctor.append(Doctor.Doctor(d['id'], d['fisrtname'], d['lastname'], data0, d['specjalizacja']))
        addDoctors()

        def addData():
            pass

        #pobieranie lekarzy
        for doc in doctor:
            docList.insert(tk.END, doc.name + " " + doc.surname)

        scrl.place(in_=docList, relx=1, rely=0, relheight=1)
        scrl.config(command=docList.yview)

        Name = tk.Label(root, text="Imie", bg="white").place(x=10, y=140)
        name = tk.Entry(root, width=25)
        name.pack()
        name.place(x=10, y=165)

        Surname = tk.Label(root, text="Nazwisko", bg="white").place(x=180, y=140)
        surname = tk.Entry(root, width=25)
        surname.pack()
        surname.place(x=180, y=165)

        Special = tk.Label(root, text="Specjalizacja", bg="white").place(x=10, y=195)
        special = tk.Entry(root, width=25)
        special.pack()
        special.place(x=10, y=220)

        def clickList(self):
            if len(docList.curselection()) > 0:
                global x
                x = docList.curselection()
                name.delete(0, len(name.get()))
                name.insert(0, doctor[x[len(x)-1]].name)
                surname.delete(0, len(surname.get()))
                surname.insert(0, doctor[x[len(x) - 1]].surname)
                special.delete(0, len(special.get()))
                special.insert(0, doctor[x[len(x) - 1]].special)

                if not x[len(x) - 1] == 0:
                    name4.delete(0, len(name4.get()))
                    name4.insert(0, doctor[x[len(x) - 1]].name)
                    surname4.delete(0, len(surname4.get()))
                    surname4.insert(0, doctor[x[len(x) - 1]].surname)

        docList.bind('<<ListboxSelect>>', clickList)

        var = tk.StringVar()
        Info = tk.Label(root, textvariable=var, bg="white", fg="red").place(x=10, y=250)
        def clickBut():
            try:
                if client.isConnect(HOST, PORT):
                    #zmiana zmiennych lekarza
                    doctor[x[len(x) - 1]].name = name.get()
                    doctor[x[len(x) - 1]].surname = surname.get()
                    doctor[x[len(x) - 1]].special = special.get()
                    docList.delete(0, docList.size())
                    for doc in doctor:
                        docList.insert(tk.END, doc.name + " " + doc.surname)
                    client.sendChangeDoctor()
                    var.set("Zapisano Zmiany")
                else:
                    var.set("Nie można połączyć z serverem")
            except NameError:
                var.set("Wybierz edytowanego użytkownika")


        Log = tk.Button(root, text="Zmień", command=clickBut).place(width=100, height=30, x=190, y=205)

        Title = tk.Label(root, text="Terminarz:", bg="white").place(x=450, y=10)
        scrl2 = tk.Scrollbar(root)
        textB = tk.Text(root, width = 50, height = 24, highlightthickness = 1, bd=0, highlightbackground = "grey", wrap="none")
        textB.pack(expand=True)
        textB.place(x=450, y = 40)

        scrl2.place(in_=textB, relx=1, rely=0, relheight=1)

        textB.configure(state='disabled')
        textB.config(cursor="arrow", yscrollcommand = scrl2.set)
        scrl2.config(command=textB.yview)

        def setTextB(text):
            textB.configure(state='normal')
            textB.delete('1.0', tk.END)
            textB.insert(tk.END, text)
            textB.configure(state='disabled')

        # s = ""
        # for i in range(100):
        #     s = s + "siema"+str(i)+"\n"
        # setTextB(s)

        def minutesString(n):
            if n<10:
                return "0" + str(n)
            else:
                return str(n)

        def getTextDoctor(id, l, day, month ,year):
            d = l[id]
            s = d.name + " " + d.surname + ": \n"
            if not d.data == data0:
                if day == -1:
                    for j in range(len(d.data)):
                        s = s + "   " + minutesString(d.data[j].day) + "." + minutesString(d.data[j].month) + "." + str(d.data[j].year) + " " + str(
                            d.data[j].godzina) + ":" + minutesString(d.data[j].minuta) + " - " + d.data[j].name + " " + d.data[
                                j].surname + "\n"
                else:
                    for j in range(len(d.data)):
                        if day == d.data[j].day and month == d.data[j].month and year ==d.data[j].year:
                            s = s + "   " + minutesString(d.data[j].day) + "." + minutesString(d.data[j].month) + "." + str(
                                d.data[j].year) + " " + str(
                                d.data[j].godzina) + ":" + minutesString(d.data[j].minuta) + " - " + d.data[j].name + " " + \
                                d.data[
                                    j].surname + "\n"
            return s

        cal = CalendarGraph.CalendarGraph(root, 10, 380)

        def setTextData(id, l):
            saveday = cal.getSaveDay()
            savemonth = cal.getSaveMonth()
            saveyear = cal.getSaveYear()
            s = ""
            if id == 0:
                for i in range(len(l)-1):
                    s = s + getTextDoctor(i+1, l, saveday, savemonth, saveyear) + "\n"
            else:
                s = getTextDoctor(id, l, saveday, savemonth, saveyear)
            setTextB(s)

        def upgradeTermByCal(event):
            global x
            cal.save(event)
            try:
                setTextData(x[len(x) - 1], doctor)
            except NameError:
                setTextData(0, doctor)

        setTextData(0, doctor)

        root.bind("<Button-1>", upgradeTermByCal)

        Login = tk.Label(root, text="Login nowego lekarza:", bg="white").place(x=890, y=10)
        login = tk.Entry(root, width=50)
        login.pack()
        login.place(x=890, y=40)

        Pas = tk.Label(root, text="Hasło:", bg="white").place(x=890, y=80)
        pas = tk.Entry(root, width=50, show="*")
        pas.pack()
        pas.place(x=890, y=110)

        Pasp = tk.Label(root, text="Powtórz Hasło:", bg="white").place(x=890, y=150)
        pasp = tk.Entry(root, width=50, show="*")
        pasp.pack()
        pasp.place(x=890, y=180)

        Name2 = tk.Label(root, text="Imie:", bg="white").place(x=890, y=220)
        name2 = tk.Entry(root, width=50)
        name2.pack()
        name2.place(x=890, y=250)

        Surname2 = tk.Label(root, text="Nazwisko:", bg="white").place(x=890, y=290)
        surname2 = tk.Entry(root, width=50)
        surname2.pack()
        surname2.place(x=890, y=320)

        Special2 = tk.Label(root, text="Specjalizacja:", bg="white").place(x=890, y=360)
        special2 = tk.Entry(root, width=50)
        special2.pack()
        special2.place(x=890, y=390)

        var2 = tk.StringVar()
        Info2 = tk.Label(root, textvariable=var2, bg="white", fg="red").place(x=890, y=420)

        def registerDoctor():
            if client.isConnect(HOST, PORT):
                if pas.get() == pasp.get():
                    if len(pas.get()) > 5:
                        client.sendRegisterDoctor(name2.get(), surname2.get(), special2.get(), msg['name'], msg['id'], login.get(), pas.get())
                        re = client.isSucces()
                        if re:
                            doctor.append(Doctor.Doctor(len(doctor), name2.get(), surname2.get(), data0, special2.get()))
                            docList.insert(tk.END, name2.get() + " " + surname2.get())
                            setTextData(0, doctor)
                            var2.set("Rejsetracja powiodła się")
                        else:
                            var2.set("Doktor istnieje już w bazie danych")
                    else:
                        var2.set("Hasło musi mieć conajmniej 6 znaków")
                else:
                    var2.set("Przepisz poprawnie hasło")
            else:
                var2.set("Nie można połączyć z serverem")

        Reg = tk.Button(root, text="Zarejestruj", command=registerDoctor).place(width=100, height=30, x=890, y=450)

        changeData = tk.Label(root, text="Zmień date wizyty", bg="white").place(x=450, y=450)
        changeData = tk.Label(root, text="Podaj starą date i godzine wizyty oraz dane pacjenta", bg="white").place(x=450, y=470)

        dayVar = tk.IntVar()
        daySpin = tk.Spinbox(root, from_=1, to=31, textvariable=dayVar, width = 6)
        daySpin.pack()
        daySpin.place(x = 450, y = 500)

        monthVar = tk.IntVar()
        monthSpin = tk.Spinbox(root, from_=1, to=12, textvariable=monthVar, width=6)
        monthSpin.pack()
        monthSpin.place(x = 510, y = 500)

        yearVar = tk.IntVar()
        yearSpin = tk.Spinbox(root, from_=datetime.datetime.now().year, to=datetime.datetime.now().year+1000, textvariable=yearVar, width=6)
        yearSpin.pack()
        yearSpin.place(x = 570, y = 500)

        hourVar = tk.IntVar()
        hourSpin = tk.Spinbox(root, from_=1, to=24, textvariable=hourVar, width=6)
        hourSpin.pack()
        hourSpin.place(x=650, y=500)

        minuteVar = tk.IntVar()
        minuteSpin = tk.Spinbox(root, from_=0, to=60, textvariable=minuteVar, width=6)
        minuteSpin.pack()
        minuteSpin.place(x=710, y=500)

        Name3 = tk.Label(root, text="Imie:", bg="white").place(x=450, y=520)
        name3 = tk.Entry(root, width=20)
        name3.pack()
        name3.place(x=450, y=540)

        Surname3 = tk.Label(root, text="Nazwisko:", bg="white").place(x=580, y=520)
        surname3 = tk.Entry(root, width=20)
        surname3.pack()
        surname3.place(x=580, y=540)

        changeData = tk.Label(root, text="Podaj nową date i godzine wizyty oraz dane lekarza", bg="white").place(x=450, y=570)

        dayVarNew = tk.IntVar()
        daySpinNew = tk.Spinbox(root, from_=1, to=31, textvariable=dayVarNew, width = 6)
        daySpinNew.pack()
        daySpinNew.place(x = 450, y = 600)

        monthVarNew = tk.IntVar()
        monthSpinNew = tk.Spinbox(root, from_=1, to=12, textvariable=monthVarNew, width=6)
        monthSpinNew.pack()
        monthSpinNew.place(x = 510, y = 600)

        yearVarNew = tk.IntVar()
        yearSpinNew = tk.Spinbox(root, from_=datetime.datetime.now().year, to=datetime.datetime.now().year+1000, textvariable=yearVarNew, width=6)
        yearSpinNew.pack()
        yearSpinNew.place(x = 570, y = 600)

        hourVarNew = tk.IntVar()
        hourSpinNew = tk.Spinbox(root, from_=1, to=24, textvariable=hourVarNew, width=6)
        hourSpinNew.pack()
        hourSpinNew.place(x=650, y=600)

        minuteVarNew = tk.IntVar()
        minuteSpinNew = tk.Spinbox(root, from_=0, to=60, textvariable=minuteVarNew, width=6)
        minuteSpinNew.pack()
        minuteSpinNew.place(x=710, y=600)

        Name4 = tk.Label(root, text="Imie:", bg="white").place(x=450, y=620)
        name4 = tk.Entry(root, width=20)
        name4.pack()
        name4.place(x=450, y=640)

        Surname4 = tk.Label(root, text="Nazwisko:", bg="white").place(x=580, y=620)
        surname4 = tk.Entry(root, width=20)
        surname4.pack()
        surname4.place(x=580, y=640)

        def lookForDoctor(lookName, lookSurname):
            for i in range(len(doctor)):
                if doctor[i].name == lookName and doctor[i].surname == lookSurname:
                    return i
            return -1
        def lookForDoctorByName(lookName, lookSurname):
            for i in range(len(doctor)):
                for j in range(len(doctor[i].data)):
                    if doctor[i].data[j].name == lookName and doctor[i].data[j].surname == lookSurname:
                        if doctor[i].data[j].day == dayVar.get() and doctor[i].data[j].month == monthVar.get() and doctor[i].data[j].year == yearVar.get():
                            if doctor[i].data[j].minuta == minuteVar.get() and doctor[i].data[j].godzina == hourVar.get():
                                return i
            return -1

        var3 = tk.StringVar()
        Info3 = tk.Label(root, textvariable=var3, bg="white", fg="red").place(x=450, y=680)

        def changeD():
            if client.isConnect(HOST, PORT):
                if len(name3.get()) > 0 and len(name4.get()) > 0 and len(surname3.get()) > 0 and len(surname4.get()) > 0:
                    if True:
                        indexDoc1 = lookForDoctorByName(name3.get(), surname3.get())
                        go = False
                        if not indexDoc1 == -1:
                            go = True
                        indexDoc2 = lookForDoctor(name4.get(), surname4.get())
                        if (not lookForDoctor(name4.get(), surname4.get()) == -1) and go:
                            doctor[lookForDoctorByName(name3.get(), surname3.get())].removeData(dayVar.get(), monthVar.get(),yearVar.get(),hourVar.get(),minuteVar.get())
                            doctor[indexDoc2].data.append(Data.Data(dayVarNew.get(), monthVarNew.get(), yearVarNew.get(), name3.get(), surname3.get(), hourVarNew.get(), minuteVarNew.get()))
                            setTextData(0, doctor)
                            var3.set("Udało się zmienić")
                        else:
                            if go:
                                var3.set("Nie znaleziono lekarza")
                            else:
                                var3.set("Nie znaleziono terminu")
                else:
                    var3.set("Uzupełnij wszystkie pola formularza")
            else:
                var3.set("Nie można połączyć z serverem")

        Reg = tk.Button(root, text="Zmień", command=changeD).place(width=100, height=30, x=450, y=710)

        root.mainloop()

    def addDoctor(self, d):
        self.doctor[len(self.doctor)] = d