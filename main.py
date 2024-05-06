@namespace
class SpriteKind:
    invinisble = SpriteKind.create()

def on_up_pressed():
    if not (menu):
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                1,
                4945,
                70,
                87,
                100,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        mySprite.set_velocity(mySprite.vx, -100 + mySprite.ay)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    mySprite.set_velocity(0, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global mySprite4, mySprite3
    if not (menu):
        music.play(music.create_sound_effect(WaveShape.NOISE,
                5000,
                1,
                255,
                255,
                200,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        if moving_left:
            mySprite4 = sprites.create(img("""
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
                """),
                SpriteKind.projectile)
            mySprite4.set_position(mySprite.x, mySprite.y)
            mySprite4.set_velocity(-250, 0)
            mySprite4.lifespan = 5000
        else:
            mySprite3 = sprites.create(img("""
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
                """),
                SpriteKind.projectile)
            mySprite3.set_position(mySprite.x, mySprite.y)
            mySprite3.set_velocity(250, 0)
            mySprite3.lifespan = 5000
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global moving_left
    if not (menu):
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                1,
                4945,
                70,
                87,
                100,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        mySprite.set_velocity(-100 + mySprite.vx, mySprite.vy)
        moving_left = True
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap(sprite, otherSprite):
    music.play(music.create_sound_effect(WaveShape.NOISE,
            2269,
            1734,
            52,
            65,
            100,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    mySprite2.start_effect(effects.fire)
    mySprite2.start_effect(effects.fire)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.projectile, on_on_overlap)

def on_right_pressed():
    global moving_left
    if not (menu):
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                1,
                4945,
                70,
                87,
                100,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        mySprite.set_velocity(100 + mySprite.vx, mySprite.vy)
        moving_left = False
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    if not (menu):
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                1,
                4945,
                70,
                87,
                100,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        mySprite.set_velocity(mySprite.vx, 100 + mySprite.ay)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_menu_pressed():
    global commands, menu, hardness
    commands = game.ask_for_string("enter commands", 24)
    if commands == "pause":
        if menu:
            menu = False
        else:
            menu = True
    else:
        if commands == "time":
            info.start_countdown(60)
        else:
            if commands == "time more":
                info.start_countdown(120)
            elif commands == "harder":
                hardness = 2000
            elif commands == "hardest":
                hardness = 1000
            elif commands == "easter":
                mySprite.say_text("how" + " did  " + " you" + " find" + "this" + text_list._pick_random(),
                    2000,
                    True)
            else:
                mySprite.say_text("invalid command", 2000, True)
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    music.play(music.create_sound_effect(WaveShape.NOISE,
            2269,
            1734,
            101,
            150,
            100,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    sprites.destroy(mySprite2)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    music.play(music.create_sound_effect(WaveShape.NOISE,
            5000,
            0,
            255,
            255,
            1000,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
    game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

commands = ""
mySprite2: Sprite = None
mySprite3: Sprite = None
mySprite4: Sprite = None
moving_left = False
menu = False
hardness = 0
text_list: List[str] = []
mySprite: Sprite = None
game.show_long_text("how to play < > to move and ^ down arrow or wasd. objective destroy astroids. to summon a laser press A or space. to pause the game press munu and enter pause to toggle. note game will not actuly pause it will just make you not take damage. and not be able to move. ",
    DialogLayout.FULL)
game.show_long_text("the game will last forever. intil you press menu and enter time. if you want more time than 60 seconds enter time more. for twice as much time. if the game is to easy press menu and enter harder. if thats still not hard. enter harest. ",
    DialogLayout.FULL)
console.log_value("input", 0)
mySprite = sprites.create(img("""
        ....................f...............
            ....................................
            ...............111111...............
            222..........222222d21111111........
            24422.....2221112222d21111111111....
            .22442..22114222222222222222222111..
            ..422422242222266666662222222222211.
            ..424422222222266666662222222222221.
            ..444142222222222222222222222222221.
            .244112222222222222222222222222222..
            244412....22222222222222222222222...
            22222.......2222222222222222222.....
            .............2222222114222222.......
            ...............2222114..............
            ...............444444...............
            ....................................
    """),
    SpriteKind.player)
scene.camera_follow_sprite(mySprite)
mySprite.set_stay_in_screen(True)
mySprite.start_effect(effects.fire)
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ff
        ffff9fffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9ffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffff9ffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffff9ffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffff9ffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffff
        ffffff9ffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffff9ffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffff
        fffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffff9fffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffff
        9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffff9ffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffff
        fff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9f
        ffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffff9fffffffffffff9fffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffff9fffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffff
        ffffffff9fffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fff
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
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9ffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fff
        ffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffff
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
"""))
scroller.scroll_background_with_camera(scroller.CameraScrollMode.BOTH_DIRECTIONS)
text_list = [" out!", " out?", " out.", "out??", "out!!"]
list2 = [img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """),
    img("""
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
    """)]
info.set_score(0)
hardness = 5000

def on_on_update():
    if menu:
        mySprite.set_velocity(0, 0)
        mySprite.set_kind(SpriteKind.invinisble)
        mySprite.say_text("game_paused", 100, False)
    else:
        mySprite.set_kind(SpriteKind.player)
game.on_update(on_on_update)

def on_on_update2():
    if mySprite.vx > 200:
        mySprite.vx = 1000
    if mySprite.vy > 200:
        mySprite.vy = 1000
game.on_update(on_on_update2)

def on_on_update3():
    pass
game.on_update(on_on_update3)

def on_update_interval():
    global mySprite2
    if Math.percent_chance(50):
        mySprite2 = sprites.create(list2._pick_random(), SpriteKind.enemy)
        mySprite2.set_velocity(-5, randint(-5, 5))
        mySprite2.set_position(mySprite.x + randint(-100, 100),
            mySprite.y + randint(-60, 60))
        mySprite2.lifespan = 10000
    else:
        if Math.percent_chance(50):
            mySprite2 = sprites.create(list2._pick_random(), SpriteKind.enemy)
            mySprite2.lifespan = 10000
            if Math.percent_chance(50):
                mySprite2.set_velocity(-15, randint(-5, 5))
            else:
                mySprite2.set_velocity(15, randint(-5, 5))
            mySprite2.set_position(mySprite.x + 100, mySprite.y + randint(10, 60))
        else:
            if Math.percent_chance(50):
                mySprite2 = sprites.create(list2._pick_random(), SpriteKind.enemy)
                mySprite2.lifespan = 10000
                mySprite2.set_velocity(-35, randint(-5, 5))
                mySprite2.set_position(mySprite.x + 100, mySprite.y + randint(10, 60))
                if Math.percent_chance(50):
                    mySprite2.set_velocity(-15, randint(-5, 5))
                else:
                    mySprite2.set_velocity(15, randint(-5, 5))
            else:
                if Math.percent_chance(50):
                    mySprite2 = sprites.create(list2._pick_random(), SpriteKind.enemy)
                    mySprite2.lifespan = 10000
                    mySprite2.set_velocity(-65, 0)
                    mySprite2.set_position(mySprite.x + 100, mySprite.y + randint(10, 60))
                    if Math.percent_chance(50):
                        mySprite2.set_velocity(-15, randint(-5, 5))
                    else:
                        mySprite2.set_velocity(15, randint(-5, 5))
                else:
                    mySprite2 = sprites.create(list2._pick_random(), SpriteKind.enemy)
                    mySprite2.lifespan = 10000
                    mySprite2.set_velocity(-125, 0)
                    mySprite2.set_position(mySprite.x + 100, mySprite.y + randint(10, 60))
                    if Math.percent_chance(50):
                        mySprite2.set_velocity(-15, randint(-5, 5))
                    else:
                        mySprite2.set_velocity(15, 0)
game.on_update_interval(hardness, on_update_interval)

def on_update_interval2():
    if characterAnimations.matches_rule(mySprite, characterAnimations.rule(Predicate.NOT_MOVING)):
        effects.clear_particles(mySprite)
    else:
        mySprite.start_effect(effects.fire)
game.on_update_interval(100, on_update_interval2)
