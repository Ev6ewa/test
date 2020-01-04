init 1:
    layeredimage audrey:
        attribute_function Picker(audrey)


        group position auto



        attribute pubes:
            if_all ["naked"]
            "audrey_pubes"


        attribute pregnant if_any "a":
            "audrey_pregnant_a"
        attribute pregnant if_any "b":
            "audrey_pregnant_b"


        group exp auto:
            attribute normal default

        attribute collar:
            "audrey_collar"
        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"           

        group outfit auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group outfit auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null

        attribute strapon if_any "naked"

        attribute sunglasses:
            "audrey_sunglasses"
        if audrey.get_flag_value("storynecklace"):
            if_any ["date", "casual", "work"]
            "audrey_necklace"

    layeredimage audrey smartphone:
        always "audrey_smartphone"

    layeredimage audrey note:
        always "audrey_note"

    layeredimage audrey spoon:
        always "audrey_spoon_background"
        always "audrey_spoon_body"

        if audrey.get_flag_value("pubes",audrey.pubes):
            "audrey_pubes"  
        group exp auto:
            attribute normal default

        attribute cum_a:
            "audrey_spoon_cum_a"
        attribute cum_b:
            "audrey_spoon_cum_b"

        group penis:
            attribute penis_a:
                "audrey_spoon_penis_a"
            attribute penis_b:
                "audrey_spoon_penis_b"
            attribute fuck:
                "audrey_spoon_fuck"

        group creampie:
            if_any "fuck"
            attribute creampie_a:
                "audrey_spoon_creampie_a"
            attribute creampie_b:
                "audrey_spoon_creampie_b"

        group hand auto:
            attribute squeeze default
        if audrey.get_piercings("clit"):
            if_not "penis_a"
            "audrey_spoon_piercings_clit"
        if audrey.get_piercings("tongue"):
            "audrey_spoon_piercings_tongue"
        if audrey.get_piercings("nipples"):
            if_any "choke"
            "audrey_spoon_piercings_nipples_a"
        elif audrey.get_piercings("nipples"):
            "audrey_spoon_piercings_nipples_b"
        if audrey.get_piercings("navel"):
            "audrey_spoon_piercings_navel"
        if audrey.get_piercings("nose"):
            "audrey_spoon_piercings_nose"    
        attribute cumshot:
            if_any "penis_b"
            "audrey_spoon_cumshot"
        attribute xray:
            if_any "xray"
            "audrey_spoon_xray"
        always "audrey_spoon_light"

    layeredimage audrey danny:
        always "audrey_danny"
        always "audrey_danny_glasses"
        always "audrey_danny_piercings"

    layeredimage audrey eat:
        always "audrey_eat_bg"
        always "audrey_eat_man"

        group position auto:
            attribute eat default

        attribute dick:
            if_not ["handjob", "kiss"]
            "audrey_eat_dick_out"

        group exp auto:
            if_not ["kiss"]
            attribute normal default

        group hand auto:
            if_any "handjob"
            attribute rub default

        if audrey.get_piercings("tongue"):
            if_any "eat"
            if_not ["handjob","kiss"]
            "audrey_eat_piercings_eat_tongue"
        if audrey.get_piercings("nose"):
            if_any "eat"
            if_not ["handjob","kiss"]
            "audrey_eat_piercings_eat_nose"
        if audrey.get_piercings("navel"):
            if_any "eat"
            if_not ["handjob","kiss"]
            "audrey_eat_piercings_eat_navel"

        if audrey.get_piercings("tongue"):
            if_any "handjob"
            if_not ["eat","kiss"]
            "audrey_eat_piercings_handjob_tongue"
        if audrey.get_piercings("nose"):
            if_any "handjob"
            if_not ["eat","kiss"]
            "audrey_eat_piercings_handjob_nose"
        if audrey.get_piercings("navel"):
            if_any "handjob"
            if_not ["eat","kiss"]
            "audrey_eat_piercings_handjob_navel"

        if audrey.get_piercings("tongue"):
            if_any "kiss"
            if_not ["eat","handjob"]
            "audrey_eat_piercings_kiss_tongue"
        if audrey.get_piercings("nose"):
            if_any "kiss"
            if_not ["eat","handjob"]
            "audrey_eat_piercings_kiss_nose"
        if audrey.get_piercings("navel"):
            if_any "kiss"
            if_not ["eat","handjob"]
            "audrey_eat_piercings_kiss_navel"

        group cum auto
        group table auto:
            attribute solid default


    layeredimage audrey desk:
        always "audrey_desk_bg"
        always "audrey_desk_base"

        group position auto:
            attribute down default

        if audrey.get_flag_value("pregnant") >= 9:
            "audrey_desk_preg"

        group exp auto:
            if_any "up"
            attribute ahegao default

        if audrey.get_piercings("tongue"):
            if_any "up"
            "audrey_desk_piercings_tongue"
        if audrey.get_piercings("nose"):
            if_any "up"
            "audrey_desk_piercings_nose"
        if audrey.get_piercings("nipples"):
            if_any "up"
            "audrey_desk_piercings_nipples"

        group fx auto

    layeredimage audrey kiss:
        attribute_function MyPicker(audrey)
        attribute pregnant null
        always:
            "audrey_kiss"




        group outfit auto:
            attribute casual default
            attribute naked null

        if audrey.get_flag_value("collared") and audrey.sub >= 50:
            "audrey_kiss_collar"

        group outfitmike auto:
            attribute normal default
            attribute naked null

        group acc auto multiple
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
