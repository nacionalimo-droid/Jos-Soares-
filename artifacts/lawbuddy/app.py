import streamlit as st
st.set_page_config(page_title="AI Beatmaker Pro", layout="wide")
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .box { background:#13131a; padding:15px; border-radius:12px; text-align:center; font-family:Arial; color:white; }
        .grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:20px 0; }
        .char { background:#1c1c24; border:2px dashed #4e4e66; padding:10px; border-radius:8px; }
        .char.on { border-style:solid; border-color:#00d2ff; background:#132533; }
        .char.on .av { animation:b 0.4s infinite alternate; }
        .btn { background:#252533; border:2px solid #3d3d52; padding:10px; border-radius:10px; color:white; cursor:pointer; font-weight:bold; }
        .btn.on { background:#00d2ff; color:black; }
        @keyframes b { from{transform:translateY(0);} to{transform:translateY(-6px);} }
    </style>
</head>
<body>
    <div class="box">
        <h2>AI Beatmaker Pro 🎧</h2>
        <button class="btn" id="all-btn" style="background:#ff416c;color:white;">Tocar Todos 🎲</button>
        <div class="grid">
            <div class="char" id="c1"><div class="av">👤</div><small>Off</small></div>
            <div class="char" id="c2"><div class="av">👤</div><small>Off</small></div>
            <div class="char" id="c3"><div class="av">👤</div><small>Off</small></div>
            <div class="char" id="c4"><div class="av">👤</div><small>Off</small></div>
        </div>
        <div class="grid">
            <button class="btn s-btn" id="b1">🥁 B1</button>
            <button class="btn s-btn" id="b2">⚡ B2</button>
            <button class="btn s-btn" id="b3">🎹 Synth</button>
            <button class="btn s-btn" id="b4">🎤 Voz</button>
        </div>
    </div>
    <script>
        let ctx = null, beats = {b1:false,b2:false,b3:false,b4:false}, step = 0, time = 0;
        function init() { if(!ctx){ctx=new(window.AudioContext||window.webkitAudioContext)();loop();} if(ctx.state==='suspended')ctx.resume(); }
        function loop() { while(time<ctx.currentTime+0.1){play(step,time); step=(step+1)%8; time+=0.23;} setTimeout(loop,25); }
        function play(s,t) {
            if(beats.b1&&(s==0||s==4)){let o=ctx.createOscillator(),g=ctx.createGain();o.connect(g);g.connect(ctx.destination);o.frequency.setValueAtTime(110,t);o.frequency.exponentialRampToValueAtTime(0.01,t+0.15);g.gain.setValueAtTime(1,t);g.gain.exponentialRampToValueAtTime(0.01,t+0.15);o.start(t);o.stop(t+0.15);}
            if(beats.b2&&(s==2||s==6)){let o=ctx.createOscillator(),g=ctx.createGain();o.connect(g);g.connect(ctx.destination);o.type='triangle';o.frequency.setValueAtTime(160,t);g.gain.setValueAtTime(0.6,t);g.gain.exponentialRampToValueAtTime(0.01,t+0.12);o.start(t);o.stop(t+0.12);}
            if(beats.b3&&s%2==0){let notes=[261,329,392,523],o=ctx.createOscillator(),g=ctx.createGain();o.connect(g);g.connect(ctx.destination);o.frequency.setValueAtTime(notes[s/2%4],t);g.gain.setValueAtTime(0.2,t);g.gain.exponentialRampToValueAtTime(0.01,t+0.2);o.start(t);o.stop(t+0.2);}
            if(beats.b4&&s%2!=0){let notes=[349,440,523,392],o=ctx.createOscillator(),g=ctx.createGain();o.connect(g);g.connect(ctx.destination);o.type='triangle';o.frequency.setValueAtTime(notes[Math.floor(s/2)%4],t);g.gain.setValueAtTime(0.12,t);g.gain.exponentialRampToValueAtTime(0.01,t+0.18);o.start(t);o.stop(t+0.18);}
        }
        function toggle(id,lbl,emo) { init(); beats[id]=!beats[id]; let b=document.getElementById(id),c=document.getElementById('c'+id.slice(1)); if(beats[id]){b.classList.add('on');c.classList.add('on');c.querySelector('.av').innerText=emo;c.querySelector('small').innerText=lbl;}else{b.classList.remove('on');c.classList.remove('on');c.querySelector('.av').innerText='👤';c.querySelector('small').innerText='Off';} }
        document.getElementById('b1').onclick=()=>toggle('b1','Batida 1','🕺');
        document.getElementById('b2').onclick=()=>toggle('b2','Batida 2','💃');
        document.getElementById('b3').onclick=()=>toggle('b3','Synth','🎹');
        document.getElementById('b4').onclick=()=>toggle('b4','Voz','🎤');
        document.getElementById('all-btn').onclick=()=> { init(); let list=[{id:'b1',n:'Batida 1',e:'🕺'},{id:'b2',n:'Batida 2',e:'💃'},{id:'b3',n:'Synth',e:'🎹'},{id:'b4',n:'Voz',e:'🎤'}]; list.forEach(i=>{beats[i.id]=false;toggle(i.id,i.n,i.e);}); };
    </script>
</body>
</html>
"""
st.markdown(html_code, unsafe_allow_html=True)
