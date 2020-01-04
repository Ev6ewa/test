init -15 python:
    Activity(**{
        "name": "dance_with",
        "fun": 2,
        "grooming": 0,
        "duration": 1,
        "game_conditions": {
            "min_energy":2,
            "min_hunger":3,
            "min_grooming":3,
            "min_fun":1,
            "room":["nightclub","date_nightclub"],
            "activity":"interact",
            },
        "display_name": "Ask to dance",
        "icon":"dance",
        "label": ["dance_with"]
        })

label dance_with:
    $ game.active_girl.set_flag("interact",1,1,"+")
    call expression game.active_girl.id+"_greet" from _call_expression_21
    if renpy.has_label(game.active_girl.id+"_dance_with"):
        call expression game.active_girl.id+"_dance_with" from _call_expression_22
    else:
        show expression game.active_girl.id
        hero.say "[game.active_girl.name] do you want to dance?"
        if hero.charm >= 40 - game.active_girl.love() or game.get_flag_value("dateinprogress") == game.active_girl:
            active_girl.say "Why not."
            "I dance with [game.active_girl.name]."
            $ bonus = hero.fitness()/20
            if hero.check_skill("dance"):
                $ bonus += 2
            $ game.active_girl.love += bonus
            $ hero.fun += 2
            $ game.pass_time(needs=True)
        else:
            active_girl.say "Sorry, I don't feel like dancing"
            $ hero.activity.set_flag("canceled",True)
        $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
