init 1:
    layeredimage bree:
        attribute_function Picker(bree)

        attribute pregnant null

        group position auto variant "pregnant" if_any "pregnant"
        group position auto if_not "pregnant"

        group exp auto variant "a" if_any "a":
            attribute normal default
        group exp auto variant "b" if_any "b":
            attribute normal default

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"           

        group necklace auto  variant "a" if_any "a" if_not "collar"
        group necklace auto  variant "b" if_any "b" if_not "collar"
        attribute collar:
            if_any "a"
            "bree_collar_a"
        attribute collar:
            if_any "b"
            "bree_collar_b"
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
            "bree_pubes_a"  
        attribute pubes:
            if_all ["naked","b"]
            "bree_pubes_b"  
        group acc multiple auto  variant "a" if_any "a"
        group acc multiple auto  variant "b" if_any "b"

    layeredimage bree bowsette:
        group outfit auto:
            attribute dress default

        group exp auto:
            attribute normal default

    layeredimage bree smartphone:
        always "bree_smartphone"

    layeredimage bree pool oral:
        group bg auto:
            attribute pool default

        group male auto:
            attribute a default

        group body auto:
            attribute closed default

        if bree.get_flag_value("pregnant") >= 9:
            "bree_pool_oral_pregnant" 

        if bree.get_flag_value("pubes",bree.pubes):
            "bree_pool_oral_pubes"  

        attribute pain:
            "bree_pool_oral_pain"

        attribute fx:
            "bree_pool_oral_fx"

        group outfit auto variant "open" if_any "open":
            attribute swimsuit default
            attribute naked null

        group outfit auto if_not "closed":
            attribute swimsuit default
            attribute naked null

        attribute sasha:
            if_any "open"
            "bree_pool_oral_sasha"

        group panel auto

    layeredimage couch fun:
        attribute facial null

        always:
            "3bj_background"
        always:
            "3bj_dick_masturbate"

        attribute masturbate:
            "3bj_masturbate"

        attribute sasha:
            "3bj_sasha_body"

        always:
            if_all ["sasha","facial"]
            "3bj_sasha_facial"

        if sasha.get_piercings("tongue"):
            "3bj_sasha_piercings_tongue"

        always:
            if_not "masturbate"
            "3bj_dick_bj"

        attribute bree:
            "3bj_bree_body"

        if bree.get_piercings("navel"):
            "3bj_bree_piercings_navel"
        if bree.get_piercings("tongue"):
            "3bj_bree_piercings_tongue"

        always:
            if_all ["bree","facial"]
            "3bj_bree_facial"

        attribute cumshot:
            "3bj_cumshot"

    layeredimage bree miss:
        attribute cum null
        group bg:
            attribute breebedroom:
                "bree_miss_bg_bedroom2"
            attribute heroroom default:
                "bree_miss_bg_bedroom"

        group body:
            attribute normal default:
                "bree_miss_body_normal"
            attribute bowsette:
                "bree_miss_body_bowsette"

        if bree.get_flag_value("pregnant") >= 9:
            "bree_miss_pregnant"

        group bowsetteexp auto:
            if_any "bowsette"
            attribute base default

        group exp auto:
            if_not "bowsette"
            attribute base default

        group outfit:
            attribute naked null default
            attribute dressed if_any ["bowsette"]:
                "bree_miss_oufit"
            attribute dressed:
                "bree_miss_leg"

        attribute arm:
            "bree_miss_arm"

        attribute fuck:
            "bree_miss_pussyopen"

        attribute fuck:
            "bree_miss_dickin"

        attribute condom:
            if_any "fuck"
            "bree_miss_dickin_condom"

        if persistent.xray:
            if_all ['fuck']
            "bree_miss_xray"

        if persistent.xray:
            if_all ['fuck', "cum"]
            "bree_miss_xray_cum"
        if not persistent.xray:
            if_not ["fuck"]
            if_all ["cum"]
            "bree_miss_bellycum"
        if not persistent.xray:
            if_all ["cum"]
            if_not ["fuck"]
            "bree_miss_boobycum"
        if not persistent.xray:
            if_all ['fuck', "cum"]
            "bree_miss_cuminside"

        attribute dickout:
            if_not "fuck"
            "bree_miss_dickout"

        attribute condom:
            if_not "fuck"
            if_any "dickout"
            "bree_miss_dickout_condom"

        always:
            "bree_miss_man"

        if bree.get_piercings("nipples"):
            "bree_miss_piercings_nipple_left"
        if bree.get_piercings("nipples"):
            "bree_miss_piercings_nipple_right"
        if bree.get_piercings("clit"):
            "bree_miss_piercings_clit"
        if bree.get_piercings("navel") and not bree.get_flag_value("pregnant") >= 9:
            "bree_miss_piercings_navel"
        if bree.get_piercings("navel") and bree.get_flag_value("pregnant") >= 9:
            "bree_miss_piercings_navel_pregnant"
        if bree.get_piercings("nose"):
            "bree_miss_piercings_nose"    
        if bree.get_piercings("tongue"):
            if_any ["cum","ahegao"]
            "bree_miss_piercings_tongue"    
        if bree.get_flag_value("pubes",bree.pubes) and not persistent.xray:
            "bree_miss_pubes"  

        group cum auto multiple

    layeredimage bree kiss:
        always:
            "bree_kiss"




        group outfit auto:
            attribute casual default
            attribute naked null

        group outfitmike auto:
            attribute normal default
            attribute naked null






    layeredimage bree doggy:
        attribute suck null
        attribute fuck null
        attribute anal null
        attribute deep null
        attribute noone null

        attribute pull null

        group bg auto:
            attribute bedroom1 default

        always:
            "bree_doggy_body"

        group suck auto:
            if_not ["fuck","anal"]
            attribute nosuck null

        group fuck auto:
            if_not ["suck","deep", "sasha", "noone"]

        group face auto:
            attribute fuck default

        if bree.get_piercings("nipples"):
            "bree_doggy_piercings_nipples"
        if bree.get_piercings("clit"):
            "bree_doggy_piercings_clit"
        if bree.get_piercings("nose"):
            "bree_doggy_piercings_nose"    

        if bree.get_flag_value("pregnant") >= 9:
            "bree_doggy_pregnant"

        group pull auto:
            if_any "pull"

        group dick auto:
            if_all ["fuck"]
            attribute dickout default

        group cum auto multiple

        group eyes auto:
            attribute normal default

        group mouth auto:
            if_not ["suck", "deep"]
            attribute normal default

        attribute sasha:
            "bree_doggy_sasha"

        group toy auto multiple
        group fx auto multiple

    layeredimage 3bj2:

        always:
            "3bj2_bg"

        attribute bree:
            "3bj2_bree"

        attribute sasha:
            "3bj2_sasha"

        if bree.get_piercings("nose"):
            if_all "bree"
            "3bj2_bree_piercings_nose"    
        if bree.get_piercings("ears"):
            if_all "bree"
            "3bj2_bree_piercings_ears"    
        if bree.get_piercings("lips"):
            if_all "bree"
            "3bj2_bree_piercings_lips"    

        if sasha.get_piercings("nose"):
            if_all "sasha"
            "3bj2_sasha_piercings_nose"    
        if sasha.get_piercings("ears"):
            if_all "sasha"
            "3bj2_sasha_piercings_ears"    
        if sasha.get_piercings("lips"):
            if_all "sasha"
            "3bj2_sasha_piercings_lips"    
        if sasha.get_piercings("tongue"):
            if_all "sasha"
            "3bj2_sasha_piercings_tongue"    

        group dick auto:
            attribute normal default

        group breeexp auto:
            attribute breeopen default

        group sashaexp auto:
            attribute sashaopen default

        group hand auto:
            attribute none null default

        attribute breecumtongue:
            "3bj2_bree_cum_tongue"

        attribute breecummouth:
            "3bj2_bree_cum_mouth"

        attribute breefacial:
            "3bj2_bree_facial"

        attribute breesaliva:
            "3bj2_bree_saliva"

        attribute sashacumtongue:
            "3bj2_sasha_cum_tongue"

        attribute sashacummouth:
            "3bj2_sasha_cum_tongue"

        attribute sashafacial:
            "3bj2_sasha_facial"

        attribute sashasaliva:
            "3bj2_sasha_saliva"

        attribute cumshare:
            "3bj2_cumshare"

        attribute cumshot:
            "3bj2_cumshot"

        attribute wet:
            "3bj2_dick_wet"

    layeredimage bree boobjob:
        attribute lick null

        always:
            if_not "lick"
            "bree_boobjob_bg_base"
        always:
            if_any "lick"
            "bree_boobjob_bg_lick"

        group mouth auto:
            if_not "lick"
            attribute closed default
        group eyes auto:
            if_not "lick"
            attribute eyesopen default

        if bree.get_piercings("tongue"):
            if_any "open"
            if_not "lick"
            "bree_boobjob_piercings_tongue"
        if bree.get_piercings("tongue"):
            if_any "lick"
            "bree_boobjob_piercings_tongue_lick"
        if bree.get_piercings("nose"):
            "bree_boobjob_piercings_nose"    
        if bree.get_piercings("nipples"):
            "bree_boobjob_piercings_nipples"  

        group cum auto multiple


    layeredimage bree spoon:

        group bg auto:
            attribute bedroom1 default

        always:
            "bree_spoon_body"

        group guy auto:
            attribute mike default

        group fuck auto variant "scottie" if_any "scottie":
            attribute out default
        group fuck auto variant "mike" if_any "mike":
            attribute out default

        always:
            if_any "mike"
            if_not "vaginal"
            "bree_spoon_mike_legs"

        always:
            if_any "scottie"
            if_not "vaginal"
            "bree_spoon_scottie_legs"

        group exp auto:
            attribute normal default

        if bree.get_piercings("clit"):
            "bree_spoon_piercings_clit"
        if bree.get_piercings("nose"):
            "bree_spoon_piercings_nose"    

        if bree.get_flag_value("pregnant") >= 9:
            "bree_spoon_pregnant"

        group cum auto


    layeredimage bree shower:
        always:
            "shower_bg"
        always:
            "shower_bree"
        if bree.get_flag_value("pregnant") >= 9:
            "shower_bree_preg"
        always:
            "shower_water"
        always:
            "shower_steam_a"
        always:
            "shower_steam_b"
        always:
            "shower_door"

    layeredimage bitches:

        always:
            "bitches_bg"
        always:
            "bitches_mike"

        group position auto:
            attribute walk default

        if sasha.get_flag_value("pregnant") >= 9:
            if_any "blowjob"
            "bitches_blowjob_sasha_pregnant"
        if sasha.get_flag_value("pregnant") >= 9:
            if_any "walk"
            "bitches_walk_sasha_pregnant"
        if sasha.get_flag_value("boobjob"):
            if_any "walk"
            "bitches_walk_sasha_bigboobs"
        if sasha.get_flag_value("boobjob"):
            if_any "blowjob"
            "bitches_blowjob_sasha_bigboobs"
        if sasha.get_flag_value("haircut"):
            if_any "walk"
            "bitches_walk_sasha_blonde"
        if sasha.get_flag_value("haircut"):
            if_any "blowjob"
            "bitches_blowjob_sasha_blonde"

        group suck auto if_any "blowjob"

        group cum auto multiple

        group pee auto multiple if_any "blowjob"

        attribute dick:
            if_not ["breesuck","sashasuck"]
            "bitches_blowjob_dick"

        if bree.get_flag_value("pregnant") >= 9:
            if_any "blowjob"
            "bitches_blowjob_bree_pregnant"
        if bree.get_flag_value("pregnant") >= 9:
            if_any "walk"
            "bitches_walk_bree_pregnant"

        if bree.get_piercings("clit"):
            if_any "blowjob"
            "bitches_blowjob_bree_piercings_clit"
        if bree.get_piercings("navel") and not bree.get_flag_value("pregnant") >= 9:
            if_any "blowjob"
            "bitches_blowjob_bree_piercings_navel"
        if bree.get_piercings("navel") and bree.get_flag_value("pregnant") >= 9:
            if_any "blowjob"
            "bitches_blowjob_bree_piercings_navel_pregnant"
        if bree.get_piercings("nipples"):
            if_any "blowjob"
            "bitches_blowjob_bree_piercings_nipples"

        if bree.get_piercings("nose"):
            if_any "walk"
            "bitches_walk_bree_piercings_nose"
        if bree.get_piercings("tongue"):
            if_any "walk"
            "bitches_walk_bree_piercings_tongue"
        if bree.get_piercings("nipples"):
            if_any "walk"
            "bitches_walk_bree_piercings_nipples"

        if sasha.get_piercings("clit"):
            if_any "blowjob"
            "bitches_blowjob_sasha_piercings_clit"
        if sasha.get_piercings("nose"):
            if_any "blowjob"
            "bitches_blowjob_sasha_piercings_nose"
        if sasha.get_piercings("navel") and not sasha.get_flag_value("pregnant") >= 9:
            if_any "blowjob"
            "bitches_blowjob_sasha_piercings_navel"
        if sasha.get_piercings("navel") and sasha.get_flag_value("pregnant") >= 9:
            if_any "blowjob"
            "bitches_blowjob_sasha_piercings_navel_pregnant"
        if sasha.get_piercings("nipples") and not sasha.get_flag_value("boobjob"):
            if_any "blowjob"
            "bitches_blowjob_sasha_piercings_nipples"
        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            if_any "blowjob"
            "bitches_blowjob_sasha_piercings_nipples_bigboobs"

        if sasha.get_piercings("nose"):
            if_any "walk"
            "bitches_walk_sasha_piercings_nose"
        if sasha.get_piercings("tongue"):
            if_any "walk"
            "bitches_walk_sasha_piercings_tongue"
        if sasha.get_piercings("nipples"):
            if_any "walk"
            "bitches_walk_sasha_piercings_nipples"

    layeredimage bree showersex:

        always:
            "bree_showersex_background"

        always:
            "bree_showersex_water"

        always:
            "bree_showersex_body"

        if bree.get_flag_value("pregnant") >= 9:
            "bree_showersex_pregnant"

        if bree.get_piercings("nose"):
            "bree_showersex_piercings_nose"
        if bree.get_piercings("tongue"):
            "bree_showersex_piercings_tongue"

        if bree.get_flag_value("collared"):
            "bree_showersex_collar"

        group fx auto multiple

    layeredimage bree mast:

        group si:
            attribute finger null default
            attribute small null
            attribute medium null
            attribute big null

        attribute left null
        attribute ass null

        always:
            "bree_mast_bg"

        always:
            "bree_mast_body"

        if bree.get_flag_value("pubes",bree.pubes):
            "bree_mast_pubes"  

        if bree.get_flag_value("pregnant") >= 9:
            "bree_mast_preg"

        if bree.get_piercings("clit"):
            "bree_mast_piercings_clit"
        if bree.get_piercings("nose"):
            "bree_mast_piercings_nose"    
        if bree.get_piercings("nipples"):
            "bree_mast_piercings_nipples"    
        if bree.get_piercings("tongue"):
            "bree_mast_piercings_tongue"    
        if bree.get_piercings("navel") and not bree.get_flag_value("pregnant") >= 9:
            "bree_mast_piercings_navel"    
        if bree.get_piercings("navel") and bree.get_flag_value("pregnant") >= 9:
            "bree_mast_piercings_navel_preg"    

        always:
            if_not "left"
            "bree_mast_left_arm"

        group exp auto:
            attribute cum default

        group exp2 auto if_not "mouth":
            attribute cum default

        always:
            if_any "mouth"
            "bree_mast_exp2_cum"

        group dildo auto variant "small" if_not ["finger","ass"]:
            attribute pussy default
        group dildo auto variant "finger" if_any "finger" if_not ["ass"]:
            attribute pussy default
        group dildo auto variant "medium" if_any "medium" if_not ["ass"]
        group dildo auto variant "big" if_any "big" if_not ["ass"]

        always:
            if_any "ass"
            if_not ["finger","small"]
            "bree_mast_ass_small"

        always:
            if_any "ass"
            "bree_mast_dildo_finger_pussy"

        group ass auto if_any "ass":
            attribute finger default

        group wet auto

