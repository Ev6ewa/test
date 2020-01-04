init -11 python:
    from math import modf

    STATS = []

    class Stat(Flagged, store.object):
        def __init__(self, id, name, val=10, min=0, max=10):
            self.name = name
            self.id = id
            val = self.normal_val(val)
            setattr(store, self.id, val)
            setattr(store, self.id+"_min", min)
            setattr(store, self.id+"_max", max)
            STATS.append(self)
            self.update(val)
        
        def __call__(self):
            return int(getattr(store, self.id))
        
        def normal_val(self, val):
            return int(val)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def __iadd__(self, val):
            if isinstance(val, Stat):
                self.notify(val())
                self.update(val())
            else:
                
                val = self.normal_val(val)
                self.notify(val)
                self.update(val)
            
            return self
        
        def __isub__(self, val):
            if isinstance(val, Stat):
                self.notify(-val())
                self.update(-val())
            else:
                val = self.normal_val(val)
                self.notify(-val)
                self.update(-val)
            return self
        
        def __eq__(self, val):            
            if isinstance(val, Stat) and getattr(store, self.id) == val():
                return True
            else:
                return getattr(store, self.id) == val
        
        def __ne__(self, val):
            if isinstance(val, Stat) and getattr(store, self.id) != val():
                return True
            else:
                return getattr(store, self.id) != val
        
        def __gt__(self, val):
            if isinstance(val, Stat) and getattr(store, self.id) > val():
                return True
            else:
                return getattr(store, self.id) > val
        
        def __ge__(self, val):
            if isinstance(val, Stat) and getattr(store, self.id) >= val():
                return True
            else:
                return getattr(store, self.id) >= val
        
        def __lt__(self, val):
            if isinstance(val, Stat) and getattr(store, self.id) < val():
                return True
            else:
                return getattr(store, self.id) < val
        
        def __le__(self, val):
            if isinstance(val, Stat) and getattr(store, self.id) <= val():
                return True
            else:
                return getattr(store, self.id) <= val          
        
        def notify(self, val):
            if isinstance(val, float):
                rnd, val = modf(val)
                if rnd == 0:
                    val = int(val)
                else:
                    val = val + rnd
            
            if val >= 0.:
                if getattr(store, self.id) + val > getattr(store, self.id+"_max"):
                    val = getattr(store, self.id+"_max") - getattr(store, self.id) 
                s = "+"
            else:
                if getattr(store, self.id) + val < getattr(store, self.id+"_min"):
                    val = - (getattr(store, self.id+"_min") + getattr(store, self.id))
                s = ""
            if val == 0:
                return
            NOTIFICATIONS.append([self.name+s+str(val),2])
        
        def update(self,val=0):
            
            
            val = self.normal_val(val + getattr(store, self.id))
            if val > getattr(store, self.id+"_max"):
                setattr(store, self.id, getattr(store, self.id+"_max"))
            elif val < getattr(store, self.id+"_min"):
                setattr(store, self.id, getattr(store, self.id+"_min"))
            else:
                setattr(store, self.id, val)

    class Need(Stat):
        
        def normal_val(self, val):
            if isinstance(val, float) and persistent.randomness == 2:
                rnd, val = modf(val)
                if random() <= abs(rnd):
                    if rnd > 0:
                        val += 1
                    elif rnd < 0:
                        val -= 1
                val = int(val)
            return val

    class Attribute(Stat):
        def __init__(self,id, name, val=0, up_hook = None, min=0, max=100, date=False, negative=False):
            self.name = name
            self.id = id
            self.up_hook = up_hook
            self.date = date
            self.negative = negative
            setattr(store, self.id, val)
            setattr(store, self.id+"_min", min)
            setattr(store, self.id+"_max", max)
            STATS.append(self)
            self.update(val)
        
        def normal_val(self, val):
            if isinstance(val, float):
                rnd, val = modf(val)
                if random() <= abs(rnd):
                    if rnd > 0:
                        val += 1
                    elif rnd < 0:
                        val -= 1
            return int(val)
        
        def notify(self, val):
            if isinstance(val, float):
                rnd, val = modf(val)
                if rnd == 0:
                    val = int(val)
                else:
                    val = val + rnd
            if persistent.difficulty == 0 and val > 0:
                val = int(val*1.5)
            elif persistent.difficulty == -1 and val > 0:
                val = val*2
            if val >= 0.:
                if getattr(store, self.id) + val > getattr(store, self.id+"_max"):
                    val = getattr(store, self.id+"_max") - getattr(store, self.id) 
                s = "+"
            else:
                if getattr(store, self.id) + val < getattr(store, self.id+"_min"):
                    val = getattr(store, self.id+"_min") - getattr(store, self.id)
                s = ""
            if val == 0:
                return
            name = self.name
            if hasattr(self, 'negative') and self.negative and getattr(store, self.id) + val < 0:
                name = self.negative
                val = val * -1
                s = "" if s == '+' else '+'
            
            NOTIFICATIONS.append([name+s+str(val),2])
        
        def update(self,val=1):
            if persistent.difficulty == 0 and val > 0:
                val = int(val*1.5)
            elif persistent.difficulty == -1 and val > 0:
                val = val*2
            
            if self.date and game and game.get_flag_value("dateinprogress") and game.get_flag_value("dateinprogress").id in self.name:
                if val > 0:
                    game.set_flag("datescore",(val*5)+5,"day","+")
                else:
                    game.set_flag("datescore",val*5,"day","+")
                if game.get_flag_value("datescore") > 100:
                    game.set_flag("datescore",100,"day","=")
            if val > 0 and self.up_hook:
                for k in self.up_hook:
                    if k == "/10":
                        m = getattr(store, self.id)%10
                        
                        for i in range(0,int((m+val)/10)):
                            
                            if isinstance(self.up_hook["/10"], str) or isinstance(self.up_hook["/10"], unicode):
                                exec(self.up_hook["/10"])
                            else:
                                self.up_hook["/10"]() 
                    elif k == "/20":
                        m = getattr(store, self.id)%20
                        
                        for i in range(0,int((m+val)/20)):
                            if isinstance(self.up_hook["/20"], str) or isinstance(self.up_hook["/20"], unicode):
                                exec(self.up_hook["/20"])
                            else:
                                self.up_hook["/20"]() 
            val = self.normal_val(val + getattr(store, self.id))
            if val > getattr(store, self.id+"_max"):
                setattr(store, self.id, getattr(store, self.id+"_max"))
            elif val < getattr(store, self.id+"_min"):
                setattr(store, self.id, getattr(store, self.id+"_min"))
            else:
                setattr(store, self.id, val)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
