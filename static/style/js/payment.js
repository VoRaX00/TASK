// function changeInput(){
//     this.change(function(){
            
//                 $('#price_cashless_nds').html(`
//                 <div class="col-4">
//                     <label for="deliveryCostNDS">С НДС</label>
//                 </div>
//                 <div class="col-8">
//                     <input type="number" placeholder="С НДС" class="form-control" id="deliveryCostNDS" name="deliveryCostNDS" min="1" style="max-width: 300px">
//                 </div>
//                 `)
            
//     })
// }

// const f = () => {
//     alert('Hi')
// }

// document.getElementById('without_nds').onclick = function() {
//     alert('Hi')
// }

$(document).ready(function() {
    // При изменении состояния первого чекбокса
    $('#cboxCashless').change(function() {
        if(this.checked) {
            // Если чекбокс выбран, добавить дополнительные чекбоксы
            $('#extra_checkbox').html(`
                <div class="mb-3">
                    <input class="form-check-input" type="checkbox" name="cashless" id="nds" value="nds">
                    <label class="form-check-label" for="nds">НДС</label>
                </div>
                <div class="mb-3">
                    <input class="form-check-input" type="checkbox" name="cashless" id="without_nds" value="without_nds">
                    <label class="form-check-label" for="without_nds">Без НДС</label>
                </div>
            `);
        } else {
            // Если чекбокс не выбран, удалить дополнительные чекбоксы
            $('#extra_checkbox').html('');
        }
    });
});

// $(document).ready(function(){
//     $('#cboxCash').change(function() {
//         if(this.checked) {
//             // Если чекбокс выбран, добавить дополнительные чекбоксы
//             $('#price_cash_checkbox').html(`
//                 <div class="col-4">
//                     <label for="deliveryCostCash">Наличными</label>
//                 </div>
//                 <div class="col-8">
//                     <input type="number" placeholder="Наличными" class="form-control" id="deliveryCostCash" name="deliveryCostCash" min="1" style="max-width: 300px">
//                 </div>
//             `);
//         } else {
//             // Если чекбокс не выбран, удалить дополнительные чекбоксы
//             $('#price_cash_checkbox').html('');
//         }
//     });
// });