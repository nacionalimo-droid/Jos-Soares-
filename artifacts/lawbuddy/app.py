import streamlit as st

# Configuração da página para focar totalmente na leitura confortável e de luxo
st.set_page_config(page_title="O Último Algoritmo - Edição Comercial", layout="centered")

# Inicialização das variáveis de controlo de leitura, fecho do livro e pagamento
if "book_opened" not in st.session_state:
    st.session_state.book_opened = False
if "current_page" not in st.session_state:
    st.session_state.current_page = 1
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

# --- ARQUITETURA DE DESIGN PREMIUM (CSS) ---
st.markdown("""
<style>
    /* Esconder elementos desnecessários para parecer um e-book comercial */
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #090a0f; }
    
    /* Design de Folha de Livro Física Real */
    .book-sheet {
        background-color: #fdfcf7; /* Cor de papel creme/marfim premium */
        color: #1a1b20; /* Escrita escura suave para máximo conforto visual */
        padding: 45px 35px;
        border-radius: 4px 16px 16px 4px;
        box-shadow: 0 12px 28px rgba(0,0,0,0.5), inset 25px 0 20px rgba(0,0,0,0.05);
        border-left: 6px solid #2b211a; /* Lombada simulada em couro */
        margin-top: 10px;
        position: relative;
        font-family: 'Georgia', serif;
    }
    
    /* Fita Marcadora de Livro Clássica */
    .ribbon {
        position: absolute;
        top: 0;
        right: 35px;
        width: 12px;
        height: 45px;
        background-color: #b31c22;
        box-shadow: 1px 1px 4px rgba(0,0,0,0.3);
        z-index: 5;
    }
    
    /* Capa de Alta Edição */
    .luxury-cover {
        background: linear-gradient(135deg, #131722 0%, #080a10 100%);
        padding: 55px 20px;
        border-radius: 12px;
        border: 2px solid #20293a;
        text-align: center;
        box-shadow: inset 0 0 35px rgba(0, 210, 255, 0.12);
        margin-top: 20px;
    }
    .cover-main-title {
        font-family: 'Georgia', serif;
        font-size: 34px;
        font-weight: bold;
        color: #00d2ff;
        letter-spacing: 1px;
        margin-bottom: 8px;
        text-shadow: 0 0 15px rgba(0, 210, 255, 0.3);
    }
    .cover-sub-title {
        font-family: 'Arial', sans-serif;
        font-size: 13px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 25px;
    }
    .cover-author-tag {
        font-style: italic;
        font-size: 18px;
        color: #cbd5e1;
    }

    /* Tipografia Fluida e Elegante */
    .story-text {
        font-size: 19px;
        line-height: 1.85;
        text-align: justify;
    }
    .chapter-header {
        font-size: 25px;
        color: #8b5cf6; /* Cor roxa sofisticada para os títulos */
        margin-bottom: 25px;
        font-weight: bold;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 6px;
    }
    
    .page-footer-num {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 35px;
        border-top: 1px solid #e2e8f0;
        padding-top: 12px;
    }

    /* Tela de Bloqueio do Paywall (19.99€) */
    .paywall-lock-container {
        background: #11131a;
        border: 2px solid #ef4444;
        padding: 40px 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 10px;
        color: white;
    }
    
    /* Ilustração Vetorial CSS: O Olho do Algoritmo */
    .art-eye {
        width: 60px; height: 60px; margin: 20px auto;
        border: 3px solid #00d2ff; border-radius: 50% 0;
        transform: rotate(45deg); display: flex; align-items: center; justify-content: center;
    }
    .art-pupil {
        width: 20px; height: 20px; background: #8b5cf6; border-radius: 50%;
    }
</style>
""", unsafe_allow_html=True)

