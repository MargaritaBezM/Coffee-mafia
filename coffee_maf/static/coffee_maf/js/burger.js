function initBurgerMenu() {
  const burgerBtn = document.getElementById('burger');
  const menu = document.querySelector('.header_menu_list');
  const overlay = document.getElementById('overlay');

  if (!burgerBtn || !menu || !overlay) {
    console.error('Ошибка: не найдены элементы бургер-меню!');
    return;
  }

  function toggleMenu() {
    burgerBtn.classList.toggle('active');
    menu.classList.toggle('active');
    overlay.classList.toggle('active');
  }

  burgerBtn.addEventListener('click', toggleMenu);

  overlay.addEventListener('click', toggleMenu);
}

document.addEventListener('DOMContentLoaded', initBurgerMenu);