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
      <!-- Form -->
      <div class="rv" v-reveal>
        <p class="gb-intro">"Leave a trace. Let me know you were here."</p>
        <p class="gb-sub">Visitor, collaborator, or just passing through — say something.</p>
        
        <form class="gb-form" @submit.prevent="submitEntry">
          <div class="fl">
            <label>Name *</label>
            <input 
              v-model="form.name" 
              class="fi" 
              type="text" 
              placeholder="your handle" 
              maxlength="40" 
              required
              :disabled="isSubmitting"
            >
          </div>
          
          <div class="fl">
            <label>Message *</label>
            <textarea 
              v-model="form.message" 
              class="ft" 
              placeholder="What's on your mind?" 
              maxlength="280" 
              required
              :disabled="isSubmitting"
            ></textarea>
            <span class="gb-counter">{{ form.message.length }} / 280</span>
          </div>
          
          <div class="form-actions">
            <button 
              type="submit" 
              class="btn btn-pri" 
              :disabled="isSubmitting"
            >
              <span v-if="isSubmitting" class="spinner"></span>
              {{ isSubmitting ? 'Posting...' : (posted ? 'Posted ✓' : 'Post Entry →') }}
            </button>
            <span v-if="error" class="error-msg">{{ error }}</span>
            <span v-if="posted" class="success-msg">Posted!</span>
          </div>
        </form>
      </div>

      <!-- Entries -->
      <div class="rv rv-d2" v-reveal>
        <div class="gb-entries-header">
          <div class="gb-entries-title">Entries</div>
          <button @click="refresh" class="refresh-btn" :disabled="isLoading">
            <span :class="{ spin: isLoading }">↻</span>
          </button>
        </div>
        
        <div class="gb-count-label">
          {{ entries.length }} entr{{ entries.length === 1 ? 'y' : 'ies' }}
        </div>
        
        <div class="gb-list" ref="list">
          <div v-if="isLoading && entries.length === 0" class="skeleton-list">
            <div v-for="n in 3" :key="n" class="skeleton-entry"></div>
          </div>
          
          <div v-if="entries.length === 0 && !isLoading" class="gb-empty">
            No entries yet — be the first.
          </div>
          
          <GuestbookEntry 
            v-for="entry in entries" 
            :key="entry.id" 
            :entry="entry" 
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import GuestbookEntry from './GuestbookEntry.vue'
import { api } from '../services/api.js'
import { vReveal } from '../directives/reveal'

const entries = ref([])
const form = ref({ name: '', message: '' })
const isSubmitting = ref(false)
const isLoading = ref(false)
const posted = ref(false)
const error = ref('')
const list = ref(null)

const load = async () => {
  isLoading.value = true
  error.value = ''
  try {
    const res = await api.fetchGuestbook()
    entries.value = res.data
  } catch (e) {
    console.error(e)
    error.value = 'Failed to load entries'
  } finally {
    isLoading.value = false
  }
}

const refresh = () => {
  load()
  list.value?.scrollTo({ top: 0, behavior: 'smooth' })
}

const submitEntry = async () => {
  if (!form.value.name.trim() || !form.value.message.trim()) return
  
  isSubmitting.value = true
  error.value = ''
  
  try {
    const res = await api.postGuestbook({
      name: form.value.name,
      message: form.value.message
    })
    
    entries.value.unshift(res.data)
    form.value = { name: '', message: '' }
    posted.value = true
    list.value?.scrollTo({ top: 0, behavior: 'smooth' })
    setTimeout(() => posted.value = false, 3000)
  } catch (e) {
    error.value = e.message || 'Failed to post'
  } finally {
    isSubmitting.value = false
  }
}

onMounted(load)
</script>

<style scoped>
.gb-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}

.gb-intro {
  font-family: var(--serif);
  font-style: italic;
  font-size: 1.1rem;
  color: var(--pink-pale);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.gb-sub {
  font-size: 13px;
  color: var(--muted2);
  margin-bottom: 2rem;
  font-weight: 300;
}

.gb-form {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
}

.gb-counter {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--muted2);
  text-align: right;
  margin-top: 3px;
}

.form-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.spinner {
  display: inline-block;
  width: 12px;
  height: 12px;
  border: 2px solid var(--ink);
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-right: 6px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-msg { color: #ff6b6b; font-size: 12px; font-family: var(--mono); }
.success-msg { color: var(--pink); font-size: 12px; font-family: var(--mono); }

.gb-entries-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.gb-entries-title {
  font-family: var(--serif);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--white);
}

.refresh-btn {
  background: transparent;
  border: 1px solid var(--rule);
  color: var(--muted2);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.refresh-btn:hover:not(:disabled) {
  border-color: var(--pink);
  color: var(--pink);
}

.refresh-btn .spin {
  display: inline-block;
  animation: spin 1s linear infinite;
}

.gb-count-label {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--muted2);
  letter-spacing: 0.1em;
  margin-bottom: 1.25rem;
}

.gb-list {
  display: flex;
  flex-direction: column;
  gap: 0;
  max-height: 520px;
  overflow-y: auto;
  padding-right: 4px;
}

.gb-empty {
  padding: 3rem;
  text-align: center;
  font-family: var(--serif);
  font-style: italic;
  font-size: 1rem;
  color: var(--muted2);
  border: 1px dashed var(--rule);
  border-radius: 3px;
}

.skeleton-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.skeleton-entry {
  height: 80px;
  background: var(--ink2);
  border-radius: 4px;
  animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.4; }
  50% { opacity: 0.8; }
}

@media (max-width: 860px) {
  .gb-layout {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .gb-list { max-height: 400px; }
}

@media (hover: none) and (pointer: coarse) {
  .gb-list { -webkit-overflow-scrolling: touch; }
}
</style>