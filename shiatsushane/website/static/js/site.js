// static/js/site.js
const toggle = document.querySelector('.nav-toggle');
const menu = document.querySelector('.menu');
if (toggle && menu){
toggle.addEventListener('click', () => {
const open = getComputedStyle(menu).display !== 'none';
menu.style.display = open ? 'none' : 'flex';
toggle.setAttribute('aria-expanded', String(!open));
});
}