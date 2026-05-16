import requests


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


def buscar_cep(cep):
    """Consome a API pública do ViaCEP para buscar a localização do usuário."""
    # Remove traços ou espaços que o usuário possa digitar
    cep_limpo = str(cep).replace("-", "").replace(" ", "")

    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        return None, "CEP inválido. Deve conter 8 números."

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" in dados:
                return None, "CEP não encontrado."
            
            # Formata o endereço amigavelmente
            endereco = f"{dados.get('logradouro')}, {dados.get('bairro')} - {dados.get('localidade')}/{dados.get('uf')}"
            return endereco, "Sucesso"
        return None, "Erro na comunicação com o serviço de CEP."
    except requests.exceptions.RequestException:
        return None, "Sistema fora do ar. Tente novamente mais tarde."