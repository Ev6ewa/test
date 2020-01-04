init python:
    class SashaSexPicker(object):
        def __init__(self, girl):
            self.girl =  girl
        
        def __call__(self, attr):
            if self.girl.get_flag_value("collared") and self.girl.sub() >= 50:
                attr.add("collar")
            if self.girl.get_flag_value("boobjob"):
                attr.add("boobjob")
            if self.girl.get_flag_value("haircut"):
                attr.add("haircut")
            if self.girl.get_flag_value("pubes",self.girl.pubes):
                attr.add("pubes")
            for o in attr:
                if self.girl.get_flag_value("sexy"+o):
                    attr.remove(o)
                    attr.add("sexy"+o)
            if self.girl.get_flag_value("pregnant") >= 9:
                attr.add("pregnant")
            for v in SEXATTRIBUTES:
                attr.add(v)
            
            return attr


init 1:
    layeredimage sasha:
        attribute_function Picker(sasha)

        attribute pregnant null
        attribute boobjob null
        attribute haircut null

        group position auto if_not ["pregnant","boobjob"]
        group position auto variant "pregnant" if_any "pregnant" if_not "boobjob"

        group position auto variant "bb" if_not "pregnant" if_any "boobjob"
        group position auto variant "pregnant_bb" if_all ["pregnant", "boobjob"]

        group exp auto variant "a" if_any "a":
            attribute normal default
        group exp auto variant "b" if_any "b":
            attribute normal default
        always:
            if_all ["a","haircut"]
            if_not "boobjob"
            "sasha_blonde_a"
        always:
            if_all ["b","haircut"]
            if_not "boobjob"
            "sasha_blonde_b"
        always:
            if_all ["a","haircut","boobjob"]
            "sasha_blonde_a_bb"
        always:
            if_all ["b","haircut","boobjob"]
            "sasha_blonde_b_bb"

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"

        group acc multiple auto
        group acc2 multiple auto variant "pregnant_b" if_all ["pregnant","b"]
        group acc2 multiple auto variant "pregnant_a" if_all ["pregnant","a"]
        group acc2 multiple auto variant "a" if_any "a" if_not "pregnant"
        group acc2 multiple auto variant "b" if_any "b" if_not "pregnant"
        group outfit auto variant "a" if_any "a" if_not ["pregnant","boobjob"]:
            attribute naked null
        group outfit auto variant "b" if_any "b" if_not ["pregnant","boobjob"]:
            attribute naked null
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"] if_not "boobjob":
            attribute naked null
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"] if_not "boobjob":
            attribute naked null
        group outfit auto variant "a_bb" if_all ["a","boobjob"] if_not ["pregnant"]:
            attribute naked null
        group outfit auto variant "b_bb" if_all ["b","boobjob"] if_not ["pregnant"]:
            attribute naked null
        group outfit auto variant "a_pregnant_bb" if_all ["a", "pregnant", "boobjob"]:
            attribute naked null
        group outfit auto variant "b_pregnant_bb" if_all ["b", "pregnant", "boobjob"]:
            attribute naked null

        attribute pubes:
            if_all ["naked","a"]
            "sasha_pubes_a"  
        attribute pubes:
            if_all ["naked","b"]
            "sasha_pubes_b"  
        attribute collar:
            "sasha_collar"  
        attribute leash:
            if_all ["collar"]
            "sasha_leash"  

    layeredimage sasha smartphone:
        always "sasha_smartphone"

    layeredimage sasha strap:
        attribute_function MyPicker(sasha)

        attribute pubes null

        always "sasha_strap_background"

        group cum auto

        always "sasha_strap_dick"

        always "sasha_strap_body"

        attribute pregnant:
            "sasha_strap_pregnant"

        attribute boobjob:
            "sasha_strap_bb"

        attribute haircut:
            "sasha_strap_blonde"

        attribute collar:
            "sasha_strap_collar"

        if sasha.get_piercings("nipples"):
            if_any "boobjob"
            "sasha_strap_nipples_bb"
        if sasha.get_piercings("nipples"):
            if_not "boobjob"
            "sasha_strap_nipples"
        if sasha.get_piercings("tongue"):
            "sasha_strap_tongue"
        if sasha.get_piercings("nose"):
            "sasha_strap_nose"
        if sasha.get_piercings("navel") and not sasha.get_flag_value("pregnant") >= 9:
            "sasha_strap_navel"
        if sasha.get_piercings("navel") and sasha.get_flag_value("pregnant") >= 9:
            "sasha_strap_navel_pregnant"

        group exp auto:
            attribute normal default

        attribute bree:
            "sasha_strapon_bree"

        group bree auto:
            if_any "bree"
            attribute breesmile default

        attribute light:
            "sasha_strapon_light"

    layeredimage sasha kiss:
        attribute_function MyPicker(sasha)

        attribute pubes null

        always:
            "sasha_kiss"

        attribute boobjob:
            "sasha_kiss_bb"

        attribute haircut:
            "sasha_kiss_hair_blonde"

        attribute pregnant:
            "sasha_kiss_preg"




        group outfit auto if_not ["boobjob","pregnant"]:
            attribute casual default
            attribute naked null

        group outfit auto variant "bb" if_any "boobjob" if_not "pregnant":
            attribute casual default
            attribute naked null

        group outfit auto variant "preg" if_any "pregnant" if_not "boobjob":
            attribute casual default
            attribute naked null

        group outfit auto variant "bb_preg" if_all ["boobjob","pregnant"]:
            attribute casual default
            attribute naked null


        group outfitmike auto variant "bb" if_any "boobjob":
            attribute red default
            attribute naked null

        group outfitmike auto if_not "boobjob":
            attribute red default
            attribute naked null






    layeredimage sasha bj:
        attribute_function MyPicker(sasha)

        always:
            "sasha_bj_bg"

        always:
            "sasha_bj_sasha"


        group sasha auto multiple

        group exp auto:
            attribute open default

        if sasha.get_piercings("nipples"):
            if_any "boobjob"
            "sasha_bj_piercings_nipples_bb"
        if sasha.get_piercings("nipples"):
            if_not "boobjob"
            "sasha_bj_piercings_nipples"
        if sasha.get_piercings("nose"):
            "sasha_bj_piercings_nose"
        if sasha.get_piercings("tongue"):
            if_not "dickin"
            "sasha_bj_piercings_tongue"
        if sasha.get_piercings("lip"):
            if_not "dickin"
            "sasha_bj_piercings_lip"

        group outfit auto if_not ["boobjob","pregnant"]:
            attribute naked null default

        group outfit auto variant "bb" if_any "boobjob" if_not "pregnant":
            attribute naked null default

        group outfit auto variant "preg" if_any "pregnant" if_not "boobjob":
            attribute naked null default

        group outfit auto variant "bb_preg" if_all ["boobjob","pregnant"]:
            attribute naked null default

        if sasha.get_piercings("ears"):
            "sasha_bj_piercings_ears"

        group beads auto:
            attribute nobeads null default

        attribute mike

        group dick auto if_any "mike":
            attribute dickout default
            attribute nodick null
            attribute dickin if_not 'cumafter'

        attribute condom null
        group condom auto if_all ["mike", "condom"]

        attribute cum null
        group cum auto if_any "cum" if_not ["cumafter", "condom"]

        always:
            if_all ["cum", "condom", "dickout"]
            "sasha_bj_cum_dickout_condom"

        attribute cumafter null
        group cumafter auto if_any "cumafter" if_not "condom"

        always:
            if_all ["cumafter", "condom", "dickout"]
            "sasha_bj_cum_dickout_condom"

        attribute handmove null
        group handmove auto if_any "handmove"

    layeredimage sasha stand:
        attribute_function SashaSexPicker(sasha)

        always:
            "sasha_stand_bg"

        always:
            "sasha_stand_sasha"


        group sasha auto multiple

        group exp auto:
            attribute open default
        attribute blush

        if sasha.get_piercings("nipples"):
            if_any "boobjob"
            "sasha_stand_piercings_nipples_bb"
        if sasha.get_piercings("nipples"):
            if_not "boobjob"
            "sasha_stand_piercings_nipples"
        if sasha.get_piercings("navel"):
            if_any "pregnant"
            "sasha_stand_piercings_navelpregnant"
        if sasha.get_piercings("navel"):
            if_not "pregnant"
            "sasha_stand_piercings_navel"
        if sasha.get_piercings("clit"):
            "sasha_stand_piercings_clit"
        if sasha.get_piercings("ears"):
            "sasha_stand_piercings_ears"
        if sasha.get_piercings("nose"):
            "sasha_stand_piercings_nose"
        if sasha.get_piercings("tongue"):
            "sasha_stand_piercings_tongue"
        if sasha.get_piercings("lip"):
            "sasha_stand_piercings_lip"

        group outfit auto if_not ["boobjob","pregnant"]:
            attribute naked null default

        group outfit auto variant "bb" if_any "boobjob" if_not "pregnant":
            attribute naked null default

        group outfit auto variant "preg" if_any "pregnant" if_not "boobjob":
            attribute naked null default

        group outfit auto variant "bb_preg" if_all ["boobjob","pregnant"]:
            attribute naked null default

        group dick auto:
            attribute dickout default
            attribute nodick null

        attribute condom null
        group condom auto if_all ["condom"]

        attribute cum null
        group cum auto if_any "cum" if_not "cumafter":
            attribute dickout "sasha_stand_cum_dickout_condom" if_any "condom"
            attribute dickout if_not "condom"
            attribute dickin null if_any "condom"
            attribute dickin if_not "condom"

        attribute cumafter "sasha_stand_cumafter_dickout" if_any 'dickout'

        always:
            "sasha_stand_fx"

    layeredimage sasha missionary:
        attribute_function SashaSexPicker(sasha)
        always:
            "sasha_missionary_bg"

        always:
            "sasha_missionary_body"

        group body auto multiple:
            attribute leash if_all ["collar", "leash"]

        always:
            if_any "boobjob"
            "sasha_missionary_tits_boobjob"
        always:
            if_not "boobjob"
            "sasha_missionary_tits_small"

        group exp auto:
            attribute sashanormal default

        attribute pubes

        group dick auto if_any "man":
            attribute nodick null default

        group outfit auto:
            attribute naked null default

        always:
            if_all ["rope", "fuck"]
            "sasha_missionary_rope_fuck"

        always:
            if_all ["rope"]
            if_not ["fuck"]
            "sasha_missionary_rope_normal"

        if sasha.get_piercings("nipples"):
            if_any "boobjob"
            "sasha_missionary_piercings_nipples_bb"
        if sasha.get_piercings("nipples"):
            if_not "boobjob"
            "sasha_missionary_piercings_nipples"
        if sasha.get_piercings("navel"):
            if_any "pregnant"
            "sasha_missionary_piercings_navelpregnant"
        if sasha.get_piercings("navel"):
            if_not "pregnant"
            "sasha_missionary_piercings_navel"
        if sasha.get_piercings("clit"):
            "sasha_missionary_piercings_clit"
        if sasha.get_piercings("ears"):
            "sasha_missionary_piercings_ears"
        if sasha.get_piercings("nose"):
            "sasha_missionary_piercings_nose"
        if sasha.get_piercings("lip"):
            "sasha_missionary_piercings_lip"

        attribute bree:
            "sasha_missionary_bree"

        if bree.get_flag_value('pregnant') > 7:
            if_any "bree"
            "sasha_missionary_breepregnant"

        if bree.get_flag_value("collared") and bree.sub > 50:
            if_all ["bree", "leash"]
            "sasha_missionary_breeleash"

        group breeexp if_any "bree":
            attribute breenormal default

        attribute blush:
            if_any "bree"
            "sasha_missionary_blush"


        group fx auto

        group cum:
            attribute cumshot:
                if_any "fuck"
                "sasha_missionary_pussycum"
            attribute cumshot:
                if_any "out"
                "sasha_missionary_cumout"
            attribute nocumshot null

        group man:
            attribute man default:
                "sasha_missionary_man"
            attribute noman null

        attribute speed:
            "sasha_missionary_speed"

    layeredimage sasha doggy:
        attribute_function SashaSexPicker(sasha)
        always:
            "sasha_doggy_bg"

        always:
            "sasha_doggy_sasha"

        group sasha auto multiple

        attribute boobjob

        attribute mouthbeads null
        group exp auto if_not 'mouthbeads':
            attribute waiting default

        group exp auto variant "beads" if_any 'mouthbeads':
            attribute waiting default

        group outfit auto:
            attribute naked null default


        attribute cumface null


















        group beads auto if_not "pussy":
            attribute nobeads null default

        group dick auto if_any "mike" if_not "cumafter":
            attribute nodick null default

        attribute cum null
        group cum auto if_any "cum" if_not ["condom", "cumafter"]

        attribute condom null
        group condom auto if_all ["mike", "condom"]

        group beads auto if_any "pussy":
            attribute nobeads null default

        attribute mike

        always:
            if_all ["cum", "condom", "dickout"]
            "sasha_doggy_cum_dickout_condom"

        attribute cumafter null
        group cumafter auto if_any "cumafter" if_not "condom":

            attribute pussy null

        always:
            if_all ["cumafter", "condom", "dickout"]
            "sasha_doggy_cum_dickout_condom"

        attribute hand null
        group hand auto:
            attribute nohand null default

    layeredimage band foursome:
        attribute cum null

        group bg auto:
            attribute bedroom3 default
        always:
            "band_foursome_base"
        if sasha.get_flag_value("pregnant") >= 9:
            "band_foursome_preg_sasha"
        if sasha.get_piercings("nipples"):
            "band_foursome_piercings_sasha_nipples"
        if sasha.get_piercings("tongue"):
            "band_foursome_piercings_sasha_tongue"
        if sasha.get_piercings("nose"):
            "band_foursome_piercings_sasha_nose"
        if sasha.get_piercings("clit"):
            "band_foursome_piercings_sasha_clit"
        group dick auto:
            attribute nodick null default
        if persistent.xray:
            if_all ["pussy","cum"]
            if_not ["ass", "mouth"]
            "band_foursome_xray_pussy"
        if persistent.xray:
            if_all ["ass","cum"]
            if_not ["pussy", "mouth"]
            "band_foursome_xray_ass"
        group cum auto:
            if_any "cum"
        attribute kleio:
            "band_foursome_kleio"
        if kleio.get_piercings("nose"):
            "band_foursome_piercings_kleio_nose"
        if kleio.get_flag_value("pregnant") >= 9:
            "band_foursome_preg_kleio"
        attribute anna:
            "band_foursome_anna"
        if anna.get_piercings("nose"):
            "band_foursome_piercings_anna_nose"
        attribute lick:
            if_any "anna"
            "band_foursome_anna_lick"

    layeredimage sasha tittyfuck:
        always:
            "sasha_tittyfuck_bg"
        always:
            "sasha_tittyfuck_base"
        group exp auto:
            attribute lick default
        if sasha.get_piercings("nipples"):
            "sasha_tittyfuck_piercings_nipples"
        group cum auto

    layeredimage band foursome2:
        always:
            "band_foursome2_bg"

        always:
            if_any "kleio"
            "band_foursome2_kleio_shadow"

        attribute kleio

        always:
            "band_foursome2_anna"

        attribute sasha

        group sashaexp auto:
            if_any "sasha"
            if_not "blowjob"
            attribute asslick default

        group annaexp auto:
            attribute scream default

        always:
            if_any "kleio"
            "band_foursome2_kleioexp_normal"

        if kleio.get_flag_value("pubes",kleio.pubes):
            if_any "kleio"
            "band_foursome2_kleio_pubes"

        if anna.get_flag_value("pregnant") >= 9:
            "band_foursome2_anna_preg"
        if kleio.get_flag_value("pregnant") >= 9:
            if_any "kleio"
            "band_foursome2_kleio_preg"
        if anna.get_piercings("nipples"):
            "band_foursome2_anna_piercings_nipples"
        if kleio.get_piercings("nipples"):
            if_any "kleio"
            "band_foursome2_anna_piercings_nipples"
        if anna.get_piercings("tongue"):
            "band_foursome2_anna_piercings_tongue"
        if kleio.get_piercings("tongue"):
            if_any "kleio"
            "band_foursome2_kleio_piercings_tongue"
        if anna.get_piercings("nose"):
            "band_foursome2_anna_piercings_nose"
        if kleio.get_piercings("nose"):
            if_any "kleio"
            "band_foursome2_kleio_piercings_nose"
        if anna.get_piercings("clit"):
            "band_foursome2_anna_piercings_clit"
        if kleio.get_piercings("clit"):
            if_any "kleio"
            "band_foursome2_kleio_piercings_clit"

        always:
            "band_foursome2_man"

        group fuck auto

        attribute cum:
            if_any "vaginal"
            "band_foursome2_cum_vaginal"
        attribute cum:
            if_any "anal"
            "band_foursome2_cum_anal"
        attribute cum:
            if_any "blowjob"
            "band_foursome2_cum_blowjob"
        attribute cum:
            if_any "out"
            "band_foursome2_cum_out"

    layeredimage sasha shower:
        always:
            "shower_bg"
        always:
            "shower_sasha"
        if sasha.get_flag_value("pregnant") >= 9:
            "shower_sasha_preg"
        if sasha.get_flag_value("boobjob"):
            "shower_sasha_bb"
        if sasha.get_flag_value("haircut"):
            "shower_sasha_blonde"
        always:
            "shower_water"
        always:
            "shower_steam_a"
        always:
            "shower_steam_b"
        always:
            "shower_door"

    layeredimage sasha showersex:
        always:
            "sasha_showersex_bg"
        always:
            "sasha_showersex_body"
        if sasha.get_flag_value("pregnant") >= 9:
            "sasha_showersex_pregnant"
        if sasha.get_flag_value("boobjob"):
            "sasha_showersex_bb"
        if sasha.get_flag_value("haircut"):
            "sasha_showersex_hair_blonde"
        else:
            "sasha_showersex_hair_black"
        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            "sasha_showersex_piercings_nipples_bb"
        if sasha.get_piercings("nipples") and not sasha.get_flag_value("boobjob"):
            "sasha_showersex_piercings_nipples"
        if sasha.get_piercings("tongue"):
            "sasha_showersex_piercings_tongue"
        if sasha.get_piercings("nose"):
            "sasha_showersex_piercings_nose"
        if sasha.get_piercings("navel") and not sasha.get_flag_value("pregnant") >= 9:
            "sasha_showersex_piercings_navel"
        if sasha.get_piercings("navel") and sasha.get_flag_value("pregnant") >= 9:
            "sasha_showersex_piercings_navel_pregnant"
        always:
            "sasha_showersex_arm"
        always:
            "sasha_showersex_man"
        always:
            "sasha_showersex_wet"

    layeredimage gog:
        always:
            "gog_bg"

        always:
            "gog_bree"
        if bree.get_flag_value("pregnant") >= 9:
            "gog_bree_pregnant"
        if bree.get_flag_value("collared") and bree.sub >= 50:
            "gog_bree_collar"
        if bree.get_piercings("nipples"):
            "gog_bree_piercings_nipples"
        if bree.get_piercings("tongue"):
            "gog_bree_piercings_tongue"
        if bree.get_piercings("ears"):
            "gog_bree_piercings_ears"
        if bree.get_piercings("nose"):
            "gog_bree_piercings_nose"
        if bree.get_piercings("navel") and not bree.get_flag_value("pregnant") >= 9:
            "gog_bree_piercings_navel"
        if bree.get_piercings("navel") and bree.get_flag_value("pregnant") >= 9:
            "gog_bree_piercings_navel_pregnant"

        always:
            "gog_sasha"
        if sasha.get_flag_value("pregnant") >= 9:
            "gog_sasha_pregnant"
        if sasha.get_flag_value("boobjob"):
            "gog_sasha_bb"
        if sasha.get_flag_value("haircut"):
            "gog_sasha_hair_blonde"
        else:
            "gog_sasha_hair_black"
        if sasha.get_piercings("ears"):
            "gog_sasha_piercings_ears"
        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            "gog_sasha_piercings_nipples_bb"
        if sasha.get_piercings("nipples") and not sasha.get_flag_value("boobjob"):
            "gog_sasha_piercings_nipples"
        if sasha.get_piercings("tongue"):
            "gog_sasha_piercings_tongue"

        always:
            "gog_wet"

    layeredimage shower 2bj:
        always:
            "shower_2bj_bg"
        always:
            "shower_2bj_mike_leg"

        attribute sasha:
            "shower_2bj_sasha"
        if sasha.get_flag_value("pregnant") >= 9:
            if_any "sasha"
            "shower_2bj_sasha_preg"
        if sasha.get_flag_value("boobjob"):
            if_any "sasha"
            "shower_2bj_sasha_bb"
        if not sasha.get_flag_value("haircut"):
            if_any "sasha"
            "shower_2bj_sasha_hair_black"
        always:
            if_any "sasha"
            "shower_2bj_sasha_hair_line"
        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            if_any "sasha"
            "shower_2bj_sasha_collar"
        if sasha.get_piercings("ears"):
            if_any "sasha"
            "shower_2bj_sasha_piercings_ears"
        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            if_any "sasha"
            "shower_2bj_sasha_piercings_nipples_bb"
        if sasha.get_piercings("nipples") and not sasha.get_flag_value("boobjob"):
            if_any "sasha"
            "shower_2bj_sasha_piercings_nipples"
        if sasha.get_piercings("tongue"):
            if_any "sasha"
            if_not "sashamouth"
            "shower_2bj_sasha_piercings_tongue"

        attribute bodycum:
            if_any "sasha"
            "shower_2bj_sasha_bodycum"
        attribute facial:
            if_any "sasha"
            "shower_2bj_sasha_facial"


        attribute bree:
            "shower_2bj_bree"
        if bree.get_flag_value("pregnant") >= 9:
            if_any "bree"
            "shower_2bj_bree_preg"
        if bree.get_piercings("nipples"):
            if_any "bree"
            "shower_2bj_bree_piercings_nipples"
        if bree.get_piercings("tongue"):
            if_any "bree"
            if_not "breemouth"
            "shower_2bj_bree_piercings_tongue"
        if bree.get_piercings("ears"):
            if_any "bree"
            "shower_2bj_bree_piercings_ears"
        if bree.get_piercings("nose"):
            if_any "bree"
            "shower_2bj_bree_piercings_nose"
        if bree.get_piercings("navel") and not bree.get_flag_value("pregnant") >= 9:
            if_any "bree"
            "shower_2bj_bree_piercings_navel"
        if bree.get_piercings("navel") and bree.get_flag_value("pregnant") >= 9:
            if_any "bree"
            "shower_2bj_bree_piercings_navel_pregnant"

        attribute bodycum:
            if_any "bree"
            "shower_2bj_bree_bodycum"

        attribute facial:
            if_any "bree"
            "shower_2bj_bree_facial"

        attribute cumshot:
            if_any "up"
            "shower_2bj_cumshot"

        always:
            "shower_2bj_mike"

        group dick auto:
            attribute up default


    layeredimage shower ffm:
        always:
            "shower_ffm_bg"
        always:
            "shower_ffm_arms"
        always:
            "shower_ffm_bodies"
        if bree.get_flag_value("pregnant") >= 9:
            "shower_ffm_bree_preg"
        if bree.get_flag_value("collared") and bree.sub >= 50:
            "shower_ffm_bree_collar"
        if bree.get_piercings("nipples"):
            "shower_ffm_bree_piercings_nipples"
        if bree.get_piercings("tongue"):
            "shower_ffm_bree_piercings_tongue"

        if sasha.get_flag_value("pregnant") >= 9:
            "shower_ffm_sasha_pregnant"
        if sasha.get_flag_value("boobjob"):
            "shower_ffm_sasha_bb"
        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            "shower_ffm_sasha_collar"
        if sasha.get_flag_value("haircut"):
            "shower_ffm_sasha_blonde"
        else:
            "shower_ffm_sasha_black"

        always:
            "shower_ffm_line"
        always:
            "shower_ffm_sasha_arm_shadow"
        always:
            "shower_ffm_sasha_arm"
        always:
            "shower_ffm_wet"


    layeredimage sasha foreplay:
        group bg auto:
            attribute bedroom default

        always:
            "sasha_foreplay_body"

        group dick auto:
            attribute down default

        group exp auto:
            attribute normal default

        if sasha.get_flag_value("pregnant") >= 9:
            "sasha_foreplay_preg"
        if sasha.get_flag_value("boobjob"):
            "sasha_foreplay_bb"
        if sasha.get_flag_value("haircut"):
            "sasha_foreplay_blonde"

        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            "sasha_foreplay_piercings_nipples_bb"
        if sasha.get_piercings("nipples") and not sasha.get_flag_value("boobjob"):
            "sasha_foreplay_piercings_nipples"
        if sasha.get_piercings("tongue"):
            if_any "orgasm"
            "sasha_foreplay_piercings_tongue_orgasm"
        if sasha.get_piercings("tongue"):
            if_any "pleasure"
            "sasha_foreplay_piercings_tongue_pleasure"
        if sasha.get_piercings("tongue"):
            if_any "normal"
            "sasha_foreplay_piercings_tongue_normal"
        if sasha.get_piercings("nose"):
            "sasha_foreplay_piercings_nose"
        if sasha.get_piercings("navel") and not sasha.get_flag_value("pregnant") >= 9:
            "sasha_foreplay_piercings_navel"
        if sasha.get_piercings("navel") and sasha.get_flag_value("pregnant") >= 9:
            "sasha_foreplay_piercings_navel_preg"
        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            "shower_foreplay_acc_collar"

        attribute boxer:
            "sasha_foreplay_boxer"

        group outfit:
            attribute underwear null
            attribute swimsuit null
            attribute rope null
            attribute naked null

        if sasha.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("boobjob"):
            if_any "underwear"
            "sasha_foreplay_outfit_bb_preg_underwear"
        elif sasha.get_flag_value("boobjob"):
            if_any "underwear"
            "sasha_foreplay_outfit_bb_underwear"
        elif sasha.get_flag_value("pregnant") >= 9:
            if_any "underwear"
            "sasha_foreplay_outfit_preg_underwear"
        else:
            if_any "underwear"
            "sasha_foreplay_outfit_underwear"

        if sasha.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("boobjob"):
            if_any "rope"
            "sasha_foreplay_outfit_bb_preg_rope"
        elif sasha.get_flag_value("boobjob"):
            if_any "rope"
            "sasha_foreplay_outfit_bb_rope"
        elif sasha.get_flag_value("pregnant") >= 9:
            if_any "rope"
            "sasha_foreplay_outfit_preg_rope"
        else:
            if_any "rope"
            "sasha_foreplay_outfit_rope"

        if sasha.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("boobjob") and not sasha.get_flag_value("sexyswimsuit"):
            if_any "swimsuit"
            "sasha_foreplay_outfit_bb_preg_swimsuit"
        elif sasha.get_flag_value("boobjob") and not sasha.get_flag_value("sexyswimsuit"):
            if_any "swimsuit"
            "sasha_foreplay_outfit_bb_swimsuit"
        elif sasha.get_flag_value("pregnant") >= 9 and not sasha.get_flag_value("sexyswimsuit"):
            if_any "swimsuit"
            "sasha_foreplay_outfit_preg_swimsuit"
        elif not sasha.get_flag_value("sexyswimsuit"):
            if_any "swimsuit"
            "sasha_foreplay_outfit_swimsuit"
        elif sasha.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("boobjob") and sasha.get_flag_value("sexyswimsuit"):
            if_any "swimsuit"
            "sasha_foreplay_outfit_bb_preg_sexyswimsuit"
        elif sasha.get_flag_value("boobjob") and sasha.get_flag_value("sexyswimsuit"):
            if_any "swimsuit"
            "sasha_foreplay_outfit_bb_sexyswimsuit"
        elif sasha.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("sexyswimsuit"):
            if_any "swimsuit"
            "sasha_foreplay_outfit_preg_sexyswimsuit"
        else:
            if_any "swimsuit"
            "sasha_foreplay_outfit_swimsuit"

        group acc auto multiple

        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            "sasha_foreplay_acc_collar"

        group cum auto multiple

        always:
            if_any "pool"
            "sasha_foreplay_water"

    layeredimage sasha mast:
        always:
            "sasha_mast_bg"
        always:
            "sasha_mast_body"
        if sasha.get_flag_value("haircut"):
            "sasha_mast_hair_blonde"
        else:
            "sasha_mast_hair_black"
        always:
            "sasha_mast_line"
        always:
            "sasha_mast_toys"

        if sasha.get_flag_value("pregnant") >= 9:
            "sasha_mast_preg"
        if sasha.get_flag_value("boobjob"):
            "sasha_mast_bb"

        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            "sasha_mast_piercings_nipples_bb"
        if sasha.get_piercings("nipples") and not sasha.get_flag_value("boobjob"):
            "sasha_mast_piercings_nipples"
        if sasha.get_piercings("tongue"):
            "sasha_mast_piercings_tongue"
        if sasha.get_piercings("nose"):
            "sasha_mast_piercings_nose"
        if sasha.get_piercings("clit"):
            "sasha_mast_piercings_clit"
        if sasha.get_piercings("navel") and not sasha.get_flag_value("pregnant") >= 9:
            "sasha_mast_piercings_navel"

        if not sasha.get_flag_value("pregnant") >= 9:
            "sasha_mast_pussy"
        else:
            "sasha_mast_pussy_preg"

        group left auto:
            attribute normal default

    layeredimage breeSasha threesome:
        attribute cumshot null

        always:
            "breeSasha_threesome_bg"
        always:
            "breeSasha_threesome_bodies"

        group sashaExp auto:
            attribute sashaNormal default

        group bree auto:
            attribute nobree default

        always:
            if_any "bree"
            "breeSasha_threesome_bree_face"

        group dick auto:
            attribute out default

        if sasha.get_flag_value("pregnant") >= 9:
            "breeSasha_threesome_sasha_pregnant"
        if sasha.get_flag_value("boobjob"):
            "breeSasha_threesome_sasha_bb"
        if not sasha.get_flag_value("haircut"):
            "breeSasha_threesome_sasha_hair_black"
        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            "breeSasha_threesome_sasha_collar"
        if bree.get_flag_value("collared") and bree.sub >= 50:
            if_any "bree"
            "breeSasha_threesome_bree_collar"
        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            "breeSasha_threesome_sasha_piercings_nipples_bb"
        if sasha.get_piercings("nose"):
            "breeSasha_threesome_sasha_piercings_nose"

        group cumshot auto multiple:
            if_any "cumshot"

        group fx auto multiple

    layeredimage breeSasha cumshot:
        always:
            "breeSasha_cumshot_bg"

        always:
            "breeSasha_cumshot_bree"
        always:
            "breeSasha_cumshot_bree_face"

        if bree.get_piercings("nipples"):
            "breeSasha_cumshot_bree_piercings_nipples"
        if bree.get_piercings("navel") and not bree.get_flag_value("pregnant") >= 9:
            "breeSasha_cumshot_bree_piercings_navel"
        if bree.get_flag_value("pregnant") >= 9:
            "breeSasha_cumshot_bree_preg"

        always:
            "breeSasha_cumshot_mike"
        always:
            "breeSasha_cumshot_sasha"

        group sasha_body auto:
            attribute suck default

        if sasha.get_flag_value("pregnant") >= 9:
            "breeSasha_cumshot_sasha_pregnant"

        if sasha.get_flag_value("boobjob"):
            if_any "suck"
            "breeSasha_cumshot_sasha_suck_bb"
        if sasha.get_flag_value("boobjob"):
            if_any "lick"
            "breeSasha_cumshot_sasha_lick_bb"
        if sasha.get_flag_value("boobjob"):
            if_any "spit"
            "breeSasha_cumshot_sasha_spit_bb"

        if not sasha.get_flag_value("haircut"):
            if_any "suck"
            "breeSasha_cumshot_sasha_suck_hair_black"
        if not sasha.get_flag_value("haircut"):
            if_any "spit"
            "breeSasha_cumshot_sasha_spit_hair_black"
        if not sasha.get_flag_value("haircut"):
            if_any "lick"
            "breeSasha_cumshot_sasha_lick_hair_black"

        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            if_any "suck"
            "breeSasha_cumshot_sasha_suck_collar"
        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            if_any "spit"
            "breeSasha_cumshot_sasha_spit_collar"

        if bree.get_flag_value("collared") and bree.sub >= 50:
            "breeSasha_cumshot_bree_collar"

        if sasha.get_piercings("nipples") and sasha.get_flag_value("boobjob"):
            if_any "spit"
            "breeSasha_cumshot_sasha_spit_piercings_nipples_bb"

        if sasha.get_piercings("nose"):
            if_any "spit"
            "breeSasha_cumshot_sasha_spit_piercings_nose"
        if sasha.get_piercings("nose"):
            if_any "suck"
            "breeSasha_cumshot_sasha_suck_piercings_nose"
        if sasha.get_piercings("nose"):
            if_any "lick"
            "breeSasha_cumshot_sasha_lick_piercings_nose"

        group sasha_face auto:
            attribute normal default

        group dick auto:
            attribute down default

        attribute cum null
        group cum auto:
            if_any "cum"

    layeredimage sasha foot:
        always:
            "sasha_foot_bg"

        always:
            "sasha_foot_sasha"
        if sasha.get_flag_value("pregnant") >= 9:
            "sasha_foot_preg"
        if sasha.get_flag_value("boobjob"):
            "sasha_foot_bb"
        if not sasha.get_flag_value("haircut"):
            "sasha_foot_hair_black"
        if sasha.get_flag_value("collared") and sasha.sub >= 50:
            "sasha_foot_collar"
        if sasha.get_piercings("navel") and sasha.get_flag_value("pregnant") >= 9:
            "sasha_foot_piercings_nipples_bb"
        if sasha.get_piercings("nose"):
            "sasha_foot_piercings_nose"

        always:
            "sasha_foot_mike"

        group mikeExp auto:
            attribute blush default

        group p auto:
            attribute massage default

        attribute cum:
            if_any "footjob"
            "sasha_foot_cum"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
