

init 1:
    layeredimage lexi:
        attribute_function Picker(lexi)

        attribute cum null

        group phone auto variant "a" if_any "a":
            attribute phone default
            attribute nophone null
        group phone auto variant "b" if_any "b":
            attribute phone default    
            attribute nophone null 
        group position:
            attribute a default
        attribute pregnant:
            if_any "a"
            "lexi_a_preg"
        attribute pregnant:
            if_any "b"
            "lexi_b_preg"



        group outfit auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group outfit auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null

        group exp auto variant "a" if_any "a":
            attribute normal default
        group exp auto variant "b" if_any "b":
            attribute normal default

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"           








        always:
            if_all ["cum","b"]
            "lexi_b_cum"
        always:
            if_all ["cum","a"]
            "lexi_a_cum"

    layeredimage lexi smartphone:
        always "lexi_smartphone"

    layeredimage lexi bj:
        attribute facial null
        attribute cum null

        group bg auto:
            attribute nightclub default
            attribute nobg null

        always:
            "lexi_bj_butt"

        group outfit auto variant "butt":
            attribute date default
            attribute naked null

        always:
            "lexi_bj_body"

        if lexi.get_piercings("nipples"):
            "lexi_bj_piercings_nipples"

        group outfit auto:
            attribute date default
            attribute naked null

        always:
            "lexi_bj_hair"

        group head auto:
            attribute normal default


        group exp auto if_any "normal" if_not ["deepthroat","suck"]:
            attribute smile default
            attribute open "lexi_bj_exp_smile"
            attribute closed "lexi_bj_exp_smile"
        group exp auto variant "deepthroat" if_any "deepthroat" if_not ["normal","suck"]:
            attribute open default
            attribute smile "lexi_bj_exp_suck_open"
            attribute showcum "lexi_bj_exp_suck_open"
            attribute swallow "lexi_bj_exp_suck_open"
        group exp auto variant "suck" if_any "suck" if_not ["deepthroat","normal"]:
            attribute open default
            attribute smile "lexi_bj_exp_suck_open"
            attribute showcum "lexi_bj_exp_suck_open"
            attribute swallow "lexi_bj_exp_suck_open"

        group facial auto if_any "facial":
            attribute nofacial null

        group man auto:
            attribute pants default

        group dick auto:
            if_not ["suck","slap"]
            attribute dick default
            attribute nodick null

        attribute slap:
            if_any "normal"
            "lexi_bj_slap"

        group cum auto if_any "cum":
            attribute nocum null

        group pull auto multiple if_not "deepthroat"
        group pull auto multiple variant "deepthroat" if_any "deepthroat"

    layeredimage lexi stand:
        group bg auto:
            attribute bedroom default

        if lexi.get_flag_value("pregnant") >= 9:
            "lexi_stand_body_pregnant" 
        else:
            "lexi_stand_body" 

        group exp auto:
            attribute normal default

        group hand auto:
            attribute pull default

        always:
            "lexi_stand_man_face"

        always:
            "lexi_stand_piercings_ears"

        group xray auto:
            attribute none null default

        attribute cum:
            "lexi_stand_cum_face"

        if lexi.get_piercings("tongue"):
            "lexi_stand_piercings_tongue"

        if lexi.get_piercings("nipples"):
            "lexi_stand_piercings_nipples"

        if lexi.get_piercings("navel") and not lexi.get_flag_value("pregnant") >= 9:
            if_not "pregnant"
            "lexi_stand_piercings_navel"

        if lexi.get_piercings("navel") and lexi.get_flag_value("pregnant") >= 9:
            if_not "pregnant"
            "lexi_stand_piercings_navel_pregnant"

        always:
            if_any "pool"
            "lexi_stand_water"

    layeredimage lexi kiss:
        always:
            "lexi_kiss"

        if lexi.get_piercings("nipples"):
            "lexi_kiss_piercings_nipples"

        group outfit auto:
            attribute casual default
            attribute naked null

        if lexi.get_piercings("tongue"):
            "lexi_kiss_piercings_tongue"


    layeredimage lexi stand2:
        group bg auto:
            attribute bedroom default

        always:
            "lexi_stand2_body"

        group exp auto:
            attribute normal default

        group outfit auto:
            attribute naked null default

        attribute manoutfit:
            "lexi_stand2_man_outfit"

        group xray auto:
            attribute none null default

        attribute cum:
            "lexi_stand2_cumface"

layeredimage lexi pimping:
    always:
        "lexi_pimping_bg"

    group pos auto

    if lexi.get_flag_value("pregnant") >= 9:
        if_any "fuck"
        "lexi_pimping_pregnant_fuck" 
    if lexi.get_flag_value("pregnant") >= 9:
        if_any "laying"
        "lexi_pimping_pregnant_laying" 
    if lexi.get_flag_value("pregnant") >= 9:
        if_any "blowjob"
        "lexi_pimping_pregnant_blowjob" 
    if lexi.get_piercings("tongue"):
        if_any "fuck"
        "lexi_pimping_piercings_tongue_fuck"
    if lexi.get_piercings("nipples"):
        if_any "fuck"
        "lexi_pimping_piercings_nipples_fuck"
    if lexi.get_piercings("nipples"):
        if_all ["blowjob","naked"]
        "lexi_pimping_piercings_nipples_blowjob"
    if lexi.get_piercings("nose"):
        if_any "fuck"
        "lexi_pimping_piercings_nose_fuck"

    group outfit auto:
        if_any "blowjob"
        attribute naked null default

    always:
        "lexi_pimping_glass"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
