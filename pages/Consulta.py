import streamlit as st
import pandas as pd

def carregar_dados():
    try:
        return pd.read_csv("clientes.csv", sep=';')
    except FileNotFoundError:
        st.error("O arquivo 'clientes.csv' não foi encontrado.", icon="⚠️")
        return pd.DataFrame(columns=["nome", "data_nasc", "tipo", "endereco", "telefone", "cpf_cnpj"])
    except pd.errors.EmptyDataError:
        st.warning("Nenhum cliente cadastrado ainda.", icon="⚠️")
        return pd.DataFrame(columns=["nome", "data_nasc", "tipo", "endereco", "telefone", "cpf_cnpj"])

def formatar_telefone(telefone):
    if isinstance(telefone, str):
        # Remover qualquer caractere não numérico do telefone
        telefone = ''.join(filter(str.isdigit, telefone))
        if len(telefone) == 11:
            return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        elif len(telefone) == 10:
            return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
        else:
            return telefone
    else:
        return telefone

def formatar_cpf_cnpj(cpf_cnpj):
    if isinstance(cpf_cnpj, str):
        # Remover qualquer caractere não numérico do CPF/CNPJ
        cpf_cnpj = ''.join(filter(str.isdigit, cpf_cnpj))
        if len(cpf_cnpj) == 11:
            return f"{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}"
        elif len(cpf_cnpj) == 14:
            return f"{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:]}"
        else:
            return cpf_cnpj
    else:
        return cpf_cnpj

df = carregar_dados()

st.set_page_config(
    page_title="Consulta de Clientes",
    page_icon="📋",
    layout="centered"
)

st.title("Clientes Cadastrados")
st.write("Abaixo está a lista de clientes cadastrados:")

st.divider()

if not df.empty:
    # Aplicar formatação aos campos de telefone e CPF/CNPJ
    df["telefone"] = df["telefone"].apply(formatar_telefone)
    df["cpf_cnpj"] = df["cpf_cnpj"].apply(formatar_cpf_cnpj)
    st.dataframe(df)
else:
    st.info("Nenhum cliente cadastrado.", icon="ℹ️")
