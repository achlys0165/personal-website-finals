<template>
  <section id="guestbook" class="wrap">
    <div class="ed-header rv" v-reveal>
      <div class="ed-num">05</div>
      <div class="ed-title-block">
        <p class="ed-label">Community</p>
        <h2 class="ed-title">Guest<em>book</em></h2>
      </div>
    </div>
    <div class="gb-layout">
      <div class="rv" v-reveal>
        <p class="gb-intro">"Leave a trace. Let me know you were here."</p>
        <p class="gb-sub">Visitor, collaborator, or just passing through — say something. I read every entry.</p>
        <form class="gb-form" @submit.prevent="submit">
          <div class="gb-row">
            <div class="fl">
              <label>Name *</label>
              <input v-model="form.name" class="fi" type="text" placeholder="your handle" maxlength="40" required>
            </div>
            <div class="fl">
              <label>From (optional)</label>
              <input v-model="form.from" class="fi" type="text" placeholder="city / internet" maxlength="40">
            </div>
          </div>
          <div class="fl">
            <label>Message *</label>
            <textarea v-model="form.message" class="ft" placeholder="What's on your mind?" maxlength="280" required></textarea>
            <span class="gb-counter">{{ form.message.length }} / 280</span>
          </div>
          <button type="submit" class="btn btn-pri" style="align-self:flex-start;cursor:none;" :disabled="posted">
            {{ posted ? 'Posted ✓' : 'Post Entry →' }}
          </button>
        </form>
      </div>
      <div class="rv rv-d2" v-reveal>
        <div class="gb-entries-title">Entries</div>
        <div class="gb-count-label">{{ entries.length }} entr{{ entries.length === 1 ? 'y' : 'ies' }}</div>
        <div class="gb-list" ref="list">
          <div v-if="entries.length === 0" class="gb-empty">No entries yet — be the first to sign.</div>
          <GuestbookEntry v-for="e in reversed" :key="e.id" :entry="e" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import GuestbookEntry from './GuestbookEntry.vue'
import { vReveal } from '../directives/reveal'

const SKEY = 'gb:v3:entries'
const entries = ref([])
const form = ref({ name: '', from: '', message: '' })
const posted = ref(false)
const list = ref(null)

const reversed = computed(() => [...entries.value].reverse())

const load = () => {
  try {
    const d = localStorage.getItem(SKEY)
    if (d) entries.value = JSON.parse(d)
  } catch(e) { entries.value = [] }
}

const save = () => {
  try { localStorage.setItem(SKEY, JSON.stringify(entries.value)) } catch(e) {}
}

const submit = () => {
  if (!form.value.name.trim() || !form.value.message.trim()) return
  entries.value.push({
    id: Date.now(),
    name: form.value.name.trim(),
    from: form.value.from.trim(),
    message: form.value.message.trim(),
    ts: new Date().toISOString()
  })
  save()
  form.value = { name: '', from: '', message: '' }
  posted.value = true
  if (list.value) list.value.scrollTo({ top: 0, behavior: 'smooth' })
  setTimeout(() => posted.value = false, 2000)
}

onMounted(load)
</script>

<style scoped>
.gb-layout{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start;}
.gb-intro{
  font-family:var(--serif);font-style:italic;
  font-size:1.1rem;color:var(--pink-pale);
  line-height:1.6;margin-bottom:1.5rem;
}
.gb-sub{font-size:13px;color:var(--muted2);margin-bottom:2rem;font-weight:300;}
.gb-form{display:flex;flex-direction:column;gap:.9rem;}
.gb-row{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;}
.gb-counter{font-family:var(--mono);font-size:10px;color:var(--muted2);text-align:right;margin-top:3px;}
.gb-entries-title{
  font-family:var(--serif);font-size:1.5rem;font-weight:700;
  color:var(--white);margin-bottom:.5rem;
}
.gb-count-label{font-family:var(--mono);font-size:10px;color:var(--muted2);letter-spacing:.1em;margin-bottom:1.25rem;}
.gb-list{display:flex;flex-direction:column;gap:0;max-height:520px;overflow-y:auto;padding-right:4px;}
.gb-empty{
  padding:3rem;text-align:center;
  font-family:var(--serif);font-style:italic;
  font-size:1rem;color:var(--muted2);
  border:1px dashed var(--rule);border-radius:3px;
}
@media(max-width:860px){
  .gb-layout{grid-template-columns:1fr;gap:2.5rem;}
  .gb-row{grid-template-columns:1fr;}
}
</style>