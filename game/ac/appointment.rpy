init -15 python:
    Activity(**{
        "name":"go_on_date",
        "duration":0,
        "game_conditions": {
            "min_energy":1,
            "min_hunger":1,
            "min_grooming":1,
            "min_fun":1,
            "validappointment":True,
            "flag_dateinprogress":False
            },
        "icon":"date",
        "display_name": "Go on a date",
        "label": ["go_on_date"]
        })

label go_on_date:
    python:
        hero.activity = None
        if game.hour in [14,15,16]:
            h = 14
        elif game.hour in [20,21,22]:
            h = 20
        choices = [g.replace("_"," ").title() for g in hero.appointments[game.days_played][h]]
        if len(choices) > 1:
            result = renpy.call_screen("select",choices,"with whom ?",cap=False)
        else:
            result = choices[0]
    if result != "None":
        if result.lower() in GIRLS:
            $ game.active_girl = GIRLS[result.lower()]
            "I leave for my date with [game.active_girl.name]."
            if game.days_played in hero.appointments.keys() and h in hero.appointments[game.days_played].keys() and game.active_girl.id in hero.appointments[game.days_played][h]:
                $ hero.appointments[game.days_played][h].remove(game.active_girl.id)
            call date from _call_date
        elif renpy.has_label(result.lower().replace(" ","_")):
            call expression result.lower().replace(" ","_") from _call_expression_88
    else:
        $ hero.activity.set_flag("canceled",True)
    $ game.pass_time(0)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
