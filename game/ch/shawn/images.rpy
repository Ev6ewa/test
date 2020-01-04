init 1:
    layeredimage shawn:
        always:
            "shawn_head"
        group outfit auto:
            attribute shirt default
        group exp auto:
            attribute normal default null
        always:
            if_any ["shady","shady-hands"]
            "shawn_glasses"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
