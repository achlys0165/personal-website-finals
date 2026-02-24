<template>
  <section id="about">
    <div class="container">
      <div class="section-header">
        <span class="section-label">// identity.txt</span>
        <h2 class="section-title">About Me</h2>
      </div>

      <div class="about-grid">
        <div class="about-text">
          <div class="card">
            <p class="about-intro">
              <span class="highlight">&gt; </span>
              I'm a cybersecurity student and ethical hacker passionate about breaking things to understand how to protect them.
              Currently pursuing my degree in Information Security while competing in CTF competitions worldwide.
            </p>
            <p class="about-body" style="margin-top: 16px">
              With hands-on experience in penetration testing, vulnerability research, and secure software development,
              I bridge the gap between offense and defense. I believe that understanding an attacker's mindset is
              the key to building robust defenses.
            </p>
            <p class="about-body" style="margin-top: 16px">
              When I'm not hunting bugs, you'll find me contributing to open-source security tools,
              writing CTF writeups, or mentoring newcomers in the cybersecurity community.
            </p>
          </div>

          <div class="stats-row">
            <div class="stat-card" v-for="s in stats" :key="s.label">
              <div class="stat-value">{{ s.value }}</div>
              <div class="stat-label">{{ s.label }}</div>
            </div>
          </div>
        </div>

        <div class="about-details">
          <div class="detail-block">
            <p class="detail-header"><span class="prompt">$</span> cat info.json</p>
            <div class="json-display">
              <p><span class="json-key">"name"</span>: <span class="json-str">"Alex Chen"</span>,</p>
              <p><span class="json-key">"alias"</span>: <span class="json-str">"0xShadow"</span>,</p>
              <p><span class="json-key">"location"</span>: <span class="json-str">"United States"</span>,</p>
              <p><span class="json-key">"education"</span>: <span class="json-str">"B.S. Information Security"</span>,</p>
              <p><span class="json-key">"certs"</span>: [</p>
              <p class="json-indent"><span class="json-str">"CompTIA Security+"</span>,</p>
              <p class="json-indent"><span class="json-str">"eJPT"</span>,</p>
              <p class="json-indent"><span class="json-str">"CEH (in progress)"</span></p>
              <p>],</p>
              <p><span class="json-key">"available"</span>: <span class="json-bool">true</span></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const stats = [
  { value: '50+', label: 'CTFs Completed' },
  { value: '15+', label: 'Bugs Found' },
  { value: '3+', label: 'Years Hacking' },
  { value: '∞', label: 'Curiosity' },
]
</script>

<style scoped>
.about-grid {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 40px;
  align-items: start;
}

.about-intro {
  font-family: 'Share Tech Mono', monospace;
  font-size: 1rem;
  color: var(--neon-green);
  line-height: 1.8;
}

.about-body {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.9rem;
  color: var(--text-dim);
  line-height: 1.8;
}

.highlight { color: var(--neon-cyan); }

.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 24px;
}

.stat-card {
  background: rgba(0, 255, 65, 0.04);
  border: 1px solid var(--card-border);
  padding: 20px 12px;
  text-align: center;
  clip-path: polygon(12px 0%, 100% 0%, calc(100% - 12px) 100%, 0% 100%);
  transition: all 0.3s ease;
}

.stat-card:hover {
  background: rgba(0, 255, 65, 0.08);
  border-color: var(--neon-green);
}

.stat-value {
  font-family: 'Orbitron', sans-serif;
  font-size: 1.8rem;
  font-weight: 900;
  color: var(--neon-green);
  text-shadow: var(--glow-green);
}

.stat-label {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.7rem;
  color: var(--text-dim);
  letter-spacing: 2px;
  margin-top: 4px;
}

.detail-block {
  background: rgba(0, 0, 0, 0.6);
  border: 1px solid rgba(0, 255, 65, 0.2);
  border-radius: 4px;
  overflow: hidden;
}

.detail-header {
  background: rgba(0, 255, 65, 0.06);
  border-bottom: 1px solid rgba(0, 255, 65, 0.15);
  padding: 10px 16px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  color: var(--text-dim);
}

.prompt { color: var(--neon-green); margin-right: 6px; }

.json-display {
  padding: 20px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  line-height: 1.8;
  color: var(--text-dim);
}

.json-key { color: var(--neon-cyan); }
.json-str { color: #ce9178; }
.json-bool { color: #569cd6; }
.json-indent { padding-left: 20px; }

@media (max-width: 960px) {
  .about-grid { grid-template-columns: 1fr; }
  .stats-row { grid-template-columns: repeat(2, 1fr); }
}
</style>