<template>
  <div class="sidebar-block">
    <div class="sb-label">Interests</div>
    <div class="interest-list">
      <div class="int-item">Web Exploitation</div>
      <div class="int-item">AI & Automation</div>
      <div class="int-item">CTF Competitions</div>
      <div class="int-item">Linux & Open Source</div>
      <div class="int-item">Arduino & IoT</div>
      <div class="int-item">OSINT</div>
    </div>
  </div>
</template>

<style scoped>
.sidebar-block{
  background:var(--ink2);
  border:1px solid var(--rule);
  border-radius:3px;
  padding:1.5rem;
  margin-bottom:1rem;
}
.sb-label{
  font-family:var(--mono);font-size:9px;
  letter-spacing:.18em;text-transform:uppercase;
  color:var(--muted2);margin-bottom:1rem;
  padding-bottom:.6rem;
  border-bottom:1px solid var(--rule);
}
.interest-list{display:flex;flex-direction:column;gap:.35rem;}
.int-item{
  font-size:11px;color:var(--muted2);
  padding:.35rem .75rem;
  border:1px solid var(--rule);border-radius:2px;
  display:flex;align-items:center;gap:.6rem;
  transition:all .2s;
}
.int-item:hover{border-color:var(--pink-dim);color:var(--muted);}
.int-item::before{content:'→';color:var(--pink);font-size:9px;}
</style>