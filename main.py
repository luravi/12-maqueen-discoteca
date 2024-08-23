def on_forever():
    music.play(music.string_playable("G B A G C5 B A B ", 120),
        music.PlaybackMode.UNTIL_DONE)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    basic.pause(2000)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)
basic.forever(on_forever)
