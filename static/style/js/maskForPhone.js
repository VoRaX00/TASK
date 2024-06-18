// $(document).ready(function(){
// $('#phone').mask('+7 (999) 999-99-99');
// });

  $(document).ready(function(){
    // Функция для обновления маски в соответствии с введенным кодом страны
    function updateMask(countryCodeLength) {
      var mask = '+';
      for (var i = 0; i < countryCodeLength; i++) {
        mask += '9';
      }
      mask += ' 999 999 99 99';
      return mask;
    }
    
    // Устанавливаем начальную маску с длиной кода страны в одну цифру
    var initialCountryCodeLength = 1;
    var initialMask = updateMask(initialCountryCodeLength);
    
    $('#phone').inputmask({
      mask: initialMask,
      placeholder: '+',
      definitions: {
        '9': {
          validator: '[0-9]',
          cardinality: 1
        }
      }
    });
    
    // Слушаем изменения в поле ввода кода страны и обновляем маску
    $('#phone').on('input', function() {
      var countryCodeLength = $(this).val().replace(/\D/g, '').length;
      var newMask = updateMask(countryCodeLength);
      $(this).inputmask('option', { mask: newMask });
    });
  });