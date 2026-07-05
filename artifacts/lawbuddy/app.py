import streamlit as st
import streamlit.components.v1 as components

# Forçar a página a carregar no modo largo para o telemóvel
st.set_page_config(page_title="AI Beatmaker Studio", layout="wide")

# O código do jogo otimizado com interface de botões diretos de 1 clique
beatmaker_html = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { margin: 0; font-family: Arial, sans-serif; background-color: #0b0b0d; color: #ffffff; text-align: center; padding-bottom: 30px; }
        header { background-color: #13131a; padding: 15px; border-bottom: 2px solid #23232f; }
        h1 { margin: 5px 0; font-size: 22px; }
        .control-panel { display: flex; justify-content: center; gap: 10px; margin-top: 10px; }
        button { background: linear-gradient(135deg, #00f2fe, #4facfe); border: none; color: white; padding: 10px 20px; font-size: 14px; font-weight: bold; cursor: pointer; border-radius: 20px; }
        #stop-btn { background: linear-gradient(135deg, #ff416c, #ff4b2b); }
        .game-container { display: flex; flex-direction: column; align-items: center; padding: 20px; gap: 30px; }
        .characters-zone { display: flex; gap: 15px; justify-content: center; width: 100%; max-width: 480px; }
        .character { background-color: #1c1c24; border: 2px dashed #4e4e66; border-radius: 12px; padding: 15px 5px; flex: 1; text-align: center; transition: all 0.2s ease; }
        .character.playing { border-style: solid; border-color: #00d2ff; background-color: #132533; }
        .avatar { font-size: 40px; margin-bottom: 8px; filter: grayscale(100%); transition: all 0.2s; user-select: none; }
        .character.playing .avatar { filter: grayscale(0%); animation: bounce 0.4s infinite alternate; }
        .status { font-size: 11px; color: #a0a0b0; }
        .sounds-zone { display: flex; gap: 10px; background-color: #13131a; padding: 15px; border-radius: 25px; width: 100%; max-width: 480px; box-sizing: border-box; }
        .sound-icon { background-color: #252533; border: 2px solid #3d3d52; padding: 15px 5px; border-radius: 15px; cursor: pointer; font-weight: bold; font-size: 13px; flex: 1; text-align: center; }
        .sound-icon.active { background-color: #00d2ff; color: #0b0b0d; border-color: #ffffff; }
        @keyframes bounce { from { transform: translateY(0); } to { transform: translateY(-8px); } }
    </style>
</head>
<body>
    <header>
        <h1>AI Beatmaker Studio 🎧</h1>
        <div class="control-panel">
            <button id="demo-btn">Tocar Todos 🎲</button>
            <button id="stop-btn">Limpar Tudo</button>
        </div>
    </header>
    <main class="game-container">
        <!-- ZONA DE VISUALIZAÇÃO DOS DANÇARINOS -->
        <div class="characters-zone">
            <div class="character" id="visual-kick"><div class="avatar">👤</div><div class="status">Desativado</div></div>
            <div class="character" id="visual-snare"><div class="avatar">👤</div><div class="status">Desativado</div></div>
            <div class="character" id="visual-synth"><div class="avatar">👤</div><div class="status">Desativado</div></div>
        </div>
        <!-- ZONA DOS BOTÕES DE SOM DIRETOS -->
        <div class="sounds-zone">
            <div class="sound-icon" id="btn-kick" data-sound="kick">🥁 Batida</div>
            <div class="sound-icon" id="btn-snare" data-sound="snare">⚡ Caixa</div>
            <div class="sound-icon" id="btn-synth" data-sound="synth">🎹 Melodia</div>
        </div>
    </main>
    <script>
        let audioCtx = null;
        const activeLoops = { kick: false, snare: false, synth: false };
        let currentBeat = 0;
        let nextNoteTime = 0.0;

        function startAudioEngine() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                runScheduler();
            }
            if (audioCtx.state === 'suspended') { audioCtx.resume(); }
        }

        function runScheduler() {
            while (nextNoteTime < audioCtx.currentTime + 0.1) {
                triggerInstruments(currentBeat, nextNoteTime);
                currentBeat = (currentBeat + 1) % 8;
                nextNoteTime += 0.25;
            }
            setTimeout(runScheduler, 25);
        }

        function triggerInstruments(beatNumber, time) {
            if (activeLoops['kick'] && (beatNumber === 0 || beatNumber === 4)) {
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                osc.frequency.setValueAtTime(120, time); osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.15);
                gain.gain.setValueAtTime(1, time); gain.gain.exponentialRampToValueAtTime(0.01, time + 0.15);
                osc.start(time); osc.stop(time + 0.15);
            }
            if (activeLoops['snare'] && (beatNumber === 2 || beatNumber === 6)) {
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                osc.type = 'triangle'; osc.frequency.setValueAtTime(170, time);
                gain.gain.setValueAtTime(0.5, time); gain.gain.exponentialRampToValueAtTime(0.01, time + 0.12);
                osc.start(time); osc.stop(time + 0.12);
            }
            if (activeLoops['synth'] && beatNumber % 2 === 0) {
                const scale = [261.63, 329.63, 392.00, 523.25];
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                osc.type = 'sine'; osc.frequency.setValueAtTime(scale[beatNumber / 2 % 4], time);
                gain.gain.setValueAtTime(0.18, time); gain.gain.exponentialRampToValueAtTime(0.01, time + 0.22);
                osc.start(time); osc.stop(time + 0.22);
            }
        }

        function toggleSound(type) {
            startAudioEngine();
            activeLoops[type] = !activeLoops[type];
            
            const btn = document.getElementById('btn-' + type);
            const view = document.getElementById('visual-' + type);
            
            if (activeLoops[type]) {
                btn.classList.add('active');
                view.classList.add('playing');
                view.querySelector('.avatar').innerText = "🕺";
                view.querySelector('.status').innerText = "A tocar...";
            } else {
                btn.classList.remove('active');
                view.classList.remove('playing');
                view.querySelector('.avatar').innerText = "👤";
                view.querySelector('.status').innerText = "Desativado";
            }
        }

        document.addEventListener("DOMContentLoaded", () => {
            document.getElementById('btn-kick').addEventListener('click', () => toggleSound('kick'));
            document.getElementById('btn-snare').addEventListener('click', () => toggleSound('snare'));
            document.getElementById('btn-synth').addEventListener('click', () => toggleSound('synth'));

            document.getElementById('demo-btn').addEventListener('click', () => {
                startAudioEngine();
                ['kick', 'snare', 'synth'].forEach(type => {
                    activeLoops[type] = true;
                    document.getElementById('btn-' + type).classList.add('active');
                    const view = document.getElementById('visual-' + type);
                    view.classList.add('playing');
                    view.querySelector('.avatar').innerText = "🕺";
                    view.querySelector('.status').innerText = "A tocar...";
                });
            });

            document.getElementById('stop-btn').addEventListener('click', () => {
                ['kick', 'snare', 'synth'].forEach(type => {
                    activeLoops[type] = false;
                    document.getElementById('btn-' + type).classList.remove('active');
                    const view = document.getElementById('visual-' + type);
                    view.classList.remove('playing');
                    view.querySelector('.avatar').innerText = "👤";
                    view.querySelector('.status').innerText = "Desativado";
                });
            });
        });
    </script>
</body>
</html>
"""

# IMPORTANTE: allow="autoplay" adicionado para dar permissão de som direta no telemóvel
components.html(beatmaker_html, height=650, scrolling=False)
