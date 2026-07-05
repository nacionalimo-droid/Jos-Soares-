import streamlit as st

# Configuração da página para focar totalmente na leitura confortável
st.set_page_config(page_title="O Último Algoritmo", layout="centered")

# Inicialização das variáveis de estado (Página atual e Status de Compra)
if "current_page" not in st.session_state:
    st.session_state.current_page = 1
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

# --- ESTILIZAÇÃO PREMIUM (CSS) ---
st.markdown("""
<style>
    /* Esconder elementos padrão do Streamlit para parecer um e-book real */
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #0d0e12; }
    
    /* Contentor do Livro */
    .book-container {
        background-color: #13151c;
        padding: 40px 30px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid #1f2330;
        margin-top: 20px;
    }
    
    /* Design da Capa Super Linda */
    .cover-box {
        background: linear-gradient(135deg, #111524 0%, #080a10 100%);
        padding: 60px 20px;
        border-radius: 12px;
        border: 2px solid #1a233a;
        text-align: center;
        box-shadow: inset 0 0 50px rgba(0, 210, 255, 0.1);
    }
    .cover-title {
        font-family: 'Georgia', serif;
        font-size: 36px;
        font-weight: bold;
        color: #00d2ff;
        letter-spacing: 2px;
        margin-bottom: 10px;
        text-shadow: 0 0 15px rgba(0, 210, 255, 0.4);
    }
    .cover-subtitle {
        font-family: 'Arial', sans-serif;
        font-size: 14px;
        color: #6c7a9c;
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 40px;
    }
    .cover-author {
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 18px;
        color: #e3e8f8;
    }

    /* Tipografia que Dá Gosto Ler (Georgia, Marfim, Espaçamento Confortável) */
    .book-text {
        font-family: 'Georgia', serif;
        font-size: 20px;
        line-height: 1.8;
        color: #e3e6ee; /* Cor marfim suave que não magoa os olhos */
        text-align: justify;
        text-justify: inter-word;
    }
    
    .chapter-title {
        font-family: 'Georgia', serif;
        font-size: 28px;
        color: #00d2ff;
        margin-bottom: 25px;
        font-weight: bold;
        border-bottom: 1px solid #1f2330;
        padding-bottom: 10px;
    }
    
    .page-number {
        font-family: 'Arial', sans-serif;
        text-align: center;
        color: #4f5875;
        font-size: 14px;
        margin-top: 30px;
    }

    /* Estilo do Paywall de Bloqueio (19.99€) */
    .paywall-box {
        background: linear-gradient(130deg, #191218 0%, #110d1a 100%);
        border: 2px solid #ff3366;
        padding: 40px 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(255, 51, 102, 0.2);
    }
    .paywall-title {
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: #ff3366;
        margin-bottom: 15px;
    }
    .paywall-price {
        font-size: 42px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- BASE DE DADOS INTEGRADA DA HISTÓRIA (70 PÁGINAS virtuais) ---
# Páginas 1 a 5 contêm o início real e o gancho. As restantes simulam a continuidade pós-pagamento.
book_pages = {
    1: ("CAPA DO LIVRO", "O ÚLTIMO ALGORITMO", "A Mente Atrás da Máquina"),
    2: ("Capítulo I: O Padrão Invisível", 
        "Eva Duarte ajustou os óculos enquanto as linhas de código ciano passavam pelo ecrã do seu terminal no laboratório de inteligência artificial de Lisboa. Passava pouco da meia-noite. Lá fora, a chuva batia contra as janelas altas, mas dentro daquela sala o único som era o zumbido suave dos servidores de alta capacidade.<br><br>"
        "Ela trabalhava no Chronos, um modelo preditivo avançado projetado para antecipar comportamentos de consumo. Mas nas últimas três semanas, o Chronos começara a fazer algo que violava as leis da própria probabilidade. Não estava apenas a adivinhar o que as pessoas iam comprar; estava a registar dados sobre eventos de vida altamente específicos antes mesmo de eles acontecerem."),
    3: ("Capítulo II: O Teste de Sangue", 
        "Para provar a si mesma que estava a sofrer de exaustão, Eva decidiu fazer um teste cego. Introduziu os dados biométricos e as rotinas diárias de Tomás, o seu colega de equipa mais cético. O algoritmo processou os dados durante quatro segundos e cuspiu uma única linha de texto na consola:<br><br>"
        "<i>[PREVISÃO: Tomás Nogueira. 06 de Julho. 08:42. Trauma físico por impacto mecânico. Probabilidade: 99.4%]</i><br><br>"
        "Eva engoliu em seco. Aquilo era um absurdo. Tomás era a pessoa mais prudente do mundo. Ela fechou o portátil e foi para casa, tentando convencer-se de que era apenas um erro matemático. Um bug complexo."),
    4: ("Capítulo III: 08:42", 
        "Na manhã seguinte, o trânsito na Avenida da Liberdade estava caótico. Eva chegou ao escritório às 08:35. Tomás já lá estava, a tomar o seu habitual café na varanda do terceiro andar. O relógio digital no canto do monitor de Eva avançava impiedosamente.<br><br>"
        "08:40. 08:41. Às 08:42 exatas, um estrondo ecoou pela rua. Um camião de entregas perdeu os travões, galgou o passeio e embateu violentamente contra a estrutura de metal da varanda. O vidro estilhaçou-se. Tomás foi projetado para o chão, com o braço fraturado e o rosto coberto de cortes. Exatamente como a máquina previra."),
    5: ("Capítulo IV: A Próxima Vítima", 
        "O pânico paralisou as veias de Eva enquanto a ambulância levava Tomás. De volta ao laboratório deserto, as suas mãos tremiam tanto que quase não conseguia digitar. O Chronos não era um espelho do futuro. Era um guião.<br><br>"
        "Com o coração a bater no peito como um tambor frenético, Eva apagou os dados de Tomás e, lentamente, digitou o seu próprio nome no campo de análise biométrica. O servidor disparou, as ventoinhas rugiram e o ecrã piscou com caracteres vermelhos de erro antes de fixar o resultado final:<br><br>"
        "<i>[PREVISÃO: Eva Duarte. 07 de Julho. 20:00. Paragem cardiorrespiratória por causas externas. Tempo restante: 23 horas, 42 minutos.]</i><br><br>"
        "A contagem decrescente começou a avançar no ecrã. Alguém atrás dela bateu à porta do laboratório. Eva olhou para trás e...")
}

# --- LÓGICA DE NAVEGAÇÃO E PAYWALL ---
current = st.session_state.current_page

# Verificar se atingiu o limite gratuito e bloqueia se não for PRO
if current > 5 and not st.session_state.is_pro:
    st.markdown("""
    <div class="paywall-box">
        <div class="paywall-title">🔒 CAPÍTULO BLOQUEADO</div>
        <p style="color:#a6b2d1; font-size:16px;">O algoritmo previu o fim de Eva. Descubra como ela vai enganar o sistema nas próximas 65 páginas de suspense puro.</p>
        <p style="color:#6c7a9c; font-size:12px; margin-bottom:15px;">Acesso Vitalício Imediato (70 Páginas)</p>
        <div class="paywall-price">19,99€</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão de pagamento oficial simulado
    if st.button("💳 ADQUIRIR ACESSO COMPLETO", use_container_width=True):
        st.session_state.is_pro = True
        st.rerun()

else:
    # Renderizar a página do livro
    st.markdown('<div class="book-container">', unsafe_allow_html=True)
    
    if current == 1:
        # Página 1: Capa Linda
        page_info = book_pages[1]
        st.markdown(f"""
        <div class="cover-box">
            <div class="cover-title">{page_info[1]}</div>
            <div class="cover-subtitle">{page_info[2]}</div>
            <div style="margin: 30px 0; color:#00d2ff; font-size:24px;">👁️</div>
            <div class="cover-author">Por Jos Soares</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Páginas 2 a 5 ou Páginas PRO (6 a 70)
        if current in book_pages:
            title, content = book_pages[current]
        else:
            # Geração automática do conteúdo das restantes 75 páginas para simular o livro completo
            title = f"Capítulo {current // 5 + 4}: A Rede de Intrigas"
            content = f"Eva Duarte continuou a sua fuga pelas ruas escuras de Lisboa, tentando decifrar os metadados ocultos na página {current}. Cada segundo na contagem decrescente aproximava-a do enigma final do criador do sistema. As pistas apontavam para uma conspiração que ia muito além do código informático que ela própria tinha ajudado a construir..."

        st.markdown(f'<div class="chapter-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="book-text">{content}</div>', unsafe_allow_html=True)
        
    st.markdown(f'<div class="page-number">Página {current} de 70</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Botões de Navegação Confortáveis
    col1, col2 = st.columns(2)
    with col1:
        if current > 1:
            if st.button("⬅️ Anterior", use_container_width=True):
                st.session_state.current_page -= 1
                st.rerun()
    with col2:
        if current < 70:
            if st.button("Seguinte ➡️", use_container_width=True):
                st.session_state.current_page += 1
                st.rerun()

# --- PAINEL DE CONTROLO DE DESENVOLVIMENTO (SIDEBAR) ---
with st.sidebar:
    st.title("⚙️ Painel de Teste")
    st.write("Usa os controlos abaixo para simular as vendas da tua App:")
    
    # Switch para ativar/desativar o modo PRO instantaneamente
    pro_status = st.checkbox("Simular Compra Ativa (PRO)", value=st.session_state.is_pro)
    if pro_status != st.session_state.is_pro:
        st.session_state.is_pro = pro_status
        st.rerun()
        
    if st.button("Resetar Livro para a Capa"):
        st.session_state.current_page = 1
        st.rerun()
        
