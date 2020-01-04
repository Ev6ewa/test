init 1:
    layeredimage kleio:
        attribute_function Picker(kleio)

        attribute pregnant null

        group position auto variant "pregnant" if_any "pregnant"
        group position auto if_not "pregnant"

        group exp auto:
            attribute normal default

        group piercings multiple auto           

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
            "kleio_pubes_a"  
        attribute pubes:
            if_all ["naked","b"]
            "kleio_pubes_b"  

    layeredimage kleio smartphone:
        always "kleio_smartphone"

    layeredimage kleio topless:
        always "kleio_topless"


    layeredimage kleio rough:

        attribute condom null

        group bg auto:
            attribute studio default

        group position:
            attribute basic default:
                "kleio_rough_normal_body"
            attribute step:
                "kleio_rough_step_body"

        if kleio.get_flag_value("pregnant") >= 9:
            "kleio_rough_pregnant"

        group exp:
            attribute ahegao null
            attribute lick null
            attribute normal null

        always:
            if_all ["step","ahegao"]
            "kleio_rough_step_ahegao"
        always:
            if_not "step"
            if_any "ahegao"
            "kleio_rough_normal_ahegao"
        always:
            if_not "step"
            if_any "lick"
            "kleio_rough_step_lick"
        always:
            if_not ["step", "ahegao","lick"]
            "kleio_rough_normal_normal"
        always:
            if_any "step"
            if_not ["ahegao","lick"]
            "kleio_rough_step_normal"

        group penetration:
            attribute anal:
                "kleio_rough_anal_base"
            attribute vaginal default:
                "kleio_rough_vaginal_base"
            attribute out:
                "kleio_rough_out_base"

        if kleio.get_piercings("clit"):
            if_not "anal"
            "kleio_rough_vaginal_piercing"
        if kleio.get_piercings("clit"):
            if_not "vaginal"
            "kleio_rough_anal_piercing"

        if kleio.get_piercings("tongue"):
            if_any "ahegao"
            "kleio_rough_piercings_tongue_ahegao"
        if kleio.get_piercings("tongue"):
            if_any ["normal", "lick"]
            "kleio_rough_piercings_tongue_normal"

        attribute cum null
        always:
            if_all ["cum","anal"]
            if_not "vaginal"
            "kleio_rough_anal_cum"
        always:
            if_all ["cum","vaginal"]
            if_not "anal"
            "kleio_rough_vaginal_cum"

        attribute xray null
        always:
            if_all ["anal","xray"]
            if_not "vaginal"
            "kleio_rough_anal_xray"
        always:
            if_all ["vaginal","xray"]
            if_not "anal"
            "kleio_rough_vaginal_xray"

        if kleio.get_flag_value("pubes",kleio.pubes):
            "kleio_rough_pubes"  

        if kleio.get_piercings("nipples"):
            "kleio_rough_piercings_nipples"
        if kleio.get_piercings("navel"):
            "kleio_rough_piercings_navel"
        if kleio.get_piercings("nose"):
            "kleio_rough_piercings_nose"    

        attribute dick:
            if_any "out"
            "kleio_rough_out_dick"

        attribute cumshot null
        if kleio.get_flag_value("pregnant") >= 9:
            if_all ["cumshot","dick","out"]
            "kleio_rough_out_cumshot_pregnant"
        if kleio.get_flag_value("pregnant") < 9:
            if_all ["cumshot","dick","out"]
            "kleio_rough_out_cumshot"

        group man:
            attribute man default:
                "kleio_rough_man"
            attribute none null


    layeredimage kleio kiss:
        attribute underwear null

        always:
            "kleio_kiss"

        group outfit auto:
            attribute casual default
            attribute naked null

        group man auto:
            attribute normal default
            attribute none null

        if kleio.get_piercings("nipples"):
            if_any ["naked","underwear"]
            "kleio_kiss_piercings_nipples"

    layeredimage kleio doggy:

        attribute xray null

        always "kleio_doggy_bg"
        always "kleio_doggy_base"

        group penetration auto:
            attribute vaginal null default
            attribute anal null

        if kleio.get_flag_value("pregnant") >= 9:
            "kleio_doggy_pregnant"

        group exp auto:
            attribute ahegao
            attribute cum
            attribute normal default

        attribute facial:
            "kleio_doggy_facial"

        attribute cumshot:
            if_all ["dick"]
            "kleio_doggy_cumout"

        attribute cumshot:
            if_all ["xray","vaginal"]
            if_not ["condom"]
            "kleio_doggy_xray_vaginal"

        attribute cumshot:
            if_all ["xray","anal"]
            if_not ["condom"]
            "kleio_doggy_xray_anal"

        attribute condom:
            if_all ["vaginal", "xray"]
            "kleio_doggy_xray_vaginal_condom"











    layeredimage kleio bj:
        attribute casual null

        group bg:
            attribute studio:
                "kleio_bj_bg_studio"
            attribute bedroom default:
                "kleio_bj_bg_room"

        always:
            "kleio_bj_base"

        group outfit auto:
            attribute naked null default

        group head:
            attribute lick default:
                "kleio_bj_head_lick"
            attribute suck:
                "kleio_bj_head_suck"

        group exp:
            attribute closed:
                if_any "suck"
                "kleio_bj_exp_suck_closed"
            attribute open:
                if_any "suck"
                "kleio_bj_exp_suck_open"
            attribute closed:
                if_any "lick"
                "kleio_bj_exp_lick_closed"
            attribute open default:
                if_any "lick"
                "kleio_bj_exp_lick_open"

        attribute cumshot:
            if_all ["suck"]
            "kleio_bj_suck_cum"

        attribute cumshot:
            if_all ["lick"]
            "kleio_bj_lick_cum"

        attribute facial:
            "kleio_bj_facial"

        if kleio.get_piercings("tongue"):
            if_all ["lick"]
            "kleio_bj_piercings_tongue"




        if kleio.get_piercings("nose"):
            if_all ["lick"]
            "kleio_bj_piercings_lick_nose"
        elif kleio.get_piercings("nose"):
            if_all ["suck"]
            "kleio_bj_piercings_suck_nose"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
