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
