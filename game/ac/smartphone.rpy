init -15 python:
    Activity(**{
        "name": "smartphone",
        "duration": 0,
        "game_conditions": {
            "min_energy":1,
            "min_hunger":1,
            "min_grooming":1,
            "min_fun":1
            },
        "icon":"smartphone",
        "display_name": "Use smartphone",
        "label": ["use_smartphone"]
        })

label use_smartphone:
    show smartphone
    python:
        res = "Contacts"
        while res in ["Contacts","Agenda"]:
            hero.show_smartphone_info()
            res = renpy.call_screen("select",["Contacts","Calendar"],title = "smartphone")
            if res == "Contacts":
                contacts_temp = {}
                for girl in hero.smartphone_contacts:
                    if girl in GIRLS:
                        contacts_temp[girl] = []
                        if girl not in [ g.id for g in ROOMS[game.room].get_present_girls()] and girl not in HIDDEN:
                            actions = ["send_friendly_text","send_flirty_text","send_dirty_text","call","hint"]
                        else:
                            actions = []
                        if game.hour >= 20 and g not in ["bree", "sasha"] and game.room in ["bedroom1","bedroom2","bedroom3","bedroom4","bedroom5","kitchen","livingroom", "pool"]:
                            actions.append("booty_call")
                        for act in actions:
                            if GIRLS[girl].id+"_"+act not in DONE_DAY:
                                contacts_temp[girl].append(act.replace("_"," "))
                contacts = {}
                for girl in contacts_temp.keys():
                    if contacts_temp[girl]:
                        contacts[girl] = contacts_temp[girl]
                if contacts:
                    contact = renpy.call_screen("select",contacts.keys(),title = "contacts")
                    if contact != "None":
                        renpy.show_screen("show_smartphone_info", GIRLS[contact])
                        result2 = renpy.call_screen("select",contacts[contact],title = "action")
                        if result2 != "None":
                            renpy.hide(("smartphone"))
                            renpy.hide((GIRLS[contact].id))
                            result2 = result2.replace(" ","_")
                            DONE_DAY.append(GIRLS[contact].id+"_"+result2)
                            old_active_girl = game.active_girl
                            game.active_girl = GIRLS[contact]
                            if (renpy.has_label('smartphone_' + game.active_girl.id + '_' + result2)):
                                result2 = game.active_girl.id + '_' + result2
                            renpy.call_in_new_context("smartphone_" + result2)
                            game.active_girl = old_active_girl
                        renpy.hide((GIRLS[contact].id))
                        renpy.hide_screen("show_smartphone_info")
            elif res == "Calendar":
                renpy.call_screen("calendar")
    hide smartphone
    return

label smartphone_booty_call:
    hero.say "Wanna come over for a little fun?"
    if game.active_girl.love >= 150 and game.active_girl.sub >= 25 and game.active_girl.get_flag_value("sex") >= 1:
        game.active_girl.say "Sure"
        call expression game.active_girl.id+"_fuck_date"
    else:
        game.active_girl.say "No fucking way!"
        $ game.active_girl.love -= 1
        $ game.active_girl.sub -= 1
    return

label smartphone_send_friendly_text:
    python:
        t = randchoice(guy_friendly_texts)
        for index, line in enumerate(t):
            if line[0] == "guy":
                hero.say(line[1])
            else:
                active_girl.say(line[1])
            if index == 0:
                if game.active_girl.get_activity()[1]["activity"]=="sleep" and game.active_girl.love() < 70:
                    active_girl.say("Leave me alone, I was asleep...")
                    game.active_girl.love -=2
                    break
        else:
            hero.fun += 0.2
            game.active_girl.love += 1
        renpy.hide((game.active_girl.id))
        game.active_girl.set_flag("interact",1,1,"+")
    return

label smartphone_send_flirty_text:
    python:
        t = randchoice(guy_flirty_texts)
        for index, line in enumerate(t):
            if line[0] == "guy":
                hero.say(line[1])
            else:
                active_girl.say(line[1])
            if index == 0:
                if game.active_girl.get_activity()[1]["activity"]=="sleep" and game.active_girl.love() < 140:
                    active_girl.say("Leave me alone, I was asleep...")
                    game.active_girl.love -=2
                    break
        else:
            hero.fun += 0.3
            if (game.active_girl.love() <= 80 or not game.active_girl.get_flag_value("sex")) and not hero.charm >= 30:
                active_girl.say("Don't send me that kind of text, it's inappropriate.")
                game.active_girl.love +=1
            elif not game.active_girl.get_flag_value("sex") or (game.active_girl.love() <= 100 and not hero.charm >= 50):
                active_girl.say("Stop joking around ;)")
                game.active_girl.love += 1
            else:
                active_girl.say("you make me blush :$")
                game.active_girl.love += 1
        renpy.hide((game.active_girl.id))
        game.active_girl.set_flag("interact",1,1,"+")
    return

