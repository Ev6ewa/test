init 1:
    layeredimage aletta:
        attribute_function Picker(aletta)


        always:
            if_not ["hairdown", "helmet"]
            "aletta_hairup"


        group position auto

        attribute pregnant:
            "aletta_pregnant_belly"


        group exp auto:
            attribute normal default

        group piercings multiple auto         

        attribute collar:
            "aletta_collar"

        group outfit auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group outfit auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null

        group necklace auto:
            if_not "collar"

        group acc multiple auto


        group hair auto variant "a" if_any "a" if_not "helmet"
        group hair auto variant "b" if_any "b" if_not "helmet"



        attribute pubes:
            if_all ["naked"]
            "aletta_pubes"  

        always:
            if_any "a"
            if_not "helmet"
            "aletta_glasses_a"
        always:
            if_any "b"
            if_not "helmet"
            "aletta_glasses_b"

    layeredimage aletta smartphone:
        always "aletta_smartphone"

    layeredimage aletta oral:
        always "aletta_oral_bg_office"
        always "aletta_oral_body"

        group exp:
            attribute orgasm null
            attribute normal null default

        always:
            if_any "orgasm"
            "aletta_oral_eyes_closed"
        always:
            if_any "normal"
            "aletta_oral_eyes_open"
        always:
            if_any "normal"
            "aletta_oral_mouth_closed"
        always:
            if_any "orgasm"
            "aletta_oral_mouth_open"

        always "aletta_oral_glasses"

        group man:
            attribute noman null
            attribute mana default:
                "aletta_oral_man"
            attribute manb:
                "aletta_oral_manb"

        attribute arm:
            if_any "mana"
            "aletta_oral_man_arm"

        group eyes:
            attribute open if_any "mana" default:
                "aletta_oral_man_eyes_open"
            attribute open if_any "manb" default:
                "aletta_oral_manb_eyes_open"
            attribute closed if_any "mana":
                "aletta_oral_man_eyes_closed"
            attribute closed if_any "manb":
                "aletta_oral_manb_eyes_closed"

        attribute tongue:
            if_any "mana"
            "aletta_oral_man_tongue"

        attribute cum:
            "aletta_oral_cum_a"

    layeredimage aletta kiss:
        attribute_function MyPicker(aletta)
        attribute pregnant null
        group acc1 auto multiple
        always:
            if_any "suit"
            "aletta_kiss_hair_do"
        always:
            if_not "suit"
            "aletta_kiss_hair_up"

        always:
            "aletta_kiss"




        group outfit auto:
            attribute casual default
            attribute naked null

        attribute collar:
            "aletta_kiss_collar"

        group outfitmike auto:
            attribute normal default
            attribute naked null

        group acc2 auto multiple
        group acc3 auto multiple






    layeredimage aletta cowgirl:
        always:
            "aletta_cowgirl_bg"

        group exp auto:
            attribute normal default

        if aletta.get_flag_value("pregnant") >= 9:
            "aletta_cowgirl_pregnant"

        if aletta.get_flag_value("collared") and aletta.sub >= 75:
            "aletta_cowgirl_collar"

        if aletta.get_piercings("nipples"):
            "aletta_cowgirl_piercings_nipples"

        attribute cumface:
            "aletta_cowgirl_cumface"

    layeredimage aletta shooting:
        group bg auto:
            attribute range default

        attribute mike:
            "aletta_shooting_mike"

        group expmike auto:
            if_any "mike"
            attribute normal default

        group position:
            attribute finger:
                if_not "mike"
                "aletta_shooting_finger"
            attribute bj:
                if_any "mike"
                null

        always:
            if_not "mike"
            "aletta_shooting_body"

        if aletta.get_flag_value("pubes",aletta.pubes):
            if_not "mike"
            "aletta_shooting_pubes"

        group outfit auto:
            if_not "mike"
            attribute closed default
            attribute naked null

        group exp auto:
            if_not "mike"
            attribute normal default

        always:
            if_not "mike"
            "aletta_shooting_glasses"

        always:
            if_not "mike"
            "aletta_shooting_arms"

        group outfitarms auto:
            if_not "mike"
            attribute clothed default
            attribute naked null

        attribute fire:
            if_not "mike"
            "aletta_shooting_fire1"

        attribute fire:
            if_any "mike"
            "aletta_shooting_fire2"

        attribute juice:
            if_not "mike"
            "aletta_shooting_juice"

        always:
            if_any "finger"
            "aletta_shooting_finger_arms"

        always:
            if_any "finger"
            "aletta_shooting_finger_head"

        attribute bj:
            if_any "mike"
            "aletta_shooting_bj"

        group bj auto:
            if_any "bj"
            attribute suck default

        group bj_cumshot auto if_any "bj"


        group fg auto

    layeredimage aletta ride:
        always:
            "aletta_ride_bg"

        always:
            "aletta_ride_bike"

        attribute mike:
            "aletta_ride_hero"

        always:
            "aletta_ride_body"

        group suit auto:
            attribute closed default

        always:
            if_any "mike"
            "aletta_ride_hero_leg"

        group righthand auto:
            if_any "mike"
            attribute waist default

        group lefthand auto:
            if_any "mike"
            attribute lwaist default

        always:
            "aletta_ride_bike_front"

        group exp auto:
            attribute normal default

        always:
            if_any "mike"
            "aletta_ride_hero_face"

        always:
            "aletta_ride_glasses"

        always:
            "aletta_ride_arm"

        always:
            "aletta_ride_helmet"

        always:
            "aletta_ride_blur"

    layeredimage aletta whip:
        always:
            "aletta_whip_bg"
        always:
            "aletta_whip_mike"
        group dick auto:
            attribute erect default
        group girl auto multiple
        group fx auto multiple
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
