init 1:
    layeredimage samantha:
        attribute_function Picker(samantha)

        attribute pregnant null

        group position auto variant "pregnant" if_any "pregnant"
        group position auto if_not "pregnant"

        group exp auto:
            attribute normal default

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"           

        attribute collar:
            if_all ["a"]
            if_not "b"
            "samantha_collar_a"  
        attribute collar:
            if_all ["b"]
            if_not "a"
            "samantha_collar_b"

        group outfit auto variant "a" if_any "a" if_not "pregnant":
            attribute naked null
        group outfit auto variant "b" if_any "b" if_not "pregnant":
            attribute naked null
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"]:
            attribute naked null
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"]:
            attribute naked null

        attribute pubes:
            if_all ["naked"]
            "samantha_pubes"  

        if samantha.get_flag_value("engaged") and samantha.love < 100:
            "samantha_ring_a"  
        elif samantha.get_flag_value("engaged") and samantha.love >= 100:
            "samantha_ring_b"  

    layeredimage samantha smartphone:
        always "samantha_smartphone"


    layeredimage samantha babyshopping:
        always "samantha_babyshopping"


    layeredimage samantha cowgirl:

        always "samantha_cowgirl_background"

        always "samantha_cowgirl_man"

        if samantha.get_flag_value("pregnant") >= 9:
            "samantha_cowgirl_pregnant"
        else:
            "samantha_cowgirl_normal"

        attribute fuck:
            "samantha_cowgirl_fuck"

        if samantha.get_flag_value("pubes",samantha.pubes):
            "samantha_cowgirl_pubes" 

        if samantha.get_piercings("tongue"):
            if_any ["orgasm","orgasm2"]
            "samantha_cowgirl_piercing_tongue"

        if samantha.get_piercings("nipples"):
            "samantha_cowgirl_piercing_nipples"

        if samantha.get_piercings("clit"):
            if_any "fuck"
            "samantha_cowgirl_piercing_clitfuck"
        elif samantha.get_piercings("clit"):
            "samantha_cowgirl_piercing_clit"

        if samantha.get_piercings("navel") and samantha.get_flag_value("pregnant") >= 9:
            "samantha_cowgirl_piercing_navelpregnant"
        elif samantha.get_piercings("navel"):
            "samantha_cowgirl_piercing_navel"



        attribute dickout:
            "samantha_cowgirl_dickout"

        always:
            "samantha_cowgirl_mpubes"


        group hand auto

        group exp auto:
            attribute normal default

        attribute fx:
            "samantha_cowgirl_fx"
        attribute blush:
            "samantha_cowgirl_blush"
        attribute cum:
            "samantha_cowgirl_cum"
        attribute cumshot:
            "samantha_cowgirl_cumshot"
        attribute cumshot2:
            "samantha_cowgirl_cumshot2"

    layeredimage samantha reverse:

        always "samantha_cowgirl_background"

        always "samantha_cowgirl_man"

        always:
            "samantha_reverse_fuck"

        if samantha.get_flag_value("pregnant") >= 9:
            "samantha_reverse_pregnant"
        else:
            "samantha_reverse_normal"

        attribute dickout:
            "samantha_cowgirl_dickout"

        always:
            "samantha_cowgirl_mpubes"

        group exp auto:
            attribute normal default

        attribute fx:
            "samantha_cowgirl_fx"
        attribute cum:
            "samantha_reverse_cum"
        attribute cumshot:
            "samantha_cowgirl_cumshot"
        attribute cumshot2:
            "samantha_cowgirl_cumshot2"

    layeredimage samantha kiss:
        always:
            "samantha_kiss"

        if samantha.get_piercings("nipples"):
            if_any "naked"
            "samantha_kiss_piercings_nipples"

        if samantha.get_piercings("ears"):
            "samantha_kiss_piercings_ears"

        if samantha.get_piercings("lips"):
            "samantha_kiss_piercings_lips"

        group outfit auto:
            attribute casual default
            attribute naked null

        group man auto:
            attribute normal default
            attribute nude null

    layeredimage samantha bj:

        group stuff:
            attribute suck null
            attribute nosuck default

        attribute cumshot null

        always "samantha_bj_bg"

        always "samantha_bj_body"

        always "samantha_bj_man"

        always:
            if_any ["suck"]
            "samantha_bj_head_suck"

        always:
            if_not ["suck"]
            "samantha_bj_head_normal"

        group exp:
            attribute closed default:
                if_any ["suck"]
                "samantha_bj_exp_suckA"
            attribute open:
                if_any ["suck"]
                "samantha_bj_exp_suckB"

        group exp2:
            attribute normal default:
                if_not ["suck"]
                "samantha_bj_exp_normal"
            attribute surprise:
                if_not ["suck"]
                "samantha_bj_exp_surprise"

        if samantha.get_piercings("tongue"):
            if_any ["surprise"]
            if_not ["normal", "suck"]
            "samantha_bj_piercings_tongueB"

        if samantha.get_piercings("tongue"):
            if_not ["surprise", "suck"]
            if_any ["normal"]
            "samantha_bj_piercings_tongueA"


        group dick:
            attribute out default:
                if_not ["suck"]
                "samantha_bj_dick"
            attribute inside:
                if_not ["suck"]
                "samantha_bj_dick_tits"

        always:
            if_all ["suck", "cumshot"]
            "samantha_bj_cum_mouth"

        always:
            if_not ["suck"]
            if_any ["cumshot"]
            "samantha_bj_cumshot"

        group arms auto

        attribute cumface:
            if_not ["suck"]
            "samantha_bj_cum_face"

        attribute cumchest:
            if_not ["suck"]
            "samantha_bj_cum_chest"

        attribute lotion:
            if_not ["suck"]
            "samantha_bj_lotion"


        if samantha.get_piercings("nipples"):
            "samantha_bj_piercings_nipples"

        always:
            "samantha_bj_shadow"



    layeredimage samantha doggy:

        attribute arm null
        attribute xray null
        attribute condom null
        attribute cumshot null
        attribute cumface null

        group penetration:
            attribute vaginal default null
            attribute anal null
            attribute out null
            attribute none null

        always "samantha_doggy_bg"

        always "samantha_doggy_body"

        always:
            if_any ["anal"]
            if_not ["none","vaginal", "out"]
            "samantha_doggy_anal_man"

        always:
            if_any ["vaginal", "out"]
            if_not ["none","anal"]
            "samantha_doggy_vaginal_man"

        attribute milk:
            "samantha_doggy_milk"

        attribute red:
            "samantha_doggy_red"

        attribute write:
            "samantha_doggy_write"

        always:
            if_any ["anal"]
            if_not ["none","vaginal", "out"]
            "samantha_doggy_anal_dick"

        always:
            if_any ["vaginal"]
            if_not ["none","anal", "out"]
            "samantha_doggy_vaginal_dick"

        always:
            if_any ["out"]
            if_not ["none","anal", "vaginal"]
            "samantha_doggy_dick_out"

        always:
            if_all ["anal","condom"]
            if_not ["none","vaginal", "out"]
            "samantha_doggy_anal_condom"

        always:
            if_all ["vaginal", "condom"]
            if_not ["none","anal", "out"]
            "samantha_doggy_vaginal_condom"

        always:
            if_all ["out", "condom"]
            if_not ["none","anal", "vaginal", "cumshot"]
            "samantha_doggy_dick_out_condom"

        always:
            if_all ["out", "condom", "cumshot"]
            if_not ["none","anal", "vaginal"]
            "samantha_doggy_dick_out_condom_cum"

        always:
            if_any ["vaginal", "out"]
            if_all ["arm"]
            if_not ["none","anal"]
            "samantha_doggy_vaginal_hand"

        always:
            if_all ["anal", "arm"]
            if_not ["none","vaginal", "out"]
            "samantha_doggy_anal_hand"

        always:
            if_any ["vaginal"]
            if_all ["xray"]
            if_not ["none","anal", "out", "condom"]
            "samantha_doggy_vaginal_xray"

        always:
            if_all ["anal", "xray"]
            if_not ["none","vaginal", "out", "condom"]
            "samantha_doggy_anal_xray"

        always:
            if_all ["vaginal", "cumshot", "xray"]
            if_not ["none","anal", "out", "condom"]
            "samantha_doggy_vaginal_xray_cum"

        always:
            if_all ["anal", "cumshot", "xray"]
            if_not ["none","vaginal", "out", "condom"]
            "samantha_doggy_anal_xray_cum"

        always:
            if_all ["cumshot", "out"]
            if_not ["anal", "none","vaginal", "condom"]
            "samantha_doggy_dick_out_cumshot"

        always:
            if_not ["none"]
            "samantha_doggy_dick_hair"

        attribute asscum:
            "samantha_doggy_ass_cum"

        attribute bodycum:
            "samantha_doggy_body_cum"

        attribute beads:
            if_not ["anal"]
            "samantha_doggy_beads"

        attribute dildo:
            if_not ["vaginal"]
            "samantha_doggy_dildo"

        attribute squirt:
            if_not ["vaginal"]
            if_any ["dildo"]
            "samantha_doggy_dildo_squirt"

        group eyes:
            attribute wink default:
                "samantha_doggy_eyes_wink"
            attribute closed:
                "samantha_doggy_eyes_wink"
            attribute blind:
                "samantha_doggy_blindfold"

        group mouth:
            attribute scream default:
                "samantha_doggy_mouth_scream"
            attribute gag:
                "samantha_doggy_gag"
            attribute smile:
                "samantha_doggy_mouth_smile"
            attribute pant:
                "samantha_doggy_mouth_open"

        attribute drool:
            if_not ["scream", "smile", "pant"]
            if_any ["gag"]
            "samantha_doggy_gag_drool"

        attribute facial:
            "samantha_doggy_cum_face"

        attribute spank:
            if_any ["spank"]
            "samantha_doggy_spanking"

        if samantha.get_piercings("tongue"):
            if_any ["smile"]
            if_not ["scream", "gag", "pant"] 
            "samantha_doggy_piercings_lipsA"

        if samantha.get_piercings("tongue"):
            if_not ["smile"]
            if_any ["scream", "gag", "pant"] 
            "samantha_doggy_piercings_lipsB"

        if samantha.get_piercings("nose"):
            "samantha_doggy_piercings_nose"

        if samantha.get_piercings("nipples"):
            "samantha_doggy_piercings_nipples"

        if samantha.get_piercings("clit"):
            "samantha_doggy_piercings_clit"

        if samantha.get_flag_value("pubes",samantha.pubes):
            "samantha_doggy_pubes" 

    layeredimage samantha mmf:

        always "samantha_mmf_bg"

        always "samantha_mmf_body"

        if samantha.get_flag_value("pregnant") >= 9:
            "samantha_mmf_pregnant"

        group mouth auto:
            attribute bad default

        group eyes auto:
            attribute closed default

        if samantha.get_piercings("nipples"):
            "samantha_mmf_piercings_nipples"

        if samantha.get_piercings("navel") and samantha.get_flag_value("pregnant") >= 9:
            "samantha_mmf_piercings_navel"

        if samantha.get_piercings("navel") and not samantha.get_flag_value("pregnant") >= 9:
            "samantha_mmf_piercings_navel_pregnant"


        attribute ryan:
            "samantha_mmf_ryan"

        group ryandick:
            if_any "ryan"
            attribute suck default

        group cum auto multiple


    layeredimage samantha miss:

        always "samantha_miss_base"

        if samantha.get_flag_value("pregnant") >= 9:
            "samantha_miss_preg"

        group mouth auto:
            attribute normal default

        group eyes auto:
            attribute normaleyes default

        if samantha.get_piercings("nipples"):
            "samantha_miss_piercings_nipples"

        if samantha.get_piercings("navel"):
            "samantha_miss_piercings_navel"

        if samantha.get_piercings("tongue"):
            if_any "ahegao"
            "samantha_miss_piercings_tongue"

        if samantha.get_piercings("hip"):
            "samantha_miss_piercings_hip"

        if samantha.get_piercings("clit"):
            "samantha_miss_piercings_clit"

        group dick auto:
            attribute dickout default

        group cum auto multiple

    layeredimage samantha bj2:

        always "samantha_bj2_base"

        group mouth auto:
            attribute lick default

        group eyes auto:
            attribute open default

        group fx auto multiple

    layeredimage samantha ending:
        group id auto:
            attribute a default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
