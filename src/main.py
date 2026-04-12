from tracker import adicionar_medicamento, listar_medicamentos


def menu():
    meus_remedios = []
    while True:
        print("\n--- MediKeep: Controle ---")
        print("1. Adicionar Medicamento")
        print("2. Listar")
        print("3. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            nome = input("Nome: ")
            hora = input("Hora: ")
            sucesso, msg = adicionar_medicamento(meus_remedios, nome, hora)
            print(msg)
        elif opcao == "2":
            print(listar_medicamentos(meus_remedios))
        elif opcao == "3":
            break


if __name__ == "__main__":
    menu()
    
