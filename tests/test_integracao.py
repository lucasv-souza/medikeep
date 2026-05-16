import requests
from src.tracker import buscar_cep


def test_buscar_cep_sucesso_integracao():
    """Teste de integração real que valida a comunicação com a API do ViaCEP."""
    cep_teste = "01001000"  # CEP da Praça da Sé - SP (sem traço para bater com a nossa limpeza)
    endereco, mensagem = buscar_cep(cep_teste)

    assert mensagem == "Sucesso"
    assert endereco is not None
    assert "Praça da Sé" in endereco
    assert "SP" in endereco


def test_buscar_cep_invalido_integracao():
    """Valida o comportamento do sistema com um CEP que não segue o padrão."""
    cep_invalido = "123"
    endereco, mensagem = buscar_cep(cep_invalido)

    assert endereco is None
    assert "CEP inválido" in mensagem