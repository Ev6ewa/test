layeredimage bg bedroom2:
    if game.hour >= 20 or game.hour <= 5:
        "bedroom2_night"
    else:
        "bedroom2_day"

init -2 python:
    Room(**{
        "name":"bedroom2",
        "exits": ["livingroom", "secondfloor","kitchen","pool", "bedroom1","bedroom3","bathroom", "bedroom4", "bedroom6"],
        "alternate_exits": ["secondfloor"],
        "display_name": "Bree's bedroom",
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
