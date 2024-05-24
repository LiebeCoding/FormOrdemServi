import streamlit as st
import subprocess

# Importando o menu do streamlit_antd_components
import streamlit_antd_components as sac

# Cor de fundo para a barra lateral
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa; /* Cor de fundo da barra lateral */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título da barra lateral
st.sidebar.title(""" Menu
                    Isael - Oficina e Funilaria """)

# Exibindo a mensagem formatada em Markdown na barra lateral
st.sidebar.markdown("""
**Versão do Sistema:** 1.001

Email de serviço ao cliente: rvcorp.clientservices@rvcorp.com

""")


# Definindo as opções do menu
menu_options = [
    sac.MenuItem('Cadastros', icon='plus-circle-fill', children=[
        sac.MenuItem('Criar Novos Pedidos', icon='plus-circle-fill'),
        sac.MenuItem('Cadastrar Novos Serviços', icon='plus-circle-fill'),
        sac.MenuItem('Cadastrar Clientes', icon='plus-circle-fill'),
        sac.MenuItem('Cadastrar Funcionários', icon='plus-circle-fill'),
        ]),
    sac.MenuItem('Consultas', icon='eye-fill', children=[
        sac.MenuItem('Consultar Pedidos', icon='eye-fill'),
        sac.MenuItem('Consultar Histórico de Serviços', icon='eye-fill'),
        sac.MenuItem('Consultar Funcionários', icon='eye-fill'),
])]

# Criando o menu dropdown na sidebar
menu_selected = sac.menu(menu_options, format_func='title', open_all=True)

# Verificando se uma opção válida foi selecionada
if menu_selected is not None:
    # Verificando qual opção foi selecionada e executando a ação correspondente
    if menu_selected == 'Criar Novos Pedidos':
        subprocess.Popen(["streamlit", "run", "inserped.py"])
    elif menu_selected == 'Cadastrar Novos Serviços':
        subprocess.Popen(["streamlit", "run", "inserserv.py"])
    elif menu_selected == 'Cadastrar Clientes':
        subprocess.Popen(["streamlit", "run", "insercli.py"])
    elif menu_selected == 'Cadastrar Funcionários':
        subprocess.Popen(["streamlit", "run", "inserfunc.py"])
    elif menu_selected == 'Consultar Pedidos':
        subprocess.Popen(["streamlit", "run", "consped.py"])
    elif menu_selected == 'Consultar Histórico de Serviços':
        subprocess.Popen(["streamlit", "run", "histserv.py"])
    elif menu_selected == 'Consultar Funcionários':
        subprocess.Popen(["streamlit", "run", "consfunc.py"])


