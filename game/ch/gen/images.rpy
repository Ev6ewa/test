init python:
    class CGPicker(object):
        def __call__(self, attr):
            for a in attr:
                if a in GIRLS:
                    g = GIRLS[a]
                    break
            if g:
                if g.get_flag_value("pregnant") >= 9:
                    attr.add("pregnant")
                if g.get_flag_value("haircut"):
                    attr.add("haircut")
                if g.get_flag_value("boobjob"):
                    attr.add("boobjob")
                if g.get_flag_value("collared") and g.sub >= 50:
                    attr.add("collar")
            
            return attr

    class XrayPicker(object):
        def __init__(self, girl):
            self.girl =  girl
        
        def __call__(self, attr):
            if persistent.xray:
                attr.add("xray")
            if self.girl.get_flag_value("pregnant") >= 9:
                attr.add("pregnant")
            if self.girl.get_flag_value("male") >= 40:
                attr.add("male40")
            if self.girl.get_flag_value("male") >= 60:
                attr.add("male60")
            return attr

init 1:

    layeredimage bar:
        always:
            "bar_background"
        always:
            "bar_man_back"
        always:
            "bar_foreground"

        group girl auto:
            attribute none default null
            attribute aletta null
            attribute audrey null
            attribute shiori null

        group exp auto variant "bree" if_any "bree":
            attribute normal default
        group exp auto variant "sasha" if_any "sasha":
            attribute normal default
        group exp auto variant "samantha" if_any "samantha":
            attribute normal default
        group exp auto variant "lexi" if_any "lexi":
            attribute normal default
        group exp auto variant "kleio" if_any "kleio":
            attribute normal default


        group exp auto variant "anna" if_any "anna":
            attribute normal default





        group outfit auto variant "hanna" if_any "hanna":
            attribute casual default
            attribute sport null

        always:
            "bar_man"
        always:
            "bar_light"



    layeredimage pool:
        attribute_function CGPicker()

        attribute pregnant null
        attribute collar null
        attribute haircut null
        attribute boobjob null
        attribute xray null
        attribute shiori null

        always:
            "pool_bg"

        group girl auto:
            attribute none default null

        if not game.get_flag_value("female"):
            if_any "shiori"
            "pool_spe_shiori_a"
        else:
            if_any "shiori"
            "pool_spe_shiori_b"

        group pregnant auto:
            if_any "pregnant"

        if not game.get_flag_value("female"):
            if_not "shiori"
            "pool_mc_mike"
        else:
            if_not "shiori"
            "pool_mc_bree"

        always:
            "pool_balls"

    layeredimage date pub burger:
        attribute_function CGPicker()

        attribute pregnant null
        attribute collar null
        attribute haircut null
        attribute boobjob null
        attribute xray null

        always:
            "date_pub_burger_bg"
        always:
            "date_pub_burger_bar"
        always:
            "date_pub_burger_stools_shadows" 

        if not game.get_flag_value("female"):
            "date_pub_burger_leg_mike"
        if game.get_flag_value("female"):
            "date_pub_burger_leg_bree"
        always:
            "date_pub_burger_stools" 

        group girl auto:
            attribute none default null

        group pregnant auto:
            if_any "pregnant"

        if not game.get_flag_value("female"):
            "date_pub_burger_mc_mike"
        else:
            "date_pub_burger_mc_bree"

        always:
            "date_pub_burger_light"


    layeredimage tv:
        always:
            "tv_bg"
        always:
            "tv_mike"

        attribute bree
        attribute sasha

        if sasha.get_clothes() == "sleep":
            if_any "sasha"
            "tv_sashaoutfit_sleep"
        if sasha.get_clothes() == "casual":
            if_any "sasha"
            "tv_sashaoutfit_casual"
        if sasha.get_clothes() == "underwear" and not get_flag_value("boobjob"):
            if_any "sasha"
            "tv_sashaoutfit_underwear"
        if sasha.get_clothes() == "underwear" and get_flag_value("boobjob"):
            if_any "sasha"
            "tv_sashaoutfit_underwearbb"
        if sasha.get_flag_value("collared") and sasha.sub() >= 50 and game.get_flag_value("homeharem"):
            if_all ["sasha","bree"]
            "tv_sasha_collar"
        if sasha.get_flag_value("collared") and sasha.sub() >= 50:
            if_any "sasha"
            if_not "bree"
            "tv_sasha_collar"
        if sasha.get_flag_value("haircut"):
            if_any "sasha"
            "tv_sasha_blonde"
        if sasha.get_piercings("nose"):
            if_any "sasha"
            "tv_sashapiercings_nose"
        if sasha.get_piercings("clit") and sasha.get_clothes() == "naked":
            if_any "sasha"
            "tv_sashapiercings_clit"
        if sasha.get_piercings("ears"):
            if_any "sasha"
            "tv_sashapiercings_ears"
        if sasha.get_piercings("lips"):
            if_any "sasha"
            "tv_sashapiercings_lips"

        if bree.get_clothes() == "sleep":
            if_any "bree"
            "tv_breeoutfit_sleep"
        if bree.get_clothes() == "casual":
            if_any "bree"
            "tv_breeoutfit_casual"
        if bree.get_clothes() == "underwear":
            if_any "bree"
            "tv_breeoutfit_underwear"
        if bree.get_flag_value("collared") and bree.sub() >= 50 and game.get_flag_value("homeharem"):
            if_all ["bree","bree"]
            "tv_bree_collar"
        if bree.get_flag_value("collared") and bree.sub() >= 50:
            if_any "bree"
            if_not "bree"
            "tv_bree_collar"
        if bree.get_piercings("nose"):
            if_any "bree"
            "tv_breepiercings_nose"
        if bree.get_piercings("nipples") and bree.get_clothes() == "naked":
            if_any "bree"
            "tv_breepiercings_nipples"
        if bree.get_piercings("ears"):
            if_any "bree"
            "tv_breepiercings_ears"
        if bree.get_piercings("lips"):
            if_any "bree"
            "tv_breepiercings_lips"

    layeredimage spank:
        attribute_function CGPicker()

        attribute pregnant null
        attribute collar null
        attribute haircut null
        attribute boobjob null
        attribute xray null

        group bg auto:
            attribute office default

        always:
            "spank_mike"

        group girl auto:
            attribute audrey default

        group pregnant auto if_any "pregnant"

        group exp auto variant "audrey" if_any "audrey":
            attribute normal null default
        group exp auto variant "palla" if_any "palla":
            attribute normal null default
        group exp auto variant "aletta" if_any "aletta":
            attribute normal null default
        group exp auto variant "lavish" if_any "lavish":
            attribute normal null default

        group outfit auto variant "audrey" if_any "audrey" if_not "pregnant":
            attribute work default
            attribute naked null

        group outfit auto variant "audrey_pregnant" if_all ["audrey","pregnant"]:
            attribute work default
            attribute naked null

        if audrey.get_piercings("nipples"):
            if_any "audrey"
            "spank_piercings_audrey_nipples"
        if audrey.get_piercings("nose"):
            if_any "audrey"
            "spank_piercings_audrey_nose"
        if audrey.get_piercings("tongue"):
            if_any "audrey"
            "spank_piercings_audrey_tongue"
        if audrey.get_piercings("navel"):
            if_any "audrey"
            if_not "pregnant"
            "spank_piercings_audrey_navel"
        if audrey.get_piercings("navel"):
            if_all ["audrey", "pregnant"]
            "spank_piercings_audrey_navel_pregnant"

        group outfit auto variant "palla" if_any "palla" if_not "pregnant":
            attribute casual default
            attribute naked null

        group outfit auto variant "palla_pregnant" if_all ["palla","pregnant"]:
            attribute casual default
            attribute naked null

        if palla.get_piercings("nipples"):
            if_any "palla"
            "spank_piercings_palla_nipples"
        if palla.get_piercings("nose"):
            if_any "palla"
            "spank_piercings_palla_nose"
        if palla.get_piercings("tongue"):
            if_any "palla"
            "spank_piercings_palla_tongue"
        if palla.get_piercings("navel"):
            if_all ["palla", "pregnant"]
            "spank_piercings_palla_navel_pregnant"
        if palla.get_piercings("navel"):
            if_any "palla"
            if_not "pregnant"
            "spank_piercings_palla_navel"
        if palla.get_piercings("clit"):
            if_all ["palla", "naked"]
            "spank_piercings_palla_clit"

        group outfit auto variant "aletta" if_any "aletta" if_not "pregnant":
            attribute work default
            attribute naked null

        group outfit auto variant "aletta_pregnant" if_all ["aletta","pregnant"]:
            attribute work default
            attribute naked null

        if aletta.get_piercings("nipples"):
            if_any "aletta"
            "spank_piercings_aletta_nipples"
        if aletta.get_piercings("nose"):
            if_any "aletta"
            "spank_piercings_aletta_nose"

        group outfit auto variant "lavish" if_any "lavish" if_not "pregnant":
            attribute work default
            attribute naked null

        group outfit auto variant "lavish_pregnant" if_all ["lavish","pregnant"]:
            attribute work default
            attribute naked null

        if lavish.get_piercings("nipples"):
            if_all ["lavish", "naked"]
            "spank_piercings_lavish_nipples"
        if lavish.get_piercings("ears"):
            if_any "lavish"
            "spank_piercings_lavish_ears"
        if lavish.get_piercings("tongue"):
            if_all ["lavish", "ahegao"]
            "spank_piercings_lavish_tongue"
        if lavish.get_piercings("clit"):
            if_all ["lavish", "naked"]
            "spank_piercings_lavish_clit"
        if lavish.get_piercings("lips"):
            if_any "lavish"
            "spank_piercings_lavish_lips"

        group fx auto multiple

        group arm auto:
            attribute spank default

        group moutfit auto:
            attribute mwork default
            attribute mnaked null

        group armoutfit auto variant "mwork" if_any "mwork"


    layeredimage date pub dart:
        attribute_function CGPicker()

        attribute pregnant null
        attribute collar null
        attribute haircut null
        attribute boobjob null
        attribute xray null

        always:
            "date_pub_dart_bg"

        group girl auto:
            attribute none default null

        group pregnant auto if_any "pregnant"
        group haircut auto if_any "haircut"
        group haircut auto variant "default" if_not "haircut"
        group line auto
        group boobjob auto if_any "boobjob"
        group collar auto if_any "collar"

        group fx auto:
            attribute nodart null

        if not game.get_flag_value("female"):
            "date_pub_dart_mc_mike"
        else:
            "date_pub_dart_mc_bree"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
