<template>
  <div id="app">
    <CustomCursor />
    <BackgroundEffects />
    
    <nav>
      <a href="#hero" class="nav-logo" @click.prevent="scrollTo('hero')">jansultan.dev</a>
      <ul class="nav-links">
        <li><a href="#about" :class="{ active: activeSection === 'about' }" @click.prevent="scrollTo('about')">About</a></li>
        <li><a href="#skills" :class="{ active: activeSection === 'skills' }" @click.prevent="scrollTo('skills')">Skills</a></li>
        <li><a href="#projects" :class="{ active: activeSection === 'projects' }" @click.prevent="scrollTo('projects')">Projects</a></li>
        <li><a href="#certs" :class="{ active: activeSection === 'certs' }" @click.prevent="scrollTo('certs')">Certs</a></li>
        <li><a href="#guestbook" :class="{ active: activeSection === 'guestbook' }" @click.prevent="scrollTo('guestbook')">Guestbook</a></li>
        <li><a href="#contact" :class="{ active: activeSection === 'contact' }" @click.prevent="scrollTo('contact')">Contact</a></li>
      </ul>
    </nav>

    <div class="page">
      <HeroSection />
      <RuleDivider />
      <AboutSection />
      <RuleDivider />
      <SkillsSection />
      <RuleDivider />
      <ProjectsSection />
      <RuleDivider />
      <CertificatesSection />
      <RuleDivider />
      <GuestbookSection />
      <RuleDivider />
      <ContactSection />
    </div>

    <FooterSection />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import CustomCursor from './components/CustomCursor.vue'
import BackgroundEffects from './components/BackgroundEffects.vue'
import RuleDivider from './components/RuleDivider.vue'
import HeroSection from './sections/HeroSection.vue'
import AboutSection from './sections/AboutSection.vue'
import SkillsSection from './sections/SkillsSection.vue'
import ProjectsSection from './sections/ProjectsSection.vue'
import CertificatesSection from './sections/CertificatesSection.vue'
import GuestbookSection from './sections/GuestbookSection.vue'
import ContactSection from './sections/ContactSection.vue'
import FooterSection from './sections/FooterSection.vue'

const activeSection = ref('hero')

const scrollTo = (id) => {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}

const onScroll = () => {
  const y = window.scrollY + 80
  const sections = ['hero', 'about', 'skills', 'projects', 'certs', 'guestbook', 'contact']
  for (const id of sections) {
    const el = document.getElementById(id)
    if (el && y >= el.offsetTop) activeSection.value = id
  }
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<style>
:root {
  --ink:       #0e0c0f;
  --ink2:      #161319;
  --ink3:      #1e1a21;
  --rule:      #2a2330;
  --rule2:     #382e40;
  --pink:      #f4a7b9;
  --pink-dim:  #3d1f2a;
  --pink-pale: #fce8ee;
  --pink-mid:  #e8799a;
  --rose:      #ff6b8a;
  --cream:     #f5f0eb;
  --white:     #fafaf9;
  --muted:     #7a6d80;
  --muted2:    #4a3f52;
  --mono:      'DM Mono', monospace;
  --serif:     'Playfair Display', serif;
  --sans:      'Instrument Sans', sans-serif;
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{
  background:var(--ink);
  color:var(--muted);
  font-family:var(--sans);
  font-size:14px;
  line-height:1.7;
  overflow-x:hidden;
  cursor:none;
}

#app{position:relative;min-height:100vh;}

::-webkit-scrollbar{width:3px;}
::-webkit-scrollbar-track{background:var(--ink);}
::-webkit-scrollbar-thumb{background:var(--pink-dim);}

nav{
  position:fixed;top:0;left:0;right:0;z-index:300;
  height:58px;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 clamp(1.5rem,6vw,5rem);
  background:rgba(14,12,15,.88);
  backdrop-filter:blur(20px);
  border-bottom:1px solid var(--rule);
}
.nav-logo{
  font-family:var(--serif);
  font-size:15px;font-style:italic;
  color:var(--pink);text-decoration:none;
  letter-spacing:.01em;
}
.nav-links{display:flex;gap:2rem;list-style:none;}
.nav-links a{
  font-family:var(--mono);
  font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted2);text-decoration:none;transition:color .2s;
}
.nav-links a:hover,.nav-links a.active{color:var(--pink);}

.page{position:relative;z-index:1;}
.wrap{
  max-width:1100px;margin:0 auto;
  padding:clamp(5rem,10vw,8rem) clamp(1.5rem,6vw,5rem);
}

.ed-header{
  display:grid;grid-template-columns:auto 1fr;
  align-items:end;gap:1.5rem;
  margin-bottom:3.5rem;
  padding-bottom:1.25rem;
  border-bottom:1px solid var(--rule);
}
.ed-num{
  font-family:var(--mono);font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--pink);
  writing-mode:vertical-rl;transform:rotate(180deg);
  padding-bottom:4px;
}
.ed-label{
  font-family:var(--mono);font-size:9px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--muted2);
  margin-bottom:.5rem;
}
.ed-title{
  font-family:var(--serif);
  font-size:clamp(2.5rem,5.5vw,4.5rem);
  color:var(--white);line-height:.95;
  font-weight:900;
}
.ed-title em{color:var(--pink);font-style:italic;}
.ed-title .ghost{
  -webkit-text-stroke:1px var(--rule2);
  color:transparent;
}

.rv{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease;}
.rv.in{opacity:1;transform:none;}
.rv-d1{transition-delay:.1s;}
.rv-d2{transition-delay:.18s;}
.rv-d3{transition-delay:.26s;}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
@keyframes blink{50%{opacity:0}}
@keyframes pls{0%,100%{box-shadow:0 0 0 0 rgba(244,167,185,.5);opacity:1}50%{box-shadow:0 0 0 5px rgba(244,167,185,0);opacity:.6}}

.btn{
  display:inline-flex;align-items:center;gap:.45rem;
  padding:.6rem 1.5rem;
  font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;
  text-decoration:none;border-radius:2px;
  transition:all .22s;cursor:none;border:none;background:none;
}
.btn-pri{
  background:var(--pink);color:var(--ink);font-weight:500;
  border:1px solid var(--pink);
}
.btn-pri:hover{background:transparent;color:var(--pink);}
.btn-ghost{
  background:transparent;color:var(--muted);
  border:1px solid var(--rule2);
}
.btn-ghost:hover{border-color:var(--pink);color:var(--pink);}

.fl{display:flex;flex-direction:column;gap:5px;}
.fl label{font-family:var(--mono);font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted2);}
.fi,.ft,.cfi,.cft{
  background:var(--ink3);border:1px solid var(--rule);
  border-radius:2px;padding:.7rem .9rem;
  font-family:var(--mono);font-size:12px;
  color:var(--white);outline:none;resize:none;
  transition:border-color .2s;width:100%;
}
.ft{height:110px;}
.cft{height:130px;}
.fi:focus,.ft:focus,.cfi:focus,.cft:focus{border-color:var(--pink);}
.fi::placeholder,.ft::placeholder,.cfi::placeholder,.cft::placeholder{color:var(--muted2);}

@media(max-width:860px){
  .nav-links{display:none;}
  .ed-header{grid-template-columns:1fr;}
  .ed-num{writing-mode:horizontal-tb;transform:none;}
}
</style>