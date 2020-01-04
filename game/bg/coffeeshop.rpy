layeredimage bg coffeeshop:
    always:
        "coffeeshop"

init -2 python:
    Room(**{
        "name":"coffeeshop",
        "exits": ["mall","drugstore","bakery","bookstore","clothesshop","publicpool","arcade","flowershop","jewelrystore","sexshop","electronic"],
        "alternate_exits": ["mall"],
        "display_name": "Coffee shop",
        "hours": (9,20),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "drink_a_coffe_coffeshop",
        "label":["drink_coffee"],
        "duration": 0,
        "energy":2,
        "money_cost":10,
        "icon":"coffee",
        "game_conditions":{"room":["coffeeshop"],"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0, "flag_coffee":False},
        "display_name": "Order a coffee",
        "once_day":True,
        "say": [
            "Just coffee. Black - like my soul.",
            "Even bad coffee is better than no coffee at all.",
            "Adventure in life is good; consistency in coffee even better.",
            "It doesn't matter where you're from - or how you feel... There's always peace in a strong cup of coffee.",
            "Do you know how helpless you feel if you have a full cup of coffee in your hand and you start to sneeze?"
            ]
        })

label drink_coffee:
    python:
        renpy.say("",randchoice([
                "Just coffee. Black - like my soul.",
                "As long as there is coffee in the world, how bad could things be?",
                "It is inhumane, in my opinion, to force people who have a genuine medical need for coffee to wait in line behind people who apparently view it as some kind of recreational activity.",
                "Coffee is a way of stealing time that should by rights belong to your older self.",
                "Black as night, sweet as sin."
                ]))
    $ game.set_flag("coffee",True,"day")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
