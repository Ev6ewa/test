init 1:
    layeredimage lavish:
        attribute_function Picker(lavish)

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
            if_all ["naked"]
            "lavish_pubes"  

    layeredimage lavish smartphone:
        always "lavish_smartphone"

    layeredimage lavish kiss:
        group outfit auto:
            attribute casual null default
            attribute naked null
            attribute date null
            attribute sport null
            attribute sexyswimsuit null
            attribute swimsuit null
            attribute underwear null
            attribute work null

    layeredimage lavish files:
        always "lavish_files"

    layeredimage lavish pool sex:
        always "lavish_pool"

    layeredimage lavish missionary:
        always:
            "lavish_missionary_bg"
        always:
            "lavish_missionary_body"

        group exp auto

        if lavish.get_flag_value("pregnant") >= 9:
            "lavish_missionary_piercings_preg" 
        if lavish.get_piercings("tongue"):
            if_not "normal"
            "lavish_missionary_piercings_tongue"
        if lavish.get_piercings("nipples"):
            "lavish_missionary_piercings_nipples"
        if lavish.get_piercings("nose"):
            "lavish_missionary_piercings_nose"
        if lavish.get_piercings("lips"):
            "lavish_missionary_piercings_lips"
        if lavish.get_piercings("clit"):
            "lavish_missionary_piercings_clit"
        if lavish.get_piercings("ears"):
            "lavish_missionary_piercings_ears"
        if lavish.get_piercings("navel") and lavish.get_flag_value("pregnant") >= 9:
            "lavish_missionary_piercings_navel"
        if lavish.get_piercings("navel") and not lavish.get_flag_value("pregnant") >= 9:
            "lavish_missionary_piercings_navel_preg"

        group dick auto

        attribute condom:
            "lavish_missionary_condom"

        group cum auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
