layeredimage bg mall:
    always:
        "mall"

init -2 python:
    Room(**{
        "name":"mall",
        "exits": ["map","bakery","bookstore","clothesshop","publicpool","arcade","flowershop","jewelrystore","sexshop","coffeeshop","electronic","drugstore"],
        "alternate_exits": ["map","bakery","bookstore","clothesshop","publicpool","arcade","flowershop","jewelrystore","sexshop","coffeeshop","electronic","drugstore"],
        "days": "123456",
        "hours": (9,20),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "buy": [
                Item("bike",money_cost = 500, one_only=True, tooltip="Go to far away places (slowly)"),
                Item("car",money_cost = 10000, one_only=True, tooltip="Go to far away places (fast)"),
                Item("sport_car", display_name="Sport Car",money_cost = 200000, one_only=True, tooltip="Go to far away places (fast) with class"),
                Item("luxury bed",money_cost = 200, one_only=True, tooltip="Be rested with less sleep"),
                Item("wedding ring",money_cost = 2000, tooltip="Ask a girl to marry you"),
                ],
        "outfit":"casual"
        })

    Activity(**{
        "name": "mall_shop",
        "duration": 0,
        "icon":"shop",
        "display_name": "Shop",
        "game_conditions":{"room":["mall"]},
        "label": ["mall_shop"]
        })

    Activity(**{
        "name": "eat_a_hotdog",
        "duration": 0,
        "hunger": 2,
        "money_cost": 5,
        "game_conditions": {"min_hunger":0, "room":["mall", "date_mall"]},
        "display_name": "Eat a hotdog",
        "icon":"hotdog",
        "once_day":True,
        "say": [
            "Munch, munch...\nMunch...",
            ]
        })

    Activity(**{
        "name": "get_a_haircut",
        "charm": 3,
        "game_conditions": {
                "room":["mall"],
                "min_energy":5,
                "min_hunger":5,
                "min_grooming":5,
                "min_fun":5,
                "max_charm":50,
                },
        "display_name": "Get a haircut",
        "once_week": True,
        "icon":"haircut",
        "say": [
                "I'll look better this way",
                ],
        "money_cost":50,
        })

label mall_shop:
    python:
        hero.shop(ROOMS["mall"].buy)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
