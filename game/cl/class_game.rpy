init -15 python:
    class Game(Flagged, store.object):
        def __init__(self):
            self.hour = 10
            self.id = "GAME!"
            self.day = randint(1,31)
            self.season = randint(0,3)
            self.days_played = 0
            self.week = 1
            self.week_day = randint(1,5)
            self.event_move = ""
            
            self.girls_shown = []
            self.active_girl = None
            self.room = "office"
            self.from_room = "livingroom"
            self.set_flag("last_sleep",self.day, "permanent")
            
            
            self.talk_subjects = [
                "politics",
                "food",
                "travels",
                "tv",
                "sports",
                "fashion",
                "books",
                "people",
                "computers",
                "music",
                "love",
                "sex"
                ]
            self.girl_clothes = None
        
        def get_dates(self):
            
            result = []
            
            for date in DATES.values():
                if date.test():
                    result.append(date)
            
            return result
        
        def get_week_day(self):
            return self.week_day
        
        def smooth_talk(self,girl):
            renpy.show((girl.id))
            
            res = randint(1,100)
            if res <= 50 + hero.charm():
                if not self.get_flag_value("female"):
                    lines = good_pickup_lines
                else:
                    lines = girl_pickup_lines
                if hero.check_skill("video_games"):
                    if self.get_flag_value("female"):
                        lines += girl_nerdy_pickup_lines
                    else:
                        lines += nerdy_pickup_lines
                result = randchoice(lines)
                for l in result:
                    if l[0] == "girl":
                        girl.say(l[1].replace("[girlname]",girl.name))
                    else:
                        hero.say(l[1].replace("[girlname]",girl.name))
                girl.love += 1
            elif res <= 80 + hero.charm():
                if game.get_flag_value("female"):
                    renpy.say("","I don't know what to say...")
                else:
                    renpy.say("", "I can't find anything smooth to say...")
                    renpy.say("", "Maybe I should work on my pickup lines...")
            else:
                if not self.get_flag_value("female"):
                    result = randchoice(bad_pickup_lines)
                else:
                    result = randchoice(girl_bad_pickup_lines)
                for l in result:
                    if l[0] == "girl":
                        girl.say(l[1].replace("[girlname]",girl.name))
                    else:
                        hero.say(l[1].replace("[girlname]",girl.name))
                if game.get_flag_value("female"):
                    renpy.say("","And once again I make a fool of myself...")
                    renpy.say("","Good job...")
                else:
                    renpy.say("", "Fuck that was stupid to say, she must be so pissed off...")
                    renpy.say("", "Maybe I should work on my pickup lines...")
                girl.love -= 1
            renpy.hide((girl.id))
        
        def test_time(self,test,val):
            if test == "<":
                if game.hour < val+1:
                    return True
                else:
                    renpy.say("","I don't have enough time for this.")
                    return False
        
        def get_season(self,nbr = 4):
            if nbr > 3 or nbr < 0:
                return SEASONS[game.season]
            else:
                return SEASONS[nbr]
        
        def get_day_str(self,nbr = 4):
            if nbr > 7 or nbr < 1:
                return DAYS[game.week_day-1]
            else:
                return DAYS[nbr-1]
        
        def new_week(self):
            chores = self.get_flag_value("chores")
            if not chores >= 100:
                if bree.sub <= 25:
                    bree.love -= 10
                elif bree.love <= 50:
                    bree.love -= 10
                if sasha.sub <= 25:
                    sasha.love -= 10
                elif sasha.love <= 50:
                    sasha.love -= 10
                if game.get_flag_value("female"):
                    renpy.say("", "I didn't do my chores, my roommates will be mad...")
                else:
                    renpy.say("", "I didn't do my chores, the girls will be mad...")
            self.new_day()
        
        def new_day(self):
            
            valid_events = []
            self.clean_up()
            hero.activity = "wake_up"
            for e in EVENTS.values():
                if e.test() and e.game_conditions.get("activity","None") == "wake_up":
                    valid_events.append(e)
            if valid_events:
                for ev in valid_events:
                    renpy.call_in_new_context("event_do",ev)
            for g in GIRLS.values():
                if self.get_season() == g.birthday[0] and self.day == g.birthday[1] and g.get_flag_value("birthdayknown") and g.id not in HIDDEN:
                    renpy.say("","It's "+g()+"'s birthday.")
            if self.get_season() == "spring" and self.day == 14:
                renpy.say("","It's valentine's day.")
            elif self.get_season() == "winter" and self.day == 25:
                renpy.say("","It's christmas.")
            elif self.get_season() == "spring" and self.day == 1:
                renpy.say("","It's new year's day.")
            elif self.get_season() == "summer" and self.day == 4:
                renpy.say("","It's independence day.")
            elif self.get_season() == "fall" and self.day == 31:
                renpy.say("","It's halloween.")
            if self.get_season() == hero.birthday[0] and self.day == hero.birthday[1]:
                renpy.say("","It's my birthday.")
            hero.activity = ""
            for girl in GIRLS.values():
                girl.increment_counters()
        
        def update_rooms():
            for r in ROOMS.values():
                r.present_girls = []
            for girl in GIRLS.values():
                girl.set_room()
        
        def pass_time(self, duration=1, needs = False):
            if duration:
                del DONE_HOUR[:]
                self.hour = int(self.hour+duration)
                if self.hour >= 24:
                    del DONE_DAY[:]
                    self.hour = self.hour-24
                    old_day = self.days_played
                    if self.get_flag_value("worksatisfaction") and not self.get_flag_value("hasworked") and self.week_day <= 5:
                        self.set_flag("worksatisfaction",1,mod="-")
                    self.day += 1
                    self.days_played += 1
                    self.week_day += 1
                    if self.week_day > 7:
                        del DONE_WEEK[:]
                        self.week_day = 1
                    if self.day > 31:
                        del DONE_MONTH[:]
                        self.day = 1
                        self.season +=1
                        if self.season > 3:
                            self.season = 0
                    if hero.appointments.has_key(old_day):
                        for k in hero.appointments[old_day]:
                            for g in hero.appointments[old_day][k]:
                                if g in GIRLS and not (game.get_flag_value("dateinprogress") and game.get_flag_value("dateinprogress").id == g): 
                                    GIRLS[g].love -= 10
                                    renpy.say("", "Shit I missed my date with "+GIRLS[g].name+".")
                        del hero.appointments[old_day]
                if game.hour >= 6:
                    if game.get_flag_value("last_reset") != game.day and game.week_day == 1 and game.days_played > 0:
                        game.new_week()
                        game.set_flag("last_reset", game.day)
                    elif game.get_flag_value("last_reset") != game.day and game.days_played > 0:
                        game.new_day()
                        game.set_flag("last_reset", game.day)
                
                
                if needs:
                    
                    hero.hunger -= duration*1
                    
                    hero.grooming -= duration*0.3
                    hero.fun -= duration*0.5
                    
                    hero.energy -= duration*0.4
            
            
            for r in ROOMS.values():
                r.present_girls = []
            for girl in GIRLS.values():
                girl.set_room()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
