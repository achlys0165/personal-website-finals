<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="nav-container">
      <a href="#hero" class="nav-logo">
        <svg width="28" height="28" viewBox="0 0 32 32" shape-rendering="crispEdges">
          <rect width="32" height="32" fill="#000"/>
          <rect x="8" y="4" width="16" height="2" fill="#00ff41"/>
          <rect x="6" y="6" width="20" height="2" fill="#00ff41"/>
          <rect x="6" y="8" width="20" height="8" fill="#00ff41"/>
          <rect x="8" y="16" width="16" height="2" fill="#00ff41"/>
          <rect x="10" y="18" width="12" height="2" fill="#00ff41"/>
          <rect x="12" y="20" width="8" height="2" fill="#00ff41"/>
          <rect x="14" y="22" width="4" height="2" fill="#00ff41"/>
          <rect x="12" y="10" width="8" height="6" fill="#00e5ff"/>
          <rect x="13" y="7" width="2" height="3" fill="#00e5ff"/>
          <rect x="17" y="7" width="2" height="3" fill="#00e5ff"/>
          <rect x="13" y="7" width="6" height="2" fill="#00e5ff"/>
          <rect x="14" y="11" width="4" height="1" fill="#000"/>
          <rect x="15" y="12" width="2" height="2" fill="#000"/>
        </svg>
        <span class="logo-text">0x<span class="logo-accent">HACK</span></span>
      </a>

      <button class="hamburger" @click="menuOpen = !menuOpen" :class="{ open: menuOpen }">
        <span></span><span></span><span></span>
      </button>

      <ul class="nav-links" :class="{ open: menuOpen }">
        <li v-for="link in links" :key="link.id">
          <a :href="`#${link.id}`" @click="menuOpen = false">
            <span class="link-prefix">//</span> {{ link.label }}
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const menuOpen = ref(false)

const links = [
  { id: 'about', label: 'About' },
  { id: 'skills', label: 'Skills' },
  { id: 'projects', label: 'Projects' },
  { id: 'guestlist', label: 'Guestlist' },
  { id: 'contact', label: 'Contact' },
]

const handleScroll = () => {
  isScrolled.value = window.scrollY > 60
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0; left: 0;
  width: 100%;
  z-index: 1000;
  padding: 16px 0;
  transition: all 0.3s ease;
  border-bottom: 1px solid transparent;
}

.navbar.scrolled {
  background: rgba(2, 12, 6, 0.95);
  backdrop-filter: blur(12px);
  border-bottom-color: rgba(0, 255, 65, 0.2);
}

.nav-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}

.logo-text {
  font-family: 'Orbitron', sans-serif;
  font-size: 1.2rem;
  font-weight: 900;
  color: var(--neon-green);
  text-shadow: var(--glow-green);
  letter-spacing: 2px;
}

.logo-accent {
  color: var(--neon-cyan);
  text-shadow: var(--glow-cyan);
}

.nav-links {
  display: flex;
  gap: 32px;
  list-style: none;
}

.nav-links a {
  text-decoration: none;
  color: var(--text-dim);
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  letter-spacing: 1px;
  transition: all 0.2s ease;
}

.nav-links a:hover {
  color: var(--neon-green);
  text-shadow: var(--glow-green);
}

.link-prefix {
  color: var(--neon-cyan);
  opacity: 0.6;
}

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.hamburger span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--neon-green);
  transition: all 0.3s ease;
  box-shadow: var(--glow-green);
}

.hamburger.open span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }

@media (max-width: 768px) {
  .hamburger { display: flex; }

  .nav-links {
    display: none;
    position: fixed;
    top: 60px; left: 0;
    width: 100%;
    background: rgba(2, 12, 6, 0.98);
    flex-direction: column;
    gap: 0;
    border-top: 1px solid var(--card-border);
    border-bottom: 1px solid var(--card-border);
  }

  .nav-links.open { display: flex; }

  .nav-links li a {
    display: block;
    padding: 16px 24px;
    border-bottom: 1px solid var(--card-border);
  }
}
</style>