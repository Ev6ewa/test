label date:
    $ game.set_flag("dateinprogress",game.active_girl)
    $ date_girl = game.active_girl














    if game.hour in [14,20]:
        $ dif = 20
    elif game.hour in [15,21]:
        $ dif = 30
        $ date_girl.love -= 1
    elif game.hour in [16,22]:
        $ dif = 40
        $ date_girl.love -= 2
    elif game.hour in [17,23]:
        $ dif = 50
        $ date_girl.love -= 3
    $ date_stay = True
    $ afternoon = False
    $ evening = False
    $ diner = False
    $ night = False
    while date_stay:
        $ game.active_girl = game.get_flag_value("dateinprogress")
        scene bg street

        if game.hour in [14, 15, 16, 17] and not afternoon:
            $ afternoon = True
            show expression game.get_flag_value("dateinprogress").id +" casual"
            $ dif += 25
            call choose_and_do_date from _call_choose_and_do_date
        elif game.hour == 18 and game.get_flag_value("datescore") >= dif and not evening:
            $ evening = True
            show expression game.get_flag_value("dateinprogress").id +" casual"

            $ dif += 25
            date_girl.say "I really don't want to end things right now, maybe we can do something else?"
            menu:
                "Yes":
                    hero.say "Sure, I would love to."
                    $ game.pass_time(2)
                    call choose_and_do_date from _call_choose_and_do_date_1
                "No":
                    hero.say "Sorry I don't have time."
                    $ date_stay = False
        elif game.hour in [20, 21, 22, 23] and not diner:
            $ diner = True
            show expression game.get_flag_value("dateinprogress").id +" casual"

            $ dif += 25
            call choose_and_do_date from _call_choose_and_do_date_2
        elif game.hour >= 0 and game.week_day in [6,7] and game.get_flag_value("datescore") >= dif and not night:
            $ night = True
            show expression game.get_flag_value("dateinprogress").id

            date_girl.say "What do you say we end this at the club?"
            if "nightclub" in DATES and DATES["nightclub"].test():
                menu:
                    "Yes":
                        hero.say "Sure, I would love to."
                        call date_do (DATES["nightclub"], game.get_flag_value("dateinprogress")) from _call_date_do
                    "No":
                        hero.say "Sorry I don't have time."
            else:
                hero.say "Sorry, don't feel like it."

                $ date_stay = False
        else:
            show expression game.get_flag_value("dateinprogress").id
            if not game.get_flag_value("female"):
                $ _return = False
                if renpy.has_label(game.get_flag_value("dateinprogress").id+"_ask_fuck_date"):
                    call expression game.get_flag_value("dateinprogress").id+"_ask_fuck_date"
                else:
                    if (game.get_flag_value("datescore") >= (100 - game.get_flag_value("dateinprogress").get_flag_value("drinks")*5)
                        and renpy.has_label(game.get_flag_value("dateinprogress").id+"_fuck_date")):
                        date_girl.say "Maybe I could, you know..."
                        date_girl.say "Come for a hot coffee."
                        hero.say "I would love that."
                        $ _return = True
                    else:
                        date_girl.say "It was really nice."
                if _return:
                    hide expression game.get_flag_value("dateinprogress").id
                    call expression game.get_flag_value("dateinprogress").id+"_fuck_date" from _call_expression_95
            else:
                if game.get_flag_value("datescore") >= 100:
                    $ game.get_flag_value("dateinprogress").set_flag("datenumber", 1, mod = "+")
                if ((game.get_flag_value("datescore") >= (100 - game.get_flag_value("dateinprogress").get_flag_value("drinks")*5) 
                    or game.get_flag_value("dateinprogress").love >= 150
                    or game.get_flag_value("dateinprogress").get_flag_value("sex"))
                    and renpy.has_label(game.get_flag_value("dateinprogress").id+"_fuck_date_female")):
                    date_girl.say "What do you say we end that at my place?"
                    if (game.get_flag_value("morality") <= -50
                        or game.get_flag_value("morality") <= -25 and game.get_flag_value("dateinprogress").get_flag_value("datenumber") >= 1
                        or game.get_flag_value("morality") <= 0 and game.get_flag_value("dateinprogress").get_flag_value("datenumber") >= 2
                        or game.get_flag_value("morality") <= 25 and game.get_flag_value("dateinprogress").get_flag_value("datenumber") >= 3
                        or game.get_flag_value("morality") <= 50 and game.get_flag_value("dateinprogress").get_flag_value("datenumber") >= 4
                        or game.get_flag_value("morality") <= 75 and game.get_flag_value("dateinprogress").get_flag_value("datenumber") >= 6):
                        hero.say "I would love that."
                        hide expression game.get_flag_value("dateinprogress").id
                        call expression game.get_flag_value("dateinprogress").id+"_fuck_date_female" from _call_expression_112
                    else:
                        hero.say "Maybe some other time."
                else:
                    date_girl.say "See you around."
            $ date_stay = False
        hide expression game.get_flag_value("dateinprogress").id
    $ game.set_flag("dateinprogress",val=False)
    $ game.set_flag("currentdate",None,"day")


    return

label choose_and_do_date:
    python:
        renpy.show(("bg street"))
        spots = game.get_dates()

        spot = "None"
        if spots:
            n_spots = []
            for spot in spots:
                n_spots.append((spot.display_name,spot))
            spot = renpy.call_screen("select",n_spots, "date spots")
            renpy.hide((game.get_flag_value("dateinprogress").id))
        else:
            renpy.say("","There is no dating place I could or would take her to right now.")
            result = "None"

    if spot != "None":
        python:
            day = game.days_played
            hour = game.hour
            game.set_flag("currentdate",spot.name,"day")
        call date_do (spot, game.get_flag_value("dateinprogress")) from _call_date_do_1
    else:

        if hero.activity:
            $ hero.activity.set_flag("canceled",True)
    return

