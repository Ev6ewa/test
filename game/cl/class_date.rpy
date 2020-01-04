init -10 python:
    class Date(Shtick):
        def __init__(self,
                name,
                game_conditions = {},
                girls_conditions = {},
                
                grooming = 0,
                fun = 0,
                hunger = 0,
                energy = 0,
                knowledge = 0,
                fitness = 0,
                charm = 0,
                money_cost = 0,
                display_name = "",
                min_love = 0,
                clothes = "casual",
                love_gain = 1,
                max_time = 4,
                conditions = []
                 ):
            self.name = name
            self.id = name
            self.clothes = clothes
            self.display_name = display_name
            if not self.display_name:
                self.display_name = self.name
            self.conditions = conditions
            self.game_conditions = {"min_energy":1,"min_hunger":1,"min_grooming":1,"min_fun":1}
            self.game_conditions.update(game_conditions)
            
            self.girls_conditions = {}
            self.money_cost = money_cost
            self.needs = {"energy":energy, "grooming":grooming, "fun":fun,"hunger":hunger}
            self.attributes = {"knowledge":knowledge,"fitness":fitness,"charm":charm}
            self.min_girls = 0
            self.max_girls = 100
            self.once_day = False
            self.once_week = False
            self.once_hour = False
            self.do_once = False
            
            self.duration = 4
            self.love_gain = love_gain
            self.max_time = max_time
            self.tooltip = ""
            if not self.id in DATES:
                DATES[self.id] = self
        
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
                    if rnd:
                        t += "("+str(int(x))+"→"+str(int(x)+1)+")"
                    else:
                        t += str(int(x))
                    tt.append(t)
            if self.money_cost:
                tt.append("{image=ui/icon_money.png}"+"-"+str(self.money_cost)+"$")
            if self.max_time:
                tt.append("{image=ui/icon_clock.png}"+"+"+str(self.max_time)+"$")
            if self. tooltip:
                tt = [self.tooltip] + tt
            return tt        

label date_do(date, date_girl, score=0):
    $ date = date
    if not game.get_flag_value("dateinprogress") == date_girl:
        if score:
            $ game.set_flag("datescore",score,"day")
        else:
            $ game.set_flag("datescore",date_girl.love()/5,"day")

    if date.name in date_girl.desire_factors:
        $ game.set_flag("datescore",25,"day","+")
    elif "not_"+date.name in date_girl.desire_factors:
        $ game.set_flag("datescore",-25,"day","+")
    if date.money_cost:
        $ hero.money -= date.money_cost
    $ starting_time = game.hour
    $ starting_day = game.day
    $ date_girl.set_room("date_"+date.name)
    if date.clothes:
        $ date_do_old_girl_clothes = game.girl_clothes
        $ game.girl_clothes = date.clothes
    scene expression "bg date_"+date.name
    call expression date_girl.id+"_greet" from _call_expression_98
    if renpy.has_label(date_girl.id+"_date_"+date.name):
        call expression date_girl.id+"_date_"+date.name from _call_expression_99
    else:
        call expression "date_"+date.name from _call_expression_100





    if game.hour in [14,20]:
        $ max_time = 4
    elif game.hour in [15,21]:
        $ max_time = 3
    elif game.hour in [16,22]:
        $ max_time = 2
    elif game.hour in [17,23]:
        $ max_time = 1
    $ game.room = "date_"+date.name
    call enter_room (room_present_girls=[date_girl.id], max_time=max_time) from _call_enter_room_2

    python:
        for n in date.needs.keys():
            hero[n] += date.needs[n]
        for s in date.attributes.keys():
            hero[s] += date.attributes[s]

        love_gain = date.love_gain
        for g in date_girl.desire_factors:
            if g == date.name:
                love_gain = love_gain*1.5
            elif g == "not_"+date.name:
                love_gain = love_gain/2
        score = game.get_flag_value("datescore")
        if score >= 100:
            love_gain += 5
        elif score >= 80:
            love_gain += 4
        elif score >= 60:
            love_gain += 2
        elif score >= 50:
            love_gain += 0
        elif score >= 40:
            love_gain -= 5
        elif score >= 20:
            love_gain -= 10
        else:
            love_gain -= 20

    $ date_girl.love += love_gain
    if starting_day == game.day and game.hour < starting_time + max_time and game.hour != 0:
        $ game.pass_time(starting_time + max_time - game.hour, True)
    if date.clothes:
        $ game.girl_clothes = date_do_old_girl_clothes
    $ room_present_girls = None
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
