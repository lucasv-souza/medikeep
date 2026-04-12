# tests/test_tracker.py
from src.tracker import adicionar_medicamento

def test_adicionar_medicamento_sucesso():
    """Caso 1: Caminho Feliz (Dados corretos)"""
    lista = []
    sucesso, msg = adicionar_medicamento(lista, "Aspirina", "08:00")
    assert sucesso is True
    assert len(lista) == 1
    assert lista[0]["nome"] == "Aspirina"

def test_adicionar_medicamento_sem_nome():
    """Caso 2: Entrada Inválida (Nome vazio)"""
    lista = []
    sucesso, msg = adicionar_medicamento(lista, "", "08:00")
    assert sucesso is False
    assert "obrigatórios" in msg
    assert len(lista) == 0

def test_adicionar_medicamento_sem_horario():
    """Caso 3: Entrada Inválida (Horário vazio)"""
    lista = []
    sucesso, msg = adicionar_medicamento(lista, "Dipirona", "")
    assert sucesso is False
    assert len(lista) == 0