def adicionar_medicamento(lista, nome, horario):
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
    if not lista:
        return "Nenhum medicamento cadastrado."
    corpo = ""
    for i, med in enumerate(lista):
        status = "[X]" if med["tomado"] else "[ ]"
        corpo += f"{i} - {status} {med['nome']} às {med['horario']}\n"
    return corpo
    
