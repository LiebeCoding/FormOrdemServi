import sqlalchemy as sal
import streamlit as st
import pyodbc

VidFuncAss = st.text_input('ID do Funcionário Associado ao Serviço')
VtipServ = st.text_input('Tipo ou Descrição do Serviço')
VprecServ = st.text_input('Preço do Serviço')

def QueryInsertParameter():
    vInsert = f"""
    INSERT INTO tbServicos
    (id_func_assoc,
    tipo_servico,
    preco_servico)
    VALUES(
    '{VidFuncAss}'
    ,'{VtipServ}'
    ,'{VprecServ}'
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