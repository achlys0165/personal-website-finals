<template>
  <div class="hero-meta-col">
    <div class="hero-meta-item"><span class="hmi-k">Focus</span><span class="hmi-v">Penetration Testing</span></div>
    <div class="hero-meta-item"><span class="hmi-k">Platform</span><span class="hmi-v">HackTheBox · TryHackMe</span></div>
    <div class="hero-meta-item"><span class="hmi-k">Status</span><span class="hmi-v">Open to opportunities</span></div>
  </div>
</template>

<style scoped>
.hero-meta-col{
  display:grid;grid-template-columns:1fr;gap:.5rem;
}
.hero-meta-item{
  display:flex;justify-content:space-between;align-items:baseline;
  padding:.65rem 1rem;
  background:var(--ink2);
  border:1px solid var(--rule);
  border-radius:2px;
  font-family:var(--mono);font-size:11px;
}
.hmi-k{color:var(--muted2);letter-spacing:.06em;}
.hmi-v{color:var(--pink);}
</style>