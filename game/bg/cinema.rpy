layeredimage bg cinema:
    if game.hour >= 20 or game.hour <= 5 and game.season == 0:
        "cinema_0_night"
    elif game.season == 0:
        "cinema_0_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 1:
        "cinema_1_night"
    elif game.season == 1:
        "cinema_1_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 2:
        "cinema_2_night"
    elif game.season == 2:
        "cinema_2_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 3:
        "cinema_3_night"
    elif game.season == 3:
        "cinema_3_day"

init -2 python:
    Room(**{
        "name":"cinema",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Movie Theater",
        "hours": (14,23),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "watch_a_movie",
        "duration": 2,
        "fun": 5,
        "icon":"cinema",
        "money_cost": 10,
        "display_name": "Watch a movie",
        "game_conditions":{"room":["cinema"]},
        "label": ["watch_movie"],
        })

label watch_movie:
    "I go watch a movie"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
