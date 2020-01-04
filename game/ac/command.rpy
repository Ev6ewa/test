init -15 python:
    Activity(**{
        "name": "command",
        "display_name": "Command",
        "label": ["command_girl"],
        "duration": 0,
        "game_conditions": {"activity":"interact"},
        "girls_conditions": {
            "ACTIVE":{
                "min_sub":50,
                "not_activity":["sleep"],
                }
            },
        "once_day": "ACTIVE_GIRL",
        "icon":"command",
        })

label command_girl:
    call expression game.active_girl.id+"_greet" from _call_expression_70
    if renpy.has_label(game.active_girl.id+"_command"):
        call expression game.active_girl.id+"_command" from _call_expression_71
    else:
        show expression game.active_girl.id
        menu:
            "Give me some money":
                $ hero.money += 25
                $ game.active_girl.love -= 2
            "You should start taking the pill" if not game.active_girl.get_flag_value("pill") and (game.active_girl.sub >= 50 or game.active_girl.love >= 100) and game.active_girl.get_flag_value("sex"):
                $ game.active_girl.set_flag("pill",True)
            "You should stop taking the pill" if game.active_girl.get_flag_value("pill") and (game.active_girl.sub >= 50 or game.active_girl.love >= 150) and game.active_girl.get_flag_value("sex"):
                $ game.active_girl.set_flag("pill",False)
            "You should shave your pussy" if game.active_girl.get_flag_value("pubes",game.active_girl.pubes) and game.active_girl.sub >= 75:
                $ game.active_girl.set_flag("pubes",False)
            "You should stop shaving your pussy" if not game.active_girl.get_flag_value("pubes",game.active_girl.pubes) and game.active_girl.sub >= 75:
                $ game.active_girl.set_flag("pubes",True)
            "Clean this room" if game.room == "secondfloor" and not "clean_the_secondfloor" in DONE_WEEK and game.active_girl.sub >= 25:
                $ game.set_flag("chores",25,"week","+")
                if not "clean_the_secondfloor" in DONE_WEEK:
                    $ DONE_WEEK.append("clean_the_secondfloor")
                if game.active_girl.sub <= 50:
                    $ game.active_girl.love -= 1
                    $ game.active_girl.sub += 1
            "Clean this room" if game.room == "livingroom" and not "clean_the_livingroom" in DONE_WEEK and game.active_girl.sub >= 25:
                $ game.set_flag("chores",25,"week","+")
                if not "clean_the_livingroom" in DONE_WEEK:
                    $ DONE_WEEK.append("clean_the_livingroom")
                if game.active_girl.sub <= 50:
                    $ game.active_girl.love -= 1
                    $ game.active_girl.sub += 1
            "Clean this room" if game.room == "bathroom" and not "clean_the_bathroom" in DONE_WEEK and game.active_girl.sub >= 25:
                $ game.set_flag("chores",25,"week","+")
                if not "clean_the_bathroom" in DONE_WEEK:
                    $ DONE_WEEK.append("clean_the_bathroom")
                if game.active_girl.sub <= 50:
                    $ game.active_girl.love -= 1
                    $ game.active_girl.sub += 1
            "Clean the pool" if game.room == "pool" and not "clean_the_pool" in DONE_WEEK and game.active_girl.sub >= 25:
                $ game.set_flag("chores",25,"week","+")
                if not "clean_the_pool" in DONE_WEEK:
                    $ DONE_WEEK.append("clean_the_pool")
                if game.active_girl.sub <= 50:
                    $ game.active_girl.love -= 1
                    $ game.active_girl.sub += 1
            "Do the dishes" if game.room == "kitchen" and not "do_the_dishes" in DONE_DAY and game.active_girl.sub >= 25:
                $ game.set_flag("chores",5,"week","+")
                if not "do_the_dishes" in DONE_DAY:
                    $ DONE_WEEK.append("clean_the_pool")
            "Cancel":
                $ hero.activity.set_flag("canceled",True)
        $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
