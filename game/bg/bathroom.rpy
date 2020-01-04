layeredimage bg bathroom:
    always:
        "bathroom"

init -2 python:
    Room(**{
        "name":"bathroom",
        "exits": ["livingroom", "secondfloor","kitchen","pool", "bedroom1","bedroom2","bedroom3", "bedroom4", "bedroom6"],
        "alternate_exits": ["secondfloor"],
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"underwear"
        })

    Activity(**{
        "name": "take_a_shower",
        "grooming": 8,
        "game_conditions": {
                "room":["bathroom"],
                "min_hunger":0,
                "min_energy":0,
                "min_grooming":0,
                "max_grooming":10,
                "min_fun":0
                },
        "display_name": "Take a shower",
        "label": ["take_a_shower"],
        "icon":"shower",
        "say": [
                "...",
                "...I'm Picky 'cause I'm all alone\nMaybe I'm alone 'cause I'm a picky one\nI got a lotta girls waiting for me not to call...",
                "...Je ne fais pourtant de tort à personne,\nEn n'écoutant pas le clairon qui sonne...",
                "...Till the sandman comes\nSleep with one eye open\nGripping your pillow tight...",
                "...Cause' I'm a picker\nI'm a grinner\nI'm a lover And I'm a sinner...",
                "I can't be the only guy who mentally adds my cock to the sight of a girl yawning.",
                ]
        })

    Activity(**{
        "name": "practicespeech",
        "charm": 0.5,
        "icon":"mirror",
        "game_conditions": {
                "room":["bathroom"],
                "min_energy":5,
                "min_hunger":5,
                "min_grooming":5,
                "min_fun":5,
                "max_charm":25,
                "flag_female":0
                },
        "display_name": "Practice speech",
        "once_day": True,
        "say": [
                "Hey babe, how are you doin'?",
                "Looking sexy!",
                "Wow, I am hot indeed...",
                "You know you want me.",
                "Wanna try the backdoor?"
                ]
        })

    Activity(**{
        "name": "makeup",
        "charm": 0.5,
        "icon":"mirror",
        "game_conditions": {
                "room":["bathroom"],
                "min_energy":5,
                "min_hunger":5,
                "min_grooming":5,
                "min_fun":5,
                "max_charm":25,
                "flag_female":1
                },
        "display_name": "Put some make-up on",
        "once_day": True,
        "say": [
                "Looking sexy!",
                ]
        })

    Activity(**{
        "name": "clean_the_bathroom",
        "game_conditions": {
                "room":["bathroom"],
                "min_energy":2,
                "min_hunger":2,
                "min_grooming":2,
                "min_fun":2,
                "flagmax_chores":99
                },
        "icon":"vacuum",
        "display_name": "Clean",
        "label": ["clean_the_bathroom"],
        "once_week": True
        })

label take_a_shower:
    python:
        for girl in ROOMS[game.room].get_present_girls():
            girl.love += 1
    return

label clean_the_bathroom:
    python:
        game.set_flag("chores",25,"week","+")
        if game.get_flag_value("chores") > 100:
            bree.love += 1
            sasha.love += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
