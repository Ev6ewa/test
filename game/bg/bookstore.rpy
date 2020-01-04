layeredimage bg bookstore:
    always:
        "bookstore"

init -2 python:
    Room(**{
        "name":"bookstore",
        "exits": ["mall","drugstore","bakery","clothesshop","publicpool","arcade","flowershop","jewelrystore","sexshop","coffeeshop","electronic"],
        "alternate_exits": ["mall"],
        "hours": (9,20),
        "display_name": "Book Store",
        "buy": [
            Gift("gift book", money_cost = 30, label = "book", love_bonus = 1, limit=50),
            Gift("Mistress Amanda", money_cost = 50, label = "book", sub_bonus = -1),
            Gift("Yuri Manga", money_cost = 50, label = "book", les_bonus = 1),
            Gift("A sex slave's story", money_cost = 50, label = "book", sub_bonus = 1, limit=100),
            Consumable("knowledge book", money_cost = 100, effects = [("knowledge",2),("time",4)], limit = "week"),
            Consumable("charm book", money_cost = 100, effects = [("charm",2),("time",4)], limit = "week"),
            Consumable("fun book", money_cost = 25, effects = [("fun",4),("time",2)], limit = "day"),
            ],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "bookstore_shop",
        "label": ["bookstore_shop"],
        "duration": 0,
        "icon":"shop",
        "game_conditions":{"room":["bookstore"],},
        "display_name": "Shop",
        })

    Event(**{
        "name": "book_signing",
        "label": ["book_signing"],
        "duration": 0,
        "game_conditions": {
            "room":["bookstore"],
            "chances": 5, 
            "flag_female":0
            },
        "girls_conditions": {
            "bree":{
                "min_love":25,
                "not_room":["bookstore"]
                }
            },
        "do_once": False
        })

    Activity(**{
        "name": "ask_for_a_job_bookstore",
        "duration": 0,
        "icon": "askforjob",
        "game_conditions":{"room":["bookstore"],"flag_job":False,"flagmin_morality":25},
        "display_name": "Ask for a job",
        "once_month":True,
        "label": ["bakery_ask_for_a_job"]
        })

    Activity(**{
        "name": "work_bookstore",
        "money_gain": (["charm"],(1,)),
        "duration": 4,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"flag_job":"bookstore","room":["bookstore"]},
        "display_name": "Work",
        "icon":"work",
        "say": [
            "If I can sell a hundred books I get a one dollar bonus!"
            ]
        })

label book_signing:

    "Bree's favorite author is here, signing books."
    "Maybe I should get his latest book and get it signed."
    $ result = renpy.display_menu([("Do it",1),("Don't do it",2)])
    if result ==1:
        if hero.money >= 50:
            $ hero.money-=50
            $ hero.gain_item(Gift("Fantasy book (signed)",money_cost=50, label="signed_fantasy_book",love_bonus=0))
            "I am pretty sure she will be thrilled."
            $ game.pass_time(needs=True)
        else:
            "Too bad I don't have enough money."
    else:
        "It's not worth the my time."

    return

label bookstore_shop:
    $ BUY = list(ROOMS["bookstore"].buy)
    if game.day%2 == 0:
        $ BUY += [Consumable("Skill book: massage", money_cost = 200, label = ["massage_skill_book"], uses = 10, tooltip="A book to learn how to give massages")]
    if game.day%2 == 1:
        $ BUY += [Consumable("Skill book: guitar", money_cost = 200, label = ["guitar_skill_book"], uses = 10, tooltip="A book to learn how to play the guitar")]
    $ hero.shop(BUY)
    return


label massage_skill_book:
    if "massage" in hero.skills:
        "I know everything I need to about massages."
    else:
        $ game.pass_time(2)
        $ game.set_flag("massageTraining",1,mod="+")
        $ skill = game.get_flag_value("guitarTraining")*10
        "I read about massages in the book. ([skill]%%)"
        if game.get_flag_value("massageTraining") >= 100 and not "massage" in hero.skills:
            $ hero.skills.append("massage")
    return


label guitar_skill_book:
    if "guitar" in hero.skills:
        "I know everything I need to about playing guitar."
    else:
        $ game.pass_time(2)
        $ game.set_flag("guitarTraining",1,mod="+")
        $ skill = game.get_flag_value("guitarTraining")*10
        "I practice guitar. ([skill]%%)"
        if skill >= 100 and not "guitar" in hero.skills:
            $ hero.skills.append("guitar")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
