init 1 python:
    class PallaPicker(Picker):
        def outfits(self, attr):
            attr = Picker.outfits(self, attr)
            if ('swimsuit' in attr or 'sexyswimsuit' in attr or 'casual' in attr) and palla.room in ['waterpark', 'date_waterpark', 'beach', 'date_beach', 'mall', 'map', 'park']:
                attr.add('glasses')
            
            return attr

init 1:
    layeredimage palla:
        attribute_function PallaPicker(palla)


        group position auto

        group exp auto:
            attribute normal default


        group acc multiple auto
        group acc multiple auto  variant "a" if_any "a"
        group acc multiple auto  variant "b" if_any "b"


        attribute pregnant if_any "a":
            "palla_pregnant_a"
        attribute pregnant if_any "b":
            "palla_pregnant_b"


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

        attribute pubes if_any "naked"

    layeredimage palla smartphone:
        always "palla_smartphone"

    layeredimage palla stand:
        always "palla_stand_bg"
        always "palla_stand_body"

        attribute cumscreen

        group exp auto:
            attribute angry default
        group dick auto:
            attribute nodick default null
        attribute cum:
            if_all ["dick"]
            if_not ["nodick"]
            "palla_stand_cum_dick"
        attribute cum:
            if_all ["nodick"]
            if_not ["dick"]
            "palla_stand_cum_nodick"
        attribute wet:
            if_all ["dick"]
            if_not ["nodick"]
            "palla_stand_wet_dick"
        attribute wet:
            if_all ["nodick"]
            if_not ["dick"]
            "palla_stand_wet_nodick"

        if palla.get_piercings("tongue"):
            if_any ['angry', 'pleasure']
            "palla_stand_piercings_tongue"

        if palla.get_piercings("lips"):
            if_any ['angry', 'pleasure']
            "palla_stand_piercings_lipspleasure"
        if palla.get_piercings("lips"):
            if_any 'smile'
            "palla_stand_piercings_lipssmile"

        if palla.get_piercings("nose"):
            "palla_stand_piercings_nose"

        if palla.get_piercings("nipples"):
            "palla_stand_piercings_nipples"

        if palla.get_piercings("navel"):
            "palla_stand_piercings_navel"

    layeredimage palla doggy:
        always "palla_doggy_bg"
        always "palla_doggy_body"

        attribute pubes

        group exp auto:
            attribute normal default
        if palla.get_flag_value("pregnant") >= 9:
            "palla_doggy_pregnant"
        if palla.get_piercings("tongue"):
            if_any ["orgasm"]
            "palla_doggy_piercings_tongue_orgasm"
        if palla.get_piercings("tongue"):
            if_any ["ahegao"]
            "palla_doggy_piercings_tongue_ahegao"
        if palla.get_piercings("tongue"):
            if_any ["normal"]
            "palla_doggy_piercings_tongue_normal"
        if palla.get_piercings("nose"):
            if_any ["orgasm"]
            "palla_doggy_piercings_nose_orgasm"
        if palla.get_piercings("nose"):
            if_any ["ahegao"]
            "palla_doggy_piercings_nose_ahegao"
        if palla.get_piercings("nose"):
            if_any ["normal"]
            "palla_doggy_piercings_nose_normal"
        if palla.get_piercings("lips"):
            if_any ["orgasm"]
            "palla_doggy_piercings_lips_orgasm"
        if palla.get_piercings("lips"):
            if_any ["ahegao"]
            "palla_doggy_piercings_lips_ahegao"
        if palla.get_piercings("lips"):
            if_any ["normal"]
            "palla_doggy_piercings_lips_normal"

    layeredimage palla restaurantbj:
        always "palla_restaurantbj_bg"

        group body auto:
            attribute kissdick default

        group cum auto if_any ['kissdick', 'suckdick']

    layeredimage palla kiss:
        attribute_function PallaPicker(palla, False, False)

        always:
            "palla_kiss"

        group outfit auto:
            attribute casual default
            attribute naked null

        group outfitMike auto:
            attribute mikeCasual default
            attribute mikeNaked null

        group acc multiple auto 

layeredimage pallaAudrey threesome:

    always "pallaAudrey_threesome_bg"
    always "pallaAudrey_threesome_girls"

    group audreyExp auto:
        attribute audreyOpen default

    group pallaExp auto:
        attribute pallaOpen default

    if palla.get_flag_value("pregnant") >= 9:
        "pallaAudrey_threesome_palla_pregnant"

    if audrey.get_flag_value("pregnant") >= 9:
        "pallaAudrey_threesome_audrey_pregnant"

    if palla.get_flag_value("collared"):
        "pallaAudrey_threesome_palla_collar"

    if audrey.get_flag_value("collared"):
        "pallaAudrey_threesome_audrey_collar"

    if palla.get_piercings("nose"):
        "pallaAudrey_threesome_palla_piercings_nose"

    if palla.get_piercings("clit"):
        "pallaAudrey_threesome_palla_piercings_clit"

    if palla.get_piercings("ears"):
        "pallaAudrey_threesome_palla_piercings_ears"

    if audrey.get_piercings("nose"):
        "pallaAudrey_threesome_audrey_piercings_nose"

    if audrey.get_piercings("nipples"):
        "pallaAudrey_threesome_audrey_piercings_nipples"

    if audrey.get_piercings("ears"):
        "pallaAudrey_threesome_audrey_piercings_ears"

    attribute strapOn:
        "pallaAudrey_threesome_strapOn"

    group acc auto multiple

    always:
        "pallaAudrey_threesome_audrey_arm"

    attribute mike:
        "pallaAudrey_threesome_mike"

    group dick auto if_any "mike":
        attribute ass null

    group fx auto multiple
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