label smartphone_send_dirty_text:
    python:
        nbr = randint(1,4)
        t = randchoice(guy_dirty_texts)
        for index, line in enumerate(t):
            if line[0] == "guy":
                hero.say(line[1])
            else:
                active_girl.say(line[1])
            if index == 0:
                if game.active_girl.get_activity()[1]["activity"]=="sleep" and game.active_girl.love() < 140:
                    active_girl.say("Leave me alone, I was asleep...")
                    game.active_girl.love -=2
                    break
        else:
            if game.active_girl.love() <= 100 and not hero.charm >= 40 :
                active_girl.say("Don't send me that kind of text, it's inappropriate.")
                game.active_girl.love -= 2
            elif game.active_girl.get_flag_value("sex") < 2 or game.active_girl.love() <= 150:
                active_girl.say("Ok, I am horny now, what will you do about it ? :*")
                game.active_girl.love += 1
            else:
                active_girl.say("you make me so wet :$")
                game.active_girl.love += 2
            hero.fun += 0.2
        renpy.hide((game.active_girl.id))
        game.active_girl.set_flag("interact",1,1,"+")
    return

label smartphone_call:
    "I call [game.active_girl.name]"
    if (not randint(1,100) <= game.active_girl.love() and not hero.charm >= 40) or game.active_girl.get_activity()[1]["activity"]=="sleep" or game.active_girl.id in HIDDEN:
        "She doesn't pick up."
    else:
        active_girl.say "Yes?"
        python:
            choices = [("Chat",1),("Ask location",2)]
            dates = []
            for d in hero.appointments.keys():
                for h in hero.appointments[d].keys():
                    for i in hero.appointments[d][h]:
                        if not i in dates:
                            dates.append(i)
            if game.active_girl.id not in dates:
                choices.append(("Ask on a date",3))
            else:
                choices.append(("Cancel date",4))
            result = renpy.display_menu(choices)
        if result == 1:
            call expression game.active_girl.get_chat() from _call_expression_57
        elif result == 2:
            hero.say "Where are you ?"
            if game.active_girl.get_room().lower() != "none":
                if game.active_girl.love() >= 40:
                    $ smart_room = game.active_girl.get_room()
                    if smart_room in ["amusmentpark"]:
                        active_girl.say "I am at the amusment park."
                    elif smart_room in ["apartmentbuilding","bedroom1","bathroom","kitchen","pool","livingroom","secondfloor"]:
                        active_girl.say "I am at home."
                    elif smart_room in ["map"]:
                        active_girl.say "I am in the city."
                    elif smart_room in ["bookstore","bakery","clothesshop","arcade","flowershop","mall","publicpool","jewelrystore"]:
                        active_girl.say "I am at the mall."
                    elif smart_room in ["beach"]:
                        active_girl.say "I am at the beach."
                    elif smart_room in ["cinema"]:
                        active_girl.say "I am at the cinema."
                    elif smart_room in ["familyrestaurant","highclassrestaurant"]:
                        active_girl.say "I am at the restaurant."
                    elif smart_room in ["hospital","hospitalroom"]:
                        active_girl.say "I am at the hospital."
                    elif smart_room in ["gym","mma"]:
                        active_girl.say "I am at the gym."
                    elif smart_room in ["lounge"]:
                        active_girl.say "I am at the lounge."
                    elif smart_room in ["office","personaloffice"]:
                        active_girl.say "I am at work."
                    elif smart_room in ["onsen"]:
                        active_girl.say "I am on a little trip."
                    elif smart_room in ["park"]:
                        active_girl.say "I am at the park."
                    elif smart_room in ["station"]:
                        active_girl.say "I am at the train station."
                    elif smart_room in ["stripclub"]:
                        active_girl.say "I am at the stripclub."
                    elif smart_room in ["university","classroom","library"]:
                        active_girl.say "I am at the university."
                    elif smart_room in ["pub"]:
                        active_girl.say "I am at the pub."
                    elif smart_room in ["nightclub"]:
                        active_girl.say "I am at the nightclub."
                    elif smart_room in ["church"]:
                        active_girl.say "I am at the church."
                    elif smart_room in ["punkbar"]:
                        active_girl.say "I am at the punk bar downtown."
                    else:
                        active_girl.say "I think I am a little lost."
                else:
                    active_girl.say "I am quite sure this is not your problem."
            else:
                active_girl.say "Try to guess."
        elif result == 3:
            $ _return = False
            if renpy.has_label(game.active_girl.id+"_ask_date"):
                call expression game.active_girl.id+"_ask_date" from _call_expression_117
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
                    if (week_day in [6,7] and not game.days_played == day) or (week_day in [6,7] and game.days_played == day and game.hour < 14):
                        choices = [("Afternoon",14),("Evening",20)]
                        hour = renpy.display_menu(choices)
                    else:
                        hour = 20




                    s = "I'll pick you up "
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
        elif result == 4:
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
                            renpy.return_statement()
        $ game.active_girl.set_flag("interact",1,1,"+")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
