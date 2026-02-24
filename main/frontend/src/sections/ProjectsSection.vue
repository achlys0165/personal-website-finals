<template>
  <section id="projects" class="wrap">
    <div class="ed-header rv" v-reveal>
      <div class="ed-num">03</div>
      <div class="ed-title-block">
        <p class="ed-label">Work</p>
        <h2 class="ed-title">Things I've <em>Built</em></h2>
      </div>
    </div>
    <div class="proj-grid">
      <ProjectCard 
        v-for="(p, i) in projects" 
        :key="p.name"
        :project="p"
        :class="[p.size, 'rv', i > 0 ? `rv-d${i}` : '']"
        v-reveal
      />
    </div>
  </section>
</template>

<script setup>
import ProjectCard from './ProjectCard.vue'
import { vReveal } from '../directives/reveal'

const projects = [
  { name: 'Network Port Scanner', icon: '🔍', desc: 'Lightweight Python tool for scanning open ports on a target host. Built from scratch to understand TCP handshakes, socket programming, and how recon tools actually work under the hood.', tags: ['Python', 'Sockets', 'Networking', 'CLI'], size: 'proj-wide' },
  { name: 'School Management System', icon: '🏫', desc: 'Full CRUD application for student records, grades, and scheduling. Database integration with a clean CLI interface.', tags: ['Python', 'SQLite'], size: 'proj-narrow' },
  { name: 'Password Strength Analyzer', icon: '🔑', desc: 'Analyzes passwords against patterns, dictionary entries, and entropy. Built to understand what makes credentials weak.', tags: ['Python', 'Security'], size: 'proj-third' },
  { name: 'OSINT Recon Helper', icon: '🕵️', desc: 'CLI tool for passive recon — pulls WHOIS, DNS records, and subdomain enumeration for a given target domain.', tags: ['Python', 'OSINT'], size: 'proj-third' },
  { name: 'IoT Environment Monitor', icon: '🌡️', desc: 'Arduino sensor system logging temperature, humidity, and motion. Thinking about the security risks of connected devices.', tags: ['Arduino', 'C++'], size: 'proj-third' }
]
</script>

<style scoped>
.proj-grid{
  display:grid;
  grid-template-columns:repeat(12,1fr);
  gap:1rem;
}
@media(max-width:860px){
  .proj-wide,.proj-narrow,.proj-third{grid-column:span 12 !important;}
}
</style>