layeredimage bg secondfloor:
    if game.hour >= 20 or game.hour <= 5:
        "secondfloor_night"
    else:
        "secondfloor_day"

init python:
    Room(**{
        "name":"secondfloor",
        "display_name": "hallway",
        "exits": ["livingroom","kitchen","pool", "bedroom1","bedroom2","bedroom3","bathroom", "bedroom4", "bedroom6"],
        "alternate_exits": ["livingroom","kitchen","bedroom2","bedroom3","bathroom", "bedroom4", "bedroom6"],
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "knock_bathroom_1",
        "duration": 0,
        "game_conditions":{"room":["secondfloor"],"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0, "flag_female":0},
        "girls_conditions":{"sasha":{"not_room":"bathroom"},"bree":{"room":"bathroom", "valid":True}},
        "display_name": "Knock (bathroom)",
        "icon":"knock_bathroom",
        "label": ["knock_bathroom"],
        })

    Activity(**{
        "name": "knock_bathroom_2",
        "duration": 0,
        "game_conditions":{"room":["secondfloor"],"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0},
        "girls_conditions":{"bree":{"not_room":"bathroom"},"sasha":{"room":"bathroom", "valid":True}},
        "display_name": "Knock (bathroom)",
        "label": ["knock_bathroom"],
        "icon":"knock_bathroom",
        })

    Activity(**{
        "name": "knock_bedroom2",
        "duration": 0,
        "game_conditions":{"room":["secondfloor"],"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0, "flag_female":0},
        "girls_conditions":{"bree":{"room":"bedroom2","valid":True}},
        "display_name": "Knock (Bree)",
        "label": ["knock_bedroom2"],
        "icon":"knock_bedroom2",
        })

    Activity(**{
        "name": "knock_bedroom3",
        "duration": 0,
        "game_conditions":{"room":["secondfloor"],"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0},
        "girls_conditions":{"sasha":{"room":"bedroom3","valid":True}},
        "display_name": "Knock (Sasha)",
        "label": ["knock_bedroom3"],
        "icon":"knock_bedroom3",
        })

    Activity(**{
        "name": "clean_the_secondfloor",
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"room":["secondfloor"],"flagmax_chores":99},
        "display_name": "Vacuum",
        "label": ["clean_the_secondfloor"],
        "icon":"vacuum",
        "once_week": True
        })

label clean_the_secondfloor:
    $ game.set_flag("chores",25,"week","+")
    if game.get_flag_value("chores") > 100:
        $ bree.love += 1
        $ sasha.love += 1
    return

label knock_bedroom2:
    python:
        girls = ROOMS["bedroom2"].get_present_girls()
        if girls:
            girl = girls[0]
            if girl.get_activity()[1]["activity"] == "sleep":
                girl.say("No answer, she must be sleeping.")
            elif girl.activity["clothes"] == "naked" and girl.love() < 140:
                girl.say("Don't come in...")
            elif girl.activity["clothes"] in ["underwear","towel"] and girl.love() < 100 - hero.charm()/2:
                girl.say("Don't come in...")
            else:
                girl.say("Yes ?")
        else:
            renpy.say("","No answer")
    return

label knock_bedroom3:
    python:
        girls = ROOMS["bedroom3"].get_present_girls()
        if girls:
            girl = girls[0]
            if girl.get_activity()[1]["activity"] == "sleep":
                girl.say("No answer, she must be sleeping.")
            elif girl.activity["clothes"] == "naked" and girl.love() < 140:
                girl.say("Don't come in...")
            elif girl.activity["clothes"] == ["underwear","towel"] and girl.love() < 100:
                girl.say("Don't come in...")
            else:
                girl.say("Yes ?")
        else:
            renpy.say("","No answer")
    return

label knock_bathroom:
    python:
        girls = ROOMS["bathroom"].get_present_girls()
        if girls:
            if len(girls) > 1:
                if girls[0].love >= girls[1].love():
                    girl = girls[1]
                else:
                    girl = girls[0]
            else:
                girl = girls[0]
            if girl.activity["clothes"] == "naked" and girl.love() < 140:
                girl.say("Don't come in, it's occupied.")
            elif girl.activity["clothes"] == ["underwear","towel"] and girl.love() < 100:
                girl.say("Don't come in...")
            else:
                girl.say("Yes ?")
            for girl in girls:
                if girl.get_activity()[1]["activity"] == "shower" and not girl.get_flag_value("peeped"):
                    p = True
                    break
                else:
                    p = False
        else:
            renpy.say("","No answer")
    if p:
        "The door is not locked, maybe I could take a peek."
        menu:
            "Do it.":
                show expression girl.id+" shower"
                "I see [girl.name] showering..."
                "She is so beautiful."
                $ girl.set_flag("peeped", True, "day")
                $ hero.fun += 1
                hide expression girl.id+" shower"
            "Don't":
                pass
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
