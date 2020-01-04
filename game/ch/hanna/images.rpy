

init 1:
    layeredimage hanna:
        attribute_function Picker(hanna)

        attribute pregnant null

        group position auto variant "pregnant" if_any "pregnant"
        group position auto if_not "pregnant"

        group exp auto:
            attribute normal default

        group piercings multiple auto:
            attribute piercings_navel:
                if_not "pregnant"
        group piercings multiple auto:
            attribute piercings_navel:
                if_not "pregnant"


        group acc multiple auto variant "a" if_any "a"
        group acc multiple auto variant "b" if_any "b"
        group outfit auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group outfit auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null

        attribute pubes:
            if_all ["naked","a"]
            "hanna_pubes_a"  
        attribute pubes:
            if_all ["naked","b"]
            "hanna_pubes_b"  



    layeredimage hanna smartphone:
        always "hanna_smartphone"

    layeredimage hanna mast:
        always "hanna_mast_back"
        always "hanna_mast_body"
        group exp auto:
            attribute a default
        attribute outfit:
            "hanna_mast_top"
        attribute outfit:
            "hanna_mast_bot"
        attribute squirt:
            "hanna_mast_squirt"
        attribute wet:
            "hanna_mast_wet"
        always "hanna_mast_light"

    layeredimage hanna kiss:
        group outfit auto:
            attribute casual null default
            attribute naked null
            attribute date null
            attribute sport null
            attribute sexyswimsuit null
            attribute swimsuit null
            attribute underwear null
            attribute work null

    layeredimage hanna bj:
        always "hanna_bj_bg"
        always "hanna_bj_body"
        always "hanna_bj_man"

        group face auto:
            attribute normal default
        group exp auto variant "suck" if_any "suck":
            attribute open default
        group exp auto variant "normal" if_any "normal":
            attribute open default
        group dick auto:
            attribute b default

        if hanna.get_piercings("tongue"):
            if_not ["suck"]
            "hanna_bj_piercings_tongue"
        if hanna.get_piercings("nipples"):
            if_not ["outfit"]
            "hanna_bj_piercings_nipples"
        if hanna.get_piercings("nose"):
            if_not ["suck"]
            "hanna_bj_piercings_nose"    

        attribute outfit:
            "hanna_bj_outfit"


        attribute cumshot:
            if_any "normal"
            if_not "suck"
            "hanna_bj_cumshot"

        attribute cumshot:
            if_any "suck"
            if_not "normal"
            "hanna_bj_cum_mouth"

        attribute cum:
            "hanna_bj_cum_body"

        attribute lotion:
            if_any "b"
            if_not "a"
            "hanna_bj_cum_body"

        attribute wet:
            if_any "b"
            if_not "a"
            "hanna_bj_wet_dick"

        always "hanna_bj_water_fx"

    layeredimage hanna cowgirl:
        always:
            "hanna_cowgirl_bg"
        always:
            "hanna_cowgirl_man"
        always:
            "hanna_cowgirl_dick"
        group fuck auto:
            attribute up default
        if hanna.get_flag_value("pregnant") >= 9:
            "hanna_cowgirl_pregnant"
        always:
            "hanna_cowgirl_body"
        group exp auto:
            attribute smile default
        group boob auto:
            attribute normal default
        group fx multiple auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
