document.querySelectorAll('.country').forEach(country => {
    country.addEventListener('click', () => {
       
        document.getElementById('popup-text').textContent = country.dataset.info;
        document.getElementById('popup').style.display = 'flex';
    });
});

document.querySelector('.close').addEventListener('click', () => {
    document.getElementById('popup').style.display = 'none';
});

document.getElementById('popup').addEventListener('click', (e) => {
    if (e.target === document.getElementById('popup')) {
        document.getElementById('popup').style.display = 'none';
    }
});

const burgerBtn = document.getElementById('burger');
const menu = document.querySelector('.header_menu_list');
const overlay = document.getElementById('overlay');

burgerBtn.addEventListener('click', () => {
    burgerBtn.classList.toggle('active');
    menu.classList.toggle('active');
    overlay.classList.toggle('active');
});

overlay.addEventListener('click', () => {
    burgerBtn.classList.remove('active');
    menu.classList.remove('active');
    overlay.classList.remove('active');
});