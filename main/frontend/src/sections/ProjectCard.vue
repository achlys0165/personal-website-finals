<template>
  <div class="proj">
    <div class="proj-top">
      <span class="proj-ico">{{ project.icon }}</span>
      <a href="#" class="proj-link">↗ view</a>
    </div>
    <div class="proj-name">{{ project.name }}</div>
    <div class="proj-desc">{{ project.desc }}</div>
    <div class="proj-tags">
      <span v-for="tag in project.tags" :key="tag" class="ptag">{{ tag }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({ project: Object })
</script>

<style scoped>
.proj{
  background:var(--ink2);border:1px solid var(--rule);
  border-radius:3px;padding:1.75rem;
  display:flex;flex-direction:column;
  transition:border-color .22s,transform .22s;
  position:relative;overflow:hidden;
}
.proj::before{
  content:'';position:absolute;top:0;left:0;width:2px;height:100%;
  background:linear-gradient(180deg,var(--pink),var(--pink-mid));
  opacity:0;transition:opacity .25s;
}
.proj:hover{border-color:var(--rule2);transform:translateY(-3px);}
.proj:hover::before{opacity:1;}
.proj-wide{grid-column:span 7;}
.proj-narrow{grid-column:span 5;}
.proj-third{grid-column:span 4;}
.proj-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1.25rem;}
.proj-ico{font-size:1.6rem;}
.proj-link{
  font-family:var(--mono);font-size:9px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted2);text-decoration:none;
  border:1px solid var(--rule);border-radius:2px;padding:3px 9px;
  transition:all .2s;
}
.proj-link:hover{border-color:var(--pink);color:var(--pink);}
.proj-name{
  font-family:var(--serif);font-size:1.25rem;font-weight:700;
  color:var(--white);margin-bottom:.5rem;line-height:1.2;
}
.proj-desc{font-size:12px;color:var(--muted2);line-height:1.65;flex:1;}
.proj-tags{display:flex;flex-wrap:wrap;gap:.35rem;margin-top:1.25rem;}
.ptag{
  font-family:var(--mono);font-size:9px;letter-spacing:.07em;text-transform:uppercase;
  padding:2px 8px;border-radius:2px;
  background:var(--pink-dim);color:var(--pink);
  border:1px solid rgba(244,167,185,.18);
}
</style>