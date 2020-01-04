init 1 python:
    class CassidyPicker(Picker):
        def outfits(self, attr):
            attr = Picker.outfits(self, attr)
            
            if cassidy.get_flag_value('gold'):
                if 'swimsuit' in attr:
                    attr.remove('swimsuit')
                    attr.add('swimsuit_gold')
                if 'sexyswimsuit' in attr:
                    attr.remove('sexyswimsuit')
                    attr.add('sexyswimsuit_gold')
            
            return attr

init 1:
    layeredimage cassidy:
        attribute_function CassidyPicker(cassidy)


        group position auto


        attribute pregnant if_any "a":
            "cassidy_pregnant_a"
        attribute pregnant if_any "b":
            "cassidy_pregnant_b"


        attribute blush if_any "a":
            "cassidy_blush_a"
        attribute blush if_any "b":
            "cassidy_blush_b"


        attribute facecum if_any "a":
            "cassidy_facecum_a"
        attribute facecum if_any "b":
            "cassidy_facecum_b"


        attribute wet if_any "a":
            "cassidy_wet_a"
        attribute wet if_any "b":
            "cassidy_wet_b"


        group exp auto variant "a" if_any "a":
            attribute normal default
        group exp auto variant "b" if_any "b":
            attribute normal default


        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"


        group acc multiple auto  variant "a" if_any "a"
        group acc multiple auto  variant "b" if_any "b"

        attribute topless null
        attribute bottomless null


        group bot auto variant "a" if_any "a" if_not ["bottomless", "pregnant"]:
            attribute naked null
            attribute work "cassidy_bot_a_casual"
        group bot auto variant "b" if_any "b" if_not ["bottomless", "pregnant"]:
            attribute naked null
            attribute work "cassidy_bot_b_casual"
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not "bottomless":
            attribute naked null
            attribute work "cassidy_bot_a_pregnant_casual"
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not "bottomless":
            attribute naked null
            attribute work "cassidy_bot_b_pregnant_casual"
        group top auto variant "a" if_any "a" if_not ["topless", "pregnant"]:
            attribute naked null
            attribute work "cassidy_top_a_casual"
        group top auto variant "b" if_any "b" if_not ["topless", "pregnant"]:
            attribute naked null
            attribute work "cassidy_top_b_casual"
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not "topless":
            attribute naked null
            attribute work "cassidy_top_a_pregnant_casual"
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not "topless":
            attribute naked null
            attribute work "cassidy_top_b_pregnant_casual"

    layeredimage cassidy smartphone:
        always "cassidy_smartphone"

    layeredimage cassidy kiss:
        always:
            "cassidy_kiss"
        always:
            "cassidy_kiss_mike_shirt_red"

        group outfit auto:
            attribute naked null
            attribute swimsuit null
            attribute sexyswimsuit null

        if cassidy.get_flag_value("gold"):
            if_any 'sexyswimsuit'
            "cassidy_kiss_outfit_sexyswimsuit_gold"
        else:
            if_any 'sexyswimsuit'
            "cassidy_kiss_outfit_sexyswimsuit"

        if cassidy.get_flag_value("gold"):
            if_any 'swimsuit'
            "cassidy_kiss_outfit_swimsuit_gold"
        else:
            if_any 'swimsuit'
            "cassidy_kiss_outfit_swimsuit"

        if cassidy.love > 160:
            "cassidy_kiss_flare"

    layeredimage cassidy tittyfuck:
        if game.room == 'personal':
            "cassidy_tittyfuck_bg_office"
        else:
            "cassidy_tittyfuck_bg_bedroom"

        always:
            "cassidy_tittyfuck_mike_legs"
        always:
            "cassidy_tittyfuck_mike"
        always:
            "cassidy_tittyfuck_tits"

        attribute dickhead

        group outfit:
            attribute top default
            attribute topless null

        group head auto:
            attribute up default

        group expup auto if_any ['up']:
            attribute closed default

        group expsuck auto if_any ['suck']:
            attribute closed default

        if cassidy.get_piercings("eyebrow"):
            if_any 'up'
            "cassidy_tittyfuck_piercings_eyebrowup"

        if cassidy.get_piercings("lips"):
            if_any 'up'
            "cassidy_tittyfuck_piercings_lipsup"

        if cassidy.get_piercings("eyebrow"):
            if_any 'suck'
            "cassidy_tittyfuck_piercings_eyebrowsuck"

        if cassidy.get_piercings("lips"):
            if_any 'suck'
            "cassidy_tittyfuck_piercings_lipssuck"

        if cassidy.get_piercings("nipples"):
            if_any 'topless'
            "cassidy_tittyfuck_piercings_nipples"

        group cum:
            attribute cum if_any ['up']
            attribute facecum if_any ['up']
            attribute mouthcum if_any ['suck']

    layeredimage cassidy miss:
        always:
            "cassidy_miss_bg"
        always:
            "cassidy_miss_cassidy"

        if cassidy.get_flag_value("pregnant") >= 9:
            "cassidy_miss_pregnant"

        group exp auto:
            attribute normal default

        if cassidy.get_piercings("lips"):
            "cassidy_miss_piercings_lips"

        if cassidy.get_piercings("eyebrow"):
            if_any 'ahegao'
            "cassidy_miss_piercings_eyebrowahegao"
        if cassidy.get_piercings("eyebrow"):
            if_any 'pain'
            "cassidy_miss_piercings_eyebrowpain"
        if cassidy.get_piercings("eyebrow"):
            if_any 'normal'
            "cassidy_miss_piercings_eyebrownormal"
        if cassidy.get_piercings("nipples"):
            "cassidy_miss_piercings_nipples"
        if cassidy.get_piercings("navel"):
            "cassidy_miss_piercings_navel"

        group dick auto:
            attribute outside default

        attribute condom if_any ['vaginal']

        if persistent.xray:
            if_all ['vaginal'] if_not ['condom']
            "cassidy_miss_xray_vaginal"
        if persistent.xray:
            if_all ['vaginal', "cum"] if_not ['condom']
            "cassidy_miss_xray_cum"
        if persistent.xray:
            if_all ['anal']
            "cassidy_miss_xray_anal"
        if cassidy.get_piercings("clit"):
            if_not ['outside']
            "cassidy_miss_piercings_clit"

        attribute bellycum if_all ['outside']

        attribute cum if_all ['outside']:
            "cassidy_miss_cum_outside"

        if not persistent.xray:
            if_all ['cum', 'vaginal'] if_not ['condom']
            "cassidy_miss_cum_vaginal"

    layeredimage cassidy lick:
        group bg auto:
            attribute desk default
        always:
            "cassidy_lick_body"

        if cassidy.get_flag_value("pregnant") >= 9:
            "cassidy_lick_pregnant"

        if cassidy.get_piercings("eyebrow"):
            "cassidy_lick_piercings_eyebrow"
        if cassidy.get_piercings("lips"):
            "cassidy_lick_piercings_lips"
        if cassidy.get_piercings("nipples"):
            if_any 'naked'
            "cassidy_lick_piercings_nipples"
        if cassidy.get_piercings("clit"):
            "cassidy_lick_piercings_clit"
        if cassidy.get_piercings("navel") and cassidy.get_flag_value("pregnant") >= 9:
            "cassidy_lick_piercings_navelpregnant"
        elif cassidy.get_piercings("navel"):
            "cassidy_lick_piercings_navel"


        if cassidy.get_flag_value("pregnant") >= 9:
            if_not 'naked'
            "cassidy_lick_outfit_pregnantcasual"
        else:
            if_not 'naked'
            "cassidy_lick_outfit_casual"

        attribute naked null
        attribute mikeclothes
        attribute cum
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
