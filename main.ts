input.onButtonPressed(Button.A, function () {
    basic.showString(kitronik_halo_hd.readTime(), 70)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Time in ABQ is...", 70)
basic.showNumber(kitronik_halo_hd.readTimeParameter(TimeParameter.Hours) - 8)
    basic.showString("o'clock.", 70)
})
input.onButtonPressed(Button.B, function () {
    if (kitronik_halo_hd.readTimeParameter(TimeParameter.Hours) < 14) {
        haloDisplay.showColor(kitronik_halo_hd.colors(ZipLedColors.Red))
        haloDisplay.show()
        basic.showIcon(IconNames.Asleep)
        soundExpression.yawn.play()
        basic.pause(5000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        haloDisplay.showColor(kitronik_halo_hd.colors(ZipLedColors.Black))
    } else if (kitronik_halo_hd.readTimeParameter(TimeParameter.Hours) < 16) {
        haloDisplay.showColor(kitronik_halo_hd.colors(ZipLedColors.Yellow))
        haloDisplay.show()
        basic.showIcon(IconNames.Asleep)
        soundExpression.yawn.play()
        basic.pause(5000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        haloDisplay.showColor(kitronik_halo_hd.colors(ZipLedColors.Black))
    } else {
        haloDisplay.showColor(kitronik_halo_hd.colors(ZipLedColors.Green))
        haloDisplay.show()
        basic.showIcon(IconNames.Happy)
        soundExpression.hello.play()
        basic.pause(5000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        haloDisplay.showColor(kitronik_halo_hd.colors(ZipLedColors.Black))
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    haloDisplay.showBarGraph(kitronik_halo_hd.readTimeParameter(TimeParameter.Hours), 16)
    basic.pause(5000)
    haloDisplay.showColor(kitronik_halo_hd.colors(ZipLedColors.Black))
})
let haloDisplay: kitronik_halo_hd.ZIPHaloHd = null
haloDisplay = kitronik_halo_hd.createZIPHaloDisplay(60)
haloDisplay.setBrightness(20)
kitronik_halo_hd.setTime(17, 6, 0)
