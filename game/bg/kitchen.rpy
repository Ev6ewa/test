layeredimage bg kitchen:
    if game.hour >= 20 or game.hour <= 5:
        "kitchen_night"
    else:
        "kitchen_day"

init -2 python:
    Room(**{
        "name":"kitchen",
        "exits": ["livingroom", "secondfloor","pool", "bedroom1","bedroom2","bedroom3","bathroom", "bedroom4", "bedroom6"],
        "alternate_exits": ["livingroom"],
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "have_a_meal",
        "hunger": 10,
        "game_conditions": {"min_energy":0,"min_hunger":0,"min_fun":0,"min_grooming":0,"max_hunger":8, "room":["kitchen"], "flag_female":0},
        "girls_conditions":{"sasha":{"not_activity":"meal"},"bree":{"not_activity":"meal"}},
        "display_name": "Have a meal",
        "icon":"eat",
        "say": [
                "I love pasta...\nMaybe that's why I have so much weight to lose...",
                "I make myself a sandwich.",
                "I cook some chicken.",
                "I was never a fish lover, I fancy myself a carnivor.",
                "Why bother with vegetables, meat is life !"
                ]
        })

    Activity(**{
        "name": "have_a_meal_female",
        "hunger": 10,
        "game_conditions": {"min_energy":0,"min_hunger":0,"min_fun":0,"min_grooming":0,"max_hunger":8, "room":["kitchen"], "flag_female":1},
        "girls_conditions":{"sasha":{"not_activity":"meal"},"mike":{"not_activity":"meal"}},
        "display_name": "Have a meal",
        "icon":"eat",
        "say": [
                "I love pasta...\nMaybe that's why I have so much weight to lose...",
                "I make myself a sandwich.",
                "I cook some chicken.",
                "I was never a fish lover, I fancy myself a carnivor.",
                "Why bother with vegetables, meat is life !"
                ]
        })

    Activity(**{
        "name": "drink_a_coffee",
        "energy": 2,
        "duration":0,
        "icon":"coffee",
        "label":["drink_coffee"],
        "game_conditions": {"min_energy":0,"min_hunger":0,"min_fun":0,"min_grooming":0, "room":["kitchen"], "flag_coffee":False},
        "display_name": "Drink a coffee",
        "once_day": True
        })

    Activity(**{
        "name": "have_a_meal_with_everyone",
        "hunger": 10,
        "fun": 2,
        "icon":"eat",
        "girls_conditions": {"sasha":{"present":True,"activity":"meal", "valid":True},"bree":{"present":True,"activity":"meal", "valid":True}},
        "game_conditions": {"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0,"max_hunger":9, "room":["kitchen"], "flag_female":0},
        "display_name": "Eat with the everyone",
        "label": ["have_a_meal_with_everyone"]
        })

    Activity(**{
        "name": "have_a_meal_with_everyone_b",
        "hunger": 10,
        "fun": 2,
        "icon":"eat",
        "girls_conditions": {"sasha":{"present":True,"activity":"meal", "valid":True},"mike":{"present":True,"activity":"meal", "valid":True}},
        "game_conditions": {"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0,"max_hunger":9, "room":["kitchen"], "flag_female":1},
        "display_name": "Eat with the everyone",
        "label": ["have_a_meal_with_everyone"]
        })

    Activity(**{
        "name": "do_the_dishes",
        "duration":0,
        "fun":-0.5,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2, "room":["kitchen"],"flagmax_chores":99},
        "display_name": "Do the dishes",
        "icon":"dishes",
        "label": ["do_the_dishes"],
        "once_day": True
        })

    Event(**{
        "name": "sasha_kitchen_bree",
        "label": ["sasha_kitchen_bree"],
        "duration": 0,
        "girls_conditions": {"sasha":{"present":True},"bree":{"present":True}},
        "game_conditions": {"room":["kitchen"],"chances":5, "flag_female":0, "flag_homeharem":0},
        "do_once": False,
        "once_week": True
        })

label sasha_kitchen_bree:
    show bree at left
    show sasha at right
    "Sasha and Bree are chatting in the kitchen."
    if game.days_played <= 7:
        sasha.say "It's great to have found this place."
        bree.say "Yes, it's cheap and nice."
        sasha.say "And the roommate is kinda cute."
        bree.say "Yes, I wouldn't mind having a slice of him."
        sasha.say "Be careful of your diet."
        $ bree.love += 1
        $ sasha.love += 1
    elif sasha.love() + hero.charm() > 100 and bree.love() + hero.charm() > 100 and sasha.get_flag_value("lesbian") >= 5 and bree.get_flag_value("lesbian") >= 25:
        bree.say "I have seen the way you look at [hero.name]."
        sasha.say "I would not mind sharing him..."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "Me neither."
    elif sasha.love() + hero.charm() > 100 and bree.love() + hero.charm() > 100 and sasha.get_flag_value("lesbian") >= 5:
        bree.say "I have seen the way you look at [hero.name]."
        sasha.say "I would not mind sharing him..."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "Over my dead body."
    elif sasha.love() + hero.charm() > 100 and bree.love() + hero.charm() > 100 and bree.get_flag_value("lesbian") >= 5:
        bree.say "I have seen the way you look at [hero.name]."
        sasha.say "You are no better."
        bree.say "Where there is room for on, there is room for two..."
        sasha.say "Where there is room for me there is not for anyone else."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "Lol."
    elif sasha.love() + hero.charm() > 100 and bree.love() + hero.charm() > 100:
        bree.say "I have seen the way you look at [hero.name]."
        sasha.say "You are no better."
        bree.say "I guess that make us rivals."
        sasha.say "Don't be a sore loser when you find me in bed with him..."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "Lol."
    elif bree.love() + hero.charm() > 100:
        bree.say "I am thinking on making a move on [hero.name]."
        sasha.say "Good luck with that."
        $ sasha.love += 1
    elif sasha.love() + hero.charm() > 100:
        sasha.say "I am thinking of making [hero.name] my personal sextoy."
        bree.say "You should totally go for it."
        $ bree.love += 1
    else:
        "They just chat about girly stuff."
        $ bree.love += 1
        $ sasha.love += 1

    return

label do_the_dishes:
    $ game.set_flag("chores",5,"week","+")
    return

label have_a_meal_with_everyone:
    if not game.get_flag_value("female"):
        call bree_greet from _call_bree_greet_6
    call sasha_greet from _call_sasha_greet_2
    show bree sasha diner
    "We have a nice meal together"
    sasha.say "It's pretty good"
    if not game.get_flag_value("female"):
        bree.say "Yeah, I think so too."
    else:
        mike_say "So true!"
    python:
        g = ["sasha"]
        if not game.get_flag_value("female"):
            g.append("bree")
        for girl in g:
            girl = GIRLS[girl]
            girl.love += 1
            if hero.charm >= 20:
                girl.love += 1
            if hero.check_skill("cooking"):
                girl.love += 1
    hide bree sasha diner
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
