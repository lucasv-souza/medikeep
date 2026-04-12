# src/main.py
from tracker import adicionar_medicamento, listar_medicamentos

def menu():
    meus_remedios = []
    
    while True:
        print("\n--- MediKeep: Controle de Medicamentos ---")
        print("1. Adicionar Medicamento")
        print("2. Listar Meus Medicamentos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do remédio: ")
            hora = input("Horário (ex: 08:00): ")
            sucesso, msg = adicionar_medicamento(meus_remedios, nome, hora)
            print(msg)
            
        elif opcao == "2":
            print("\nSua Lista:")
            print(listar_medicamentos(meus_remedios))
            
        elif opcao == "3":
            print("Encerrando... Cuide da sua saúde!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()