import streamlit as st
import streamlit.components.v1 as components

# Configuração da página em modo estendido para caber os 7 bonecos no telemóvel
st.set_page_config(page_title="AI Beatmaker Pro", layout="wide")

beatmaker_html = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { margin: 0; font-family: 'Helvetica Neue', Arial, sans-serif; background-color: #08080a; color: #ffffff; text-align: center; padding-bottom: 40px; }
        header { background-color: #111116; padding: 15px; border-bottom: 2px solid #1e1e24; }
        h1 { margin: 5px 0; font-size: 24px; letter-spacing: 1px; color: #00d2ff; }
        p { margin: 5px 0; font-size: 13px; color: #8a8a9e; }
        .control-panel { display: flex; justify-content: center; gap: 12px; margin-top: 10px; }
        
        button { border: none; color: white; padding: 10px 22px; font-size: 13px; font-weight: bold; cursor: pointer; border-radius: 20px; transition: transform 0.2s; }
        button:active { transform: scale(0.95); }
        #demo-btn { background: linear-gradient(135deg, #00f2fe, #4facfe); color: #000; }
        #stop-btn { background: linear-gradient(135deg, #ff416c, #ff4b2b); }
        
        .game-container { display: flex; flex-direction: column; align-items: center; padding: 15px; gap: 25px; }
        
        /* Grelha de 7 Avatares - Responsiva para ecrãs de telemóvel */
        .characters-zone { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; width: 100%; max-width: 600px; }
        @media (min-width: 480px) { .characters-zone { grid-template-columns: repeat(7, 1fr); } }
        
        .character { background-color: #14141c; border: 2px dashed #3a3a4a; border-radius: 10px; padding: 12px 2px; text-align: center; transition: all 0.2s ease; }
        .character.playing { border-style: solid; background-color: #121e2b; }
        
        /* Cores temáticas para as bordas dos avatares ativos baseadas no Incredibox */
        #visual-b1.playing { border-color: #ff3366; }
        #visual-b2.playing { border-color: #ff6633; }
        #visual-e1.playing { border-color: #ffcc00; }
        #visual-m1.playing { border-color: #33cc66; }
        #visual-m2.playing { border-color: #00ffcc; }
        #visual-k1.playing { border-color: #0099ff; }
        #visual-v1.playing { border-color: #b333ff; }
        
        .avatar { font-size: 32px; filter: grayscale(100%); transition: all 0.2s; user-select: none; }
        .character.playing .avatar { filter: grayscale(0%); animation: bounce 0.38s infinite alternate cubic-bezier(0.45, 0.05, 0.55, 0.95); }
        .status { font-size: 10px; color: #7c7c90; margin-top: 4px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
        
        /* Zona de Instrumentos de Toque Direto */
        .sounds-zone { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; background-color: #111116; padding: 12px; border-radius: 20px; width: 100%; max-width: 600px; box-sizing: border-box; }
        @media (min-width: 480px) { .sounds-zone { grid-template-columns: repeat(7, 1fr); } }
        
        .sound-icon { background-color: #22222e; border: 2px solid #323242; padding: 12px 2px; border-radius: 12px; cursor: pointer; font-weight: bold; font-size: 11px; text-align: center; transition: all 0.15s; }
        
        /* Cores individuais dos botões estilo Categorias do Jogo */
        #btn-b1.active { background-color: #ff3366; color: #fff; border-color: #fff; }
        #btn-b2.active { background-color: #ff6633; color: #fff; border-color: #fff; }
        #btn-e1.active { background-color: #ffcc00; color: #000; border-color: #fff; }
        #btn-m1.active { background-color: #33cc66; color: #fff; border-color: #fff; }
        #btn-m2.active { background-color: #00ffcc; color: #000; border-color: #fff; }
        #btn-k1.active { background-color: #0099ff; color: #fff; border-color: #fff; }
        #btn-v1.active { background-color: #b333ff; color: #fff; border-color: #fff; }
        
        @keyframes bounce { from { transform: translateY(0) scale(1); } to { transform: translateY(-6px) scale(1.05); } }
    </style>
</head>
<body>
    <header>
        <h1>AI Beatmaker Pro 🎧</h1>
        <p>Toque diretamente nos botões coloridos abaixo para ligar/desligar as pistas!</p>
        <div class="control-panel">
            <button id="demo-btn">Mix Completo 🎲</button>
            <button id="stop-btn">Parar Tudo</button>
        </div>
    </header>
    <main class="game-container">
        
        <!-- CORPO INTEGRADO DE 7 AVATARES -->
        <div class="characters-zone">
            <div class="character" id="visual-b1"><div class="avatar">👤</div><div class="status">Off</div></div>
            <div class="character" id="visual-b2"><div class="avatar">👤</div><div class="status">Off</div></div>
            <div class="character" id="visual-e1"><div class="avatar">👤</div><div class="status">Off</div></div>
            <div class="character" id="visual-m1"><div class="avatar">👤</div><div class="status">Off</div></div>
            <div class="character" id="visual-m2"><div class="avatar">👤</div><div class="status">Off</div></div>
            <div class="character" id="visual-k1"><div class="avatar">👤</div><div class="status">Off</div></div>
            <div class="character" id="visual-v1"><div class="avatar">👤</div><div class="status">Off</div></div>
        </div>
        
        <!-- PAINEL DE 7 INSTRUMENTOS SEPARADOS POR CATEGORIAS -->
        <div class="sounds-zone">
            <div class="sound-icon" id="btn-b1" data-sound="b1">🥁 Beat 1</div>
            <div class="sound-icon" id="btn-b2" data-sound="b2">🥁 Beat 2</div>
            <div class="sound-icon" id="btn-e1" data-sound="e1">✨ Efeito</div>
            <div class="sound-icon" id="btn-m1" data-sound="m1">🎹 Synth 1</div>
            <div class="sound-icon" id="btn-m2" data-sound="m2">🎸 Baixo</div>
            <div class="sound-icon" id="btn-k1" data-sound="k1">⚡ Caixa</div>
            <div class="sound-icon" id="btn-v1" data-sound="v1">🎤 Voz</div>
        </div>
    </main>
    <script>
        let audioCtx = null;
        const activeLoops = { b1: false, b2: false, e1: false, m1: false, m2: false, k1: false, v1: false };
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
            while (nextNoteTime < audioCtx.currentTime + 0.08) {
                triggerInstruments(currentBeat, nextNoteTime);
                currentBeat = (currentBeat + 1) % 8;
                nextNoteTime += 0.22; // 136 BPM para um ritmo mais dançante e polido
            }
            setTimeout(runScheduler, 20);
        }

        // Sintetizadores matemáticos nativos em tempo real para cada uma das 7 pistas
        function triggerInstruments(beatNumber, time) {
            // Pista 1: Batida Principal (Kick)
            if (activeLoops['b1'] && (beatNumber === 0 || beatNumber === 4)) {
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                osc.frequency.setValueAtTime(110, time); osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.16);
                gain.gain.setValueAtTime(1, time); gain.gain.exponentialRampToValueAtTime(0.01, time + 0.16);
                osc.start(time); osc.stop(time + 0.16);
            }
            // Pista 2: Batida Secundária (Percussão Alternada)
            if (activeLoops['b2'] && (beatNumber === 2 || beatNumber === 6)) {
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                osc.frequency.setValueAtTime(75, time); osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.2);
                gain.gain.setValueAtTime(0.8, time); gain.gain.exponentialRampToValueAtTime(0.01, time + 0.2);
                osc.start(time); osc.stop(time + 0.2);
            }
            // Pista 3: Efeitos Espaciais (Arpejo Agudo)
            if (activeLoops['e1'] && beatNumber === 7) {
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                osc.type = 'triangle'; osc.frequency.setValueAtTime(880, time);
                osc.frequency.linearRampToValueAtTime(1200, time + 0.15);
                gain.gain.setValueAtTime(0.15, time); gain.gain.exponentialRampToValueAtTime(0.001, time + 0.15);
                osc.start(time); osc.stop(time + 0.15);
            }
            // Pista 4: Synth de Acordes Harmonizados
            if (activeLoops['m1'] && beatNumber % 2 === 0) {
                const chords = [261.63, 329.63, 392.00, 349.23];
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                osc.type = 'sine'; osc.frequency.setValueAtTime(chords[beatNumber / 2 % 4], time);
                gain.gain.setValueAtTime(0.16, time); gain.gain.exponentialRampToValueAtTime(0.01, time + 0.2);
                osc.start(time); osc.stop(time + 0.2);
            }
            // Pista 5: Linha de Baixo Pesado (Sub-bass)
            if (activeLoops['m2']) {
                const bassNotes = [65.41, 65.41, 82.41, 98.00, 87.31, 87.31, 73.42, 98.00];
                const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain(); osc.connect(gain); gain.connect(audioCtx.destination);
                
