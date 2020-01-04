

init -1 python:
    Event(**{
        "name":"kleio_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "kleio",
        "girls_conditions": {"kleio":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"kleio_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "kleio",
        "girls_conditions": {"kleio":{"contact":"kleio","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(15,16),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"kleio_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "kleio",
        "priority":100,
        "girls_conditions": {"kleio":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"kleio_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "kleio",
        "priority":100,
        "girls_conditions": {"kleio":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"kleio_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "kleio",
        "priority":100,
        "girls_conditions": {"kleio":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_kleio_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"kleio_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "kleio",
        "priority":100,
        "girls_conditions": {"kleio":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"kleio_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "kleio",
        "girls_conditions": {"kleio":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_kleio_hint:
    $ story = kleio.get_flag_value("story")
    if not kleio_love == kleio_love_max:
        "I should get to know Kleio better."
    elif story == 1 or story == 2 or ("kleio_event_02" in DONE and "kleio_event_03" not in DONE):
        "I think she will call me when she wants to hang out"
    elif story == 3 and "guitar" in hero.skills:
        "I should try to see her at the studio."
    else:
        "I reached the end of Kleio's story for now."
    return

label kleio_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = kleio.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = kleio.get_activity(bye_hour)
    if not activity == kleio.activity:
        if day != game.week_day:
            $ kleio.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ kleio.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "kleio "+bye_outfit
        if activity["activity"] == "sleep":
            kleio.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            kleio.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            kleio.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            kleio.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            kleio.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            kleio.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            kleio.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            kleio.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            kleio.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            kleio.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            kleio.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            kleio.say "I ll go get dressed."
        hide expression "kleio "+bye_outfit
    return

label kleio_cheated:
    show kleio
    if (game.get_flag_value("bandharem") == 1 and game.active_girl.id in ["anna"]) or (game.get_flag_value("bandharem") == 2 and game.active_girl.id in ["anna", "sasha"]):
        kleio.say "I want some too!"
        show kleio kiss
        "And without warning Kleio kisses me."
        $ kleio.love += 1
    else:
        "I see Kleio looking at me kissing someone else angrily..."
        $ kleio.love -= 5
    hide kleio

    return

label kleio_greet:
    if not kleio.get_flag_value("greeted"):
        $ kleio.set_flag("greeted",True,1)
        show kleio
        $ result = randint (1,3)
        if result == 1:
            kleio.say "Hello, [hero.name]."
        elif result == 2:
            kleio.say "Hi, [hero.name]."
        elif result == 3:
            kleio.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                kleio.say "Good morning [hero.name]."
            elif game.hour < 19:
                kleio.say "Good afternoon [hero.name]."
            else:
                kleio.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Kleio."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                kleio.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Kleio."
            elif game.hour < 19:
                hero.say "Good afternoon Kleio."
            else:
                hero.say "Good evening Kleio."
    return

label kleio_kiss:
    scene expression "bg "+game.room
    if kleio.love() + hero.charm() < 80 and not kleio.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show kleio
        "Kleio quickly takes a step back, and turns away."
        if kleio.love < 40:
            kleio.say "Sorry but... I don't really feel comfortable with that."
            $ kleio.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                kleio.say "Sorry [hero.name], but let's just not."
                $ kleio.love -= 1
            else:
                kleio.say "I'm sorry, but I have to go..."
            "Before I can react, Kleio turns and rushes away."
        hide kleio
    elif kleio.love() + hero.charm() < 60 or (game.get_flag_value("datescore") >= 75 and not kleio.love() + hero.charm() < 60):
        hide kleio
        show expression "kleio kiss "+kleio.get_clothes()+" normal"
        if not kleio.get_flag_value("kiss"):
            "I watch Kleio's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "kleio kiss "+kleio.get_clothes()+" normal"
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kleio and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_58
            elif kleio.love >= 60:
                show kleio
                kleio.say "Um, I think we should talk about this later, alright?"
            else:
                show kleio
                kleio.say "Oh uh... I've got to go..."
                "Before I can object, Kleio begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ kleio.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Kleio, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "kleio kiss "+kleio.get_clothes()+" normal"
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kleio and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_59
        $ kleio.love += 1
    else:
        hide kleio
        show expression "kleio kiss "+kleio.get_clothes()+" normal"
        if not kleio.get_flag_value("kiss"):
            "I feel my lips passing over Kleio's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Kleio with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "kleio kiss "+kleio.get_clothes()+" normal"
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kleio and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_60
            elif kleio.love() >= 60:
                show kleio
                kleio.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show kleio
                kleio.say "Um... I should go..."
                "Before I can object, Kleio turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Kleio's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Kleio with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Kleio, close enough that our bodies are very nearly touching."
                "I bring one hand to Kleio's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Kleio's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "kleio kiss "+kleio.get_clothes()+" normal"
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kleio and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_61
            if hero.charm() >= 160 - kleio.love():
                show kleio
                kleio.say "Stop doing that."
        hide kleio
        $ kleio.love += 2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
