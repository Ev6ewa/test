layeredimage bg bedroom6:
    if game.hour >= 20 or game.hour <= 5:
        "bedroom6_night"
    else:
        "bedroom6_day"

init -2 python:
    Room(**{
        "name":"bedroom6",
        "exits": ["livingroom", "secondfloor","kitchen","pool","bedroom2","bedroom3","bathroom", "bedroom4"],
        "alternate_exits": ["livingroom"],
        "display_name": "Mike's bedroom",
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
