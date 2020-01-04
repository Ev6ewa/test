layeredimage bg arcade:
    always:
        "arcade"

init -2 python:
    Room(**{
        "name":"arcade",
        "hours":(12,20),
        "display_name": "Arcade",
        "exits": ["mall","drugstore","bakery","bookstore","clothesshop","publicpool","flowershop","jewelrystore","sexshop","coffeeshop","electronic"],
        "alternate_exits": ["mall"],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "play_a_videogame",
        "duration": 1,
        "game_conditions": {
            "room":["arcade"],
            "min_grooming":1,
            "min_fun":0,
            "min_hunger":1,
            "min_energy":1
            },
        "icon":"arcade",
        "fun": 3,
        "money_cost": 1,
        "display_name": "Play a game",
        "say": [
            "I play a few games of Street Racer.",
            "I play a Fatal Kombat for a while.",
            "Meat fighter 2 is such a great game, the boobs physics are awesome...",
            ],
        })

    Event(**{
        "name": "arcade_competion",
        "label": ["arcade_competion"],
        "duration": 0,
        "game_conditions": {
            "days":"3",
            "room":["arcade"]
            },
        "do_once": False
        })

    Event(**{
        "name":"play_with_bree",
        "label": ["play_with_bree"],
        "duration": 0,
        "game_conditions": {
            "room":["arcade"],
            "chances":50, 
            "flag_female":0
            },
        "girls_conditions": {
            "bree":{
                "present":True,
                "min_love":10,
                "flag_playarcade":True
                }
            },
        "do_once": False,
        "once_day": True
        })

label play_with_bree:
    call expression "bree_greet" from _call_expression_16
    show bree
    "Bree looks at me with a defiant look."
    bree.say "Wanna play me?"
    menu:
        "Accept":
            $ bree.love += 1
            hero.say "Sure."
            if hero.check_skill("video_games"):
                $ bonus = 10
            else:
                $ bonus = 0
            if hero.knowledge() + bonus >= 25:
                if hero.knowledge() + bonus >= bree.love():
                    $ bree.love += 1
                "I beat her quite easily."
                hero.say "That was fun..."
                bree.say "Yeah, we absolutely must do it again some other time."
            else:
                hero.say "I got defeated."
                bree.say "Don't worry, you'll get me next time."
        "Refuse":
            show bree sad
            hero.say "No sorry."
            bree.say "Another time then."
    hide bree
    return


label arcade_competion:
    "There is a videogame competition going on."
    "The participation fee is 25$."
    if hero.money >= 25:
        $ result = renpy.display_menu([("Participate",1),("Don't participate",2)])
        if result == 1:
            $ hero.money -= 25
            if hero.check_skill("video_games"):
                $ bonus = 3
            else:
                $ bonus = 0
            $ bonus += hero.knowledge()/20 + randint(-5,5)
            if bonus > 0:
                $ money = bonus*15
                "I won, the prize was [money]$"
                $ hero.money += money
            else:
                "I lost."
        else:
            "I don't feel like participating."
    else:
        "I don't have money to participate."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
