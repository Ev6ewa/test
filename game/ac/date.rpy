init -15 python:
    Activity(**{
        "name": "date",
        "display_name": "Ask on a date",
        "label": ["date_her"],
        "game_conditions": {
            "activity":"interact",
            "min_energy":2,
            "min_hunger":2,
            "min_grooming":2,
            "min_fun":2
            },
        "icon":"askdate",
        "girls_conditions": {
            "ACTIVE":{
                "min_love":20,
                "date_planned":False,
                "not_activity":["sleep"]
                }
            },
        "once_day": "ACTIVE_GIRL",
        "duration": 0
        })

    Activity(**{
        "name": "cancel_date",
        "display_name": "cancel date",
        "label": ["cancel_date"],
        "game_conditions": {
            "activity":"interact",
            "min_energy":2,
            "min_hunger":2,
            "min_grooming":2,
            "min_fun":2,
            "flag_dateinprogress":0
            },
        "girls_conditions": {
            "ACTIVE":{
                "date_planned":True,
                "not_activity":["sleep"]
                }
            },
        "duration": 0,
        "icon": "abortdate",
        })

label cancel_date:
    $ game.active_girl.set_flag("interact",1,1,"+")
    call expression game.active_girl.id+"_greet" from _call_expression_87
    show expression game.active_girl.id
    hero.say "About our date..."
    hero.say "I will not be able to make it."
    active_girl.say "Ok, don't worry."
    python:
        for d in hero.appointments.keys():
            for h in hero.appointments[d].keys():
                if game.active_girl.id in hero.appointments[d][h]:
                    hero.appointments[d][h].remove(game.active_girl.id)
                    game.active_girl.love -= 5
                    game.active_girl.set_flag("interact",1,1,"+")
                    renpy.hide((game.active_girl.id))
                    renpy.return_statement()
        renpy.hide((game.active_girl.id))
    return

label date_her:
    $ game.active_girl.set_flag("interact",1,1,"+")
    call expression game.active_girl.id+"_greet" from _call_expression_29
    show expression game.active_girl.id

    $ _return = False
    if renpy.has_label(game.active_girl.id+"_ask_date"):
        call expression game.active_girl.id+"_ask_date"
    else:
        hero.say "[game.active_girl.name], would you like to go on a date with me ?"
        if game.active_girl.love() < 50 or game.active_girl.get_flag_value("nodate"):
            active_girl.say "I am sorry [hero.name], I don't see you that way."
        else:
            active_girl.say "Sure, it might be fun, when do you want us to go ?"
            $ _return = True
    if _return:
        python:
            choices = []
            if game.hour == 20 or (game.hour == 14 and game.week_day in [6,7]):
                choices.append(("Now",("now",0)))
            if game.hour <20:
                if not(
                    hero.appointments.has_key(game.days_played)
                    and (
                        hero.appointments[game.days_played].has_key(14)
                            and game.active_girl.id in hero.appointments[game.days_played][14]
                        or hero.appointments[game.days_played].has_key(20)
                            and game.active_girl.id in hero.appointments[game.days_played][20]
                        )
                    ):
                    choices.append(("Today",(game.days_played,game.week_day)))
            if game.week_day != 7:
                if not(
                    hero.appointments.has_key(game.days_played+1)
                    and (
                        hero.appointments[game.days_played+1].has_key(14)
                            and game.active_girl.id in hero.appointments[game.days_played+1][14]
                        or hero.appointments[game.days_played+1].has_key(20)
                            and game.active_girl.id in hero.appointments[game.days_played+1][20]
                        )
                    ):
                    choices.append(("Tomorrow",(game.days_played+1,game.week_day+1)))
                start = 1
            else:
                if not(
                    hero.appointments.has_key(game.days_played+1)
                    and (
                        hero.appointments[game.days_played+1].has_key(14)
                            and game.active_girl.id in hero.appointments[game.days_played+1][14]
                        or hero.appointments[game.days_played+1].has_key(20)
                            and game.active_girl.id in hero.appointments[game.days_played+1][20]
                        )
                    ):
                    choices.append(("Tomorrow",(game.days_played+1,1)))
                start = 2
            if game.week_day + 2 <=7:
                
                for i in range(game.week_day+2,8):
                    if not(
                    hero.appointments.has_key(game.days_played-game.week_day+i)
                    and (
                        hero.appointments[game.days_played-game.week_day+i].has_key(14)
                            and game.active_girl.id in hero.appointments[game.days_played-game.week_day+i][14]
                        or hero.appointments[game.days_played-game.week_day+i].has_key(20)
                            and game.active_girl.id in hero.appointments[game.days_played-game.week_day+i][20]
                        )
                    ):
                        
                        choices.append(("Next "+game.get_day_str(i),(game.days_played-game.week_day+i,i)))
            if game.week_day > 1:
                
                for i in range(start,game.week_day):
                    
                    choices.append(("Next "+game.get_day_str(i),(game.days_played-game.week_day+i+7,i)))
            day, week_day = renpy.display_menu(choices)
            if day == "now":
                renpy.call("date")
            else:
                if (week_day in [6,7] and not game.days_played == day) or (week_day in [6,7] and game.days_played == day and game.hour < 14):
                    choices = [("Afternoon",14),("Evening",20)]
                    hour = renpy.display_menu(choices)
                else:
                    hour = 20
                
                
                
                
                s = "Let's do this "
                if day == game.days_played and hour == 20:
                    s += "tonight."
                elif day == game.days_played and hour == 14:
                    s += "this afternoon."
                elif day == game.days_played+1 and hour == 20:
                    s += "tomorrow night."
                elif day == game.days_played+1 and hour == 14:
                    s += "tomorrow afternoon."
                elif hour == 20:
                    s += "next "+game.get_day_str(week_day)+" evening."
                elif hour == 14:
                    s += "next "+game.get_day_str(week_day)+" afternoon."
                hero.say(s)
                hero.set_appointment(day,hour,game.active_girl.id)
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
