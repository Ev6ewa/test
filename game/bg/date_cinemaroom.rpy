layeredimage bg date_cinemaroom:
    always:
        "cinemaroom"

init -2 python:
    Room(**{
        "name":"date_cinemaroom",
        "exits": ["date_cinema"],
        "alternate_exits": ["map"],
        "display_name": "Movie Theater",
        "hours": (14,24),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name" : "date_put_hand_on_leg",
        "display_name" : "Hand on leg",
        "icon": "caress",
        "label" : ["date_put_hand_on_leg"],
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":0},
        "once_day" : True,
        "duration" : 0,
        "girls_conditions":{"ACTIVE":{"flag_datehand":False}}
        })

    Activity(**{
        "name": "date_put_hand_between_legs",
        "display_name": "Hand between her legs",
        "icon": "between",
        "label": ["date_put_hand_between_legs"],
        "once_day": True,
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":0,"flag_male":False},
        "duration": 0,
        "girls_conditions":{"ACTIVE":{"flag_datehand":"leg"}}
        })

    Activity(**{
        "name": "date_put_hand_in_panties",
        "display_name": "Finger her",
        "icon": "finger",
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":0},
        "label": ["date_put_hand_in_panties"],
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":"between","flag_male":False}}
        })

    Activity(**{
        "name": "date_caress_boobs",
        "display_name": "Caress her boobs",
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":0},
        "label": ["date_caress_boobs"],
        "icon":"caressboobs",
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":False,"flag_male":False}}
        })

    Activity(**{
        "name": "date_caress_boobs_inside",
        "display_name": "Put your hand inside",
        "label": ["date_caress_boobs_inside"],
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":0},
        "icon":"handinbra",
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":"breasts","flag_male":False}}
        })

    Activity(**{
        "name": "date_watch_the_movie",
        "display_name": "Watch the movie",
        "fun":2,
        "icon":"cinema",
        "label": ["date_watch_the_movie"],
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":0},
        "duration": 1,
        })




    Activity(**{
        "name" : "date_put_hand_on_leg_b",
        "display_name" : "Hand on leg",
        "icon": "caress",
        "label" : ["date_put_hand_on_leg"],
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":25},
        "once_day" : True,
        "duration" : 0,
        "girls_conditions":{"ACTIVE":{"flag_datehand":False}}
        })

    Activity(**{
        "name": "date_put_hand_between_legs_b",
        "display_name": "Hand between her legs",
        "icon": "between",
        "label": ["date_put_hand_between_legs"],
        "once_day": True,
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":15},
        "duration": 0,
        "girls_conditions":{"ACTIVE":{"flag_datehand":"leg","flag_male":False}}
        })

    Activity(**{
        "name": "date_put_hand_in_panties_b",
        "display_name": "Finger her",
        "icon": "finger",
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":-15},
        "label": ["date_put_hand_in_panties"],
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":"between","flag_male":False}}
        })

    Activity(**{
        "name": "date_caress_boobs_b",
        "display_name": "Caress her boobs",
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":-5},
        "label": ["date_caress_boobs"],
        "icon": "caressboobs",
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":False,"flag_male":False}}
        })

    Activity(**{
        "name": "date_caress_boobs_inside_b",
        "display_name": "Put your hand inside",
        "label": ["date_caress_boobs_inside"],
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":-10},
        "icon": "handinbra",
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":"breasts","flag_male":False}}
        })



    Activity(**{
        "name": "date_put_hand_on_crotch",
        "display_name": "Hand on his crotch",
        "icon": "crotch",
        "label": ["date_put_hand_on_crotch"],
        "once_day": True,
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":15},
        "duration": 0,
        "girls_conditions":{"ACTIVE":{"flag_datehand":"leg","flag_male":True}}
        })

    Activity(**{
        "name": "date_put_hand_in_pants",
        "display_name": "Put your hand in his pants",
        "icon": "pants",
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":0},
        "label": ["date_put_hand_in_pants"],
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":"crotch","flag_male":True}}
        })

    Activity(**{
        "name": "date_jerk_off",
        "display_name": "Jerk him off",
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":-20},
        "label": ["date_jerk_off"],
        "icon": "handjob",
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":"pants","flag_male":True}}
        })

    Activity(**{
        "name": "date_blow_him",
        "display_name": "Blow him",
        "label": ["date_blow"],
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1, "flagmax_morailty":-50},
        "icon": "blowjob",
        "once_day": True,
        "duration": 0,
        "girls_conditions": {"ACTIVE":{"flag_datehand":"pants","flag_male":True}}
        })

    Activity(**{
        "name": "date_watch_the_movie",
        "display_name": "Watch the movie",
        "fun":2,
        "icon":"cinema",
        "label": ["date_watch_the_movie"],
        "game_conditions":{"room":["date_cinemaroom"], "flag_female":1},
        "duration": 1,
        })

