init 1:
    layeredimage scottie:
        attribute_function Picker(scottie)

        attribute pregnant null

        group position:
            attribute a default

        group outfit auto variant "a" if_any "a":
            attribute naked null
        group outfit auto variant "b" if_any "b":
            attribute naked null

        group exp auto:
            attribute normal default null

        always:
            if_all ["naked"]
            "scottie_dick"
        group piercings multiple auto           
        group acc multiple auto


    layeredimage scottie smartphone:
        always "scottie_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
