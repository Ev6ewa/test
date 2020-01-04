init -15 python:
    Activity(**{
        "name": "cinema_with",
        "fun": 2,
        "grooming": 0,
        "duration": 2,
        "game_conditions": {
            "min_energy":2,
            "min_hunger":3,
            "min_grooming":3,
            "min_fun":1,
            "activity":"interact",
            "room":["cinema"]
            },
        "icon":"cinema",
        "display_name": "Invite to movie",
        "label": ["cinema_with"]
        })

label cinema_with:
    $ game.active_girl.set_flag("interact",1,1,"+")
    call expression game.active_girl.id+"_greet" from _call_expression_35
    if renpy.has_label(game.active_girl.id+"_cinema_with"):
        call expression game.active_girl.id+"_cinema_with" from _call_expression_36
    else:
        show expression game.active_girl.id
        hero.say "[game.active_girl.name] do you want to go watch a movie together?"
        if hero.charm >= 40 - game.active_girl.love():
            active_girl.say "Why not."
            "I watch a movie with [game.active_girl.name]."
            $ game.active_girl.love += hero.charm()/20
            $ hero.fun += 2
        else:
            active_girl.say "Sorry, I don't feel like it"
            $ hero.activity.set_flag("canceled",True)
        hide expression game.active_girl.id
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
