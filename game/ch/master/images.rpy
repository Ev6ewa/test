init python:
    class MyPicker(object):
        def __init__(self, girl):
            self.girl =  girl
        
        def __call__(self, attr):
            if self.girl.get_flag_value("collared") and self.girl.sub() >= 50:
                attr.add("collar")
            if self.girl.get_flag_value("boobjob"):
                attr.add("boobjob")
            if self.girl.get_flag_value("haircut"):
                attr.add("haircut")
            if self.girl.get_flag_value("pubes",self.girl.pubes):
                attr.add("pubes")
            for o in attr:
                if self.girl.get_flag_value("sexy"+o):
                    attr.remove(o)
                    attr.add("sexy"+o)
            if self.girl.get_flag_value("pregnant") >= 9:
                attr.add("pregnant")
            return attr

init 1:
    layeredimage master:
        group position auto:
            attribute a default

        group exp auto:
            attribute normal null default

        attribute glasses:
            "master_glasses"

    layeredimage beach bj:
        attribute pubes null
        always:
            "beach_bj_bg"

        group man auto:
            attribute master default

        group position auto:
            attribute handjob default

        if bree.get_piercings("nipples"):
            if_any "handjob"
            "beach_bj_piercings_handjob_nipples"
        if bree.get_piercings("tongue"):
            if_any "handjob"
            "beach_bj_piercings_handjob_tongue"
        if bree.get_piercings("nose"):
            if_any "handjob"
            "beach_bj_piercings_handjob_nose"    
        if bree.get_flag_value("pregnant") >= 9:
            "beach_bj_handjob_pregnant"
        if bree.get_flag_value("collared") > 7 and bree.sub >= 50:
            "beach_bj_handjob_collar"

        if bree.get_piercings("nipples"):
            if_any "blowjob"
            "beach_bj_piercings_blowjob_nipples"
        if bree.get_piercings("tongue"):
            if_any "blowjob"
            "beach_bj_piercings_blowjob_tongue"
        if bree.get_piercings("nose"):
            if_any "blowjob"
            "beach_bj_piercings_blowjob_nose"    
        if bree.get_flag_value("pregnant") >= 9:
            "beach_bj_blowjob_pregnant"
        if bree.get_flag_value("collared") > 7 and bree.sub >= 50:
            "beach_bj_blowjob_collar"

        group outfit auto variant "blowjob" if_any "blowjob":
            attribute naked null
        group outfit auto variant "handjob" if_any "handjob":
            attribute naked null

        group exp auto variant "blowjob" if_any "blowjob":
            attribute open default
        group exp auto variant "handjob" if_any "handjob":
            attribute open default

        attribute cum null
        group cumshot auto:
            if_any "cum"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
