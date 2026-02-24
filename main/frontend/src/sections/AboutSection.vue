<template>
  <section id="about" class="wrap">
    <div class="ed-header rv" v-reveal>
      <div class="ed-num">01</div>
      <div class="ed-title-block">
        <p class="ed-label">About</p>
        <h2 class="ed-title">Who <em>I Am</em></h2>
      </div>
    </div>
    <div class="about-layout rv rv-d1" v-reveal>
      <div>
        <p class="about-intro">"The goal isn't to be the smartest person in the room — it's to be the most curious one."</p>
        <div class="about-body">
          <p>I'm a student with a deep interest in <strong>cybersecurity</strong> and software development. My path started with a single question — "how does this actually work?" — and it hasn't stopped since.</p>
          <p>Most of my time goes into <strong>Python programming</strong>, Linux systems, and understanding how networks communicate. CTF competitions are where I test what I know — they demand creativity, patience, and a high tolerance for being wrong before being right.</p>
          <p>Outside of tech, I study <strong>philosophy</strong> and think seriously about the ethics behind security work. Knowing why something matters is just as important as knowing how to do it.</p>
          <p>The goal is a career in <strong>penetration testing</strong> — methodical, disciplined, always improving. Every debugged script and solved challenge is a step forward.</p>
        </div>
      </div>
      <aside class="about-sidebar">
        <PhotoUpload />
        <InterestsBlock />
      </aside>
    </div>
  </section>
</template>

<script setup>
import PhotoUpload from './PhotoUpload.vue'
import InterestsBlock from './InterestsBlock.vue'
import { vReveal } from '../directives/reveal'
</script>

<style scoped>
.about-layout{
  display:grid;grid-template-columns:5fr 3fr;gap:5rem;align-items:start;
}
.about-intro{
  font-family:var(--serif);font-size:clamp(1.15rem,2vw,1.45rem);
  font-style:italic;color:var(--pink-pale);
  line-height:1.55;margin-bottom:2rem;
  border-left:2px solid var(--pink);
  padding-left:1.5rem;
}
.about-body{
  font-size:14px;color:var(--muted);font-weight:300;
  line-height:1.8;
}
.about-body p{margin-bottom:1.1rem;}
.about-body strong{color:var(--pink);font-weight:500;}
@media(max-width:860px){
  .about-layout{grid-template-columns:1fr;gap:2.5rem;}
}
</style>