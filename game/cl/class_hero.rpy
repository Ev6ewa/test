init -10 python:
    class Hero(Flagged, store.object):
        def __init__(self, name, family_name):
            self.name = name.capitalize()
            self.id = "HERO!"
            self.family_name = family_name
            self.birthday = (randchoice(SEASONS),randint(1,31))
            self.money = 150
            self.skills = []
            self.status = "single"
            self.age = 25
            self.equipment = {"clothes":None,"accessory":None}
            self.appointments = {}
            self.energy = Need("energy", "{image=ui/icon_energy_white.png}", max = 10)
            self.grooming = Need("grooming", "{image=ui/icon_grooming_white.png}", max = 10)
            self.hunger = Need("hunger", "{image=ui/icon_hunger_white.png}", max = 10)
            self.fun = Need("fun", "{image=ui/icon_fun_white.png}", max = 10)
            self.fitness = Attribute("fitness", "{image=ui/icon_fitness.png}", up_hook = {"/20":"setattr(store, 'energy_max', getattr(store, 'energy_max')+1)"})
            self.knowledge = Attribute("knowledge", "{image=ui/icon_knowledge.png}",up_hook = {"/10":self.gain_talk_subject, "/20":"setattr(store, 'fun_max', getattr(store, 'fun_max')+1)"})
            self.charm = Attribute("charm", "{image=ui/icon_charm.png}", up_hook = {"/20":"setattr(store, 'grooming_max', getattr(store, 'grooming_max')+1)"})
            
            self.activity = ""
            
            self.known_talk_subjects = []
            for x in xrange(2):
                self.gain_talk_subject()
            self.inventory = {}
            self.smartphone_contacts = []
            self.say = Character(self.name, who_outlines=[ (1, '#0099ff') ], who_color="#ffffff")
        
        def __setitem__(self, key, item):
            if key == "energy":
                self.energy = item
            elif key == "grooming":
                self.grooming = item
            elif key == "fun":
                self.fun = item
            elif key == "hunger":
                self.hunger = item
            elif key == "fitness":
                self.fitness = item
            elif key == "charm":
                self.charm = item
            elif key == "knwoledge":
                self.knwoledge = item
        
        def __getitem__(self, key):
            if key == "energy":
                return self.energy
            elif key == "grooming":
                return self.grooming
            elif key == "fun":
                return self.fun
            elif key == "hunger":
                return self.hunger
            elif key == "fitness":
                return self.fitness
            elif key == "charm":
                return self.charm
            elif key == "knowledge":
                return self.knowledge
        
        def update_need(self, need, val):
            self[need] = self[need] + val
            if self[need] < 0:
                self[need] = 0
            elif self[need] > 10:
                self[need] = 10
        
        def gain_talk_subject(self):
            if game.talk_subjects:
                subject = randchoice(game.talk_subjects)
                game.talk_subjects.remove(subject)
                self.known_talk_subjects.append(subject)
        
        def test_money(self, val):
            
            if self.money > val-1:
                return True
            else:
                renpy.say("","I don't have enough money.")
                return False
        
        def show_smartphone_info(self):
            ui.hbox(xpos = 475, ypos = 155, xmaximum = 445, ymaximum = 290, yfill = True, xfill = True)
            if game.get_flag_value("female"):
                ui.add("bree smartphone")
            else:
                ui.add("mike smartphone")
            ui.vbox(xfill=True, xalign = 1.0, xmaximum = 220)
            ui.text("Name : "+self.name.capitalize()+" "+self.family_name.capitalize(), size=15)
            if self.status:
                ui.text("Status : "+self.status.capitalize(), size=15)
            ui.text("Age : "+str(self.age), size=15)
            if game.get_flag_value("female"):
                ui.text("Sex : Female", size=15)
            else:
                ui.text("Sex : Male", size=15)
            ui.text("Birthday : "+self.birthday[0].capitalize()+ " " + str(self.birthday[1]), size=15)
            ui.text("Days played : {}".format(game.days_played), size=15)
            job = game.get_flag_value("job")
            if not job:
                if not game.get_flag_value('female') and not game.get_flag_value('fired'):
                    job = "office"
                else:
                    job = "unemployed"
            if ROOMS.get(job):
                job = ROOMS[job].display_name
            ui.text("Job : {}".format(job.capitalize()), size=15)
            ui.close()
            ui.close()
            renpy.show("smartphone")
        
        def set_appointment(self, day, hour, girl):
            if not day in self.appointments:
                self.appointments[day] = {}
            if not hour in self.appointments[day]:
                self.appointments[day][hour] = []
            if not girl in self.appointments[day][hour]:
                self.appointments[day][hour].append(girl)
        
        def lose_item(self,item):
            if isinstance(item, str) or isinstance(item, unicode):
                if item in self.inventory.keys():
                    item =  self.inventory[item]
                else:
                    return
            if item.name in self.inventory.keys():
                self.inventory[item.name].nbr -= 1
                if self.inventory[item.name].nbr <= 0:
                    del self.inventory[item.name]
        
        def has_item(self, item):
            if item in self.inventory.keys():
                return self.inventory[item].nbr
            else:
                return 0
        
        def gain_item(self, item):
            if item.name in self.inventory.keys():
                self.inventory[item.name].nbr += 1
            else:
                self.inventory[item.name] = copy.deepcopy(item)
        
        def check_skill(self,skill):
            if skill in self.skills:
                return True
            return False
        
        
        def select_items(self, items):
            select = []
            for b in items:
                if b.test():
                    if not (b.one_only and b.name in hero.inventory.keys()):
                        n = b.name
                        if b.money_cost > hero.money:
                            select.append(("{color=#f00}"+b.display_name.capitalize()+"{/color}",b))
                        else:
                            select.append((b.display_name.capitalize(),b))
            if not select:
                renpy.say("","There is nothing for me here.")
                return None
            return select
        
        def shop(self, items):
            select = self.select_items(items)
            while select:
                item = renpy.call_screen("select",select, cap = False)
                if item == "None":
                    return "None"
                elif item.money_cost <= hero.money:
                    self.money -= item.money_cost
                    self.gain_item(item)
                    NOTIFICATIONS.append(["+ "+item.display_name,2])
                    NOTIFICATIONS.append(["- "+str(item.money_cost)+"{image=ui/icon_money.png}",2])
                
                
                else:
                    renpy.say("", "I don't have enough money to buy that.")
                    return "None"
                select = self.select_items(items)
            return "None"
        
        def has_condom(self):
            return any([x in self.inventory for x in 'condom', 'box of condoms'])
        
        def use_condom(self):
            if "condom" not in self.inventory:
                if "box of condoms" not in self.inventory:
                    return False
                self.inventory["box of condoms"].use()
            self.lose_item("condom")
            return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
