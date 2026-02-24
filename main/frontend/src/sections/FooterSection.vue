<template>
  <footer>
    <div class="footer-inner">
      <p class="foot-l">© 2026 <span>Jan Sultan</span>. Built with curiosity &amp; stubbornness.</p>
      <div class="foot-r"><span class="pulse"></span>Currently learning — always</div>
    </div>
  </footer>
</template>

<style scoped>
footer{
  position:relative;z-index:1;
  border-top:1px solid var(--rule);
}
.footer-inner{
  max-width:1100px;margin:0 auto;
  padding:1.75rem clamp(1.5rem,6vw,5rem);
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;
}
.foot-l{font-family:var(--serif);font-style:italic;font-size:13px;color:var(--muted2);}
.foot-l span{color:var(--pink);}
.foot-r{display:flex;align-items:center;gap:7px;font-family:var(--mono);font-size:10px;color:var(--muted2);letter-spacing:.08em;}
.pulse{width:6px;height:6px;border-radius:50%;background:var(--pink);animation:pls 2.4s ease-in-out infinite;}
</style>