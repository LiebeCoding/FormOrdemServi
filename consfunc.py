import sqlalchemy as sal
import streamlit as st
import pyodbc

VidFunc = st.text_input('ID do Funcionário')


def QueryInsertParameter0():
    vInsert = f"""
    SELECT nome_func
    FROM tbFunc
    WHERE id_func = {VidFunc}
    """
    return vInsert

def QueryInsertParameter1():
    vInsert = f"""
    SELECT endereco_func
    FROM tbFunc
    WHERE id_func = {VidFunc}
    """
    return vInsert

def QueryInsertParameter2():
    vInsert = f"""
    SELECT telefone_func
    FROM tbFunc
    WHERE id_func = {VidFunc}
    """
    return vInsert

def QueryInsertParameter3():
    vInsert = f"""
    SELECT funcao_func
    FROM tbFunc
    WHERE id_func = {VidFunc}
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
        result = con.execute(sal.text(Query))
        row = result.fetchone()
        if row is not None:  # Verifica se a consulta retornou alguma linha
            return row[0]  # Retorna o primeiro valor da linha
        else:
            return None


if st.button("Consultar Funcionário"):
    vQuery = (QueryInsertParameter0())
    if vQuery is not None:
        vQuery1 = (QueryInsertParameter1())
        vQuery2 = (QueryInsertParameter2())
        vQuery3 = (QueryInsertParameter3())
        nome_func = ExeculteCommandSql(vQuery)
        endereco_func = ExeculteCommandSql(vQuery1)
        telefone_func = ExeculteCommandSql(vQuery2)
        funcao_func = ExeculteCommandSql(vQuery3)

        if nome_func is not None and endereco_func is not None and telefone_func is not None and funcao_func is not None:
            st.sidebar.write(f"Nome do Funcionário: {nome_func}")
            st.sidebar.write(f"Endereço do Funcionário: {endereco_func}")
            st.sidebar.write(f"Telefone do Funcionário: {telefone_func}")
            st.sidebar.write(f"Cargo: {funcao_func}")






