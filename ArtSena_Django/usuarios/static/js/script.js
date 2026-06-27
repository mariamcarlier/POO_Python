'use strict';

/* ═══════════════════════════════════════
   ArtSENA — script.js
   Funcionalidades:
   1. Navbar toggle móvil
   2. Animación de entrada (stagger) en cards
   3. Highlight de nav-link activo
   ═══════════════════════════════════════ */

/* ── 1. NAVBAR TOGGLE MÓVIL ── */
function initNavToggle() {
  const toggle   = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (!toggle || !navLinks) return;

  toggle.addEventListener('click', function () {
    const isOpen = navLinks.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });

  // Cerrar al hacer click en un link
  navLinks.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

/* ── 2. ANIMACIÓN DE ENTRADA CON INTERSECTION OBSERVER ── */
function initCardAnimations() {
  // Agrega clase CSS que controla la animación de entrada
  const style = document.createElement('style');
  style.textContent = `
    .obra-card,
    .artista-card,
    .stat-card,
    .poo-card {
      opacity: 0;
      transform: translateY(24px);
      transition: opacity 0.45s ease, transform 0.45s cubic-bezier(.22,.68,0,1.1);
    }
    .obra-card.is-visible,
    .artista-card.is-visible,
    .stat-card.is-visible,
    .poo-card.is-visible {
      opacity: 1;
      transform: translateY(0);
    }
  `;
  document.head.appendChild(style);

  const cards = document.querySelectorAll(
    '.obra-card, .artista-card, .stat-card, .poo-card'
  );

  if (!cards.length) return;

  // Respeta preferencia de reducción de movimiento
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    cards.forEach(c => c.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          // Stagger: cada card aparece 60ms después de la anterior
          setTimeout(() => {
            entry.target.classList.add('is-visible');
          }, i * 60);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );

  cards.forEach(card => observer.observe(card));
}

/* ── 3. HIGHLIGHT DEL LINK ACTIVO EN NAVBAR ── */
function initActiveNavLink() {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll('.nav-link');

  links.forEach(link => {
    const href = link.getAttribute('href');
    // Considera activo si el path actual empieza con el href del link
    // (excepto '/' que solo es activo si es exactamente '/')
    if (
      (href === '/' && currentPath === '/') ||
      (href !== '/' && currentPath.startsWith(href))
    ) {
      link.style.color = 'var(--clr-gold)';
      link.setAttribute('aria-current', 'page');
    }
  });
}

/* ── INIT ── */
function init() {
  initNavToggle();
  initCardAnimations();
  initActiveNavLink();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}