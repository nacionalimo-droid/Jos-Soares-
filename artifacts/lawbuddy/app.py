import streamlit as st

# Configuração focada no modo de leitura limpo e imersivo (UI Premium)
st.set_page_config(
    page_title="StoryVerse Pro — Livros Interativos",
    page_icon="🌹",
    layout="centered"
)

# LINK DE PAGAMENTO STRIPE REAL (19.99€ VITALÍCIO)
STRIPE_PAYMENT_URL = "https://stripe.com"

# ==============================================================================
# 💾 MOTOR MATEMÁTICO: GESTÃO DE ESTADOS E CONTADOR INVISÍVEL
# ==============================================================================
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"       # "Free" ou "Pro"
if "genero" not in st.session_state:
    st.session_state.genero = None              # "Homem" ou "Mulher"
if "no_atual" not in st.session_state:
    st.session_state.no_atual = "capa"          # Nó invisível de controlo
if "passos_lidos" not in st.session_state:
    st.session_state.passos_lidos = 0           # Contador cego de páginas lidas
if "personalidade" not in st.session_state:
    st.session_state.personalidade = {
        "romance": 0, "misterio": 0, "audacia": 0
    }

# --- BARRA LATERAL ADMINISTRATIVA (Invisível ou Ocultável pelo utilizador) ---
with st.sidebar:
    st.markdown("### ⚙️ Painel do Game-Book")
    if st.button("🔄 Reiniciar História", use_container_width=True):
        st.session_state.no_atual = "capa"
        st.session_state.genero = None
        st.session_state.passos_lidos = 0
        st.session_state.personalidade = {"romance": 0, "misterio": 0, "audacia": 0}
        st.rerun()
    st.divider()
    st.markdown("### 📊 Estatísticas Ocultas")
    st.write(f"Páginas lidas nesta sessão: **{st.session_state.passos_lidos}**")
    if st.session_state.user_status == "Free":
        st.error("Acesso Gratuito Ativo")
        if st.button("🔓 Simular Licença Pro (Pós-Stripe)"):
            st.session_state.user_status = "Pro"
            st.rerun()
    else:
        st.success("⭐ Licença Vitalícia Ativa")

