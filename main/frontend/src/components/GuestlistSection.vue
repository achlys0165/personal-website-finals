<template>
  <section id="guestlist" class="guestlist-section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">// visitor_log.db</span>
        <h2 class="section-title">Guestlist</h2>
        <p class="section-sub">Leave a trace. You've been here.</p>
      </div>

      <div class="guestlist-layout">
        <div class="form-panel">
          <div class="panel-header">
            <span class="panel-icon">⌨</span>
            <span>Log Your Visit</span>
          </div>
          <form @submit.prevent="submitEntry" class="guest-form">
            <div class="form-group">
              <label class="form-label">
                <span class="label-prompt">&gt; </span>Handle / Name
              </label>
              <input
                v-model="form.name"
                type="text"
                class="form-input"
                placeholder="anonymous_user_7741"
                maxlength="60"
                required
              />
            </div>
            <div class="form-group">
              <label class="form-label">
                <span class="label-prompt">&gt; </span>Message
              </label>
              <textarea
                v-model="form.message"
                class="form-input form-textarea"
                placeholder="Your message to the world..."
                maxlength="300"
                rows="4"
                required
              ></textarea>
              <span class="char-count">{{ form.message.length }}/300</span>
            </div>
            <div class="form-status" v-if="status.message" :class="status.type">
              <span class="status-indicator">{{ status.type === 'success' ? '[+]' : '[!]' }}</span>
              {{ status.message }}
            </div>
            <button type="submit" class="btn submit-btn" :disabled="loading">
              <span v-if="!loading">✦ Submit Entry</span>
              <span v-else class="loading-text">WRITING TO DB<span class="dots">...</span></span>
            </button>
          </form>
        </div>

        <div class="entries-panel">
          <div class="panel-header">
            <span class="panel-icon">📋</span>
            <span>Visitor Log</span>
            <span class="entry-count">{{ entries.length }} entries</span>
          </div>
          <div class="entries-list" ref="logEl">
            <div v-if="fetchLoading" class="log-loading">
              <span class="loading-text">FETCHING RECORDS<span class="dots">...</span></span>
            </div>
            <div v-else-if="fetchError" class="log-error">
              <span class="err-icon">[!]</span> {{ fetchError }}
              <button @click="fetchEntries" class="retry-btn">RETRY</button>
            </div>
            <div v-else-if="entries.length === 0" class="log-empty">
              <p>// No entries yet. Be the first to sign in.</p>
            </div>
            <div v-else class="log-entry" v-for="(entry, idx) in entries" :key="entry.id">
              <div class="entry-header">
                <span class="entry-index">#{{ String(idx + 1).padStart(3, '0') }}</span>
                <span class="entry-name">{{ entry.name }}</span>
                <span class="entry-time">{{ formatDate(entry.created_at) }}</span>
              </div>
              <p class="entry-message">&gt; {{ entry.message }}</p>
            </div>
          </div>
          <button @click="fetchEntries" class="refresh-btn">↻ Refresh Log</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { guestlistAPI } from '../api.js'

const entries = ref([])
const fetchLoading = ref(false)
const fetchError = ref(null)
const loading = ref(false)
const logEl = ref(null)
const form = ref({ name: '', message: '' })
const status = ref({ type: '', message: '' })

const formatDate = (iso) => {
  if (!iso) return 'unknown'
  return new Date(iso).toLocaleDateString('en-US', {
    month: 'short', day: 'numeric', year: 'numeric',
    hour: '2-digit', minute: '2-digit'
  })
}

const fetchEntries = async () => {
  fetchLoading.value = true
  fetchError.value = null
  try {
    const res = await guestlistAPI.getEntries()
    entries.value = res.data.entries || []
  } catch (err) {
    fetchError.value = err.response?.data?.error || 'Failed to connect to server.'
  } finally {
    fetchLoading.value = false
  }
}

const submitEntry = async () => {
  if (!form.value.name.trim() || !form.value.message.trim()) return
  loading.value = true
  status.value = { type: '', message: '' }
  try {
    await guestlistAPI.postEntry({
      name: form.value.name.trim(),
      message: form.value.message.trim()
    })
    status.value = { type: 'success', message: 'Entry logged successfully!' }
    form.value = { name: '', message: '' }
    await fetchEntries()
    if (logEl.value) logEl.value.scrollTop = 0
  } catch (err) {
    status.value = {
      type: 'error',
      message: err.response?.data?.error || 'Submission failed. Check backend connection.'
    }
  } finally {
    loading.value = false
    setTimeout(() => { status.value = { type: '', message: '' } }, 5000)
  }
}

onMounted(fetchEntries)
</script>

