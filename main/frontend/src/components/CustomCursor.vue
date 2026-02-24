<template>
  <div id="cur" ref="cur"></div>
  <div id="cur-ring" ref="ring"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const cur = ref(null)
const ring = ref(null)
let mx = 0, my = 0, rx = 0, ry = 0, raf = null

const onMove = (e) => {
  mx = e.clientX
  my = e.clientY
  if (cur.value) {
    cur.value.style.left = mx + 'px'
    cur.value.style.top = my + 'px'
  }
}

const tick = () => {
  rx += (mx - rx) * 0.12
  ry += (my - ry) * 0.12
  if (ring.value) {
    ring.value.style.left = rx + 'px'
    ring.value.style.top = ry + 'px'
  }
  raf = requestAnimationFrame(tick)
}

const onEnter = () => {
  if (!ring.value) return
  ring.value.style.width = '52px'
  ring.value.style.height = '52px'
  ring.value.style.borderColor = 'rgba(244,167,185,.65)'
  ring.value.style.borderRadius = '4px'
}

const onLeave = () => {
  if (!ring.value) return
  ring.value.style.width = '34px'
  ring.value.style.height = '34px'
  ring.value.style.borderColor = 'rgba(244,167,185,.3)'
  ring.value.style.borderRadius = '50%'
}

onMounted(() => {
  document.addEventListener('mousemove', onMove)
  raf = requestAnimationFrame(tick)
  
  const addListeners = () => {
    document.querySelectorAll('a,button,.cert-card,.proj,.sk-row').forEach(el => {
      el.addEventListener('mouseenter', onEnter)
      el.addEventListener('mouseleave', onLeave)
    })
  }
  addListeners()
  setTimeout(addListeners, 1000)
})

onUnmounted(() => {
  document.removeEventListener('mousemove', onMove)
  cancelAnimationFrame(raf)
})
</script>

<style scoped>
#cur{
  position:fixed;width:7px;height:7px;
  background:var(--pink);border-radius:50%;
  pointer-events:none;z-index:9999;
  transform:translate(-50%,-50%);
  transition:transform .08s;
}
#cur-ring{
  position:fixed;width:34px;height:34px;
  border:1px solid rgba(244,167,185,.3);
  border-radius:50%;pointer-events:none;z-index:9998;
  transform:translate(-50%,-50%);
  transition:width .25s,height .25s,border-color .25s,border-radius .25s;
}
</style>