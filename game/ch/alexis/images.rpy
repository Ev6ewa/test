init 1:
    layeredimage alexis:
        attribute_function Picker(alexis)


        group position auto


        attribute pregnant if_any "a":
            "alexis_pregnant_a"
        attribute pregnant if_any "b":
            "alexis_pregnant_b"


        attribute blush:
            "alexis_blush"


        group exp auto:
            attribute normal default


        group piercings multiple auto           



        group bot auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group bot auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null
        group top auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group top auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group top auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group top auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null

        group acc multiple auto   


        attribute pubes:
            if_all ["naked"]
            "alexis_pubes"  

    layeredimage alexis smartphone:
        always "alexis_smartphone"

    layeredimage alexis reverse:
        always "alexis_reverse_body"
        if alexis.get_flag_value("pregnant") >= 9:
            "alexis_reverse_pregnant"
        if alexis.get_flag_value("collared") and alexis.sub() >= 50:
            "alexis_reverse_collar"
        group bg auto:
            attribute bedroom default
        group exp auto:
            attribute normal default
        group dick auto:
            if_any "toilets"
            attribute dickin default
        attribute condom:
            if_any "bedroom"
            "alexis_reverse_condom"
        if alexis.get_piercings("clit"):
            "alexis_reverse_piercings_clit"


        if alexis.get_piercings("nipples"):
            "alexis_reverse_piercings_nipples"
        if alexis.get_piercings("navel") and not alexis.get_flag_value("pregnant") >= 9:
            "alexis_reverse_piercings_navel"
        if alexis.get_piercings("navel") and alexis.get_flag_value("pregnant") >= 9:
            "alexis_reverse_piercings_navel_preg"
        if alexis.get_piercings("nose"):
            "alexis_reverse_piercings_nose"

        group cum auto if_not "toilets"
        group cum auto variant "toilets" if_any "toilets"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