layeredimage bree ending:
    attribute bree null
    attribute sasha null

    always:
        if_any "bree"
        if_not "sasha"
        "bree_ending_breesolo"
    if bree.get_flag_value("collared"):
        if_any "bree"
        if_not "sasha"
        "bree_ending_breesolo_collar"

    if sasha.get_flag_value("haircut"):
        if_any "sasha"
        if_not "bree"
        "bree_ending_sashasolo_blonde"
    else:
        if_any "sasha"
        if_not "bree"
        "bree_ending_sashasolo"
    if sasha.get_flag_value("boobjob"):
        if_any "sasha"
        if_not "bree"
        "bree_ending_sashasolo_bb"
    if sasha.get_flag_value("collared"):
        if_any "sasha"
        if_not "bree"
        "bree_ending_sashasolo_collar"
    always:
        if_not "bree"
        if_any "sasha"
        "bree_ending_sashasolo_mike"

    always:
        if_all ["sasha","bree"]
        "bree_ending_sashabree_bree"
    if bree.get_flag_value("collared"):
        if_all ["sasha","bree"]
        "bree_ending_sashabree_breecollar"

    if sasha.get_flag_value("haircut"):
        if_all ["sasha","bree"]
        "bree_ending_sashabree_sasha_blonde"
    else:
        if_all ["sasha","bree"]
        "bree_ending_sashabree_sasha"
    if sasha.get_flag_value("boobjob"):
        if_all ["sasha","bree"]
        "bree_ending_sashabree_bb"
    if sasha.get_flag_value("collared"):
        if_all ["sasha","bree"]
        "bree_ending_sashabree_sashacollar"
    always:
        if_all ["sasha","bree"]
        "bree_ending_sashabree_mike"

    if sasha.get_flag_value("pregnant"):
        if_any "sasha"
        "bree_ending_sashakid"
    if bree.get_flag_value("pregnant"):
        if_any "bree"
        "bree_ending_breekid"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
