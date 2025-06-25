import streamlit as st
import csv
import os

ARQUIVO = "cadastro.csv"

# Funções
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

def calcular_media_idades(pessoas):
    if not pessoas:
        return 0
    soma = sum(p["idade"] for p in pessoas)
    return soma / len(pessoas)

def filtrar_por_estado(pessoas, estado_procurado):
    return [p for p in pessoas if p["estado"].lower() == estado_procurado.lower()]

def encontrar_mais_velho(pessoas):
    return max(pessoas, key=lambda p: p["idade"])

# App
st.set_page_config(page_title="Cadastro de Pessoas", layout="centered")
st.title("📝 Cadastro de Pessoas")

# Carrega dados
pessoas = ler_arquivo(ARQUIVO)

# Formulário
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

    # Estatísticas gerais
    media = calcular_media_idades(pessoas)
    st.write(f"📊 Média de idade geral: {media:.1f} anos")

    # Filtro por estado
    estado_filtro = st.selectbox("Escolha um estado para filtrar", sorted({p['estado'] for p in pessoas}))
    pessoas_estado = filtrar_por_estado(pessoas, estado_filtro)

    if pessoas_estado:
        st.write(f"👥 Pessoas em {estado_filtro}:")
        for p in pessoas_estado:
            st.write(f"- {p['nome']} ({p['idade']} anos)")

        mais_velho = encontrar_mais_velho(pessoas_estado)
        st.write(f"👑 Mais velho em {estado_filtro}: {mais_velho['nome']} ({mais_velho['idade']} anos)")
    else:
        st.info(f"Nenhuma pessoa cadastrada em {estado_filtro}.")
else:
    st.info("Nenhuma pessoa cadastrada ainda.")
