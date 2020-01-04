layeredimage bg date_cinema:
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
        "name":"date_cinema",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "Movie Theater",
        "hours": (14,24),
        "money_cost": 30,
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Date(
        "cinema",
        display_name="cinema",
        money_cost=30,
        game_conditions={"valid_room":"date_cinema"},
        clothes = "casual",
        )

    Activity(**{
        "name": "date_watch_a_movie",
        "duration": 0,
        "game_conditions":{"room":["date_cinema"]},
        "display_name": "Watch a movie",
        "icon":"cinema",
        "label": ["date_watch_movie"]
        })

    Activity(**{
        "name": "date_buy_popcorn",
        "duration": 0,
        "game_conditions":{"room":["date_cinema","date_cinemaroom"]},
        "hunger": 1,
        "icon": "buypopcorn",
        "money_cost":10,
        "display_name": "Buy popcorn",
        "label": ["date_buy_popcorn"],
        "once_day": True
        })

    Event(**{
        "name": "date_no_seat_left",
        "label": ["date_no_seat_left"],
        "duration": 0,
        "game_conditions": {
            "activity":["date_watch_a_movie"],
            "chances": 5,
            },
        "once_day": True,
        })

label date_buy_popcorn:
    show expression game.active_girl.id
    "We buy some popcorn."
    call expression game.active_girl.get_chat() from _call_expression_86
    if "gourmand" in game.active_girl.traits:
        $ game.set_flag("datescore",5,1,"+")
    return

label date_no_seat_left:
    "When we reach the cinema, an employee tells us that it's full."
    show expression game.active_girl.id
    "[game.active_girl.name] looks a little disappointed."
    $ renpy.hide((game.active_girl.id))
    $ choices = [("Leave",1),("Convince the employee",2),("Try to sneak in",4)]
    if hero.money >= 10:
        $ choices.append(("Bribe the employee",3))
    $ result = renpy.display_menu(choices)
    if result == 1:
        hero.say "Too bad, maybe next time."
        $ game.set_flag("datescore",5,1,"+")
        $ game.pass_time(2, needs=True)
    elif result ==2:
        hero.say "Are you sure you can't let us in ?"
        if hero.charm >= 20:
            $ renpy.say("Employee","Ok, but just this time.")
            $ game.set_flag("datescore",5,1,"+")
        else:
            $ renpy.say("Employee","Absolutely not.")
            $ game.set_flag("datescore",5,1,"+")
            $ game.pass_time(2, needs=True)
    elif result ==3:
        hero.say "I give 10 bucks to the employee."
        $ hero.money -= 10
        $ renpy.say("Employee","Ok, but just this time.")
        $ game.set_flag("datescore",5,1,"+")
    else:
        "We sneak into the movie theater from the back door."
        if game.active_girl.has_trait("rebel"):
            $ game.set_flag("datescore",10,1,"+")
        elif game.active_girl.has_trait("not_rebel"):
            show expression game.active_girl.id
            active_girl.say "We shouldn't be doing that."
            $ renpy.hide((game.active_girl.id))
    return

label date_cinema:
    if game.active_girl:
        show expression game.active_girl.id
        "We go to the cinema."
        $ renpy.hide((game.active_girl.id))
    return

label date_watch_movie:
    show expression game.active_girl.id
    active_girl.say "What kind of movie should we go see ?"
    $ movie = renpy.call_screen("select",["action", "comedy","horror","romance","science fiction"],"movies")
    $ game.room="date_cinemaroom"
    call enter_room (room_present_girls=[game.active_girl.id], max_time=2) from _call_enter_room_1
    $ game.active_girl = game.get_flag_value("dateinprogress")
    if "cinema" in game.active_girl.desire_factors:
        $ love_gain = 2
    elif "not_cinema" in game.active_girl.desire_factors:
        $ love_gain = 0.5
    else:
        $ love_gain = 1
    python:
        for g in game.active_girl.desire_factors:
            if g == movie:
                love_gain = love_gain*1.5
            elif g == "not_"+movie:
                love_gain = love_gain/2
        game.set_flag("datescore",love_gain*5, 1, '+')
        renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
