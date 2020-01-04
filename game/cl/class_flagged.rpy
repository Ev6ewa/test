init -30 python:
    import os



    class Flagged(store.object):
        
        def clean_up(self):
            for f in list(FLAGS.keys()):
                if not FLAGS[f].update():
                    del FLAGS[f]
        
        def set_flag(self, flag, val=True, duration="permanent", mod="=", hook = None):
            
            flag = self.id + flag
            if flag in FLAGS:
                flag = FLAGS[flag]
                if mod == "=":
                    flag.value = val
                elif mod == "+":
                    flag.value += val
                elif mod == "-":
                    flag.value -= val
            else:
                if mod == "-":
                    val = -val
                FLAGS[flag] = Flag(val, duration, hook)
        
        def has_flag(self, flag):
            flag = self.id + flag
            if flag in FLAGS:
                return True
            else:
                return False
        
        def get_flag_value(self, flag, default=0):
            flag = self.id + flag
            if flag in FLAGS:
                
                return FLAGS[flag].value
            else:
                
                return default
        
        def get_flag(self, flag):
            flag = self.id + flag
            if flag in FLAGS:
                return FLAGS[flag]
            else:
                return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
