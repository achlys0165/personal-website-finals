<template>
  <section id="contact" class="wrap">
    <div class="ed-header rv" v-reveal>
      <div class="ed-num">06</div>
      <div class="ed-title-block">
        <p class="ed-label">Reach Out</p>
        <h2 class="ed-title">Let's <em>Connect</em></h2>
      </div>
    </div>
    <div class="contact-layout rv rv-d1" v-reveal>
      <div>
        <p class="contact-quote">"I'm always looking to learn from people who know more than I do."</p>
        <p class="contact-p">Whether you want to talk security, collaborate on a project, or just exchange notes — I'm open to it.</p>
        <div class="clinks">
          <ContactLink v-for="l in links" :key="l.label" :link="l" />
        </div>
      </div>
      <form class="cf" @submit.prevent="send">
        <div class="cf-row">
          <div class="fl"><label>Name</label><input v-model="form.name" type="text" class="cfi" placeholder="your name" required></div>
          <div class="fl"><label>Email</label><input v-model="form.email" type="email" class="cfi" placeholder="you@example.com" required></div>
        </div>
        <div class="fl"><label>Message</label><textarea v-model="form.message" class="cft" placeholder="What's on your mind?"></textarea></div>
        <button type="submit" class="btn btn-pri" style="align-self:flex-start;cursor:none;" :disabled="sent">
          {{ sent ? 'Sent ✓' : 'Send Message →' }}
        </button>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import ContactLink from './ContactLink.vue'
import { vReveal } from '../directives/reveal'

const links = [
  { icon: '✉', label: 'hello@yourname.dev', href: 'mailto:hello@yourname.dev' },
  { icon: '⌥', label: 'github.com/yourhandle', href: 'https://github.com', ext: true },
  { icon: '◈', label: 'linkedin.com/in/yourname', href: 'https://linkedin.com', ext: true },
  { icon: '⬡', label: 'HackTheBox Profile', href: 'https://hackthebox.com', ext: true }
]

const form = ref({ name: '', email: '', message: '' })
const sent = ref(false)

const send = () => {
  sent.value = true
  setTimeout(() => {
    form.value = { name: '', email: '', message: '' }
    sent.value = false
  }, 3000)
}
</script>

<style scoped>
.contact-layout{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;}
.contact-quote{
  font-family:var(--serif);font-style:italic;
  font-size:clamp(1.2rem,2.5vw,1.6rem);
  color:var(--pink-pale);line-height:1.5;
  margin-bottom:2.5rem;
  border-left:2px solid var(--pink);
  padding-left:1.5rem;
}
.contact-p{font-size:14px;color:var(--muted2);font-weight:300;line-height:1.75;margin-bottom:2rem;}
.clinks{display:flex;flex-direction:column;gap:.5rem;}
.cf{display:flex;flex-direction:column;gap:.9rem;}
.cf-row{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;}
@media(max-width:860px){
  .contact-layout{grid-template-columns:1fr;gap:2.5rem;}
  .cf-row{grid-template-columns:1fr;}
}
</style>