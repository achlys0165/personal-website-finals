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
        :class="[p.size, 'rv', i > 0 ? `rv-d${i % 3}` : '']"
        v-reveal
      />
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import ProjectCard from './ProjectCard.vue'
import { vReveal } from '../directives/reveal'

const projects = ref([
  {
    name: 'CaFTAP [IoT Arduino Project]',
    icon: '📡',
    description: 'An IoT-based automation and monitoring system built using Arduino, designed to collect sensor data and execute real-time control logic. The project integrates hardware components with embedded programming to demonstrate practical applications of IoT in monitoring and automation environments.',
    tags: ['Arduino', 'IoT', 'C++', 'Embedded Systems', 'Sensors'],
    size: 'proj-wide',
    github: 'https://wokwi.com/projects/456768557157923841'
  },
  {
    name: 'Music Ministry Management Web App',
    icon: '🎵',
    description: 'A web-based management system developed to streamline scheduling, coordination, and communication for a music ministry. The platform includes role-based access (admin and musician), structured scheduling modules, and centralized data management to improve organization and workflow efficiency.',
    tags: ['Vue.js', 'Flask', 'PostgreSQL', 'Authentication', 'Full Stack'],
    size: 'proj-wide',
    github: 'https://github.com/achlys0165/Usher-s-Ministry-Attendance-Dashboard'
  },
  {
    name: 'RFID Attendance Monitoring System',
    icon: '🏷️',
    description: 'A contactless attendance system utilizing RFID technology for automated identity verification and record logging. The system improves accuracy and reduces manual errors by integrating RFID hardware with a backend database for real-time attendance tracking and reporting.',
    tags: ['RFID', 'Python', 'Database', 'Hardware Integration', 'Automation'],
    size: 'proj-narrow',
    github: 'https://github.com/achlys0165/Usher-s-Ministry-Attendance-Dashboard'
  },
  {
    name: 'JournalApp (Mental Health Tracker)',
    icon: '📓',
    description: 'A desktop application built with Python that allows users to log journal entries and track emotional well-being over time. The system supports structured input, data storage, and basic analytical insights to encourage self-reflection and mental health awareness.',
    tags: ['Python', 'Tkinter', 'SQLite', 'Data Analysis', 'Desktop App'],
    size: 'proj-narrow',
    github: 'https://github.com/achlys0165/JournalApp'
  }
])

</script>

<style scoped>
.proj-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
}

.proj-wide { grid-column: span 12; }
.proj-narrow { grid-column: span 6; }

@media (max-width: 860px) {
  .proj-wide, .proj-narrow {
    grid-column: span 12;
  }
}
</style>