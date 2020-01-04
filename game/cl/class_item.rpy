init -10 python:
    class Item(Shtick):
        def __init__(self,
                name,
                money_cost = 0,
                display_name = "",
                game_conditions = {},
                girls_conditions = {},
                conditions = [],
                one_only = False,
                tooltip = ""
                ):
            self.name = name
            self.id = name
            self.one_only = one_only
            self.money_cost = money_cost
            if display_name:
                self.display_name = display_name
            else:
                self.display_name = name
            self.conditions = conditions
            self.game_conditions = game_conditions
            self.girls_conditions = girls_conditions
            self.nbr = 1
            self.tooltip = tooltip
        
        def get_tooltip(self):
            tt = []
            if self.money_cost:
                tt.append("{image=ui/icon_money.png}"+"-"+str(self.money_cost)+"$")
            if self. tooltip:
                tt = [self.tooltip] + tt
            return tt

    class Gift(Item):
        def __init__(self,
                name,
                money_cost = 0,
                display_name = "",
                love_bonus = 0,
                sub_bonus = 0,
                les_bonus = 0,
                label = "",
                game_conditions = {},
                girls_conditions = {},
                once = False,
                conditions = [],
                limit = 200
                ):
            self.conditions = conditions
            self.name = name
            self.id = name
            self.one_only = False
            self.money_cost = money_cost
            if display_name:
                self.display_name = display_name
            else:
                self.display_name = name
            self.love_bonus = love_bonus
            self.sub_bonus = sub_bonus
            self.les_bonus = les_bonus
            self.label = label
            self.game_conditions = game_conditions
            self.girls_conditions = girls_conditions
            self.nbr = 1
            self.once = once
            self.tooltip = "Gift"
        
        def get_tooltip(self):
            tt = []
            if self.love_bonus:
                x = self.love_bonus
                if x > 0:
                    s = "+"
                else:
                    s = ""
                t = "{image=ui/icon_love_vsmall.png}"+s
                rnd, x = modf(x)
                if rnd:
                    t += "("+str(int(x))+"→"+str(int(x)+1)+")"
                else:
                    t += str(int(x))
                tt.append(t)
            if hasattr(self, "sub_bonus") and self.sub_bonus:
                x = self.sub_bonus
                if x > 0:
                    s = "+"
                else:
                    s = ""
                t = "{image=ui/icon_sub_vsmall.png}"+s
                rnd, x = modf(x)
                if rnd:
                    t += "("+str(int(x))+"→"+str(int(x)+1)+")"
                else:
                    t += str(int(x))
                tt.append(t)
            if hasattr(self, "les_bonus") and self.les_bonus:
                x = self.les_bonus
                if x > 0:
                    s = "+"
                else:
                    s = ""
                t = "{image=ui/icon_les_vsmall.png}"+s
                rnd, x = modf(x)
                if rnd:
                    t += "("+str(int(x))+"→"+str(int(x)+1)+")"
                else:
                    t += str(int(x))
                tt.append(t)
            if self.money_cost:
                tt.append("{image=ui/icon_money.png}"+"-"+str(self.money_cost)+"$")
            if self. tooltip:
                tt = [self.tooltip] + tt
            return tt
        
        def use(self, girl):
            if hasattr(self, "limit"):
                limit = self.limit
            else:
                limit = 200
            love_gain = int(self.love_bonus)
            if hasattr(self, "sub_bonus"):
                if girl.sub() + int(self.sub_bonus) > limit:
                    sub_gain = limit - girl.sub()
                else:
                    sub_gain = int(self.sub_bonus)
                girl.sub += sub_gain
            if hasattr(self, "les_bonus") and self.les_bonus != 0:
                NOTIFICATIONS.append([girl.name+" {image=ui/icon_les_vsmall.png}+"+str(self.les_bonus*5),2])
                girl.set_flag("lesbian", girl.get_flag_value("lesbian")+self.les_bonus)
            if game.get_season() == girl.birthday[0] and game.day == girl.birthday[1]:
                love_gain = love_gain*1.5
            for g in girl.desire_factors:
                if g == self.label or g == self.name:
                    love_gain = love_gain*1.5
                elif g == "not_"+self.label or g == "not_"+self.name:
                    if love_gain > 0:
                        love_gain = 0
                    love_gain -= 1
            hero.lose_item(self)
            girl.set_flag("gift"+result.name,1,7,mod="+")
            b = - girl.get_flag_value("gift"+self.name) +1
            love_gain = love_gain + b
            if love_gain > limit:
                love_gain = limit - girl.love
            girl.love += love_gain


    class Equip(Item):
        def __init__(self,
                name,
                display_name = None,
                money_cost = 0,
                game_conditions = {},
                girls_conditions = {},
                effects = {},
                type = "clothes",
                limit = None,
                conditions = []
                ):
            self.name = name
            self.id = name
            self.one_only = True
            self.conditions = conditions
            if display_name:
                self.display_name = display_name
            else:
                self.display_name = name
            self.money_cost = money_cost
            self.game_conditions = game_conditions
            self.girls_conditions = girls_conditions
            self.nbr = 1
            self.effects = effects
            self.type = type
            self.limit = limit
            self.tooltip = ""
        
        def get_tooltip(self):
            tt = [self.type.capitalize()+":"]
            for e in self.effects:
                if e in ["energy","hunger","fun","grooming",]:
                    x = self.effects[e]
                    if x > 0:
                        s = "+"
                    else:
                        s = ""
                    t = "{image=ui/icon_"+a+".png}"+s
                    rnd, x = modf(x)
                    if rnd:
                        t += "("+str(int(x))+"→"+str(int(x)+1)+")"
                    else:
                        t += str(int(x))
                    tt.append(t)
                elif e in ["charm","fitness","knowledge"]:
                    x = self.effects[e]
                    if x > 0:
                        s = "+"
                    else:
                        s = ""
                    t = "{image=ui/icon_"+e+".png}"+s
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
            if self. tooltip:
                tt = [self.tooltip] + tt
            return tt
        
        def equip(self):
            if hero.equipment[self.type] == self:
                self.unequip()
            else:
                if hero.equipment[self.type]:
                    hero.equipment[self.type].unequip()
                hero.equipment[self.type] = self
                for e in self.effects:
                    if e in ["fitness","charm","knowledge"]:
                        if persistent.difficulty == 0:
                            setattr(store, e+"_max", getattr(store, e+"_max") + (int(self.effects[e]*1.5)))
                        elif persistent.difficulty == -1:
                            setattr(store, e+"_max", getattr(store, e+"_max") + (self.effects[e]*2))
                        else:
                            setattr(store, e+"_max", getattr(store, e+"_max") + self.effects[e])
                        hero[e] += self.effects[e]
        
        
        def unequip(self):
            hero.equipment[self.type] = None
            for e in self.effects:
                if e in ["fitness","charm","knowledge"]:
                    if persistent.difficulty == 0:
                        setattr(store, e+"_max", getattr(store, e+"_max") - int(self.effects[e]*1.5))
                        hero[e] -= int(self.effects[e]*1.5)
                    elif persistent.difficulty == -1:
                        setattr(store, e+"_max", getattr(store, e+"_max") - (self.effects[e]*2))
                        hero[e] -= self.effects[e]*2
                    else:
                        setattr(store, e+"_max", getattr(store, e+"_max") - self.effects[e])
                        hero[e] -= self.effects[e]


    class Consumable(Item):
        def __init__(self,
                name,
                duration = 0,
                effects = [],
                money_cost = 0,
                money_gain = (),
                label = None,
                action_params = None,
                display_name = "",
                game_conditions = {},
                girls_conditions = {},
                limit = None,
                conditions = [],
                uses =  1,
                tooltip = ""
                ):
            self.name = name
            self.one_only = False
            self.id = name
            self.conditions = conditions
            if display_name:
                self.display_name = display_name
            else:
                self.display_name = name
            self.money_cost = money_cost
            self.money_gain = money_gain
            self.duration = duration
            self.game_conditions = game_conditions
            self.girls_conditions = girls_conditions
            self.label = label
            self.effects = effects
            self.say = []
            self.uses = uses
            self.nbr = 1
            self.limit = limit
            self.tooltip = tooltip
        
        def get_tooltip(self):
            tt = []
            for e, x in self.effects:
                if e in ["energy","hunger","fun","grooming",]:
                    if x > 0:
                        s = "+"
                    else:
                        s = ""
                    t = "{image=ui/icon_"+e+"_white.png}"+s
                    rnd, x = modf(x)
                    chances = str(int(abs(rnd*100)))+"%"
                    if rnd:
                        t += "("+str(int(x))+"/"+chances+"→"+str(int(x+1))+")"
                    else:
                        t += str(int(x))
                    tt.append(t)
                elif e in ["charm","fitness","knowledge"]:
                    if x > 0:
                        s = "+"
                    else:
                        s = ""
                    t = "{image=ui/icon_"+e+".png}"+s
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
                elif e == "time":
                    tt.append("{image=ui/icon_clock.png}"+"+"+str(x)+"h")
            if self.money_cost:
                tt.append("{image=ui/icon_money.png}"+"-"+str(self.money_cost)+"$")
            if self.uses:
                tt.append(str(self.uses)+" use(s)")
            if self.tooltip:
                tt = [self.tooltip] + tt
            return tt
        
        def use(self):
            if self.label:
                renpy.call_in_new_context(*self.label)
            for e in self.effects:
                if e[0] in ["fitness","knowledge","charm","fun","hunger","energy","grooming"]:
                    hero[e[0]] += e[1]
                elif e[0] == "skill" and e[1] not in hero.skills:
                    hero.skills.append(e[1])
                elif e == "time":
                    game.pass_time(e[1], needs= True)
            self.uses -= 1
            if not hasattr(self, "uses") or not self.uses:
                hero.lose_item(self)
            if self.limit:
                game.set_flag(self.name,True,self.limit)
        
        def __setstate__(self, dict):
            self.__dict__ = dict
            
            if not hasattr(self, 'uses'):
                self.uses = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
