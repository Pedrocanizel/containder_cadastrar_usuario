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
    sobrenome = data['sobrenome']
    cidade = data['cidade']
    telefone = data['telefone']
    estado = str(data['estado']).upper()
    cadastro_criado_em = str(datetime.datetime.now())

    cursor = conn.cursor()
    query = f"""INSERT INTO bitgcp.reg_user (email, name, password, last_name, city, phone, state, created_at, search_id, active) VALUES ('{email}', '{name}', '{password}', '{sobrenome}', '{cidade}', '{telefone}' , '{estado}', '{cadastro_criado_em}', '{name}-{email}', 3)"""
    cursor.execute(query)
    conn.commit()
    conn.close()


def conferir_email(email):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""SELECT COUNT(email) FROM bitgcp.users WHERE email = '{email}'"""
    contagem = pd.read_sql_query(query, con=conn)
    contagem = contagem['count'].loc[0]
    return contagem
