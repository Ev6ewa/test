init -15 python:
    Activity(**{
        "name": "spank",
        "display_name": "Slap ass",
        "duration":0,
        "girls_conditions": {
            "ACTIVE":{
                "not_activity":["sleep"],
                }
            },
        "icon": "spank",
        "game_conditions": {"activity":"interact", "flag_female":0},
        "label": ["spank"],
        "once_day":"ACTIVE_GIRL"
        })

label spank:
    call expression game.active_girl.id+"_greet" from _call_expression_93
    if renpy.has_label(game.active_girl.id+"_spank_activity"):
        call expression game.active_girl.id+"_spank_activity" from _call_expression_94
    else:
        "I spank [game.active_girl.name] on the ass."
        if game.active_girl.sub >= 10:
            show expression game.active_girl.id+" blush"
            if game.active_girl.sub < 25:
                $ game.active_girl.sub += 1
            elif game.active_girl.sub < 50:
                $ game.active_girl.sub += randint(0,1)
            "She smiles and blush..."
        else:
            show expression game.active_girl.id+" angry"
            $ game.active_girl.love -= 1
            active_girl.say "What are you doing?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
