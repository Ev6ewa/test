init -25 python:
    class Shtick(Flagged):
        def play_music(self):
            if hasattr(self, "music") and not renpy.music.get_playing() == self.music:
                renpy.music.play(self.music,loop=True)
        
        def test(self,debug=False):
            if debug: print "----Testing "+self.name
            
            
            
            if isinstance(self,Equip) and self.name in hero.inventory:
                return False
            if hasattr(self, 'once_day'):
                if self.once_day == "ACTIVE_GIRL" and game.active_girl and self.name+"_"+game.active_girl.id in DONE_DAY:
                    if debug: print "already done today"
                    return False
                elif self.once_day and self.name in DONE_DAY:
                    if debug: print "already done today"
                    return False
            if hasattr(self, 'once_month') and self.once_month and self.name in DONE_MONTH:
                if debug: print "already done this month"
                return False
            if hasattr(self, 'once_week') and self.once_week and self.name in DONE_WEEK:
                if debug: print "already done this week"
                return False
            if hasattr(self, 'once_hour') and self.once_hour and self.name in DONE_HOUR:
                if debug: print "already done this hour"
                return False
            if hasattr(self, 'do_once') and self.do_once and self.name in DONE:
                if debug: print "already done"
                return False
            if hasattr(self, 'min_girls') and self.min_girls:
                if self.min_girls > len(ROOMS[game.room].get_present_girls()):
                    if debug: print "Not enough girls."
                    return False
            if hasattr(self, 'max_girls') and self.max_girls < len(ROOMS[game.room].get_present_girls()):
                if debug: print "Too many girls."
                return False
            if hasattr(self, 'money_cost') and self.money_cost > 0 and not hero.money >= self.money_cost and not isinstance(self, Item):
                if debug: print "Too expensive."
                return False
            if hasattr(self, 'required_item') and self.required_item != None:
                if "not_" in self.required_item and self.required_item.replace("not_","") in hero.inventory.keys():
                    return False
                elif self.required_item not in hero.inventory.keys():
                    return False
            
            
            
            if hasattr(self, 'duration') and not isinstance(self,Date):
                if isinstance(self,Room):
                    h0 = self.hours[0]
                    h1 = self.hours[1]
                else:
                    h0 = ROOMS[game.room].hours[0]
                    h1 = ROOMS[game.room].hours[1]
                if h1 > h0:
                    if game.hour + self.duration > h1:
                        if debug: print "too little time(1)."
                        return False
                else:
                    if game.hour + self.duration > h1 and game.hour + self.duration < h0:
                        if debug: print "too little time(2)."
                        return False
                    elif game.hour + self.duration < h0 and game.hour + self.duration > h1:
                        if debug: print "too little time(3)."
                        return False
            for c in self.conditions:
                if not eval(c):
                    return False  
            
            for g in self.girls_conditions.keys():
                if debug: print "Checking "+g
                if debug: print str(GIRLS.keys())
                if g == "ACTIVE" and not game.active_girl:
                    return False
                elif g == "ACTIVE":
                    tested_girl = game.active_girl
                elif g not in GIRLS:
                    return False
                else:
                    tested_girl = GIRLS[g]
                for c in self.girls_conditions[g].keys():
                    if debug: print "Checking "+g+"/"+c
                    if debug: print ",".join(self.girls_conditions[g].keys())
                    if c == "date_planned":
                        dates = []
                        if debug: print str(hero.appointments)
                        for d in hero.appointments.keys():
                            for h in hero.appointments[d].keys():
                                for i in hero.appointments[d][h]:
                                    if not i in dates:
                                        dates.append(i)
                        if self.girls_conditions[g][c] != (g in dates):
                            return False
                    elif c =="not":
                        if tested_girl.id == self.girls_conditions[g][c]:
                            return False
                    elif c =="active":
                        if (game.active_girl == tested_girl) != self.girls_conditions[g][c]:
                            return False
                    elif c =="birthday":
                        if SEASONS.index(tested_girl.birthday[0]) != game.season or game.day != tested_girl.birthday[1]:
                            return False
                    elif c == "validappointment":
                        if game.hour in [14,15,16]:
                            h = 14
                        elif game.hour in [20,21,22]:
                            h = 20
                        else:
                            h = game.hour
                        if hero.appointments.has_key(game.days_played) and hero.appointments[game.days_played].has_key(h):
                            appointments = hero.appointments[game.days_played][h]
                        else:
                            appointments = []
                        if not g in appointments:
                            return False
                    elif c == "clothes":
                        if not tested_girl.get_clothes() in self.girls_conditions[g][c]:
                            return False
                    elif c == "status":
                        if tested_girl.get_status() != self.girls_conditions[g][c]:
                            return False
                    elif c == "not_status":
                        if tested_girl.get_status() == self.girls_conditions[g][c]:
                            return False
                    elif c =="birthday":
                        if SEASONS.index(girl.birthday[0]) != game.season or game.day != girl.birthday[1]:
                            return False
                    elif "activity" in c:
                        if "not" in c:
                            if tested_girl.get_activity()[1]["activity"] in self.girls_conditions[g][c]:
                                if debug: print g+" doing "+str(self.girls_conditions[g][c])
                                return False
                        else:
                            if tested_girl.get_activity()[1]["activity"] not in self.girls_conditions[g][c] :
                                if debug: print g+" not doing "+str(self.girls_conditions[g][c])
                                return False
                    elif c == "room":
                        if not tested_girl.get_room() or not tested_girl.get_room() in self.girls_conditions[g][c]:
                            if debug: print g+" not in "+str(self.girls_conditions[g][c])
                            return False
                    elif c == "not_room":
                        if self.girls_conditions[g][c] == tested_girl.get_room():
                            if debug: print g+" in "+c
                            return False
                    elif c == "contact":
                        if debug: print "testing contact"
                        
                        
                        if debug: print g
                        if debug: print c
                        if debug: print str(self.girls_conditions[g][c])
                        if g == "ACTIVE" and game.active_girl:
                            tg = game.active_girl.id
                        else:
                            tg = g
                        if self.girls_conditions[g][c]:
                            if tg not in hero.smartphone_contacts:
                                if debug: print g+" not in contact"
                                return False
                        else:
                            if tg in hero.smartphone_contacts:
                                if debug: print g+" in contact"
                                return False
                    elif c == "not_clothes":
                        if tested_girl.get_clothes() in self.girls_conditions[g][c]:
                            return False
                    elif c == "valid":
                        if not (tested_girl.id in HIDDEN) != self.girls_conditions[g][c]:
                            if debug: print g+" wrong validity"
                            return False
                    
                    
                    
                    
                    elif c == "present":
                        if game.room != tested_girl.get_room() and self.girls_conditions[g][c]:
                            if debug: print "Not present"
                            return False
                        elif game.room == tested_girl.get_room() and not self.girls_conditions[g][c]:
                            if debug: print "Present"
                            return False
                    else:
                        t = c.rsplit("_")[0]
                        stat = "_".join(c.rsplit("_")[1:])
                        if stat == "love":
                            score = tested_girl.love()
                        elif stat == "sub":
                            score = tested_girl.sub()
                        elif "flag" in t:
                            comp = t.replace("flag","")
                            flag = tested_girl.get_flag_value(stat)
                            if debug: print "Testing flag :"+stat
                            if not comp or comp == "eq":
                                if flag !=  self.girls_conditions[g][c]:
                                    if debug: print "flag "+stat+" not set at the right value "+str(flag)+" should be "+str(self.girls_conditions[g][c])
                                    return False
                            elif comp == "min":
                                if flag <  self.girls_conditions[g][c]:
                                    if debug: print "flag "+stat+" too low "+str(flag)+"/"+str(self.girls_conditions[g][c])
                                    return False
                            elif comp == "max":
                                if flag >  self.girls_conditions[g][c]:
                                    if debug: print "flag "+stat+" too high "+str(flag)+"/"+str(self.girls_conditions[g][c])
                                    return False
                        elif "counter" in t:
                            comp = t.replace("counter","")
                            counter = tested_girl.get_counters(stat)
                            if debug: print "Testing counter :"+stat
                            if not comp or comp == "eq":
                                if counter !=  self.girls_conditions[g][c]:
                                    if debug: print "counter "+stat+" not set at the right value "+str(counter)+" should be "+str(self.girls_conditions[g][c])
                                    return False
                            elif comp == "min":
                                if counter <  self.girls_conditions[g][c]:
                                    if debug: print "counter "+stat+" too low "+str(counter)+"/"+str(self.girls_conditions[g][c])
                                    return False
                            elif comp == "max":
                                if counter >  self.girls_conditions[g][c]:
                                    if debug: print "counter "+stat+" too high "+str(counter)+"/"+str(self.girls_conditions[g][c])
                                    return False
                        if t == "min":
                            if score < self.girls_conditions[g][c]:
                                if debug: print g+" not enough "+stat
                                return False
                        elif t == "max":
                            if score > self.girls_conditions[g][c]:
                                if debug: print g+" too much "+stat
                                return False
            if debug: print "Checking game conditions"
            if debug: print str(self.game_conditions.keys())
            if "activity" in self.game_conditions.keys():
                a = hero.activity
                if not a:
                    if debug: print "no activity"
                    return False
                if not isinstance(a, str) and not isinstance(a, unicode):
                    a = a.name
                if not a in self.game_conditions["activity"]:
                    if debug: print a+" not in "+str(self.game_conditions["activity"])
                    if debug: print "wrong activity"
                    return False
            elif hero.activity and isinstance(self, Event):
                return False
            for c in self.game_conditions.keys():
                if debug: print "Checking game_condition "+c
                if c == "activity":
                    pass
                elif c == "not_valid":
                    if self.game_conditions[c] in ACTIVITIES:
                        if ACTIVITIES[self.game_conditions[c]].test():
                            return False
                    elif self.game_conditions[c] in EVENTS:
                        if EVENTS[self.game_conditions[c]].test():
                            return False
                    else:
                        return False
                elif c == "valid":
                    if self.game_conditions[c] in ACTIVITIES:
                        if not ACTIVITIES[self.game_conditions[c]].test():
                            return False
                    elif self.game_conditions[c] in EVENTS:
                        if not EVENTS[self.game_conditions[c]].test():
                            return False
                    else:
                        return False
                elif c == "not_done":
                    if self.game_conditions[c] in DONE:
                        return False
                elif c == "done":
                    if isinstance(self.game_conditions[c],list):
                        for i in self.game_conditions[c]:
                            if not i in DONE:
                                return False
                    else:
                        if not self.game_conditions[c] in DONE:
                            return False
                elif c[:4] == "var_":
                    if not eval(c.replace("var_","")+"==True"):
                        return False
                elif c == "seasons":
                    if str(game.season) not in self.game_conditions[c]:
                        return False
                elif c == "skill":
                    if self.game_conditions[c] not in hero.skills:
                        return False
                elif c == "not_skill":
                    if self.game_conditions[c] in hero.skills:
                        return False
                elif c == "validappointment":
                    if debug: print str(hero.appointments)
                    if game.hour in [14,15,16]:
                        h = 14
                    elif game.hour in [20,21,22]:
                        h = 20
                    else:
                        h = game.hour
                    appointments = []
                    if hero.appointments.has_key(game.days_played) and hero.appointments[game.days_played].has_key(h):
                        appointments = hero.appointments[game.days_played][h]
                    if debug: print str(appointments)
                    if self.game_conditions[c] == True:
                        if not appointments:
                            if debug: print "no appointments"
                            return False
                    elif self.game_conditions[c] == False:
                        if appointments:
                            if debug: print "appointments"
                            return False
                    elif not self.game_conditions[c] in appointments:
                        if debug: print str(self.game_conditions[c])+" not in appointments"
                        return False 
                elif c =="date":
                    if self.game_conditions[c] == "birthday":
                        if SEASONS.index(hero.birthday[0]) != game.season or game.day != hero.birthday[1]:
                            return False
                    elif self.game_conditions[c] == "independenceday":
                        if game.get_season() != "summer" or game.day != 4:
                            return False
                    elif self.game_conditions[c] == "newyear":
                        if game.get_season() != "spring" or game.day != 1:
                            return False
                    elif self.game_conditions[c] == "valentine":
                        if game.get_season() != "spring" or game.day != 14:
                            return False
                    elif self.game_conditions[c] == "halloween":
                        if game.get_season() != "fall" or game.day != 31:
                            return False
                    elif self.game_conditions[c] == "christmaseve":
                        if game.get_season() != "winter" or game.day != 24:
                            return False
                    elif self.game_conditions[c] == "christmas":
                        if game.get_season() != "winter" or game.day != 25:
                            return False
                    elif self.game_conditions[c] == "newyeareve":
                        if game.get_season() != "winter" or game.day != 31:
                            return False
                elif c == "label":
                    l = self.game_conditions[c].replace("ACTIVE_GIRL", game.active_girl.id).replace("ROOM",game.room)
                    if not renpy.has_label(l):
                        return False
                elif c == "days":
                    if str(game.week_day) not in self.game_conditions[c]:
                        if debug: print "Not the right day"
                        return False
                elif c == "datespots":
                    if not game.get_dates():
                        return False
                elif c == "inventory":
                    if self.game_conditions[c] == "any":
                        if not hero.inventory:
                            if debug: print "No item in inventory"
                            return False
                    elif self.game_conditions[c] == "gifts":
                        if not [g for g in hero.inventory.values() if isinstance(g,Gift)]:
                            if debug: print "No gifts in inventory"
                            return False
                    elif self.game_conditions[c] not in hero.inventory.keys():
                        if debug: print "Item "+self.game_conditions[c]+" not in inventory"
                        return False
                elif c == "room":
                    if game.room not in self.game_conditions[c]:
                        if debug: print "Not the right room"
                        return False
                elif c == "days_played":
                    if game.days_played < self.game_conditions[c]:
                        if debug: print "Not enough days played"
                        return False
                elif c == "hours":
                    if self.game_conditions[c][0] <= self.game_conditions[c][1]:
                        if not self.game_conditions[c][0] <= game.hour <= self.game_conditions[c][1]:
                            if debug: print "Wrong time (1)"
                            return False
                    else:
                        if not (game.hour >= self.game_conditions[c][0] or  game.hour <= self.game_conditions[c][1]):
                            if debug: print "Wrong time (2)"
                            return False
                elif c == "valid_room":
                    if not ROOMS[self.game_conditions[c]].test():
                        return False
                elif c == "chances":
                    if debug: print "CHANCES"
                    if "_" in str(self.game_conditions[c]):
                        if debug: print self.name+" "+self.game_conditions[c]
                        t, g, d= self.game_conditions[c].rsplit("_")
                        if g == "girl":
                            g = self.girl.id
                        if t == "love":
                            chances = int(GIRLS[g].love()/float(d))/2
                    else:
                        chances = self.game_conditions[c]
                    if not self.get_flag_value("lastchance") == str(game.days_played)+"-"+str(game.hour):
                        self.set_flag("lastchance", str(game.days_played)+"-"+str(game.hour))
                        r = randint(1,100)
                        if r > chances:
                            if debug: print "not a chance"
                            return False
                        if debug: print "chances ok"
                    else:
                        return False
                else:
                    t, stat = c.rsplit("_")
                    if stat in ["fitness","knowledge","charm"]:
                        score = hero[stat]()
                    elif stat == "daysplayed":
                        score = game.days_played
                    elif stat in ["energy","grooming","fun","hunger"]:
                        score = hero[stat]
                    elif stat == "money":
                        score = hero.money
                    elif "flag" in t:
                        comp = t.replace("flag","")
                        flag = game.get_flag_value(stat)
                        val = self.game_conditions[c]
                        if isinstance(val,str) or isinstance(val,unicode):
                            val = val.split("_")
                            if val[0] == "daysplayed":
                                val[0] = game.days_played
                            if len(val) > 1:
                                val = val[0] + int(val[1])
                            else:
                                val = val[0]
                        if not comp or comp == "eq":
                            if flag != val:
                                if debug: print "flag"+stat+" not set at the right value "+str(flag)+"/"+str(self.game_conditions[c])
                                return False
                        elif comp == "in":
                            if not flag in  val:
                                return False
                        elif comp == "min":
                            if flag <  val:
                                if debug: print "flag"+stat+" too low "+str(flag)+"/"+str(self.game_conditions[c])
                                return False
                        elif comp == "max":
                            if flag >  val:
                                if debug: print "flag"+stat+" too high "+str(flag)+"/"+str(self.game_conditions[c])
                                return False
                    if t == "min":
                        if score < self.game_conditions[c]:
                            if debug: print "not enough "+stat
                            return False
                    elif t == "max":
                        if score > self.game_conditions[c]:
                            if debug: print "too much "+stat
                            return False
            
            
            
            
            if debug: print "OK"
            return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
