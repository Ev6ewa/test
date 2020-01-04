layeredimage bg pool:
    if game.hour >= 20 or game.hour <= 5:
        "pool_night"
    else:
        "pool_day"

init -2 python:
    Room(**{
        "name":"pool",
        "exits": ["livingroom", "secondfloor","kitchen", "bedroom1","bedroom2","bedroom3","bathroom", "bedroom4", "bedroom6"],
        "alternate_exits": ["livingroom"],
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"swimsuit"
        })

    Activity(**{
        "name": "swim_pool_home",
        "fun": 1,
        "fitness": 1,
        "duration": 1,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_grooming":0,"min_fun":3,"seasons":"01","room":["pool"]},
        "display_name": "Swim",
        "required_item": "swimsuit",
        "icon":"swim",
        "label": ["swim_pool_home"],
        "once_day": True
        })

    Activity(**{
        "name": "clean_the_pool",
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"room":["pool"],"flagmax_chores":99},
        "display_name": "Clean the pool",
        "label": ["clean_the_pool"],
        "icon":"cleanpool",
        "once_week": True
        })

    Event(**{
        "name":"wish_had_swimsuit",
        "label": ["wish_had_swimsuit"],
        "game_conditions": {"room":["pool"],"chances":5},
        "required_item":"not_swimsuit",
        "duration": 0,
        "do_once": True,
        "quit": False
        })

    Activity(**{
        "name": "pool_tan",
        "charm": 1,
        "fun": 1,
        "energy":1,
        "game_conditions": {
                "min_energy":0,
                "min_hunger":5,
                "min_grooming":5,
                "min_fun":0,
                "hours":(9,19),
                "seasons":"01",
                "room":["pool"]
                },
        "icon":"tan",
        "display_name": "sunbath",
        "once_day": True,
        "say": [
                "I take a nap in the sun",
                ]
        })

    Activity(**{
        "name": "play_in_the_pool_with_everyone",
        "duration": 1,
        "fun": 3,
        "icon":"playpool",
        "display_name": "Play with the girls",
        "girls_conditions": {
            "bree":{
                "present":True,
                "min_love": 10
                },
            "sasha":{
                "present":True,
                "min_love": 10
                },
            },
        "game_conditions": {
            "room":["pool"],
            "seasons":"01", 
            "flag_female":0
            },
        "once_day":True,
        "required_item": "swimsuit",
        "label": ["play_in_the_pool_with_everyone"]
        })

label play_in_the_pool_with_everyone:
    show sasha at left
    show bree at right
    "I play in the pool with the girls."
    $ bree.love += 1
    $ bree.set_flag("greeted",True,1)
    $ sasha.love += 1
    $ sasha.set_flag("greeted",True,1)
    return

label wish_had_swimsuit:
    "If only I had a swimsuit I could take a dive..."
    return

label clean_the_pool:
    $ game.set_flag("chores",25,"week","+")
    if game.get_flag_value("chores") > 100:
        $ bree.love += 1
        $ sasha.love += 1
    return

label swim_pool_home:
    python:
        swim_say = [
            "I go for a swim in the pool."
            ]
        successes = []
        for girl in ROOMS["pool"].get_present_girls():
            if hero.fitness()*2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes:
        if len(successes) == 1:
            show expression successes[0].id
            "[successes[0].name] can't takes her eyes off mewhile I swim."
            hide expression successes[0].id
        else:
            "The girls can't take their eyes off me while I swim."
    else:
        $ renpy.say("",randchoice(swim_say))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
