import psycopg2
import datetime
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='localhost', database='bit_pro',
                           user='postgres', password='123')
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
    query = f"""INSERT INTO public.cadastro_usuario (email, name, password, razao_social, sobrenome, idade, cpf, cnpj, telefone, estado, cadastro_criado_em) VALUES ('{email}', '{name}', '{password}', '{razao_social}', '{sobrenome}', '{idade}', '{cpf}', '{cnpj}', '{telefone}' , '{estado}', '{cadastro_criado_em}')"""
    cursor.execute(query)
    conn.commit()
    conn.close()
