layeredimage bg date_livingroom:
    if game.hour >= 20 or game.hour <= 5:
        "livingroom_night"
    else:
        "livingroom_day"

init -2 python:
    Room(**{
        "name":"date_livingroom",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Home",
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })

    Date(
        "livingroom",
        display_name="home",
        clothes = "casual",
        game_conditions={"valid_room":"date_livingroom"},
        love_gain = 0,
        )

    Activity(**{
        "name": "date_play_console",
        "duration": 1,
        "icon":"videogame",
        "game_conditions":{"room":["date_livingroom"]},
        "display_name": "Play console",
        "label": ["date_play_console"],
        "once_day":True,
        "required_item": "zbox 360"
        })

    Activity(**{
        "name": "date_play_boardgame",
        "duration": 1,
        "icon": "boardgame",
        "game_conditions":{"room":["date_livingroom"]},
        "display_name": "Play boardgame",
        "label": ["date_play_boardgame"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_snacks",
        "duration": 1,
        "hunger":2,
        "icon":"eat",
        "game_conditions":{"room":["date_livingroom"]},
        "display_name": "Make some snacks",
        "label": ["date_snacks"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_watch_tv",
        "duration": 1,
        "icon":"tv",
        "game_conditions":{"room":["date_livingroom"]},
        "display_name": "Watch TV",
        "label": ["date_watch_tv"],
        "once_day":True,
        })

    Activity(**{
        "name": "date_chat_couch",
        "duration": 1,
        "icon": "talk",
        "game_conditions":{"room":["date_livingroom"]},
        "display_name": "Chat on the couch",
        "label": ["date_chat_couch"]
        })

    Activity(**{
        "name": "date_play_guitar",
        "duration": 1,
        "icon":"guitar",
        "game_conditions":{"room":["date_livingroom"], "skill":"guitar"},
        "display_name": "Play guitar",
        "label": ["date_play_guitar"]
        })

    Activity(**{
        "name": "date_swim_pool_home",
        "fun": 1,
        "duration": 1,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_grooming":0,"min_fun":3,"seasons":"01","room":["date_livingroom"]},
        "display_name": "Go for a swim",
        "required_item": "swimsuit",
        "label": ["date_swim_pool_home"],
        "once_day": True,
        "icon":"swim"
        })

label date_chat_couch:
    show expression game.active_girl.id
    "We sit on the couch to chat."
    call expression game.active_girl.get_chat() from _call_expression_7
    return

label date_watch_tv:
    show expression game.active_girl.id
    menu:
        "Watch a movie":
            $ p = False
        "Watch Porn":
            $ p = True
    if not p:
        "We watch some TV."
        $ game.set_flag("datescore",5,1,"+")
    else:
        if hero.charm >= 100 - game.active_girl.love():
            "We watch some porn."
            $ game.set_flag("datescore",5,1,"+")
            if "slutty" in game.active_girl.traits:
                $ game.set_flag("datescore",5,1,"+")
                $ game.active_girl.sub += 1
            menu:
                "SM porn":
                    $ game.active_girl.sub += 1
                "Femdom porn":
                    $ game.active_girl.sub -= 1
                "Gonzo porn":
                    $ game.set_flag("datescore",5,1,"+")
                "Lesbian porn":
                    $ game.set_flag("datescore",5,1,"+")
                    $ NOTIFICATIONS.append([game.active_girl.name+" {image=ui/icon_les_vsmall.png}+5",2])
                    $ game.active_girl.set_flag("lesbian",1,mod="+")
        else:
            active_girl.say "Sorry, I don't want to watch this sort of things."
            $ game.set_flag("datescore",5,1,"-")
    hide expression game.active_girl.id
    return

label date_swim_pool_home:
    scene bg pool
    show expression game.active_girl.id+" swimsuit"
    "We go to the pool and play in the water."
    $ game.set_flag("datescore",5,1,"+")
    return

label date_snacks:
    scene bg kitchen
    show expression game.active_girl.id
    "We go to the kitchen and eat some snacks."
    call expression game.active_girl.get_chat() from _call_expression_4
    $ game.set_flag("datescore",5,1,"+")
    return

label date_play_console:
    show expression game.active_girl.id
    "I play some video games with [game.active_girl.name]."
    $ d = 0
    if "geek" in game.active_girl.traits:
        $ d += 1
    if "playful" in game.active_girl.traits:
        $ d += 1
    if d == 0:
        $ d -= 1
    $ game.set_flag("datescore",d*5,1,"+")
    return

label date_play_guitar:
    show expression game.active_girl.id
    "I play some guitar for [game.active_girl.name]."
    $ d = 1
    if "guitar" in game.active_girl.traits:
        $ d += 1
    $ game.set_flag("datescore",d*5,1,"+")
    return

label date_play_boardgame:
    show expression game.active_girl.id
    "I play some boardgames with [game.active_girl.name]."
    $ d = 0
    if "geek" in game.active_girl.traits:
        $ d += 1
    if "playful" in game.active_girl.traits:
        $ d += 1
    if d == 0:
        $ d -= 1
    $ game.set_flag("datescore",d*5,1,"+")
    return

label date_livingroom:
    show expression game.active_girl.id
    "We decide to hang out at the house."
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
