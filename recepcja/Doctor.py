
class Doctor:
    def __init__(self, id, name, surname, data1, special):
        self.id = id
        self.name = name
        self.surname = surname
        self.data = []
        self.special = special

    # def addData(self, d):
    #     self.data[len(self.data)] = d
    #
    # def getData(self, index):
    #     return self.data[index]
    #
    def removeData(self, day, month, year, minuta, godzina):
        newData = []
        for i in range(len(self.data)):
            if not day == self.data[i].day and month == self.data[i].month and year == self.data[i].year and minuta == self.data[i].minuta and godzina == self.data[i].godzina:
                newData.append(self.data[i])
        self.data = newData