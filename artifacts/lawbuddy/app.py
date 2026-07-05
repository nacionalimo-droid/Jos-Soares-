import streamlit as st

# 1. Configuração focada no ecrã do telemóvel
st.set_page_config(page_title="O Último Algoritmo", layout="centered")

# 2. Inicialização das variáveis na memória do navegador
if "livro_aberto" not in st.session_state:
    st.session_state.livro_aberto = False
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 1
if "comprado" not in st.session_state:
    st.session_state.comprado = False

# --- CONFIGURAÇÃO DE ESTILO: MODO LIVRO ORIGINAL ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #0b0c10; }
    
    .art-cover-box {
        width: 100%; height: 200px;
        background: linear-gradient(135deg, #6d28d9 0%, #00d2ff 100%);
        border-radius: 12px; margin: 15px 0;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 8px 20px rgba(0,210,255,0.2);
    }
    .art-cover-circle {
        width: 60px; height: 60px; border: 4px solid white; border-radius: 50% 0; transform: rotate(45deg);
    }
    .art-page-box {
        width: 100%; height: 120px; border-radius: 10px; margin-bottom: 15px;
        display: flex; align-items: center; justify-content: center; font-size: 36px;
    }
    .art-p1 { background: linear-gradient(90deg, #1e3a8a, #3b82f6); }
    .art-p2 { background: linear-gradient(90deg, #311b92, #651fff); }
    .art-p3 { background: linear-gradient(90deg, #b71c1c, #ff1744); }
    .art-p4 { background: linear-gradient(90deg, #004d40, #00b0ff); }
    .art-p5 { background: linear-gradient(90deg, #374151, #111827); }
    
    .paper-sheet {
        background-color: #fdfaf2; color: #1a1b20; padding: 30px 20px;
        border-radius: 4px 20px 20px 4px; font-family: 'Georgia', serif; margin-bottom: 15px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6), inset 20px 0 15px rgba(0,0,0,0.05);
        border-left: 6px solid #2d2219;
    }
    .book-title { font-size: 24px; font-weight: bold; color: #6d28d9; margin-bottom: 12px; }
    .book-body { font-size: 18px; line-height: 1.8; text-align: justify; }
    .book-page-num { text-align: center; font-size: 13px; color: #7c7971; margin-top: 20px; border-top: 1px solid #e5e1d3; padding-top: 10px; }
    
    .lock-box {
        background-color: #11131a; border: 2px solid #ef4444; padding: 35px 20px;
        border-radius: 12px; text-align: center; color: white; margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Base de dados da história original
paginas_livro = {
    1: {
        "titulo": "Capítulo I: O Padrão Invisível", "classe_art": "art-p1", "emoji": "💻",
        "texto": "Eva Duarte ajustou os óculos enquanto as linhas de código ciano passavam pelo ecrã do seu terminal no laboratório de inteligência artificial de Lisboa. Passava pouco da meia-noite. Lá fora, a chuva batia contra as janelas altas, mas dentro daquela sala o único som era o zumbido suave dos servidores.\n\nEla trabalhava no Chronos, um modelo preditivo avançado projetado para antecipar comportamentos de consumo. Mas nas últimas três semanas, o Chronos começara a fazer algo que violava as leis da própria probabilidade. Não estava apenas a adivinhar o que as pessoas iam comprar; estava a registar dados sobre eventos de vida altamente específicos antes mesmo de eles acontecerem."
    },
    2: {
        "titulo": "Capítulo II: O Teste de Sangue", "classe_art": "art-p2", "emoji": "🔬",
        "texto": "Para provar a si mesma que estava a sofrer de exaustão, Eva decidiu fazer um teste cego. Introduziu os dados biométricos e as rotinas diárias de Tomás, o seu colega de equipa mais cético. O algoritmo processou os dados durante quatro segundos e cuspiu uma única linha de texto na consola:\n\n[PREVISÃO: Tomás Nogueira. Trauma físico por impacto mecânico. Probabilidade: 99.4%]\n\nEva engoliu em seco. Aquilo era um absurdo. Tomás era a pessoa mais prudente do world. Ela fechou o portátil e foi para casa, tentando convencer-se de que era apenas um erro matemático. Um bug complexo."
    },
    3: {
        "titulo": "Capítulo III: O Impacto", "classe_art": "art-p3", "emoji": "⚠️",
        "texto": "Na manhã seguinte, o trânsito na Avenida da Liberdade estava caótico. Eva chegou ao escritório às 08:35. Tomás já lá estava, a tomar o seu habitual café na varanda do terceiro andar. O relógio digital no canto do monitor de Eva avançava impiedosamente.\n\nÀs 08:42 exatas, um estrondo ecoou pela rua. Um camião de entregas perdeu os travões, galgou o passeio e embateu violentamente contra a estrutura de metal da varanda. O vidro estilhaçou-se. Tomás foi projetado para o chão, com o braço fraturado e o rosto coberto de cortes. Exatamente como a máquina previra."
    },
    4: {
        "titulo": "Capítulo IV: A Próxima Vítima", "classe_art": "art-p4", "emoji": "👁️",
        "texto": "O pânico paralisou as queixas de Eva enquanto a ambulância levava Tomás. De volta ao laboratório deserto, as suas mãos tremiam tanto que quase não conseguia digitar. O Chronos não era um espelho do futuro. Era um guião.\n\nCom o coração a bater no peito como um tambor frenético, Eva apagou os dados de Tomás e, lentamente, digitou o seu próprio nome no campo de análise biométrica. O servidor disparou, as ventoinhas rugiram e o ecrã piscou com caracteres vermelhos de erro antes de fixar o resultado final:\n\n[PREVISÃO: Eva Duarte. Paragem cardiorrespiratória por causas externas. Tempo restante: 23 horas, 42 minutos.]"
    },
    5: {
        "titulo": "Capítulo V: O Código Vermelho", "classe_art": "art-p5", "emoji": "🚨",
        "texto": "A contagem decrescente começou a avançar no ecrã do terminal. Os segundos desaparecerciam diante dos olhos de Eva. 23:41:59... 23:41:58...\n\nDe repente, as luzes do laboratório falharam, deixando a sala imersa numa penumbra digital, iluminada apenas pelo brilho encarnado do monitor. Passos ecoaram no corredor deserto. Alguém — ou algo — sabia que ela tinha descobriro o guião do Chronos. A maçaneta da porta começou a rodar lentamente. Eva olhar em volta, procurando uma saída, mas já era tarde demais. A porta abriu-se e..."
    }
}

# --- FLUXO DA APLICAÇÃO ---

if not st.session_state.livro_aberto:
    st.title("O ÚLTIMO ALGORITMO")
    st.subheader("A Mente Atrás da Máquina")
    st.markdown('<div class="art-cover-box"><div class="art-cover-circle"></div></div>', unsafe_allow_html=True)
    st.write("*Um thriller psicológico sobre Inteligência Artificial, destino e controlo corporativo.*")
    st.caption("Autor: Jos Soares | Edição Especial Ilustrada")
    
    if st.button("📖 ABRIR LIVRO E COMEÇAR LEITURA", use_container_width=True, type="primary"):
        st.session_state.livro_aberto = True
        st.session_state.pagina_atual = 1
        st.rerun()

else:
    num_pag = st.session_state.pagina_atual

    # BLOQUEIO DO PAYWALL SE PASSAR DA PÁGINA 5
    if num_pag > 5 and not st.session_state.comprado:
        st.markdown("""
        <div class="lock-box">
            <h3 style="color:#ef4444; margin-top:0;">🔒 CONTEÚDO BLOQUEADO</h3>
            <p style="color:#94a3b8; font-size:14px; line-height:1.4;">O tempo de Eva Duarte está a esgotar-se. Desbloqueie o acesso vitalício imediato para ler as restantes 65 páginas de puro suspense.</p>
            <h2 style="font-size:34px; color:white; margin:10px 0;">19,99€</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Uso estrito do componente nativo do Streamlit associado ao link direto reutilizável
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

    # LEITURA ATIVA DAS PÁGINAS ORIGINAL RESTAURADA
    else:
        if num_pag in paginas_livro:
            st.markdown('<div class="art-page-box ' + paginas_livro[num_pag]["classe_art"] + '">' + paginas_livro[num_pag]["emoji"] + '</div>', unsafe_allow_html=True)
            st.markdown('<div class="paper-sheet"><div class="book-title">' + paginas_livro[num_pag]["titulo"] + '</div><div class="book-body">' + paginas_livro[num_pag]["texto"].replace('\n\n', '<br><br>') + '</div><div class="book-page-num">Página ' + str(num_pag) + ' de 70</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="art-page-box art-p5">🌌</div>', unsafe_allow_html=True)
            st.markdown('<div class="paper-sheet"><div class="book-title">Capítulo ' + str(num_pag // 5 + 5) + ': A Fuga de Lisboa</div><div class="book-body">Eva recolheu o seu portátil num movimento rápido, escapando pelas escadas de emergência...</div><div class="book-page-num">Página ' + str(num_pag) + ' de 70</div></div>', unsafe_allow_html=True)

        st.write("") 

        if num_pag < 70:
            if st.button("Avançar Página ➡️", use_container_width=True, type="primary", key=f"next_p{num_pag}"):
                st.session_state.pagina_atual += 1
                st.rerun()
                
        if num_pag > 1:
            if st.button("⬅️ Anterior", use_container_width=True, key=f"prev_p{num_pag}"):
                st.session_state.pagina_atual -= 1
                st.rerun()
        else:
            if st.button("🚪 Fechar Livro", use_container_width=True, key="close_book_btn"):
                st.session_state.livro_aberto = False
                st.rerun()

# BARRA LATERAL
with st.sidebar:
    st.title("⚙️ Painel de Testes")
    pro_simulado = st.checkbox("Simular Compra Concluída", value=st.session_state.comprado)
    if pro_simulado != st.session_state.comprado:
        st.session_state.comprado = pro_simulado
        st.rerun()
    if st.button("Reiniciar Aplicação"):
        st.session_state.livro_aberto = False
        st.session_state.pagina_atual = 1
