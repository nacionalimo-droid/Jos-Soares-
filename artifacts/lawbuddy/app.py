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
# 💾 ESTADO DE JOGO AND MEMÓRIA PERSISTENTE
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
# 🎮 INTERFACE E FLUXO DA HISTÓRIA (ESTRUTURA LINEAR SEM LOOPS)
# ==============================================================================

# --- TELA 1: A CAPA DO LIVRO (A HOME PRINCIPAL) ---
if st.session_state.no_atual == "capa":
    st.markdown("<h1 style='text-align: center;'>🌹 A Rosa Branca de Sintra</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #bdc3c7;'>Um Romance Interativo de Mistério e Segredos Cruzados</p>", unsafe_allow_html=True)
    
    st.image("https://unsplash.com", caption="Edição Especial Vitalícia — Pro Gaming", use_container_width=True)
    
    st.write(
        "Mergulha numa narrativa épica de suspense e paixão nas encostas enigmáticas de Sintra. "
        "As decisões que fores tomando ao longo dos capítulos vão ditar as dezenas de desfechos possíveis desta história. "
        "O teu destino começa agora."
    )
    st.divider()
    
    st.write("### 👥 Escolhe o teu Protagonista:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🙋‍♂️ Protagonista Masculino", use_container_width=True):
            st.session_state.genero = "Homem"
            st.session_state.no_atual = "p1_inicio"
            st.rerun()
    with col2:
        if st.button("🙋‍♀️ Protagonista Feminina", use_container_width=True):
            st.session_state.genero = "Mulher"
            st.session_state.no_atual = "p1_inicio"
            st.rerun()

# --- TELA 2: PÁGINA 1 DA HISTÓRIA ---
elif st.session_state.no_atual == "p1_inicio":
    st.title("O Nevoeiro da Serra")
    st.image("https://unsplash.com", use_container_width=True)
    
    pronome = "O" if st.session_state.genero == "Homem" else "A"
    st.write(
        f"A serra de Sintra erguia-se como um titã de pedra envolto em mistério. O nevoeiro denso e gélido descia pelas encostas, engolindo os palácios antigos e as ruelas estreitas. {pronome} protagonista caminhava em silêncio, tentando fugir do peso do passado e dos segredos que consumiam a alma.\n\n"
        "Ao passares pelos portões de ferro forjado de uma propriedade abandonada, algo invulgar capturou o teu olhar. No meio da vegetação selvagem e morta, brilhava uma única rosa branca perfeita, imaculada, intocada pelo inverno. Mas o mais perturbador não era a flor... era a figura misteriosa que estava ajoelhada ao lado dela.\n\n"
        "A pessoa ergueu-se lentamente. Os vossos olhares cruzaram-se através da bruma. Havia uma tristeza profunda e magnética naqueles olhos, misturada com um segredo terrível que parecia ligar-se diretamente à tua própria história."
    )
    st.divider()
    st.write("### 🔥 Qual será a tua reação emocional?")
    
    if st.button("❤️ [Romantismo] Aproximar-te com suavidade, oferecer o teu lenço e falar com calma.", use_container_width=True):
        st.session_state.romantismo += 3
        st.session_state.no_atual = "p2_romance"
        st.rerun()
    if st.button("🕵️‍♂️ [Mistério] Manter a distância, mas exigir saber o que aquela rosa significa.", use_container_width=True):
        st.session_state.audacia += 3
        st.session_state.no_atual = "p2_misterio"
        st.rerun()
    if st.button("🏃‍♂️ [Prudência] Recuar discretamente para a estrada antes que se torne perigosa.", use_container_width=True):
        st.session_state.no_atual = "p2_fuga"
        st.rerun()

