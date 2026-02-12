# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:38:24 2026

@author: ompha
"""

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bianca ❤️</title>

<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
*{
  margin:0;
  padding:0;
  box-sizing:border-box;
}

body{
  font-family:'Poppins',sans-serif;
  height:100vh;
  overflow:hidden;
  background: radial-gradient(circle at top, #1a002b, #000);
  color:white;
  display:flex;
  justify-content:center;
  align-items:center;
  text-align:center;
}

canvas{
  position:fixed;
  top:0;
  left:0;
  z-index:-1;
}

.container{
  max-width:800px;
  padding:20px;
  animation:fadeIn 1.5s ease forwards;
}

h1,h2{
  font-family:'Cinzel',serif;
  letter-spacing:2px;
}

h1{
  font-size:3rem;
  background:linear-gradient(90deg,#ff2e92,#9b5cff);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}

p{
  margin-top:20px;
  font-size:1.1rem;
  line-height:1.6;
  opacity:0.85;
}

button{
  margin-top:30px;
  padding:14px 30px;
  border:none;
  border-radius:40px;
  font-weight:600;
  cursor:pointer;
  transition:0.3s;
  font-size:1rem;
}

.yes{
  background:linear-gradient(45deg,#ff2e92,#ff6a00);
  color:white;
  box-shadow:0 0 20px #ff2e92;
}

.yes:hover{
  transform:scale(1.1);
  box-shadow:0 0 40px #ff2e92;
}

.no{
  background:white;
  color:black;
  position:absolute;
}

.hidden{
  display:none;
}

.timeline{
  margin-top:40px;
  font-size:1.3rem;
  letter-spacing:3px;
  animation:glow 2s infinite alternate;
}

@keyframes glow{
  from{text-shadow:0 0 10px #ff2e92;}
  to{text-shadow:0 0 30px #9b5cff;}
}

@keyframes fadeIn{
  from{opacity:0;transform:translateY(20px);}
  to{opacity:1;transform:translateY(0);}
}

.final{
  font-size:1.5rem;
  animation:pulse 2s infinite;
}

@keyframes pulse{
  0%{transform:scale(1);}
  50%{transform:scale(1.05);}
  100%{transform:scale(1);}
}
</style>
</head>

<body>

<canvas id="particles"></canvas>

<audio id="music" loop>
  <source src="https://raw.githubusercontent.com/MrOTheAnalyst/repo01/main/iloveyou.mpeg" type="audio/mpeg">
</audio>

<div class="container" id="page1">
  <h1>Bianca ❤️</h1>
  <p>Will you be my Valentine?</p>
  <button class="yes" onclick="startLove()">YES 💍</button>
  <button class="no" id="noBtn">No</button>
</div>

<div class="container hidden" id="page2">
  <h2>One More Thing...</h2>
  <p>There's a special Valentine's message waiting for you.</p>
  <button class="yes" onclick="nextPage(3)">READ YOUR LETTER 💌</button>
</div>

<div class="container hidden" id="page3">
  <h2>When I First Saw You</h2>
  <p>
    From the moment our eyes met, I knew there was something special about you.<br>
    Something worth waiting for.
  </p>
  <button class="yes" onclick="nextPage(4)">Next →</button>
</div>

<div class="container hidden" id="page4">
  <h2>Every Moment Together</h2>
  <p>
    Through laughter, conversations, and quiet moments —<br>
    every second with you has been a gift I treasure.
  </p>
  <button class="yes" onclick="nextPage(5)">Next →</button>
</div>

<div class="container hidden" id="page5">
  <h2>From Grade Strangers → Lovers</h2>
  <div class="timeline">2022 ✦ 2026</div>
  <button class="yes" onclick="nextPage(6)">Next →</button>
</div>

<div class="container hidden" id="page6">
  <h2>I Choose You, Bianca ❤️</h2>
  <p>
    Loving you was never a question.<br>
    It was patience. Timing. Trusting life would meet us halfway.<br><br>
    You are my peace. My safe place. My heart.<br><br>
    This isn't a moment.<br>
    It's a continuation.
  </p>
  <button class="yes" onclick="nextPage(7)">Final Message →</button>
</div>

<div class="container hidden final" id="page7">
  <h1>QUEEN OF MY HEART</h1>
  <p>
    Pretty face… I can't wait to kiss those cheeks 😘<br><br>
    I choose you.<br>
    My forever. My home.
  </p>
</div>

<script>
function startLove(){
  document.getElementById("page1").classList.add("hidden");
  document.getElementById("page2").classList.remove("hidden");

  let music=document.getElementById("music");
  music.muted=false;
  music.play().catch(()=>{}); // Catch autoplay errors on mobile
}

function nextPage(num){
  for(let i=2;i<=7;i++){
    let p=document.getElementById("page"+i);
    if(p) p.classList.add("hidden");
  }
  document.getElementById("page"+num).classList.remove("hidden");
}

// NO BUTTON ESCAPE
let noBtn=document.getElementById("noBtn');
noBtn.addEventListener("mouseover",moveNo);
noBtn.addEventListener("touchstart",moveNo); // mobile touch support

function moveNo(){
  noBtn.style.top=Math.random()*80+"vh";
  noBtn.style.left=Math.random()*80+"vw";
}

// PARTICLES
const canvas=document.getElementById("particles");
const ctx=canvas.getContext("2d");

function resizeCanvas(){
  canvas.width=window.innerWidth;
  canvas.height=window.innerHeight;
}
window.addEventListener('resize',resizeCanvas);
resizeCanvas();

let particles=[];
for(let i=0;i<100;i++){
  particles.push({
    x:Math.random()*canvas.width,
    y:Math.random()*canvas.height,
    r:Math.random()*2+1,
    d:Math.random()*1
  });
}

function draw(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  ctx.fillStyle="rgba(255,46,146,0.7)";
  ctx.beginPath();
  for(let i=0;i<particles.length;i++){
    let p=particles[i];
    ctx.moveTo(p.x,p.y);
    ctx.arc(p.x,p.y,p.r,0,Math.PI*2,true);
  }
  ctx.fill();
  update();
}

function update(){
  for(let i=0;i<particles.length;i++){
    let p=particles[i];
    p.y+=p.d;
    if(p.y>canvas.height){
      p.y=0;
      p.x=Math.random()*canvas.width;
    }
  }
}

setInterval(draw,33);
</script>

</body>
</html>
