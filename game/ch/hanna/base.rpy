init -1 python:
    Event(**{
        "name":"hanna_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "hanna",
        "girls_conditions": {"hanna":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"hanna_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "hanna",
        "girls_conditions": {"hanna":{"contact":"hanna","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(14,15),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"hanna_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "hanna",
        "priority":100,
        "girls_conditions": {"hanna":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"hanna_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "hanna",
        "priority":100,
        "girls_conditions": {"hanna":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"hanna_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "hanna",
        "priority":100,
        "girls_conditions": {"hanna":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_hanna_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"hanna_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "hanna",
        "priority":100,
        "girls_conditions": {"hanna":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"hanna_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "hanna",
        "girls_conditions": {"hanna":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_hanna_hint:
    $ story = hanna.get_flag_value("story")
    if not hanna_love == hanna_love_max:
        "I should get to know Hanna better."
    elif story == 1:
        "I hope Hanna will call me..."
    else:
        "I reached the end of Hanna's story for now."
    return

label hanna_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = hanna.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = hanna.get_activity(bye_hour)
    if not activity == hanna.activity:
        if day != game.week_day:
            $ hanna.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ hanna.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "hanna "+bye_outfit
        if activity["activity"] == "sleep":
            hanna.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            hanna.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            hanna.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            hanna.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            hanna.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            hanna.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            hanna.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            hanna.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            hanna.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            hanna.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            hanna.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            hanna.say "I ll go get dressed."
        hide expression "hanna "+bye_outfit
    return

label hanna_cheated:
    show hanna
    "I see Hanna looking at me kissing someone else with envy and lust in her eyes."
    $ hanna.love += 1
    hide hanna
    return

label hanna_greet:
    if not hanna.get_flag_value("greeted"):
        $ hanna.set_flag("greeted",True,1)
        show hanna
        $ result = randint (1,3)
        if result == 1:
            hanna.say "Hello, [hero.name]."
        elif result == 2:
            hanna.say "Hi, [hero.name]."
        elif result == 3:
            hanna.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                hanna.say "Good morning [hero.name]."
            elif game.hour < 19:
                hanna.say "Good afternoon [hero.name]."
            else:
                hanna.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Hanna."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                hanna.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Hanna."
            elif game.hour < 19:
                hero.say "Good afternoon Hanna."
            else:
                hero.say "Good evening Hanna."
    return

label hanna_kiss:
    scene expression "bg "+game.room
    if hanna.love() + hero.charm() < 80 and not hanna.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show hanna
        "Hanna quickly takes a step back, and turns away."
        if hanna.love < 40:
            hanna.say "Sorry but... I don't really feel comfortable with that."
            $ hanna.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                hanna.say "Sorry [hero.name], but let's just not."
                $ hanna.love -= 1
            else:
                hanna.say "I'm sorry, but I have to go..."
            "Before I can react, Hanna turns and rushes away."
        hide hanna
    elif hanna.love() + hero.charm() < 60 or (game.get_flag_value("datescore") >= 75 and not hanna.love() + hero.charm() < 60):
        hide hanna
        show expression "hanna kiss "+hanna.get_clothes()
        if not hanna.get_flag_value("kiss"):
            "I watch Hanna's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "hanna kiss "+hanna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != hanna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_72
            elif hanna.love >= 60:
                show hanna
                hanna.say "Um, I think we should talk about this later, alright?"
            else:
                show hanna
                hanna.say "Oh uh... I've got to go..."
                "Before I can object, Hanna begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ hanna.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Hanna, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "hanna kiss "+hanna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != hanna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_73
        $ hanna.love += 1
    else:
        hide hanna
        show expression "hanna kiss "+hanna.get_clothes()
        if not hanna.get_flag_value("kiss"):
            "I feel my lips passing over Hanna's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling her with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "hanna kiss "+hanna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != hanna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_74
            elif hanna.love() >= 60:
                show hanna
                hanna.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show hanna
                hanna.say "Um... I should go..."
                "Before I can object, Hanna turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Hanna's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Hanna with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Hanna, close enough that our bodies are very nearly touching."
                "I bring one hand to Hanna's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Hanna's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "hanna kiss "+hanna.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != hanna and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_75
        hide hanna
        $ hanna.love += 2
    return

label hanna_fuck_date:
    scene bg bedroom1
    show hanna
    "We make it through the bedroom door, barely, before my hands find my way to her waist, pulling her, gently, in to me."
    "I’ve been dying to get my hands on her."
    "I run my palms down the curve of her waist, down to her hips, and Hanna gives a soft, coy giggle, and gently presses the door closed behind me with her fingertips."
    "Her body feels as nice as I’d imagine it would."
    "I feel her everywhere -- over her tight abs, the toned muscles of her back, her plump, firm ass, and finally, up to her soft, heavy tits."
    hide hanna
    show expression "hanna kiss "+hanna.get_clothes()
    "Our lips find each other’s, as if she can’t get enough of me feeling every inch of her hard work just as much as I can’t get enough of feeling the animalistic perfection of her."
    "Her fingertips press into my back, pulling me closer, and I allow her breasts to press against me as I relent and grip instead at her asscheeks, giving them an appreciative, squeezing massage as our tongues wrestle for dominance."
    "Somewhere in the midst of this heated, eager dance between our mouths and our hands, I manage to move her over to my bed, sometimes nearly lifting her by her ample rump as I dig my fingers into the flesh."
    "There’s just something about feeling the body of a woman who worked for it, who’s really committed herself to taking care of it."
    "It’s like exploring the taste of something made by a master chef; something not just anyone has the skill or discipline to create."
    "I need to taste it."
    "I need to have her, now."
    "She’s earned this body, and I’ve earned her."
    "I move her to the bed, and lean myself forward over her as it presses against the back of her knees, making them buckle and allowing me to fall on top of her, propping myself up by my knee just beside her hip."
    "Our kiss breaks apart, and she stares up at me, soft, heated panting escaping her lips. Her eyes fix on mine with adoration and lust, and I know she wants this as badly as I do."
    hide expression "hanna kiss "+hanna.get_clothes()
    show hanna blush
    "She still seems a little bit shy, almost, when I slide my hands back up her stomach and under her shirt, dipping my fingertip beneath the band of her sports bra and hungrily cupping the soft, full weight of her breast."
    "But if she has any reservations about this at all, she forgets them immediately as I brush the pad of my thumb over her nipple, eliciting a soft, mewling moan and a shudder out of her."
    "She arches her body to allow me to slide off her shirt and bra in one fluid motion, leaving her bare upper body behind there on my blankets like a greek sculpture."
    show hanna underwear blush
    "A finger makes its way up to her lips, and she closes her teeth gently over the tip of a fingernail, watching me with a slight, demure blush on her cheeks."
    "I don’t know what she has to be shy about."
    show hanna naked blush
    "She looks amazing. I feel an aching, hungry throb against my genes, and get back to work, tossing her shirt and bra aside and quickly removing the remainder of her clothing, ravenous to see her fully exposed for me."
    "It takes no time at all for me to follow suit, and within the minute I’m standing there before her, rock hard, watching her squirm timidly a little bit in my sheets as I take the sight of her in."
    hero.say "You want this?"
    "The blush on her cheeks is still present, but she nods, and allows her tongue to slip from between her teeth, licking sexily along the finger whose nail she’d been nervously clasping between them."
    "My cock gives another eager throb in return."
    hero.say "Good. Because so do I."
    $ CONDOM = ""
    if hanna.get_flag_value("pregnant") < 9:
        if hanna.get_flag_value("drinks")<3:
            if hanna.love < 180 and hero.has_condom():
                hanna.say "Let's use protection."
                "I'm too caught up in the moment to object, scambling for a condom from the bedside table."
                $ hero.use_condom()
                $ CONDOM = " condom"
            elif hanna.love < 180:
                hanna.say "Let's use protection."
                "I fumble for a condom from the bedside table, but there's none to be found."
                hero.say "Shit...I ran out!"
                hanna.say "Sorry, another time then..."
                hide hanna
                return
        elif not CONDOM and hero.has_condom():
            menu:
                "Use a condom":
                    "One last thing."
                    "I take a step back to where I’ve discarded my jeans and take the condom out of my pocket, slipping it on."
                    $ hero.use_condom()
                    $ CONDOM = " condom"
                "Do it raw":
                    "I step forward to the bed, like a werewolf stepping up over a sheep, ready to devour her whole."
                    if hanna.love < 180:
                        hanna.say "Wait…"
                        "She looks ready and willing, but then seems to realize something, and draws a sharp, almost inaudible gasp, dropping the hand at her mouth suddenly to cover the lips between her legs."
                        "Damn."
                        "Knowing exactly what that single word, and her nervously, cutely knit brows meant, I step back over to where I’ve discarded my jeans and pull a condom out of my pocket, slipping it on."
                        $ hero.use_condom()
                        $ CONDOM = " condom"
                    else:
                        "She looks ready and willing, but then seems to realize something, and draws a sharp, almost inaudible gasp."
                        "Blushing madly she end up smiling at me and signing me to come closer."
    $ hanna.set_flag("sex",1,"permanent",mod="+")
    "I crawl myself back up and over her, where I had been when we’d been kissing here moments before."
    "She seems to hesitate, again, though I know by the look deep in her eyes that she wants it, and I expect fully to take control of this from beginning to end, which is fine by me."
    "But she stops me, just as I’m about to dip down and slip it in, pressing one of her hands to the center of my chest."
    hanna.say "Actually…"
    "What now?"
    "She lowers her lashes a moment, meekly, turns her face slightly, then looks back up and locks her eyes on mine with a new confidence."
    hanna.say "I want to be on top."
    "Oh."
    "I’m absolutely not about to protest."
    "I shift myself off of her and lay down on the bed while she gets up onto her knees, laying myself back onto my pillow and making myself comfortable."
    "I’m still standing at full attention for her."
    "She reaches forward and takes my cock in her gentle grip for a moment, and it gives another twitch in response."
    "There’s a spark in her eye, suddenly, and she crawls up and over me, holding my erection steady beneath her as she positions herself over me, and carefully, tantalizingly, lowers herself down."
    show hanna cowgirl up
    "I let a low moan roll over in my chest as she takes me in, steadily, like a champ."
    "She’s hot and tight there, too, just like the rest of her body."
    "It seems to squeeze me in and massage me as she takes me to the hilt, and I let my eyes roll closed for a moment and tilt my head back into the pillows."
    show hanna cowgirl down
    "She starts to move, cautiously at first, milking every inch of my cock in her tight, silken grip."
    "It’s bliss. I reopen my eyes to watch her, admiring every motion of her toned body."
    "The look on her face is nothing short of determined, now, almost animalistic. Her breaths are coming heavy already, and I know it’s not from fatigue."
    "There’s a hot red flush to her face as she works, leaning her body back and allowing me to see its full glory, rolling and tight like an animal as she grinds my cock in and out of her slick folds."
    "At first the motions are controlled, but then her hips start bucking, and her heavy breathing devolves into needy, desperate moans."
    show hanna cowgirl bounce
    "I feel like I could bust already, just watching her, the muscles rippling as she moves, the growing need and frantic lust that’s painting itself across her face as I fill her to the hilt with every grinding motion."
    show hanna cowgirl normal speed
    "After a few minutes of this she seems to not be able to take it anymore, and leans herself forward, gripping me for leverage as she shifts her feet back beneath her and starts to bounce violently onto my shaft, her moans getting heavier and deeper as she drops the weight of her body onto it."
    show hanna cowgirl bounce speed pleasure
    "She seems to have changed completely from the shy, blushing girl from minutes ago."
    "Her motions get more and more aggressive, until she’s slamming her soft pussy lips down onto me as hard as she can, her tits bouncing beautifully, like she just can’t get enough."
    "I decide to help her with that."
    show hanna cowgirl bounce speed pleasure sweat
    "Bracing myself by grabbing onto her, I thrust up to meet her, and her moans become near-screams."
    "She doesn’t speak."
    "She doesn’t seem to remember how to, fully focused on this, absorbed in the pleasure, losing her mind while we slam against each other, just the wet, smacking sound of two hardened bodies meeting with an animal drive."
    "She starts to squeeze, rhythmically, around me, and I know she’s just about done."
    "I speed up my thrusts into her, and her eyes roll back into her head as she starts to quiver on top of me, what seems like the only word she still remembers escaping her lips in a whimpering moan."
    show hanna cowgirl bounce speed ahegao
    hanna.say "Mmmmmh..."
    "A gutteral, almost growling moan escapes her as she digs her fingers into me, deep, spasming around me as I thrust into her like a jackhammer, pumping until I find my own release deep in her quivering walls."
    show hanna cowgirl bounce speed ahegao cum
    "I’m spent, almost as soon as my balls are."
    hide hanna
    "It takes me a few minutes to even regain my senses and realize that I’ve closed my eyes, just trying to catch my breath."
    "Hanna has collapsed beside me, at some point, her own chest and beautiful breasts still heaving from the encounter."
    "She breaths a musical, satisfied sigh, and rolls herself over, curling up against my side."
    "Her arm across my ribs and hand resting just above my collarbone are warm and soothing in our post-intimacy bliss, and I let my eyes fall back closed, shifting an arm around her to pull her in closer."
    "The both of us are asleep before we can even consider cleaning up."
    if not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills) and not hanna.get_flag_value("pregnant") and not hanna.get_flag_value("pill"):
        $ hanna.set_flag("pregnant",1)
    call sleep from _call_sleep_2
    $ game.room = "bedroom1"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
