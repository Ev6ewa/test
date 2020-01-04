init -7 python:
    class Room(Flagged, store.object):
        def __init__(self,
            name,
            seasons = False,
            hours = (0,100),
            money_cost = 0,
            display_name = "",
            bg = None,
            exits = [],
            alternate_exits = [],
            days = "1234567",
            buy = [],
            required_item = None,
            music = None,
            valid = True,
            open_seasons = [],
            travel_time = 0,
            outfit = "casual",
            ):
            self.id = name
            self.open_seasons = open_seasons
            if display_name:
                self.display_name = display_name
            else:
                self.display_name = self.id
            
            self.days = days
            self.hours = hours
            self.exits = exits
            self.alternate_exits = alternate_exits
            self.buy = buy
            self.money_cost = money_cost
            self.travel_time = travel_time
            self.image = True
            self.day_night = False
            self.seasons = False
            self.required_item = required_item
            self.tooltip = ""
            self.music = music
            self.present_girls = []
            self.outfit = outfit
            if bg:
                self.bg = bg
            else:
                self.bg = self.id
            ROOMS[self.id] = self
            if not valid:
                HIDDEN.append(self.id)
        
        def play_music(self):
            
            if hasattr(self, "music") and not (renpy.music.get_playing() == self.music):
                renpy.music.play(self.music,loop=True,fadein=0.5)
            elif not hasattr(self, "music"):
                renpy.music.stop(fadeout=0.5)
        
        def get_tooltip(self):
            tt = []
            if self.money_cost and not (game.get_flag_value("paidrooms") and self.id in game.get_flag_value("paidrooms")):
                tt.append("{image=ui/icon_money.png}"+"-"+str(self.money_cost)+"$")
            if self.travel_time:
                tt.append("{image=ui/icon_clock.png}"+"+"+str(self.travel_time)+"h")
            if self. tooltip:
                tt = [self.tooltip] + tt
            return tt        
        
        
        def test(self):
            
            if self.id == "bedroom2" and game.room not in ["secondfloor","bedroom2"] and bree.get_room() == "bedroom2":
                return False
            elif self.id == "bedroom3" and game.room not in ["secondfloor","bedroom3"] and sasha.get_room() == "bedroom3":
                return False
            elif self.id == "bathroom" and game.room not in ["secondfloor","bathroom"] and (bree.get_room() == "bathroom" or sasha.get_room() == "bathroom"):
                return False
            
            if self.id in HIDDEN:
                return False
            if self.hours[0] < self.hours[1]:
                if not self.hours[0] <= game.hour <= self.hours[1]:
                    return False
            else:
                if self.hours[1] < game.hour < self.hours[0]:
                    return False
            if str(game.get_week_day()) not in self.days:
                return False
            if self.money_cost > 0 and not hero.money >= self.money_cost:
                if not self.id in game.get_flag_value("paidrooms",[]):
                    return False
            if self.open_seasons and not str(game.season) in self.open_seasons:
                return False
            if hasattr(self, 'required_item') and self.required_item != None:
                if isinstance(self.required_item, list):
                    req = self.required_item
                else:
                    req = [self.required_item]
                for r in req:
                    if r == "vehicule":
                        if not ("car" in hero.inventory or "bike" in hero.inventory or  "sport_car" in hero.inventory):
                            return False
                    elif r == "bigVehicule":
                        if not ("car" in hero.inventory or  "sport_car" in hero.inventory):
                            return False
                    elif "not_" in r:
                        if r.replace("not_","") in hero.inventory.keys():
                            
                            return False
                    elif r not in hero.inventory.keys():
                        
                        return False
            
            return True
        
        def get_present_girls(self, valid = True, girls = []):
            if girls:
                result = [g for g in GIRLS.values() if g.id in girls]
            else:
                result = []
                for g in self.present_girls:
                    if valid and g.id not in HIDDEN:
                        result.append(g)
                    elif not valid:
                        result.append(g)
            return result
        
        def get_events(self):
            
            valid_events = []
            
            
            for e in EVENTS.values():
                if e.test():
                    valid_events.append(e)
            
            return valid_events
        
        def travel_to(self):
            if self.travel_time and not ("car" in hero.inventory or  "sport_car" in hero.inventory):
                game.pass_time(self.travel_time,True)
        
        def pay_entrance(self):
            if self.money_cost and not self.id in game.get_flag_value("paidrooms",[]):
                hero.money -= self.money_cost
                game.set_flag("paidrooms",[self.id],1, mod = "+")

label enter_room(back="map", room_present_girls=[], max_time=0):
    $ room = ROOMS[game.room]
    $ _window_hide(trans=False)
    if max_time:
        $ end_time = game.hour + max_time
        if end_time > 23:
            $ end_time = end_time - 24
            $ end_day = game.day + 1
        else:
            $ end_day = game.day
    if game.from_room and game.from_room != game.room:
        $ ROOMS[game.from_room].travel_to()
    $ room.travel_to()
    $ room.pay_entrance()

    while game.room == room.id:
        python:
            for r in ROOMS.values():
                r.present_girls = []
            for girl in GIRLS.values():
                girl.set_room()
        $ room = ROOMS[game.room]
        $ room.play_music()
        $ entering_time = game.hour
        scene expression "bg "+room.bg
        if max_time and end_time <= game.hour and end_day == game.day or not room.test():
            $ game.room = back
            $ game.from_room = room.id
            return
        else:

            $ room.present_girls = room.get_present_girls(girls=room_present_girls)
            $ room_valid_events = sorted(room.get_events(), key=lambda event: event.priority)
            while room_valid_events:
                $ room_e = room_valid_events.pop()
                call event_do (room_e) from _call_event_do_1
                if game.room != room.id or room_e.quit:
                    $ room_valid_events = []


            if game.room == room.id and entering_time == game.hour:
                python:
                    for g in room.present_girls:
                        if g.id not in HIDDEN:
                            g.desire_bonus()

                if game.get_flag_value("dateinprogress"):
                    $ game.active_girl = game.get_flag_value("dateinprogress")
                python:


                    for girl in GIRLS.values():
                        girl.set_room()
                call screen room(room=room)
                if isinstance(_return, (Girl)):
                    call girl_interact (_return) from _call_girl_interact

                elif isinstance(_return, (Activity)):
                    call activity_do (_return) from _call_activity_do_1

                $ game.from_room = room.id
            else:




                $ game.from_room = room.id
                return
    $ game.from_room = room.id
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
