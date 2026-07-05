import streamlit as st

# Configuração de ecrã focada na imersão da leitura
st.set_page_config(
    page_title="A Rosa Branca de Sintra — Livro Interativo",
    page_icon="🌹",
    layout="centered"
)

# LINK DE PAGAMENTO STRIPE REAL (19.99€ VITALÍCIO)
STRIPE_PAYMENT_URL = "https://stripe.com"

# ==============================================================================
# 💾 ESTADO DE JOGO E MEMÓRIA PERSISTENTE
# ==============================================================================
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"  # "Free" ou "Pro"
if "genero" not in st.session_state:
    st.session_state.genero = None         # "Homem" ou "Mulher"
if "no_atual" not in st.session_state:
    st.session_state.no_atual = "capa"     # Começa na capa do livro
if "romantismo" not in st.session_state:
    st.session_state.romantismo = 0        # Pontuação oculta
if "audacia" not in st.session_state:
    st.session_state.audacia = 0           # Pontuação oculta

# --- BARRA LATERAL: CONTROLOS DO LEITOR ---
with st.sidebar:
    st.markdown("### 📖 Menu do Leitor")
    if st.button("🔄 Reiniciar Livro", use_container_width=True):
        st.session_state.no_atual = "capa"
        st.session_state.genero = None
        st.session_state.romantismo = 0
        st.session_state.audacia = 0
        st.rerun()
    st.divider()
    st.markdown("### 💳 Licença da Obra")
    if st.session_state.user_status == "Free":
        st.error("Acesso Gratuito: Cap. 1")
        if st.button("🔓 Simular Ativação PRO"):
            st.session_state.user_status = "Pro"
            st.rerun()
    else:
        st.success("⭐ Proprietário Vitalício")

# ==============================================================================
# 🌹 NARRATIVA COMPLEXA ESCRITA: "A ROSA BRANCA DE SINTRA"
# ==============================================================================
# Toda a árvore de decisões já inventada, encadeada e escrita por extenso.
HISTORIA = {
    "capitulo_1_inicio": {
        "titulo": "Capítulo 1: O Nevoeiro da Serra",
        "imagem": "https://unsplash.com",
        "texto": """A serra de Sintra erguia-se como um titã de pedra envolto em mistério. O nevoeiro denso e gélido descia pelas encostas, engolindo os palácios antigos e as ruelas estreitas. Tu caminhavas em silêncio, tentando fugir do peso do teu passado e dos segredos que te consumiam a alma. 

Ao passares pelos portões de ferro forjado de uma propriedade abandonada, algo invulgar capturou o teu olhar. No meio da vegetação selvagem e morta, brilhava uma única rosa branca perfeita, imaculada, intocada pelo inverno. Mas o mais perturbador não era a flor... era a figura misteriosa que estava ajoelhada ao lado dela. 

A pessoa ergueu-se lentamente. Os vossos olhares cruzaram-se através da bruma. Havia uma tristeza profunda e magnética naqueles olhos, misturada com um segredo terrível que parecia ligar-se diretamente à tua própria história.""",
        "opcoes": [
            {"texto": "❤️ [Romantismo] Aproximar-te com suavidade, oferecer o teu lenço e dizer algo reconfortante.", "proximo_no": "rota_romantica", "add_rom": 3, "add_aud": 0},
            {"texto": "🕵️‍♂️ [Mistério] Manter a distância, mas exigir saber o que aquela rosa significa e quem é ele/ela.", "proximo_no": "rota_misterio", "add_rom": 0, "add_aud": 3},
            {"texto": "🏃‍♂️ [Prudência] Recuar discretamente para a estrada antes que a situação se torne perigosa.", "proximo_no": "rota_fuga", "add_rom": 0, "add_aud": -1}
        ]
    },

    # --- RAMIFICAÇÃO 1: ROTA ROMÂNTICA ---
    "rota_romantica": {
        "titulo": "Capítulo 1: Um Toque na Bruma",
        "imagem": "https://unsplash.com",
        "texto": """Os teus passos suaves na gravilha não assustaram a figura. Ao aproximares-te, estendes o lenço. A pessoa hesita por um segundo eterno, mas aceita. Os vossos dedos tocam-se e um choque elétrico de emoção cruza o teu corpo. 

'Obrigado...', murmura com uma voz melancólica que faz o teu coração acelerar. 'Poucos se atrevem a entrar no jardim da Quinta das Lágrimas. Esta rosa... ela floresce com o sangue de uma promessa quebrada.' 

De repente, ouve-se um estalar de ramos secos vindo do interior do palacete abandonado. Alguém ou algo está a observar-vos intensamente de uma das janelas partidas do andar superior. A emoção dá lugar ao puro suspense.""",
        "opcoes": [
            {"texto": "🌹 Proteger a pessoa com o teu corpo e olhar fixamente para a janela.", "proximo_no": "paywall_bloqueio"},
            {"texto": "🤝 Pegar na mão da pessoa e sugerir fugirem dali juntos imediatamente.", "proximo_no": "paywall_bloqueio"},
            {"texto": "🤫 Sussurrar para manterem o silêncio e esconderem-se atrás das estátuas de pedra.", "proximo_no": "paywall_bloqueio"}
        ]
    },

    # --- RAMIFICAÇÃO 2: ROTA MISTÉRIO ---
    "rota_misterio": {
        "titulo": "Capítulo 1: Confronto na Quinta",
        "imagem": "https://unsplash.com",
        "texto": """A tua voz firme corta o silêncio da serra. A figura recua um passo, surpreendida com a tua audácia. Um sorriso enigmático e amargo surge nos seus lábios frios. 

'As perguntas certas no lugar errado trazem consequências devastadoras', responde. A pessoa afasta a capa preta, revelando que segura um diário antigo com o brasão de armas da tua própria família gravado a ouro na capa de couro. 

O teu sangue gela. Como é que aquele desconhecido tem o diário perdido do teu avô? Antes que possas avançar, um canídeo de grande porte surge de entre os arbustos, rosnando agressivamente na tua direção.""",
        "opcoes": [
            {"texto": "⚔️ Enfrentar o perigo, agarrar num ramo pesado e defender a tua posição.", "proximo_no": "paywall_bloqueio"},
            {"texto": "🗣️ Tentar acalmar o animal falando com voz mansa e sem movimentos bruscos.", "proximo_no": "paywall_bloqueio"},
            {"texto": "👁️ Olhar nos olhos do desconhecido e exigir que ele controle o animal.", "proximo_no": "paywall_bloqueio"}
        ]
    },

    # --- RAMIFICAÇÃO 3: ROTA FUGA ---
    "rota_fuga": {
        "titulo": "Capítulo 1: A Sombra que Persegue",
        "imagem": "https://unsplash.com",
        "texto": """O teu instinto de sobrevivência fala mais alto. Viras as costas e caminhas apressadamente em direção aos portões de ferro. No entanto, Sintra não liberta os seus eleitos tão facilmente. 

O nevoeiro adensa-se ao ponto de não conseguires ver os teus próprios pés. Passos pesados começam a ecoar mesmo atrás de ti, acompanhados pelo som metálico de correntes a arrastarem-se no asfalto. Olhas para trás e a estrada desapareceu. Estás de volta ao centro do jardim da propriedade abandonada, mas a figura misteriosa sumiu. No chão, resta apenas a rosa branca... agora manchada com gotas frescas de sangue.""",
        "opcoes": [
            {"texto": "🩸 Apanhar a rosa ensanguentada do chão para decifrar o mistério.", "proximo_no": "paywall_bloqueio"},
            {"texto": "🏛️ Correr desesperadamente em direção à porta principal do palacete para te abrigares.", "proximo_no": "paywall_bloqueio"},
            {"texto": "🔊 Gritar por ajuda na bruma profunda, esperando que alguém ouça.", "proximo_no": "paywall_bloqueio"}
        ]
    }
}

