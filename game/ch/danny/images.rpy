init 1:
    layeredimage danny:
        group body auto:
            attribute basic default
        group exp auto:
            attribute normal default null

    layeredimage danny fight:

        attribute lexi if_any "win":
            "danny_fight_lexi_happy"

        attribute lexi if_any "lose":
            "danny_fight_lexi_sad"

        attribute win:
            "danny_fight_danny_win"

        attribute win:
            "danny_fight_hero_lose"

        attribute lose:
            "danny_fight_hero_win"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
