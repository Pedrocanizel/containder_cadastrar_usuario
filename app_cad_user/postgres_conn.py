import psycopg2
import datetime
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='bd.bitgcp.com', database='bitgcp_tables',
                           user='postgres', password='example')
    return con


def insert_lines(data):
    conn = get_connect()
    email = data['email']
    name = data['name']
    password = data['password']
    razao_social = data['razao_social']
    sobrenome = data['sobrenome']
    idade = data['idade']
    cpf = data['cpf']
    cnpj = data['cnpj']
    telefone = data['telefone']
    estado = data['estado']
    cadastro_criado_em = str(datetime.datetime.now())

    cursor = conn.cursor()
    query = f"""INSERT INTO bitgcp.cadastro_usuario (email, name, password, razao_social, sobrenome, idade, cpf, cnpj, telefone, estado, cadastro_criado_em, id_consulta) VALUES ('{email}', '{name}', '{password}', '{razao_social}', '{sobrenome}', {idade}, '{cpf}', '{cnpj}', '{telefone}' , '{estado}', '{cadastro_criado_em}', '{name}-{email}')"""
    cursor.execute(query)
    conn.commit()
    conn.close()
