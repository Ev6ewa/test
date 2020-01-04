layeredimage bg bedroom1:
    if game.hour >= 20 or game.hour <= 5:
        "bedroom1_night"
    else:
        "bedroom1_day"

init -2 python:
    Room(**{
        "name":"bedroom1",
        "exits": ["livingroom", "secondfloor","kitchen","pool","bedroom2","bedroom3","bathroom", "bedroom4", "bedroom6"],
        "alternate_exits": ["livingroom"],
        "display_name": "My bedroom",
        "music": "music/TRG_Banks/lost_in_the_city.mp3",
        "outfit":"casual"
        })

    Activity(**{
        "name": "sleep",
        "duration": 0,
        "label":["sleep"],
        "game_conditions": {
            "room":["bedroom1","bedroom4"],
            "min_grooming":0,
            "min_fun":0,
            "min_hunger":1,
            "min_energy":0,
            "max_energy":8,
            },
        "icon":"sleep",
        "display_name": "Sleep",
        "once_day":False
        })


    Activity(**{
        "name": "set_alarm",
        "duration": 0,
        "game_conditions": {
            "room":["bedroom1","bedroom4"],
            "min_grooming":0,
            "min_fun":0,
            "min_hunger":0,
            "min_energy":0
            },
        "icon":"alarm",
        "label": ["set_alarm"],
        "display_name": "Set Alarm",
        })

    Activity(**{
        "name": "clean_my_bedroom",
        "game_conditions": {
            "room":["bedroom1","bedroom4"],
            "min_energy":2,
            "min_hunger":2,
            "min_grooming":2,
            "min_fun":2,
            "flagmax_chores":99
            },
        "icon":"vacuum",
        "display_name": "Clean my bedroom",
        "label": ["clean_my_bedroom"],
        "once_week": True
        })

    Event(**{
        "name": "sleep_nightmare",
        "label": ["sleep_nightmare"],
        "duration": 0,
        "game_conditions": {
            "activity":"sleep_dream",
            "max_fun":2,
            "chances":20,
            },
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name": "sleep_dream",
        "label": ["sleep_dream"],
        "duration": 0,
        "game_conditions": {
            "activity":"sleep_dream",
            "min_fun":8,
            "chances":20,
            },
        "do_once": False,
        "once_day": True
        })

    Activity(**{
        "name": "dopushups",
        "fitness": 0.5,
        "game_conditions": {
            "room":["bedroom1","bedroom4"],
            "min_energy":5,
            "min_hunger":5,
            "min_grooming":5,
            "min_fun":5,
            "max_fitness":25
            },
        "display_name": "Do some push-ups",
        "once_day": True,
        "icon":"push",
        "say": [
            "1, 2, 3, 4...",
            "10, 11, 12, 13, 14...",
            "100, 101, 102, 103, 104...",
            "1000, 1001, 1002, 1003, 1004...",
            "10000, 10001, 10002, 10003, 10004...",
            ]
        })

label take_a_nap:
    scene bg black
    with dissolve
    "I sleep for a while."
    scene expression "bg "+game.room
    with dissolve
    $ hero.energy += 2
    return

label clean_my_bedroom:
    $ game.set_flag("chores",25,"week","+")
    if game.get_flag_value("chores") > 100:
        $ bree.love += 1
        $ sasha.love += 1
    return

label sleep_dream:
    "I had a nice dream."
    $ hero.fun += 1
    return

label sleep_nightmare:
    $ game.pass_time(randint(1,3),True)
    if hero.activity:
        $ hero.activity.set_flag("canceled",True)
    hero.say "WAAAH !"
    "What a horrible nightmare..."
    return

label set_alarm:
    python:
        result = renpy.display_menu([("Morning",1),("Afternoon",2),("No alarm",3)])
        if result in [1,2]:
            if result == 1:
                result = renpy.display_menu([("00:00",0),("01:00",1),("02:00",2),("03:00",3),("04:00",4),("05:00",5),("06:00",6),("07:00",7),("08:00",8),("09:00",9),("10:00",10),("11:00",11)])
            elif result == 2:
                result = renpy.display_menu([("12:00",12),("13:00",13),("14:00",14),("15:00",15),("16:00",16),("17:00",17),("18:00",18),("19:00",19),("20:00",20),("21:00",21),("22:00",22),("23:00",23)])
            game.set_flag("alarm_time",result)
            game.set_flag("alarm_clock")
        elif result == 3:
            game.set_flag("alarm_clock",False)
    return

label sleep:
    python:
        if not game.get_flag_value("female"):
            game.room = "bedroom1"
        else:
            game.room = "bedroom4"
        duration = 8
        if game.hour + duration > 23:
            wake_up = game.hour + duration - 24
        else:
            wake_up = game.hour + duration
        alarm = False
        if game.get_flag_value("alarm_clock"):
            alarm_time = game.get_flag_value("alarm_time")
            if wake_up > game.hour and wake_up > alarm_time:
                alarm = True
            elif wake_up < game.hour and (wake_up > alarm_time or game.hour < alarm_time):
                alarm = True
        if alarm:
            if game.hour > alarm_time:
                duration = 24 - game.hour + alarm_time
            else:
                duration =  alarm_time - game.hour
        if duration > hero.hunger()*2:
            duration = hero.hunger()*2
    if not duration > 0:
        "I am not tired."
        return
    scene bg black
    with dissolve
    python:
        energy_recovery = duration
        if duration >= 8:
            energy_recovery += 1
            hero.fun += 1
            if hero.check_skill("no_sleep"):
                duration -= 1
                energy_recovery += 1
            if "luxury bed" in hero.inventory.keys():
                duration -= 1
                energy_recovery += 1
        if duration < 1:
            duration = 1

        hero.energy += energy_recovery

        hero.hunger -= duration/2
        hero.grooming -= duration/3



        if duration >= 4:
            if "fitness machine" in hero.inventory.keys():
                if randint(1,3) == 3:
                    hero.fitness += 1
            if "knowledge machine" in hero.inventory.keys():
                if randint(1,3) == 3:
                    hero.knowledge += 1
            if "charm machine" in hero.inventory.keys():
                if randint(1,3) == 3:
                    hero.charm += 1
    $ game.pass_time(duration)
    pause 1.0
    scene expression "bg "+game.room
    with dissolve
    if alarm:
        $ renpy.sound.play("sd/alarm_clock.mp3")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
