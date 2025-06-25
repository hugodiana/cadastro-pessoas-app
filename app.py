import streamlit as st
import csv
import os

ARQUIVO = "cadastro.csv"

def ler_arquivo(nome_arquivo):
    pessoas = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", newline='', encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                try:
                    pessoas.append({
                        "nome": linha["nome"],
                        "idade": int(linha["idade"]),
                        "estado": linha["estado"]
                    })
                except:
                    continue
    return pessoas

def salvar_arquivo(pessoas, nome_arquivo):
    with open(nome_arquivo, "w", newline='', encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["nome", "idade", "estado"])
        escritor.writeheader()
        for pessoa in pessoas:
            escritor.writerow(pessoa)

# Inicia app
st.set_page_config(page_title="Cadastro de Pessoas", layout="centered")
st.title("📝 Cadastro de Pessoas")

pessoas = ler_arquivo(ARQUIVO)

# Formulário de cadastro
with st.form("cadastro_form"):
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=0, step=1)
    estado = st.selectbox("Estado", [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES",
        "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
        "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
        "SP", "SE", "TO"
    ])
    submitted = st.form_submit_button("Cadastrar")

    if submitted:
        if nome.strip() == "":
            st.warning("Digite um nome válido.")
        else:
            pessoas.append({"nome": nome.strip(), "idade": idade, "estado": estado})
            salvar_arquivo(pessoas, ARQUIVO)
            st.success(f"{nome} cadastrado(a) com sucesso!")

# Exibe tabela
st.header("👥 Pessoas cadastradas")
if pessoas:
    st.table(pessoas)
else:
    st.info("Nenhuma pessoa cadastrada ainda.")
