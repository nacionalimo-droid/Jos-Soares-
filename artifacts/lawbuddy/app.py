import streamlit as st

# Configuração da página focada numa leitura imersiva e de luxo
st.set_page_config(page_title="O Último Algoritmo - Edição Premium", layout="centered")

# Inicialização das variáveis de controlo
if "current_page" not in st.session_state:
    st.session_state.current_page = 1
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

# --- ARQUITETURA DE DESIGN AVANÇADA (CSS PREMIUM) ---
st.markdown("""
<style>
    /* Ocultação de elementos padrão da plataforma Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #08090c; }
    
    /* Corpo Principal do Livro - Simulação de Folha Física Real */
    .book-page-sheet {
        background-color: #fcfbf7; /* Cor de papel marfim/creme texturado antigo */
        color: #1c1d21; /* Texto cinza-carvão escuro (máximo conforto de leitura) */
        padding: 50px 40px;
        border-radius: 4px 16px 16px 4px;
        box-shadow: 5px 10px 25px rgba(0,0,0,0.6), inset 30px 0 20px rgba(0,0,0,0.06);
        border-left: 5px solid #2e241f; /* Simulação da lombada de couro do livro */
        margin-top: 15px;
        position: relative;
        font-family: 'Georgia', serif;
    }
    
    /* Marcador de Página em Fita de Cetim Embutido */
    .bookmark-ribbon {
        position: absolute;
        top: 0;
        right: 40px;
        width: 14px;
        height: 50px;
        background-color: #b81d24;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        z-index: 10;
    }
    
    /* Design de Capa de Alta Edição */
    .premium-cover {
        background: linear-gradient(135deg, #161a24 0%, #0a0d14 100%);
        padding: 65px 25px;
        border-radius: 12px;
        border: 2px solid #232c3f;
        text-align: center;
        box-shadow: inset 0 0 40px rgba(0, 210, 255, 0.15);
    }
    .cover-title-text {
        font-family: 'Georgia', serif;
        font-size: 38px;
        font-weight: bold;
        color: #00d2ff;
        letter-spacing: 1px;
        margin-bottom: 12px;
        text-shadow: 0 0 20px rgba(0, 210, 255, 0.3);
    }
    .cover-author-text {
        font-style: italic;
        font-size: 19px;
        color: #d1d9ec;
        margin-top: 30px;
    }

    /* Tipografia de Livro de Romance/Suspense */
    .story-body-text {
        font-size: 19px;
        line-height: 1.9;
        text-align: justify;
    }
    .story-chapter-title {
        font-size: 26px;
        color: #9c27b0; /* Tom elegante para capitulação */
        margin-bottom: 30px;
        font-weight: bold;
        border-bottom: 2px solid #e8e6df;
        padding-bottom: 8px;
    }
    
    .footer-page-num {
        text-align: center;
        color: #8c8a81;
        font-size: 13px;
        margin-top: 40px;
        border-top: 1px solid #e8e6df;
        padding-top: 15px;
    }

    /* Caixa do Paywall de Bloqueio Embutida na Folha */
    .locked-page-box {
        background: #111216;
        border: 2px solid #ff3366;
        padding: 40px 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 10px;
        color: white;
    }
    
    /* Painel do Leitor de Música Superior */
    .audio-bar-box {
        background: #12141c;
        border: 1px solid #222633;
        padding: 12px;
        border-radius: 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    
    /* Vetor Geométrico Futurista (Ilustração Digital por CSS) */
    .digital-eye-art {
        width: 70px; height: 70px; margin: 25px auto;
        border: 3px solid #00d2ff; border-radius: 50% 0;
        transform: rotate(45deg); display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 15px rgba(0,210,255,0.3);
    }
    .digital-eye-pupil {
        width: 25px; height: 25px; background: #9c27b0; border-radius: 50%;
        animation: pulse 2s infinite alternate;
    }
    @keyframes pulse { from { transform: scale(0.8); } to { transform: scale(1.1); } }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO INTERATIVO: MÚSICA DE PIANO INTEGRADA (ON/OFF) ---
st.markdown("""
<div class="audio-bar-box">
    <span style="color:#a0a0b0; font-size:13px; font-family:Arial; margin-left:10px;">🎼 Banda Sonora: <b>Piano de Suspense Cinematográfico</b></span>
    <audio id="piano-loop" src="https://soundhelix.com" loop></audio>
    <button onclick="let a=document.getElementById('piano-loop'); if(a.paused){a.play();this.innerText='⏸️ Som On';this.style.background='#9c27b0';}else{a.pause();this.innerText='▶️ Som Off';this.style.background='#252533';}" 
            style="border:none; color:white; background:#252533; padding:6px 16px; font-size:12px; font-weight:bold; border-radius:20px; cursor:pointer;">
        ▶️ Som Off
    </button>
</div>
""", unsafe_allow_html=True)

# --- BASE DE DADOS DA HISTÓRIA ---
book_pages = {
    1: {"title": "O ÚLTIMO ALGORITMO", "subtitle": "A Mente Atrás da Máquina"},
    2: {"title": "Capítulo I: O Padrão Invisível", "content": "Eva Duarte ajustou os óculos enquanto as linhas de código ciano passavam pelo ecrã do seu terminal no laboratório de inteligência artificial de Lisboa. Passava pouco da meia-noite. Lá fora, a chuva batia contra as janelas altas, mas dentro daquela sala o único som era o zumbido suave dos servidores de alta capacidade.<br><br>Ela trabalhava no Chronos, um modelo preditivo avançado projetado para antecipar comportamentos de consumo. Mas nas últimas três semanas, o Chronos começara a fazer algo que violava as leis da própria probabilidade. Não estava apenas a adivinhar o que as pessoas iam comprar; estava a registar dados sobre eventos de vida altamente específicos antes mesmo de eles acontecerem."},
    3: {"title": "Capítulo II: O Teste de Sangue", "content": "Para provar a si mesma que estava a sofrer de exaustão, Eva decidiu fazer um teste cego. Introduziu os dados biométricos e as rotinas diárias de Tomás, o seu colega de equipa mais cético. O algoritmo processou os dados durante quatro segundos e cuspiu uma única linha de texto na consola:<br><br><i>[PREVISÃO: Tomás Nogueira. 06 de Julho. 08:42. Trauma físico por impacto mecânico. Probabilidade: 99.4%]</i><br><br>Eva engoliu em seco. Aquilo era um absurdo. Tomás era a pessoa mais prudente do mundo. Ela fechou o portátil e foi para casa, tentando convencer-se de que era apenas um erro matemático. Um bug complexo."},
    4: {"title": "Capítulo III: 08:42", "content": "Na manhã seguinte, o trânsito na Avenida da Liberdade estava caótico. Eva chegou ao escritório às 08:35. Tomás já lá estava, a tomar o seu habitual café na varanda do terceiro andar. O relógio digital no canto do monitor de Eva avançava impiedosamente.<br><br>08:40. 08:41. Às 08:42 exatas, um estrondo ecoou pela rua. Um camião de entregas perdeu os travões, galgou o passeio e embateu violentamente contra a estrutura de metal da varanda. O vidro estilhaçou-se. Tomás foi projetado para o chão, com o braço fraturado e o rosto coberto de cortes. Exatamente como a máquina previra."},
    5: {"title": "Capítulo IV: A Próxima Vítima", "content": "O pânico paralisou as veias de Eva enquanto a ambulância levava Tomás. De volta ao laboratório deserto, as suas mãos tremiam tanto que quase não conseguia digitar. O Chronos não era um espelho do futuro. Era um guião.<br><br>Com o coração a bater no peito como um tambor frenético, Eva apagou os dados de Tomás e, lentamente, digitou o seu próprio nome no campo de análise biométrica. O servidor disparou, as ventoinhas rugiram e o ecrã piscou com caracteres vermelhos de erro antes de fixar o resultado final:<br><br><i>[PREVISÃO: Eva Duarte. 07 de Julho. 20:00. Paragem cardiorrespiratória por causas externas. Tempo restante: 23 horas, 42 minutos.]</i><br><br>A contagem decrescente começou a avançar no ecrã. Alguém atrás dela bateu à porta do laboratório. Eva olhou para trás e..."}
}

# --- LÓGICA DO SISTEMA ---
current = st.session_state.current_page

# Bloqueio de Leitura (Paywall) após as 5 páginas se não for PRO
if current > 5 and not st.session_state.is_pro:
    st.markdown("""
    <div class="locked-page-box">
        <h3 style="color:#ff3366;margin-top:0;">🔒 LEITURA INTERROMPIDA</h3>
        <p style="color:#a6b2d1;font-size:15px;">O guião da máquina previu o fim de Eva Duarte nas próximas horas. Descubra como sabotar o sistema nos restantes capítulos.</p>
        <h2 style="font-size:36px;margin:15px 0;color:white;">19,99€</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("💳 DESBLOQUEAR ACESSO VITALÍCIO", use_container_width=True):
        st.session_state.is_pro = True
        st.rerun()

else:
    # Renderização Física das Páginas do Livro
    st.markdown('<div class="book-page-sheet"><div class="bookmark-ribbon"></div>', unsafe_allow_html=True)
    
    if current == 1:
        # PÁGINA DA CAPA PREMIUM COM ILUSTRAÇÃO DIGITAL VETORIAL
        st.markdown(f"""
        <div class="premium-cover">
            <div class="cover-title-text">{book_pages[1]['title']}</div>
            <div style="font-size:12px;color:#6c7a9c;letter-spacing:5px;text-transform:uppercase;">{book_pages[1]['subtitle']}</div>
            
            <!-- Ilustração Vetorial Olho Digital da IA -->
            <div class="digital-eye-art"><div class="digital-eye-pupil"></div></div>
            
            <div class="cover-author-text">Por Jos Soares</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # CONTEÚDO DAS PÁGINAS DE LEITURA DO LIVRO
        if current in book_pages:
            title = book_pages[current]["title"]
            content = book_pages[current]["content"]
        else:
            title = f"Capítulo {current // 5 + 4}: O Labirinto Binário"
            
