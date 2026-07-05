import streamlit as st

# Configuração focada no modo de leitura longo
st.set_page_config(
    page_title="O Último Manuscrito de Coimbra",
    page_icon="📜",
    layout="centered"
)

# LINK DE PAGAMENTO STRIPE REAL (19.99€ VITALÍCIO)
STRIPE_PAYMENT_URL = "https://stripe.com"

# --- SISTEMA DE NAVEGAÇÃO LINEAR ANTI-ERRO ---
if "user_status" not in st.session_state:
    st.session_state.user_status = "Free"
if "genero" not in st.session_state:
    st.session_state.genero = None
if "pagina" not in st.session_state:
    st.session_state.pagina = 0  # Controla em que página da história o leitor está
if "linha_temporal" not in st.session_state:
    st.session_state.linha_temporal = "Neutro"

# Imagens imersivas de alta resolução
IMG_CAPA = "https://unsplash.com"
IMG_BIBLIOTECA = "https://unsplash.com"
IMG_PERIGO = "https://unsplash.com"

# --- BARRA LATERAL ---
with st.sidebar:
    st.markdown("### 📜 Opções da Conta")
    if st.button("🔄 Recomeçar do Início", use_container_width=True):
        st.session_state.pagina = 0
        st.session_state.genero = None
        st.session_state.linha_temporal = "Neutro"
        st.rerun()
    st.divider()
    if st.session_state.user_status == "Free":
        st.error("Demonstração Limitada")
        if st.button("🔓 Desbloqueio Pro (Teste)"):
            st.session_state.user_status = "Pro"
            st.rerun()
    else:
        st.success("⭐ Licença Vitalícia Ativa")

# ==============================================================================
# PAGINA 0: A CAPA DO LIVRO (HOME)
# ==============================================================================
if st.session_state.pagina == 0:
    st.markdown("<h1 style='text-align: center;'>📜 O Último Manuscrito de Coimbra</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic;'>Uma Obra Épica de Suspense e Conspiração Histórica</p>", unsafe_allow_html=True)
    st.image(IMG_CAPA, use_container_width=True)
    st.write(
        "Bem-vindo a uma narrativa massiva com centenas de desdobramentos. Estás prestes a entrar "
        "nos corredores escuros da Biblioteca Joanina, onde um segredo com mais de quinhentos anos "
        "ameaça reescrever a história da humanidade. Cada decisão moldará o teu destino definitivo."
    )
    st.divider()
    st.write("### 👥 Escolhe o perfil da tua personagem para iniciar:")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🙋‍♂️ Protagonista Masculino", use_container_width=True):
            st.session_state.genero = "Homem"
            st.session_state.pagina = 1
            st.rerun()
    with c2:
        if st.button("🙋‍♀️ Protagonista Feminina", use_container_width=True):
            st.session_state.genero = "Mulher"
            st.session_state.pagina = 1
            st.rerun()

# ==============================================================================
# PAGINA 1: INTRODUÇÃO DENSA (PÁGINA LITERÁRIA 1)
# ==============================================================================
elif st.session_state.pagina == 1:
    st.title("Página 1: A Cripta de Carvalho")
    st.image(IMG_BIBLIOTECA, use_container_width=True)
    
    pronome = "O" if st.session_state.genero == "Homem" else "A"
    st.write(
        f"{pronome} jovem investigador caminhava com passos ecoantes sob os tetos afrescados da "
        "Velha Universidade. O relógio da torre badalou a meia-noite, um som pesado que vibrou no peito. "
        "Tinham-te prometido que o acesso ao arquivo proibido seria privado, mas o cheiro a cera de abelha "
        "e pergaminho antigo parecia carregar uma presença sufocante.\n\n"
        "Nas tuas mãos, um par de luvas de algodão protegia o que restava do códice roubado de Alexandria. "
        "Sabias que, se a fação dos Iluminados descobrisse que estavas em Portugal com estes documentos, "
        "a tua vida não valeria um único tostão. Ao puxares a gaveta oculta da mesa de carvalho do século XVIII, "
        "um estalo seco revelou um fundo falso. Lá dentro, envolto num cetim carmesim apodrecido, repousava "
        "um segundo documento: o diário pessoal de Luís de Camões, escrito nos seus últimos dias de febre.\n\n"
        "A prosa era caótica, mas uma frase saltava à vista em latim: 'A máquina do mundo não é uma metáfora. "
        "Ela pulsa sob as fundações de Coimbra.' De repente, ouves o som de passos pesados nas escadas de pedra "
        "da entrada. Alguém vinha armado, e vinha depressa."
    )
    st.divider()
    st.write("### 🔥 Como reages a este perigo iminente?")
    
    if st.button("🎯 [Ação] Agarrar no manuscrito, apagar a lanterna e esconder-te atrás do busto de mármore.", use_container_width=True):
        st.session_state.linha_temporal = "Ação"
        st.session_state.pagina = 2
        st.rerun()
    if st.button("🧠 [Estratégia] Deixar o diário falso à vista, saltar pela janela lateral para o pátio das escolas.", use_container_width=True):
        st.session_state.linha_temporal = "Fuga"
        st.session_state.pagina = 2
        st.rerun()
    if st.button("🗣️ [Diplomacia] Ficar no teu lugar, erguer as mãos e confrontar quem entra com autoridade académica.", use_container_width=True):
        st.session_state.linha_temporal = "Confronto"
        st.session_state.pagina = 2
        st.rerun()

