import streamlit as st
import time

# Configuração da página
st.set_page_config(
    page_title="RealtyBuddy - O Teu Mentor AI",
    page_icon="🏢",
    layout="wide"
)

# LINK REAL DE PAGAMENTO (STRIPE CHECKOUT)
STRIPE_PAYMENT_URL = "https://stripe.com" 

# --- ESTADO GLOBAL DA APLICAÇÃO (MEMÓRIA DO BOT) ---
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"
if "ai_messages_left" not in st.session_state:
    st.session_state.ai_messages_left = 3
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"

# Memória dinâmica gerada pela IA a partir do texto do utilizador
if "dados_do_dia" not in st.session_state:
    st.session_state.dados_do_dia = {
        "titulo_foco": "Sem tarefas processadas para hoje",
        "checklist": [],
        "alertas_notificacao": [],
        "rota_gps": ""
    }

# --- BARRA LATERAL: ANTI-BATOTA & UPGRADE VITALÍCIO ---
with st.sidebar:
    st.title("🏢 RealtyBuddy")
    st.caption("O teu parceiro inteligente")
    st.divider()
    
    if st.button("🏠 Ir para a Home", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()
        
    st.divider()
    st.subheader("🛡️ Proteção de Acesso")
    if st.session_state.user_status == "Free":
        st.error("Plano Grátis (Limitado por Hardware)")
        st.write(f"Créditos de IA restantes: **{st.session_state.ai_messages_left}**")
        
        st.markdown(
            f'<a href="{STRIPE_PAYMENT_URL}" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #ff4b4b; color: white; text-align: center; '
            'padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer;">'
            '🚀 ADQUIRIR PRO VITALÍCIO (19.99€)'
            '</div></a>', 
            unsafe_allow_html=True
        )
        if st.button("Simular Ativação PRO"):
            st.session_state.user_status = "Pro"
            st.rerun()
    else:
        st.success("⭐ Membro PRO Vitalício")
        st.write("Mensagens de IA: **Ilimitadas (Local LLM)**")

# --- NAVEGAÇÃO POR PÁGINAS (HOME / SEPARADORES) ---

# PÁGINA: HOME (Menu por Nomes e Ícones)
if st.session_state.pagina_atual == "Home":
    st.title("👋 Bem-vindo ao RealtyBuddy")
    st.subheader("O que queres organizar ou consultar agora?")
    st.write("Seleciona uma pasta abaixo para trabalhar com o teu Mentor AI.")
    
    # Grelha visual de Botões com Ícones Temáticos
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⏰ O Meu Dia", use_container_width=True):
            st.session_state.pagina_atual = "O Meu Dia"
            st.rerun()
        if st.button("⚖️ Separador Advogado", use_container_width=True):
            st.session_state.pagina_atual = "Separador Advogado"
            st.rerun()
            
    with col2:
        if st.button("👥 Leads & Clientes", use_container_width=True):
            st.session_state.pagina_atual = "Leads & Clientes"
            st.rerun()
        if st.button("📣 Hub de Marketing", use_container_width=True):
            st.session_state.pagina_atual = "Hub de Marketing"
            st.rerun()
            
    with col3:
        if st.button("📊 Preço m² por Zona", use_container_width=True):
            st.session_state.pagina_atual = "Preço m² por Zona"
            st.rerun()

# PÁGINA: O MEU DIA (O Processador Dinâmico da AI)
elif st.session_state.pagina_atual == "O Meu Dia":
    st.title("⏰ O Meu Dia — Mentor Inteligente")
    st.write("Despeja aqui tudo o que tens planeado ou na cabeça. O Mentor vai organizar visualmente, criar a checklist e agendar os alarmes e GPS para ti.")
    
    # Campo de Entrada Livre para o Consultor desabafar
    entrada_caos = st.text_area(
        "Escreve livremente (Ex: 'Vou ter com o cliente X às 14h na Rua das Flores para ver um T2, tenho de levar os contratos e não posso esquecer de passar no banco antes...')",
        height=150,
        placeholder="Escreve o teu dia aqui..."
    )
    
    if st.button("⚡ Organizar o meu Dia com AI"):
        if st.session_state.user_status == "Free" and st.session_state.ai_messages_left <= 0:
            st.error("❌ Limite de créditos grátis esgotado. Faz o upgrade para PRO para continuar a usar o Mentor AI.")
        elif entrada_caos:
            if st.session_state.user_status == "Free":
                st.session_state.ai_messages_left -= 1
                
            with st.spinner("O teu Mentor AI está a analisar o texto e a estruturar o teu dia..."):
                time.sleep(1.5) # Simulação do processamento da Local LLM
                
                # SIMULAÇÃO DA INTELIGÊNCIA ARTIFICIAL: 
                # O bot analisa o texto introduzido pelo utilizador e preenche os blocos dinamicamente.
                # Para o exemplo, vamos quebrar o texto simulando a interpretação da IA.
                st.session_state.dados_do_dia["titulo_foco"] = "Compromisso Detetado na Agenda"
                st.session_state.dados_do_dia["checklist"] = [
                    f"Preparar os materiais necessários implícitos no seu texto",
                    f"Validar os detalhes e chaves do imóvel mencionado",
                    f"Confirmar o trajeto antes da hora indicada"
                ]
                st.session_state.dados_do_dia["alertas_notificacao"] = [
                    "🔔 Alarme automático programado para as 08:00 para iniciar a preparação.",
                    "🚗 Notificação ativa: O GPS vai abrir automaticamente 30 minutos antes do compromisso."
                ]
                st.session_state.dados_do_dia["rota_gps"] = "https://google.com"
                st.success("✨ Dia organizado e estruturado visualmente pelo Mentor AI!")
                st.rerun()

    st.divider()
    
    # --- INTERFACE VISUAL GERADA DINAMICAMENTE PELA AI ---
    st.subheader("📋 O Teu Dia Estruturado Visualmente")
    st.info(f"**Foco Principal de Hoje:** {st.session_state.dados_do_dia['titulo_foco']}")
    
    c_col1, c_col2 = st.columns(2)
    
    with c_col1:
        st.write("### 🗂️ Checklist Extraída")
        if not st.session_state.dados_do_dia["checklist"]:
            st.caption("Nenhum item na lista. Diga ao Mentor o que vai fazer hoje.")
        for item in st.session_state.dados_do_dia["checklist"]:
            st.checkbox(item, value=False)
            
    with c_col2:
        st.write("### 🚨 Automações & Notificações Agendadas")
        if not st.session_state.dados_do_dia["alertas_notificacao"]:
            st.caption("Sem notificações ativas neste momento.")
        for alerta in st.session_state.dados_do_dia["alertas_notificacao"]:
            st.write(alerta)
            
        if st.session_state.dados_do_dia["rota_gps"]:
            st.markdown(
                f'<a href="{st.session_state.dados_do_dia["rota_gps"]}" target="_blank">'
                '<button style="width:100%; padding:10px; background-color:#1E88E5; color:white; '
                'border:none; border-radius:5px; font-weight:bold; cursor:pointer; margin-top:10px;">'
                '🗺️ Abrir Rota no GPS Automatizado'
                '</button></a>', 
                unsafe_allow_html=True
            )

# PÁGINAS SECUNDÁRIAS (Estrutura Simples para manter o exemplo leve)
else:
    st.title(f"📂 {st.session_state.pagina_atual}")
    st.write("Esta pasta funciona da mesma forma: tu dás a informação livre e o Mentor AI encarrega-se de organizar os dados, leis, leads ou marketing aqui dentro.")
    st.info("O motor dinâmico principal está montado no separador 'O Meu Dia'.")
            
