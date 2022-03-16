#instalação da Biblioteca
import mysql.connector #Comando: pip install mysql-connector

db = mysql.connector.connect(
    host="XXX",
    user="XXX",
    passwd="XXX",
    database="XXX"
)

cursor = db.cursor()

#Criar base de dados

def CriarBase():
    cursor.execute("CREATE DATABASE cadastro")

#Criar Tabela

def CriarTabela():
    cursor.execute("CREATE TABLE LOGIN( Nome VARCHAR(45), Email VARCHAR(45), Senha CHAR(12));")

#Inserir Dados

def InserirDados():
    input_nome = input('Informe seu nome completo: ')
    input_email = input('Informe seu e-mail: ')
    input_senha = input('Informe uma senha de 12 dígitos: ')

    comando_sql = "INSERT INTO LOGIN (Nome, Email, Senha) VALUES(%s,%s,%s)"
    valores = (input_nome,input_email,input_senha)

    cursor.execute(comando_sql,valores)
    db.commit()

InserirDados()
