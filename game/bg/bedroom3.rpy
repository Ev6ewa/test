layeredimage bg bedroom3:
    if game.hour >= 20 or game.hour <= 5:
        "bedroom3_night"
    else:
        "bedroom3_day"

init -2 python:
    Room(**{
        "name":"bedroom3",
        "exits": ["livingroom", "secondfloor","kitchen","pool", "bedroom1","bedroom2","bathroom", "bedroom4", "bedroom6"],
        "alternate_exits": ["secondfloor"],
        "display_name": "Sasha's bedroom",
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
