init -15 python:
    Activity(**{
        "name": "askbirthday",
        "display_name": "Ask birthday",
        "label": ["ask_birthday"],
        "duration": 0,
        "game_conditions": {"activity":"interact"},
        "girls_conditions": {
            "ACTIVE":{
                "min_love":5,
                "not_activity":["sleep"],
                "flag_birthdayknown":False
                }
            },
        "once_day": "ACTIVE_GIRL",
        "icon": "birthday",
        })

label ask_birthday:
    call expression game.active_girl.id+"_greet" from _call_expression_28
    show expression game.active_girl.id
    hero.say "Hey [game.active_girl.name], when is your birthday ?"
    if not hero.charm >= 20 - game.active_girl.love():
        active_girl.say "I don't think that's any of your business"
    else:
        active_girl.say "It's on the [game.active_girl.birthday[1]] of [game.active_girl.birthday[0]]."
        active_girl.say "Are you planning on getting me a gift ?"
        hero.say "Maybe..."
        $ game.active_girl.set_flag("birthdayknown")
        $ game.active_girl.love += 1
    hide expression game.active_girl.id
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
