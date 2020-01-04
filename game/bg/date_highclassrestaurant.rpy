layeredimage bg date_highclassrestaurant:
    always:
        "highclassrestaurant"

layeredimage bg highclassrestaurant:
    always:
        "highclassrestaurant"

layeredimage bg publicbathroom:
    always:
        "publicbathroom"

init -2 python:
    Room(**{
        "name":"date_highclassrestaurant",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Fancy restaurant",
        "hours": (19,24),
        "required_item": "fancy clothes",
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"date"
        })

    Date(
        "highclassrestaurant",
        display_name="fancy restaurant",
        money_cost=100,
        game_conditions={"valid_room":"date_highclassrestaurant"},
        clothes = "date",
        love_gain = 2,
        )

    Activity(**{
        "name": "date_hand_on",
        "duration": 0,
        "icon": "touch",
        "game_conditions":{"room":["date_highclassrestaurant"]},
        "display_name": "Touch her hand",
        "label": ["date_hand_on"],
        "once_day": True
        })

    Activity(**{
        "name": "date_order_for_her",
        "duration": 1,
        "icon": "order",
        "game_conditions":{"room":["date_highclassrestaurant"]},
        "display_name": "Order for her",
        "label": ["date_order_for_her"],
        "girls_conditions": {
                "ACTIVE":{
                        "flag_eatenrestaurant":False,
                        "flag_orderedrestaurant":False
                        }
                },
        "once_day": True
        })

    Activity(**{
        "name": "date_eat_restaurant",
        "duration": 1,
        "icon":"eat",
        "display_name": "Eat",
        "label": ["date_eat_restaurant"],
        "min_girls": 1,
        "hunger": 10,
        "fun": 2,
        "game_conditions": {
                "room":["date_highclassrestaurant"],
                "min_energy":0,
                "min_hunger":0,
                "min_grooming":0,
                "min_fun":0
                },
        "girls_conditions": {
                "ACTIVE":{
                        "flag_eatenrestaurant":False,
                        }
                },
        "once_day": True
        })

    Activity(**{
        "name": "date_pay_restaurant",
        "duration": 0,
        "icon": "pay",
        "display_name": "Pay for both of you",
        "label": ["date_pay_restaurant"],
        "min_girls": 1,
        "money_cost": 100,
        "game_conditions": {
                "room":["date_highclassrestaurant"],
                "min_energy":0,
                "min_hunger":0,
                "min_grooming":0,
                "min_fun":0
                },
        "girls_conditions": {
                "ACTIVE":{
                        "flag_eatenrestaurant":True,
                        }
                },
        "once_day": True
        })

label date_highclassrestaurant:
    show expression game.active_girl.id
    "We go to a high class restaurant."
    $ renpy.hide((game.active_girl.id))
    return

label date_pay_restaurant:
    show expression game.active_girl.id
    "I pay for both our meals."
    python:
        for t in game.active_girl.traits:
            if t in ["submissive","dominant","princess","poor"]:
                game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    return

label date_eat_restaurant:
    show expression game.active_girl.id
    $ game.set_flag("datescore",5,1,"+")
    if hero.charm >= game.active_girl.love:
        $ game.set_flag("datescore",5,1,"+")
    "I eat with [game.active_girl.name]."
    $ chat = game.active_girl.get_chat()
    $ renpy.call_in_new_context(chat)
    $ game.active_girl.set_flag("eatenrestaurant",True,"day")
    $ game.active_girl.set_flag("orderedrestaurant",True,"day")
    $ renpy.hide((game.active_girl.id))
    return

label date_order_for_her:
    show expression game.active_girl.id
    "I order some food for [game.active_girl.name]."
    if not game.active_girl.has_trait("submissive"):
        active_girl.say "I can order for myself, thank you very much..."
        $ game.set_flag("datescore",10,1,"-")
    else:
        active_girl.say "I like a man who his not afraid of taking charge."
        $ game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    $ game.active_girl.set_flag("orderedrestaurant",True,"day")
    return

label date_hand_on:
    show expression game.active_girl.id
    "I move my hand on top of hers."
    if hero.charm < 100 - game.active_girl.love():
        active_girl.say "What do you think you are doing ?"
        $ game.set_flag("datescore",10,1,"-")
    else:
        "[game.active_girl.name] interlock her fingers with mine while smiling."
        $ game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
