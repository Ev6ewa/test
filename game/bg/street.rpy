layeredimage bg street:
    if game.hour >= 20 or game.hour <= 5 and game.season == 0:
        "street_0_night"
    elif game.season == 0:
        "street_0_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 1:
        "street_1_night"
    elif game.season == 1:
        "street_1_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 2:
        "street_2_night"
    elif game.season == 2:
        "street_2_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 3:
        "street_3_night"
    elif game.season == 3:
        "street_3_day"

layeredimage bg alley:
    if game.hour >= 20 or game.hour <= 5 and game.season == 0:
        "alley_0_night"
    elif game.season == 0:
        "alley_0_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 1:
        "alley_1_night"
    elif game.season == 1:
        "alley_1_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 2:
        "alley_2_night"
    elif game.season == 2:
        "alley_2_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 3:
        "alley_3_night"
    elif game.season == 3:
        "alley_3_day"

layeredimage bg rooftop:
    if game.hour >= 20 or game.hour <= 5:
        "rooftop"
    else:
        "rooftop"

init -2 python:
    Room(**{
        "name":"street",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