# ==============================================================================
# PAGINA 2: DESDOBRAMENTO DA ESCOLA (PÁGINA LITERÁRIA 2)
# ==============================================================================
elif st.session_state.pagina == 2:
    st.title("Página 2: O Desdobrar da Sombra")
    
    if st.session_state.linha_temporal == "Ação":
        st.write(
            "Prendeste a respiração enquanto o teu corpo se fundia com a sombra do busto de mármore. "
            "A porta de madeira maciça foi arrombada com violência. Dois homens trajados com longos sobretudos "
            "escuros e óculos de lentes cromadas entraram taticamente. Os feixes das suas lanternas táticas "
            "varreram a sala de leitura, passando a escassos centímetros do teu rosto.\n\n"
            "'Ele esteve aqui', rosnou um deles, tocando na cadeira ainda quente. 'Encontrem o rapaz antes "
            "que ele decifre a coordenada da terceira página.' Sentes o batimento cardíaco descontrolado. "
            "O manuscrito está colado ao teu peito. Tens apenas alguns segundos antes que eles olhem para trás."
        )
    elif st.session_state.linha_temporal == "Fuga":
        st.write(
            "O impacto com a gravilha do pátio das escolas cortou-te o fôlego por instantes, mas o instinto "
            "de sobrevivência falou mais alto. Sob a chuva miúda que começava a cair sobre Coimbra, corres "
            "em direção aos arcos góticos. Atrás de ti, um grito de raiva ecoou da janela aberta da biblioteca.\n\n"
            "Eles perceberam o truque do diário falso muito mais rápido do que previas. Olhas para a descida "
            "íngreme das escadas monumentais: estão desertas, mas o som de um motor de alta cilindrada começa "
            "a rugir na base da colina, bloqueando a tua única rota de fuga tradicional."
        )
    else:
        st.write(
            "Mantiveste-te firme, sentado na cadeira de couro, com as mãos espalmadas sobre a mesa. "
            "A figura que cruzou o limiar da porta não era um capanga comum. Era o próprio Diretor do "
            "Instituto de Arqueologia Avançada, o homem que financiou a tua bolsa e que, agora sabias, "
            "liderava a fação dissidente.\n\n"
            "'Fizeste um trabalho brilhante, meu caro', disse ele, apontando uma arma silenciosa diretamente "
            "ao teu peito. 'Mas a verdade sobre a máquina do mundo pertence à corporação. Passa para cá o cetim "
            "carmesim e talvez tenhas direito a uma morte rápida e indolor.'"
        )
        
    st.divider()
    st.write("### 🔥 A narrativa adensa-se. Qual é o teu próximo passo?")
    
    if st.button("➡️ Avançar para a Página 3 do Livro", use_container_width=True):
        st.session_state.pagina = 3
        st.rerun()

# ==============================================================================
# PAGINA 3: O MURO DE PAGAMENTO (PAYWALL INTEGRADO)
# ==============================================================================
elif st.session_state.pagina == 3:
    st.title("🔒 Fim da Demonstração Gratuita")
    st.image(IMG_PERIGO, use_container_width=True)
    
    st.warning("Atingiste o limiar da introdução de 'O Último Manuscrito de Coimbra'.")
    st.write(
        "A tua linha de escolhas levou a tua personagem a um beco sem saída cheio de adrenalina e suspense. "
        "Este livro massivo foi desenhado para durar vários dias de leitura intensiva, contendo mais de **100 páginas "
        "de prosa rica**, enigmas criptográficos reais para resolver e dezenas de finais alternativos baseados na tua rota.\n\n"
        "Para obteres o acesso vitalício à obra completa, apoiar o autor e desbloquear imediatamente todos os caminhos "
        "restantes deste e de futuros livros, faz o teu upgrade PRO único."
    )
    
    # Botão de Pagamento Stripe integrado e livre de erros
    st.markdown(
        f'<a href="{STRIPE_PAYMENT_URL}" target="_blank" style="text-decoration: none;">'
        '<div style="background-color: #ff4b4b; color: white; text-align: center; '
        'padding: 18px; border-radius: 8px; font-weight: bold; font-size: 18px; cursor: pointer; '
        'box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4); margin-top: 20px;">'
        '🚀 COMPRAR ACESSO COMPLETO PRO VITALÍCIO (19.99€)'
        '</div></a>', 
        unsafe_allow_html=True
            )
    