<style scoped>
.guestlist-section {
  background: linear-gradient(180deg, transparent, rgba(0, 229, 255, 0.02), transparent);
}

.section-sub {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  color: var(--text-dim);
  margin-top: 8px;
  letter-spacing: 2px;
}

.guestlist-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  align-items: start;
}

.panel-header {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--neon-cyan);
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  background: rgba(0, 229, 255, 0.04);
  border-bottom: 1px solid rgba(0, 229, 255, 0.15);
  display: flex;
  align-items: center;
  gap: 10px;
}

.panel-icon { font-size: 1rem; }

.entry-count {
  margin-left: auto;
  font-size: 0.7rem;
  color: var(--text-dim);
  font-family: 'Share Tech Mono', monospace;
}

.form-panel {
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(0, 229, 255, 0.2);
  overflow: hidden;
}

.guest-form {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  position: relative;
}

.form-label {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  color: var(--text-dim);
  letter-spacing: 1px;
}

.label-prompt { color: var(--neon-green); }

.form-input {
  background: rgba(0, 255, 65, 0.03);
  border: 1px solid rgba(0, 255, 65, 0.2);
  color: var(--text-primary);
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.9rem;
  padding: 12px 16px;
  outline: none;
  transition: all 0.2s ease;
  resize: none;
  width: 100%;
}

.form-input::placeholder { color: rgba(200, 255, 212, 0.25); }

.form-input:focus {
  border-color: var(--neon-green);
  box-shadow: 0 0 16px rgba(0, 255, 65, 0.1);
  background: rgba(0, 255, 65, 0.05);
}

.form-textarea { min-height: 100px; }

.char-count {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.7rem;
  color: var(--text-dim);
  text-align: right;
}

.form-status {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  padding: 10px 14px;
  border-left: 3px solid;
}

.form-status.success {
  color: var(--neon-green);
  border-left-color: var(--neon-green);
  background: rgba(0, 255, 65, 0.05);
}

.form-status.error {
  color: #ff6b6b;
  border-left-color: #ff4d4d;
  background: rgba(255, 77, 77, 0.05);
}

.submit-btn { width: 100%; padding: 14px; font-size: 0.9rem; }
.submit-btn:disabled { opacity: 0.6; cursor: not-allowed; }

.entries-panel {
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(0, 229, 255, 0.2);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.entries-list {
  max-height: 420px;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  scroll-behavior: smooth;
}

.log-loading, .log-error, .log-empty {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.85rem;
  color: var(--text-dim);
  padding: 20px;
  text-align: center;
}

.log-error { color: #ff6b6b; }
.err-icon { color: #ff4d4d; }

.retry-btn {
  display: block;
  margin: 10px auto 0;
  background: none;
  border: 1px solid #ff4d4d;
  color: #ff4d4d;
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.75rem;
  padding: 6px 16px;
  cursor: pointer;
  letter-spacing: 2px;
  transition: all 0.2s ease;
}

.retry-btn:hover { background: rgba(255, 77, 77, 0.1); }

.log-entry {
  background: rgba(0, 255, 65, 0.02);
  border: 1px solid rgba(0, 255, 65, 0.1);
  border-left: 2px solid var(--neon-green);
  padding: 12px 16px;
  animation: fadeInUp 0.4s ease;
}

.log-entry:hover { background: rgba(0, 255, 65, 0.05); }

.entry-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 6px;
  flex-wrap: wrap;
}

.entry-index {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.7rem;
  color: var(--text-dim);
  opacity: 0.6;
}

.entry-name {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--neon-cyan);
  letter-spacing: 1px;
}

.entry-time {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.7rem;
  color: var(--text-dim);
  margin-left: auto;
}

.entry-message {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.82rem;
  color: var(--text-primary);
  line-height: 1.6;
}

.refresh-btn {
  background: none;
  border: none;
  border-top: 1px solid rgba(0, 255, 65, 0.1);
  color: var(--text-dim);
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.78rem;
  padding: 12px;
  cursor: pointer;
  letter-spacing: 2px;
  transition: all 0.2s ease;
  width: 100%;
}

.refresh-btn:hover {
  color: var(--neon-green);
  background: rgba(0, 255, 65, 0.04);
}

.dots { display: inline-block; animation: dotBlink 1.2s step-end infinite; }

@keyframes dotBlink {
  0%, 100% { opacity: 1; }
  33% { opacity: 0.3; }
  66% { opacity: 0.6; }
}

.loading-text { color: var(--neon-green); font-family: 'Share Tech Mono', monospace; }

@media (max-width: 768px) {
  .guestlist-layout { grid-template-columns: 1fr; }
}
</style>