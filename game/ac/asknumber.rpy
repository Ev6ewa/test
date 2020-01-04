init -15 python:
    Activity(**{
        "name": "asknumber",
        "display_name": "Ask number",
        "duration": 0,
        "label": ["ask_number"],
        "game_conditions": {"activity":"interact"},
        "girls_conditions": {
            "ACTIVE":{
                "contact":False,
                "not_activity":["sleep"]
                }
            },
        "icon": "number",
        "once_day": "ACTIVE_GIRL"
        })

label ask_number:
    call expression game.active_girl.id+"_greet" from _call_expression_17
    show expression game.active_girl.id
    hero.say "Can I have your number ?"
    if renpy.has_label(game.active_girl.id+"_ask_number"):
        call expression game.active_girl.id+"_ask_number"
    elif not hero.charm >= 20 - game.active_girl.love():
        active_girl.say "I don't think so."
    else:
        $ hero.smartphone_contacts.append(game.active_girl.id)
        active_girl.say "Sure."
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
