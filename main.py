def on_button_pressed_a():
    basic.show_string(kitronik_halo_hd.read_time(), 70)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Time in ABQ is...", 70)
    basic.show_number(kitronik_halo_hd.read_time_parameter(TimeParameter.HOURS) - 8)
    basic.show_string("o'clock.", 70)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if kitronik_halo_hd.read_time_parameter(TimeParameter.HOURS) < 14:
        haloDisplay.show_color(kitronik_halo_hd.colors(ZipLedColors.RED))
        haloDisplay.show()
        basic.show_icon(IconNames.ASLEEP)
        soundExpression.yawn.play()
        basic.pause(5000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        haloDisplay.show_color(kitronik_halo_hd.colors(ZipLedColors.BLACK))
    elif kitronik_halo_hd.read_time_parameter(TimeParameter.HOURS) < 16:
        haloDisplay.show_color(kitronik_halo_hd.colors(ZipLedColors.YELLOW))
        haloDisplay.show()
        basic.show_icon(IconNames.ASLEEP)
        soundExpression.yawn.play()
        basic.pause(5000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        haloDisplay.show_color(kitronik_halo_hd.colors(ZipLedColors.BLACK))
    else:
        haloDisplay.show_color(kitronik_halo_hd.colors(ZipLedColors.GREEN))
        haloDisplay.show()
        basic.show_icon(IconNames.HAPPY)
        soundExpression.hello.play()
        basic.pause(5000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        haloDisplay.show_color(kitronik_halo_hd.colors(ZipLedColors.BLACK))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    haloDisplay.show_bar_graph(kitronik_halo_hd.read_time_parameter(TimeParameter.HOURS),
        16)
    basic.pause(5000)
    haloDisplay.show_color(kitronik_halo_hd.colors(ZipLedColors.BLACK))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

haloDisplay: kitronik_halo_hd.ZIPHaloHd = None
haloDisplay = kitronik_halo_hd.create_zip_halo_display(60)
haloDisplay.set_brightness(20)
kitronik_halo_hd.set_time(13, 58, 0)