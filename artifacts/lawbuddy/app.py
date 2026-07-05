import streamlit as st
import time

# Configuração visual e responsiva para telemóveis
st.set_page_config(
    page_title="StoryVerse Pro — O Teu Destino",
    page_icon="🔮",
    layout="centered"
)

# LINK DO TEU STRIPE CHECKOUT VITALÍCIO (19.99€)
STRIPE_PAYMENT_URL = "https://stripe.com"

# ==============================================================================
# 💾 SISTEMA DE MEMÓRIA PERSISTENTE E INVENTÁRIO (SESSÃO DE JOGO)
# ==============================================================================
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"  # "Free" ou "Pro"
if "genero" not in st.session_state:
    st.session_state.genero = None         # "Homem" ou "Mulher"
if "no_atual" not in st.session_state:
    st.session_state.no_atual = "capitulo_1"
if "mochila" not in st.session_state:
    st.session_state.mochila = []          # Inventário de itens capturados nas rotas

# --- BARRA LATERAL ESTILIZADA ---
with st.sidebar:
    st.markdown("## 🔮 StoryVerse Pro")
    st.caption("Versão 2026 • Entretenimento Vitalício")
    st.divider()
    
    # Exibição visual da Mochila / Inventário do Jogador
    st.markdown("### 🎒 O Teu Inventário")
    if not st.session_state.mochila:
        st.caption("A tua mochila está vazia.")
    else:
        for item in st.session_state.mochila:
            st.markdown(f"• 📦 **{item}**")
            
    st.divider()
    if st.button("🔄 Reiniciar e Apagar Progresso", use_container_width=True):
        st.session_state.no_atual = "capitulo_1"
        st.session_state.genero = None
        st.session_state.mochila = []
        st.rerun()
        
    st.divider()
    st.markdown("### 💳 Estado da Obra")
    if st.session_state.user_status == "Free":
        st.error("Demonstração Gratuita Ativa")
        if st.button("🔓 Forçar Desbloqueio PRO (Teste)"):
            st.session_state.user_status = "Pro"
            st.rerun()
    else:
        st.success("⭐ Licença Vitalícia Ativada")

# ==============================================================================
# 📚 A BASE DE DADOS DA NARRATIVA MASSIVA (RAMIFICAÇÕES COMPLEXAS)
# ==============================================================================
HISTORIA = {
    "capitulo_1": {
        "titulo": "Capítulo 1: O Sussurro do Neo-Porto",
        "imagem": "https://unsplash.com",
        "texto": """A névoa elétrica sobre Neo-Porto nunca dissipa. Sob o brilho dos painéis de néon degradados, tu caminhas com as mãos cravadas nos bolsos do teu sobretudo. O ar cheira a ozono e a metal queimado. 

De repente, o teu terminal holográfico de pulso vibra violentamente. Uma frequência encriptada que não deverias conseguir receber projeta um endereço nas tuas retinas: *Armazém 4, Doca Velha*. Uma voz distorcida ecoa pelo recetor de áudio: 'Eles sabem o que escondes. Se queres sobreviver à noite, mexe-te.'

A tua mente viaja instantaneamente para os segredos do teu passado. Cada decisão a partir de agora ditará se vês o amanhecer nesta cidade cruel.""",
        "opcoes": [
            {"texto": "🚨 [Ação] Correr em direção à Doca Velha imediatamente.", "proximo_no": "doca_velha", "item_ganho": None},
            {"texto": "🕵️‍♂️ [Prudência] Investigar a origem do sinal e roubar o chip de dados do beco.", "proximo_no": "investigar_sinal", "item_ganho": "Chip de Dados Encriptado"},
            {"texto": "👥 [Contactos] Ligar para um aliado do submundo e armar-te.", "proximo_no": "chamar_aliado", "item_ganho": "Pistola Laser Compacta"}
        ]
    },
    
    "doca_velha": {
        "titulo": "Capítulo 1: A Rota de Colisão",
        "imagem": "https://unsplash.com",
        "texto": """A adrenalina dispara. Os teus passos ecoam no chão molhado enquanto corres pelas ruelas industriais. Ao aproximares-te do Armazém 4, notas três silhuetas estáticas nas sombras, vigiando a entrada principal com armas táticas de curto alcance. 

Entrar pela frente é suicídio, mas a voz no terminal disse que estavas a ficar sem tempo. O teu instinto avisa-te de que este é o ponto de não retorno.""",
        "opcoes": [
            {"texto": "🎯 Procurar uma entrada secundária pelas condutas de ventilação.", "proximo_no": "bloqueio_paywall", "item_ganho": None},
            {"texto": "💥 Avançar diretamente e tentar neutralizar os guardas.", "proximo_no": "bloqueio_paywall", "item_ganho": None}
        ]
    },

    "investigar_sinal": {
        "titulo": "Capítulo 1: Linhas de Código",
        "imagem": "https://unsplash.com",
        "texto": """Recusas-te a ser uma marioneta. Encostas-te à parede escura do beco e abres a consola de depuração do teu terminal. Os teus dedos voam sobre o teclado virtual, intercetando os pacotes de dados da chamada. 

Consegues extrair um dispositivo físico escondido na caixa de fusíveis do beco. Tens agora um Chip de Dados Encriptado na tua mochila! O rastreio aponta para uma localização impossível: os servidores centrais da Corporação Apex. Alguém de muito alto cargo está a jogar contigo.""",
        "opcoes": [
            {"texto": "💻 Tentar quebrar a encriptação do chip aqui mesmo.", "proximo_no": "bloqueio_paywall", "item_ganho": None},
            {"texto": "🏃‍♂️ Guardar o segredo e fugir a pé da cidade antes que te localizem.", "proximo_no": "bloqueio_paywall", "item_ganho": None}
        ]
    },

    "chamar_aliado": {
        "titulo": "Capítulo 1: Dívidas de Sangue",
        "imagem": "https://unsplash.com",
        "texto": """Inicias uma chamada de alta segurança para Vance, um ex-mercenário que te deve a vida. Ele atende do interior de um jipe blindado e lança-te um objeto pesado antes de arrancar: uma Pistola Laser Compacta.

'Estás louco por andar na rua desarmado?', rosna Vance. 'A cidade está bloqueada. Há caçadores de prémios com a tua fotografia em todos os distritos. Vai para o armazém, mas não confies em ninguém.'""",
        "opcoes": [
            {"texto": "🤝 Entrar no armazém de arma em punho, pronto para disparar.", "proximo_no": "bloqueio_paywall", "item_ganho": None},
            {"texto": "🤫 Ocultar a pistola no sobretudo e entrar fingindo rendição.", "proximo_no": "bloqueio_paywall", "item_ganho": None}
        ]
    }
}

