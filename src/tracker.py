# src/tracker.py

def adicionar_medicamento(lista, nome, horario):
    """Adiciona um medicamento à lista após validar os dados."""
    if not nome or not horario:
        return False, "Nome e horário são obrigatórios."
    
    medicamento = {
        "nome": nome,
        "horario": horario,
        "tomado": False
    }
    lista.append(medicamento)
    return True, "Medicamento adicionado com sucesso!"

def listar_medicamentos(lista):
    """Retorna a lista de medicamentos formatada."""
    if not lista:
        return "Nenhum medicamento cadastrado."
    
    corpo = ""
    for i, med in enumerate(lista):
        status = "[X]" if med["tomado"] else "[ ]"
        corpo += f"{i} - {status} {med['nome']} às {med['horario']}\n"
    return corpo