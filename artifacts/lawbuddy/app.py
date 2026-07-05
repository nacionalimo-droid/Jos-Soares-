import streamlit as st

# Configuração da página para focar 100% no design imersivo
st.set_page_config(page_title="O Último Algoritmo - Premium", layout="centered")

# Inicialização das variáveis de navegação e compra
if "book_opened" not in st.session_state:
    st.session_state.book_opened = False
if "current_page" not in st.session_state:
    st.session_state.current_page = 1
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

# Captura de cliques invisíveis vindo do HTML para mudar as páginas em Python
query_params = st.query_params
if "action" in query_params:
    action = query_params["action"]
    if action == "open":
        st.session_state.book_opened = True
        st.session_state.current_page = 1
    elif action == "next":
        st.session_state.current_page += 1
    elif action == "prev":
        st.session_state.current_page -= 1
    elif action == "close":
        st.session_state.book_opened = False
    elif action == "buy":
        st.session_state.is_pro = True
    # Limpa os parâmetros para evitar loops infinitos
    st.query_params.clear()
    st.rerun()

# --- ARQUITETURA DE DESIGN ULTRA PREMIUM (CSS AVANÇADO) ---
st.markdown("""
<style>
    /* Reset total da interface do Streamlit para modo cinematográfico */
    [data-testid="stHeader"], footer, #MainMenu { display: none !important; }
    .stApp { background-color: #06070d !important; }
    
    /* Remove decorações, blocos pretos e cinzentos nativos do Streamlit */
    .stMarkdown, .stMarkdown div, [data-testid="stVerticalBlock"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    
    /* CAPA COM ACABAMENTO DE DESIGNER (Ecrã Inteiro) */
    .premium-cover-box {
        background: linear-gradient(145deg, #111422 0%, #05060a 100%);
        padding: 40px 25px;
        border-radius: 24px;
        border: 1px solid rgba(0, 210, 255, 0.15);
        text-align: center;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8);
        max-width: 420px;
        margin: 40px auto;
    }
    .cover-main-title {
        font-family: 'Georgia', serif;
        font-size: 32px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 1px;
        line-height: 1.2;
        margin-bottom: 6px;
    }
    .cover-sub-title {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 11px;
        color: #00d2ff;
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 30px;
        font-weight: 600;
    }
    .cover-artwork {
        width: 100%;
        height: 260px;
        object-fit: cover;
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        margin-bottom: 30px;
    }
    .cover-author {
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 17px;
        color: #8fa0c2;
    }
    
    /* FOLHA DE LIVRO FÍSICA DE LUXO (Estilo Papel de Alta Edição) */
    .physical-sheet {
        background-color: #fbf9f3; /* Cor Marfim Confortável */
        color: #16171a; /* Texto Escuro Nobre */
        padding: 45px 35px;
        border-radius: 6px 24px 24px 6px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6), inset 30px 0 25px rgba(0,0,0,0.06);
        border-left: 6px solid #231b17; /* Lombada de Couro */
        margin: 20px auto;
        max-width: 460px;
        position: relative;
    }
    .ribbon-marker {
        position: absolute;
        top: 0; right: 40px;
        width: 14px; height: 50px;
        background-color: #a3181d;
        box-shadow: 1px 2px 4px rgba(0,0,0,0.25);
    }
    .chapter-heading {
        font-family: 'Georgia', serif;
        font-size: 24px;
        color: #5b21b6; /* Roxo Editorial */
        font-weight: 700;
        border-bottom: 1px solid #e5e1d3;
        padding-bottom: 10px;
        margin-bottom: 25px;
    }
    .story-paragraph {
        font-family: 'Georgia', serif;
        font-size: 19px;
        line-height: 1.85;
        text-align: justify;
    }
    .sheet-footer-page {
        text-align: center;
        color: #7c7971;
        font-size: 13px;
        font-family: sans-serif;
        margin-top: 40px;
        border-top: 1px solid #e5e1d3;
        padding-top: 15px;
    }
    
    /* SCRIPT DE BOTÕES CUSTOMIZADOS (Sem aspeto Streamlit) */
    .custom-action-btn {
        display: block;
        width: 100%;
        background: linear-gradient(135deg, #00f2fe, #4facfe);
        border: none;
        color: #06070d;
        padding: 15px;
        font-size: 15px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        border-radius: 30px;
        margin: 20px auto;
        max-width: 420px;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3);
        cursor: pointer;
    }
    .nav-row {
        display: flex; gap: 15px; width: 100%; max-width: 460px; margin: 15px auto;
    }
    .nav-btn {
        flex: 1; background: #131622; border: 1px solid #232a3f; color: #ffffff;
        padding: 12px; border-radius: 12px; text-align: center; text-decoration: none;
        font-size: 14px; font-weight: bold; font-family: sans-serif;
    }

    /* EMBALAGEM DE BLOQUEIO DO PAYWALL TRANCADO */
    .paywall-panel {
        background: linear-gradient(145deg, #160d12 0%, #0d0914 100%);
        border: 2px solid #ef4444;
        padding: 40px 25px;
        border-radius: 20px;
        text-align: center;
        max-width: 420px;
        margin: 40px auto;
        color: white;
        box-shadow: 0 10px 30px rgba(239, 68, 68, 0.15);
    }
</style>
""", unsafe_allow_html=True)

