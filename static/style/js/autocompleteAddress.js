$("#loading_address").suggestions({
    token: "c8ee837b0820947efe93dae077bbc61f01c96621",
    type: "ADDRESS",
    /* Вызывается, когда пользователь выбирает одну из подсказок */
    onSelect: function(suggestion) {
        console.log(suggestion);
    }
});

$("#unloading_address").suggestions({
    token: "c8ee837b0820947efe93dae077bbc61f01c96621",
    type: "ADDRESS",
    /* Вызывается, когда пользователь выбирает одну из подсказок */
    onSelect: function(suggestion) {
        console.log(suggestion);
    }
});

$("#place_from").suggestions({
    token: "c8ee837b0820947efe93dae077bbc61f01c96621",
    type: "ADDRESS",
    /* Вызывается, когда пользователь выбирает одну из подсказок */
    onSelect: function(suggestion) {
        console.log(suggestion);
    }
});

$("#place_to").suggestions({
    token: "c8ee837b0820947efe93dae077bbc61f01c96621",
    type: "ADDRESS",
    /* Вызывается, когда пользователь выбирает одну из подсказок */
    onSelect: function(suggestion) {
        console.log(suggestion);
    }
});