

init 1:
    layeredimage mike:
        attribute_function Picker(mike)

        attribute pregnant null

        group position:
            attribute a default

        group outfit auto variant "a" if_any "a":
            attribute naked null
        group outfit auto variant "b" if_any "b":
            attribute naked null

        group exp auto:
            attribute normal default

        group piercings multiple auto           
        attribute naked "mike_dick"

    layeredimage mike smartphone:
        always "mike_smartphone"

    layeredimage mike kiss:
        always:
            "bree_kiss"




        group outfit auto:
            attribute casual default
            attribute naked null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
