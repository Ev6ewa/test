layeredimage bg flowershop:
    always:
        "flowershop"

init -2 python:
    Room(**{
        "name":"flowershop",
        "exits": ["mall","drugstore","bakery","bookstore","clothesshop","publicpool","arcade","jewelrystore","sexshop","coffeeshop","electronic"],
        "alternate_exits": ["mall"],
        "hours": (9,20),
        "display_name": "Flower Shop",
        "buy": [
            Gift("flowers",money_cost=50,label="flowers",love_bonus=1, limit=50),
            Gift("lots of flowers",money_cost=100,label="flowers",love_bonus=2, limit=50)
            ],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "flowershop_shop",
        "duration": 0,
        "display_name": "Shop",
        "icon":"shop",
        "game_conditions": {"room":["flowershop"]},
        "label": ["flowershop_shop"]
        })

label flowershop_shop:
    python:
        hero.shop(ROOMS["flowershop"].buy)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
