<template>
  <div class="bg-noise"></div>
  <div class="bg-orb1"></div>
  <div class="bg-orb2"></div>
</template>

<style scoped>
.bg-noise{
  position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.45;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.04'/%3E%3C/svg%3E");
}
.bg-orb1{position:fixed;pointer-events:none;z-index:0;width:600px;height:600px;background:radial-gradient(ellipse,rgba(244,167,185,.07) 0%,transparent 68%);top:-180px;right:-80px;border-radius:50%;}
.bg-orb2{position:fixed;pointer-events:none;z-index:0;width:400px;height:400px;background:radial-gradient(ellipse,rgba(232,121,154,.05) 0%,transparent 68%);bottom:-100px;left:-60px;border-radius:50%;}
</style>