<template>
  <div class="rule-div"></div>
</template>

<style scoped>
.rule-div{
  position:relative;z-index:1;
  max-width:1100px;margin:0 auto;
  padding:0 clamp(1.5rem,6vw,5rem);
}
.rule-div::after{content:'';display:block;height:1px;background:var(--rule);}
</style>