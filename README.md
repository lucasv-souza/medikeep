# 💊 MediKeep - Gerenciador de Medicamentos

![CI Status](https://github.com/lucasv-souza/medikeep/actions/workflows/ci.yml/badge.svg)

**Acesse a aplicação ao vivo aqui:** [https://medikeep-hc5hyggbu5eraxepjywths.streamlit.app](https://medikeep-hc5hyggbu5eraxepjywths.streamlit.app)

---

## 📝 Descrição do Problema
Muitas pessoas, especialmente idosos e pacientes com doenças crônicas, enfrentam dificuldades para organizar seus horários de medicação. O esquecimento ou a confusão sobre quais doses já foram tomadas pode comprometer seriamente o tratamento e a saúde do paciente.

## 🚀 Proposta da Solução e Evolução
O **MediKeep** nasceu como uma aplicação de linha de comando (CLI) simples e eficaz. Na presente etapa intermediária, o projeto evoluiu para uma **interface Web moderna e responsiva**, tornando a experiência de uso ainda mais amigável, sem distrações e acessível diretamente pelo navegador.

**Público-alvo:** Idosos, cuidadores e pessoas em tratamentos temporários.

### 📍 Novas Funcionalidades:
* **Interface Gráfica Web:** Implementada com Streamlit para facilitar a interação do usuário.
* **Integração com API Pública (ViaCEP):** Conexão em tempo real com o serviço externo do ViaCEP para buscar, tratar e validar o endereço de atendimento ou entrega de medicamentos do usuário a partir do CEP informado.

---
## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Interface Web:** Streamlit
* **Consumo de API:** Requests
* **Testes:** Pytest
* **Qualidade de Código (Lint):** Flake8
* **Automação & Hospedagem:** GitHub Actions (CI) & Streamlit Cloud (Deploy)
* **Versão Atual:** 1.0.0 (Semantic Versioning)

---

## ⚙️ Como Instalar e Rodar

1. **Clone o repositório:**
```bash
git clone https://github.com/lucasv-souza/medikeep.git
cd medikeep
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```
3. **Execute a aplicação Web:**
```bash
streamlit run src/main.py
```

## 🧪 Testes e Qualidade
Para garantir o funcionamento correto e a integridade do código, o projeto conta com testes automatizados (unitários e de integração) integrados ao pipeline de CI:

* Testes Unitários (tests/test_tracker.py): Valida a lógica isolada de cadastro e validação de medicamentos.

* Testes de Integração (tests/test_integracao.py): Valida a comunicação real com a API pública do ViaCEP (cenários de sucesso e comportamento com CEP inválido).

* **Para rodar a suíte completa de testes:**
```bash
python -m pytest
```

* **Para rodar o linter (análise estática):**
```bash
flake8 src/ tests/ --ignore=W293,E302,E305,E501,W292,F401
```

---

## 🎓 Identificação do Autor

* **Aluno:** Lucas Vinicius de Souza
* **RA:** 22504534
* **Curso:** Ciência da Computação
