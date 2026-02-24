<template>
  <section id="skills" class="wrap">
    <div class="ed-header rv" v-reveal>
      <div class="ed-num">02</div>
      <div class="ed-title-block">
        <p class="ed-label">Technical</p>
        <h2 class="ed-title"><em>Stack</em> &amp; Skills</h2>
      </div>
    </div>
    <div class="rv rv-d1" v-reveal>
      <table class="skills-table">
        <thead>
          <tr>
            <th style="width:3rem"></th>
            <th>Skill</th>
            <th class="sk-desc">Description</th>
            <th>Level</th>
          </tr>
        </thead>
        <tbody>
          <SkillRow 
            v-for="skill in skills" 
            :key="skill.name"
            :skill="skill"
          />
        </tbody>
      </table>
    </div>
  </section>
</template>

<script setup>
import SkillRow from './SkillRow.vue'
import { vReveal } from '../directives/reveal'

const skills = [
  { icon: '🐍', name: 'Python', desc: 'Scripts, automation, security tools, data processing. Primary language.', level: 'Advanced', cls: 'lvl-adv' },
  { icon: '🐧', name: 'Linux', desc: 'Daily driver. Bash scripting, process management, permissions, file systems.', level: 'Advanced', cls: 'lvl-adv' },
  { icon: '🌐', name: 'Networking', desc: 'TCP/IP, DNS, HTTP(S), subnetting, Wireshark packet analysis.', level: 'Intermediate', cls: 'lvl-int' },
  { icon: '🚩', name: 'CTF / Hacking', desc: 'Web exploitation, reverse engineering, cryptography, OSINT. HackTheBox, TryHackMe.', level: 'Intermediate', cls: 'lvl-int' },
  { icon: '🔐', name: 'Security Concepts', desc: 'OWASP Top 10, vulnerability assessment, threat modeling, responsible disclosure.', level: 'Intermediate', cls: 'lvl-int' },
  { icon: '⚡', name: 'Arduino & IoT', desc: 'Hardware interfacing, embedded systems, sensor projects, IoT security thinking.', level: 'Learning', cls: 'lvl-beg' }
]
</script>

<style scoped>
.skills-table{width:100%;border-collapse:collapse;}
.skills-table thead tr{border-bottom:2px solid var(--rule2);}
.skills-table th{
  font-family:var(--mono);font-size:9px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--muted2);padding:.6rem 1rem .6rem 0;text-align:left;
}
.skills-table th:last-child{text-align:right;}
@media(max-width:860px){
  .skills-table .sk-desc{display:none;}
}
</style>