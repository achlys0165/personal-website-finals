<template>
  <section id="hero" class="hero">
    <!-- Matrix rain canvas -->
    <canvas ref="matrixCanvas" class="matrix-canvas"></canvas>
    
    <div class="hero-content container">
      <div class="terminal-window">
        <div class="terminal-header">
          <div class="terminal-dots">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
          </div>
          <span class="terminal-title">root@kali:~#</span>
        </div>
        <div class="terminal-body">
          <p class="cmd"><span class="prompt">$ </span>whoami</p>
          <h1 class="hero-name">{{ displayName }}<span class="cursor" v-if="typing">█</span></h1>
          
          <p class="cmd" style="margin-top: 20px"><span class="prompt">$ </span>cat role.txt</p>
          <div class="role-tags">
            <span v-for="role in roles" :key="role" class="role-tag">{{ role }}</span>
          </div>
          
          <p class="cmd" style="margin-top: 20px"><span class="prompt">$ </span>./status.sh</p>
          <p class="status-line">
            <span class="status-ok">[+]</span> Currently: <span class="status-highlight">Hunting Bugs & Building Tools</span>
          </p>
          <p class="status-line">
            <span class="status-ok">[+]</span> CTF Rank: <span class="status-highlight">Top 5% Global</span>
          </p>
          <p class="status-line">
            <span class="status-ok">[+]</span> Status: <span class="status-blink">ACTIVE</span>
          </p>
          
          <div class="hero-ctas">
            <a href="#projects" class="btn"><span>View Projects</span></a>
            <a href="#contact" class="btn btn-cyan"><span>Contact Me</span></a>
          </div>
        </div>
      </div>
      
      <!-- Pixel art logo large -->
      <div class="hero-logo">
        <svg width="180" height="180" viewBox="0 0 32 32" shape-rendering="crispEdges" class="hero-svg">
          <rect width="32" height="32" fill="#000"/>
          <rect x="8" y="4" width="16" height="2" fill="#00ff41"/>
          <rect x="6" y="6" width="20" height="2" fill="#00ff41"/>
          <rect x="6" y="8" width="20" height="2" fill="#00ff41"/>
          <rect x="6" y="10" width="20" height="2" fill="#00ff41"/>
          <rect x="6" y="12" width="20" height="2" fill="#00ff41"/>
          <rect x="6" y="14" width="20" height="2" fill="#00ff41"/>
          <rect x="8" y="16" width="16" height="2" fill="#00ff41"/>
          <rect x="10" y="18" width="12" height="2" fill="#00ff41"/>
          <rect x="12" y="20" width="8" height="2" fill="#00ff41"/>
          <rect x="14" y="22" width="4" height="2" fill="#00ff41"/>
          <rect x="12" y="12" width="8" height="6" fill="#00e5ff"/>
          <rect x="13" y="8" width="2" height="4" fill="#00e5ff"/>
          <rect x="17" y="8" width="2" height="4" fill="#00e5ff"/>
          <rect x="13" y="8" width="6" height="2" fill="#00e5ff"/>
          <rect x="14" y="13" width="4" height="1" fill="#000"/>
          <rect x="15" y="14" width="2" height="2" fill="#000"/>
          <rect x="4" y="4" width="2" height="2" fill="#00e5ff"/>
          <rect x="26" y="4" width="2" height="2" fill="#00e5ff"/>
          <rect x="2" y="2" width="2" height="2" fill="#00ff41" opacity="0.4"/>
          <rect x="28" y="2" width="2" height="2" fill="#00ff41" opacity="0.4"/>
        </svg>
        <div class="logo-glow-ring"></div>
      </div>
    </div>
    
    <div class="scroll-hint">
      <span>SCROLL DOWN</span>
      <div class="scroll-arrow">▼</div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const matrixCanvas = ref(null)
const displayName = ref('')
const typing = ref(true)
const fullName = 'Alex "0xShadow" Chen'

const roles = ['Cybersecurity Student', 'Ethical Hacker', 'CTF Player', 'Developer']

let matrixInterval = null
let typeTimeout = null

// Typewriter effect
const typeWriter = (text, i = 0) => {
  if (i <= text.length) {
    displayName.value = text.slice(0, i)
    typeTimeout = setTimeout(() => typeWriter(text, i + 1), 80)
  } else {
    typing.value = false
  }
}

