<template>
  <section id="certs" class="wrap">
    <div class="ed-header rv" v-reveal>
      <div class="ed-num">04</div>
      <div class="ed-title-block">
        <p class="ed-label">Credentials</p>
        <h2 class="ed-title">Certi<em>ficates</em></h2>
      </div>
    </div>
    <div class="certs-grid">
      <CertificateCard 
        v-for="(c, i) in certs" 
        :key="c.name"
        :cert="c"
        :class="['rv', i > 0 ? `rv-d${i % 3}` : '']"
        v-reveal
      />
    </div>
  </section>
</template>

<script setup>
import CertificateCard from './CertificateCard.vue'
import { vReveal } from '../directives/reveal'

const certs = [
  { badge: '🎓', issuer: 'Cisco', name: 'Introduction to Cybersecurity', earned: false},
  { badge: '🛡️', issuer: 'TryHackMe', name: 'Pre-Security Learning Path', earned: true },
  { badge: '🌐', issuer: 'Cisco', name: 'Networking Basics', earned: true },
  { badge: '⚔️', issuer: 'CompTIA', name: 'Security+', earned: false },
  { badge: '📦', issuer: 'AWS ', name: 'Cloud Foundations', earned: true}
]
</script>

<style scoped>
.certs-grid{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(300px,1fr));
  gap:1rem;
}
</style>