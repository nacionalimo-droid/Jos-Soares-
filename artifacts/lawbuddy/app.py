import streamlit as st
import time
from datetime import datetime

# Configuração da página do Streamlit
st.set_page_config(
    page_title="RealtyBuddy - O Teu Mentor Imobiliário AI",
    page_icon="🏢",
    layout="wide"
)

# LINK REAL DE PAGAMENTO (STRIPE CHECKOUT)
STRIPE_PAYMENT_URL = "https://buy.stripe.com/dRmfZhaBC321b0682rdQQ00" 

# --- SIMULAÇÃO DE SISTEMA ANTI-BATOTA & CONTROLO DE ACESSO ---
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"  # Opções: "Free", "Pro"
if "ai_messages_left" not in st.session_state:
    st.session_state.ai_messages_left = 3  # Limite estrito de 3 mensagens na versão grátis
if "leads" not in st.session_state:
    st.session_state.leads = [
        {"nome": "Emanuel Silva", "telefone": "912 345 678", "interesse": "Morada X - Fotos hoje", "status": "Ativo"}
    ]

# --- BARRA LATERAL: PERFIL E UPGRADE ANTI-BATOTA ---
with st.sidebar:
    st.title("🏢 RealtyBuddy")
    st.caption("O teu parceiro imobiliário inteligente")
    st.divider()
    
    st.subheader("Estado da Conta")
    if st.session_state.user_status == "Free":
        st.error(" Plano Grátis (Limitado)")
        st.write(f"Mensagens de AI restantes: **{st.session_state.ai_messages_left}**")
        st.write("Limite de Dispositivo Ativo: 1 Conta por Hardware")
        
        # Botão oficial direcionando para o Stripe Checkout a cobrar 19.99€
        st.markdown(
            f'<a href="{STRIPE_PAYMENT_URL}" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #ff4b4b; color: white; text-align: center; '
            'padding: 12px; border-radius: 8px; font-weight: bold; margin-top: 10px; '
            'box-shadow: 0px 4px 6px rgba(0,0,0,0.1); cursor: pointer;">'
            '🚀 ADQUIRIR ACESSO PRO VITALÍCIO (19.99€)'
            '</div></a>', 
            unsafe_allow_html=True
        )
        st.caption("Desbloqueio vitalício sem mensalidades recorrentes.")
        
        st.divider()
        # Botão simulador para testar a versão PRO localmente na app
        if st.button("Simular Ativação PRO (Pós-Venda Stripe)"):
            st.session_state.user_status = "Pro"
            st.rerun()
    else:
        st.success("⭐ Membro PRO Vitalício")
        st.write("Mensagens de AI: **Ilimitadas (Local LLM)**")
        st.write("Proteção de Hardware: Vinculado ao seu telemóvel")

# --- PAINEL PRINCIPAL: SEPARADORES DO CRM INTUITIVO ---
tab_dia, tab_leads, tab_advogado, tab_marketing, tab_mercado = st.tabs([
    "⏰ O Meu Dia", 
    "👥 Leads & Clientes", 
    "⚖️ Separador Advogado", 
    "📣 Hub de Marketing", 
    "📊 Preço m² por Zona"
])

# --- SEPARADOR 1: O MEU DIA (DESPERTADOR E GPS) ---
with tab_dia:
    st.header("🌅 Briefing Matinal Automatizado")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("⏰ **Alarme Configurado:** Diariamente às 08:00")
        st.metric(label="Próximo Foco Programado pela AI", value="Venda & Fotos com Emanuel")
    
    with col2:
        st.warning("🚗 **Gatilho de Saída Automático:** Saída planeada para as 09:30")
        gps_url = "https://google.com"
        st.markdown(
            f'<a href="{gps_url}" target="_blank">'
            '<button style="width:100%; padding:10px; background-color:#1E88E5; color:white; '
            'border:none; border-radius:5px; font-weight:bold; cursor:pointer;">'
            '🗺️ Abrir GPS Automático (Rota para o Imóvel)'
            '</button></a>', 
            unsafe_allow_html=True
        )

    st.subheader("📝 Mentor AI: Checklist de Preparação para Hoje")
    st.write("Com base na tarefa agendada com o Emanuel, não te esqueças de:")
    
    c1 = st.checkbox("Carregar as baterias da câmara fotográfica", value=False)
    c2 = st.checkbox("Colocar o tripé na mala do carro", value=False)
    c3 = st.checkbox("Verificar as chaves do apartamento/morada", value=False)
    c4 = st.checkbox("Documento de autorização de angariação assinado", value=False)
    
    if c1 and c2 and c3 and c4:
        st.success("🎉 Tudo pronto! Estás organizado e sem falhas para a reunião.")