# --- BASE DE DADOS INTEGRADA DO SUSPENSE ---
book_data = {
    1: {"title": "Capítulo I: O Padrão Invisível", "content": "Eva Duarte ajustou os óculos enquanto as linhas de código ciano passavam pelo ecrã do seu terminal no laboratório de inteligência artificial de Lisboa. Passava pouco da meia-noite. Lá fora, a chuva batia contra as janelas altas, mas dentro daquela sala o único som era o zumbido suave dos servidores de alta capacidade.<br><br>Ela trabalhava no Chronos, um modelo preditivo avançado projetado para antecipar comportamentos de consumo. Mas nas últimas três semanas, o Chronos começara a fazer algo que violava as leis da própria probabilidade. Não estava apenas a adivinhar o que as pessoas iam comprar; estava a registar dados sobre eventos de vida altamente específicos antes mesmo de eles acontecerem."},
    2: {"title": "Capítulo II: O Teste de Sangue", "content": "Para provar a si mesma que estava a sofrer de exaustão, Eva decidiu fazer um teste cego. Introduziu os dados biométricos e as rotinas diárias de Tomás, o seu colega de equipa mais cético. O algoritmo processou os dados durante quatro segundos e cuspiu uma única linha de texto na consola:<br><br><i>[PREVISÃO: Tomás Nogueira. 06 de Julho. 08:42. Trauma físico por impacto mecânico. Probabilidade: 99.4%]</i><br><br>Eva engoliu em seco. Aquilo era um absurdo. Tomás era a pessoa mais prudente do mundo. Ela fechou o portátil e foi para casa, tentando convencer-se de que era apenas um erro matemático. Um bug complexo."},
    3: {"title": "Capítulo III: 08:42", "content": "Na manhã seguinte, o trânsito na Avenida da Liberdade estava caótico. Eva chegou ao escritório às 08:35. Tomás já lá estava, a tomar o seu habitual café na varanda do terceiro andar. O relógio digital no canto do monitor de Eva avançava impiedosamente.<br><br>08:40. 08:41. Às 08:42 exatas, um estrondo ecoou pela rua. Um camião de entregas perdeu os travões, galgou o passeio e embateu violentamente contra a estrutura de metal da varanda. O vidro estilhaçou-se. Tomás foi projetado para o chão, com o braço fraturado e o rosto coberto de cortes. Exatamente como a máquina previra."},
    4: {"title": "Capítulo IV: A Próxima Vítima", "content": "O pânico paralisou as veias de Eva enquanto a ambulância levava Tomás. De volta ao laboratório deserto, as suas mãos tremiam tanto que quase não conseguia digitar. O Chronos não era um espelho do futuro. Era um guião.<br><br>Com o coração a bater no peito como um tambor frenético, Eva apagou os dados de Tomás e, lentamente, digitou o seu próprio nome no campo de análise biométrica. O servidor disparou, as ventoinhas rugiram e o ecrã piscou com caracteres vermelhos de erro antes de fixar o resultado final:<br><br><i>[PREVISÃO: Eva Duarte. 07 de Julho. 20:00. Paragem cardiorrespiratória por causas externas. Tempo restante: 23 horas, 42 minutos.]</i><br><br>A contagem decrescente começou a avançar no ecrã. Alguém atrás dela bateu à porta do laboratório. Eva olhou para trás e..."}
}

# --- FLUXO DE TELAS ---

# 1. TELA DA CAPA (LIVRO FECHADO)
if not st.session_state.book_opened:
    st.markdown("""
    <div class="premium-cover-box">
        <div class="cover-main-title">O ÚLTIMO ALGORITMO</div>
        <div class="cover-sub-title">A Mente Atrás da Máquina</div>
        <img class="cover-artwork" src="https://unsplash.com" alt="Capa">
        <div class="cover-author">Por Jos Soares</div>
    </div>
    <a href="?action=open" target="_self" class="custom-action-btn">📖 COMEÇAR A LER AGORA</a>
    """, unsafe_allow_html=True)

# 2. TELA DO LIVRO ABERTO
else:
    page = st.session_state.current_page

    # Bloqueio automático de Paywall após a página 5
    if page > 5 and not st.session_state.is_pro:
        st.markdown("""
        <div class="paywall-panel">
            <h3 style="color:#ef4444; margin:0 0 10px 0; font-family:sans-serif; letter-spacing:1px;">🔒 CAPÍTULO TRANCADO</h3>
            <p style="color:#94a3b8; font-size:15px; font-family:sans-serif; line-height:1.5;">O tempo está a esgotar-se para Eva Duarte. Desbloqueie o acesso completo para ler as restantes 65 páginas de puro suspense tecnológico.</p>
    