# ==============================================================================
# 🎮 INTERFACE E EXECUÇÃO DO LIVRO JOGO
# ==============================================================================

# --- TELA 1: A CAPA DO LIVRO (A HOME PRINCIPAL) ---
if st.session_state.no_atual == "capa":
    st.markdown("<h1 style='text-align: center; color: #fdfefe;'>🌹 A Rosa Branca de Sintra</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #bdc3c7;'>Um Romance Interativo de Mistério e Segredos Cruzados</p>", unsafe_allow_html=True)
    
    # Capa bonita inspirada no título
    st.image("https://unsplash.com", caption="Edição Especial Vitalícia — Pro Gaming", use_container_width=True)
    
    st.write(
        "Mergulha numa narrativa épica de suspense e paixão nas encostas enigmáticas de Sintra. "
        "As decisões que tomares ao longo dos capítulos vão ditar as dezenas de desfechos possíveis desta história. "
        "O teu destino começa agora."
    )
    st.divider()
    
    st.write("### 👥 Escolhe o teu Protagonista:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🙋‍♂️ Protagonista Masculino", use_container_width=True):
            st.session_state.genero = "Homem"
            st.session_state.no_atual = "capitulo_1_inicio"
            st.rerun()
    with col2:
        if st.button("🙋‍♀️ Protagonista Feminina", use_container_width=True):
            st.session_state.genero = "Mulher"
            st.session_state.no_atual = "capitulo_1_inicio"
            st.rerun()

# --- TELA 2: FLUXO DE LEITURA E DECISÕES (DINÂMICO) ---
else:
    no = st.session_state.no_atual
    
    # TRATAMENTO DO MURO DE PAGAMENTO (PAYWALL ANTI-BATOTA)
    if no == "paywall_bloqueio" and st.session_state.user_status == "Free":
        st.markdown("<h1 style='text-align: center;'>🔒 Fim do Capítulo Gratuito</h1>", unsafe_allow_html=True)
        st.image("https://unsplash.com", use_container_width=True)
        
        st.warning("O clímax do Capítulo 1 foi atingido! O teu progresso emocional foi salvo.")
        st.write(
            "Descobriste os primeiros segredos da Quinta das Lágrimas e a tua personalidade começou a moldar "
            "o rumo dos acontecimentos. No entanto, para entrares no **Capítulo 2: Os Segredos do Diário** e "
