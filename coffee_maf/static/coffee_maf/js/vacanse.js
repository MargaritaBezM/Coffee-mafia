// Маска для телефона: +7 (XXX) XXX-XX-XX
document.getElementById('phone').addEventListener('input', function(e) {
    let value = this.value.replace(/\D/g, '');
    
    if (value.startsWith('8')) value = value.substring(1);
    if (value.startsWith('7')) value = value.substring(1);
    
    // Форматирование
    let formatted = '+7';
    if (value.length > 0) formatted += ' (' + value.substring(0, 3);
    if (value.length > 3) formatted += ') ' + value.substring(3, 6);
    if (value.length > 6) formatted += '-' + value.substring(6, 8);
    if (value.length > 8) formatted += '-' + value.substring(8, 10);
    
    this.value = formatted.substring(0, 18);
    validatePhone();
  });
  
  // Realtime-валидация полей
  document.getElementById('email').addEventListener('input', validateEmail);
  document.getElementById('phone').addEventListener('blur', validatePhone);
  
  function validateEmail() {
    const email = this.value.trim();
    const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    toggleError('email', isValid, 'Введите корректный email');
  }
  
  function validatePhone() {
    const phone = document.getElementById('phone').value.trim();
    const isValid = /^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/.test(phone);
    toggleError('phone', isValid, 'Формат: +7 (XXX) XXX-XX-XX');
  }
  
  // Показ/скрытие ошибок
  function toggleError(fieldId, isValid, errorMessage) {
    const input = document.getElementById(fieldId);
    const errorElement = document.getElementById(`${fieldId}Error`);
    
    if (!isValid && input.value.trim() !== '') {
      input.classList.add('error-border');
      errorElement.textContent = errorMessage;
    } else {
      input.classList.remove('error-border');
      errorElement.textContent = '';
    }
  }
  
  // Валидация при отправке формы
  function validateForm() {
    validateEmail.call(document.getElementById('email'));
    validatePhone();
    
    const errors = document.querySelectorAll('.error-border');
    const consent = document.getElementById('consent').checked;
    
    if (errors.length > 0 || !consent) {
      if (!consent) alert('Дайте согласие на обработку данных');
      return false;
    }
    return true;
  }

  document.addEventListener('DOMContentLoaded', function() {
    // Находим все кнопки "Откликнуться" и поле "Должность"
    const buttons = document.querySelectorAll('.vacanse-card_button');
    const positionInput = document.getElementById('position');
    const formSection = document.getElementById('form');
  
    // Для каждой кнопки добавляем обработчик
    buttons.forEach(button => {
      button.addEventListener('click', function(e) {
        e.preventDefault(); // Отменяем переход по ссылке
  
        // Находим заголовок карточки, в которой находится кнопка
        const card = this.closest('.vacanse-card');
        const title = card.querySelector('.vacanse-card_title').textContent;
  
        // Заполняем поле "Должность"
        positionInput.value = title.trim();
  
        // Плавный скролл к форме
        formSection.scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
  });