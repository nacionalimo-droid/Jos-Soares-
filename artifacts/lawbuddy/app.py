import streamlit as st
import json
import time

# Configuração da página do Streamlit
st.set_page_config(
    page_title="RealtyBuddy - O Teu Mentor AI",
    page_icon="🏢",
    layout="wide"
)

# LINK REAL DE PAGAMENTO (STRIPE CHECKOUT)
STRIPE_PAYMENT_URL = "https://stripe.com" 

# Configuração Segura da API da Google Gemini (Chave guardada nos Secrets do Streamlit)
# Para testares localmente sem secrets, podes substituir por: genai.configure(api_key="A_TUA_CHAVE_AQUI")
import google.generativeai as genai
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    # Fallback caso ainda não tenhas configurado a chave nos Secrets do Streamlit
    st.warning("⚠️ Chave API do Gemini não detetada nos Secrets. O Mentor vai correr em modo de simulação até a configurares.")

# --- ESTADO GLOBAL DA APLICAÇÃO (MEMÓRIA DO CRM) ---
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"
if "ai_messages_left" not in st.session_state:
    st.session_state.ai_messages_left = 3
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"
if "leads" not in st.session_state:
    st.session_state.leads = []
if "resposta_ai_real" not in st.session_state:
    st.session_state.resposta_ai_real = None

# --- BARRA LATERAL: MENU E CONTROLO ---
with st.sidebar:
    st.title("🏢 RealtyBuddy")
    st.caption("Mentor AI & CRM Real")
    st.divider()
    
    if st.button("🏠 Voltar ao Menu Principal", use_container_width=True):
        st.session_state.pagina_atual = "Home"
        st.rerun()
        
    st.divider()
    st.subheader("🛡️ Proteção Anti-Batota")
    if st.session_state.user_status == "Free":
        st.error("Plano Grátis Limitado")
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

# --- NAVEGAÇÃO ---

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

