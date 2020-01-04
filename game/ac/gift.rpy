init -15 python:
    Activity(**{
        "name": "gift",
        "display_name": "Offer a gift",
        "label": ["give_a_gift"],
        "girls_conditions": {
            "ACTIVE":{
                "min_love":40,
                "not_activity":["sleep","work"]
                }
            },
        "game_conditions": {
            "activity":"interact",
            "inventory":"gifts"
            },
        "icon": "gift",
        "once_day": "ACTIVE_GIRL",
        "duration": 0
        })

    Activity(**{
        "name": "gift_b",
        "display_name": "Offer a gift",
        "label": ["give_a_gift"],
        "girls_conditions": {
            "ACTIVE":{
                "min_love":20,
                "max_love":39,
                "not_activity":["sleep","work"],
                "birthday":True,
                }
            },
        "icon":"gift",
        "game_conditions": {
            "activity":"interact",
            "inventory":"gifts"
            },
        "once_day": "ACTIVE_GIRL",
        "duration": 0
        })

label give_a_gift:
    $ game.active_girl.set_flag("interact",1,1,"+")
    call expression game.active_girl.id+"_greet" from _call_expression_18
    $ result = renpy.call_screen("select",[g.name for g in hero.inventory.values() if isinstance(g, Gift)],"Available gifts")
    python:
        d = 75
        if game.get_season() == game.active_girl.birthday[0] and game.day == game.active_girl.birthday[1]:
            d -= 25
        elif game.get_season() == "spring" and game.day == 14:
            d += 25
        elif game.get_season() == "winter" and game.day == 25:
            d -= 25
    if result != "None":
        if hero.charm >= d - game.active_girl.love() and not (hasattr(hero.inventory[result], "once") and hero.inventory[result].once and game.active_girl.get_flag_value("gift"+hero.inventory[result].name)):
            $ result = hero.inventory[result]
            if game.get_season() == game.active_girl.birthday[0] and game.day == game.active_girl.birthday[1] and renpy.has_label(game.active_girl.id+"_birthday_gift"):
                call expression game.active_girl.id+"_birthday_gift" from _call_expression_19
            elif game.get_season() == "spring" and game.day == 14 and renpy.has_label(game.active_girl.id+"_valentine_gift"):
                call expression game.active_girl.id+"_valentine_gift" from _call_expression_40
            elif game.get_season() == "winter" and game.day == 25 and renpy.has_label(game.active_girl.id+"_christmas_gift"):
                call expression game.active_girl.id+"_christmas_gift" from _call_expression_41
            if renpy.has_label(game.active_girl.id+"_gift_"+result.label):
                call expression game.active_girl.id+"_gift_"+result.label from _call_expression_20
            else:
                show expression game.active_girl.id
                active_girl.say "Thank you."
                $ renpy.hide((game.active_girl.id))
            if not hero.activity.get_flag_value('canceled'):
                $ result.use(game.active_girl)
        else:
            show expression game.active_girl.id
            $ hero.activity.set_flag("canceled",True)
            active_girl.say "No thanks."
            $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
