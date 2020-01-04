layeredimage bg date_mall:
    always:
        "mall"

init -2 python:
    Room(**{
        "name":"date_mall",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Mall",
        "hours": (14,18),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Date(
        "mall",
        display_name="mall",
        clothes = "casual",
        game_conditions={"valid_room":"date_mall"},
        love_gain = 0,
        )

    Activity(**{
        "name": "date_go_shopping",
        "duration": 1,
        "icon":"shop",
        "game_conditions":{"room":["date_mall"], "min_money":50},
        "display_name": "Go shopping",
        "label": ["date_go_shopping"]
        })


    Activity(**{
        "name": "date_steal_shit",
        "duration": 1,
        "icon": "steal",
        "game_conditions":{"room":["date_mall"]},
        "display_name": "Steal shit",
        "label": ["date_steal_shit"]
        })

    Activity(**{
        "name": "date_play_arcade",
        "duration": 1,
        "game_conditions":{"room":["date_mall"]},
        "fun": 2,
        "icon":"arcade",
        "money_cost":25,
        "display_name": "Play at the arcade",
        "label": ["date_play_arcade"]
        })

    Activity(**{
        "name": "date_piercing_shop",
        "duration": 1,
        "icon": "piercing",
        "game_conditions":{"room":["date_mall"], "min_money":50},
        "girls_conditions":{"ACTIVE":{"min_sub":30}},
        "display_name": "Visit the piercing shop",
        "label": ["date_piercing_shop"],
        "once_day":True
        })

    Activity(**{
        "name": "date_coffee",
        "duration": 1,
        "money_cost":20,
        "energy":1,
        "icon":"coffee",
        "game_conditions":{"room":["date_mall"]},
        "display_name": "Have a coffee",
        "label": ["date_coffee"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_photobooth",
        "duration": 0,
        "money_cost":5,
        "icon": "picture",
        "game_conditions":{"room":["date_mall"]},
        "display_name": "Take a pic together",
        "label": ["date_photobooth"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_bakery",
        "duration": 1,
        "money_cost":20,
        "hunger":1,
        "icon": "pastry",
        "game_conditions":{"room":["date_mall"]},
        "display_name": "Have a pastry",
        "label": ["date_bakery"],
        "once_day":True,
        })

label date_photobooth:
    show expression game.active_girl.id
    "We go to a photo booth and have hour pictures taken."
    $ game.set_flag("datescore",5,1,"+")
    return

label date_steal_shit:
    show expression game.active_girl.id
    "We go and steal some stuff in various shops."
    if not "rebel" in game.active_girl.traits and not "poor" in game.active_girl.traits:
        $ game.set_flag("datescore",25,1,"-")
    else:
        $ game.set_flag("datescore",5,"day","+")
    return


label date_bakery:
    scene bg bakery
    show expression game.active_girl.id
    "We go to the bakery to eat a pastry."
    call expression game.active_girl.get_chat() from _call_expression_5
    if "gourmand" in game.active_girl.traits:
        $ game.set_flag("datescore",5,"day","+")
    return

label date_coffee:
    scene bg coffeeshop
    show expression game.active_girl.id
    "We go to the coffeeshop to have a coffee."
    call expression game.active_girl.get_chat() from _call_expression_6
    return

label date_piercing_shop:
    show expression game.active_girl.id
    "I take [game.active_girl.name] to the piercing shop."
    $ piercings = game.active_girl.get_piercings()
    menu:
        "What piercing should I ask her to get?"
        "Nose ($50)" if "nose" in piercings and not piercings["nose"].get("pierced",False):
            $ piercings["nose"]["pierced"] = True
            $ hero.money -= 50
        "Remove nose ($50)" if "nose" in piercings and piercings["nose"].get("pierced",False):
            $ piercings["nose"]["pierced"] = False
            $ hero.money -= 50
        "Navel ($100)" if "navel" in piercings and not piercings["navel"].get("pierced",False):
            $ piercings["navel"]["pierced"] = True
            $ hero.money -= 100
        "Remove navel ($50)" if "navel" in piercings and piercings["navel"].get("pierced",False):
            $ piercings["navel"]["pierced"] = False
            $ hero.money -= 50
        "Tongue ($200)" if "tongue" in piercings and not piercings["tongue"].get("pierced",False):
            $ piercings["tongue"]["pierced"] = True
            $ hero.money -= 200
        "Remove tongue ($50)" if "tongue" in piercings and piercings["tongue"].get("pierced",False):
            $ piercings["tongue"]["pierced"] = False
            $ hero.money -= 50
        "Lips ($200)" if "lips" in piercings and not piercings["lips"].get("pierced",False):
            $ piercings["lips"]["pierced"] = True
            $ hero.money -= 200
        "Remove lips ($50)" if "lips" in piercings and piercings["lips"].get("pierced",False):
            $ piercings["lips"]["pierced"] = False
            $ hero.money -= 50
        "Eyebrow ($200)" if "eyebrow" in piercings and not piercings["eyebrow"].get("pierced",False):
            $ piercings["eyebrow"]["pierced"] = True
            $ hero.money -= 200
        "Remove eyebrow ($50)" if "eyebrow" in piercings and piercings["eyebrow"].get("pierced",False):
            $ piercings["eyebrow"]["pierced"] = False
            $ hero.money -= 50
        "Nipples ($400)" if "nipples" in piercings and not piercings["nipples"].get("pierced",False):
            $ piercings["nipples"]["pierced"] = True
            $ hero.money -= 400
        "Remove nipples ($50)" if "nipples" in piercings and piercings["nipples"].get("pierced",False):
            $ piercings["nipples"]["pierced"] = False
            $ hero.money -= 50
        "Clit ($800)" if "clit" in piercings and not piercings["clit"].get("pierced",False):
            $ piercings["clit"]["pierced"] = True
            $ hero.money -= 800
        "Remove clit ($50)" if "clit" in piercings and piercings["clit"].get("pierced",False):
            $ piercings["clit"]["pierced"] = False
            $ hero.money -= 50
        "None":
            pass
    $ game.active_girl.set_flag("newpiercings",piercings)
    active_girl.say "Thank you [hero.name]."
    hide expression game.active_girl.id
    return

label date_play_arcade:
    scene bg arcade
    show expression game.active_girl.id
    "I take [game.active_girl.name] to the arcade."
    $ d = 0
    if "geek" in game.active_girl.traits:
        $ d += 1
    if "playful" in game.active_girl.traits:
        $ d += 1
    if d == 0:
        $ d -= 1
    $ game.set_flag("datescore",d*5,1,"+")
    hide expression game.active_girl.id
    hide bg arcade
    return

label date_go_shopping:
    show expression game.active_girl.id
    "I take [game.active_girl.name] on a shopping spree."
    menu:
        "Spend $50":
            $ game.set_flag("datescore",5,1,"+")
            $ hero.money -= 50
        "Spend $100" if hero.money >= 100:
            $ game.set_flag("datescore",10,1,"+")
            $ hero.money -= 100
        "Spend $200" if hero.money >= 200:
            $ game.set_flag("datescore",15,1,"+")
            $ hero.money -= 200
        "Spend $400" if hero.money >= 400:
            $ game.set_flag("datescore",20,1,"+")
            $ hero.money -= 400
        "Spend $800" if hero.money >= 800:
            $ game.set_flag("datescore",25,1,"+")
            $ hero.money -= 800
        "Spend $1600" if hero.money >= 1600:
            $ game.set_flag("datescore",30,1,"+")
            $ hero.money -= 1600
    hide expression game.active_girl.id
    return

label date_mall:
    show expression game.active_girl.id
    "We go to the mall."
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
