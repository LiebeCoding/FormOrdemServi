import sqlalchemy as sal
import streamlit as st
import pyodbc

VidHist = st.text_input('ID do Pedido Histórico')


def QueryInsertParameter():
    vInsert = f"""
    SELECT id_pedido
    FROM tbHistPedidos
    WHERE id_hist = {VidHist}
    """
    return vInsert

def QueryInsertParameter1():
    vInsert = f"""
    SELECT id_cliente
    FROM tbHistPedidos
    WHERE id_hist = {VidHist}
    """
    return vInsert

def QueryInsertParameter2():
    vInsert = f"""
    SELECT id_servico
    FROM tbHistPedidos
    WHERE id_hist = {VidHist}
    """
    return vInsert

def QueryInsertParameter3():
    vInsert = f"""
    SELECT status_pedido
    FROM tbHistPedidos
    WHERE id_hist = {VidHist}
    """
    return vInsert

def QueryInsertParameter4():
    vInsert = f"""
    SELECT modelo_veiculo
    FROM tbHistPedidos
    WHERE id_hist = {VidHist}
    """
    return vInsert

def QueryInsertParameter5():
    vInsert = f"""
    SELECT placa_veiculo
    FROM tbHistPedidos
    WHERE id_hist = {VidHist}
    """
    return vInsert

def QueryInsertParameter6():
    vInsert = f"""
    SELECT chassi_veiculo
    FROM tbHistPedidos
    WHERE id_hist = {VidHist}
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


if st.button("Consultar Serviço no Histórico"):
    vQuery = (QueryInsertParameter())
    if vQuery is not None:
        vQuery1 = (QueryInsertParameter1())
        vQuery2 = (QueryInsertParameter2())
        vQuery3 = (QueryInsertParameter3())
        vQuery4 = (QueryInsertParameter4())
        vQuery5 = (QueryInsertParameter5())
        vQuery6 = (QueryInsertParameter6())
        id_pedido = ExeculteCommandSql(vQuery)
        id_cliente = ExeculteCommandSql(vQuery1)
        id_servico = ExeculteCommandSql(vQuery2)
        status_pedido = ExeculteCommandSql(vQuery3)
        modelo_veiculo = ExeculteCommandSql(vQuery4)
        placa_veiculo = ExeculteCommandSql(vQuery5)
        chassi_veiculo = ExeculteCommandSql(vQuery6)

        if id_pedido is not None and id_cliente is not None and id_servico is not None and status_pedido is not None and modelo_veiculo is not None and placa_veiculo is not None and chassi_veiculo is not None:
            st.sidebar.write(f"ID do Pedido: {id_pedido}")
            st.sidebar.write(f"ID do Cliente: {id_cliente}")
            st.sidebar.write(f"ID antigo do Serviço: {id_servico}")
            st.sidebar.write(f"Status do Pedido: {status_pedido}")
            st.sidebar.write(f"Modelo do Veículo: {modelo_veiculo}")
            st.sidebar.write(f"Placa do Veiculo: {placa_veiculo}")
            st.sidebar.write(f"Chassi do Veiculo: {chassi_veiculo}")
        else:
            st.sidebar.write("Pedido está completo")






