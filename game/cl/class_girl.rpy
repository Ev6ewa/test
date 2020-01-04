init python:
    left = Transform(xalign=0.25, yalign=1.0, yanchor="bottom", xanchor=0.5)
    right = Transform(xalign=0.75, yalign=1.0, yanchor="bottom", xanchor=0.5)

init -15 python:
    class Girl(Flagged, store.object):
        def __init__(
                self,
                name,
                status,
                age,
                birthday,
                traits,
                desire_factors,
                schedule = {},
                pubes = True,
                piercings = ["nipples","navel","nose"],
                flags = None,
                min_sub = 0,
                outfits = [],
                expressions = [],
                ):
            self.id = name
            self.piercings = piercings
            self.name = name.capitalize()
            self.sub = Attribute(self.id+"_sub", self.id+" {image=ui/icon_sub_vsmall.png}",min=min_sub, negative=self.id+" {image=ui/icon_dom_vsmall.png}")
            self.love = Attribute(self.id+"_love", self.id+" {image=ui/icon_love_vsmall.png}",up_hook = {"/30":self.discover_trait}, max=20, date=True)
            self.schedule = schedule
            self.desire_factors = desire_factors
            self.status = status
            self.birthday = birthday
            self.age = age
            self.clothes = {}
            self.room = None
            self.talk_subjects = []
            self.location = {}
            self.traits = traits
            self.known_traits = []
            self.activity = None
            self.outfits = outfits
            self.expressions = expressions
            
            
            GIRLS[self.id] = self
            self.pubes = pubes
            if flags:
                for f in flags:
                    self.set_flag(f,flags[f])
            self.say = Character(self.name, who_outlines=[ (1, "#FF00FF") ], who_color="#ffffff")
        
        def __call__(self):
            return self.name
        
        def __getattribute__(self, item):
            if item == 'heroname':
                name = self.get_flag_value('heroname')
                return name if name else hero.name
            return object.__getattribute__(self, item)
        
        def discover_trait(self):
            to_remove = []
            known_traits = self.get_flag_value("knowntraits",[])
            for t in known_traits:
                if t not in self.traits:
                    to_remove.append(t)
            for t in to_remove:
                known_traits.remove(t)
            for t in self.traits:
                if t not in known_traits:
                    known_traits.append(t)
                    break
            self.set_flag("knowntraits",known_traits)
        
        def has_trait(self,trait):
            if not trait in self.traits:
                return False
            else:
                return True
        
        def get_status(self):
            return self.get_flag_value("status", self.status)
        
        def get_talk_subjects(self):
            subjects = hero.known_talk_subjects + self.talk_subjects
            if renpy.has_label(self.id+"_talk_subjects"):
                renpy.call_in_new_context(self.id+'_talk_subjects', subjects)
            if game.get_season() == self.birthday[0] and game.day == self.birthday[1] and self.get_flag_value("birthdayknown"):
                subjects.append("birthday")
            if game.days_played in hero.appointments and game.hour in hero.appointments[game.days_played] and self.id in hero.appointments[game.days_played][game.hour] and not game.get_flag_value("dateinprogress") == self:
                subjects.append("date")
            return [s for s in subjects if not self.get_flag_value(s+"_talk_used")]
        
        def get_clothes(self,clothes = None):
            
            
            
            
            if not clothes:
                if game.get_flag_value("dateinprogress") and game.get_flag_value("dateinprogress").id == self.id:
                    if game.get_flag_value("currentdate"):
                        clothes =  DATES[game.get_flag_value("currentdate")].clothes
                    else:
                        clothes  = 'casual'
                elif self.room and game.room and self.room == game.room and self.activity.get("clothes",None):
                    clothes = self.activity["clothes"]
                elif game.room and ROOMS[game.room].outfit:
                    clothes = ROOMS[game.room].outfit
                else:
                    clothes = "casual"
            
            
            
            
            
            
            
            return clothes
        
        def get_chat(self):
            result = randint(0,1)
            if result == 0:
                t = "love"
            else:
                t = "desire"
            return self.id+"_"+t+"_"+str(self.love()/40)
        
        def get_piercings(self, piercing = None):
            if not hasattr(self, "piercings"):
                self.piercings = []
            piercings = self.piercings
            newpiercings = self.get_flag_value("newpiercings", {})
            for k in newpiercings:
                piercings[k]['pierced'] = newpiercings[k].get('pierced', False)
            if piercing:
                if piercing in piercings and piercings[piercing].get("pierced",False) and piercings[piercing].get("worn",True):
                    return True
                else:
                    return False
            else:
                return piercings
        
        def get_room(self):
            return self.room
        
        def set_room(self, temp_room=None):
            while self.room and self.room in ROOMS and self in ROOMS[self.room].present_girls:
                ROOMS[self.room].present_girls.remove(self)
            if not temp_room:
                self.set_activity()
                temp_room = self.activity.get("room","none")
            self.room = temp_room
            if self.room and self.room in ROOMS and not self in ROOMS[self.room].present_girls:
                ROOMS[self.room].present_girls.append(self)
        
        
        def desire_bonus(self):
            if not self.get_flag_value("desireBonusDone"):
                self.set_flag("desireBonusDone",True,1)
                bonus = 0
                for d in self.desire_factors:
                    if d in ["fitness","charm","knowledge"]:
                        if hero[d]()*2 > self.love:
                            bonus += 1
                    elif "not_" in d and d.replace("not_","") in ["fitness","charm","knowledge"]:
                        if hero[d.replace("not_","")]()*2 > self.love:
                            bonus -= 1
                    elif d == "career":
                        if game.get_flag_value("promoted")*10 >= self.love():
                            bonus += 1
                    elif hero.check_skill(d):
                        bonus += 1
                    elif "not_" in d and hero.check_skill(d.replace("not_","")):
                        bonus -= 1
                    elif d == "money":
                        if hero.money >= 100 + self.love() * self.love():
                            bonus += 1
                    elif hero.equipment["clothes"] or hero.equipment["accessory"]:
                        if hero.equipment["clothes"]:
                            for e in hero.equipment["clothes"].effects:
                                if e[0] == d and randint(1,100) <= e[1]:
                                    bonus += 1
                        if hero.equipment["accessory"]:
                            for e in hero.equipment["accessory"].effects:
                                if e[0] == d and randint(1,100) <= e[1]:
                                    bonus += 1
                self.love += bonus
        
        def get_activity(self, hour = "Now"):
            if hour != "Now":
                if hour > 23:
                    hour = 0
                    day = game.get_week_day()+1
                    if day > 7:
                        day = 1
                else:
                    day = game.get_week_day()
            else:
                hour = game.hour
                day = game.get_week_day()
            day = str(day)
            schedule = self.get_schedule()
            for k in schedule.keys():
                if day in k:
                    
                    break
            
            hours = sorted([int(a) for a in schedule[k].keys()])
            for a in hours:
                if hour <= a:
                    
                    break
            a = str(a)
            if game.get_flag_value("dateinprogress") and game.get_flag_value("dateinprogress").id == self.id:
                if game.get_flag_value("currentdate"):
                    d = DATES[game.get_flag_value("currentdate")]
                    result = {"activity":"date","clothes":d.clothes,"room":game.room} 
                else:
                    result = {"activity":"date","clothes":"casual","room":game.room} 
            else:
                if not self.get_flag_value("activity-"+day+"-"+a) or self.get_flag_value("activity-"+day+"-"+a)["activity"] == "date":
                    
                    r = self.get_flag_value(k+str(a))
                    if r:
                        result = r
                    else:
                        tmp_list = []
                        for c in schedule[k][a]:
                            if "seasons" in c.keys():
                                if str(game.season) in c["seasons"]:
                                    tmp_list.append(c)
                            else:
                                tmp_list.append(c)
                        if persistent.randomness >= 1:
                            result = randchoice(tmp_list)
                            self.set_flag(k+str(a),result, 1)
                        else:
                            result = tmp_list[0]
                            self.set_flag(k+str(a),result, 1)
                else:
                    
                    result = self.get_flag_value("activity-"+day+"-"+a)
            return a, result
        
        def set_activity(self):
            
            a, self.activity = self.get_activity()
            self.set_flag("activity-"+str(game.week_day)+"-"+a,self.activity,"day")
        
        
        
        def get_events(self):
            valid_events = []
            if self.get_flag_value("last_test") != str(game.hour)+" "+str(game.days_played):
                self.set_flag("last_test",str(game.hour)+" "+str(game.days_played),"day")
                for e in EVENTS.values():
                    if e.test():
                        valid_events.append(e)
            return valid_events
        
        def get_counters(self, counter=None):
            counters = self.get_flag_value('counters')
            if not counters:
                counters = {}
                self.set_flag('counters', counters)
            if counter:
                return counters.get(counter)
            else:
                return counters
        
        def set_counter(self, counter, value=0):
            counters = self.get_counters()
            if value == None:
                counters.pop(counter, None)
            else:
                
                
                counters[counter] = int(value)
        
        def increment_counters(self):
            counters = self.get_counters()
            for counter in counters:
                counters[counter] += 1
        
        def get_schedule(self):
            schedule_name = self.get_flag_value('schedule')
            if not schedule_name:
                schedule_name = 'default'
            return self.schedule.get(schedule_name)
        
        def impregnate(self, counter=True):
            if not self.get_flag_value('pregnant') and not self.get_flag_value('pill') and (randint(1, 3) == 1 or 'hung' in hero.skills):
                self.set_flag("pregnant",1)
                self.set_counter("pregnant")

