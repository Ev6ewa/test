init -15 python:
    Activity(**{
        "name": "talk",
        "display_name": "talk",
        "girls_conditions": {
            "ACTIVE":{
                "not_activity":["sleep"]
                }
            },
        "icon": "talk",
        "game_conditions": {"activity":"interact"},
        "label": ["talk"],
        })

label talk:
    call expression game.active_girl.id+"_greet" from _call_expression_25
    python:
        d = game.active_girl.get_flag_value("daily_interact")



        if hero.charm >= d*10 - game.active_girl.love() or game.get_flag_value("dateinprogress") == game.active_girl:
            game.active_girl.set_flag("daily_interact",1,1, "+")
            subjects = game.active_girl.get_talk_subjects()
            if subjects:
                renpy.show(game.active_girl.id)
                result = renpy.call_screen("select", choices=subjects, title = "subjects")
                game.active_girl.set_flag(result+"_talk_used",duration=1)
                renpy.hide((game.active_girl.id))
                if result != "None":
                    renpy.call_in_new_context(game.active_girl.id+"_talk_"+result)
                else:
                    hero.activity.set_flag("canceled")
            else:
                renpy.say("","We have nothing to talk about.")
                hero.activity.set_flag("canceled")
        else:
            renpy.show(game.active_girl.id)
            active_girl.say("Sorry, I don't have time right now.")
            hero.activity.set_flag("canceled")
            renpy.hide((game.active_girl.id))
        game.active_girl.set_flag("interact",1,1,"+")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
