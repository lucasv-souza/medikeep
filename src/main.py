import streamlit as st
from tracker import adicionar_medicamento, listar_medicamentos, buscar_cep

# Configuração da página Web
st.set_page_config(page_title="MediKeep", page_icon="💊")
st.title("💊 MediKeep - Controle de Medicamentos")

# Inicializa a lista de remédios na memória da página web
if "meus_remedios" not in st.session_state:
    st.session_state.meus_remedios = []

# --- SEÇÃO 1: API PÚBLICA (NOVO REQUISITO) ---
st.header("📍 Localização do Usuário")
cep_input = st.text_input("Digite seu CEP para configurar o endereço de atendimento:")

if cep_input:
    endereco, mensagem = buscar_cep(cep_input)
    if endereco:
        st.success(f"📍 Endereço Configurado: {endereco}")
    else:
        st.error(mensagem)

st.markdown("---")

# --- SEÇÃO 2: GERENCIAMENTO ---
st.header("📝 Cadastrar Medicamento")
nome_remedio = st.text_input("Nome do remédio:")
hora_remedio = st.text_input("Horário (ex: 08:00):")

if st.button("Adicionar"):
    sucesso, msg = adicionar_medicamento(st.session_state.meus_remedios, nome_remedio, hora_remedio)
    if sucesso:
        st.success(msg)
    else:
        st.error(msg)

st.markdown("---")

st.header("📋 Meus Medicamentos")
lista_formatada = listar_medicamentos(st.session_state.meus_remedios)
st.text(lista_formatada)