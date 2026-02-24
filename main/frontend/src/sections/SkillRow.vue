<template>
  <tr class="sk-row">
    <td class="sk-icon">{{ skill.icon }}</td>
    <td><div class="sk-name">{{ skill.name }}</div></td>
    <td class="sk-desc">{{ skill.desc }}</td>
    <td class="sk-level"><span class="sk-badge" :class="skill.cls">{{ skill.level }}</span></td>
  </tr>
</template>

<script setup>
defineProps({ skill: Object })
</script>

<style scoped>
.sk-row{
  border-bottom:1px solid var(--rule);
  transition:background .2s;
}
.sk-row:hover{background:var(--ink2);}
.sk-row td{padding:1.1rem 1rem 1.1rem 0;vertical-align:middle;}
.sk-icon{font-size:1.3rem;width:3rem;padding-left:.5rem !important;}
.sk-name{
  font-family:var(--serif);font-size:1.25rem;
  color:var(--white);font-weight:700;letter-spacing:.01em;
}
.sk-desc{font-size:12px;color:var(--muted2);padding-left:1rem !important;}
.sk-level{text-align:right !important;padding-right:.5rem !important;}
.sk-badge{
  display:inline-block;
  font-family:var(--mono);font-size:9px;letter-spacing:.08em;
  padding:3px 10px;border-radius:2px;text-transform:uppercase;
}
.lvl-adv{background:rgba(244,167,185,.12);color:var(--pink);border:1px solid rgba(244,167,185,.25);}
.lvl-int{background:rgba(244,167,185,.07);color:var(--pink-mid);border:1px solid rgba(244,167,185,.15);}
.lvl-beg{background:var(--ink3);color:var(--muted2);border:1px solid var(--rule);}
</style>