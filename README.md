# 💊 MediKeep - Gerenciador de Medicamentos CLI

![CI Status](https://github.com/lucasv-souza/medikeep/actions/workflows/ci.yml/badge.svg)

## 📝 Descrição do Problema
Muitas pessoas, especialmente idosos e pacientes com doenças crônicas, enfrentam dificuldades para organizar seus horários de medicação. O esquecimento ou a confusão sobre quais doses já foram tomadas pode comprometer seriamente o tratamento e a saúde do paciente.

## 🚀 Proposta da Solução
O **MediKeep** é uma aplicação de linha de comando (CLI) simples e eficaz que permite ao usuário cadastrar seus medicamentos e horários, além de listar as tarefas do dia. O objetivo é oferecer uma ferramenta leve, sem distrações e fácil de usar para garantir que nenhum remédio seja esquecido.

**Público-alvo:** Idosos, cuidadores e pessoas em tratamentos temporários.

**Funcionalidades:** Cadastro de remédios, definição de horários e visualização de lista.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Testes:** Pytest
* **Qualidade de Código (Lint):** Flake8
* **Automação:** GitHub Actions (CI)
* **Versão Atual:** 1.0.0 (Semantic Versioning)

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
3. **Execute a aplicação:**
```bash
python src/main.py
```

## 🧪 Testes e Qualidade
Para garantir o funcionamento correto, o projeto conta com testes automatizados e análise estática:

* **Para rodar os testes:**
```bash
pytest
```

* **Para rodar o lint (estilo de código):**
```bash
flake8 src/ --ignore=W293,E302,E305
```