elif st.session_state.pagina_atual == "O Meu Dia":
    st.title("⏰ O Meu Dia — Análise do Mentor AI")
    st.write("Despeja tudo o que tens para fazer. O Mentor vai analisar o teu texto através de Inteligência Artificial real e organizar o teu dia.")
    
    entrada_texto = st.text_area(
        "O que tens planeado?",
        height=150,
        placeholder="Escreve aqui o teu plano..."
    )
    
    if st.button("⚡ Analisar Contexto com AI Real"):
        if st.session_state.user_status == "Free" and st.session_state.ai_messages_left <= 0:
            st.error("❌ Créditos esgotados. Faz o upgrade para PRO para continuares.")
        elif entrada_texto:
            if st.session_state.user_status == "Free":
                st.session_state.ai_messages_left -= 1
                
            with st.spinner("O Mentor AI Real está a estudar a tua mensagem..."):
                try:
                    # Engenharia de Prompt para forçar o Gemini a responder em formato estruturado (JSON)
                    prompt = f"""
                    Atua como um mentor de elite para consultores imobiliários. 
                    Analisa o seguinte plano enviado pelo consultor e extrai conselhos práticos, tarefas e dados de CRM.
                    Texto do consultor: "{entrada_texto}"
                    
                    Responde EXCLUSIVAMENTE num formato JSON válido com esta estrutura exata (não adiciones nenhum texto fora do JSON):
                    {{
                        "conselhos": ["lista de 2 ou 3 conselhos de imobiliária e postura específicos para o que ele descreveu"],
                        "checklist": ["tarefas lógicas que ele tem de fazer com base nas horas e eventos ditados"],
                        "alarme_hora": "hora sugerida para o alarme acordar o utilizador ex: 08:00",
                        "gps_local": "nome do local para o GPS se houver, ou string vazia",
                        "pergunta_crm": "uma pergunta inteligente sobre os clientes mencionados para guardar no CRM",
                        "sugestao_lead": "nome sugerido para criar uma lead se aplicável"
                    }}
                    """
                    
                    model = genai.Model(model_name="gemini-1.5-flash")
                    response = model.generate_content(prompt)
                    
                    # Limpa e processa o JSON devolvido pela IA
                    texto_resposta = response.text.strip().replace("```json", "").replace("```", "")
                    st.session_state.resposta_ai_real = json.loads(texto_resposta)
                
                except Exception as e:
                    # Fallback de segurança caso a API falhe ou não esteja configurada
                    st.session_state.resposta_ai_real = {
                        "conselhos": [
                            "💼 **Preparação Profissional:** Organiza os teus argumentos comerciais antes de falar com qualquer contacto de negócios.",
                            "⏰ **Gestão de Horários:** Garante que defines alarmes com margem suficiente para não chegares atrasado às visitas de manhã."
                        ],
                        "checklist": [
                            "Confirmar a agenda exata dos compromissos",
                            "Validar a documentação necessária para o cliente"
                        ],
                        "alarme_hora": "08:00",
                        "gps_local": "Localização do Imóvel",
                        "pergunta_crm": "O cliente mencionado para amanhã de manhã é um contacto novo (Lead) ou já registado?",
                        "sugestao_lead": "Cliente de Manhã"
                    }
                st.rerun()

    # --- INTERFACE VISUAL GERADA PELA IA REAL ---
    if st.session_state.resposta_ai_real:
        st.divider()
        st.header("🧠 Conselhos Personalizados do Teu Mentor AI")
        
        for conselho in st.session_state.resposta_ai_real["conselhos"]:
            st.write(conselho)
            
        st.subheader("📋 Checklist Gerada pela IA")
        for item in st.session_state.resposta_ai_real["checklist"]:
            st.checkbox(item, value=False)
            
        st.subheader("🚗 Automações de Tempo")
        st.info(f"⏰ Alarme sugerido ajustado automaticamente para as **{st.session_state.resposta_ai_real['alarme_hora']}** devido aos teus compromissos.")
        
        if st.session_state.resposta_ai_real["gps_local"]:
            gps_url = f"https://google.com{st.session_state.resposta_ai_real['gps_local'].replace(' ', '+')}"
            st.markdown(
                f'<a href="{gps_url}" target="_blank">'
                f'<button style="padding:10px; background-color:#1E88E5; color:white; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">'
                f'🗺️ Ligar GPS para {st.session_state.resposta_ai_real["gps_local"]}'
                '</button></a>', unsafe_allow_html=True
            )
            
        # O INTERATIVO REAL: Pergunta dinâmica para preencher o CRM
        if st.session_state.resposta_ai_real["pergunta_crm"]:
            st.divider()
            st.subheader("🤖 Interação com o CRM")
            st.info(st.session_state.resposta_ai_real["pergunta_crm"])
            
            tipo_selecionado = st.radio("Escolha a opção para a base de dados:", ["É uma Nova Lead (Guardar na pasta)", "Já é Cliente Registado"])
            
            if st.button("Confirmar e Injetar na Pasta"):
                if tipo_selecionado == "É uma Nova Lead (Guardar na pasta)":
                    st.session_state.leads.append({
                        "nome": st.session_state.resposta_ai_real["sugestao_lead"],
                        "tipo": "Lead Capturada por AI",
                        "data": time.strftime("%Y-%m-%d")
                    })
                    st.success("📥 Sucesso! O Mentor extraiu o cliente do teu texto e guardou-o na pasta de Leads.")
                else:
                    st.success("✅ Histórico de interações atualizado!")
                st.session_state.resposta_ai_real["pergunta_crm"] = None
                st.rerun()

elif st.session_state.pagina_atual == "Leads & Clientes":
    st.title("👥 Pasta de Leads & Clientes")
    if not st.session_state.leads:
        st.info("A pasta está vazia. Fala com o Mentor em texto livre para ele criar leads automaticamente.")
    else:
        for lead in st.session_state.leads:
            with st.expander(f"👤 {lead['nome']}"):
                st.write(f"📂 **Origem:** {lead['tipo']}")
                st.write(f"📅 **Data de Registo:** {lead['data']}")
            
