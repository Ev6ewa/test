init -15 python:
    Activity(**{
        "name": "wait",
        "duration": 1,
        "game_conditions": {
                "min_energy":0,
                "min_hunger":0,
                "min_grooming":0,
                "min_fun":0
                },
        "icon":"wait",
        "display_name": "Wait"
        })

    Event(**{
        "name":"wait_bored",
        "fun": -1,
        "quit": False,
        "label": ["wait_bored"],
        "game_conditions": {
                "activity":"wait",
                "chances":5,
                },
        "quit": False,
        })

label wait_bored:
    "I am bored..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
