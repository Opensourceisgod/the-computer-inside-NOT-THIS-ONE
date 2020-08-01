function Clear () {
    startup_clear = 1
    basic.clearScreen()
}
// COMPASS WHEN A IS CLICKED
input.onButtonPressed(Button.A, function () {
    Clear()
    degrees = input.compassHeading()
    if (degrees < 22.5 || degrees > 337.5) {
        basic.showString("N")
    } else if (degrees < 67.5) {
        basic.showString("NE")
    } else if (degrees < 112.5) {
        basic.showString("E")
    } else if (degrees < 157.5) {
        basic.showString("SE")
    } else if (degrees < 202.5) {
        basic.showString("S")
    } else if (degrees < 247.5) {
        basic.showString("SW")
    } else if (degrees < 292.5) {
        basic.showString("W")
    } else {
        basic.showString("NW")
    }
    basic.pause(200)
    basic.clearScreen()
})
function Saveing_information_here_because_I_can_ () {
	
}
// TEST FEATURE
input.onGesture(Gesture.ScreenDown, function () {
    Startup()
})
// FUNCTION just to set basic items
function _set () {
    cookieclicker = 0
    C = images.createImage(`
        . . . . .
        # . # # #
        . . # . .
        . . # . .
        . . # # #
        `)
    _0 = images.createImage(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    _1 = images.createImage(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        `)
    _2 = images.createImage(`
        # # . . .
        # . . . .
        . . . . .
        . . . . #
        . . . # #
        `)
    _3 = images.createImage(`
        # # # . .
        # # . . .
        # . . . #
        . . . # #
        . . # # #
        `)
    _4 = images.createImage(`
        # # # # .
        # # # . #
        # # . # #
        # . # # #
        . # # # #
        `)
    _5 = images.createImage(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
}
pins.onPulsed(DigitalPin.P4, PulseValue.High, function () {
    pins.digitalWritePin(DigitalPin.P0, pins.analogReadPin(AnalogPin.P0))
    pins.analogWritePin(AnalogPin.P0, 1023)
})
// FUNCTION - IMAGES/Startup
function Startup () {
    if (startup_clear == 0) {
        _1.showImage(0)
    }
    if (startup_clear == 0) {
        _2.showImage(0)
    }
    if (startup_clear == 0) {
        _3.showImage(0)
    }
    if (startup_clear == 0) {
        _4.showImage(0)
    }
    if (startup_clear == 0) {
        _5.showImage(0)
    }
    if (startup_clear == 0) {
        _4.showImage(0)
    }
    if (startup_clear == 0) {
        _3.showImage(0)
    }
    if (startup_clear == 0) {
        _2.showImage(0)
    }
    if (startup_clear == 0) {
        _1.showImage(0)
    }
    if (startup_clear == 0) {
        _0.showImage(0)
    }
}
input.onButtonPressed(Button.AB, function () {
    Clear()
    led.stopAnimation()
    cookieclicker += 1
    led.stopAnimation()
    basic.showNumber(cookieclicker)
    led.stopAnimation()
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    Clear()
    for (let index = 0; index < 1; index++) {
        basic.showString("" + (input.temperature()))
        C.showImage(0)
        basic.showString("")
    }
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    Clear()
    led.stopAnimation()
    basic.showNumber(randint(1, 6))
    basic.pause(500)
    led.stopAnimation()
    basic.clearScreen()
    led.stopAnimation()
})
let _5: Image = null
let _4: Image = null
let _3: Image = null
let _2: Image = null
let _1: Image = null
let _0: Image = null
let C: Image = null
let cookieclicker = 0
let degrees = 0
let startup_clear = 0
// USING FUNCTIONS
_set()
Startup()
// COOKIE CLICKER ON A+B
basic.forever(function () {
    if (cookieclicker == 9) {
        cookieclicker = -1
    }
})
