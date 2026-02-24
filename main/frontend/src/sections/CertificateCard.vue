<template>
  <div class="cert-card">
    <div class="cert-badge">{{ cert.badge }}</div>
    <div class="cert-body">
      <div class="cert-issuer">{{ cert.issuer }}</div>
      <div class="cert-name">{{ cert.name }}</div>
      <div :class="['cert-status', cert.earned ? 'cert-earned' : 'cert-progress']">
        <span class="cert-dot"></span>
        {{ cert.earned ? 'Earned' : 'In Progress' }}
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ cert: Object })
</script>

<style scoped>
.cert-card{
  background:var(--ink2);
  border:1px solid var(--rule);
  border-radius:3px;
  padding:1.65rem;
  display:flex;gap:1.25rem;align-items:flex-start;
  transition:border-color .22s,transform .22s;
  position:relative;overflow:hidden;
}
.cert-card::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,var(--pink),transparent);
  opacity:0;transition:opacity .25s;
}
.cert-card:hover{border-color:var(--rule2);transform:translateY(-2px);}
.cert-card:hover::after{opacity:1;}
.cert-badge{
  flex-shrink:0;width:52px;height:52px;border-radius:6px;
  display:flex;align-items:center;justify-content:center;
  font-size:1.6rem;
  background:var(--ink3);border:1px solid var(--rule);
}
.cert-issuer{
  font-family:var(--mono);font-size:9px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--pink);margin-bottom:.35rem;
}
.cert-name{
  font-family:var(--serif);font-size:1.05rem;font-weight:700;
  color:var(--white);line-height:1.3;margin-bottom:.5rem;
}
.cert-status{
  display:inline-flex;align-items:center;gap:5px;
  font-family:var(--mono);font-size:9px;letter-spacing:.08em;text-transform:uppercase;
}
.cert-dot{width:5px;height:5px;border-radius:50%;}
.cert-earned .cert-dot{background:var(--pink);}
.cert-earned{color:var(--pink);}
.cert-progress .cert-dot{background:var(--muted2);animation:blink 1.5s ease-in-out infinite;}
.cert-progress{color:var(--muted2);}
</style>