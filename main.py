def on_button_pressed_a():
    global countA, countB
    pins.digital_write_pin(DigitalPin.P14, 0)
    pins.digital_write_pin(DigitalPin.P15, 0)
    pins.digital_write_pin(DigitalPin.P16, 0)
    countA += 1
    countB = 0
    if countA == 2:
        countA = 0
    basic.pause(200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global countB
    pins.digital_write_pin(DigitalPin.P14, 0)
    pins.digital_write_pin(DigitalPin.P15, 0)
    pins.digital_write_pin(DigitalPin.P16, 0)
    countB = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global countB, countA
    countB += 1
    countA = 0
    if countB == 4:
        countB = 0
    basic.pause(200)
input.on_button_pressed(Button.B, on_button_pressed_b)

countB = 0
countA = 0
countA = 0
countB = 0
pins.digital_write_pin(DigitalPin.P14, 0)
pins.digital_write_pin(DigitalPin.P15, 0)
pins.digital_write_pin(DigitalPin.P16, 0)

def on_forever():
    if countA == 1:
        pins.digital_write_pin(DigitalPin.P14, 1)
        pins.digital_write_pin(DigitalPin.P16, 0)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P14, 0)
        pins.digital_write_pin(DigitalPin.P15, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P15, 0)
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.pause(500)
    elif countB == 1:
        pins.digital_write_pin(DigitalPin.P14, 1)
        pins.digital_write_pin(DigitalPin.P15, 1)
        pins.digital_write_pin(DigitalPin.P16, 0)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P14, 0)
        pins.digital_write_pin(DigitalPin.P15, 1)
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P14, 1)
        pins.digital_write_pin(DigitalPin.P15, 0)
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P14, 1)
        pins.digital_write_pin(DigitalPin.P15, 1)
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.pause(500)
    else:
        pins.digital_write_pin(DigitalPin.P14, 0)
        pins.digital_write_pin(DigitalPin.P15, 0)
        pins.digital_write_pin(DigitalPin.P16, 0)
basic.forever(on_forever)
