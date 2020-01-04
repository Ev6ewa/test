layeredimage bg date_beach:
    if game.hour >= 20 or game.hour <= 5:
        "beach_night"
    else:
        "beach_day"


init -2 python:
    Room(**{
        "name":"date_beach",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Beach",
        "hours": (14,17),
        "open_seasons":"1",
        "required_item": ["swimsuit", "bigVehicule"],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"swimsuit"
        })

    Date(
        "beach",
        display_name="beach",
        game_conditions={"valid_room":"date_beach"},
        clothes = "swimsuit",
        love_gain = 3,
        )

    Activity(**{
        "name": "date_icecream_beach",
        "duration": 1,
        "money_cost":10,
        "hunger":1,
        "icon": "icecream",
        "game_conditions":{"room":["date_beach"]},
        "display_name": "Have an ice cream",
        "label": ["date_icecream_beach"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_suntan",
        "duration": 1,
        "money_cost":50,
        "energy":2,
        "icon": "masturbate",
        "game_conditions":{"room":["date_beach"]},
        "display_name": "Apply sunscreen on her",
        "label": ["date_suntan"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_swimmingrace_beach",
        "duration": 1,
        "energy":-2,
        "icon":"swim",
        "game_conditions":{"room":["date_beach"]},
        "display_name": "Race her in the sea",
        "label": ["date_swimmingrace_beach"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_play_beach",
        "duration": 1,
        "icon": False,
        "game_conditions":{"room":["date_beach"]},
        "display_name": "Play in the sea",
        "label": ["date_play_beach"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_volley_beach",
        "duration": 1,
        "icon": False,
        "game_conditions":{"room":["date_beach"], "min_fitness": 50},
        "display_name": "Play some beach volley",
        "label": ["date_volley_beach"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_castle_beach",
        "duration": 1,
        "icon": False,
        "game_conditions":{"min_charm": 50, "room":["date_beach"]},
        "display_name": "Make a sand castle",
        "label": ["date_castle_beach"],
        "once_day":True,
        })

label date_castle_beach:
    show expression game.active_girl.id
    "I make a sand castle with [game.active_girl.name]."
    call expression game.active_girl.get_chat() from _call_expression_64
    if "playful" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_volley_beach:
    show expression game.active_girl.id
    "I play some beach volley with [game.active_girl.name]."
    $ game.set_flag("datescore",5,1,"+")
    call expression game.active_girl.get_chat() from _call_expression_65
    if "playful" in game.active_girl.traits or "sportsy"  in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_play_beach:
    show expression game.active_girl.id
    "I play [game.active_girl.name] in the sea."
    $ game.set_flag("datescore",5,1,"+")
    call expression game.active_girl.get_chat() from _call_expression_90
    if "playful" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_swimmingrace_beach:
    show expression game.active_girl.id
    "I race [game.active_girl.name] in the sea."
    $ game.set_flag("datescore",5,1,"+")
    call expression game.active_girl.get_chat() from _call_expression_92
    if "sportsy" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_suntan:
    show expression game.active_girl.id
    "I put sunscreen lotion on [game.active_girl.name]."
    $ game.set_flag("datescore",5,1,"+")
    call expression game.active_girl.get_chat() from _call_expression_132
    if "princess" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_icecream_beach:
    show expression game.active_girl.id
    "We eat an ice cream together."
    call expression game.active_girl.get_chat() from _call_expression_133
    if "gourmand" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_beach:
    show expression game.active_girl.id
    "We go to the beach."
    if "sport_car" in hero.inventory:
        $ game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
