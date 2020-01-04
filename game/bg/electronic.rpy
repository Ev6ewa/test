layeredimage bg electronic:
    always:
        "electronic"

init -2 python:
    Room(**{
        "name":"electronic",
        "exits": ["mall","bakery","bookstore","clothesshop","publicpool","arcade","flowershop","jewelrystore","sexshop","coffeeshop","drugstore"],
        "alternate_exits": ["mall"],
        "display_name": "Electronic Store",
        "hours": (9,20),
        "buy": [
                Item("zbox 360",money_cost = 200, one_only=True, tooltip="Play videogames at home"),
                Item("fitness machine",money_cost = 600, one_only=True, tooltip="Gain Fitness while sleeping"),
                Item("knowledge machine",money_cost = 600, one_only=True, tooltip="Gain Knowledge while sleeping"),
                Item("charm machine",money_cost = 600, one_only=True, tooltip="Gain Charm while sleeping"),
                Item("spy camera",money_cost = 500, one_only=True, tooltip="Micro camera for secretly recording things"),
                Item("electric guitar",money_cost = 1000, one_only=True, tooltip="An axe shaped electric guitar... METAL!")
                ],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "electronic_shop",
        "duration": 0,
        "icon":"shop",
        "display_name": "Shop",
        "game_conditions":{"room":["electronic"]},
        "label": ["electronic_shop"]
        })

    Activity(**{
        "name": "work_electronic",
        "money_gain": (["knowledge"],(0.5,)),
        "duration": 4,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"flag_job":"electronic","room":["electronic"]},
        "display_name": "Work",
        "icon":"work",
        "say": [
            "Workin' hard or hardly workin'? That's what the customers ask. The answer is always hardly workin'."
            ]
        })

label electronic_shop:
    python:
        hero.shop(ROOMS["electronic"].buy)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
