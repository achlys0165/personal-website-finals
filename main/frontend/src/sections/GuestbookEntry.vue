<template>
  <div class="gb-entry">
    <div class="gb-entry-head">
      <div class="gb-name">{{ entry.name }}</div>
      <span class="gb-time">{{ formattedDate }}</span>
    </div>
    <div class="gb-msg">{{ entry.message }}</div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({ entry: Object })

const formattedDate = computed(() => {
  return new Date(entry.created_at).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })
})
</script>

<style scoped>
.gb-entry {
  padding: 1.1rem 0;
  border-bottom: 1px solid var(--rule);
  animation: fadeUp 0.35s ease forwards;
}

.gb-entry:first-child {
  border-top: 1px solid var(--rule);
}

.gb-entry-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 0.4rem;
}

.gb-name {
  font-family: var(--serif);
  font-size: 1rem;
  font-weight: 700;
  color: var(--white);
}

.gb-time {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--muted2);
}

.gb-msg {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.65;
  font-weight: 300;
  word-break: break-word;
}
</style>