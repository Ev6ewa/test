layeredimage bg waterpark:
    always:
        "waterpark"

init -2 python:
    Room(**{
        "name":"waterpark",
        "hours":(10,20),
        "display_name": "Waterpark",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "required_item": "swimsuit",
        "open_seasons":"01",
        "money_cost":10,
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"swimsuit"
        })

    Activity(**{
        "name":"swim_waterpark",
        "fun": 1,
        "fitness": 1,
        "duration": 2,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_grooming":3,"min_fun":3,"room":["waterpark"]},
        "display_name": "Swim",
        "icon":"swim",
        "say":[
            "I go for a swim in the pool...",
            "Swimming is good for what I have."
            ]
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
