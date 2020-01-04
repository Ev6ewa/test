layeredimage bg date_waterpark:
    always:
        "waterpark"

init -2 python:
    Room(**{
        "name":"date_waterpark",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Waterpark",
        "hours": (14,17),
        "open_seasons":"01",
        "money_cost": 10,
        "required_item": "swimsuit",
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"swimsuit"
        })

    Date(
        "waterpark",
        display_name="water park",
        money_cost=100,
        game_conditions={"valid_room":"date_waterpark"},
        clothes = "swimsuit",
        love_gain = 2,
        )

    Activity(**{
        "name": "date_try_the_waterslide",
        "duration": 1,
        "icon": "waterslide",
        "display_name": "Waterslide",
        "game_conditions": {"room":["date_waterpark"]},
        "fun": 2,
        "label": ["date_try_the_waterslide"],
        "once_day": True
        })


    Activity(**{
        "name": "date_icecream",
        "duration": 1,
        "money_cost":10,
        "hunger":1,
        "icon": "icecream",
        "game_conditions":{"room":["date_waterpark"]},
        "display_name": "Have an ice cream",
        "label": ["date_icecream"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_spa",
        "duration": 1,
        "money_cost":50,
        "energy":2,
        "icon": "spa",
        "game_conditions":{"room":["date_waterpark"]},
        "display_name": "Go to the spa",
        "label": ["date_spa"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_swimmingrace",
        "duration": 1,
        "energy":-2,
        "icon":"swim",
        "game_conditions":{"room":["date_waterpark"]},
        "display_name": "Race her in the pool",
        "label": ["date_swimmingrace"],
        "once_day":True,
        })

label date_swimmingrace:
    show expression game.active_girl.id
    "I race [game.active_girl.name] in the pool."
    $ game.set_flag("datescore",5,1,"+")
    call expression game.active_girl.get_chat() from _call_expression_2
    if "sportsy" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_spa:
    show expression game.active_girl.id
    "We have a relaxing time in the spa."
    $ game.set_flag("datescore",5,1,"+")
    call expression game.active_girl.get_chat() from _call_expression_3
    if "princess" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_icecream:
    show expression game.active_girl.id
    "We eat an ice cream together."
    call expression game.active_girl.get_chat() from _call_expression_31
    if "gourmand" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_try_the_waterslide:
    show expression game.active_girl.id
    "We go to the waterslide."
    if renpy.has_label(game.active_girl.id+"_date_try_the_waterslide"):
        call expression game.active_girl.id+"_date_try_the_waterslide" from _call_expression_26
    else:
        if not game.active_girl.has_trait("playful"):
            active_girl.say "Why not..."
            $ game.set_flag("datescore",5,1,"+")
        else:
            active_girl.say "Yes, sure."
            $ game.set_flag("datescore",10,1,"+")
    $ renpy.hide((game.active_girl.id))
    return

label date_waterpark:
    show expression game.active_girl.id
    "We go to a water park."
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
