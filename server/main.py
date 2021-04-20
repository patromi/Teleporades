# -*- coding: utf-8 -*-
import socket, threading
import Funckje
import ast
import datetime
list = []
list_users = []
list_rec = []
list_lek = []
list_op = []

###error;515 - błędne hasło lub login
###error;755 - Brak dostępu - Brak zalogowania
##error;500 - Próba utworzenia recpcji bedąc jednoczęśnie zalogowanym na użytkownika lub recepcje
##error;344 - Błąd w skłani polecenia
##error;977 - Nie można wylogować jeżeli nie jesteś zalogowany
##error;653 - jesteś już zalogowany
##error;431; - Nie można zajerestrować lekarza ponieważ nie jesteś zalogowany na recepcje!
##error;404; - Brak lekarzy w id kliniki
##error;436 - Nie można wywołać polecenia jako użytkownik albo nie zalogowany!
##error;349 - Błędne id nie - znaleziono recepcji
##error:432 - Nie można zologwać na lekarza kiedy jesteś już zalogowany
###Potwierdzenie emailu!
class Klient(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        list.append(clientsocket)
        IP = clientAddress
        self.IP = IP
        self.recID = None
        print("Nowe polaczenie od", clientAddress)

    def run(self):
        print("Polaczono z: ", clientAddress)
        msg = ''
        #################
        # Sekcja  klienta#
        #################
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode('UTF-8')
            print(msg)
            try:
                msg = ast.literal_eval(msg)
            except:
                continue
                #wiad = '{"type":"unlogged","error":"344"}'
                #self.csocket.send(bytes((wiad + '\n').encode('UTF-8')))
            if msg == '':
                continue
            if msg['type'] == 'loginreception':
                #logowanie recepcji
                if self.IP in list_op:
                    #bład kiedy użytkownik jest już zalogowany#
                    wiad = '{"type":"loginreception","error":"653"}'
                    self.csocket.send(bytes((wiad + '\n').encode('UTF-8')))
                else:
                    #Wykorzystanie funkcji
                    x = Funckje.logowanie_recepcji(msg)
                    try:
                        #Zmienienie naszej wiadomości w słownik
                        x = ast.literal_eval(x)
                    except:
                        pass
                    print(x)
                    if x == False :
                        #Kiedy nasza funkcja zwróci złą składnie
                        wiad = '{"type":"loginreception","error":"344"}'
                        self.csocket.send(bytes((wiad + '\n').encode('UTF-8')))
                    else:
                        #wpisujemy naszegą recepcje do listy, aby móc go identyfikować po ID z bazy danych, oraz wysyłamy wiadomość
                        list_op.append(self.IP)
                        self.recID = x["id"]
                        list = [self.IP[0],self.IP[1],str(self.recID)]
                        self.recID = tuple(list)
                        list_rec.append(self.recID)
                        print(list_rec)
                        x = str(x)
                        self.csocket.send(bytes((x + '\n').encode('UTF-8')))
            elif msg['type'] == 'loginpatient':
                #logowanie uzytkownika
                #Wykorzystanie funkcji
                x = Funckje.logowanie_uzytkownik(msg)
                try:
                    # Zmienienie naszej wiadomości w słownik
                    x = ast.literal_eval(x)
                except:
                    pass
                if self.IP in list_rec or self.IP in list_op:
                    # bład kiedy użytkownik jest już zalogowany#
                    wiad = '{"type":"loginpatient","error":"653"}'
                    self.csocket.send(bytes((wiad + '\n').encode('UTF-8')))
                else:
                    if x == True :
                        # Kiedy nasza funkcja zwróci brak wyników
                        wiad = '{"type":"loginpatient","error":"515"}'
                        self.csocket.send(bytes((wiad + '\n').encode('UTF-8')))
                    elif x == False :
                        # Kiedy nasza funkcja zwróci złą składnie
                        wiad = '{"type":"loginpatient","error":"344"}'
                        self.csocket.send(bytes((wiad + '\n').encode('UTF-8')))
                    else:
                        # wpisujemy naszego użytkownika do listy, aby móc go identyfikować po ID z bazy danych, oraz wysyłamy wiadomość
                        list_op.append(self.IP)
                        self.userID = x["id"]
                        list = [self.IP[0], self.IP[1], str(self.userID)]
                        self.userID = tuple(list)
                        list_users.append(self.userID)
                        x = str(x)
                        self.csocket.send(bytes((x + '\n').encode('UTF-8')))
            elif msg['type'] == 'registeruser':
            #utworzenie nowego uzytkownika
                if self.IP in list_op:
                    #bład kiedy użytkownik jest już zalogowany#
                    wiad = '{"type":"registeruser","error":"500"}'
                    self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                else:
                    #Wykorzystanie funkcji
                    x = Funckje.nowy_uzytkownik(msg)
                    self.csocket.send(bytes((x + '\n').encode('UTF-8')))
            elif msg['type'] == 'registerreception':
                ###utworzenie nowej recepcji
                if self.IP in list_op:
                    #bład kiedy użytkownik jest już zalogowany#
                    wiad = '{"type":"registerreception","error":"500"}'
                    self.csocket.send(bytes((wiad + '\n').encode('utf8')))
                else:
                    #Wykorzystanie funkcji
                    x = Funckje.nowa_recepcja(msg)
                    if x == False:
                    #sprawdzenie czy została podana odpowiednia składnia polecenia
                        wiad = '{"type":"createreception","stan":"344"}'
                        self.csocket.send(bytes((x + '\n').encode('utf-8')))
                    else:
                        self.csocket.send(bytes((x + '\n').encode('utf-8')))
            elif msg['type'] == 'registerdoctor':
                ###utworzenie nowego lekarza
                try:
                    if self.recID in list_rec:
                        x = Funckje.rejestracja_lekarza(msg)

                        if x == False:
                            wiad = '{"type":"registerdoctor","error":"344"}'
                            self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                        else:
                            wiad = '{"type":"registerdoctor","error":"sukces"}'
                            self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                    else:
                        wiad = '{"type":"registerdoctor","error":"431"}'
                        self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                except:
                    wiad = '{"type":"registerdoctor","error":"344"}'
                    self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
            elif msg['type'] == 'listlek':
                    #wyszukujemy listę lekarzy po ID#
                    try:
                        if self.IP in list_op :
                            #wykonujemy funckje#
                            x = Funckje.lista_lekarzy(msg)
                            if x == '':
                                #sprawdzamy czy list jest pusta
                                wiad = '{"type":"listlek","error":"404"}'
                                self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                            elif x == False:
                                wiad = '{"type":"listlek","error":"344"}'
                                self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                            else:
                                for i in x:
                                    #wysyłamy pokolei liste du użytkownika#
                                    print(i)
                                    print((i + '\n').encode('utf-8'))
                                    self.csocket.send(bytes((i + '\n').encode('utf-8')))
                        else:
                            wiad = '{"type":"listlek","error":"436"}'
                            self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                    except:
                        wiad = '{"type":"listlek","error":"436"}'
                        self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
            elif msg["type"] == 'idlek':
                try:
                    if self.IP in list_op:
                        # wykonujemy funckje#
                        x = Funckje.id_lek(msg)
                        if x == '':
                            # sprawdzamy czy list jest pusta
                            wiad = '{"type":"idlek","error":"404"}'
                            self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                        else:
                            for i in x:
                                # wysyłamy pokolei liste du użytkownika#
                                self.csocket.send(bytes((i + '\n').encode('utf-8')))
                    else:
                        wiad = '{"type":"idlek","error":"436"}'
                        self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                except:
                    wiad = '{"type":"idlek","error":"436"}'
                    self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
            elif msg['type'] == 'loginlek':
                ##logowanie lekarza##
                    try:
                        if self.IP in list_op:
                            wiad = '{"type":"loginlek","status":"error:432"}'
                            self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                        else:
                            #wykonanie funkcji
                            x = Funckje.logowanie_lekarza(msg)
                            self.lekID = x[1]
                            x = x[0]
                            self.csocket.send(bytes((x + '\n').encode('utf-8')))
                            list_op.append(self.IP)
                            #dodanie lekarza do listy z id
                            list = [self.IP[0], self.IP[1], str(self.lekID)]
                            self.lekID = tuple(list)
                    except:
                        wiad = '{"type":"listlek","error":"436"}'
                        self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                        list_lek.append(self.lekID)

            elif msg['type'] == 'getdoctor':
                ##wyszukaj lekarzy po słowie kluczowym##
                try:
                    if self.recID in list_rec or self.userID in list_users:
                        #wykonujemy funkcje
                        x = Funckje.wyszukaj_lekrza(msg)
                        for i in x:
                            i = str(i)
                            self.csocket.send(bytes((i + '\n').encode('utf-8')))
                    else:
                        wiad = '{"type":"getdoctor","error":"755"}'
                        self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                except:
                    wiad = '{"type":"getdoctor","error":"436"}'
                    self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
                    list_lek.append(self.lekID)
            elif msg['type'] == 'logoutuser':
                ##wylogownie sie jako uzytkownik
                try:
                    #usuniecie z listy
                    list_op.remove(self.IP)
                    list_users.remove(self.userID)
                    wiad = 'Wylogowano pomyslnie\n'
                    self.csocket.send(bytes(wiad.encode('utf-8')))
                except:
                    #bład użytkownik nie jest zalogowany!#
                    wiad = 'error;997\n'
                    self.csocket.send(bytes(wiad.encode('utf-8')))
            elif msg['type'] == 'logoutrec':
                #wylogowanie receepcji
                try:
                    list_op.remove(self.IP)
                    list_rec.remove(self.recID)
                    wiad = '{"type":"logoutrec","error":"sukces"}\n'
                    self.csocket.send(bytes(wiad.encode('utf-8')))
                except:
                    # bład recepcja nie jest zalogowana!#
                    wiad = '{"type":"logoutrec","error":"997"}\n'
                    self.csocket.send(bytes(wiad.encode('utf-8')))
            elif msg['type'] == 'logoutartz':
                #wylogowanie lekarza
                try:
                    list_op.remove(self.IP)
                    list_lek.remove(self.lekID)
                    wiad = '{"type":"logoutartz","error":"sukces"}\n'
                    self.csocket.send(bytes(wiad.encode('utf-8')))
                except:
                    wiad = '{"type":"logoutartz","error":"997"}\n'
                    self.csocket.send(bytes(wiad.encode('utf-8')))
            elif msg['type'] == 'test':
                #funkcja testowa
                if self.IP in list_rec:
                    self.csocket.send(bytes(('recepcja' + '\n').encode('utf-8')))
                elif self.IP in list_users:
                    self.csocket.send(bytes(('user' + '\n').encode('utf-8')))
                else:
                    self.csocket.send(bytes(('error;755' + '\n').encode('utf-8')))
            elif msg['type'] == 'ping':
                print(msg["time"])
                wiad = '{"type":"pong","time":' + str(msg['time']) + '}'
                print(wiad)
                self.csocket.send(bytes((wiad + '\n').encode('utf-8')))
        list.remove(self.csocket)

class Watek(threading.Thread):
    def run(self):
        ##################
        ##Sekcja Serwera##
        ##################
        # Komendy serwerowe
        while True:
            wiad = raw_input()
            if wiad == 'listlek':
                print(list_lek)
            elif wiad == 'listop':
                print(list_op)
            elif wiad == 'listrec':
                print(list_rec)
            elif wiad == 'listusers':
                print(list_users)


################
# config Serwera#
################
LOCALHOST = ''
PORT = 20001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Serwer staruje")
print("Czekanie na klienta")
Watek().start()

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = Klient(clientAddress, clientsock)
    newthread.start()
