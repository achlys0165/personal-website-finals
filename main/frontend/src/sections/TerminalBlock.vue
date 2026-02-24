<template>
  <div class="terminal">
    <div class="t-bar">
      <span class="t-dot td-r"></span>
      <span class="t-dot td-y"></span>
      <span class="t-dot td-g"></span>
      <span class="t-ttl">zsh — ~/whoami</span>
    </div>
    <div class="t-body">
      <div class="tl"><span class="tp">❯ </span><span class="tc">cat profile.json</span></div>
      <div class="tl"><span class="to">{</span></div>
      <div class="tl" style="padding-left:1rem"><span class="to">"role":   </span><span class="ts">"student + aspiring pentester"</span><span class="to">,</span></div>
      <div class="tl" style="padding-left:1rem"><span class="to">"stack":  </span><span class="tv">["Python","Linux","CTFs"]</span><span class="to">,</span></div>
      <div class="tl" style="padding-left:1rem"><span class="to">"status": </span><span class="tv">learning_actively</span><span class="to">,</span></div>
      <div class="tl" style="padding-left:1rem"><span class="to">"open":   </span><span class="tv">true</span></div>
      <div class="tl"><span class="to">}</span></div>
      <div class="tl" style="margin-top:.5rem"><span class="tp">❯ </span><span class="tblk"></span></div>
    </div>
  </div>
</template>

<style scoped>
.terminal{
  background:var(--ink2);
  border:1px solid var(--rule2);
  border-radius:4px;overflow:hidden;
  box-shadow:0 24px 60px rgba(0,0,0,.5),0 0 0 1px var(--rule);
}
.t-bar{
  background:var(--ink3);border-bottom:1px solid var(--rule);
  padding:9px 14px;display:flex;align-items:center;gap:6px;
}
.t-dot{width:10px;height:10px;border-radius:50%;}
.td-r{background:#ff5f57;}.td-y{background:#febc2e;}.td-g{background:#28c840;}
.t-ttl{font-family:var(--mono);font-size:10px;color:var(--muted2);margin-left:6px;letter-spacing:.06em;}
.t-body{padding:1rem 1.25rem;font-family:var(--mono);font-size:11.5px;}
.tl{margin-bottom:.28rem;}
.tp{color:var(--pink-mid);}
.tc{color:var(--white);}
.to{color:var(--muted2);}
.tv{color:#f9c0cb;}
.ts{color:#fde68a;}
.tblk{display:inline-block;width:7px;height:11px;background:var(--pink);vertical-align:text-bottom;margin-left:2px;animation:blink 1s step-end infinite;}
</style>