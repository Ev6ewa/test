init -20 python:
    class Activity(Shtick, store.object):
        def __init__(self,
                name,
                duration = 1,
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
                max_girls = 100,
                label = None,
                
                once_day = False,
                once_week = False,
                once_month = False,
                display_name = "",
                
                game_conditions = {},
                girls_conditions = {},
                once_hour = False,
                required_item = None,
                say = [],
                action = {"action":None,"parameter":None},
                conditions = [],
                bye = True,
                music = None,
                do_once = False,
                icon = None
                ):
            self.name = name
            self.id = self.name
            self.bye = bye
            self.music = music
            self.do_once = do_once
            self.required_item = required_item
            self.display_name = display_name if display_name else name.capitalize()
            self.money_cost = money_cost
            self.money_gain = money_gain
            self.duration = duration
            self.action = action
            self.needs = {"energy":energy, "grooming":grooming, "fun":fun,"hunger":hunger}
            self.attributes = {"knowledge":knowledge,"fitness":fitness,"charm":charm}
            self.once_day = once_day
            self.once_week = once_week
            self.once_month = once_month
            self.once_hour = once_hour
            
            
            self.conditions = conditions
            self.game_conditions = {"min_energy":1,"min_hunger":1,"min_grooming":1,"min_fun":1}
            self.game_conditions.update(game_conditions)
            self.girls_conditions = girls_conditions
            self.min_girls = min_girls
            self.max_girls = max_girls
            self.label = label
            self.say = say
            self.tooltip = ""
            self.icon = icon
            ACTIVITIES[self.name]=self
        
        def get_tooltip(self):
            
            tt = []
            for n in self.needs:
                
                if self.needs[n] > 0:
                    s = "+"
                else:
                    s = ""
                t = "{image=ui/icon_"+n+"_white.png}"+s
                x = self.needs[n]
                if n == "hunger":
                    x -= self.duration*1
                elif n == "grooming":
                    x -= self.duration*0.3
                elif n == "fun":
                    x -= self.duration*0.5
                elif n == "energy":
                    x -= self.duration*0.4
                rnd = 0
                rnd, x = modf(x)
                if persistent.randomness == 2:
                    chances = str(int(abs(rnd*100)))+"%"
                    if rnd > 0.:
                        t += "("+str(int(x))+"/"+chances+"→"+str(int(x+1))+")"
                    elif rnd < 0.:
                        t += "("+str(int(x))+"/"+chances+"→"+str(int(x-1))+")"
                    else:
                        t += str(int(x))
                else:
                    if not rnd:
                        t += str(int(x))
                    else:
                        t += str(x+rnd)
                if x != 0 or rnd != 0:
                    tt.append(t)
            for a in self.attributes:
                if self.attributes[a] != 0:
                    if self.attributes[a] > 0:
                        s = "+"
                    else:
                        s = ""
                    t = "{image=ui/icon_"+a+".png}"+s
                    x = self.attributes[a]
                    if persistent.difficulty == 0 and x > 0:
                        x = int(x*1.5)
                    elif persistent.difficulty == -1 and x > 0:
                        x = x*2
                    rnd, x = modf(x)
                    chances = str(int(abs(rnd*100)))+"%"
                    if rnd:
                        t += "("+str(int(x))+"/"+chances+"→"+str(int(x+1))+")"
                    else:
                        t += str(int(x))
                    tt.append(t)
            if self.money_cost:
                tt.append("{image=ui/icon_money.png}"+"-"+str(self.money_cost)+"$")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            elif self.money_gain:
                if persistent.difficulty == 1:
                    mult = 2
                else:
                    mult = 4
                base = 5
                for i in self.money_gain[1]:
                    if isinstance(i, (str, unicode)):
                        base += game.get_flag_value(i)
                    else:
                        base *= i
                for a in self.money_gain[0]:
                    base *= 1+(hero[a]()/100.)
                m = int(base*self.duration*mult)
                tt.append("{image=ui/icon_money.png}"+"+"+str(m)+"$")
            if self.duration:
                tt.append("{image=ui/icon_clock.png}"+"+"+str(self.duration)+"h")
            if self. tooltip:
                tt = [self.tooltip] + tt
            return tt
        
        
        def get_events(self):
            valid_events = []
            if self.get_flag_value("last_test") != str(game.hour)+" "+str(game.days_played):
                self.set_flag("last_test",str(game.hour)+" "+str(game.days_played),"day")
                for e in EVENTS.values():
                    if e.test():
                        valid_events.append(e)
            return valid_events

label activity_do(do_activity):
    scene expression "bg "+game.room

    python:
        if game.get_flag_value("dateinprogress"):
            game.active_girl = game.get_flag_value("dateinprogress")
        do_activity.set_flag("canceled",False)
        do_activity.set_flag("replaced",False)
        do_activity.set_flag("endevent",False)
        hero.activity = do_activity

    $ activity_valid_events = sorted(do_activity.get_events(), key=lambda event: event.priority)
    while activity_valid_events:
        $ activity_e = activity_valid_events.pop()
        call event_do (activity_e) from _call_event_do
        if game.room != room.id or activity_e.quit:
            $ activity_valid_events = []

    if game.get_flag_value("dateinprogress"):
        $ game.active_girl = game.get_flag_value("dateinprogress")
    if not do_activity.get_flag_value("canceled"):
        if not do_activity.get_flag_value("replaced"):
            if do_activity.label:
                $ lab = list(do_activity.label)
                if game.active_girl:
                    $ lab[0] = lab[0].replace("ACTIVE_GIRL",game.active_girl.id)
                if game.room:
                    $ lab[0] = lab[0].replace("ROOM",game.room)
                if renpy.has_label(lab[0]):
                    call expression lab[0] pass (*lab[1:]) from _call_expression_103
            elif do_activity.say:
                $ renpy.say("",randchoice(do_activity.say))
        if not do_activity.get_flag_value("canceled"):
            if do_activity.duration:
                $ game.pass_time(do_activity.duration)
            python:
                for n, v in do_activity.needs.items():
                    
                    if n == "hunger":
                        v -= do_activity.duration*1
                    elif n == "grooming":
                        v -= do_activity.duration*0.3
                    elif n == "fun":
                        v -= do_activity.duration*0.5
                    elif n == "energy":
                        v -= do_activity.duration*0.5
                    hero[n] += v


                for s, v in do_activity.attributes.items():
                    hero[s] += v
                if do_activity.money_gain:
                    if persistent.difficulty == 1:
                        mult = 2
                    else:
                        mult = 4
                    base = 5
                    for i in do_activity.money_gain[1]:
                        if isinstance(i, (str, unicode)):
                            base += game.get_flag_value(i)
                        else:
                            base *= i
                    for a in do_activity.money_gain[0]:
                        base *= 1+(hero[a]()/100.)
                    hero.money += int(base*do_activity.duration*mult)
                if do_activity.money_cost:
                    hero.money -= do_activity.money_cost
                if not do_activity.name in DONE_HOUR:DONE_HOUR.append(do_activity.name)
                if not do_activity.name in DONE_WEEK:DONE_WEEK.append(do_activity.name)
                if not do_activity.name in DONE_MONTH:DONE_MONTH.append(do_activity.name)
                if do_activity.once_day == "ACTIVE_GIRL" and game.active_girl:
                    DONE_DAY.append(do_activity.name+"_"+game.active_girl.id)
                elif not do_activity.name in DONE_DAY:
                    DONE_DAY.append(do_activity.name)
                if not do_activity.name in DONE:DONE.append(do_activity.name)
    $ hero.activity = None
    $ game.active_girl = None
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
