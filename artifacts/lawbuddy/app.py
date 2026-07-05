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

# --- ESTADO GLOBAL DA APLICAÇÃO (MEMÓRIA DO CRM) ---
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"
if "ai_messages_left" not in st.session_state:
    st.session_state.ai_messages_left = 3
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"
if "leads" not in st.session_state:
    st.session_state.leads = []

# Memória do processamento da IA
if "resposta_ai" not in st.session_state:
    st.session_state.resposta_ai = None

# --- BARRA LATERAL: MENU E UPGRADE ---
with st.sidebar:
    st.title("🏢 RealtyBuddy")
    st.caption("Mentor AI & CRM Inteligente")
    st.divider()
    
    if st.button("🏠 Voltar ao Menu Principal", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()
        
    st.divider()
    st.subheader("🛡️ Proteção Anti-Batota")
    if st.session_state.user_status == "Free":
        st.error("Plano Grátis Limitado")
        st.write(f"Mensagens de IA restantes: **{st.session_state.ai_messages_left}**")
        st.markdown(
            f'<a href="{STRIPE_PAYMENT_URL}" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #ff4b4b; color: white; text-align: center; '
            'padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer;">'
            '🚀 ADQUIRIR PRO VITALÍCIO (19.99€)'
            '</div></a>', 
            unsafe_allow_html=True
        )
    else:
        st.success("⭐ Membro PRO Vitalício")

# --- NAVEGAÇÃO ---

# 1. HOME (MENU COM ÍCONES)
if st.session_state.pagina_atual == "Home":
    st.title("👋 Olá, Consultor! Bem-vindo ao RealtyBuddy")
    st.write("O teu mentor imobiliário está pronto. Escolhe onde queres entrar:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏰ O Meu Dia (Falar com Mentor)", use_container_width=True):
            st.session_state.pagina_atual = "O Meu Dia"
            st.rerun()
    with col2:
        if st.button(f"👥 Pasta de Leads & Clientes ({len(st.session_state.leads)})", use_container_width=True):
            st.session_state.pagina_atual = "Leads & Clientes"
            st.rerun()

# 2. O MEU DIA (O MOTOR INTELIGENTE DA IA)
elif st.session_state.pagina_atual == "O Meu Dia":
    st.title("⏰ O Meu Dia — Análise do Mentor AI")
    st.write("Despeja tudo o que tens para fazer. O Mentor vai analisar o teu texto, dar-te conselhos de elite, sugerir ações e atualizar o teu CRM.")
    
    entrada_texto = st.text_area(
        "O que tens planeado?",
        height=150,
        placeholder="Escreve aqui o teu caos diário..."
    )
    
    if st.button("⚡ Analisar Contexto com AI"):
        if st.session_state.user_status == "Free" and st.session_state.ai_messages_left <= 0:
            st.error("❌ Créditos esgotados. Faz o upgrade para PRO para continuares a usar o teu Mentor.")
        elif entrada_texto:
            if st.session_state.user_status == "Free":
                st.session_state.ai_messages_left -= 1
                
            with st.spinner("O Mentor AI está a ler o teu plano e a preparar a estratégia..."):
                time.sleep(1.5)
                
                # MOTOR DE INTELIGÊNCIA DINÂMICA (Analisa o que o utilizador escreveu)
                texto_minusculo = entrada_texto.lower()
                analise = {
                    "checklist": [],
                    "conselhos": [],
                    "gps": None,
                    "pergunta_crm": None,
                    "tipo_evento": "Geral"
                }
                
                # Se detetar o patrão/jantar de gala
                if "patroa" in texto_minusculo or "patrão" in texto_minusculo or "gala" in texto_minusculo:
                    analise["conselhos"].append("👔 **Código de Vestuário:** Sendo um jantar de gala com a chefia, a tua imagem é a tua marca. Opta por um fato impecável e vai bem cheiroso (um perfume marcante, mas não exagerado).")
                    analise["conselhos"].append("🎁 **Network com o Patrão:** Excelente oportunidade para reforçar a tua posição. Levar uma atenção ou uma boa garrafa de vinho como prenda demonstra respeito e profissionalismo.")
                    analise["checklist"].append("Escolher fato de gala e garantir que está passado a ferro")
                    analise["checklist"].append("Preparar/comprar a lembrança para o patrão")
                
                # Se detetar a cliente/Praia da Rocha
                if "cliente" in texto_minusculo or "apartamento" in texto_minusculo:
                    analise["conselhos"].append("🤝 **Dica de Venda para a Cliente:** Como ela é dona de um apartamento, o teu objetivo é perceber se ela quer vender, arrendar ou se precisa de gestão. Não fales logo de comissões. Ouve as dores dela primeiro.")
                    analise["checklist"].append("Fazer pesquisa prévia de preços de apartamentos na Praia da Rocha")
                    
                    if "praia da rocha" in texto_minusculo:
                        analise["gps"] = "https://google.com"
                    
                    # O AI deteta que há uma nova potencial lead e gera uma pergunta óbvia
                    analise["pergunta_crm"] = {
                        "pergunta": "💡 O Mentor detetou uma cliente na Praia da Rocha. Esta dona do apartamento já é tua cliente fidelizada ou é uma nova Lead para o teu CRM?",
                        "sugestao_nome": "Dona do Apartamento (Praia da Rocha)"
                    }
                
                # Fallback se o texto for genérico
                if not analise["checklist"]:
                    analise["checklist"].append("Organizar a agenda na pasta de contactos")
                    analise["conselhos"].append("Foca-te em gerir bem o teu tempo para não chegares atrasado aos teus compromissos.")
                
                st.session_state.resposta_ai = analise
                st.rerun()

    # Mostrar os resultados gerados pela IA
    if st.session_state.resposta_ai:
        st.divider()
        st.header("🧠 Conselhos do teu Mentor AI")
        
        # Exibir conselhos personalizados baseados no texto
        for conselho in st.session_state.resposta_ai["conselhos"]:
            st.write(conselho)
            
        st.subheader("📋 Checklist Inteligente para Hoje")
        for item in st.session_state.resposta_ai["checklist"]:
            st.checkbox(item, value=False)
            
        # Ativação do GPS dinâmico se detetar localização
        if st.session_state.resposta_ai["gps"]:
            st.write("### 🚗 Gestão de Tempo & Rotas")
            st.write("O jantar é às 20h, por isso planeia o encontro com a cliente com margem de viagem!")
            st.markdown(
                f'<a href="{st.session_state.resposta_ai["gps"]}" target="_blank">'
                '<button style="padding:10px; background-color:#1E88E5; color:white; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">'
                '🗺️ Ligar GPS para a Praia da Rocha'
                '</button></a>', unsafe_allow_html=True
            )
            
        # O INTERATIVO: Pergunta óbvia da IA para alimentar o CRM
        if st.session_state.resposta_ai["pergunta_crm"]:
            st.divider()
            st.subheader("🤖 Interação com o CRM")
            st.info(st.session_state.resposta_ai["pergunta_crm"]["question"])
            
            tipo_selecionado = st.radio("Escolha a opção:", ["É uma Nova Lead (Guardar na pasta)", "Já é Cliente Registada"])
            
            if st.button("Confirmar e Guardar na Pasta"):
                if tipo_selecionado == "É uma Nova Lead (Guardar na pasta)":
                    st.session_state.leads.append({
                        "nome": st.session_state.resposta_ai["pergunta_crm"]["sugestao_nome"],
                        "tipo": "Lead Prospeção",
                        "data": time.strftime("%Y-%m-%d")
                    })
                    st.success("📥 Registado automaticamente! Esta informação foi enviada para a tua pasta de Leads.")
                else:
                    st.success("✅ Atualizado no histórico de clientes!")
                st.session_state.resposta_ai["pergunta_crm"] = None # Remove a pergunta após responder
                st.rerun()

# 3. PASTA DE LEADS
elif st.session_state.pagina_atual == "Leads & Clientes":
    st.title("👥 Pasta de Leads & Clientes")
    st.write("Aqui estão os dados capturados automaticamente pelo teu Mentor AI através das tuas conversas.")
    
    if not st.session_state.leads:
        st.info("A tua pasta de Leads está vazia. Conversa com o Mentor no separador 'O Meu Dia' para ele extrair clientes automaticamente daqui!")
    else:
        for idx, lead in enumerate(st.session_state.leads):
            with st.expander(f"👤 {lead['nome']}"):
                st.write(f"📂 **Tipo:** {lead['tipo']}")
                st.write(f"📅 **Capturado em:** {lead['data']}")
                st.caption("Dica do Mentor: Liga a esta lead nos próximos 3 dias para não arrefecer o negócio.")
    