label date_watch_the_movie:
    "I watch the movie."
    return

label date_caress_boobs_inside:
    python:
        renpy.show(game.active_girl.id)
        renpy.say("","I move my hand inside her top to caress her skin directly.")
        if not game.active_girl.love >= 100 - hero.charm():
            active_girl.say("What do you think you are doing ?")
            game.active_girl.set_flag("datehand",False,1)
            game.set_flag("datescore",25,1,"-")
        else:
            renpy.say("","She blushes a litlle when my fingers reaches her nipples.")
            renpy.say("","After a while I remove my hand...")
            renpy.say("","She looks a little disappointed.")
            game.active_girl.set_flag("datehand",False,1)
            if "slutty" in game.active_girl.traits:
                game.set_flag("datescore",20,1,"+")
            else:
                game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return

label date_caress_boobs:
    python:
        renpy.show(game.active_girl.id)
        renpy.say("","I start caressing her breasts above her clothes.")
        if not game.active_girl.love > 75 - hero.charm():
            active_girl.say("What do you think you are doing ?")
            game.set_flag("datescore",10,1,"-")
        else:
            renpy.say("","She looks a little anxious but let my hand caress her.")
            game.active_girl.set_flag("datehand","breasts",1)
            if "slutty" in game.active_girl.traits:
                game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return

label date_put_hand_in_panties:
    python:
        renpy.say("","I push her underwear aside and try to put my finger inside her.")
        if not game.active_girl.love() > 125 - hero.charm():
            active_girl.say("What do you think you are doing ?")
            game.active_girl.set_flag("datehand",False,1)
            game.set_flag("datescore",10,1,"-")
        else:
            renpy.say("","Her breath starts to get heavy as I finger her.")
            active_girl.say("Mmmmmmh")
            renpy.say("","She slowly reach her climax, while watching the movie.")
            game.active_girl.set_flag("datehand",False,1)
            if "slutty" in game.active_girl.traits:
                game.set_flag("datescore",5,1,"+")
                game.set_flag("datescore",20,1,"+")
            else:
                game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return

label date_put_hand_between_legs:
    python:
        renpy.say("","I move my hand up toward "+game.active_girl()+"'s panties.")
        if not game.active_girl.love() > 100 - hero.charm():
            active_girl.say("What do you think you are doing ?")
            game.active_girl.set_flag("datehand",False,1)
            game.set_flag("datescore",10,1,"-")
        else:
            renpy.say("","She moan a little when I reach her underwear.")
            game.active_girl.set_flag("datehand","between",1)
            if "slutty" in game.active_girl.traits:
                game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return

label date_put_hand_on_leg:
    python:
        renpy.show(game.active_girl.id)
        renpy.say("","I slowly move my hand to "+game.active_girl()+"'s leg.")
        if not game.active_girl.love > 75 - hero.charm() and not game.active_girl.get_flag_value("male"):
            active_girl.say("What do you think you are doing ?")
            game.set_flag("datescore",10,1,"-")
        else:
            if not game.active_girl.get_flag_value("male"):
                renpy.say("","Her skin is soft under my fingers.")
                renpy.say("","She look at my hand but doesn's say anything.")
            else:
                renpy.say("","I put my hand on his leg.")
            game.active_girl.set_flag("datehand","leg",1)
            if "slutty" in game.active_girl.traits:
                game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return

label date_put_hand_on_crotch:
    python:
        renpy.show(game.active_girl.id)
        renpy.say("","I slowly move my hand to "+game.active_girl()+"'s crotch.")
        game.active_girl.set_flag("datehand","crotch",1)
        if "sluts" in game.active_girl.desire_factors:
            game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return


label date_put_hand_in_pants:
    python:
        renpy.show(game.active_girl.id)
        renpy.say("","I unbutton his pants and squeeze my hand inside it.")
        game.active_girl.set_flag("datehand","pants",1)
        if "sluts" in game.active_girl.desire_factors:
            game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return


label date_jerk_off:
    python:
        renpy.show(game.active_girl.id)
        renpy.say("","I jerk him off until he comes in my hand.")
        game.active_girl.set_flag("datehand","jerk",1)
        if "sluts" in game.active_girl.desire_factors:
            game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return


label date_blow:
    python:
        renpy.show(game.active_girl.id)
        renpy.say("","I get on my knees and blow him.")
        game.active_girl.set_flag("datehand","blow",1)
        if "sluts" in game.active_girl.desire_factors:
            game.set_flag("datescore",5,1,"+")
        renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
