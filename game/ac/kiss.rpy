init -15 python:
    Activity(**{
        "name": "kiss",
        "display_name": "Kiss",
        "label": ["kiss_her"],
        "duration": 0,
        "girls_conditions": {
            "ACTIVE":{
                "min_love":40,
                "not_activity":["sleep"]
                }
            },
        "icon": "kiss",
        "game_conditions": {"min_grooming":2,"activity":"interact"},
        "once_day": "ACTIVE_GIRL"
        })

    Activity(**{
        "name": "kiss_b",
        "icon": "kiss",
        "display_name": "Kiss",
        "label": ["kiss_her"],
        "duration": 0,
        "girls_conditions": {
            "ACTIVE":{
                "max_love":39,
                "not_activity":["sleep"]
                }
            },
        "game_conditions": {"min_grooming":2,"activity":"interact"},
        "once_day": "ACTIVE_GIRL"
        })

label kiss_her:
    $ game.active_girl.set_flag("greeting",True,1)
    $ game.active_girl.set_flag("interact",1,1,"+")
    if renpy.has_label(game.active_girl.id+"_kiss"):
        call expression game.active_girl.id+"_kiss" from _call_expression_32
    elif not hero.charm >= 120 - game.active_girl.love() and not game.active_girl.get_status() in ["girlfriend", "sex slave"] or game.active_girl.get_flag_value("nokiss") or not game.get_flag_value("datescore") >= 75:
        show expression game.active_girl.id
        hero.say "[game.active_girl.name] pushes me away."
        active_girl.say "Don't ever do that again..."
        $ game.active_girl.love -=2
        $ hero.activity.set_flag("canceled")
        hide expression game.active_girl.id
    elif game.active_girl.love() + hero.charm() < 140 or game.get_flag_value("datescore") >= 75:
        show expression game.active_girl.id+" "+game.active_girl.get_clothes()+" kiss"
        if not game.active_girl.get_flag_value("kiss"):
            hero.say "When our lips come into contact with each other, it send shivers down my back..."
            hero.say "The intoxicating smell of flowers and the taste of blueberry give a different vibe to that first kiss..."
            hero.say "As I look at her, I can see surprise and pleasure mixed together."
            $ game.active_girl.set_flag("kiss",1,"permanent","+")
        else:
            hero.say "[game.active_girl.name] kisses me softly."
            $ game.active_girl.set_flag("kiss",1,"permanent","+")
        $ game.active_girl.love +=1
        hide expression game.active_girl.id+" "+game.active_girl.get_clothes()+" kiss"
        call kiss_check_cheat from _kiss_her
    else:
        show expression game.active_girl.id+" "+game.active_girl.get_clothes()+" kiss"
        if not game.active_girl.get_flag_value("kiss"):
            hero.say "[game.active_girl.name] grip my neck and stick her wet tongue in my mouth."
            hero.say "After what feel like an eternity, we part, breathless..."
            active_girl.say "It seems that I waited for that kiss for far too long.\nI hope that there is more coming my way."
            hero.say "After that line she turns around and leave."
            $ game.active_girl.set_flag("kiss",1,"permanent","+")
        else:
            hero.say "[game.active_girl.name] kisses me passionately."
            $ game.active_girl.set_flag("kiss",1,"permanent","+")
        hide expression game.active_girl.id+" "+game.active_girl.get_clothes()+" kiss"
        $ game.active_girl.love +=2
        call kiss_check_cheat from _kiss_her_2
    return

label kiss_check_cheat:
    $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if g.get_status() in ["girlfriend", "sex slave"] and g != game.active_girl]
    if cheated_girls and renpy.has_label(cheated_girls[0].id+"_cheated"):
        call expression game.active_girl.id+"_cheated" from _call_expression_34
        return True
    return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
