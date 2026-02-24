<template>
  <div class="proj">
    <div class="proj-top">
      <span class="proj-ico">{{ project.icon }}</span>
      <div class="proj-links">
        <a 
          v-if="project.github" 
          :href="project.github" 
          class="proj-link github"
          target="_blank"
          rel="noopener noreferrer"
        >
          <svg class="github-icon" viewBox="0 0 16 16" fill="currentColor">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
          </svg>
          Code
        </a>
        <a href="#" class="proj-link">↗ Demo</a>
      </div>
    </div>
    <div class="proj-name">{{ project.name }}</div>
    <div class="proj-desc">{{ project.description }}</div>
    <div class="proj-tags">
      <span v-for="tag in project.tags" :key="tag" class="ptag">{{ tag }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  project: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.proj {
  background: var(--ink2);
  border: 1px solid var(--rule);
  border-radius: 3px;
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  transition: border-color 0.22s, transform 0.22s;
  position: relative;
  overflow: hidden;
}

.proj::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, var(--pink), var(--pink-mid));
  opacity: 0;
  transition: opacity 0.25s;
}

.proj:hover {
  border-color: var(--rule2);
  transform: translateY(-3px);
}

.proj:hover::before {
  opacity: 1;
}

.proj-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.25rem;
}

.proj-ico {
  font-size: 1.6rem;
}

.proj-links {
  display: flex;
  gap: 0.5rem;
}

.proj-link {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted2);
  text-decoration: none;
  border: 1px solid var(--rule);
  border-radius: 2px;
  padding: 3px 9px;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 4px;
}

.proj-link:hover {
  border-color: var(--pink);
  color: var(--pink);
}

.proj-link.github:hover {
  border-color: #fff;
  color: #fff;
}

.github-icon {
  width: 12px;
  height: 12px;
}

.proj-name {
  font-family: var(--serif);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.proj-desc {
  font-size: 12px;
  color: var(--muted2);
  line-height: 1.65;
  flex: 1;
}

.proj-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-top: 1.25rem;
}

.ptag {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 2px;
  background: var(--pink-dim);
  color: var(--pink);
  border: 1px solid rgba(244,167,185,.18);
}
</style>