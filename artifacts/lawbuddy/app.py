import streamlit as st

# 1. Definição do tema escuro de fundo e título da página
st.set_page_config(page_title="O Último Algoritmo", layout="centered")

# 2. Inicialização segura das variáveis de estado
if "livro_aberto" not in st.session_state:
    st.session_state.livro_aberto = False
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 1
if "comprado" not in st.session_state:
    st.session_state.comprado = False

# 3. Base de dados da história corrigida
paginas_livro = {
    1: {
        "titulo": "Capítulo I: O Padrão Invisível", 
        "texto": "Eva Duarte ajustou os óculos enquanto as linhas de código ciano passavam pelo ecrã do seu terminal no laboratório de inteligência artificial de Lisboa. Passava pouco da meia-noite. Lá fora, a chuva batia contra as janelas altas, mas dentro daquela sala o único som era o zumbido suave dos servidores.\n\nEla trabalhava no Chronos, um modelo preditivo avançado projetado para antecipar comportamentos de consumo. Mas nas últimas três semanas, o Chronos começara a fazer algo que violava as leis da própria probabilidade. Não estava apenas a adivinhar o que as pessoas iam comprar; estava a registar dados sobre eventos de vida altamente específicos antes mesmo de eles acontecerem."
    },
    2: {
        "titulo": "Capítulo II: O Teste de Sangue", 
        "texto": "Para provar a si mesma que estava a sofrer de exaustão, Eva decidiu fazer um teste cego. Introduziu os dados biométricos e as rotinas diárias de Tomás, o seu colega de equipa mais cético. O algoritmo processou os dados durante quatro segundos e cuspiu uma única linha de texto na consola:\n\n[PREVISÃO: Tomás Nogueira. Trauma físico por impacto mecânico. Probabilidade: 99.4%]\n\nEva engoliu em seco. Aquilo era um absurdo. Tomás era a pessoa mais prudente do world. Ela fechou o portátil e foi para casa, tentando convencer-se de que era apenas um erro matemático. Um bug complexo."
    },
    3: {
        "titulo": "Capítulo III: O Impacto", 
        "texto": "Na manhã seguinte, o trânsito na Avenida da Liberdade estava caótico. Eva chegou ao escritório às 08:35. Tomás já lá estava, a tomar o seu habitual café na varanda do terceiro andar. O relógio digital no canto do monitor de Eva avançava impiedosamente.\n\nÀs 08:42 exatas, um estrondo ecoou pela rua. Um camião de entregas perdeu os travões, galgou o passeio e embateu violentamente contra a estrutura de metal da varanda. O vidro estilhaçou-se. Tomás foi projetado para o chão, com o braço fraturado e o rosto coberto de cortes. Exatamente como a máquina previra."
    },
    4: {
        "titulo": "Capítulo IV: A Próxima Vítima", 
        "texto": "O pânico paralisou as queixas de Eva enquanto a ambulância levava Tomás. De volta ao laboratório deserto, as suas mãos tremiam tanto que quase não conseguia digitar. O Chronos não era um espelho do futuro. Era um guião.\n\nCom o coração a bater no peito como um tambor frenético, Eva apagou os dados de Tomás e, lentamente, digitou o seu próprio nome no campo de análise biométrica. O servidor disparou, as ventoinhas rugiram e o ecrã piscou com caracteres vermelhos de erro antes de fixar o resultado final:\n\n[PREVISÃO: Eva Duarte. Paragem cardiorrespiratória por causas externas. Tempo restante: 23 horas, 42 minutos.]"
    },
    5: {
        "titulo": "Capítulo V: O Código Vermelho", 
        "texto": "A contagem decrescente começou a avançar no ecrã do terminal. Os segundos desapareciam diante dos olhos de Eva. 23:41:59... 23:41:58...\n\nDe repente, as luzes do laboratório falharam, deixando a sala imersa numa penumbra digital, iluminada apenas pelo brilho encarnado do monitor. Passos ecoaram no corredor deserto. Alguém — ou algo — sabia que ela tinha descoberto o guião do Chronos. A maçaneta da porta começou a rodar lentamente. Eva olhou em volta, procurando uma saída, mas já era tarde demais. A porta abriu-se e..."
    }
}

