<template>
  <section id="contact">
    <div class="container">
      <div class="section-header">
        <span class="section-label">// contact.sh</span>
        <h2 class="section-title">Contact</h2>
      </div>

      <div class="contact-grid">
        <div class="contact-info">
          <p class="contact-intro">
            <span class="prompt">$</span> Looking for a cybersecurity collaborator, CTF teammate, or just want to connect?
            My inbox is always open to opportunities and interesting conversations.
          </p>
          <div class="contact-links">
            <a v-for="link in links" :key="link.label" :href="link.url" class="contact-link" target="_blank" rel="noopener">
              <span class="link-prefix">{{ link.prefix }}</span>
              <div>
                <div class="link-label">{{ link.label }}</div>
                <div class="link-value">{{ link.value }}</div>
              </div>
            </a>
          </div>
        </div>

        <div class="contact-terminal">
          <div class="terminal-line" v-for="(line, i) in termLines" :key="i" :style="{ animationDelay: `${i * 0.15}s` }">
            <span v-if="line.prompt" class="t-prompt">{{ line.prompt }}</span>
            <span :class="line.cls">{{ line.text }}</span>
          </div>
          <div class="t-cursor">█</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const links = [
  { prefix: '✉', label: 'Email', value: 'alex@0xshadow.dev', url: 'mailto:alex@0xshadow.dev' },
  { prefix: '⬡', label: 'GitHub', value: 'github.com/0xshadow', url: '#' },
  { prefix: '◈', label: 'LinkedIn', value: 'linkedin.com/in/alex-chen', url: '#' },
  { prefix: '⬢', label: 'HackTheBox', value: 'app.hackthebox.com/0xshadow', url: '#' },
  { prefix: '▲', label: 'Discord', value: '0xshadow#7741', url: '#' },
]

const termLines = [
  { prompt: '$ ', text: 'ping 0xshadow.dev', cls: 'dim' },
  { text: 'PING 0xshadow.dev: 56 bytes of data', cls: 'dim' },
  { text: '64 bytes from 0xshadow.dev: icmp_seq=1 ttl=64 time=1.2ms', cls: 'ok' },
  { text: '64 bytes from 0xshadow.dev: icmp_seq=2 ttl=64 time=0.9ms', cls: 'ok' },
  { prompt: '$ ', text: 'echo $AVAILABILITY', cls: 'dim' },
  { text: 'OPEN_TO_OPPORTUNITIES=true', cls: 'highlight' },
  { prompt: '$ ', text: 'cat response_time.txt', cls: 'dim' },
  { text: 'Usually responds within 24 hours.', cls: 'ok' },
]
</script>

<style scoped>
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: start;
}

.contact-intro {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.9rem;
  color: var(--text-dim);
  line-height: 1.8;
  margin-bottom: 32px;
}

.prompt { color: var(--neon-green); margin-right: 8px; }

.contact-links {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 20px;
  background: rgba(0, 255, 65, 0.02);
  border: 1px solid var(--card-border);
  text-decoration: none;
  transition: all 0.2s ease;
  border-left: 3px solid transparent;
}

.contact-link:hover {
  border-left-color: var(--neon-green);
  background: rgba(0, 255, 65, 0.06);
  box-shadow: 0 0 20px rgba(0, 255, 65, 0.06);
  transform: translateX(4px);
}

.link-prefix { font-size: 1.4rem; width: 28px; text-align: center; color: var(--neon-cyan); }

.link-label {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--text-dim);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 3px;
}

.link-value {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  color: var(--neon-green);
}

.contact-terminal {
  background: rgba(0, 0, 0, 0.7);
  border: 1px solid rgba(0, 255, 65, 0.2);
  padding: 24px 28px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  line-height: 2;
}

.terminal-line { animation: fadeInUp 0.4s ease both; }

.t-prompt { color: var(--neon-green); }
.ok { color: var(--neon-green); }
.highlight { color: var(--neon-cyan); }
.dim { color: var(--text-dim); }

.t-cursor {
  color: var(--neon-green);
  animation: blink 1s step-end infinite;
  margin-top: 4px;
}

@media (max-width: 768px) {
  .contact-grid { grid-template-columns: 1fr; }
  .contact-terminal { display: none; }
}
</style>