import socket
import ast

class Client:
    def __init__(self, HOST, PORT, LOGINRECEPTION1, REGISTERRECEPTION1, REGISTERDOCTOR1, GETDOCTORS1):
        global s, message
        global LOGINRECEPTION, REGISTERRECEPTION, REGISTERDOCTOR, GETDOCTORS
        LOGINRECEPTION = LOGINRECEPTION1
        REGISTERRECEPTION = REGISTERRECEPTION1
        REGISTERDOCTOR = REGISTERDOCTOR1
        GETDOCTORS = GETDOCTORS1
        message = "null"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tryCon(HOST, PORT)

    def tryCon(self, HOST, PORT):
        global isCon
        try:
            s.connect((HOST, PORT))
            isCon = True
        except ConnectionRefusedError:
            isCon = False

    def getMsg(self):
        msg = s.recv(2048)
        return msg.decode()

    def send(self, text):
        s.send(text.encode('UTF-8'))

    def close(self):
        s.close()

    def getCon(self):
        return isCon

    def isConnect(self, HOST, PORT):
        try:
            post = str({u'type': u'ping2'})
            s.send(bytes((post).encode('UTF-8')))
            return True
        except ConnectionResetError:
            self.close()
            self.__init__(HOST, PORT)
            return isCon
        except OSError:
            self.close()
            self.__init__(HOST, PORT, LOGINRECEPTION, REGISTERRECEPTION, REGISTERDOCTOR, GETDOCTORS)
            return isCon

    def sendRegisterReception(self, login, password, email, city, street, localnr, phonenumber, name):
        post = str({'type': str(REGISTERRECEPTION), 'login': str(login), 'password': str(password), 'email':str(email),'miasto':str(city),'ulica':str(street),'nrlokalu':str(localnr),'telefon':str(phonenumber),'nazwa':str(name)})
        s.send(bytes((post).encode('UTF-8')))

    def sendLoginReception(self, login, password):
        post = str({'type':str(LOGINRECEPTION),'login':str(login),'password':str(password)})
        s.send(bytes((post).encode('UTF-8')))

    def sendRegisterDoctor(self, name, surname, special, clinic, id, login, password):
        post = str({'type':str(REGISTERDOCTOR),'login':str(login),'haslo':str(password),'imie':str(name),'nazwisko':str(surname),'klinika':str(clinic),'idkliniki':str(id),'specjalizacja':str(special)})
        s.send(bytes((post).encode('UTF-8')))

    def sendChangeData(self):
        pass

    def sendChangeDoctor(self, idclic, iddoc, name, surname):
        pass

    def getData(self):
        pass

    def getDoctors(self, id):
        post = str({'type':str(GETDOCTORS),'id':str(id)})
        s.send(bytes((post).encode('UTF-8')))
        list = []
        quantity = 10 #liczba lekarzy odbieranych
        for i in range(2):
            try:
                data = s.recv(2048)
                print(data)
                msg = data.decode('UTF-8')
                msg = ast.literal_eval(msg)
                list.append(msg)
            except SyntaxError:
                pass
        return list

    def isSucces(self):
        global message
        data = s.recv(2048)
        print(data)
        msg = data.decode('UTF-8')
        msg = ast.literal_eval(msg)
        try:
            if msg["error"] == "653":
                return False
            if msg["error"] == "sukces":
                return True
        except KeyError:
            message = msg
            return True

    def getMessageRec(self):
        return message

    #Z BIBLIOTEKA JSON
    def sendTest(self):
        print("test")
        post = '{"type":"loginreception","login":"admin","password":"root"}'
        s.send(bytes((post).encode('UTF-8')))

    # def sendRegisterReception(self, login, password, email, city, street, localnr, phonenumber):
    #     data = {
    #         "type": REGISTERRECEPTION,
    #         "login": login,
    #         "password": password,
    #         "email": email,
    #         "city": city,
    #         "strit": street,
    #         "localnr": localnr,
    #         "phone": phonenumber
    #     }
    #
    #     jsonData = json.dumps(data, sort_keys=False)
    #     s.sendall(jsonData.encode())

    # def sendLoginReception(self, login, password):
    #     # data = {
    #     #     "type": "loginpatient",
    #     #     "login": login,
    #     #     "password": password
    #     # }
    #     data={
    #         "type": "loginreception","login":"admin","password":"root"
    #     }
    #
    #     jsonData = json.dumps(data, sort_keys=False)
    #     s.sendall(jsonData.encode())

    # def isSucces(self, type):
    #     print("slucham")
    #     data = s.recv(2048)
    #     print(data)
    #     msg = json.loads(data)
    #     print(msg.decode)
    #     if(msg['type'] == type):
    #         return msg['error']
    #     else:
    #         return 0