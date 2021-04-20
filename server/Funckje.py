# -*- coding: utf-8 -*-
import pymysql
import json
import ast


# -*- coding: utf-8 -*-
def nowa_recepcja(a):
    # /crec;nazwa;ulica;miasto;telefon;login;haslo
    try:
        connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
        mysql = connection_sql.cursor()
        sql = "INSERT INTO recepcja (nazwa, ulica, miasto, telefon, login, haslo,email,nrlokalu) VALUES (%s, %s, %s, " \
              "%s, %s, %s,%s,%s) "
        record = (
        a["nazwa"], a["ulica"], a["city"], a["telefon"], a["login"], a["password"], a["email"], a['nrlokalu'])

        mysql.execute(sql, record)
        connection_sql.commit()
        return '{"type":"createreception","stan":"sukces"}'
    except:
        return False

#{"type":"registeruser","login":"patromi","password":"123","imie":"patr","nazwisko":"qwe","leki":"brak"}
def nowy_uzytkownik(a):
    # /cruse;login;haslo;imie;nazwisko;leki
    try:
        print(a)
        connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
        mysql = connection_sql.cursor()
        sql = "INSERT INTO users (login, haslo, imie, nazwisko,leki,email) VALUES (%s, %s, %s, %s, %s,%s)"
        record = (a['login'], a['password'], a['imie'], a['nazwisko'],"brak",a['email'])
        mysql.execute(sql, record)
        connection_sql.commit()
        return '{"type":"creatuser","stan":"sukces"}\n'
    except:
        return '{"type":"createuser","error":"344"}\n'



def logowanie_uzytkownik(a):
    # /loguser;login;haslo
    try:
        connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
        mycursor = connection_sql.cursor()
        query = """SELECT * FROM users WHERE login=%s AND haslo=%s"""
        mycursor.execute(query, (str(a["login"]), str(a["password"])))
        myresult = mycursor.fetchall()
        if myresult == ():
            return True
        myresult = myresult[0]
        koniec = ''
        x = {
            "type": "loginpatient",
            "login": myresult[1],
            "firstname": myresult[3],
            "lastname": myresult[4],
            "medicines": myresult[5],
            "id": myresult[0]
        }

        y = json.dumps(x)
        return y
    except:
        return False

def logowanie_recepcji(a):
    # /lrep;login;haslo;
        try:
            connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
            mycursor = connection_sql.cursor()
            query = """SELECT * FROM recepcja WHERE login=%s AND haslo=%s"""
            mycursor.execute(query, (a['login'], a['password']))
            myresult = mycursor.fetchall()
            koniec = ''
            myresult = myresult[0]
            x = myresult[1]
            print(x)
            koniec = ''
            x = {
                "type": "loginreception",
                'id': myresult[0],
                "login": myresult[1],
                "name": myresult[3],
                "street": myresult[4],
                "city": myresult[5],
                "phone": myresult[6],
                "email": myresult[7],
                "nrlocal": myresult[8]
            }
            y = json.dumps(x)
            return y
        except:
                return False


def rejestracja_lekarza(a):
    # /nlekarz;imie;nazwisko;specjalizacja;klinika;IDkliniki
        try:
            connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
            mysql = connection_sql.cursor()
            mycursor = connection_sql.cursor()
            sql = "INSERT INTO lekarz (imie, nazwisko, specjalizacja, klinika, idkliniki,login,haslo) VALUES (%s, %s, %s, %s, " \
                  "%s, %s, %s) "
            record = (a["imie"], a["nazwisko"], a["specjalizacja"], a["klinika"], a["idkliniki"], a["login"], a["haslo"])
            mysql.execute(sql, record)
            connection_sql.commit()
        except:
            return False


def lista_lekarzy(a):
    # funkcja wypisuje lekarzy w danej klinicy
    # /llek;IDKliniki
    # output:  /listek;idlekarza;imie;nazwisko;specjalizacja;nazwakliniki;idkliniki
    try:
        print(a['id']+'w')
        connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
        mycursor = connection_sql.cursor()
        query = """SELECT * FROM lekarz WHERE id=%s"""
        mycursor.execute(query, a["id"])
        result = mycursor.fetchall()
        lr = len(result)
        list = []
        koniec = ''
        for i in range(lr):
            x = {
                "type": "listlek",
                "firstname": result[i][1],
                "lastname": result[i][2],
                "specjalizacja": result[i][3],
                "clinic": result[i][4],
                "id": result[i][0],
                "idkliniki": result[i][5]
            }
            y = json.dumps(x)
            list.append(y)
        return list

    except:
        return False

def id_lek(a):
    # funkcja wypisuje lekarzy w danej klinicy
    # /llek;IDKliniki
    # output:  /listek;idlekarza;imie;nazwisko;specjalizacja;nazwakliniki;idkliniki
    try:
        connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
        mycursor = connection_sql.cursor()
        query = """SELECT * FROM lekarz WHERE idkliniki=%s"""
        mycursor.execute(query, a["id"])
        result = mycursor.fetchall()
        lr = len(result)
        list = []
        koniec = ''
        for i in range(lr):
            x = {
                "type": "listlek",
                "firstname": result[i][1],
                "lastname": result[i][2],
                "specjalizacja": result[i][3],
                "clinic": result[i][4],
                "id": result[i][0],
                "idkliniki": result[i][5]
            }
            y = json.dumps(x)
            list.append(y)
        return list

    except:
        return '{"type":"listarzt","error":"344"}\n'


def wyszukaj_lekrza(a):
    ###/w;
    connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
    mycursor = connection_sql.cursor()
    query = """SELECT * FROM lekarz WHERE imie=%s or nazwisko=%s or specjalizacja=%s or klinika=%s"""
    record = (a["szukaj"], a["szukaj"], a["szukaj"], a["szukaj"])
    mycursor.execute(query, record)
    result = mycursor.fetchall()
    lr = len(result)
    koniec = ''
    list = []
    list2=[]
    for i in range(lr):
        x = {
            "ID": result[i][0],
        }
        list2.append(x)
    y = {
        "type": "getdoctor",
        "squery": a["szukaj"],
        "ID": list2}
    list.append(y)
    return list


def rozpoczecie_spotkania(a):
    # /startspotkania;iduzytkownika;idlekarza
    try:
        command = '/startspotkania;' + a[1] + ';' + a[2]
        print(command)
        return command
    except:
        return 'error;344'


def logowanie_lekarza(a):
    try:
        connection_sql = pymysql.connect(host='35.189.109.28', user='root', passwd='dnURTEpZQNA3t5k', db='teleporada')
        mycursor = connection_sql.cursor()
        query = """SELECT * FROM lekarz WHERE login=%s AND haslo=%s"""
        mycursor.execute(query, (str(a["login"]), str(a["haslo"])))
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        koniec = ''
        x = {
            "firstname": myresult[1],
            "lastname": myresult[2],
            "specialization": myresult[3],
            "clinic": myresult[4],
            "idclinic": myresult[5],
            "idarzt": myresult[0]

        }

        y = json.dumps(x)
        return y, x["idarzt"]
    except:
        return '{"type":"logarzt":"error":"344"}\n'


def sprawdzenie_opoznienia(a):
    ###########nie dziala do przemyslenia!#############
    pass


def sprawdzenie_spotkania(a):
    ###########nie dziala do przemyslenia!#############
    pass


def koniec_spotkania(a):
    ###########nie dziala do przemyslenia!#############
    pass
