import json

def calcular_media_idade(pessoas):
    if not pessoas:
        return 0
    total = sum(p["idade"] for p in pessoas)
    return total / len(pessoas)

def buscar_por_estado(pessoas, estado):
    return [p for p in pessoas if p["estado"].lower() == estado.lower()]

def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda p: p["nome"])

def ordenar_por_idade(pessoas, reverso=False):
    return sorted(pessoas, key=lambda p: p["idade"], reverse=reverso)

def buscar_por_nome(pessoas, termo):
    return [p for p in pessoas if termo.lower() in p["nome"].lower()]

def exportar_json(pessoas, nome_arquivo_json="cadastro.json"):
    with open(nome_arquivo_json, "w", encoding="utf-8") as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=4)
    print(f"Arquivo JSON '{nome_arquivo_json}' exportado com sucesso!\n")

def gerar_estatisticas(pessoas):
    if not pessoas:
        print("Nenhuma pessoa cadastrada.\n")
        return
    print(f"Total de pessoas: {len(pessoas)}")
    idades = [p["idade"] for p in pessoas]
    print(f"Maior idade: {max(idades)}")
    print(f"Menor idade: {min(idades)}")
    estados = {}
    for p in pessoas:
        estados[p["estado"]] = estados.get(p["estado"], 0) + 1
    print("Quantidade por estado:")
    for estado, qtd in estados.items():
        print(f"- {estado}: {qtd}")
    print()