# --- BASE DE DADOS COMPLETA DO LIVRO ---
book_data = {
    1: {"title": "Capítulo I: O Padrão Invisível", "content": "Eva Duarte ajustou os óculos enquanto as linhas de código ciano passavam pelo ecrã do seu terminal no laboratório de inteligência artificial de Lisboa. Passava pouco da meia-noite. Lá fora, a chuva batia contra as janelas altas, mas dentro daquela sala o único som era o zumbido suave dos servidores de alta capacidade.<br><br>Ela trabalhava no Chronos, um modelo preditivo avançado projetado para antecipar comportamentos de consumo. Mas nas últimas três semanas, o Chronos começara a fazer algo que violava as leis da própria probabilidade. Não estava apenas a adivinhar o que as pessoas iam comprar; estava a registar dados sobre eventos de vida altamente específicos antes mesmo de eles acontecerem."},
    2: {"title": "Capítulo II: O Teste de Sangue", "content": "Para provar a si mesma que estava a sofrer de exaustão, Eva decidiu fazer um teste cego. Introduziu os dados biométricos e as rotinas diárias de Tomás, o seu colega de equipa mais cético. O algoritmo processou os dados durante quatro segundos e cuspiu uma única linha de texto na consola:<br><br><i>[PREVISÃO: Tomás Nogueira. 06 de Julho. 08:42. Trauma físico por impacto mecânico. Probabilidade: 99.4%]</i><br><br>Eva engoliu em seco. Aquilo era um absurdo. Tomás era a pessoa mais prudente do mundo. Ela fechou o portátil e foi para casa, tentando convencer-se de que era apenas um erro matemático. Um bug complexo."},
    3: {"title": "Capítulo III: 08:42", "content": "Na manhã seguinte, o trânsito na Avenida da Liberdade estava caótico. Eva chegou ao escritório às 08:35. Tomás já lá estava, a tomar o seu habitual café na varanda do terceiro andar. O relógio digital no canto do monitor de Eva avançava impiedosamente.<br><br>08:40. 08:41. Às 08:42 exatas, um estrondo ecoou pela rua. Um camião de entregas perdeu os travões, galgou o passeio e embateu violentamente contra a estrutura de metal da varanda. O vidro estilhaçou-se. Tomás foi projetado para o chão, com o braço fraturado e o rosto coberto de cortes. Exatamente como a máquina previra."},
    4: {"title": "Capítulo IV: A Próxima Vítima", "content": "O pânico paralisou as veias de Eva enquanto a ambulância levava Tomás. De volta ao laboratório deserto, as suas mãos tremiam tanto que quase não conseguia digitar. O Chronos não era um espelho do futuro. Era um guião.<br><br>Com o coração a bater no peito como um tambor frenético, Eva apagou os dados de Tomás e, lentamente, digitou o seu próprio nome no campo de análise biométrica. O servidor disparou, as ventoinhas rugiram e o ecrã piscou com caracteres vermelhos de erro antes de fixar o resultado final:<br><br><i>[PREVISÃO: Eva Duarte. 07 de Julho. 20:00. Paragem cardiorrespiratória por causas externas. Tempo restante: 23 horas, 42 minutos.]</i><br><br>A contagem decrescente começou a avançar no ecrã. Alguém atrás dela bateu à porta do laboratório. Eva olhou para trás e..."}
}

# --- FLUXO 1: SE O LIVRO ESTIVER FECHADO, MOSTRA APENAS A CAPA ---
if not st.session_state.book_opened:
    st.markdown(f"""
    <div class="luxury-cover">
        <div class="cover-main-title">O ÚLTIMO ALGORITMO</div>
        <div class="cover-sub-title">A Mente Atrás da Máquina</div>
        
        <!-- Arte Geométrica do Olho -->
        <div class="art-eye"><div class="art-pupil"></div></div>
        
        <div class="cover-author-tag" style="margin-bottom: 25px;">Por Jos Soares</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão de Abertura Comercial para iniciar a leitura
    if st.button("📖 ABRIR LIVRO", use_container_width=True):
        st.session_state.book_opened = True
        st.session_state.current_page = 1
        st.rerun()

# --- FLUXO 2: SE O LIVRO JÁ ESTIVER ABERTO, ENTRA NAS PÁGINAS ---
else:
    page = st.session_state.current_page

    # Se passar da página 5 e não tiver pago, bloqueia a leitura (Páginas Gratuitas: 1 a 5)
    if page > 5 and not st.session_state.is_pro:
        st.markdown("""
        <div class="paywall-lock-container">
            <h3 style="color:#ef4444; margin-top:0;">🔒 CAPÍTULO BLOQUEADO</h3>
            <p style="color:#94a3b8; font-size:15px;">O Chronos previu o fim de Eva. Descubra como sabotar a Inteligência Artificial e reescrever o destino nas restantes 65 páginas.</p>
            <h2 style="font-size:38px; margin:15px 0; color:white;">19,99€</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💳 DESBLOQUEAR LIVRO COMPLETO", use_container_width=True):
            st.session_state.is_pro = True
            st.rerun()
            
    else:
        # BOTÃO PARA O SPOTIFY: Localizado estrategicamente no topo da página
        st.link_button(
            "🎵 Ouvir Banda Sonora no Spotify", 
            "https://spotify.com", 
            use_container_width=True
        )
        
        # Renderização da folha física do livro
        st.markdown('<div class="book-sheet"><div class="ribbon"></div>', unsafe_allow_html=True)
        
        # Mapeamento do conteúdo (Página 1 mostra o Capítulo I, e assim sucessivamente)
        if page in book_data:
            title = book_data[page]["title"]
            content = book_data[page]["content"]
        else:
            # Geração automática do conteúdo das restantes 65 páginas virtuais para utilizadores PRO
            title = f"Capítulo {page // 5 + 4}: A Rede de Vigilância"
            content = f"Eva Duarte apressou o passo pelas ruelas de Alfama na página {page}, sentindo o peso do relógio no pulso. Os acordes de piano que ouvira antes no Spotify pareciam ecoar na névoa da noite. Cada linha de código que tentava reescrever no seu terminal portátil gerava um novo labirinto de decisões. O algoritmo Chronos continuava à espreita..."

        st.markdown(f'<div class="chapter-header">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="story-text">{content}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="page-footer-num">Página {page} de 70</div></div>', unsafe_allow_html=True)

