layeredimage bg pub:
    always:
        "pub"

init -2 python:
    Room(**{
        "name":"pub",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "hours": (19,3),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "eat_a_burger",
        "duration": 0,
        "hunger": 7,
        "money_cost": 25,
        "once_day": True,
        "game_conditions": {"min_hunger":0,"room":["pub"]},
        "display_name": "Eat a burger",
        "icon":"burger",
        "say": [
            "Crunch, crunch...\nCrunch...",
            ]
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
