layeredimage bg sexshop:
    always:
        "sexshop"

init -2 python:
    Room(**{
        "name":"sexshop",
        "exits": ["mall","drugstore","bookstore","clothesshop","publicpool","arcade","flowershop","jewelrystore","bakery","coffeeshop","electronic"],
        "alternate_exits": ["mall"],
        "display_name": "Sexshop",
        "hours": (9,20),
        "buy": [
                Item("anal beads",money_cost = 200),
                Item("vibrator",money_cost = 200),
                Item("dildo",money_cost = 400),
                Item("large dildo",money_cost = 800),
                Item("blindfold",money_cost = 200),
                Gift("slave collar", money_cost = 100, label = "collar", love_bonus = 2, once=True, limit=100),
                ],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "sexshop_shop",
        "duration": 0,
        "game_conditions":{"room":["sexshop"]},
        "display_name": "Shop",
        "icon":"shop",
        "label": ["sexshop_shop"]
        })

    Activity(**{
        "name": "ask_for_a_job_sexshop",
        "duration": 0,
        "icon": "askforjob",
        "game_conditions":{"room":["sexshop"],"flag_job":False,"flagmax_morality":-25},
        "display_name": "Ask for a job",
        "once_month":True,
        "label": ["bakery_ask_for_a_job"]
        })

    Activity(**{
        "name": "work_sexshop",
        "money_gain": (["charm"],(1,)),
        "duration": 4,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"flag_job":"sexshop","room":["sexshop"]},
        "display_name": "Work",
        "icon":"work",
        "say": [
            "Going to be honest, I like selling dildos."
            ]
        })

label sexshop_shop:
    python:
        hero.shop(ROOMS["sexshop"].buy)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
