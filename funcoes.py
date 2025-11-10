from tabulate import tabulate

def media_consumo(g, d):
    consumo_medio = g/d
    return consumo_medio

def registrar_viagem(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    destino = input("Digite o destino: ")
    distancia = float(input("Digite a distância: "))
    gasto = float(input("Digite o gasto com combustível: "))
    
    consumo = media_consumo(gasto, distancia)
    
    viagem = {
    "Motorista": motorista, 
    "Destino": destino, 
    "Distância": distancia, 
    "Gasto": gasto,
    "Consumo": consumo
    }
    
    listaViagens.append(viagem)
    print("Viagem cadastrada com sucesso!")

def exibir_viagens(listaViagens):
    if not listaViagens:
        print("Nenhuma viagem cadastrada")
        return
    tabela = [[v["Motorista"], v["Destino"], v["Distância"], v["Gasto"], v["Consumo"]] for v in listaViagens]
    print(tabulate(tabela, headers=["Motorista", "Destino", "Distância", "Gasto", "Consumo"], tablefmt="fancy_grid"))
    
def buscar_motorista(listaViagens):
    motorista = input("Digite o nome do motorista que deseja buscar: ").lower().strip()
    resultado = []
    for item in listaViagens:
        if item["Motorista"].lower().strip() == motorista:
            resultado.append(item)   
    tabela = [[item["Motorista"], item["Destino"], item["Distância"], item["Gasto"], item["Consumo"]] for item in resultado]
    print(tabulate(tabela, headers=["Motorista", "Destino", "Distância", "Gasto", "Consumo"], tablefmt="fancy_grid"))


def viagem_mais_cara(listaViagens):
    caro = []
    maior_gasto = max(item["Gasto"] for item in listaViagens)
    for viagem in listaViagens:
        if viagem["Gasto"] == maior_gasto:
            caro.append(viagem)
    maior_gasto = max(v["Gasto"] for v in listaViagens)
    mais_caras = [v for v in listaViagens if v["Gasto"] == maior_gasto]
    tabela = [[v["Motorista"], v["Destino"], v["Distância"], v["Gasto"], v["Consumo"]] for v in mais_caras]
    print(tabulate(tabela, headers=["Motorista", "Destino", "Distância", "Gasto", "Consumo"], tablefmt="fancy_grid"))