# ==============================================================================
# 🌹 A ÁRVORE NARRATIVA MASSIVA: "A ROSA BRANCA DE SINTRA"
# ==============================================================================
# Arquitetura matricial cega que ramifica e converge com base na matemática de escolhas.
HISTORIA = {
    "p1_inicio": {
        "titulo": "🌹 A Rosa Branca de Sintra",
        "imagem": "https://unsplash.com",
        "texto": """A serra de Sintra erguia-se como um titã de pedra envolto em mistério. O nevoeiro gélido e denso descia pelas encostas, engolindo os palácios antigos e as ruelas estreitas. Tu caminhavas em silêncio, tentando fugir do peso do teu passado e dos segredos que te consumiam a alma.

Ao passares pelos portões de ferro forjado de uma propriedade abandonada, algo invulgar capturou o teu olhar. No meio da vegetação selvagem e morta, brilhava uma única rosa branca perfeita, imaculada, intocada pelo inverno. Mas o mais perturbador não era a flor... era a figura misteriosa que estava ajoelhada ao lado dela.

A pessoa ergueu-se lentamente. Os vossos olhares cruzaram-se através da bruma. Havia uma tristeza profunda e magnética naqueles olhos, misturada com um segredo terrível que parecia ligar-se diretamente à tua própria história.""",
        "opcoes": [
            {"texto": "❤️ Aproximar-te com suavidade, oferecer o teu lenço e tentar acalmá-la.", "proximo": "p2_romance", "atrib": "romance"},
            {"texto": "🕵️‍♂️ Manter a distância, mas exigir saber o que aquela rosa significa.", "proximo": "p2_misterio", "atrib": "misterio"},
            {"texto": "🏃‍♂️ Recuar discretamente para a estrada antes que o perigo aumente.", "proximo": "p2_fuga", "atrib": "audacia"}
        ]
    },

    # --- NÍVEL 2 (PÁGINAS GRÁTIS CONTABILIZADAS) ---
    "p2_romance": {
        "titulo": "O Toque na Bruma",
        "imagem": "https://unsplash.com",
        "texto": """Os teus passos suaves na gravilha não assustaram a figura. Ao aproximares-te, estendes o lenço. A pessoa hesita por um segundo eterno, mas aceita. Os vossos dedos tocam-se e um choque elétrico de emoção cruza o teu corpo.

'Obrigado...', murmura com uma voz melancólica. 'Poucos se atrevem a entrar no jardim da Quinta das Lágrimas. Esta rosa... ela floresce com o sangue de uma promessa antiga.'

De repente, ouve-se um estalar de ramos secos vindo do interior do palacete abandonado. Alguém ou algo está a observar-vos intensamente de uma das janelas partidas do andar superior. O suspense aperta o teu peito.""",
        "opcoes": [
            {"texto": "🌹 Colocar-te à frente da pessoa para a proteger do desconhecido.", "proximo": "p3_confronto", "atrib": "romance"},
            {"texto": "🤝 Agarrar na mão dela e correrem juntos em direção ao bosque.", "proximo": "p3_fuga_floresta", "atrib": "audacia"},
            {"texto": "🤫 Sussurrar para manterem o silêncio e agacharem-se na estátua.", "proximo": "p3_emboscada", "atrib": "misterio"}
        ]
    },
    "p2_misterio": {
        "titulo": "Confronto na Quinta",
        "imagem": "https://unsplash.com",
        "texto": """A tua voz firme corta o silêncio da serra. A figura recua um passo, surpreendida com a tua audácia. Um sorriso enigmático e amargo surge nos seus lábios frios.

'As perguntas certas no lugar errado trazem consequências devastadoras', responde. A pessoa afasta a capa preta, revelando que segura um diário antigo com o brasão de armas da tua própria família gravado a ouro na capa de couro.

O teu sangue gela. Como é que aquele desconhecido tem o diário perdido do teu avô? Antes que possas avançar, um rosnado agressivo ecoa vindo de trás das sebes mortas.""",
        "opcoes": [
            {"texto": "⚔️ Avançar com firmeza e exigir o diário de volta imediatamente.", "proximo": "p3_confronto", "atrib": "audacia"},
            {"texto": "🧐 Recuar um passo e tentar negociar uma troca pacífica.", "proximo": "p3_emboscada", "atrib": "misterio"},
            {"texto": "📱 Retirar o teu telemóvel para fotografar o brasão e a cara do sujeito.", "proximo": "p3_fuga_floresta", "atrib": "misterio"}
        ]
    },
    "p2_fuga": {
        "titulo": "A Sombra Intermitente",
        "imagem": "https://unsplash.com",
        "texto": """O teu instinto de sobrevivência fala mais alto. Viras as costas e caminhas apressadamente em direção aos portões de ferro. No entanto, Sintra não liberta os seus eleitos tão facilmente.

O nevoeiro adensa-se ao ponto de não conseguires ver os teus próprios passos. Sons rítmicos de correntes a arrastarem-se no asfalto ecoam mesmo atrás de ti. Olhas para trás e a estrada desapareceu por completo. Estás, inexplicavelmente, de volta ao centro do jardim da propriedade abandonada. A figura sumiu, mas a rosa branca está no chão, banhada em sangue quente.""",
        "opcoes": [
            {"texto": "🩸 Apanhar a rosa do chão para procurar vestígios ou pistas.", "proximo": "p3_emboscada", "atrib": "misterio"},
            {"texto": "🏛️ Arrombar a porta do palacete abandonado para te esconderes lá dentro.", "proximo": "p3_confronto", "atrib": "audacia"},
            {"texto": "🔊 Gritar por socorro na bruma profunda, quebrando o silêncio da noite.", "proximo": "p3_fuga_floresta", "atrib": "romance"}
        ]
    },

    # --- NÍVEL 3 (O ÚLTIMO NÓ DO ACESSO GRATUITO) ---
    "p3_confronto": {
        "titulo": "O Despertar do Passado",
        "imagem": "https://unsplash.com",
        "texto": """A tensão atinge o ponto de rutura. A porta do palacete abre-se com um rangido violento e duas sombras projetam feixes de luz diretamente sobre ti. O desconhecido agarra no teu braço com uma força surpreendente e sussurra: 'O tempo acabou. Se eles apanharem o manuscrito que está na rosa, a tua linhagem morre hoje.'

Passos rápidos e metálicos aproximam-se. Estás encurralado entre um segredo de família e homens armados que sabem exatamente quem tu és.""",
        "opcoes": [
            {"texto": "➡️ Avançar na escuridão...", "proximo": "paywall_bloqueio", "atrib": "audacia"},
            {"texto": "➡️ Ouvir o sussurro da bruma...", "proximo": "paywall_bloqueio", "atrib": "romance"},
            {"texto": "➡️ Revelar o diário oculto...", "proximo": "paywall_bloqueio", "atrib": "misterio"}
        ]
    },
    "p3_fuga_floresta": {
        "titulo": "O Labirinto Verde",
        "imagem": "https://unsplash.com",
        "texto": """Corres desorientadamente entre as árvores centenárias de Sintra. Os ramos rasgam as tuas roupas e o chão lamacento faz-te escorregar. Atrás de ti, o som das correntes e de vozes distorcidas por rádios comunicadores indica que a caça começou.

À tua frente, a floresta abre-se num abismo ou numa entrada secreta para uma capela subterrânea em ruínas. Não há tempo para hesitar.""",
        "opcoes": [
            {"texto": "➡️ Saltar para o interior da capela...", "proximo": "paywall_bloqueio", "atrib": "misterio"},
            {"texto": "➡️ Tentar contornar o abismo nas sombras...", "proximo": "paywall_bloqueio", "atrib": "audacia"},
            {"texto": "➡️ Esperar o teu perseguidor de armas na mão...", "proximo": "paywall_bloqueio", "atrib": "romance"}
        ]
    },
    "p3_emboscada": {
        "titulo": "O Silêncio dos Culpados",
        "imagem": "https://unsplash.com",
        "texto": """Escondido atrás do pedestal de pedra, controlas a tua respiração fria. Podes ver as luzes das lanternas a passar a milímetros de distância. O desconhecido está ao teu lado, o coração dele bate num ritmo frenético que consegues ouvir.

