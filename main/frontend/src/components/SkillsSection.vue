<template>
  <section id="skills" class="skills-section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">// skills.exe</span>
        <h2 class="section-title">Skill Tree</h2>
      </div>

      <div class="skills-grid">
        <div class="skill-category card" v-for="cat in categories" :key="cat.name">
          <div class="cat-header">
            <span class="cat-icon">{{ cat.icon }}</span>
            <h3 class="cat-name">{{ cat.name }}</h3>
          </div>
          <div class="skill-list">
            <div class="skill-item" v-for="skill in cat.skills" :key="skill.name">
              <div class="skill-info">
                <span class="skill-name">{{ skill.name }}</span>
                <span class="skill-pct">{{ skill.level }}%</span>
              </div>
              <div class="skill-bar">
                <div class="skill-fill" :style="{ width: skill.level + '%' }" :class="skill.color"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="tech-tags">
        <p class="tags-label"><span class="prompt">$</span> ls /usr/local/tools/</p>
        <div class="tags-cloud">
          <span class="tech-tag" v-for="tool in tools" :key="tool">{{ tool }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const categories = [
  {
    name: 'Offensive Security', icon: '⚔',
    skills: [
      { name: 'Penetration Testing', level: 85, color: 'green' },
      { name: 'Web App Security', level: 90, color: 'green' },
      { name: 'Network Exploitation', level: 78, color: 'green' },
      { name: 'Reverse Engineering', level: 65, color: 'cyan' },
    ]
  },
  {
    name: 'Programming', icon: '⌨',
    skills: [
      { name: 'Python', level: 92, color: 'green' },
      { name: 'Bash/Shell', level: 88, color: 'green' },
      { name: 'JavaScript', level: 75, color: 'cyan' },
      { name: 'C/C++', level: 60, color: 'cyan' },
    ]
  },
  {
    name: 'Defensive Security', icon: '🛡',
    skills: [
      { name: 'Incident Response', level: 80, color: 'cyan' },
      { name: 'Malware Analysis', level: 70, color: 'cyan' },
      { name: 'Forensics', level: 75, color: 'green' },
      { name: 'SIEM / Log Analysis', level: 72, color: 'cyan' },
    ]
  },
  {
    name: 'Networking', icon: '🌐',
    skills: [
      { name: 'TCP/IP Protocols', level: 88, color: 'green' },
      { name: 'Wireshark / Packet Analysis', level: 85, color: 'green' },
      { name: 'Firewall Configuration', level: 76, color: 'cyan' },
      { name: 'VPN & Tunneling', level: 70, color: 'cyan' },
    ]
  },
]

const tools = [
  'Kali Linux', 'Metasploit', 'Burp Suite', 'Nmap', 'Wireshark',
  'Ghidra', 'John the Ripper', 'Hashcat', 'SQLMap', 'Gobuster',
  'Volatility', 'GDB', 'Docker', 'Git', 'Splunk', 'AWS', 'CTFd'
]
</script>

<style scoped>
.skills-section {
  background: linear-gradient(180deg, transparent, rgba(0, 255, 65, 0.02), transparent);
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-bottom: 40px;
}

.skill-category { padding: 28px; }

.cat-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--card-border);
}

.cat-icon { font-size: 1.4rem; }

.cat-name {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--neon-cyan);
  letter-spacing: 2px;
  text-transform: uppercase;
}

.skill-item { margin-bottom: 16px; }

.skill-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 6px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.82rem;
}

.skill-name { color: var(--text-primary); }
.skill-pct { color: var(--neon-green); }

.skill-bar {
  height: 4px;
  background: rgba(255, 255, 255, 0.06);
  overflow: hidden;
}

.skill-fill {
  height: 100%;
  transition: width 1.5s ease;
  position: relative;
}

.skill-fill.green {
  background: linear-gradient(90deg, rgba(0, 255, 65, 0.5), var(--neon-green));
  box-shadow: 0 0 8px rgba(0, 255, 65, 0.6);
}

.skill-fill.cyan {
  background: linear-gradient(90deg, rgba(0, 229, 255, 0.5), var(--neon-cyan));
  box-shadow: 0 0 8px rgba(0, 229, 255, 0.6);
}

.skill-fill::after {
  content: '';
  position: absolute;
  right: 0; top: 0;
  width: 4px; height: 100%;
  background: rgba(255, 255, 255, 0.8);
}

.tech-tags { margin-top: 20px; }

.tags-label {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  color: var(--text-dim);
  margin-bottom: 16px;
}

.prompt { color: var(--neon-green); margin-right: 8px; }

.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tech-tag {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.78rem;
  color: var(--neon-green);
  border: 1px solid rgba(0, 255, 65, 0.25);
  padding: 6px 14px;
  letter-spacing: 1px;
  transition: all 0.2s ease;
  cursor: default;
  clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

.tech-tag:hover {
  background: rgba(0, 255, 65, 0.08);
  border-color: var(--neon-green);
  box-shadow: var(--glow-green);
  color: #fff;
}

@media (max-width: 768px) {
  .skills-grid { grid-template-columns: 1fr; }
}
</style>