# ==============================================================================
# 🎮 RENDEREZAR O JOGO INTERATIVO
# ==============================================================================

# Passo 1: Criação da Personagem
if st.session_state.genero is None:
    st.title("✨ Escolha do Protagonista")
    st.write("Configura o perfil da tua personagem para alinhar os diálogos e pronomes da história:")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🙋‍♂️ Protagonista Masculino", use_container_width=True):
            st.session_state.genero = "Homem"
            st.rerun()
    with c2:
        if st.button("🙋‍♀️ Protagonista Feminina", use_container_width=True):
            st.session_state.genero = "Mulher"
            st.rerun()

# Passo 2: O Fluxo Dinâmico
else:
    no = st.session_state.no_atual
    
    # CONTROLO DE ACESSO: MURO DE PAGAMENTO (PAYWALL)
    if no == "bloqueio_paywall" and st.session_state.user_status == "Free":
        st.title("🔒 Destino Interrompido...")
        st.image("https://unsplash.com", use_container_width=True)
        st.warning("O Capítulo 1 Gratuito terminou! As tuas escolhas e o teu inventário foram salvos com sucesso.")
        
        st.write(
            "Entraste profundamente na conspiração de Neo-Porto. O rumo que escolheste gerou uma linha "
            "temporal única baseada nas tuas decisões. Para continuares esta jornada massiva que dura vários dias, "
            "desbloqueares os restantes capítulos e descobrires as dezenas de finais alternativos, adquire a tua licença vitalícia."
        )
        
        # Botão Oficial de Vendas do Stripe Checkout de 19.99€
        st.markdown(
            f'<a href="{STRIPE_PAYMENT_URL}" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #ff4b4b; color: white; text-align: center; '
            'padding: 16px; border-radius: 8px; font-weight: bold; font-size: 18px; cursor: pointer; '
            'box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4); margin-top: 15px;">'
            '🚀 COMPRAR ACESSO COMPLETO PARA SEMPRE (19.99€)'
            '</div></a>', 
            unsafe_allow_html=True
        )
        st.caption("Pagamento único. O livro digital é teu para sempre, sem mensalidades.")
        
    else:
        # Se for Pro e bater no paywall, a história continua para o Capítulo 2 Real
        if no == "bloqueio_paywall" and st.session_state.user_status == "Pro":
            st.title("🚀 Capítulo 2: A Teia de Neo-Porto")
            st.image("https://unsplash.com", use_container_width=True)
            st.write("Conseguiste entrar no Armazém 4. A tua licença ProVitalícia está ativa!")
            
            # EXEMPLO DA COMPLEXIDADE: O jogo reage de acordo com o inventário do Capítulo 1!
            if "Pistola Laser Compacta" in st.session_state.mochila:
                st.info("⚔️ **Ramificação de Combate Ativa:** Sentes o peso da Pistola Laser no teu sobretudo. Estás pronto para o pior.")
                if st.button("Disparar contra as luzes do armazém para criar pânico", use_container_width=True):
                    st.write("A história continuaria por aqui...")
            elif "Chip de Dados Encriptado" in st.session_state.mochila:
                st.info("💻 **Ramificação de Espionagem Ativa:** Tens o Chip da Corporação Apex. Se encontrares um terminal, podes expor os segredos deles.")
    
