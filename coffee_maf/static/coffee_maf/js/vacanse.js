document.getElementById('id_phone').addEventListener('input', function(e) {
    let value = this.value.replace(/\D/g, '');

    if (value.startsWith('8')) value = value.substring(1);
    if (value.startsWith('7')) value = value.substring(1);

    let formatted = '+7';
    if (value.length > 0) formatted += ' (' + value.substring(0, 3);
    if (value.length > 3) formatted += ') ' + value.substring(3, 6);
    if (value.length > 6) formatted += '-' + value.substring(6, 8);
    if (value.length > 8) formatted += '-' + value.substring(8, 10);

    this.value = formatted.substring(0, 18);
    validatePhone();
});

document.getElementById('id_email').addEventListener('input', validateEmail);
document.getElementById('id_phone').addEventListener('blur', validatePhone);

function validateEmail() {
    const email = this.value.trim();
    const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    toggleError('id_email', isValid, 'Введите корректный email');
}

function validatePhone() {
    const phone = document.getElementById('id_phone').value.trim();
    const isValid = /^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/.test(phone);
    toggleError('id_phone', isValid, 'Формат: +7 (XXX) XXX-XX-XX');
}

function toggleError(fieldId, isValid, errorMessage) {
    const input = document.getElementById(fieldId);
    const errorElement = document.getElementById(`${fieldId}Error`);

    if (!isValid && input.value.trim() !== '') {
        input.classList.add('error-border');
        errorElement.textContent = errorMessage;
        errorElement.classList.add('show');
    } else {
        input.classList.remove('error-border');
        errorElement.textContent = '';
        errorElement.classList.remove('show');
    }
}

function validateForm() {
    validateEmail.call(document.getElementById('id_email'));
    validatePhone();

    const errors = document.querySelectorAll('.error-border');
    const consent = document.getElementById('consent').checked;
    const vacancy = document.getElementById('id_vacancy').value;

    if (!vacancy) {
        alert('Пожалуйста, выберите вакансию');
        return false;
    }

    if (errors.length > 0 || !consent) {
        if (!consent) alert('Дайте согласие на обработку данных');
        return false;
    }
    return true;
}

document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.vacanse-card_button');

    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const card = this.closest('.vacanse-card');
            const vacancyId = card.dataset.vacancyId;
            const vacancyTitle = card.querySelector('.vacanse-card_title').textContent;

            document.querySelector('[name="vacancy"]').value = vacancyId;
            document.querySelector('[name="position_text"]').value = vacancyTitle;

            const positionField = document.getElementById('position');
            if (positionField) {
                positionField.value = vacancyTitle;
            }
        });
    });
});