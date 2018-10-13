import secrets
import sqlite3


def conection():
    try:
        conn = sqlite3.connect("mydatabase.db")
        return conn
    except Error as e:
        print(e)

    return None

def getToken(data):
    if len(data) != 2: return "Dados invalidos"
    conn = conection()
    if conn == None:
        return 'Fail in to acsses DB'
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE Email  LIKE ? and Senha LIKE  ?", (data[0], data[1]))

    consult = cursor.fetchall()
    if len(consult) != 1:
        return "Dados Invalidos"
    consult = consult[0]
    token = secrets.token_urlsafe(64)
    cursor.execute("UPDATE Usuarios SET Token = ? WHERE id = ?", (token, consult[0]))
    conn.commit()
    conn.close()
    return token


def getEmails(token):
    conn = conection()
    if conn == None:
        return 'Fail in to acsses DB'
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Token  LIKE ? AND Token LIKE ?", (token, token))
    user = cursor.fetchall()
    if len(user) != 1: return "Token Invalido"
    user = user[0]
    cursor.execute("SELECT * FROM Emails WHERE Para  LIKE ? AND Para LIKE ?", (user[2], user[2]))
    result = cursor.fetchall()
    mensage = ""
    if len(result) == 0:
        return "Empty"
    for i in result:
        mensage += str(i[0]) +"\n" + str(i[4]) + "\n" + str(i[1]) + "\n"
    conn.close()
    return mensage

def getEmail(data):
    if len(data) != 2: return "Dados invalidos"
    conn = conection()
    if conn == None:
        return 'Fail in to acsses DB'
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Token  LIKE ? AND Token LIKE ?", (data[0], data[0]))
    user = cursor.fetchall()
    if len(user) != 1: return "Token Invalido"
    user = user[0]
    cursor.execute("SELECT * FROM Emails WHERE Para  LIKE ? AND id LIKE ?", (user[2], data[1]))
    result = cursor.fetchall()
    if len(result) != 1: return "Dados invalidos"
    result = result[0]
    conn.close()
    return str(result[3])

def addUser(data):
    if len(data) != 3: return "Dados invalidos"
    conn = conection()
    if conn == None:
        return "Fail in acsses DB"
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Email  LIKE ? AND Email LIKE ?", (data[1], data[1]))
    if len(cursor.fetchall()) != 0: return "user alread exist"
    cursor.execute("INSERT INTO Usuarios VALUES (?, ?, ?,?,?);", (None,data[0],data[1],data[2], None))
    conn.commit()
    conn.close()
    return "Success"

def SendEmail(data):
    if len(data) != 4: return "Dados Invalidos"
    conn = conection()
    if conn == None:
        return "Fail in acsses DB"
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Token  LIKE ? AND Token LIKE ?", (data[0], data[0]))
    user = cursor.fetchall()
    if len(user) != 1: return "Token Invalido"
    cursor.execute("SELECT * FROM Usuarios WHERE Email  LIKE ? AND Email LIKE ?", (data[3], data[3]))
    if len(cursor.fetchall()) != 1: return  "Usuario Invalido"
    cursor.execute("INSERT INTO Emails VALUES (?, ?, ?,?, ?);", (None, user[0][2], data[3], data[2], data[1]))
    conn.commit()
    conn.close()
    return "Success"

def deleteEmail(data):
    if len(data) != 2: return "Dados Invalidos"
    conn = conection()
    if conn == None:
        return "Fail in acsses DB"
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Token  LIKE ? AND Token LIKE ?", (data[0], data[0]))
    user = cursor.fetchall()
    if len(user) != 1: return "Token Invalido"
    user = user[0]
    cursor.execute("DELETE  FROM Emails WHERE Para LIKE ? AND id LIKE ?", (user[2], data[1]))
    conn.commit()
    conn.close()
    return "Success"