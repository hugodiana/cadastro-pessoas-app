from funcoes import *
from utils import (
    calcular_media_idade,
    buscar_por_estado,
    ordenar_por_nome,
    ordenar_por_idade,
    buscar_por_nome,
    exportar_json,
    gerar_estatisticas
)

def exibir_menu():
    print("=" * 30)
    print("MENU DO PROGRAMA".center(30))
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Exibir pessoas")
    print("3 - Excluir pessoa")
    print("4 - Média de idades")
    print("5 - Listar pessoas por estado")
    print("6 - Listar ordenado por nome")
    print("7 - Listar ordenado por idade")
    print("8 - Buscar por nome")
    print("9 - Exportar para JSON")
    print("10 - Mostrar estatísticas")
    print("11 - Sair\n")

def main():
    NOME_ARQUIVO = "cadastro.csv"
    pessoas = ler_arquivo(NOME_ARQUIVO)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa(pessoas, NOME_ARQUIVO)
        elif opcao == "2":
            exibir_pessoas(pessoas)
        elif opcao == "3":
            excluir_pessoa(pessoas, NOME_ARQUIVO)
        elif opcao == "4":
            media = calcular_media_idade(pessoas)
            print(f"Média de idades: {media:.2f}\n")
        elif opcao == "5":
            estado = input("Digite o estado para buscar: ")
            encontrados = buscar_por_estado(pessoas, estado)
            exibir_pessoas(encontrados)
        elif opcao == "6":
            ordenados = ordenar_por_nome(pessoas)
            exibir_pessoas(ordenados)
        elif opcao == "7":
            ordenados = ordenar_por_idade(pessoas)
            exibir_pessoas(ordenados)
        elif opcao == "8":
            termo = input("Digite parte do nome para buscar: ")
            encontrados = buscar_por_nome(pessoas, termo)
            exibir_pessoas(encontrados)
        elif opcao == "9":
            exportar_json(pessoas)
        elif opcao == "10":
            gerar_estatisticas(pessoas)
        elif opcao == "11":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
