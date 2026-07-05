import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar o ecrã inteiro
st.set_page_config(page_title="AI Beatmaker Studio", layout="wide")

# O teu código do Beatmaker injetado diretamente no servidor
beatmaker_html = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Beatmaker Studio</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #0b0b0d;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        header {
            background-color: #13131a;
            padding: 20px;
            text-align: center;
            border-bottom: 2px solid #23232f;
        }
        button {
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            border: none;
            color: white;
            padding: 12px 24px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            border-radius: 25px;
            transition: transform 0.2s;
        }
        button:hover { transform: scale(1.05); }
        .game-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex-grow: 1;
            gap: 50px;
            padding: 20px;
        }
        .characters-zone {
            display: flex;
            gap: 40px;
        }
        .character {
            background-color: #1c1c24;
            border: 3px dashed #4e4e66;
            border-radius: 15px;
            padding: 30px;
            width: 130px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .character.drag-over {
            border-color: #00ffaa;
            background-color: #122c20;
            transform: scale(1.05);
        }
        .character.playing {
            border-style: solid;
            border-color: #00d2ff;
            background-color: #132533;
        }
        .character.playing .avatar {
            font-size: 65px;
            animation: bounce 0.4s infinite alternate;
        }
        .avatar {
            font-size: 55px;
            margin-bottom: 15px;
            filter: grayscale(100%);
            transition: all 0.3s;
            user-select: none;
        }
        .character.playing .avatar {
            filter: grayscale(0%);
        }
        .status {
            font-size: 14px;
            color: #a0a0b0;
            user-select: none;
        }
        .sounds-zone {
            display: flex;
            gap: 20px;
            background-color: #13131a;
            padding: 20px 40px;
            border-radius: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .sound-icon {
            background-color: #252533;
            border: 2px solid #3d3d52;
            padding: 15px 25px;
            border-radius: 25px;
            cursor: grab;
            font-weight: bold;
            user-select: none;
        }
        @keyframes bounce {
            from { transform: translateY(0); }
            to { transform: translateY(-10px); }
        }
    </style>
</head>
<body>
    <header>
        <h1>AI Beatmaker Studio 🎧</h1>
        <p>Arraste qualquer ícone de som para cima de qualquer avatar para ativar o loop!</p>
        <button id="stop-all">Parar Todos os Sons</button>
    </header>
    <main class="game-container">
        <div class="characters-zone">
            <div class="character" id="char-1" data-active-sound="">
                <div class="avatar">👤</div>
                <div class="status">Vazio</div>
            </div>
            <div class="character" id="char-2" data-active-sound="">
                <div class="avatar">👤</div>
                <div class="status">Vazio</div>
            </div>
            <div class="character" id="char-3" data-active-sound="">
                <div class="avatar">👤</div>
                <div class="status">Vazio</div>
            </div>
        </div>
        <div class="sounds-zone">
            <div class="sound-icon" draggable="true" data-sound="kick">🥁 Batida (Kick)</div>
            <div class="sound-icon" draggable="true" data-sound="snare">⚡ Ritmo (Snare)</div>
            <div class="sound-icon" draggable="true" data-sound="synth">🎹 Melodia (Synth)</div>
        </div>
    </main>
    <script>
        let audioCtx = null;
        const activeLoops = { kick: false, snare: false, synth: false };
        const bpm = 120;
        let currentBeat = 0;
        let nextNoteTime = 0.0;
        const lookahead = 25.0;
        const scheduleAheadTime = 0.1;

        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                scheduler();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
        }

        function scheduler() {
            while (nextNoteTime < audioCtx.currentTime + scheduleAheadTime) {
                scheduleBeat(currentBeat, nextNoteTime);
                advanceBeat();
            }
            setTimeout(scheduler, lookahead);
        }

        function advanceBeat() {
            currentBeat = (currentBeat + 1) % 8;
            nextNoteTime += 0.25; 
        }

        function scheduleBeat(beatNumber, time) {
            if (activeLoops['kick'] && (beatNumber === 0 || beatNumber === 4)) {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain); gain.connect(audioCtx.destination);
                osc.frequency.setValueAtTime(150, time);
                osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.15);
                gain.gain.setValueAtTime(1, time);
                gain.gain.exponentialRampToValueAtTime(0.01, time + 0.15);
                osc.start(time); osc.stop(time + 0.15);
            }
            if (activeLoops['snare'] && (beatNumber === 2 || beatNumber === 6)) {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain); gain.connect(audioCtx.destination);
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(180, time);
                gain.gain.setValueAtTime(0.7, time);
                gain.gain.exponentialRampToValueAtTime(0.01, time + 0.1);
                osc.start(time); osc.stop(time + 0.1);
            }
            if (activeLoops['synth']) {
                const notes = [261.63, 293.66, 329.63, 392.00, 329.63, 293.66, 261.63, 349.23];
                if (beatNumber % 2 === 0) { 
                    const osc = audioCtx.createOscillator();
                    const gain = audioCtx.createGain();
                    osc.connect(gain); gain.connect(audioCtx.destination);
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(notes[beatNumber], time);
                    gain.gain.setValueAtTime(0.12, time);
                    gain.gain.exponentialRampToValueAtTime(0.01, time + 0.2);
                    osc.start(time); osc.stop(time + 0.2);
                }
            }
        }

        document.addEventListener("DOMContentLoaded", () => {
            const icons = document.querySelectorAll(".sound-icon");
            const characters = document.querySelectorAll(".character");

            icons.forEach(icon => {
                icon.addEventListener("dragstart", (e) => {
                    e.dataTransfer.setData("text/plain", e.target.dataset.sound + "|" + e.target.innerText);
                });
            });

            characters.forEach(char => {
                char.addEventListener("dragover", (e) => e.preventDefault());
                char.addEventListener("dragenter", () => char.classList.add("drag-over"));
                char.addEventListener("dragleave", () => char.classList.remove("drag-over"));
                
                char.addEventListener("drop", (e) => {
                    e.preventDefault();
                    char.classList.remove("drag-over");
                    initAudio(); 
                    const data = e.dataTransfer.getData("text/plain");
                    if (!data) return;
                    const [soundType, soundText] = data.split("|");
                    const oldSound = char.dataset.activeSound;
                    if (oldSound) activeLoops[oldSound] = false;
                    activeLoops[soundType] = true;
                    char.dataset.activeSound = soundType;
                    char.classList.add("playing");
                    char.querySelector(".avatar").innerText = "🕺";
                    char.querySelector(".status").innerText = soundText;
                });

                char.addEventListener("click", () => {
                    const currentSound = char.dataset.activeSound;
                    if (currentSound) {
                        activeLoops[currentSound] = false;
                        char.dataset.activeSound = "";
                        char.classList.remove("playing");
                        char.querySelector(".avatar").innerText = "👤";
                        char.querySelector(".status").innerText = "Vazio";
                    }
                });
            });

            document.getElementById("stop-all").addEventListener("click", () => {
                Object.keys(activeLoops).forEach(key => activeLoops[key] = false);
                characters.forEach(char => {
                    char.dataset.activeSound = "";
                    char.classList.remove("playing");
                    char.querySelector(".avatar").innerText = "👤";
                    
