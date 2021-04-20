from tkinter import *
import tkinter as tk
import calendar
import threading
import time
import datetime
import sys

class CalendarGraph:
    def __init__(self, root1, X, Y):
        global PLACEX, PLACEY, MONTH, canv, root, month, year, var, date, rect1, saveMonth, saveYear, saveDay, rect2, work
        PLACEX = X
        PLACEY = Y
        MONTH = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień","październik", "listopad", "grudzień"]
        WEEK = ["pon.", "wt.", "śr.", "czw.", "pt.", "sob.", "nie."]
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        root = root1
        var = []
        saveMonth = -1
        saveYear = -1
        saveDay = -1
        work = True

        for i in range(42):
            var.append(tk.StringVar())

        for i in range(7):
            Week = tk.Label(root, text=WEEK[i], bg ="white").place(x=PLACEX+30+i*60, y=PLACEY-12, anchor = 'center')

        date = tk.StringVar()
        Date = tk.Label(root, textvariable=date, bg="white", fg="black").place(x=PLACEX, y=PLACEY-50)
        date.set(MONTH[month-1] + ", " + str(year))

        canv = Canvas(root, bg="white", height=302, width=422, highlightbackground="gray", highlightthickness=0, bd = 0)
        for i in range(7):
            for j in range(6):
                rect = canv.create_rectangle(i*60+1,j*50+1,i*60+61,j*50+51, outline="gray")
                Day = tk.Label(root, textvariable=var[j*7+i], bg="white", fg="gray").place(x=PLACEX+2+i*60, y=PLACEY+2+j*50)
        canv.place(x = PLACEX, y = PLACEY)

        rect1 = canv.create_rectangle(-60, -50, 0, 0, outline="red", width = 2)
        rect2 = canv.create_rectangle(-60, -50, 0, 0, outline="black", width = 2)

        self.upgradeCal()

        def plus():
            global month, year, date
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1
            self.upgradeCal()
            date.set(MONTH[month - 1] + ", " + str(year))

        def minus():
            global month, year, date
            if month > 1:
                month -= 1
            else:
                month = 12
                year -= 1
            self.upgradeCal()
            date.set(MONTH[month - 1] + ", " + str(year))

        plus = tk.Button(root, text="->", command=plus).place(width=50, height=30, x=PLACEX+230, y=PLACEY+330)
        minus = tk.Button(root, text="<-", command=minus).place(width=50, height=30, x=PLACEX+140, y=PLACEY+330)

        upg = threading.Thread(target=self.__upgrade__, daemon=True)
        upg.start()

    def __upgrade__(self):
        global work
        rect = canv.create_rectangle(-60, -50, 0, 0, outline="blue")
        while work:
            # print("x: " + str(root.winfo_x()) + " y: " + str(root.winfo_y()))
            dele = True
            for i in range(7):
                for j in range(6):
                        if root.winfo_pointerx()-root.winfo_x()-10 > i*60+PLACEX and root.winfo_pointerx()-root.winfo_x()-10 < (i+1)*60+PLACEX and root.winfo_pointery()-30-root.winfo_y() > j * 50 + PLACEY and root.winfo_pointery()-30-root.winfo_y() < (j + 1) * 50 + PLACEY: #sprawdzam y
                            canv.coords(rect, i * 60+1, j * 50+1, i * 60 + 61, j * 50 + 51)
                            dele = False
            if dele:
                canv.coords(rect, -60, -50, 0, 0)
            time.sleep(0.001)

    def save(self, event):
        global saveDay, saveMonth, saveYear, month, year, PLACEX, PLACEY, root
        for i in range(7):
            for j in range(6):
                if root.winfo_pointerx() - root.winfo_x() - 10 > i * 60 + PLACEX and root.winfo_pointerx() - root.winfo_x() - 10 < (
                        i + 1) * 60 + PLACEX and root.winfo_pointery() - 30 - root.winfo_y() > j * 50 + PLACEY and root.winfo_pointery() - 30 - root.winfo_y() < (
                        j + 1) * 50 + PLACEY:
                    if saveMonth == month and saveYear == year and saveDay == int(
                            var[j * 7 + i].get().replace(" ", "")):
                        saveMonth = -1
                        saveYear = -1
                        saveDay = -1
                        self.upgradeCal()
                    else:
                        if var[j * 7 + i].get() != "":
                            saveMonth = month
                            saveYear = year
                            saveDay = int(var[j * 7 + i].get().replace(" ", ""))
                            self.upgradeCal()

    def upgradeCal(self):
        global var, year, month, var, canv, rect1, rect2

        def getDate():
            if (month < 12):
                return datetime.date(year, month + 1, 1)
            else:
                return datetime.date(year + 1, 1, 1)

        for i in range(42):
            var[i].set("")
        for i in range((getDate() - datetime.date(year, month, 1)).days):
            var[i + calendar.weekday(year, month, 1)].set(" " + str(i + 1))

        if datetime.datetime.now().month == month and datetime.datetime.now().year == year:  # zaznaczanie dzisiejszej daty
            for i in range(42):
                if var[i].get() == " " + str(datetime.datetime.now().day):
                    canv.coords(rect1, (i % 7) * 60 + 1, ((i - (i % 7)) / 7) * 50 + 1, (i % 7) * 60 + 61,
                                ((i - (i % 7)) / 7) * 50 + 51)
        else:
            canv.coords(rect1, -60, -50, 0, 0)

        if saveMonth == month and saveYear == year:
            for i in range(42):
                if var[i].get() == " " + str(saveDay):
                    canv.coords(rect2, (i % 7) * 60 + 1, ((i - (i % 7)) / 7) * 50 + 1, (i % 7) * 60 + 61,
                                ((i - (i % 7)) / 7) * 50 + 51)
        else:
            canv.coords(rect2, -60, -50, 0, 0)

    def closeThread(self):
        global work
        work = False

    def getSaveDay(self):
        global saveDay
        return saveDay

    def getSaveMonth(self):
        global saveMonth
        return saveMonth

    def getSaveYear(self):
        global saveYear
        return saveYear

