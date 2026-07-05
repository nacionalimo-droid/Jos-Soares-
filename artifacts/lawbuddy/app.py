body {
    margin: 0;
    font-family: 'Arial', sans-serif;
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
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.character.drag-over {
    border-color: #00ffaa;
    background-color: #122c20;
    transform: scale(1.05);
}

/* Animação quando o som está ativo (Efeito Incredibox) */
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
}

.character.playing .avatar {
    filter: grayscale(0%);
}

.status {
    font-size: 14px;
    color: #a0a0b0;
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
    transition: background 0.2s;
}

.sound-icon:hover { background-color: #323247; }

@keyframes bounce {
    from { transform: translateY(0); }
    to { transform: translateY(-10px); }
}
