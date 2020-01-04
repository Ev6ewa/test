init python:

    Event(**{
        "name":"pay_bills",
        "label": ["pay_bills"],
        "duration": 0,
        "priority": 1000,
        "game_conditions":{"days":"1","days_played":1,"activity":"wake_up"},
        "do_once": False,
        "once_week": True,
        "quit": False
        })

    Event(**{
        "name":"sick",
        "label": ["sick"],
        "duration": 0,
        "game_conditions":{"flag_sick":False,"activity":"wake_up","chances":5},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"low_energy",
        "label": ["low_energy"],
        "duration": 0,
        "priority": 100,
        "game_conditions":{"max_energy":3,"chances":10},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"low_hunger",
        "label": ["low_hunger"],
        "duration": 0,
        "priority": 100,
        "game_conditions":{"max_hunger":3,"chances":10},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"low_grooming",
        "label": ["low_grooming"],
        "duration": 0,
        "priority": 100,
        "game_conditions":{"max_grooming":3,"chances":10},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"low_fun",
        "label": ["low_fun"],
        "duration": 0,
        "priority": 100,
        "game_conditions":{"max_fun":3,"chances":10},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

label low_fun:
    "I am so bored."
    return

label low_grooming:
    "I smell like something died in my pants."
    return

label low_hunger:
    "I am so hungry."
    return

label low_energy:
    "I am so tired."
    return

label sick:
    hero.say "Cough. Cough"
    "I think I might be sick."
    $ game.set_flag("sick",True,randint(1,3))
    return

label cured:
    hero.say "I feel better."
    $ game.set_flag("sick",False)
    return

label pay_bills:
    if persistent.difficulty == 0:
        $ rent = 100
    elif persistent.difficulty == -1:
        $ rent = 50
    else:
        $ rent = 200
    if game.get_flag_value("debt"):
        "Time to pay my weekly debt due..."
        if hero.money >= 100:
            $ hero.money -= 100
        else:
            "I don't have enough money..."
            "I should at least give what I have..."
            $ hero.money = 0
    if hero.money >= rent:
        "Time to pay the rent..."
        $ hero.money -= rent
    else:
        "I don't have enough money to pay the rent..."
        "I should at least give what I have..."
        python:
            bree.love -= 10
            sasha.love -= 10
            hero.money = 0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