# --- TELA 3: ROTA DO ROMANCE (PÁGINA 2A) ---
elif st.session_state.no_atual == "p2_romance":
    st.title("Um Toque na Bruma")
    st.image("https://unsplash.com", use_container_width=True)
    
    st.write(
        "Os teus passos suaves na gravilha não assustaram a figura. Ao aproximares-te, estendes o lenço. A pessoa hesita por um segundo eterno, mas aceita. Os vossos dedos tocam-se e um choque elétrico de emoção cruza o teu corpo.\n\n"
        "'Obrigado...', murmura com uma voz melancólica que faz o teu coração acelerar. 'Poucos se atrevem a entrar no jardim da Quinta das Lágrimas. Esta rosa... ela floresce com o sangue de uma promessa quebrada.'\n\n"
        "De repente, ouve-se um estalar de ramos secos vindo do interior do palacete abandonado. Alguém ou algo está a observar-vos intensamente de uma das janelas partidas do andar superior. A emoção dá lugar ao puro suspense."
    )
    st.divider()
    st.write("### 🔥 Como decides agir agora?")
    
    if st.button("🌹 Proteger a pessoa com o teu corpo e olhar fixamente para a janela.", use_container_width=True):
        st.session_state.romantismo += 2
        st.session_state.no_atual = "paywall_bloqueio"
        st.rerun()
    if st.button("🤝 Pegar na mão da pessoa e sugerir fugirem dali juntos imediatamente.", use_container_width=True):
        st.session_state.audacia += 2
        st.session_state.no_atual = "paywall_bloqueio"
        st.rerun()

# --- TELA 4: ROTA DO MISTÉRIO (PÁGINA 2B) ---
elif st.session_state.no_atual == "p2_misterio":
    st.title("Confronto na Quinta")
    st.image("https://unsplash.com", use_container_width=True)
    
    st.write(
        "A tua voz firme corta o silêncio da serra. A figura recua um passo, surpreendida com a tua audácia. Um sorriso enigmático e amargo surge nos seus lábios frios.\n\n"
        "'As perguntas certas no lugar errado trazem consequências devastadoras', responde. A pessoa afasta a capa preta, revelando que segura um diário antigo com o brasão de armas da tua própria família gravado a ouro na capa de couro.\n\n"
        "O teu sangue gela. Como é que aquele desconhecido tem o diário perdido do teu avô? Antes que possas avançar, um canídeo de grande porte surge de entre os arbustos, rosnando agressivamente na tua direção."
    )
    st.divider()
    st.write("### 🔥 Como decides agir agora?")
    
    if st.button("⚔️ Enfrentar o perigo, agarrar num ramo pesado e defender a tua posição.", use_container_width=True):
        st.session_state.audacia += 3
        st.session_state.no_atual = "paywall_bloqueio"
        st.rerun()
    if st.button("🗣️ Tentar acalmar o animal falando com voz mansa e calma.", use_container_width=True):
        st.session_state.romantismo += 1
        st.session_state.no_atual = "paywall_bloqueio"
        st.rerun()

# --- TELA 5: ROTA DA FUGA (PÁGINA 2C) ---
elif st.session_state.no_atual == "p2_fuga":
    st.title("A Sombra que Persegue")
    st.image("https://unsplash.com", use_container_width=True)
    
    st.write(
        "O teu instinto de sobrevivência fala mais alto. Viras as costas e caminhas apressadamente em direção aos portões de ferro. No entanto, Sintra não liberta os seus eleitos tão facilmente.\n\n"
        "O nevoeiro adensa-se ao ponto de não conseguires ver os teus próprios pés. Passos pesados começam a ecoar mesmo atrás de ti, acompanhados pelo som metálico de correntes a arrastarem-se no asfalto. Olhas para trás e a estrada desapareceu. Estás de volta ao centro do jardim da propriedade abandonada, mas a figura misteriosa sumiu. No chão, resta apenas a rosa branca... agora manchada com gotas frescas de sangue."
    )
    st.divider()
    st.write("### 🔥 Como decides agir agora?")
    
    if st.button("🩸 Apanhar a rosa ensanguentada do chão para decifrar o mistério.", use_container_width=True):
        st.session_state.audacia += 2
        st.session_state.no_atual = "paywall_bloqueio"
        st.rerun()
    if st.button("🏛️ Correr desesperadamente em direção à porta principal do palacete.", use_container_width=True):
        st.session_state.no_atual = "paywall_bloqueio"
        st.rerun()

# --- TELA 6: O MURO DE PAGAMENTO (PAYWALL BLOQUEIO) ---
elif st.session_state.no_atual == "paywall_bloqueio":
    
    if st.session_state.user_status == "Free":
        st.markdown("<h1 style='text-align: center;'>🔒 Fim do Capítulo Gratuito</h1>", unsafe_allow_html=True)
        st.image("https://unsplash.com", use_container_width=True)

                
