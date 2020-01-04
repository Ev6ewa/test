init -20 python:
    class Flag(store.object):
        def __init__(self, value=True, duration=1, hook = None):
            self.duration = duration
            self.value = value
            self.hook = hook
        
        def update(self):
            
            if isinstance(self.duration, int) and not self.duration == 0:
                self.duration -= 1
            elif (self.duration == "week" and game.week_day == 1) or (self.duration == "month" and game.day == 1):
                self.duration = 0
            if self.duration == 0 or self.duration == "day":
                
                if self.hook:
                    if isinstance(self.hook, str) or isinstance(self.hook, unicode):
                        renpy.call_in_new_context(self.hook)
                    else:
                        self.hook()
                return False
            
            return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
