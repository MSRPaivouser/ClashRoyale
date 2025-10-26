
import requests
import json


def inicio():
    print("+----------------------------------------------+")
    print("+             CARTAS CLASH ROYALE              +")
    print("+----------------------------------------------+")


def ordenar_cartas(dados):
    return sorted(dados["items"], key=lambda c: c["name"].lower())


def busca_binaria(cartas, nome_escolhido):
    inicio = 0
    fim = len(cartas) - 1
    nome_buscado = nome_escolhido.lower()

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_atual = cartas[meio]["name"].lower()

        if nome_atual == nome_buscado:
            return cartas[meio]  # encontrou a carta
        elif nome_atual < nome_buscado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None # nao encontrou nada


def raridade_cartas(dados):
    escolha = input("""Escolha uma raridade:
               (1) Comum
               (2) Raro
               (3) Épico
               (4) Lendário
               (5) Campeão
               -> """)
    match escolha:
            
        case "1":
            cartas_comuns = [
                carta for carta in dados["items"]
                if "rarity" in carta and carta["rarity"].lower() == "common"
            ]

            print("Você escolheu cartas Comuns!")
            for carta in cartas_comuns:
                print("-", carta["name"])

            
        case "2":
            cartas_raras = [
                carta for carta in dados["items"]
                if "rarity" in carta and carta["rarity"].lower() == "rare"
            ]

            print("Você escolheu cartas Raras!")
            for carta in cartas_raras:
                print("-", carta["name"])

        case "3":
            cartas_epicas = [
                carta for carta in dados["items"]
                if "rarity" in carta and carta["rarity"].lower() == "epic"
            ]

            print("Você escolheu cartas Épicas!")
            for carta in cartas_epicas:
                print("-", carta["name"])

        case "4":
            cartas_lendarias = [
                carta for carta in dados["items"]
                if "rarity" in carta and carta["rarity"].lower() == "legendary"
            ]

            print("Você escolheu cartas Lendárias!")
            for carta in cartas_lendarias:
                print("-", carta["name"])

        case "5":
            cartas_campeoes = [
                carta for carta in dados["items"]
                if "rarity" in carta and carta["rarity"].lower() == "champion"
            ]

            print("Você escolheu cartas Campeões!")
            for carta in cartas_campeoes:
                print("-", carta["name"])

        case _:
            print("❌ Opção inválida!")
           
def custo_cartas(dados):
    escolha = input("""Qual a sua escolha? 
                   (1) 1 de elixir
                   (2) 2 de elixir
                   (3) 3 de elixir
                   (4) 4 de elixir
                   (5) 5 de elixir
                   (6) 6 de elixir
                   (7) 7 de elixir
                   (8) 8 de elixir
                   (9) 9 de elixir
                   -> """)

    elixir = [
                carta for carta in dados["items"]
                if "elixirCost" in carta and carta["elixirCost"] == int(escolha)
            ]
    
    print(f"Você escolheu cartas que custam {escolha} de elixir!")

    for carta in elixir:
        print("-", carta["name"])
    
def filtrar_cartas(dados):
    raridade_escolha = input("""Escolha uma raridade:
                             (1) Comum
                             (2) Raro
                             (3) Épico
                             (4) Lendário
                             (5) Campeão
                             -> """)
    
    match raridade_escolha:
        case "1":
            raridade = "common"
        case "2":
            raridade = "rare"
        case "3":
            raridade = "epic"
        case "4":
            raridade = "legendary"
        case "5":
            raridade = "champion"
        case _:
            print("❌ Opção inválida de raridade!")
            return
        
    custo = input("""Escolha o custo:
                  (1) 1 de elixir 
                  (2) 2 de elixir 
                  (3) 3 de elixir 
                  (4) 4 de elixir 
                  (4) 4 de elixir 
                  (5) 5 de elixir 
                  (6) 6 de elixir 
                  (7) 7 de elixir 
                  (8) 8 de elixir
                  (9) 9 de elixir 
                  -> """)
    
    try:
        custo = int(custo)
    except ValueError:
        print("❌ Opção inválida de raridade!")
        return
    
    cartas_encontradas = [
        carta for carta in dados["items"]

        if "elixirCost" in carta and "rarity"
        and carta["elixirCost"] == custo
        and carta["rarity"].lower() == raridade
    ]

    print(f"Você escolheu cartas {raridade.capitalize()} que custam {custo} de elixir!")

    if not cartas_encontradas:
        print("Nenhuma carta encontrada!")
    else:
        for carta in cartas_encontradas:
            print("- ", carta["name"])

def voltar_sair():
    while True:
        escolha = input(""" O que você deseja:
                        (1) Voltar ao menu
                        (2) Sair
                        -> """)
        if escolha == "1":
            return  
        elif escolha == "2":
            print("Encerrando o programa. Até Logo!")
            exit()
        else:
            print("❌ Opção inválida.")

url = "https://api.clashroyale.com/v1/cards"


token = "SEU TOKEN AQUI" 

headers = {
    "Authorization": f"Bearer {token}"
}


requisicao = requests.get(url, headers=headers)


if requisicao.status_code == 200:
    dados = requisicao.json()

    while True:
        inicio()
        escolha = input("""Qual a sua escolha?
                        (1) Cartas por raridade
                        (2) Cartas por elixir
                        (3) Cartas por raridade e elixir
                        (4) Todas as cartas
                        (5) Procurar carta pelo nome (em inglês)
                        (0) Sair
                        -> """)
        match int(escolha):
            case 1:
                raridade_cartas(dados)
                voltar_sair()
            case 2:
                custo_cartas(dados)
                voltar_sair()
            case 3:
                filtrar_cartas(dados)
                voltar_sair()
            case 4:
                for carta in dados["items"]:
                    print("- ", carta["name"])
                voltar_sair()
            case 5:
                nome = input("""Escreva o nome da carta
                    -> """)
                
                cartas_ordenadas = ordenar_cartas(dados)

                carta = busca_binaria(cartas_ordenadas, nome)

                if carta:
                    print("Carta encontrada!")
                    print(f"- Nome: {carta['name']}")
                    print(f"- Raridade: {carta['rarity']}")
                    print(f"- Custo de elixir: {carta['elixirCost']}")
                    
                else:
                    print("Carta não encontrada!")
                voltar_sair()
            case 0:
                print("Encerrando o programa. Até logo!")
                break

                
            case _:
                print("❌ Opção inválida!")

else:
    print("Erro ao exportar dados!")
