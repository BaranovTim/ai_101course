// Visual effects layer: scroll reveals, count-up stats, rotating headline word,
// particle "neural network" canvas, 3D card tilt, animated progress bars.
// Everything degrades gracefully and respects prefers-reduced-motion.
(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Scroll reveal ----------
  const revealEls = document.querySelectorAll("[data-reveal]");
  if (revealEls.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      revealEls.forEach((el) => el.classList.add("revealed"));
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const delay = parseInt(entry.target.dataset.revealDelay || "0", 10);
              setTimeout(() => entry.target.classList.add("revealed"), delay);
              io.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
      );
      revealEls.forEach((el) => io.observe(el));
    }
  }

  // ---------- Count-up numbers ----------
  const counters = document.querySelectorAll("[data-countup]");
  if (counters.length && !reduceMotion && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        io.unobserve(el);
        const target = parseInt(el.dataset.countup, 10);
        const suffix = el.dataset.suffix || "";
        const dur = 1400;
        const start = performance.now();
        function tick(now) {
          const p = Math.min((now - start) / dur, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased).toLocaleString() + suffix;
          if (p < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.5 });
    counters.forEach((el) => io.observe(el));
  }

  // ---------- Rotating headline word ----------
  const rotator = document.getElementById("word-rotator");
  if (rotator && !reduceMotion) {
    let words = [];
    try { words = JSON.parse(rotator.dataset.words || "[]"); } catch (e) { /* noop */ }
    if (words.length > 1) {
      let wi = 0, ci = words[0].length, deleting = false;
      const type = () => {
        const word = words[wi];
        ci += deleting ? -1 : 1;
        rotator.textContent = word.slice(0, ci);
        let pause = deleting ? 45 : 95;
        if (!deleting && ci === word.length) { deleting = true; pause = 2100; }
        else if (deleting && ci === 0) { deleting = false; wi = (wi + 1) % words.length; pause = 350; }
        setTimeout(type, pause);
      };
      setTimeout(type, 1600);
    }
  }

  // ---------- Particle neural-network canvas ----------
  const canvas = document.getElementById("hero-canvas");
  if (canvas && !reduceMotion) {
    const ctx = canvas.getContext("2d");
    let W, H, particles, raf;
    const DENSITY = 1 / 22000; // particles per px²
    const LINK_DIST = 130;

    function resize() {
      const rect = canvas.parentElement.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = rect.width; H = rect.height;
      canvas.width = W * dpr; canvas.height = H * dpr;
      canvas.style.width = W + "px"; canvas.style.height = H + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.min(90, Math.max(28, Math.floor(W * H * DENSITY)));
      particles = Array.from({ length: n }, () => ({
        x: Math.random() * W, y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.45, vy: (Math.random() - 0.5) * 0.45,
        r: 1.2 + Math.random() * 2.2,
      }));
    }

    let mouse = { x: -9999, y: -9999 };
    canvas.parentElement.addEventListener("pointermove", (e) => {
      const rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left; mouse.y = e.clientY - rect.top;
    });
    canvas.parentElement.addEventListener("pointerleave", () => { mouse.x = -9999; mouse.y = -9999; });

    function step() {
      ctx.clearRect(0, 0, W, H);
      for (const p of particles) {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > W) p.vx *= -1;
        if (p.y < 0 || p.y > H) p.vy *= -1;
        // gentle attraction to the pointer
        const dxm = mouse.x - p.x, dym = mouse.y - p.y;
        const dm = Math.hypot(dxm, dym);
        if (dm < 160 && dm > 0.001) { p.x += (dxm / dm) * 0.25; p.y += (dym / dm) * 0.25; }
      }
      // links
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const a = particles[i], b = particles[j];
          const d = Math.hypot(a.x - b.x, a.y - b.y);
          if (d < LINK_DIST) {
            ctx.strokeStyle = "rgba(79, 70, 229, " + (0.16 * (1 - d / LINK_DIST)).toFixed(3) + ")";
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
      }
      // nodes
      for (const p of particles) {
        ctx.fillStyle = "rgba(131, 26, 218, 0.35)";
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
      }
      raf = requestAnimationFrame(step);
    }

    resize();
    window.addEventListener("resize", resize);
    // pause when off-screen to save battery
    if ("IntersectionObserver" in window) {
      new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) { if (!raf) raf = requestAnimationFrame(step); }
          else { cancelAnimationFrame(raf); raf = null; }
        });
      }).observe(canvas);
    } else {
      raf = requestAnimationFrame(step);
    }
  }

  // ---------- 3D tilt on cards ----------
  if (!reduceMotion && matchMedia("(pointer: fine)").matches) {
    document.querySelectorAll(".tilt").forEach((card) => {
      card.addEventListener("pointermove", (e) => {
        const rect = card.getBoundingClientRect();
        const px = (e.clientX - rect.left) / rect.width - 0.5;
        const py = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform =
          "perspective(800px) rotateX(" + (-py * 7).toFixed(2) + "deg) rotateY(" + (px * 9).toFixed(2) + "deg) translateY(-4px)";
      });
      card.addEventListener("pointerleave", () => { card.style.transform = ""; });
    });
  }

  // ---------- Animated progress bars ----------
  // Any gradient fill bar with an inline width sweeps in from 0.
  const bars = document.querySelectorAll('[class*="bg-gradient-to-r"][style*="width"]');
  if (bars.length && !reduceMotion) {
    bars.forEach((bar) => {
      const target = bar.style.width;
      bar.classList.add("bar-animated");
      bar.style.width = "0%";
      requestAnimationFrame(() => requestAnimationFrame(() => { bar.style.width = target; }));
    });
  }

  // ---------- Sticky nav shadow ----------
  const header = document.querySelector("header.sticky");
  if (header) {
    const onScroll = () => header.classList.toggle("nav-scrolled", window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }
})();
