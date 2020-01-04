init 1:
    layeredimage shiori:
        attribute_function Picker(shiori)


        group position auto
        attribute pregnant if_any "a":
            "shiori_pregnant_a"
        attribute pregnant if_any "b":
            "shiori_pregnant_b"

        group exp auto:
            attribute normal default

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"           

        attribute collar:
            "shiori_collar"
        group outfit auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group outfit auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null
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

        attribute pubes:
            if_all ["naked","b"]
            "shiori_pubes_b"

        group necklace auto:
            if_not "collar"

        group acc auto multiple

    layeredimage shiori smartphone:
        always "shiori_smartphone"

    layeredimage shiori kiss:
        attribute_function MyPicker(shiori)
        attribute pregnant null
        always:
            "shiori_kiss"




        group outfit auto:
            attribute casual default
            attribute naked null

        attribute collar:
            "shiori_kiss_collar"
        if "nipples" in shiori.get_piercings():
            if_any "naked"
            "shiori_kiss_piercings_nipples"
        if "nose" in shiori.get_piercings():
            "shiori_kiss_piercings_nose"

        group outfitmike auto:
            attribute normal default
            attribute naked null

        group acc auto multiple:
            if_not "collar"






    layeredimage shiori spanking:
        always "shiori_spanking_bg"
        always "shiori_spanking_body"

        group exp auto:
            attribute normal default

        attribute blush "shiori_spanking_blush"

        group top auto:
            attribute top default

        group outfit auto:
            attribute bot default

        group red auto
        group slap auto
        group fx auto

        attribute leak "shiori_spanking_leak"

        attribute man:
            "shiori_spanking_man"
        attribute man:
            "shiori_spanking_man_eyes"

        attribute foot "shiori_spanking_foot"

    layeredimage shiori bj:
        attribute outfit null
        group bg auto:
            attribute bedroom default
        always:
            if_any ["office"]
            "shiori_bj_desk_back"
        group man auto
        group body auto:
            attribute default default

        always if_any "outfit":
            "shiori_bj_bottom"               

        always if_all ["outfit","default"]:
            "shiori_bj_outfit_suck"               

        always if_all ["outfit","boobs"]:
            "shiori_bj_outfit_boobs"               


        group face:
            attribute base default:
                "shiori_bj_face"

        group exp auto variant "boobs" if_any "boobs":
            attribute suck default

        group exp auto variant "default" if_any "default":
            attribute smile default

        group dick auto:
            if_not ["suck","boobs"]
            attribute high default

        attribute hand:
            if_not ["suck"]
            "shiori_bj_hand"

        always if_all ["outfit"]:
            if_any ["hand","suck"]
            if_not ["boobs"]

            "shiori_bj_outfit_hand"               

        group cumshot:
            attribute cumshot:
                if_any "suck"
                if_not "high"
                "shiori_bj_suck_wet2"

            attribute cumshot:
                if_any "high"
                if_not "suck"
                "shiori_bj_cumshot"

            attribute nocumshot null

        group facial:
            attribute facial:
                if_any "default"
                if_not "boobs"
                "shiori_bj_facial_default"

            attribute facial:
                if_any "boobs"
                if_not "default"
                "shiori_bj_facial_boobs"

            attribute nofacial null

        always "shiori_bj_leg"
        always:
            if_any ["office"]
            "shiori_bj_chair"
        always:
            if_any ["office"]
            "shiori_bj_shadow"
        always:
            if_any ["office"]
            "shiori_bj_desk"

    layeredimage shiori milk:
        always:
            "shiori_milk_bg"

        always:
            "shiori_milk_shiori"

        if shiori.get_piercings("nipples"):
            "shiori_milk_piercings_nipples"
        if shiori.get_piercings("nose"):
            "shiori_milke_piercings_nose"
        if shiori.get_piercings("lips"):
            "shiori_milk_piercings_lips"

        always:
            "shiori_milk_milk"

        always:
            "shiori_milk_desk"

        always:
            "shiori_milk_light"


    layeredimage shiori reverse:
        attribute_function XrayPicker(shiori)
        group bg auto:
            attribute bedroom default

        always "shiori_reverse_body"

        if shiori.get_flag_value("pregnant") >= 9:
            "shiori_reverse_pregnant"

        group exp auto:
            attribute normal default

        if shiori.get_piercings("nipples"):
            "shiori_reverse_piercings_nipples"
        if shiori.get_piercings("nose"):
            "shiori_reverse_piercings_nose"
        if shiori.get_piercings("clit"):
            "shiori_reverse_piercings_clit"
        if shiori.get_piercings("navel") and not shiori.get_flag_value("pregnant") >= 9:
            "shiori_reverse_piercings_navel"
        if shiori.get_piercings("navel") and shiori.get_flag_value("pregnant") >= 9:
            "shiori_reverse_piercings_navel_pregnant"

        group dick auto:
            attribute out default
            attribute nodick null

        group xray auto:
            if_any "xray"

        group cum auto

        attribute milk:
            "shiori_reverse_milk"

        attribute wet:
            "shiori_reverse_wet"

        attribute squirt:
            "shiori_reverse_squirt"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
