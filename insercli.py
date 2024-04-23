import sqlalchemy as sal
import streamlit as st
import pyodbc

VNomeCli = st.text_input('Nome Completo')
VEndCli = st.text_input('Endereço')
VTelCli = st.text_input('Telefone')
VEmailCli = st.text_input('E-mail')

def QueryInsertParameter():
    vInsert = f"""
    INSERT INTO tbClientes
    (nome_cli,
    endereco_cli,
    telefone_cli,
    email_cli)
    VALUES(
    '{VNomeCli}'
    ,'{VEndCli}'
    ,'{VTelCli}'
    ,'{VEmailCli}'
    )
    """
    return vInsert

def get_control_Connection():
    vServer = 'DESKTOP-CO5BKKJ\SQLEXPRESS'
    vDatabase = 'MECHANICS'

    engine = sal.create_engine(f'mssql+pyodbc://@{vServer}/{vDatabase}?driver=ODBC+Driver+17+for+SQL+Server')
    return engine

def ExeculteCommandSql(Query: str):
    engine = get_control_Connection()
    with engine.connect() as con:
        con.execute(sal.text(Query))
        con.commit()

if st.button("Subir para o Banco"):
    vQuery = (QueryInsertParameter())
    ExeculteCommandSql(vQuery)