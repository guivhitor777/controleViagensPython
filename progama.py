from funcoes import *

lista = []

while True:
    print("Bem-vindo!")
    print("Aqui estão suas opções:")
    print("1 - Registrar viagem")
    print("2 - Exibir todas as viagens")
    print("3 - Buscar viagem por motorista")
    print("4 - Exibir viagem mais cara")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1: 
        registrar_viagem(lista)
    if opcao == 2:
        exibir_viagens(lista)
    if opcao == 3:
        buscar_motorista(lista)
    if opcao == 4:
        viagem_mais_cara(lista)
    if opcao == 0:
        print("Programa encerrado \U0001f609")
        break
    if opcao not in [1, 2, 3, 4, 0]:
        print("Opção inválida, tente novamente \U0001f615")