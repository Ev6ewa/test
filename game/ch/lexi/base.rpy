layeredimage bg trailer:
    if game.hour >= 20 or game.hour <= 5:
        "trailer_night"
    else:
        "trailer_day"

init -1 python:
    Event(**{
        "name":"lexi_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "lexi",
        "girls_conditions": {"lexi":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lexi_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "lexi",
        "girls_conditions": {"lexi":{"contact":"lexi","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(16,17),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lexi_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "lexi",
        "priority":100,
        "girls_conditions": {"lexi":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lexi_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "lexi",
        "priority":100,
        "girls_conditions": {"lexi":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"lexi_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "lexi",
        "priority":100,
        "girls_conditions": {"lexi":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_lexi_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lexi_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "lexi",
        "priority":100,
        "girls_conditions": {"lexi":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"lexi_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "lexi",
        "girls_conditions": {"lexi":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

label lexi_spank_activity:
    "I spank lexi on her sweet slutty ass."
    show expression lexi.id+" blush"
    if lexi.sub < 25:
        $ lexi.sub += 1
    "She smiles and blush..."
    return


label smartphone_lexi_hint:
    $ story = lexi.get_flag_value("story")
    if not lexi_love == lexi_love_max:
        "I should get to know Lexi better."
    elif story == 1 or story == 2:
        "I think she will call me when she wants to hang out"
    else:


        "I reached the end of Lexi's story for now."
    return

label lexi_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = lexi.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = lexi.get_activity(bye_hour)
    if not activity == lexi.activity:
        if day != game.week_day:
            $ lexi.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ lexi.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "lexi "+bye_outfit
        if activity["activity"] == "sleep":
            lexi.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            lexi.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            lexi.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            lexi.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            lexi.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            lexi.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            lexi.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            lexi.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            lexi.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            lexi.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            lexi.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            lexi.say "I ll go get dressed."
        hide expression "lexi "+bye_outfit
    return

label lexi_cheated:
    show lexi
    "I see Lexi looking at me kissing someone else with envy and lust in her eyes."
    $ lexi.love += 1
    hide lexi
    return

label lexi_greet:
    if not lexi.get_flag_value("greeted"):
        $ lexi.set_flag("greeted",True,1)
        show lexi
        $ result = randint (1,3)
        if result == 1:
            lexi.say "Hello, [hero.name]."
        elif result == 2:
            lexi.say "Hi, [hero.name]."
        elif result == 3:
            lexi.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                lexi.say "Good morning [hero.name]."
            elif game.hour < 19:
                lexi.say "Good afternoon [hero.name]."
            else:
                lexi.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Lexi."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                lexi.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Lexi."
            elif game.hour < 19:
                hero.say "Good afternoon Lexi."
            else:
                hero.say "Good evening Lexi."
    return

label lexi_kiss:
    scene expression "bg "+game.room
    if lexi.love() + hero.charm() < 80 and not lexi.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show lexi
        "Lexi quickly takes a step back, and turns away."
        if lexi.love < 40:
            lexi.say "Sorry but... I don't really feel comfortable with that."
            $ lexi.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                lexi.say "Sorry [hero.name], but let's just not."
                $ lexi.love -= 1
            else:
                lexi.say "I'm sorry, but I have to go..."
            "Before I can react, Lexi turns and rushes away."
        hide lexi
    elif lexi.love() + hero.charm() < 60 or (game.get_flag_value("datescore") >= 75 and not lexi.love() + hero.charm() < 60):
        hide lexi
        show expression "lexi kiss "+lexi.get_clothes()
        if not lexi.get_flag_value("kiss"):
            "I watch Lexi's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "lexi kiss "+lexi.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != lexi and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_66
            elif lexi.love >= 60:
                show lexi
                lexi.say "Um, I think we should talk about this later, alright?"
            else:
                show lexi
                lexi.say "Oh uh... I've got to go..."
                "Before I can object, Lexi begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ lexi.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Lexi, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "lexi kiss "+lexi.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != lexi and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_67
        $ lexi.love += 1
    else:
        hide lexi
        show expression "lexi kiss "+lexi.get_clothes()
        if not lexi.get_flag_value("kiss"):
            "I feel my lips passing over Lexi's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Lexi with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "lexi kiss "+lexi.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != lexi and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_68
            elif lexi.love() >= 60:
                show lexi
                lexi.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show lexi
                lexi.say "Um... I should go..."
                "Before I can object, Lexi turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Lexi's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Lexi with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Lexi, close enough that our bodies are very nearly touching."
                "I bring one hand to Lexi's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Lexi's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "lexi kiss "+lexi.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != lexi and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_69
            if hero.charm() >= 160 - lexi.love():
                show lexi
                lexi.say "Stop doing that."
        hide lexi
        $ lexi.love += 2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
