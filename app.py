import streamlit as st
import csv
import pandas as pd

ARQUIVO = "cadastro.csv"

estados_brasil = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]

def ler_arquivo():
    pessoas = []
    try:
        with open(ARQUIVO, "r", newline='') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha["idade"] == "idade":  # evita cabeçalho duplicado
                    continue
                pessoas.append({
                    "nome": linha["nome"],
                    "idade": int(linha["idade"]),
                    "estado": linha["estado"]
                })
    except FileNotFoundError:
        pass
    return pessoas

def salvar_arquivo(pessoas):
    with open(ARQUIVO, "w", newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["nome", "idade", "estado"])
        escritor.writeheader()
        for pessoa in pessoas:
            escritor.writerow(pessoa)

st.set_page_config(page_title="Cadastro de Pessoas", page_icon="📝", layout="wide")
st.title("✨📋 Cadastro de Pessoas")

pessoas = ler_arquivo()

menu = st.sidebar.selectbox("Menu", [
    "Cadastrar Pessoa",
    "Exibir Pessoas",
    "Buscar por Estado",
    "Ordenar por Nome",
    "Ordenar por Idade",
    "Exportar JSON"
])

if menu == "Cadastrar Pessoa":
    st.subheader("📥 Formulário de Cadastro")
    with st.form("cadastro_form"):
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome")
            estado = st.selectbox("Selecione seu estado", estados_brasil)
        with col2:
            idade = st.number_input("Idade", min_value=0, max_value=150, step=1)
        enviar = st.form_submit_button("Cadastrar")

    if enviar:
        if not nome:
            st.error("❌ Por favor, preencha o nome.")
        else:
            nova = {"nome": nome, "idade": idade, "estado": estado}
            pessoas.append(nova)
            salvar_arquivo(pessoas)
            st.success(f"✅ {nome} cadastrado(a) com sucesso!")

elif menu == "Exibir Pessoas":
    st.subheader("📋 Lista de Pessoas")
    if pessoas:
        df = pd.DataFrame(pessoas)
        st.dataframe(df)
    else:
        st.info("Nenhuma pessoa cadastrada ainda.")

elif menu == "Buscar por Estado":
    st.subheader("🔎 Buscar Pessoas por Estado")
    estado_busca = st.selectbox("Selecione o estado para buscar", [""] + estados_brasil)
    if estado_busca:
        filtradas = [p for p in pessoas if p["estado"].lower() == estado_busca.lower()]
        if filtradas:
            df = pd.DataFrame(filtradas)
            st.dataframe(df)
        else:
            st.warning(f"Nenhuma pessoa encontrada no estado '{estado_busca}'.")

elif menu == "Ordenar por Nome":
    st.subheader("📈 Pessoas Ordenadas por Nome")
    ordenadas = sorted(pessoas, key=lambda p: p["nome"])
    if ordenadas:
        df = pd.DataFrame(ordenadas)
        st.dataframe(df)
    else:
        st.info("Nenhuma pessoa cadastrada ainda.")

elif menu == "Ordenar por Idade":
    st.subheader("📈 Pessoas Ordenadas por Idade")
    ordenadas = sorted(pessoas, key=lambda p: p["idade"])
    if ordenadas:
        df = pd.DataFrame(ordenadas)
        st.dataframe(df)
    else:
        st.info("Nenhuma pessoa cadastrada ainda.")

elif menu == "Exportar JSON":
    st.subheader("📤 Exportar Cadastro para JSON")
    nome_json = st.text_input("Nome do arquivo JSON", value="cadastro.json")
    if st.button("Exportar"):
        import json
        with open(nome_json, "w", encoding="utf-8") as f:
            json.dump(pessoas, f, ensure_ascii=False, indent=4)
        st.success(f"Arquivo '{nome_json}' exportado com sucesso!")
