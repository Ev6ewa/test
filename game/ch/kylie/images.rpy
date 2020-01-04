init 1:
    layeredimage kylie:
        attribute_function Picker(kylie)

        attribute pregnant null

        group position auto
        group pregnant auto:
            if_any "pregnant"

        group exp auto:
            attribute normal default

        attribute pubes:
            if_any ["naked", "sexyswimsuit"]
            "kylie_pubes"  

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"           

        group top auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group top auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group top auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group top auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null
        group bot auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group bot auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null

        group acc auto variant "b" if_any "b"
        group acc auto variant "a" if_any "a"
        group acc auto

        attribute knife:
            "kylie_knife"

        attribute blood:
            if_any "knife"
            "kylie_knife_blood"
        attribute blood:
            "kylie_blood"

    layeredimage kylie smartphone:
        always "kylie_smartphone"

    layeredimage kylie memory:
        always "kylie_peeping"

    layeredimage kylie missionary:
        always "kylie_missionary_bg"
        always "kylie_missionary_body"

        group exp auto:
            attribute normal default

        if kylie.get_piercings("clit"):
            "kylie_missionary_piercings_clit"



        if kylie.get_piercings("nipples"):
            "kylie_missionary_piercings_nipples"
        if kylie.get_piercings("nose"):
            "kylie_missionary_piercings_nose"
        if kylie.get_piercings("lips"):
            if_not "ahegao"
            "kylie_missionary_piercings_lips"

        group dick auto:
            attribute out default

        attribute condom:
            "kylie_missionary_condom"

        attribute blood:
            "kylie_missionary_blood"

        attribute bellycum:
            "kylie_missionary_bellycum"

        attribute cum null
        group cum auto:
            if_not "bellycum"
            if_any "cum"

    layeredimage kylie cowgirl:
        always "kylie_cowgirl_bg"
        always "kylie_cowgirl_body"

        if kylie.get_flag_value("pregnant") >= 9:
            "kylie_cowgirl_pregnant"

        group exp auto:
            attribute normal default

        if kylie.get_piercings("nipples"):
            "kylie_cowgirl_piercings_nipples"
        if kylie.get_piercings("clit"):
            "kylie_cowgirl_piercings_clit"
        if kylie.get_piercings("nose"):
            "kylie_cowgirl_piercings_nose"
        if kylie.get_piercings("ears"):
            "kylie_cowgirl_piercings_ears"

        group dick auto:
            attribute out default

        attribute condom:
            "kylie_cowgirl_condom"

        group fx auto

        attribute cum null
        group cum auto:
            if_not ["condom"]
            if_any "cum"

        attribute arm:
            "kylie_cowgirl_arm"

    layeredimage kylie doggy:
        always "kylie_doggy_bg"
        always "kylie_doggy_body"
        always "kylie_doggy_mike"

        group exp auto:
            attribute normal default

        if kylie.get_piercings("nipples"):
            "kylie_doggy_piercings_nipples"
        if kylie.get_piercings("nose"):
            "kylie_doggy_piercings_nose"
        if kylie.get_piercings("ears"):
            "kylie_doggy_piercings_ears"

        group dick auto:
            attribute out default

        attribute condom:
            "kylie_doggy_condom"

        group fx auto
        attribute cum null
        group cum auto:
            if_not ["bodycum", "condom"]
            if_any "cum"

    layeredimage kylie kiss:
        attribute_function MyPicker(kylie)
        always:
            "kylie_kiss"

        attribute pregnant:
            "kylie_kiss_pregnant"

        if kylie.get_piercings("nipples"):
            if_any "naked"
            "kylie_kiss_piercings_nipples"

        if kylie.get_piercings("ears"):
            "kylie_kiss_piercings_ears"

        if kylie.get_piercings("lips"):
            "kylie_kiss_piercings_lips"

        group outfit auto if_not "pregnant":
            attribute casual default
            attribute naked null
        group outfit auto variant "pregnant" if_any "pregnant":
            attribute casual default
            attribute naked null

        group outfitmike auto:
            attribute normal default
            attribute nude null

        group acc auto

    layeredimage kylie gift:
        always:
            "kylie_gift"

        group box auto:
            attribute closed default

        group exp auto:
            attribute normal default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