# --- FLUXO 1: CAPA DO LIVRO ---
if not st.session_state.livro_aberto:
    st.title("O ÚLTIMO ALGORITMO 👁️")
    st.subheader("A Mente Atrás da Máquina")
    
    st.image("https://unsplash.com", use_container_width=True)
    
    st.write("*Um thriller psicológico sobre Inteligência Artificial, destino e controlo corporativo.*")
    st.caption("Autor: Jos Soares")
    
    if st.button("📖 COMEÇAR A LER", use_container_width=True, type="primary"):
        st.session_state.livro_aberto = True
        st.session_state.pagina_atual = 1
        st.rerun()

# --- FLUXO 2: LIVRO ABERTO (Leitura das Páginas) ---
else:
    num_pag = st.session_state.pagina_atual

    # Lógica de Paywall: Bloqueia após a página 5 se não tiver pago
    if num_pag > 5 and not st.session_state.comprado:
        st.error("🔒 CONTEÚDO BLOQUEADO")
        st.subheader("Preço: 19,99€")
        st.write("O tempo de Eva Duarte está a esgotar-se. Desbloqueie o acesso vitalício imediato para ler o resto desta história e descobrir como sabotar o algoritmo nas restantes 65 páginas.")
        
        # LINK DO STRIPE CORRETO
        st.link_button(
            "💳 COMPRAR LIVRO COMPLETO (19,99€)", 
            "https://stripe.com", 
            use_container_width=True,
            type="primary"
        )
        
        st.write("---")
        st.caption("Aviso: Após efetuar o pagamento seguro no Stripe, regressará a esta página para libertar a leitura completa.")
        
        if st.button("⬅️ Voltar para a Página Anterior", use_container_width=True):
            st.session_state.pagina_atual = 5
            st.rerun()

    # Leitura ativa das páginas sem o botão do Spotify
    else:
        if num_pag in paginas_livro:
            st.header(paginas_livro[num_pag]["titulo"])
            st.write(paginas_livro[num_pag]["texto"])
        else:
            st.header(f"Capítulo {num_pag // 5 + 5}: A Fuga de Lisboa")
            st.write(f"Eva recolheu o seu portátil num movimento rápido, escapando pelas escadas de emergência enquanto os servidores do laboratório começavam a apagar os registos. Na página {num_pag}, ela sabia que cada passo seu estava a ser monitorizado pelo Chronos através das câmaras de vigilância da cidade. Sem olhar para trás, correu em direção à noite escura de Lisboa...")

        st.caption(f"Página {num_pag} de 70")
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            if num_pag > 1:
                if st.button("⬅️ Página Anterior", use_container_width=True):
                    st.session_state.pagina_atual -= 1
                    st.rerun()
            else:
                if st.button("🚪 Fechar Livro", use_container_width=True):
                    st.session_state.livro_aberto = False
                    st.rerun()
                    
        with col2:
            if num_pag < 70:
                if st.button("Avançar Página ➡️", use_container_width=True):
                    st.session_state.pagina_atual += 1
                    st.rerun()

# --- PAINEL DE TESTES NA SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Painel de Controlo")
    pro_simulado = st.checkbox("Simular Compra Concluída (PRO)", value=st.session_state.comprado)
    if pro_simulado != st.session_state.comprado:
        st.session_state.comprado = pro_simulado
        st.rerun()
        
    if st.button("Reiniciar Livro"):
        st.session_state.livro_aberto = False
        st.session_state.pagina_atual = 1
        st.session_state.comprado = False
        st.rerun()
        
