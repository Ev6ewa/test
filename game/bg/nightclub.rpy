layeredimage bg nightclub:
    always:
        "nightclub"

init -2 python:
    Room(**{
        "name":"nightclub",
        "hours": (22,5),
        "display_name": "Nightclub",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "money_cost": 15,
        "required_item": "fancy clothes",
        "music": "music/Nihilore/Apricity.mp3",
        "outfit":"date"
        })

    Activity(**{
        "name": "party",
        "duration": 2,
        "fun": 6,
        "charm": 3,
        "money_cost": 50,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_grooming":4,"min_fun":2,"min_charm":10,"room":["nightclub"]},
        "display_name": "Party",
        "icon":"party",
        "once_day":True,
        "say": [
            "I take a couple of drinks with some friends.",
            "I have a few too many then go home.",
            "I wonder if I am an alcoholic...",
            "Let's party !!",
            "Woah that beer is fucking great."
            ]
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
