namespace SpriteKind {
    export const invinisble = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu)) {
        music.play(music.createSoundEffect(WaveShape.Square, 1, 4945, 70, 87, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        mySprite.setVelocity(mySprite.vx, -100 + mySprite.ay)
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setVelocity(0, 0)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu)) {
        music.play(music.createSoundEffect(WaveShape.Noise, 5000, 1, 255, 255, 200, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        if (moving_left) {
            mySprite4 = sprites.create(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                . . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, SpriteKind.Projectile)
            mySprite4.setPosition(mySprite.x, mySprite.y)
            mySprite4.setVelocity(-250 - mySprite.vx, 0)
            mySprite4.lifespan = 5000
        } else {
            mySprite3 = sprites.create(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                . . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, SpriteKind.Projectile)
            mySprite3.setPosition(mySprite.x, mySprite.y)
            mySprite3.setVelocity(250 + mySprite.vx, 0)
            mySprite3.lifespan = 5000
        }
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu)) {
        music.play(music.createSoundEffect(WaveShape.Square, 1, 4945, 70, 87, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        mySprite.setVelocity(-100 + mySprite.vx, mySprite.vy)
        moving_left = true
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Projectile, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Noise, 2269, 1734, 52, 65, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    mySprite2.startEffect(effects.fire)
    mySprite2.startEffect(effects.fire)
    sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    music.play(music.createSoundEffect(WaveShape.Noise, 5000, 0, 255, 255, 1000, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
    game.setGameOverScoringType(game.ScoringType.HighScore)
    game.gameOver(false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu)) {
        music.play(music.createSoundEffect(WaveShape.Square, 1, 4945, 70, 87, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        mySprite.setVelocity(100 + mySprite.vx, mySprite.vy)
        moving_left = false
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu)) {
        music.play(music.createSoundEffect(WaveShape.Square, 1, 4945, 70, 87, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        mySprite.setVelocity(mySprite.vx, 100 + mySprite.ay)
    }
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    commands = game.askForString("enter commands", 24)
    if (commands == "pause") {
        if (menu) {
            menu = false
        } else {
            menu = true
        }
    } else if (commands == "time") {
        info.startCountdown(60)
    } else if (commands == "time more") {
        info.startCountdown(120)
    } else if (commands == "harder") {
        hardness = 2000
    } else if (commands == "hardest") {
        hardness = 1000
    } else if (commands == "easter") {
        mySprite.sayText("how" + " did  " + " you" + " find" + "this" + text_list._pickRandom(), 2000, true)
    } else {
        mySprite.sayText("invalid command", 2000, true)
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    music.play(music.createSoundEffect(WaveShape.Noise, 2269, 1734, 101, 150, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    sprites.destroy(mySprite2)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    info.changeScoreBy(1)
})
let commands = ""
let mySprite2: Sprite = null
let mySprite3: Sprite = null
let mySprite4: Sprite = null
let moving_left = false
let menu = false
let hardness = 0
let text_list: string[] = []
let mySprite: Sprite = null
game.showLongText("how to play < > to move and ^ down arrow or wasd. objective destroy astroids. to summon a laser press A or space. to pause the game press munu and enter pause to toggle. note game will not actuly pause it will just make you not take damage. and not be able to move. ", DialogLayout.Full)
game.showLongText("the game will last forever. intil you press menu and enter time. if you want more time than 60 seconds enter time more. for twice as much time. if the game is to easy press menu and enter harder. if thats still not hard. enter harest. ", DialogLayout.Full)
console.logValue("input", 0)
mySprite = sprites.create(img`
    ....................................
    ....................................
    ...............222222...............
    .............222222d22222222........
    .442......2224442222d22222222222....
    .22442..22444222222222222222222222..
    ..422422242222266666662222222222222.
    ..4244222222222666666622222222222222
    ..444442222222222222222222222222222.
    .244442222222222222222222222222222..
    .444....2222222222222222222222222...
    ............2222222222222222222.....
    .............2222224444222222.......
    ...............444444...............
    ....................................
    ....................................
    `, SpriteKind.Player)
scene.cameraFollowSprite(mySprite)
mySprite.setStayInScreen(true)
mySprite.startEffect(effects.fire)
scene.setBackgroundImage(img`
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffff9ffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffff9ffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffff
    fff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9f
    ffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffff9fffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffff9fffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fff
    ffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffff9ffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    `)
scroller.scrollBackgroundWithCamera(scroller.CameraScrollMode.BothDirections)
text_list = [
" out!",
" out?",
" out.",
"out??",
"out!!"
]
let list2 = [
img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . c c c c . . 
    . c c c c c . c c c c c f c c . 
    c c a c c c c c 8 f f c f f c c 
    c a f a a c c a f f c a a f f c 
    c a 8 f a a c a c c c a a a a c 
    c b c f a a a a a c c c c c c c 
    c b b a a c f 8 a c c c 8 c c c 
    . c b b a b c f a a a 8 8 c c . 
    . . . . a a b b b a a 8 a c . . 
    . . . . c b c a a c c b . . . . 
    . . . . b b c c a b b a . . . . 
    . . . . b b a b a 6 a . . . . . 
    . . . . c b b b 6 6 c . . . . . 
    . . . . . c a 6 6 b c . . . . . 
    . . . . . . . c c c . . . . . . 
    `,
img`
    . . . . . . . . . c c 8 . . . . 
    . . . . . . 8 c c c f 8 c c . . 
    . . . c c 8 8 f c a f f f c c . 
    . . c c c f f f c a a f f c c c 
    8 c c c f f f f c c a a c 8 c c 
    c c c b f f f 8 a c c a a a c c 
    c a a b b 8 a b c c c c c c c c 
    a f c a a b b a c c c c c f f c 
    a 8 f c a a c c a c a c f f f c 
    c a 8 a a c c c c a a f f f 8 a 
    . a c a a c f f a a b 8 f f c a 
    . . c c b a f f f a b b c c 6 c 
    . . . c b b a f f 6 6 a b 6 c . 
    . . . c c b b b 6 6 a c c c c . 
    . . . . c c a b b c c c . . . . 
    . . . . . c c c c c c . . . . . 
    `,
img`
    . . . . . . . c c c a c . . . . 
    . . c c b b b a c a a a c . . . 
    . c c a b a c b a a a b c c . . 
    . c a b c f f f b a b b b a . . 
    . c a c f f f 8 a b b b b b a . 
    . c a 8 f f 8 c a b b b b b a . 
    c c c a c c c c a b c f a b c c 
    c c a a a c c c a c f f c b b a 
    c c a b 6 a c c a f f c c b b a 
    c a b c 8 6 c c a a a b b c b c 
    c a c f f a c c a f a c c c b . 
    c a 8 f c c b a f f c b c c c . 
    . c b c c c c b f c a b b a c . 
    . . a b b b b b b b b b b b c . 
    . . . c c c c b b b b b c c . . 
    . . . . . . . . c b b c . . . . 
    `,
img`
    . . . . . . . . c c c c . . . . 
    . . . . c c c c c c c c c . . . 
    . . . c f c c a a a a c a c . . 
    . . c c f f f f a a a c a a c . 
    . . c c a f f c a a f f f a a c 
    . . c c a a a a b c f f f a a c 
    . c c c c a c c b a f c a a c c 
    c a f f c c c a b b 6 b b b c c 
    c a f f f f c c c 6 b b b a a c 
    c a a c f f c a 6 6 b b b a a c 
    c c b a a a a b 6 b b a b b a . 
    . c c b b b b b b b a c c b a . 
    . . c c c b c c c b a a b c . . 
    . . . . c b a c c b b b c . . . 
    . . . . c b b a a 6 b c . . . . 
    . . . . . . b 6 6 c c . . . . . 
    `,
img`
    . . . . . . c c c . . . . . . . 
    . . . . . a a a c c c . . . . . 
    . . . c a c f a a a a c . . . . 
    . . c a c f f f a f f a c . . . 
    . c c a c c f a a c f f a c . . 
    . a b a a c 6 a a c c f a c c c 
    . a b b b 6 a b b a a c a f f c 
    . . a b b a f f b b a a c f f c 
    c . a a a c c f c b a a c f a c 
    c c a a a c c a a a b b a c a c 
    a c a b b a a 6 a b b 6 b b c . 
    b a c b b b 6 b c . c c a c . . 
    b a c c a b b a c . . . . . . . 
    b b a c a b a a . . . . . . . . 
    a b 6 b b a c . . . . . . . . . 
    . a a b c . . . . . . . . . . . 
    `,
img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . c b a c . . . . . . 
    . . . . c c b c f a c . . . . . 
    . . . . a f b b b a c . . . . . 
    . . . . a f f b a f c c . . . . 
    . . . . c b b a f f c . . . . . 
    . . . . . b b a f a . . . . . . 
    . . . . . . c b b . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,
img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . c c . . . . . . . . 
    . . . . c a f b c . . . . . . . 
    . . . . b f f b c c . . . . . . 
    . . . a a f b a b a c . . . . . 
    . . . c a c b b f f b . . . . . 
    . . . . b f f b f a b . . . . . 
    . . . . a f f b b b a . . . . . 
    . . . . . a b b c c . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `,
img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . c c c . . . . . . 
    . . . . . . a b a a . . . . . . 
    . . . . . c b a f c a c . . . . 
    . . . . c b b b f f a c c . . . 
    . . . . b b f a b b a a c . . . 
    . . . . c b f f b a f c a . . . 
    . . . . . c a a c b b a . . . . 
    . . . . . . c c c c . . . . . . 
    . . . . . . . c . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `
]
info.setScore(0)
hardness = 5000
game.onUpdate(function () {
    if (menu) {
        mySprite.setVelocity(0, 0)
        mySprite.setKind(SpriteKind.invinisble)
        mySprite.sayText("game_paused", 100, false)
    } else {
        mySprite.setKind(SpriteKind.Player)
    }
})
game.onUpdate(function () {
    if (mySprite.vx > 200) {
        mySprite.vx = 1000
    }
    if (mySprite.vy > 200) {
        mySprite.vy = 1000
    }
})
game.onUpdateInterval(hardness, function () {
    if (Math.percentChance(50)) {
        mySprite2 = sprites.create(list2._pickRandom(), SpriteKind.Enemy)
        mySprite2.setVelocity(-5, randint(-5, 5))
        mySprite2.setPosition(mySprite.x + randint(-100, 100), mySprite.y + randint(-60, 60))
        mySprite2.lifespan = 10000
    } else if (Math.percentChance(50)) {
        mySprite2 = sprites.create(list2._pickRandom(), SpriteKind.Enemy)
        mySprite2.lifespan = 10000
        if (Math.percentChance(50)) {
            mySprite2.setVelocity(-15, randint(-5, 5))
        } else {
            mySprite2.setVelocity(15, randint(-5, 5))
        }
        mySprite2.setPosition(mySprite.x + 100, mySprite.y + randint(10, 60))
    } else if (Math.percentChance(50)) {
        mySprite2 = sprites.create(list2._pickRandom(), SpriteKind.Enemy)
        mySprite2.lifespan = 10000
        mySprite2.setVelocity(-35, randint(-5, 5))
        mySprite2.setPosition(mySprite.x + 100, mySprite.y + randint(10, 60))
        if (Math.percentChance(50)) {
            mySprite2.setVelocity(-15, randint(-5, 5))
        } else {
            mySprite2.setVelocity(15, randint(-5, 5))
        }
    } else if (Math.percentChance(50)) {
        mySprite2 = sprites.create(list2._pickRandom(), SpriteKind.Enemy)
        mySprite2.lifespan = 10000
        mySprite2.setVelocity(-65, 0)
        mySprite2.setPosition(mySprite.x + 100, mySprite.y + randint(10, 60))
        if (Math.percentChance(50)) {
            mySprite2.setVelocity(-15, randint(-5, 5))
        } else {
            mySprite2.setVelocity(15, randint(-5, 5))
        }
    } else {
        mySprite2 = sprites.create(list2._pickRandom(), SpriteKind.Enemy)
        mySprite2.lifespan = 10000
        mySprite2.setVelocity(-125, 0)
        mySprite2.setPosition(mySprite.x + 100, mySprite.y + randint(10, 60))
        if (Math.percentChance(50)) {
            mySprite2.setVelocity(-15, randint(-5, 5))
        } else {
            mySprite2.setVelocity(15, 0)
        }
    }
})
game.onUpdateInterval(100, function () {
    if (characterAnimations.matchesRule(mySprite, characterAnimations.rule(Predicate.NotMoving))) {
        effects.clearParticles(mySprite)
    } else {
        mySprite.startEffect(effects.fire)
    }
})
