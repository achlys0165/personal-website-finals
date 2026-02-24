<template>
  <section id="projects">
    <div class="container">
      <div class="section-header">
        <span class="section-label">// projects.db</span>
        <h2 class="section-title">Projects</h2>
      </div>

      <div class="projects-grid">
        <div class="project-card card" v-for="p in projects" :key="p.name">
          <div class="project-header">
            <div class="project-type" :class="p.type">{{ p.typeLabel }}</div>
            <div class="project-status" :class="p.status">
              <span class="status-dot"></span>{{ p.status }}
            </div>
          </div>
          <h3 class="project-name">{{ p.name }}</h3>
          <p class="project-desc">{{ p.desc }}</p>
          <div class="project-tags">
            <span class="p-tag" v-for="tag in p.tags" :key="tag">{{ tag }}</span>
          </div>
          <div class="project-links">
            <a :href="p.github" class="p-link" target="_blank" rel="noopener">
              <span class="link-icon">◈</span> GitHub
            </a>
            <a v-if="p.demo" :href="p.demo" class="p-link p-link-demo" target="_blank" rel="noopener">
              <span class="link-icon">▶</span> Live Demo
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const projects = [
  {
    name: 'VulnScanner-X', typeLabel: 'TOOL', type: 'tool', status: 'active',
    desc: 'Automated web vulnerability scanner with custom payload generation for OWASP Top 10 detection. Features async scanning, intelligent crawling, and detailed PDF reports.',
    tags: ['Python', 'AsyncIO', 'SQLi', 'XSS', 'OWASP'], github: '#', demo: '#',
  },
  {
    name: 'PacketGhost', typeLabel: 'TOOL', type: 'tool', status: 'active',
    desc: 'Network packet analyzer and anomaly detection system using machine learning to identify suspicious traffic patterns and potential intrusions in real-time.',
    tags: ['Python', 'Scapy', 'ML', 'Wireshark', 'IDS'], github: '#', demo: null,
  },
  {
    name: 'CTF Writeups', typeLabel: 'RESEARCH', type: 'research', status: 'ongoing',
    desc: 'Detailed writeups for 50+ CTF challenges across HackTheBox, TryHackMe, and PicoCTF. Covering pwn, web, crypto, forensics, and reversing.',
    tags: ['CTF', 'Writeups', 'HackTheBox', 'TryHackMe'], github: '#', demo: '#',
  },
  {
    name: 'CipherForge', typeLabel: 'TOOL', type: 'tool', status: 'active',
    desc: 'Custom cryptography playground for studying and breaking classical and modern cipher implementations. Includes frequency analysis and known-plaintext attacks.',
    tags: ['Python', 'Cryptography', 'AES', 'RSA', 'Education'], github: '#', demo: null,
  },
  {
    name: 'SecNotes API', typeLabel: 'APP', type: 'app', status: 'active',
    desc: 'End-to-end encrypted personal notes API with zero-knowledge architecture. Uses AES-256-GCM encryption with PBKDF2 key derivation.',
    tags: ['Flask', 'AES-256', 'REST API', 'E2E Encryption'], github: '#', demo: '#',
  },
  {
    name: 'PhishDetect ML', typeLabel: 'ML', type: 'research', status: 'ongoing',
    desc: 'Machine learning model trained on 100k+ URLs to classify phishing sites with 97% accuracy. Uses URL feature extraction and ensemble classifiers.',
    tags: ['Python', 'Scikit-learn', 'NLP', 'Phishing', 'ML'], github: '#', demo: null,
  },
]
</script>

<style scoped>
.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.project-card {
  display: flex;
  flex-direction: column;
  padding: 24px;
  transition: all 0.3s ease;
}

.project-card:hover {
  border-color: rgba(0, 255, 65, 0.5);
  box-shadow: 0 8px 32px rgba(0, 255, 65, 0.08);
  transform: translateY(-4px);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.project-type {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 3px;
  padding: 3px 10px;
  clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
}

.project-type.tool {
  background: rgba(0, 255, 65, 0.15);
  color: var(--neon-green);
  border: 1px solid rgba(0, 255, 65, 0.3);
}

.project-type.research {
  background: rgba(0, 229, 255, 0.1);
  color: var(--neon-cyan);
  border: 1px solid rgba(0, 229, 255, 0.3);
}

.project-type.app {
  background: rgba(0, 128, 255, 0.1);
  color: var(--neon-blue);
  border: 1px solid rgba(0, 128, 255, 0.3);
}

.project-status {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 1px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.project-status.active { color: var(--neon-green); }
.project-status.ongoing { color: var(--neon-cyan); }

.status-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: currentColor;
  animation: pulse-glow 2s infinite;
}

.project-name {
  font-family: 'Orbitron', sans-serif;
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 10px;
  letter-spacing: 1px;
}

.project-desc {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.82rem;
  color: var(--text-dim);
  line-height: 1.7;
  flex: 1;
  margin-bottom: 16px;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 20px;
}

.p-tag {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.7rem;
  color: rgba(0, 229, 255, 0.8);
  background: rgba(0, 229, 255, 0.06);
  border: 1px solid rgba(0, 229, 255, 0.2);
  padding: 2px 8px;
  letter-spacing: 1px;
}

.project-links { display: flex; gap: 16px; margin-top: auto; }

.p-link {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  color: var(--text-dim);
  text-decoration: none;
  letter-spacing: 1px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}

.p-link:hover { color: var(--neon-green); text-shadow: var(--glow-green); }
.p-link-demo:hover { color: var(--neon-cyan); text-shadow: var(--glow-cyan); }

@media (max-width: 960px) {
  .projects-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 600px) {
  .projects-grid { grid-template-columns: 1fr; }
}
</style>