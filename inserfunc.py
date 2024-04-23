import sqlalchemy as sal
import streamlit as st
import pyodbc

VNomeFunc = st.text_input('Nome Completo')
VEndFunc = st.text_input('Endereço')
VTelFunc = st.text_input('Telefone')
VFuncaoFunc = st.text_input('Cargo ou Função')

def QueryInsertParameter():
    vInsert = f"""
    INSERT INTO tbFunc
    (nome_func,
    endereco_func,
    telefone_func,
    funcao_func)
    VALUES(
    '{VNomeFunc}'
    ,'{VEndFunc}'
    ,'{VTelFunc}'
    ,'{VFuncaoFunc}'
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