label girl_interact(interact_girl):
    $ interact_girl = interact_girl
    scene expression "bg "+game.room
    call expression interact_girl.id+"_greet" from _call_expression_105
    $ _return = interact_girl
    $ game.active_girl = interact_girl
    $ hero.activity = "interact"
    $ interact_valid_events = sorted(interact_girl.get_events(), key=lambda event: event.priority)
    while interact_valid_events:
        $ interact_e = interact_valid_events.pop()
        call event_do (interact_e) from _call_event_do_2
        if game.room != room.id or interact_e.quit:
            $ interact_valid_events = []
    while True:
        scene expression "bg "+game.room
        $ game.active_girl = interact_girl
        $ hero.activity = "interact"
        show expression interact_girl.id
        $ bye_outfit = interact_girl.get_clothes()
        python:
            _window_hide(trans=False)
            choices = []
            for act in sorted(ACTIVITIES.values(), key=lambda x: x.display_name):
                
                if act.test() and act.game_conditions.get("activity","None") == "interact":
                    
                    choices.append(act)
        call screen select_activity(choices)
        if isinstance(_return, (Activity)):
            call activity_do (_return) from _call_activity_do
        else:
            $ game.active_girl = None
            $ hero.activity = None
            hide expression interact_girl.id
            return

        if interact_girl.get_room() != game.room:
            if randint(0,(interact_girl.love()+1)/10) != 0:
                call expression interact_girl.id+"_bye" pass (bye_outfit=bye_outfit) from _call_expression_106
            $ game.active_girl = None
            $ hero.activity = None
            hide expression interact_girl.id
            return

        if not ROOMS[game.room].test():
            $ game.active_girl = None
            $ hero.activity = None
            hide expression interact_girl.id
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