label time_for_our_date:
    show expression game.active_girl.id
    active_girl.say "Let's go on our date [hero.name]."
    menu:
        "Yes":
            hero.say "Ok."
            call date from _call_date_3
        "No":
            hero.say "Sorry I don't have time."
    hide expression game.active_girl.id
    $ game.room = "livingroom"
    return

label ask_out:
    if renpy.has_label(game.active_girl.id+"_ask_out"):
        call expression game.active_girl.id+"_ask_out" from _call_expression
    else:
        call expression game.active_girl.id+"_greet" from _call_expression_1
        python:
            renpy.show(game.active_girl.id)
            choices = []
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
                    choices.append(("today",(game.days_played,game.week_day)))
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
                    choices.append(("tomorrow",(game.days_played+1,game.week_day+1)))
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
                    choices.append(("tomorrow",(game.days_played+1,1)))
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
                        
                        choices.append(("next "+game.get_day_str(i).lower(),(game.days_played-game.week_day+i,i)))
            if game.week_day > 1:
                
                for i in range(start,game.week_day):
                    
                    choices.append(("Next "+game.get_day_str(i).lower(),(game.days_played-game.week_day+i+7,i)))
            result = randchoice(choices)
            day = result[1][0]
            week_day = result[1][1]
            if (week_day in [6,7] and not game.days_played == day) or (week_day in [6,7] and game.days_played == day and game.hour < 14):
                choices = [("afternoon",14),("evening",20)]
                hour = randchoice(choices)
            else:
                hour = ("evening",20)
        if result[0] == "today":
            $ str_day = "this"
        else:
            $ str_day = result[0]
        active_girl.say "Would you like to go somewhere with me [str_day] [hour[0]]?"
        $ choices = [("Yes",1),("No",2)]
        if renpy.display_menu(choices) == 1:
            hero.say "Sure."
            $ hero.set_appointment(day,hour[1],game.active_girl.id)
            $ game.active_girl.love += 1
        else:
            hero.say "Sorry, I don't feel like it."
            $ game.active_girl.love -=1
        hide expression game.active_girl.id
    return

label are_you_sick:
    call expression game.active_girl.id+"_greet" from _call_expression_8
    show expression game.active_girl.id
    active_girl.say "You don't look so well..."
    active_girl.say "You should rest."
    $ game.active_girl.love += 1
    hide expression game.active_girl.id
    return

label auto_chat:
    if renpy.has_label(game.active_girl.id+"_auto_chat"):
        call expression game.active_girl.id+"_auto_chat" from _call_expression_9
    else:
        call expression game.active_girl.id+"_greet" from _call_expression_10
        show expression game.active_girl.id
        active_girl.say "Do you have some time to talk ?"
        $ choices = [("No, sorry.",1),("Yeah, sure",2)]
        $ result = renpy.display_menu(choices)
        if result == 1:
            $ game.active_girl.love +=1
        else:
            $ game.active_girl.set_flag("daily_interact",1,1, "+")
            $ chat = game.active_girl.get_chat()
            show expression game.active_girl.id
            call expression chat from _call_expression_11
        $ renpy.hide((game.active_girl.id))
    return

label auto_greet:
    if renpy.has_label(game.active_girl.id+"_auto_greet"):
        call expression game.active_girl.id+"_auto_greet" from _call_expression_12
    else:
        show expression game.active_girl.id
        call expression game.active_girl.id+"_greet" from _call_expression_13
        $ renpy.hide((game.active_girl.id))
    return

label send_text:
    play sound "sd/cell_vibrate.mp3"
    pause 1.0
    "It's a text from [game.active_girl.name]."
    python:
        if game.get_flag_value("dateinprogress"):
            result = renpy.display_menu([("Ignore it",1),("Read it",2)])
            if result == 1:
                game.active_girl.love +=1
                renpy.return_statement()
        result = randint(0,game.active_girl.love())
        renpy.show_screen("show_smartphone_info", game.active_girl)
        if result >= 150 and game.active_girl.get_flag_value("sex") >= 1:
            t = randchoice(girl_dirty_texts)
            for line in t:
                if line[0] == "guy":
                    hero.say(line[1])
                else:
                    active_girl.say(line[1])
            game.active_girl.love +=2
        elif result >= 75 and game.active_girl.get_flag_value("kiss") >= 1:
            t = randchoice(girl_flirty_texts)
            for line in t:
                if line[0] == "guy":
                    hero.say(line[1])
                else:
                    active_girl.say(line[1])
            game.active_girl.love +=1
        else:
            t = randchoice(girl_friendly_texts)
            for line in t:
                if line[0] == "guy":
                    hero.say(line[1])
                else:
                    active_girl.say(line[1])
            game.active_girl.love += 1

        renpy.hide_screen("show_smartphone_info")
    return

label give_phone_number:
    if renpy.has_label(game.active_girl.id+"_give_phone_number"):
        call expression game.active_girl.id+"_give_phone_number" from _call_expression_14
    else:
        call expression game.active_girl.id+"_greet" from _call_expression_15
        show expression game.active_girl.id
        active_girl.say "We should exchange our phone numbers."
        hero.say "Sure."
        $ hero.smartphone_contacts.append(game.active_girl.id)
        hide expression game.active_girl.id
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
