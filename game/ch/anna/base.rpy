init -1 python:
    Event(**{
        "name":"anna_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "anna",
        "girls_conditions": {"anna":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"anna_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "anna",
        "girls_conditions": {"anna":{"contact":"anna","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(11,12),"flag_dateinprogress":0,"chances":10},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"anna_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "anna",
        "priority":100,
        "girls_conditions": {"anna":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"anna_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "anna",
        "priority":100,
        "girls_conditions": {"anna":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"anna_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "anna",
        "priority":100,
        "girls_conditions": {"anna":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_anna_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"anna_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "anna",
        "priority":100,
        "girls_conditions": {"anna":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"anna_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "anna",
        "girls_conditions": {"anna":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50},
        "do_once": False,
        "once_day": True
        })


label smartphone_anna_hint:
    $ story = anna.get_flag_value("story")
    if not anna_love == anna_love_max:
        "I should get to know Anna better."
    elif story == 1:
        "I hope Anna will call me..."
    else:
        "I reached the end of Anna's story for now."
    return

label anna_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = anna.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = anna.get_activity(bye_hour)
    if not activity == anna.activity:
        if day != game.week_day:
            $ anna.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ anna.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "anna "+bye_outfit
        if activity["activity"] == "sleep":
            anna.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            anna.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            anna.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            anna.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            anna.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            anna.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            anna.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            anna.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            anna.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            anna.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            anna.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            anna.say "I ll go get dressed."
        hide expression "anna "+bye_outfit
    return

label anna_cheated:
    show anna
    if (game.get_flag_value("bandharem") == 1 and game.active_girl.id in ["kleio"]) or (game.get_flag_value("bandharem") == 2 and game.active_girl.id in ["kleio", "sasha"]):
        anna.say "Hey, That's unfair!"
        anna.say "I wanna have some fun too!"
        show anna kiss
        "And without warning Anna kisses me."
        $ anna.love += 1
    else:
        "I see Anna looking at me kissing someone else sadly, tears welling up in her eyes..."
        $ anna.love -= 5
    hide anna
    return

label anna_greet:
    if not anna.get_flag_value("greeted"):
        $ anna.set_flag("greeted",True,1)
        show anna
        $ result = randint (1,3)
        if result == 1:
            anna.say "Hello, [hero.name]."
        elif result == 2:
            anna.say "Hi, [hero.name]."
        elif result == 3:
            anna.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                anna.say "Good morning [hero.name]."
            elif game.hour < 19:
                anna.say "Good afternoon [hero.name]."
            else:
                anna.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Anna."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                anna.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Anna."
            elif game.hour < 19:
                hero.say "Good afternoon Anna."
            else:
                hero.say "Good evening Anna."
    return

label anna_kiss:
    scene expression "bg "+game.room
    if anna.love() + hero.charm() < 80 and not anna.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show anna
        "Anna quickly takes a step back, and turns away."
        if anna.love < 40:
            anna.say "Sorry but... I don't really feel comfortable with that."
            $ anna.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                anna.say "Sorry [hero.name], but let's just not."
                $ anna.love -= 1
            else:
                anna.say "I'm sorry, but I have to go..."
            "Before I can react, Anna turns and rushes away."
        hide anna
    elif anna.love() + hero.charm() < 60 or (game.get_flag_value("datescore") >= 75 and not anna.love() + hero.charm() < 60):
        hide anna
        show expression "anna kiss "+anna.get_clothes()
        if not anna.get_flag_value("kiss"):
            "I watch Anna's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "anna kiss "+anna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != anna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_82
            elif anna.love >= 60:
                show anna
                anna.say "Um, I think we should talk about this later, alright?"
            else:
                show anna
                anna.say "Oh uh... I've got to go..."
                "Before I can object, Anna begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ anna.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Anna, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "anna kiss "+anna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != anna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_83
        $ anna.love += 1
    else:
        hide anna
        show expression "anna kiss "+anna.get_clothes()
        if not anna.get_flag_value("kiss"):
            "I feel my lips passing over Anna's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling her with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "anna kiss "+anna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != anna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_84
            elif anna.love() >= 60:
                show anna
                anna.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show anna
                anna.say "Um... I should go..."
                "Before I can object, Anna turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Anna's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Anna with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Anna, close enough that our bodies are very nearly touching."
                "I bring one hand to Anna's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Anna's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "anna kiss "+anna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != anna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_85
        hide anna
        $ anna.love += 2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