// Matrix rain
const initMatrix = () => {
  const canvas = matrixCanvas.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')
  
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
  
  const chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
  const fontSize = 13
  const cols = Math.floor(canvas.width / fontSize)
  const drops = Array(cols).fill(1)
  
  const draw = () => {
    ctx.fillStyle = 'rgba(2, 12, 6, 0.06)'
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    
    drops.forEach((y, i) => {
      const char = chars[Math.floor(Math.random() * chars.length)]
      const x = i * fontSize
      
      // Leading char is bright
      ctx.fillStyle = i % 7 === 0 ? '#00e5ff' : '#00ff41'
      ctx.shadowColor = '#00ff41'
      ctx.shadowBlur = drops[i] < 3 ? 8 : 0
      ctx.font = `${fontSize}px Share Tech Mono, monospace`
      ctx.fillText(char, x, y * fontSize)
      
      if (y * fontSize > canvas.height && Math.random() > 0.975) {
        drops[i] = 0
      }
      drops[i]++
    })
  }
  
  matrixInterval = setInterval(draw, 50)
}

const handleResize = () => {
  if (matrixCanvas.value) {
    matrixCanvas.value.width = window.innerWidth
    matrixCanvas.value.height = window.innerHeight
  }
}

onMounted(() => {
  initMatrix()
  setTimeout(() => typeWriter(fullName), 500)
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  clearInterval(matrixInterval)
  clearTimeout(typeTimeout)
  window.removeEventListener('resize', handleResize)
})
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  padding-top: 70px;
}

.matrix-canvas {
  position: absolute;
  inset: 0;
  opacity: 0.25;
  pointer-events: none;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 60px;
  align-items: center;
  position: relative;
  z-index: 1;
  animation: fadeInUp 0.8s ease;
}

/* Terminal Window */
.terminal-window {
  background: rgba(0, 0, 0, 0.85);
  border: 1px solid rgba(0, 255, 65, 0.3);
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 0 40px rgba(0, 255, 65, 0.1), inset 0 0 40px rgba(0, 0, 0, 0.5);
}

.terminal-header {
  background: rgba(0, 255, 65, 0.08);
  border-bottom: 1px solid rgba(0, 255, 65, 0.2);
  padding: 10px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.terminal-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 10px; height: 10px;
  border-radius: 50%;
}

.dot.red { background: #ff5f56; }
.dot.yellow { background: #ffbd2e; }
.dot.green { background: #27c93f; box-shadow: 0 0 6px #27c93f; }

.terminal-title {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.75rem;
  color: var(--text-dim);
  flex: 1;
  text-align: center;
}

.terminal-body {
  padding: 28px 32px 32px;
}

.cmd {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  color: var(--text-dim);
  margin-bottom: 8px;
}

.prompt {
  color: var(--neon-green);
  text-shadow: var(--glow-green);
}

.hero-name {
  font-family: 'Orbitron', sans-serif;
  font-size: clamp(1.4rem, 3vw, 2rem);
  font-weight: 900;
  color: var(--neon-green);
  text-shadow: var(--glow-green);
  letter-spacing: 2px;
  min-height: 2.5rem;
}

.cursor {
  animation: blink 1s step-end infinite;
  color: var(--neon-cyan);
}

.role-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 4px;
}

.role-tag {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.78rem;
  color: var(--neon-cyan);
  border: 1px solid rgba(0, 229, 255, 0.3);
  padding: 4px 12px;
  letter-spacing: 1px;
  clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

.status-line {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  color: var(--text-dim);
  margin: 4px 0;
}

.status-ok { color: var(--neon-green); }
.status-highlight { color: var(--neon-cyan); }
.status-blink {
  color: var(--neon-green);
  text-shadow: var(--glow-green);
  animation: blink 1.2s step-end infinite;
}

.hero-ctas {
  display: flex;
  gap: 16px;
  margin-top: 28px;
  flex-wrap: wrap;
}

/* Hero Logo */
.hero-logo {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-svg {
  image-rendering: pixelated;
  filter: drop-shadow(0 0 16px rgba(0, 255, 65, 0.6)) drop-shadow(0 0 32px rgba(0, 229, 255, 0.3));
  animation: pulse-glow 3s ease-in-out infinite;
  position: relative;
  z-index: 1;
}

.logo-glow-ring {
  position: absolute;
  width: 200px; height: 200px;
  border: 2px solid rgba(0, 255, 65, 0.2);
  border-radius: 50%;
  animation: spin-slow 20s linear infinite;
}

.logo-glow-ring::before {
  content: '';
  position: absolute;
  inset: 10px;
  border: 1px solid rgba(0, 229, 255, 0.15);
  border-radius: 50%;
  animation: spin-slow 10s linear infinite reverse;
}

@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Scroll hint */
.scroll-hint {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  color: var(--text-dim);
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 4px;
  z-index: 1;
}

.scroll-arrow {
  animation: bounce 2s ease infinite;
  color: var(--neon-green);
  font-size: 1rem;
  margin-top: 6px;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(8px); }
}

/* Responsive */
@media (max-width: 900px) {
  .hero-content {
    grid-template-columns: 1fr;
    text-align: left;
  }
  
  .hero-logo {
    display: none;
  }
}
</style>
