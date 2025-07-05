input.onButtonPressed(Button.A, function on_button_pressed_a() {
    led.toggle(2, 4)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    led.toggle(1, 3)
})
basic.forever(function on_forever() {
    
})
