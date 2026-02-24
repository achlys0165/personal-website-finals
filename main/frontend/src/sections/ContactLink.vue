<template>
  <a :href="link.href" class="clink" :target="link.ext ? '_blank' : null" :rel="link.ext ? 'noopener' : null">
    <span class="clink-label"><span class="clink-ico">{{ link.icon }}</span> {{ link.label }}</span>
    <span class="clink-arr">→</span>
  </a>
</template>

<script setup>
defineProps({ link: Object })
</script>

<style scoped>
.clink{
  display:flex;align-items:center;justify-content:space-between;
  padding:.75rem 1rem;
  background:var(--ink2);border:1px solid var(--rule);border-radius:2px;
  text-decoration:none;color:var(--muted2);font-size:12px;
  transition:all .2s;
  font-family:var(--mono);
}
.clink:hover{border-color:var(--rule2);color:var(--pink);background:var(--ink3);}
.clink-label{display:flex;align-items:center;gap:.75rem;}
.clink-ico{color:var(--pink);font-size:13px;width:16px;text-align:center;}
.clink-arr{font-size:12px;color:var(--rule2);transition:color .2s,transform .2s;}
.clink:hover .clink-arr{color:var(--pink);transform:translateX(3px);}
</style>