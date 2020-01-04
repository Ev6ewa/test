layeredimage bg clothesshop:
    always:
        "clothesshop"

init -2 python:
    Room(**{
        "name":"clothesshop",
        "exits": ["mall","drugstore","bakery","bookstore","publicpool","arcade","flowershop","jewelrystore","sexshop","coffeeshop","electronic"],
        "alternate_exits": ["mall"],
        "display_name": "Clothes Shop",
        "hours": (9,20),
        "buy": [
                Gift("sexy underwear", money_cost = 150, label = "underwear", love_bonus = 3, once=True, limit=100),
                Gift("sexy dress", money_cost = 200, label = "clothes", love_bonus = 4, once=True, limit=100),
                Gift("cute top", money_cost = 100, label = "clothes", love_bonus = 2, once=True, limit=100),
                Gift("nice scarf", money_cost = 50, label = "clothes", love_bonus = 1, once=True),
                Gift("sexy swimsuit", money_cost = 100, label = "swimsuit", love_bonus = 2, once=True, limit=100),
                Gift("cute swimsuit", money_cost = 200, label = "swimsuit", love_bonus = 4, once=True, limit=100),
                Gift("purse", money_cost = 200, label = "purse", love_bonus = 4, once=True, limit=100),
                Gift("fancy purse", money_cost = 400, label = "purse", love_bonus = 6, once=True, limit=100),
                Gift("shoes", money_cost = 100, label = "shoes", love_bonus = 2, once=True, limit=100),
                Gift("fancy shoes", money_cost = 200, label = "shoes", love_bonus = 4, once=True, limit=100)
                ],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "clothesshop_shop",
        "duration": 0,
        "display_name": "Shop",
        "icon":"shop",
        "game_conditions":{"room":["clothesshop"]},
        "label": ["clothesshop_shop"]
        })

label clothesshop_shop:
    python:
        result = renpy.call_screen("select",["Women section","Men section"])
        if result == "Women section" and not game.get_flag_value("female"):
            hero.shop(ROOMS["clothesshop"].buy)
        elif result == "Men section" and not game.get_flag_value("female"):
            result2 = renpy.call_screen("select",["Clothes","Accessories"])
            if result2 == "Clothes":
                shop = [
                    Equip("fancy clothes", money_cost = 200, effects = {"pacifist":20,"princess":20,"charm":10}),
                    Equip("leather jacket", money_cost = 100, effects = {"submissive":20,"rebel":20,"charm":5}),
                    Equip("tweed blazer", money_cost = 100, effects = {"bookworm":20,"family":20,"knowledge":5}),
                    Equip("sweat pants", money_cost = 100, effects = {"sportsy":20, "dominant":20,"fitness":5}),
                    Equip("funny shirt", money_cost = 100, effects = {"geek":20,"playful":20,"charm":5}),
                    Equip("military fatigues", money_cost = 100, effects = {"submissive":20,"gourmand":20,"charm":5}),
                    Equip("sport clothes", money_cost = 200, effects = {"sportsy":30,"fitness":10}),
                    Equip("swimsuit", money_cost = 200, effects = {"sportsy":30,"fitness":10})
                    ]
            else:
                shop = [
                    Equip("luxury watch", money_cost = 200, type = "accessory", effects = {"pacifist":20,"princess":20,"charm":10}),
                    Equip("cool sunglasses", money_cost = 100, type = "accessory", effects = {"submissive":20,"rebel":20,"charm":5}),
                    Equip("geeky pen", money_cost = 100, type = "accessory", effects = {"bookworm":20,"family":20,"knowledge":5}),
                    Equip("sport shoes", money_cost = 100, type = "accessory", effects = {"sportsy":20, "dominant":20,"fitness":5}),
                    Equip("funny badge", money_cost = 100, type = "accessory", effects = {"geek":20,"playful":20,"charm":5}),
                    Equip("military boots", money_cost = 100, type = "accessory", effects = {"submissive":20,"gourmand":20,"charm":5}),
                    ]
            hero.shop(shop)
        elif result == "Women section":
            result2 = renpy.call_screen("select",["Clothes","Accessories"])
            if result2 == "Clothes":
                shop = [
                    Equip("fancy dress", money_cost = 200, effects = {"pacifist":20,"princess":20,"charm":10}),
                    Equip("leather jacket", money_cost = 100, effects = {"submissive":20,"rebel":20,"charm":5}),
                    Equip("cardigan", money_cost = 100, effects = {"bookworm":20,"family":20,"knowledge":5}),
                    Equip("sweat pants", money_cost = 100, effects = {"sportsy":20, "dominant":20,"fitness":5}),
                    Equip("funny shirt", money_cost = 100, effects = {"geek":20,"playful":20,"charm":5}),
                    Equip("leather pants", money_cost = 100, effects = {"submissive":20,"gourmand":20,"charm":5}),
                    Equip("sport clothes", money_cost = 200, effects = {"sportsy":30,"fitness":10}),
                    Equip("swimsuit", money_cost = 200, effects = {"sportsy":30,"fitness":10})
                    ]
            else:
                shop = [
                    Equip("luxury bracelet", money_cost = 200, type = "accessory", effects = {"pacifist":20,"princess":20,"charm":10}),
                    Equip("cool sunglasses", money_cost = 100, type = "accessory", effects = {"submissive":20,"rebel":20,"charm":5}),
                    Equip("geeky pen", money_cost = 100, type = "accessory", effects = {"bookworm":20,"family":20,"knowledge":5}),
                    Equip("sport shoes", money_cost = 100, type = "accessory", effects = {"sportsy":20, "dominant":20,"fitness":5}),
                    Equip("funny badge", money_cost = 100, type = "accessory", effects = {"geek":20,"playful":20,"charm":5}),
                    Equip("military boots", money_cost = 100, type = "accessory", effects = {"submissive":20,"gourmand":20,"charm":5}),
                    ]
            hero.shop(shop)
        elif result == "Men section":
            shop = [
                Gift("sexy underwear", money_cost = 150, label = "underwear", love_bonus = 3, once=True, limit=100),
                Gift("tuxedo", money_cost = 200, label = "clothes", love_bonus = 4, once=True, limit=100),
                Gift("t-shirt", money_cost = 100, label = "clothes", love_bonus = 2, once=True, limit=100),
                Gift("leather shoes", money_cost = 50, label = "clothes", love_bonus = 1, once=True, limit=100),
                Gift("swimming t-back", money_cost = 100, label = "swimsuit", love_bonus = 2, once=True, limit=100),
                Gift("swimming trunk", money_cost = 200, label = "swimsuit", love_bonus = 4, once=True, limit=100),
                Gift("wallet", money_cost = 200, label = "purse", love_bonus = 4, once=True, limit=100),
                Gift("fancy watch", money_cost = 400, label = "purse", love_bonus = 6, once=True, limit=100),
                Gift("sports shoes", money_cost = 100, label = "shoes", love_bonus = 2, once=True, limit=100),
                ],
            hero.shop(shop)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
