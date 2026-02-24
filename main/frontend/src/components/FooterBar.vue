<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-logo">
          <span class="logo-text">0x<span class="logo-accent">SHADOW</span></span>
        </div>
        <p class="footer-copy">
          <span class="green">// </span>Built with
          <span class="cyan">Vue.js + Flask + Supabase</span>
          <span class="green"> // </span>
          Designed in the Terminal
        </p>
        <p class="footer-sub">{{ year }} · All bytes reserved · Stay curious, stay secure.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear()
</script>

<style scoped>
.footer {
  border-top: 1px solid rgba(0, 255, 65, 0.1);
  padding: 32px 0;
  text-align: center;
}

.footer-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.logo-text {
  font-family: 'Orbitron', sans-serif;
  font-size: 1rem;
  font-weight: 900;
  color: var(--neon-green);
  letter-spacing: 3px;
}

.logo-accent { color: var(--neon-cyan); }

.footer-copy {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  color: var(--text-dim);
  letter-spacing: 1px;
}

.footer-sub {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.72rem;
  color: rgba(200, 255, 212, 0.25);
  letter-spacing: 2px;
}

.green { color: var(--neon-green); }
.cyan { color: var(--neon-cyan); }
</style>