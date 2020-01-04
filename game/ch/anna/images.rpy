

init 1:
    layeredimage anna:
        attribute_function Picker(anna)

        attribute pregnant null

        group position:
            attribute a null default
            attribute b null

        group outfit auto variant "a" if_any "a" if_not "pregnant"
        group outfit auto variant "b" if_any "b" if_not "pregnant"
        group outfit auto variant "a_pregnant" if_all ["a", "pregnant"]
        group outfit auto variant "b_pregnant" if_all ["b", "pregnant"]

        group exp auto variant "a" if_any "a":
            attribute normal default
        group exp auto variant "b" if_any "b":
            attribute normal default

        group piercings multiple auto variant "a" if_any "a"
        group piercings multiple auto variant "b" if_any "b"           









    layeredimage anna smartphone:
        always "anna_smartphone"

    layeredimage anna cowgirl:
        always "anna_cowgirl_back"
        group body auto:
            attribute a default
        group con:
            attribute condom null
            attribute nocondom null default
        group ty:
            attribute anal:
                if_not "nocondom"
                "anna_cowgirl_dick_anal_condom"
            attribute anal:
                if_any "nocondom"
                "anna_cowgirl_dick_anal_nocondom"
            attribute vag default:
                if_not "nocondom"
                "anna_cowgirl_dick_vag_condom"
            attribute vag default:
                if_any "nocondom"
                "anna_cowgirl_dick_vag_nocondom"
            attribute out:
                if_any "nocondom"
                "anna_cowgirl_dickout_nocondom"
            attribute out:
                if_any "condom"
                "anna_cowgirl_dickout_condom"
        attribute beads:
            if_not "anal"
            "anna_cowgirl_beads"
        attribute xray:
            if_all ["xray","anal","condom"]
            if_not ["ass","beads"]
            "anna_cowgirl_xray_anal_condom"
        attribute xray:
            if_all ["xray","anal","nocondom"]
            if_not ["ass","beads"]
            "anna_cowgirl_xray_anal_nocondom"
        attribute xray:
            if_all ["xray","vag","condom"]
            if_not ["ass","beads"]
            "anna_cowgirl_xray_vag_condom"
        attribute xray:
            if_all ["xray","vag","nocondom"]
            if_not ["ass","beads"]
            "anna_cowgirl_xray_vag_nocondom"
        attribute cum:
            if_any "anal"
            if_not ["condom", "xray"]
            "anna_cowgirl_anal_cum"
        attribute cum:
            if_any "vag"
            if_not ["condom", "xray"]
            "anna_cowgirl_vag_cum"
        attribute cum:
            if_any "out"
            if_not ["condom", "xray"]
            "anna_cowgirl_cum_outside"
        group finger:
            attribute ass:
                if_not "anal"
                "anna_cowgirl_arm_b"
            attribute rest default:
                "anna_cowgirl_arm_a"

    layeredimage anna kiss:
        always:
            "anna_kiss_body"

        group man:
            attribute clothed default "anna_kiss_man_outfit"
            attribute undressed null

        group outfit auto:
            attribute casual default
            attribute naked null

    layeredimage threesome ak:

        group act:
            attribute suck default null
            attribute fuck null
        always "threesome_ak_bg"
        always "threesome_ak_body"
        group expanna auto
        group expkleio auto
        group hand auto
        if anna.get_piercings("tongue"):
            if_any ["fuck"]
            if_not ["suck"]
            "threesome_ak_pieranna_tongue"
        if anna.get_piercings("nose"):
            "threesome_ak_pieranna_nose"
        if kleio.get_piercings("tongue"):
            if_any ["fuck"]
            if_not ["suck"]
            "threesome_ak_pierkleio_tongue"
        if anna.get_piercings("nose"):
            "threesome_ak_pierkleio_nose"
        if anna.get_piercings("nipples"):
            "threesome_ak_pierkleio_nose"
        attribute xray:
            if_all ["fuck"]
            if_not ["suck"]
            "threesome_ak_cum_xray"
        attribute cum:
            if_all ["fuck"]
            if_not ["suck","xray"]
            "threesome_ak_cum_pussy"
        attribute cum:
            if_all ["suck"]
            if_not ["fuck","xray"]
            "threesome_ak_cum_mouth"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
