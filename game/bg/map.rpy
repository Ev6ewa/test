layeredimage bg map:
    if game.hour >= 20 or game.hour <= 5 and game.season == 0:
        "street_0_night"
    elif game.season == 0:
        "street_0_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 1:
        "street_1_night"
    elif game.season == 1:
        "street_1_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 2:
        "street_2_night"
    elif game.season == 2:
        "street_2_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 3:
        "street_3_night"
    elif game.season == 3:
        "street_3_day"

init -2 python:
    Room(**{
        "name":"map",
        "exits": ["livingroom","gym","gym2","cinema","church","beach", "waterpark","studio", "station","university","pub","nightclub","mall","office","park","apartmentbuilding","stripclub", "lounge", "hospital", "punkbar"],
        "alternate_exits": ["livingroom","gym","gym2","cinema","church", "waterpark","studio", "station","university","pub","nightclub","mall","office","park","apartmentbuilding","stripclub", "lounge", "hospital", "punkbar"],
        "display_name": "city",
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Event(**{
        "name": "meet",
        "game_conditions": {"room":["map"],"chances":5, "flag_female":0},
        "label": ["meet"],
        "do_once": False,
        "once_day": True,
        })

    Event(**{
        "name": "assault",
        "game_conditions": {"hours":(0,4),"room":["map"],"chances":5, "flag_female":0},
        "label": ["assault"],
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name": "found_money",
        "game_conditions": {"room":["map"],"chances":1},
        "label": ["found_money"],
        "do_once": False,
        "once_week": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"wish_had_sport_clothes",
        "game_conditions": {"room":["map"],"chances":5},
        "duration": 0,
        "label":["wish_had_sport_clothes"],
        "do_once": True,
        "required_item":"not_sport clothes",
        "quit": False
        })

    Event(**{
        "name":"wish_had_fancy_clothes",
        "label":["wish_had_fancy_clothes"],
        "game_conditions": {"room":["map"],"chances":5},
        "duration": 0,
        "required_item":"not_fancy clothes",
        "do_once": True,
        "quit": False
        })

    Event(**{
        "name":"buy_drugs",
        "label":["buy_drugs"],
        "game_conditions": {"room":["map"],"chances":5, "hours":(22,4)},
        "duration": 0,
        "quit": True
        })

label buy_drugs:
    show shawn shady
    "A shady looking guy approaches me."
    man_say "Wanna have fun?"
    menu:
        "Buy drugs" if hero.money >= 100:
            hero.say "Sure"
            $ hero.gain_item(Consumable("drugs", money_cost = 100, effects = [("fun",10), ("energy",5)], limit = "day"))
            $ hero.money -= 100
            if game.get_flag_value("morality") >= -25:
                if game.get_flag_value("female"):
                    $ NOTIFICATIONS.append(["{image=ui/icon_good.png}-1",2])
                $ game.set_flag("morality",1,mod="-")
            man_say "Pleasure doing business with you."
        "No":
            if game.get_flag_value("morality") <= 25:
                if game.get_flag_value("female"):
                    $ NOTIFICATIONS.append(["{image=ui/icon_good.png}+1",2])
                $ game.set_flag("morality",1,mod="+")

    hide shawn
    return

label wish_had_sport_clothes:
    "I heard of a good gym around here, but I will need sport clothes to be admitted."
    return

label wish_had_fancy_clothes:
    "I heard of a nightclub around here, but I will need nicer clothes to be admitted."
    return


label found_money:
    scene bg street
    $ amount = randint(5,50)
    "I found $[amount] on the sidewalk."
    menu:
        "Take it":
            $ hero.money += amount
            $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
            $ game.set_flag("morality",1,mod="-")
        "Leave it":
            $ NOTIFICATIONS.append(["{image=ui/icon_good.png}+1",2])
            $ game.set_flag("morality",1,mod="+")
            pass
    return

label assault:
    python:
        choices = []
        for g in GIRLS.values():
            if g.id not in HIDDEN and g.room in ROOMS["map"].exits:
                choices.append(g)
        if choices:
            game.active_girl = randchoice(choices)
            game.active_girl.set_room("street")
            renpy.show(("bg street"))
            renpy.say("","The city at night can be scary...")
            active_girl.say("Heeelp !")
            renpy.say("", "I hear [game.active_girl.name] screaming.")
            ch = renpy.display_menu([("Help her",1),("Don't help her",2)])
            if ch == 1:
                renpy.say("","I rush toward the dark alley the screams are coming from.")
                renpy.show("bg alley")
                renpy.show("danny fist")
                renpy.say(thug_say,"Show me what you are hiding under those clothes bitch.")
                renpy.hide("danny")
                renpy.show(game.active_girl.id)
                active_girl.say("Leave me alone...")
                renpy.hide((game.active_girl.id))
                renpy.show("danny fist")
                hero.say("You should leave her alone, or else...")
                result = game.get_flag_value("thugfight")
                if result == 0:
                    renpy.say(thug_say,"Else what you sucker.")
                    renpy.say(thug_say,"Ok, if you give me your money, I'll leave her be.")
                    fight = False
                    result = renpy.display_menu([("Give it to him",1),("Refuse",2)])
                    if result == 1:
                        renpy.say("","I give the thug my money.")
                        renpy.say(thug_say,"Good boy.")
                        renpy.hide("danny")
                        renpy.show(game.active_girl.id)
                        hero.money = 0
                        hero.fun -= 5
                        game.active_girl.love += 1
                        active_girl.say("Thanks for the help.")
                        hero.say("It was nothing.")
                        renpy.hide((game.active_girl.id))
                        if "pacifist" in game.active_girl.traits:
                            game.active_girl.love +=1
                    elif result == 2:
                        hero.say("No way, go fuck yourself.")
                        renpy.say(thug_say,"You'll regret this faggot.")
                        result = renpy.display_menu([("Attack him",1),("Intimidate him",2)])
                        if result == 1:
                            fight = True
                        else:
                            hero.say("You should leave, I am black belt in origami.")
                            if hero.charm >= 20:
                                renpy.show("danny scared")
                                renpy.say(thug_say,"Is that an ancient japanese ninja martial art ?")
                                renpy.say(thug_say,"I won't fight a fucking ninja...")
                                renpy.say("","He then run away as if the devil was on his tail.")
                                renpy.hide("danny")
                                renpy.show(game.active_girl.id)
                                active_girl.say("Thanks for the help.")
                                hero.say("It was nothing.")
                                game.active_girl.love += 1
                                if "pacifist" in game.active_girl.traits:
                                    game.active_girl.love +=1
                                if "playful" in game.active_girl.traits:
                                    game.active_girl.love +=1
                                renpy.hide((game.active_girl.id))
                            else:
                                renpy.say(thug_say,"We'll see.")
                                fight = True
                    if fight:
                        d = 25
                        if not "martial_arts" in hero.skills:
                            d += 25
                        if not hero.fitness >= d:
                            renpy.show("danny fight lose")
                            renpy.say("","I kick his ass, badly.")
                            renpy.say(thug_say,"I'll have my revenge !")
                            renpy.say("","He then run away as if the devil was on his tail.")
                            game.set_flag("thugfight",1)
                            renpy.hide("danny fight lose")
                            renpy.show(game.active_girl.id)
                            hero.say("Are you okay "+game.active_girl()+" ?")
                            active_girl.say("I am fine [hero.name], thanks for the help.")
                            game.active_girl.love += 1
                            if "submissive" in game.active_girl.traits:
                                game.active_girl.love +=1
                            if "princess" in game.active_girl.traits:
                                game.active_girl.love +=1
                            renpy.hide((game.active_girl.id))
                        else:
                            renpy.show("danny fight win")
                            renpy.say("","The thug kick my ass, take my money and leave me lying on the ground.")
                            renpy.say(thug_say,"Next time give it nicely.")
                            renpy.hide("danny fight win")
                            renpy.show(game.active_girl.id)
                            if hero.money > 500:
                                hero.money -= 500
                            else:
                                hero.money = 0
                            hero.grooming -= 5
                            hero.energy -= 5
                            hero.fun -=5
                            renpy.show(game.active_girl.id)
                            active_girl.say("Are you okay [hero.name] ?")
                            hero.say("I am fine, at least he left.")
                            active_girl.say("Thanks for the help.")
                            hero.say("It was nothing.")
                            game.active_girl.love += 1
                            if "motherly" in game.active_girl.traits:
                                game.active_girl.love +=1
                            if "princess" in game.active_girl.traits:
                                game.active_girl.love +=1
                            if "dominant" in game.active_girl.traits:
                                game.active_girl.love +=1
                            renpy.hide((game.active_girl.id))
                else:
                    renpy.show("danny scared")
                    renpy.say(thug_say,"Oh, it's you..")
                    renpy.say(thug_say,"Sorry sir, I didn't reconise you.")
                    hero.say("Are you okay "+game.active_girl()+" ?")
                    renpy.hide("danny")
                    renpy.show(game.active_girl.id)
                    active_girl.say("I am fine [hero.name], thanks for the help.")
                    game.active_girl.love += 1
                    if "submissive" in game.active_girl.traits:
                        game.active_girl.love +=1
                    if "princess" in game.active_girl.traits:
                        game.active_girl.love +=1
                    if "pacifist" in game.active_girl.traits:
                        game.active_girl.love +=1
                    if "rebel" in game.active_girl.traits:
                        game.active_girl.love +=1
                    renpy.hide((game.active_girl.id))
                renpy.hide((game.active_girl.id))
            else:
                renpy.say("","I leave the area discretly.")
                game.active_girl.love +=1
    $ game.active_girl = None
    return

label meet:
    python:
        choices = []
        for g in GIRLS.values():
            if g.id not in HIDDEN and g.room in ROOMS["map"].exits:
                choices.append(g)
    if choices:
        $ meet_girl = randchoice(choices)
        scene bg street
    else:
        return
    $ meet_change_outfit = False
    if meet_girl.get_clothes() not in ["date", "work","casual"]:
        $ meet_change_outfit = True
        $ meet_old_girl_clothes = game.girl_clothes
        $ game.girl_clothes = "casual"
    "I meet [meet_girl.name] walking in the street."
    show expression meet_girl.id
    call expression meet_girl.id+"_greet" from _call_expression_27
    call expression meet_girl.get_chat() from _call_expression_96
    meet_girl.say "See you later [hero.name]."
    hide expression meet_girl.id
    if meet_change_outfit:
        $ game.girl_clothes = meet_old_girl_clothes
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
