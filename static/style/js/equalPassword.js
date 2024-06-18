document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    var password1Input = document.getElementById('InputPassword1');
    var password2Input = document.getElementById('InputPassword2');

    form.addEventListener('submit', function(event) {
        if (password1Input.value !== password2Input.value) {
            alert('Пароли не совпадают');
            event.preventDefault(); // Остановить отправку формы
        }
    });
});