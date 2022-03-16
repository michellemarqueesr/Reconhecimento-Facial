import sqlalchemy
import pandas as pd
import pymysql
import mysql.connector

nome_completo = input(str('Insira seu nome: '))
email = input(str('Insira seu e-mail: '))
senha = input(str('Insira sua senha de 12 digitos: '))

#Conexão com BD
#engine = sqlalchemy.create_engine('mysql+pymysql://root:oracle@localhost:3306/db_biblioteca')
#conexao = pymysql.connect(db='db_biblioteca', user='root', passwd='Alesi@mi12345')
#Leitura da Tabela
#df = pd.read_sql_table('login',engine, columns=['Email', 'Senha'])
#Criando o cursor para inserção
#cursor = conexao.cursor()
#inserção de dados
#cursor.execute("INSERT INTO login VALUES (%s, %s, %s);", (nome_completo, email, senha))
##Realizando o commit
#conexao.commit()
#Encerra conexão
#conexao.close()
#exibe tabela
#print(df)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Alesi@mi12345"
)

cursor = db.cursor()

#Criar base de dados

def CriarBase():
    cursor.execute("CREATE DATABASE cadastro")

CriarBase()




#Criar Tabela

#Inserir Dados