# --- SEPARADOR 2: LEADS & CLIENTES ---
with tab_leads:
    st.header("👥 Gestão Sincera de Leads")
    
    for i, lead in enumerate(st.session_state.leads):
        with st.expander(f"👤 {lead['nome']} - {lead['interesse']}"):
            st.write(f"📞 **Contacto:** {lead['telefone']}")
            st.write(f"📌 **Status:** {lead['status']}")
            st.caption("Memória AI: Lembrar de enviar o relatório de mercado na próxima abordagem.")
            
    st.divider()
    st.subheader("➕ Adicionar Nova Lead")
    novo_nome = st.text_input("Nome do Cliente")
    novo_tel = st.text_input("Telemóvel")
    novo_int = st.text_input("Imóvel/Zona de Interesse")
    
    if st.button("Guardar Lead"):
        if st.session_state.user_status == "Free" and len(st.session_state.leads) >= 3:
            st.error("❌ Limite do Plano Grátis Atingido! Altere para PRO para gerir leads ilimitadas.")
        elif not novo_nome:
            st.warning("Por favor, introduza o nome do cliente.")
        else:
            st.session_state.leads.append({"nome": novo_nome, "telefone": novo_tel, "interesse": novo_int, "status": "Novo"})
            st.success(f"Lead {novo_nome} guardada com sucesso na memória local!")
            st.rerun()

# --- SEPARADOR 3: SEPARADOR ADVOGADO (LEIS OFFLINE) ---
with tab_advogado:
    st.header("⚖️ Consultor Jurídico Local AI")
    st.caption("Respostas imediatas baseadas na legislação imobiliária em vigor.")
    
    pergunta_legal = st.text_input("Pergunta ao Advogado AI (Ex: Quais os escalões de IMT vigentes?)")
    
    if st.button("Consultar Legislação"):
        if st.session_state.user_status == "Free" and st.session_state.ai_messages_left <= 0:
            st.error("❌ Mensagens de AI esgotadas no plano grátis. Adquira o acesso PRO para continuar.")
        elif pergunta_legal:
            if st.session_state.user_status == "Free":
                st.session_state.ai_messages_left -= 1
            
            with st.spinner("A analisar a base de dados jurídica local..."):
                time.sleep(1)
                st.chat_message("assistant").write(
                    "**[Mentor Legal AI]:** De acordo com o código do IMT, as taxas aplicam-se de forma progressiva "
                    "sobre o valor de escritura ou VPC. Recomendo validar se o cliente reúne condições para isenção "
                    "por habitação própria e permanente."
                )
                if st.session_state.user_status == "Free":
                    st.rerun()

# --- SEPARADOR 4: HUB DE MARKETING ---
with tab_marketing:
    st.header("📣 Gerador de Conteúdo e Scripts")
    tipo_marketing = st.selectbox("O que queres criar hoje?", ["Descrição de Imóvel para Portal", "Script de Chamada Fria", "Post de Redes Sociais"])
    detalhes_imovel = st.text_area("Descreve brevemente o imóvel ou o objetivo (Ex: T2 Renovado em Benfica com varanda)")
    
    if st.button("Gerar com AI"):
        if st.session_state.user_status == "Free" and st.session_state.ai_messages_left <= 0:
            st.error("❌ Mensagens de AI esgotadas. Faça o upgrade para PRO para obter marketing ilimitado.")
        elif detalhes_imovel:
            if st.session_state.user_status == "Free":
                st.session_state.ai_messages_left -= 1
                
            with st.spinner("A redigir texto focado em conversão..."):
                time.sleep(1)
                st.success("Texto gerado com sucesso!")
                st.code(f"🌟 EXCLUSIVO EM BENFICA 🌟\n\nProcura o apartamento dos seus sonhos? Este fantástico {detalhes_imovel} combina localização premium com o conforto moderno...", language="markdown")
                if st.session_state.user_status == "Free":
                    st.rerun()

# --- SEPARADOR 5: PREÇO POR METRO QUADRADO ---
with tab_mercado:
    st.header("📊 Base de Dados de Preços Locais (m²)")
    st.write("Consulta rápida de valores de mercado de referência por zona.")
    
    zona = st.selectbox("Escolha a Zona / Concelho", ["Lisboa Centro", "Porto Alfragide", "Cascais/Estoril", "Braga Centro", "Algarve Turístico"])
    
    precos_referencia = {
        "Lisboa Centro": "4.800€ / m²",
        "Porto Alfragide": "3.100€ / m²",
        "Cascais/Estoril": "5.200€ / m²",
        "Braga Centro": "1.950€ / m²",
        "Algarve Turístico": "3.500€ / m²"
    }
    
    st.metric(label=f"Preço Médio Estimado por Localidade ({zona})", value=precos_referencia[zona])
    st.caption("Nota: Estes dados correm localmente no dispositivo e servem como estimativa prévia de angariação.")
    
