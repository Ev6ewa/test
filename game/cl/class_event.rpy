init -20 python:
    class Event(Shtick, store.object):
        def __init__(self,
                name = "",
                duration = 0,
                game_conditions = {},
                grooming = 0,
                fun = 0,
                hunger = 0,
                energy = 0,
                knowledge = 0,
                fitness = 0,
                charm = 0,
                money_cost = 0,
                money_gain = (),
                min_girls = 0,
                week_days = "1234567",
                label = None,
                action_params = None,
                valid = True,
                do_once = True,
                once_day = False,
                once_week = False,
                once_hour = True,
                display_name = "",
                girls_conditions = {},
                
                priority = 50,
                move = False,
                clothes = None,
                max_girls = "None",
                
                required_item = None,
                quit = True,
                conditions = [],
                bye = False,
                music = None,
                girl = None
                ):
            self.required_item = required_item
            self.id = name
            self.girl = girl
            self.bye = bye
            self.music = music
            self.once_hour = once_hour
            self.week_days = week_days
            self.last_day = 100
            self.last_hour = 25
            self.max_girls = max_girls
            self.move = move
            self.do_once = do_once
            self.priority = priority
            self.name = name
            self.display_name = display_name
            self.money_cost = money_cost
            self.money_gain = money_gain
            self.duration = duration
            self.needs = {"energy":energy, "grooming":grooming, "fun":fun,"hunger":hunger}
            self.attributes = {"knowledge":knowledge,"fitness":fitness,"charm":charm}
            self.conditions = conditions
            self.game_conditions = game_conditions
            
            self.min_girls = min_girls
            self.girls_conditions = girls_conditions
            self.quit = quit
            self.label = label
            self.say = []
            self.clothes = clothes
            self.once_day = once_day
            self.once_week = once_week
            EVENTS[self.id]=self

label event_do(do_event, debug=False):
    scene expression "bg "+game.room
    $ do_event.set_flag("activitycanceled",False)
    $ do_event.set_flag("canceled",False)
    if do_event.clothes:
        $ event_old_girl_clothes = game.girl_clothes
        $ game.girl_clothes = do_event.clothes
    if do_event.girl:
        $ game.active_girl = GIRLS[do_event.girl]
        $ bye_outfit = game.active_girl.get_clothes()
    if do_event.label:
        if isinstance(do_event.label,list):
            call expression do_event.label[0] pass (*do_event.label[1:]) from _call_expression_101
        else:
            call expression do_event.label from _call_expression_102
    if do_event.get_flag_value("canceled") == True:
        return
    if do_event.say:
        $ renpy.say("",randchoice(do_event.say))
    $ game.pass_time(do_event.duration, needs = True)
    if do_event.girl and do_event.bye and randint(0,(do_event.girl.love()+1)/10) != 0 and do_event.girl.room != game.room:
        call expression do_event.girl.id+"_bye" pass (bye_outfit=bye_outfit) from _call_expression_104
    python:
        for n in do_event.needs.keys():
            hero[n] += do_event.needs[n]
        for s in do_event.attributes.keys():
            if do_event.attributes[s] >= 1:
                hero[s] += do_event.attributes[s]
            elif do_event.attributes[s] and random() <= do_event.attributes[s]:
                hero[s] += 1
        if do_event.money_gain:
            base = 1
            for a in do_event.money_gain[0]:
                base += hero[a]()
            hero.money += base*do_event.money_gain[1]*do_event.duration
    if do_event.money_cost:
        $ hero.money -= do_event.money_cost
    if not do_event.name in DONE_HOUR:
        $ DONE_HOUR.append(do_event.name)
    if not do_event.name in DONE_WEEK:
        $ DONE_WEEK.append(do_event.name)
    if not do_event.name in DONE_MONTH:
        $ DONE_MONTH.append(do_event.name)
    if not do_event.name in DONE_DAY:
        $ DONE_DAY.append(do_event.name)
    if not do_event.name in DONE:
        $ DONE.append(do_event.name)
    if do_event.clothes:
        $ game.girl_clothes = event_old_girl_clothes
    if do_event.girl:
        $ game.active_girl = None
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
