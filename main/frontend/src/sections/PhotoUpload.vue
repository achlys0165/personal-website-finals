<template>
  <div class="photo-block">
    <div 
      class="photo-frame" 
      @click="triggerUpload"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      :style="isDragging ? {borderColor: 'var(--pink)'} : {}"
    >
      <div v-if="!photoUrl" class="photo-inner">
        <svg class="photo-avatar" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="40" cy="30" r="16" fill="none" stroke="rgba(244,167,185,.35)" stroke-width="1.5"/>
          <path d="M10 72c0-16.569 13.431-30 30-30s30 13.431 30 30" fill="none" stroke="rgba(244,167,185,.35)" stroke-width="1.5"/>
        </svg>
        <p class="photo-hint">Click to upload photo<br><span>or drag &amp; drop</span></p>
      </div>
      <img v-else :src="photoUrl" alt="Profile" style="display:block;width:100%;height:100%;object-fit:cover;border-radius:4px;">
      <input type="file" ref="input" accept="image/*" style="display:none" @change="handleFile">
    </div>
    <div class="photo-meta">
      <div class="photo-name">Your Name</div>
      <div class="photo-role">Student · Aspiring Pentester</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const input = ref(null)
const photoUrl = ref('')
const isDragging = ref(false)

const triggerUpload = () => input.value?.click()

const handleFile = (e) => {
  const file = e.target.files[0]
  if (file) readFile(file)
}

const handleDrop = (e) => {
  isDragging.value = false
  const file = e.dataTransfer.files[0]
  if (file && file.type.startsWith('image/')) readFile(file)
}

const readFile = (file) => {
  const reader = new FileReader()
  reader.onload = (ev) => { photoUrl.value = ev.target.result }
  reader.readAsDataURL(file)
}
</script>

<style scoped>
.photo-block{margin-bottom:1.25rem;}
.photo-frame{
  width:100%;aspect-ratio:1/1;
  background:var(--ink2);
  border:1px dashed var(--rule2);
  border-radius:4px;
  display:flex;align-items:center;justify-content:center;
  cursor:pointer;
  position:relative;overflow:hidden;
  transition:border-color .25s, background .25s;
}
.photo-frame:hover{border-color:var(--pink);background:var(--ink3);}
.photo-inner{
  display:flex;flex-direction:column;align-items:center;gap:.9rem;
  padding:1.5rem;text-align:center;
  pointer-events:none;
}
.photo-avatar{width:64px;height:64px;opacity:.6;}
.photo-hint{
  font-family:var(--mono);font-size:10px;letter-spacing:.06em;
  color:var(--muted2);line-height:1.6;
}
.photo-hint span{color:var(--muted2);transition:color .2s;font-size:9px;}
.photo-meta{
  padding:.85rem 0 0;
  display:flex;flex-direction:column;gap:3px;
}
.photo-name{
  font-family:var(--serif);font-size:1.05rem;font-weight:700;
  color:var(--white);
}
.photo-role{
  font-family:var(--mono);font-size:10px;letter-spacing:.08em;
  color:var(--pink);text-transform:uppercase;
}
</style>