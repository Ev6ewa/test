init python:
    OUTFITS = ["casual", "casual2", "date", "towel", "naked", "swimsuit", "sexyswimsuit", "work", "underwear", "sexyunderwear", "rpg", "sport", "wedding", "rope", "sleep", "strapon", "suit", "cosplay", "christmas"]
    class Picker(object):
        def __init__(self, girl, preg = True, pubes = True):
            self.girl =  girl
            self.preg = preg
            self.pubes = pubes
            
            self.flags = ['boobjob', 'haircut', 'gold']
            self.private_flags = ['topless', 'bottomless', 'facecum', 'wet']
            self.private_rooms = ['personal', 'bedroom1', 'bedroom3', 'livingroom']
        
        def basic(self, attr):
            if self.girl.love < 100 and "b" not in attr:
                attr.add("a")
            elif self.girl.love >= 100 and "a" not in attr:
                attr.add("b")
            
            if self.girl.get_flag_value("pregnant") >= 9 and self.preg:
                attr.add("pregnant")
            if self.girl.get_flag_value("collared") and self.girl.sub() >= 50:
                attr.add("collar")
            if self.girl.get_flag_value("pubes",self.girl.pubes) and self.pubes:
                attr.add("pubes")
            
            for attribute in self.flags:
                if self.girl.get_flag_value(attribute):
                    attr.add(attribute)
            
            
            if game.room in self.private_rooms:
                for attribute in self.private_flags:
                    if self.girl.get_flag_value(attribute):
                        attr.add(attribute)
            return attr
        
        def outfits(self, attr):
            outfit_list = self.girl.outfits if self.girl.outfits else OUTFITS
            for o in attr:
                if o in outfit_list:
                    break
            else:
                o = self.girl.get_clothes()
                
                attr.add(o)
            for o in attr:
                if self.girl.get_flag_value("sexy"+o):
                    attr.remove(o)
                    attr.add("sexy"+o)
            return attr
        
        def piercings(self, attr):
            piercings = self.girl.get_piercings()
            for p in piercings:
                if piercings[p].get("worn",True) and piercings[p].get("pierced",False):
                    for o in piercings[p].get("outfits",["all"]):
                        if o in attr or o == "all":
                            for e in piercings[p].get("expressions",["all"]):
                                if e in attr or e == "all":
                                    if p in ["tongue","lips", "eyebrow"]:
                                        p = p+e
                                    if p == "nipples" and "boobjob" in attr:
                                        p = p+"bb"
                                    if p == "navel" and "pregnant" in attr:
                                        p = p+"pregnant"
                                    attr.add(p)
                                    break
            return attr
        
        def __call__(self, attr):
            
            attr = self.basic(attr)
            attr = self.outfits(attr)
            attr = self.piercings(attr)
            
            return attr
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
