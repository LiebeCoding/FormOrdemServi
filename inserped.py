import sqlalchemy as sal
import streamlit as st
import pyodbc

VidCli = st.text_input('ID do Cliente')
VIDServ = st.text_input('ID de Serviço')
VsttsPed = st.text_input('Status do Pedido')
VmdlCar = st.text_input('Modelo do Veículo')
VplcCar = st.text_input('Placa do Veículo')
VchsCar = st.text_input('Chassi do Veículo')


def QueryInsertParameter():
    vInsert = f"""
    INSERT INTO tbPedidos
    (id_cliente,
    id_servico,
    status_pedido,
    modelo_veiculo,
    placa_veiculo,
    chassi_veiculo)
    VALUES(
    '{VidCli}'
    ,'{VIDServ}'
    ,'{VsttsPed}'
    ,'{VmdlCar}'
    ,'{VplcCar }'
    ,'{VchsCar}'
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