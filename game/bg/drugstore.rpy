layeredimage bg drugstore:
    always:
        "drugstore"

init -2 python:
    Room(**{
        "name":"drugstore",
        "exits": ["mall","bakery","bookstore","clothesshop","publicpool","arcade","flowershop","jewelrystore","sexshop","coffeeshop","electronic"],
        "alternate_exits": ["mall"],
        "display_name": "Drugstore",
        "hours": (9,20),
        "buy": [
                Item("condom",money_cost=10),
                Consumable("box of condoms", money_cost = 100, label=["box_of_condoms"]),
                Consumable("medicine", money_cost = 50, label=["cured"])
                ],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "drugstore_shop",
        "duration": 0,
        "display_name": "Shop",
        "icon":"shop",
        "game_conditions":{"room":["drugstore"]},
        "label": ["drugstore_shop"]
        })

label drugstore_shop:
    python:
        hero.shop(ROOMS["drugstore"].buy)
    return

label box_of_condoms:
    python:
        for i in xrange(10):
            hero.gain_item(Item("condom",money_cost=10))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
