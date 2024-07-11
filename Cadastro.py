import streamlit as st
import pandas as pd
from datetime import date
import re

# Função para gravar dados
def gravar_dados(nome, data_nasc, tipo, endereco, telefone, cpf_cnpj):
    if not nome:
        st.error("O nome não pode estar vazio!", icon="⚠️")
        return
    
    
    if not re.match(r'^[a-zA-ZÀ-ÿ\s]+$', nome):
        st.error("O nome deve conter apenas letras e espaços!", icon="⚠️")
        return
    
        
    if not data_nasc <= date.today():
        st.error("A data de nascimento não pode ser no futuro!", icon="⚠️")
        return
    
    if not endereco:
        st.error("O endereço não pode estar vazio!", icon="⚠️")
        return
    
    if not telefone.isdigit() or len(telefone) < 10:
        st.error("O telefone deve conter apenas números e ter no mínimo 10 digitos!", icon="⚠️")
        return
    
    if tipo == "Pessoa Física" and (not cpf_cnpj.isdigit() or len(cpf_cnpj) != 11):
        st.error("O CPF deve conter 11 dígitos!", icon="⚠️")
        return
    
    if tipo != "Pessoa Física" and (not cpf_cnpj.isdigit() or len(cpf_cnpj) != 14):
        st.error("O CNPJ deve conter 14 dígitos!", icon="⚠️")
        return
    
    try:
        # Verificar se o arquivo existe para determinar se devemos adicionar o cabeçalho
        try:
            existing_data = pd.read_csv("clientes.csv", sep=';', encoding="utf-8")
            header = False
        except FileNotFoundError:
            header = True
        except pd.errors.EmptyDataError:
            header = True
    
    # Adicionar novo registro
        new_data = pd.DataFrame([[nome, data_nasc, tipo, endereco, telefone, cpf_cnpj]],
                                columns=["Nome", "Data de Nascimento", "Tipo", "Endereço", "Telefone", "CPF/CNPJ"])
        
        new_data.to_csv("clientes.csv", sep=';', mode='a', index=False, header=header, encoding="utf-8")
        st.session_state["sucesso"] = True
    except Exception as e:
        st.session_state["sucesso"] = False
        st.error(f"Erro ao salvar os dados: {e}", icon="⚠️")
        

# Configurações da página

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="💾",
    layout="centered"
)


# Título de descrição
st.title("Cadastro de Clientes")
st.write("Por favor, preencha as informações abaixo para cadastrar um novo cliente.")

st.divider()

# Formulário de cadastro
with st.form(key='cadastro_cliente'):
    col1, col2, = st.columns(2)
    
    with col1:
        nome = st.text_input("Nome do cliente", 
                             key="nome_client", 
                             max_chars=30)
        dt_nasc = st.date_input("Data de nascimento",
                             key="dt_nasc",
                             min_value=date(1900, 1, 1),
                             format="DD/MM/YYYY")
        tipo = st.selectbox("Tipo do cliente", ["Pessoa Física", "Pessoa Jurídica", "MEI"], 
                             key="tipo_cliente")
        
    with col2:
        endereco = st.text_input("Endereço completo",
                                key="endereco_cliente", 
                                max_chars=100)
        telefone = st.text_input("Telefone", 
                                 key="telefone_cliente", 
                                 max_chars=15)
        cpf_cnpj = st.text_input("CPF ou CNPJ", 
                                 key="cpf_cnpj_cliente", 
                                 max_chars=14)
        
    btn_cadstrar = st.form_submit_button(label="Cadastrar")
    

if btn_cadstrar:
    gravar_dados(nome, dt_nasc, tipo, endereco, telefone, cpf_cnpj)
    if st.session_state.get("sucesso"):
       st.success("Cliente cadastrado com sucesso!", icon="👍🏼")
    else:
       st.error("Houve algum problema no cadastro!", icon="👎🏼")