layeredimage bg park:
    if game.hour >= 20 or game.hour <= 5 and game.season == 0:
        "park_0_night"
    elif game.season == 0:
        "park_0_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 1:
        "park_1_night"
    elif game.season == 1:
        "park_1_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 2:
        "park_2_night"
    elif game.season == 2:
        "park_2_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 3:
        "park_3_night"
    elif game.season == 3:
        "park_3_day"

init -2 python:
    Room(**{
        "name":"park",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "music": "music/TRG_Banks/the_night_bus.mp3"
        })

    Activity(**{
        "name": "takeanappark",
        "energy": 1.5,
        "duration": 1,
        "game_conditions": {"min_energy":0, "min_hunger":0, "min_grooming":0, "min_fun":0, "seasons":"1","hours":(8,20),"room":["park"]},
        "display_name": "Take a nap",
        "once_day": True,
        "icon":"sleep",
        "say": [
            "I take a nap.",
            ]
        })

    Activity(**{
        "name": "run_park",
        "fun": 1,
        "energy": -1,
        "grooming": -2,
        "fitness": 1,
        "duration": 2,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_fun":3, "max_fitness":50,"room":["park"]},
        "display_name": "Go for a run",
        "required_item": "sport clothes",
        "icon":"jog",
        "label": ["run_activity"]
        })

    Event(**{
        "name": "thug_attack",
        "game_conditions": {"hours":(22,4),"room":["park"],"chances":5, "flag_female":0},
        "label": ["park_thug_attack"],
        "do_once": False,
        "once_day": True
        })

    Activity(**{
        "name": "think",
        "knowledge": 0.5,
        "game_conditions": {
                "min_energy":5,
                "min_hunger":5,
                "min_grooming":5,
                "min_fun":5,
                "max_knowledge":25,
                "room":["park"]
                },
        "icon":"study",
        "display_name": "Think",
        "once_day": True,
        "say": [
                "What harsh truths do you prefer to ignore?",
                "Is free will real or just an illusion?",
                "Is there a meaning to life? If so, what is it?",
                "Is the meaning of life the same for animals and humans?",
                "Where is the line between art and not art?",
                "Does fate exist? If so, do we have free will?",
                "What does it mean to live a good life?",
                "Why do we dream?",
                "Is it possible to live a normal life and not ever tell a lie?",
                "Does a person’s name influence the person they become?",
                "What should be the goal of humanity?",
                ]
        })

label run_activity:
    python:
        run_say = [
            "I go for a run in the park...",
            "Running is good for what I have."
            ]
        successes = []
        for girl in ROOMS["park"].get_present_girls():
            if hero.fitness()*2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes:
        if len(successes) == 1:
            show expression successes[0].id
            "[successes[0].name] can't takes her eyes off mewhile I run."
            hide expression successes[0].id
        else:
            "The girls can't take their eyes off me while I run."
    else:
        $ renpy.say("",randchoice(run_say))
    return

label park_thug_attack:
    "The park at night sure is scary..."
    thug_say "Hey, you !"
    show danny
    $ result = game.get_flag_value("thugfight")
    if result == 0:
        thug_say "Yes, you! Give me your money !"
        $ fight = False
        $ result = renpy.display_menu([("Give it to him",1),("Refuse",2)])
        if result == 1:
            "I give the thug my money."
            thug_say "Good boy."
            $ hero.money = 0
            $ hero.fun -= 5
        elif result == 2:
            hero.say "No way, go fuck yourself."
            thug_say "You'll regret this faggot."
            $ result = renpy.display_menu([("Attack him",1),("Intimidate him",2)])
            if result == 1:
                $ fight = True
            else:
                hero.say "You should leave, I do Macrame."
                if hero.charm >= 20:
                    thug_say "Is that that uber israelian martial art ?"
                    thug_say "Alright, alright alright..."
                    "He then run away as if the devil was on his tail."
                    $ game.set_flag("thugfight",1)
                else:
                    thug_say "We'll see."
                    $ fight = True
        if fight:
            python:
                d = 50
                if not "martial_arts" in hero.skills:
                    d += 25
            if not hero.fitness >= d:
                show danny fight lose
                "I kick his ass, badly."
                thug_say "I'll have my revenge !"
                "He then run away as if the devil was on his tail."
                $ game.set_flag("thugfight",1)
            else:
                show danny fight win
                "The thug kicks my ass, takes my money and leaves me lying on the ground."
                thug_say "Next time give it nicely."
                if hero.money > 500:
                    $ hero.money -= 500
                else:
                    $ hero.money = 0
                $ hero.grooming -= 5
                $ hero.energy -= 5
                $ hero.fun -= 5
    else:
        show danny scared
        thug_say "Oh, it's you.."
        thug_say "Sorry sir, I didn't reconise you."
    hide danny
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
