import streamlit as st

st.set_page_config(page_title="Incredibox Pro Clone", layout="wide")

# Interface Avançada com Loops de Alta Fidelidade Reais via CDN e Howler.js
incredibox_pro_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <!-- Biblioteca de Áudio Profissional Usada por Jogos Web -->
    <script src="https://cloudflare.com"></script>
    <style>
        .studio-box { background: #0b0b10; padding: 20px; border-radius: 16px; text-align: center; font-family: 'Segoe UI', Arial; color: white; border: 1px solid #1f1f2e; }
        .studio-title { font-size: 26px; font-weight: bold; color: #00d2ff; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; }
        .studio-p { font-size: 13px; color: #7e7e9a; margin-bottom: 20px; }
        
        .control-bar { display: flex; justify-content: center; gap: 12px; margin-bottom: 25px; }
        .main-btn { border: none; padding: 12px 24px; font-size: 14px; font-weight: bold; cursor: pointer; border-radius: 25px; color: white; transition: all 0.2s; }
        #mix-btn { background: linear-gradient(135deg, #00f2fe, #4facfe); color: black; }
        #clear-btn { background: linear-gradient(135deg, #ff416c, #ff4b2b); }
        .main-btn:active { transform: scale(0.95); }

        .crew-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 30px; }
        .beatboxer { background: #14141f; border: 2px dashed #3a3a4f; padding: 15px 5px; border-radius: 12px; transition: all 0.3s ease; }
        
        /* Cores de Ativação do Palco Estilo Incredibox */
        #c1.active { border-color: #ff3366; background: #20131b; }
        #c2.active { border-color: #00ffcc; background: #112220; }
        #c3.active { border-color: #ffcc00; background: #222011; }
        #c4.active { border-color: #b333ff; background: #1c1122; }
        
        .b-avatar { font-size: 42px; filter: grayscale(100%); transition: all 0.3s; user-select: none; }
        .beatboxer.active .b-avatar { filter: grayscale(0%); animation: dance 0.42s infinite alternate cubic-bezier(0.25, 0.46, 0.45, 0.94); }
        .b-status { font-size: 11px; color: #6e6e8a; margin-top: 6px; text-transform: uppercase; font-weight: bold; }
        .beatboxer.active .b-status { color: #fff; }

        .deck-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; background: #111116; padding: 15px; border-radius: 24px; border: 1px solid #1f1f2e; }
        .sound-pad { background: #1f1f2e; border: 2px solid #2e2e42; padding: 15px 5px; border-radius: 16px; color: white; cursor: pointer; font-weight: bold; font-size: 12px; transition: all 0.2s; }
        
        /* Cores Customizadas dos Pads de Instrumentos */
        #pad1.on { background: #ff3366; border-color: white; box-shadow: 0 0 10px rgba(255,51,102,0.5); }
        #pad2.on { background: #00ffcc; color: black; border-color: white; box-shadow: 0 0 10px rgba(0,255,204,0.5); }
        #pad3.on { background: #ffcc00; color: black; border-color: white; box-shadow: 0 0 10px rgba(255,204,0,0.5); }
        #pad4.on { background: #b333ff; border-color: white; box-shadow: 0 0 10px rgba(179,51,255,0.5); }

        @keyframes dance { from { transform: translateY(0) scale(1); } to { transform: translateY(-8px) scale(1.04); } }
    </style>
</head>
<body>
    <div class="studio-box">
        <div class="studio-title">Incredibox Pro Studio 🎧</div>
        <div class="studio-p">Loops Reais de Alta Fidelidade (HQ) - Toque nos pads coloridos para construir a sua Crew!</div>
        
        <div class="control-bar">
            <button class="main-btn" id="mix-btn">Drop Completo 🎲</button>
            <button class="main-btn" id="clear-btn">Parar Crew</button>
        </div>

        <!-- 4 BEATBOXERS NO PALCO -->
        <div class="crew-grid">
            <div class="beatboxer" id="c1"><div class="b-avatar">👤</div><div class="b-status">Mudo</div></div>
            <div class="beatboxer" id="c2"><div class="b-avatar">👤</div><div class="b-status">Mudo</div></div>
            <div class="beatboxer" id="c3"><div class="b-avatar">👤</div><div class="b-status">Mudo</div></div>
            <div class="beatboxer" id="c4"><div class="b-avatar">👤</div><div class="b-status">Mudo</div></div>
        </div>

        <!-- MESA DE RITMO COM LOOPS DE ESTÚDIO REAIS (MP3 HQ) -->
        <div class="deck-grid">
            <button class="sound-pad" id="pad1">🥁 BEAT INDUSTRIAL</button>
            <button class="sound-pad" id="pad2">🎸 BAIXO DEEP</button>
            <button class="sound-pad" id="pad3">🎹 SYNTH LEAD</button>
            <button class="sound-pad" id="pad4">🎤 TECHNO VOCAL</button>
        </div>
    </div>

    <script>
        // Carregamento de ficheiros áudio reais profissionais (Loops perfeitamente sincronizados a 125 BPM)
        const tracks = {
            pad1: new Howl({ src: ['https://google.com'], loop: true, volume: 0.85, html5: true }),
            pad2: new Howl({ src: ['https://google.com'], loop: true, volume: 0.90, html5: true }),
            pad3: new Howl({ src: ['https://google.com'], loop: true, volume: 0.75, html5: true }),
            pad4: new Howl({ src: ['https://google.com'], loop: true, volume: 0.80, html5: true })
        };

        const state = { pad1: false, pad2: false, pad3: false, pad4: false };
        const meta = {
            pad1: { char: 'c1', label: 'Rhythm', emo: '🕺' },
            pad2: { char: 'c2', label: 'Bassline', emo: '💃' },
            pad3: { char: 'c3', label: 'Melody', emo: '🎹' },
            pad4: { char: 'c4', label: 'Vocal', emo: '🎤' }
        };

        function toggleTrack(id) {
            // Desbloqueia de imediato o motor de áudio no telemóvel através do evento de toque
            if (Howler.ctx && Howler.ctx.state === 'suspended') { Howler.ctx.resume(); }
            
            state[id] = !state[id];
            const padElement = document.getElementById(id);
            const charElement = document.getElementById(meta[id].char);

            if (state[id]) {
                tracks[id].play();
                padElement.classList.add('on');
                charElement.classList.add('active');
                charElement.querySelector('.b-avatar').innerText = meta[id].emo;
                charElement.querySelector('.b-status').innerText = meta[id].label;
            } else {
                tracks[id].stop();
                padElement.classList.remove('on');
                charElement.classList.remove('active');
                charElement.querySelector('.b-avatar').innerText = '👤';
                charElement.querySelector('.b-status').innerText = 'Mudo';
            }
        }

        // Configuração dos gatilhos de clique/toque direto nos botões
        document.getElementById('pad1').onclick = () => toggleTrack('pad1');
        document.getElementById('pad2').onclick = () => toggleTrack('pad2');
        document.getElementById('pad3').onclick = () => toggleTrack('pad3');
        document.getElementById('pad4').onclick = () => toggleTrack('pad4');

        // Botão para disparar o arranjo completo com todas as pistas em sincronia
        document.getElementById('mix-btn').onclick = () => {
            if (Howler.ctx && Howler.ctx.state === 'suspended') { Howler.ctx.resume(); }
            Object.keys(tracks).forEach(id => {
                if (!state[id]) toggleTrack(id);
            });
        };

        // Botão para limpar o palco e cortar todas as frequências imediatamente
        document.getElementById('clear-btn').onclick = () => {
            Object.keys(tracks).forEach(id => {
                if (state[id]) toggleTrack(id);
            });
        };
    </script>
</body>
</html>
"""

st.markdown(incredibox_pro_html, unsafe_allow_html=True)
