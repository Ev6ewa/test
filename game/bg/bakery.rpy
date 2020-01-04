layeredimage bg bakery:
    always:
        "bakery"

init -2 python:
    Room(**{
        "name":"bakery",
        "exits": ["mall","drugstore","bookstore","clothesshop","publicpool","arcade","flowershop","jewelrystore","sexshop","coffeeshop","electronic"],
        "alternate_exits": ["mall"],
        "display_name": "Bakery",
        "hours": (9,20),
        "buy": [
                Gift("cake",money_cost=10, label="sweets",love_bonus=.5, limit=50),
                Gift("candies",money_cost=5, label="sweets",love_bonus=.2, limit=50),
                Consumable("Minty candies", money_cost = 25, effects = [("grooming",1)], limit = "day"),
                Consumable("Energy drink", money_cost = 25, effects = [("energy",1)], limit = "day"),
                Consumable("Pastry", money_cost = 25, effects = [("hunger",1)], limit = "day"),
                ],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "bakery_shop",
        "duration": 0,
        "icon":"shop",
        "game_conditions":{"room":["bakery"]},
        "display_name": "Shop",
        "label": ["bakery_shop"]
        })

    Activity(**{
        "name": "ask_for_a_job_mike",
        "duration": 0,
        "icon": "askforjob",
        "game_conditions":{"room":["bakery","electronic","gym", "bookstore", "sexshop"],"flag_job":False, "flag_fired":True, "flag_female":0},
        "display_name": "Ask for a job",
        "label": ["bakery_ask_for_a_job"]
        })

    Activity(**{
        "name": "ask_for_a_job",
        "duration": 0,
        "icon": "askforjob",
        "game_conditions":{"room":["bakery","electronic","gym"],"flag_job":False, "flag_female":1},
        "display_name": "Ask for a job",
        "label": ["bakery_ask_for_a_job"]
        })

    Activity(**{
        "name": "quit_job",
        "duration": 0,
        "icon": "quitjob",
        "game_conditions":{"room":["bakery","electronic","gym","sexshop","bookstore"],"flagin_job":["bakery","electronic","gym","sexshop","bookstore"]},
        "display_name": "Quit your job",
        "once_day":True,
        "label": ["bakery_quit_for_a_job"]
        })

    Activity(**{
        "name": "work_bakery",
        "money_gain": (["charm"],(0.5,)),
        "duration": 4,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"flag_job":"bakery","room":["bakery"]},
        "display_name": "Work",
        "icon":"work",
        "say": [
            "Making bread, making sandwiches, selling sandwiches. Boring but pays the bills, right?"
            ]
        })


label bakery_quit_for_a_job:
    hero.say "I wanna quit my job!"
    show_owner_say "...Too bad."
    python:
        game.set_flag("job",False)
    return

label bakery_ask_for_a_job:
    hero.say "I saw the sign saying that you are recruiting and I would like to apply if possible..."
    show_owner_say "Sure, the job is yours"
    python:
        game.set_flag("job",game.room)
    return

label bakery_shop:
    python:
        hero.shop(ROOMS["bakery"].buy)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
