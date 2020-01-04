init -15 python:
    Activity(**{
        "name": "offer_a_drink",
        "money_cost": 10,
        "duration": 0,
        "game_conditions": {
            "activity":"interact",
            "min_energy":3,
            "min_hunger":0,
            "min_grooming":3,
            "min_fun":3,
            "hours":(19,5),
            "room":["punkbar","nightclub","stripclub","pub","date_pub", "lounge", "date_nightclub"]
            },
        "icon":"buydrink",
        "display_name": "Offer a drink",
        "label": ["offer_a_drink"],
        "once_hour": True,
        })


label offer_a_drink:
    call expression game.active_girl.id+"_greet" from _call_expression_37
    if renpy.has_label(game.active_girl.id+"_offer_drink"):
        call expression game.active_girl.id+"_offer_drink" from _call_expression_38
    else:
        show expression game.active_girl.id
        hero.say "[game.active_girl.name], would you like a drink ?"
        if (hero.charm >= 60 - game.active_girl.love() and game.active_girl.get_flag_value("drinks") < 2) or game.get_flag_value("dateinprogress") == game.active_girl:
            $ hero.money -= 5
            active_girl.say "Yeah sure"
            $ renpy.hide((game.active_girl.id))
            show expression "bar "+game.active_girl.id
            call expression game.active_girl.get_chat() from _call_expression_39
            if game.active_girl.love <= 25:
                $ game.active_girl.love += 1
            elif game.get_flag_value("dateinprogress") == game.active_girl:
                $ game.set_flag("datescore",5,"day","+")
            hide expression "bar "+game.active_girl.id
            $ game.active_girl.set_flag("drinks",1,"day",mod="+")
        else:
            active_girl.say "Sorry, I don't feel like drinking"
            $ hero.activity.set_flag("canceled")
            $ renpy.hide((game.active_girl.id))
    $ game.active_girl.set_flag("interact",1,1,"+")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
