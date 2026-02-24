export const vReveal = {
  mounted(el) {
    el.classList.add('rv')
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in')
          obs.unobserve(e.target)
        }
      })
    }, { threshold: 0.08 })
    obs.observe(el)
  }
}