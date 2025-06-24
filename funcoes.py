import os
import csv

def cadastrar_pessoa(pessoas, nome_arquivo):
    nome = input("Digite o nome:")
    idade = int(input("Digite a idade:"))
    estado = input("Digite o estado:")
    pessoa = {"nome" : nome, "idade" : idade, "estado": estado}
    pessoas.append(pessoa)
    salvar_arquivo(pessoas, nome_arquivo)
    print("Pessoa cadastrada com sucesso!\n")

def salvar_arquivo(pessoas, nome_arquivo):
    with open(nome_arquivo, "a", newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["nome", "idade", "estado"])
        escritor.writeheader()
        for pessoa in pessoas:
            escritor.writerow(pessoa)
    print("Arquivo salvo com sucesso!\n")


def ler_arquivo(nome_arquivo):
    pessoas = []
    if not os.path.exists(nome_arquivo):
        # Arquivo não existe, retorna lista vazia
        return pessoas

    with open(nome_arquivo, "r", newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            # Verifica se a linha está completa e os dados são válidos
            try:
                nome = linha.get("nome", "").strip()
                idade = int(linha.get("idade", "0").strip())
                estado = linha.get("estado", "").strip()

                if nome and estado:
                    pessoas.append({
                        "nome": nome,
                        "idade": idade,
                        "estado": estado
                    })
            except (ValueError, TypeError):
                # Ignora linhas problemáticas
                continue
    return pessoas

def exibir_pessoas(pessoas):
    if not pessoas:
        print("Nenhuma pessoa para exibir.\n")
    else:
        for i, pessoa in enumerate(pessoas, start=1):
            print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Estado: {pessoa['estado']}")
        print()

def excluir_pessoa(pessoas, nome_arquivo):
    if not pessoas:
        print("Nenhuma pessoa cadastrada para excluir.\n")
        return
    
    exibir_pessoas(pessoas)
    try:
        indice = int(input("Digite o número da pessoa que deseja excluir:"))
        if 1 <= indice <= len(pessoas):
            excluida = pessoas.pop(indice - 1)
            salvar_arquivo(pessoas, nome_arquivo)
            print(f"{excluida['nome']} foi excluido(a) e arquivo atualizado. \n")
        else:
            print("Número inválido. \n")
    except ValueError:
        print("Entrada inválida. \n")