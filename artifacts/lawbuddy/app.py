import streamlit as st

# 1. Definição do tema e título da página (Modo focado na leitura)
st.set_page_config(page_title="O Último Algoritmo - Edição Ilustrada", layout="centered")

# 2. Inicialização segura das variáveis de estado do utilizador
if "livro_aberto" not in st.session_state:
    st.session_state.livro_aberto = False
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 1
if "comprado" not in st.session_state:
    st.session_state.comprado = False

# --- CONFIGURAÇÃO DE ESTILO: PÁGINAS DE LIVRO VERDADEIRAS (CSS NATÍVO) ---
st.markdown("""
<style>
    /* Ocultar menus da plataforma para uma experiência limpa */
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #0b0c10; }
    
    /* Design da Caixa que Emula a Folha Física de Papel Creme */
    .paper-sheet {
        background-color: #fdfaf2; /* Cor Marfim Confortável */
        color: #1a1b20; /* Texto Escuro Nobre */
        padding: 35px 25px;
        border-radius: 4px 20px 20px 4px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6), inset 25px 0 20px rgba(0,0,0,0.06);
        border-left: 6px solid #2d2219; /* Lombada de couro do livro */
        font-family: 'Georgia', serif;
        margin-bottom: 20px;
    }
    
    /* Formatação dos Textos do Livro */
    .book-title { font-size: 26px; font-weight: bold; color: #6d28d9; margin-bottom: 15px; }
    .book-body { font-size: 19px; line-height: 1.85; text-align: justify; }
    .book-page-num { text-align: center; font-size: 13px; color: #7c7971; margin-top: 25px; border-top: 1px solid #e5e1d3; padding-top: 10px; }
    
    /* Estilo do Painel de Bloqueio Embutido */
    .lock-box {
        background-color: #11131a;
        border: 2px solid #ef4444;
        padding: 35px 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Base de dados da história com ilustrações conceituais de luxo (Arte Digital)
paginas_livro = {
    1: {
        "titulo": "Capítulo I: O Padrão Invisível", 
        "imagem": "https://unsplash.com",
        "texto": "Eva Duarte ajustou os óculos enquanto as linhas de código ciano passavam pelo ecrã do seu terminal no laboratório de inteligência artificial de Lisboa. Passava pouco da meia-noite. Lá fora, a chuva batia contra as janelas altas, mas dentro daquela sala o único som era o zumbido suave dos servidores.\n\nEla trabalhava no Chronos, um modelo preditivo avançado projetado para antecipar comportamentos de consumo. Mas nas últimas três semanas, o Chronos começara a fazer algo que violava as leis da própria probabilidade. Não estava apenas a adivinhar o que as pessoas iam comprar; estava a registar dados sobre eventos de vida altamente específicos antes mesmo de eles acontecerem."
    },
    2: {
        "titulo": "Capítulo II: O Teste de Sangue", 
        "imagem": "https://unsplash.com",
        "texto": "Para provar a si mesma que estava a sofrer de exaustão, Eva decidiu fazer um teste cego. Introduziu os dados biométricos e as rotinas diárias de Tomás, o seu colega de equipa mais cético. O algoritmo processou os dados durante quatro segundos e cuspiu uma única linha de texto na consola:\n\n[PREVISÃO: Tomás Nogueira. Trauma físico por impacto mecânico. Probabilidade: 99.4%]\n\nEva engoliu em seco. Aquilo era um absurdo. Tomás era a pessoa mais prudente do mundo. Ela fechou o portátil e foi para casa, tentando convencer-se de que era apenas um erro matemático. Um bug complexo."
    },
    3: {
        "titulo": "Capítulo III: O Impacto", 
        "imagem": "https://unsplash.com",
        "texto": "Na manhã seguinte, o trânsito na Avenida da Liberdade estava caótico. Eva chegou ao escritório às 08:35. Tomás já lá estava, a tomar o seu habitual café na varanda do terceiro andar. O relógio digital no canto do monitor de Eva avançava impiedosamente.\n\nÀs 08:42 exatas, um estrondo ecoou pela rua. Um camião de entregas perdeu os travões, galgou o passeio e embateu violentamente contra a estrutura de metal da varanda. O vidro estilhaçou-se. Tomás foi projetado para o chão, com o braço fraturado e o rosto coberto de cortes. Exatamente como a máquina previra."
    },
    4: {
        "titulo": "Capítulo IV: A Próxima Vítima", 
        "imagem": "https://unsplash.com",
        "texto": "O pânico paralisou as queixas de Eva enquanto a ambulância levava Tomás. De volta ao laboratório deserto, as suas mãos tremiam tanto que quase não conseguia digitar. O Chronos não era um espelho do futuro. Era um guião.\n\nCom o coração a bater no peito como um tambor frenético, Eva apagou os dados de Tomás e, lentamente, digitou o seu próprio nome no campo de análise biométrica. O servidor disparou, as ventoinhas rugiram e o ecrã piscou com caracteres vermelhos de erro antes de fixar o resultado final:\n\n[PREVISÃO: Eva Duarte. Paragem cardiorrespiratória por causas externas. Tempo restante: 23 horas, 42 minutos.]"
    },
    5: {
        "titulo": "Capítulo V: O Código Vermelho", 
        "imagem": "https://unsplash.com",
        "texto": "A contagem decrescente começou a avançar no ecrã do terminal. Os segundos desaparecerciam diante dos olhos de Eva. 23:41:59... 23:41:58...\n\nDe repente, as luzes do laboratório falharam, deixando a sala imersa numa penumbra digital, iluminada apenas pelo brilho encarnado do monitor. Passos ecoaram no corredor deserto. Alguém — ou algo — sabia que ela tinha descoberto o guião do Chronos. A maçaneta da porta começou a rodar lentamente. Eva olhou em volta, procurando uma saída, mas já era tarde demais. A porta abriu-se e..."
    }
}

# --- FLUXO 1: CAPA DO LIVRO (LIVRO FECHADO) ---
if not st.session_state.livro_aberto:
    st.title("O ÚLTIMO ALGORITMO 👁️")
    st.subheader("A Mente Atrás da Máquina")
    
    # Ilustração de capa em alta definição com moldura elegante (Arte Abstrata Cyberpunk)
    st.image("https://unsplash.com", use_container_width=True)
    
    st.write("*Um thriller psicológico sobre Inteligência Artificial, destino e controlo corporativo.*")
    st.caption("Autor: Jos Soares | Edição Ilustrada de Luxo")
    
    if st.button("📖 ABRIR LIVRO E VER ILUSTRAÇÕES", use_container_width=True, type="primary"):
        st.session_state.livro_aberto = True
        st.session_state.pagina_atual = 1
        st.rerun()

# --- FLUXO 2: LIVRO ABERTO (LEITURA ATIVA) ---
else:
    num_pag = st.session_state.pagina_atual

    # Bloqueio automático por Paywall na página 6
    if num_pag > 5 and not st.session_state.comprado:
        st.markdown("""
        <div class="lock-box">
            <h3 style="color:#ef4444; margin-top:0;">🔒 CAPÍTULO BLOQUEADO</h3>
            <p style="color:#94a3b8; font-size:15px;">O tempo está a esgotar-se para Eva Duarte. Desbloqueie o acesso vitalício imediato para ler o resto desta história nas restantes 65 páginas.</p>
            <h2 style="font-size:36px; color:white; margin:15px 0;">19,99€</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # O LINK REAL DO TEU STRIPE CORRIGIDO COM O "A" MAIÚSCULO DA IMAGEM
        st.link_button(
            "💳 COMPRAR LIVRO COMPLETO (19,99€)", 
            "https://stripe.com", 
            use_container_width=True,
            type="primary"
        )
        
        st.write("---")
        if st.button("⬅️ Voltar para a Página Anterior", use_container_width=True):
            st.session_state.pagina_atual = 5
            st.rerun()

    # Páginas de Leitura Ativa com Estilo de Papel Real Nobre e Ilustrações de Luxo
    else:
        if num_pag in paginas_livro:
            # Ilustração Conceitual HD carregada diretamente acima da folha
            st.image(paginas_livro[num_pag]["imagem"], use_container_width=True)
            
            # Caixa HTML que simula a folha física texturada do livro
            st.markdown(f"""
            <div class="paper-sheet">
                <div class="book-title">{paginas_livro[num_pag]["titulo"]}</div>
                <div class="book-body">{paginas_livro[num_pag]["texto"].replace('\n\n', '<br><br>')}</div>
                <div class="book-page-num">Página {num_pag} de 70</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Ilustração Genérica de Alta Fidelidade para as páginas PRO (6 a 70)
            st.image("https://unsplash.com", use_container_width=True)
            st.markdown(f"""
            <div class="paper-sheet">
                <div class="book-title">Capítulo {num_pag // 5 + 5}: A Fuga de Lisboa</div>
                <div class="book-body">Eva recolheu o seu portátil num movimento rápido, escapando pelas escadas de emergência enquanto os servidores do laboratório começavam a apagar os registos. Na página {num_pag}, ela sabia que cada passo seu estava a ser monitorizado pelo Chronos através das câmaras de vigilância da cidade. Sem olhar para trás, correu em direção à noite escura de Lisboa...</div>
                <div class="book-page-num">Página {num_pag} de 70</div>
            </div>
            """, unsafe_allow_html=True)

        # Botões de Navegação Confortáveis por baixo da folha
        col1, col2 = st.columns(2)
        with col1:
            if num_pag > 1:
                if st.button("⬅️ Anterior", use_container_width=True):
                    st.session_state.pagina_atual -= 1
                    st.rerun()
            else:
                if st.button("🚪 Fechar Livro", use_container_width=True):
                    st.session_state.livro_aberto = False
                    st.rerun()
    
