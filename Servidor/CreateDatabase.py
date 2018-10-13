import sqlite3

conn = sqlite3.connect("mydatabase.db") # ou use :memory: para botá-lo na memória RAM

cursor = conn.cursor()

# cria uma tabela
cursor.execute("""CREATE TABLE Usuarios
                 (id integer PRIMARY KEY AUTOINCREMENT, 
                  Nome text NOT NULL, 
                  Email text NOT NULL,
                  Senha text,
                  Token text)
              """)

cursor.execute("""CREATE TABLE Emails
                 (id integer PRIMARY KEY  AUTOINCREMENT,
                  De text NOT NULL, 
                  Para text NOT NULL,
                  conteudo text NOT NULL,
                  Assunto text NOT NULL,
                  FOREIGN KEY (De) REFERENCES Usuarios (Email) 
                 )
              """)