init -1 python:
    Event(**{
        "name":"kylie_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "kylie",
        "girls_conditions": {"kylie":{"contact":"kylie","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(12,13),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"kylie_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "kylie",
        "priority":100,
        "girls_conditions": {"kylie":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"kylie_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "kylie",
        "priority":100,
        "girls_conditions": {"kylie":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"kylie_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "kylie",
        "priority":100,
        "girls_conditions": {"kylie":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_kylie_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"kylie_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "kylie",
        "priority":100,
        "girls_conditions": {"kylie":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"kylie_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "kylie",
        "girls_conditions": {"kylie":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_kylie_hint:
    "Kylie is too mysterious for hints."
    return

label kylie_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = kylie.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = kylie.get_activity(bye_hour)
    if not activity == kylie.activity:
        if day != game.week_day:
            $ kylie.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ kylie.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "kylie.say "+bye_outfit
        if activity["activity"] == "sleep":
            kylie.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            kylie.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            kylie.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            kylie.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            kylie.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            kylie.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            kylie.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            kylie.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            kylie.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            kylie.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            kylie.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            kylie.say "I ll go get dressed."
        hide expression "kylie.say "+bye_outfit
    return

label kylie_cheated:
    show kylie angry
    $ NOTIFICATIONS.append(["Kylie {image=ui/icon_yan_vsmall.png}+5",2])
    "I see Kylie looking at me kissing someone else with a strange, scary look in her eyes."
    $ kylie.set_flag("yandere",5,mod="+")
    hide kylie
    return

label kylie_greet:
    if not kylie.get_flag_value("greeted"):
        $ kylie.set_flag("greeted",True,1)
        show kylie
        $ result = randint (1,3)
        if result == 1:
            kylie.say "Hello, [hero.name]."
        elif result == 2:
            kylie.say "Hi, [hero.name]."
        elif result == 3:
            kylie.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                kylie.say "Good morning [hero.name]."
            elif game.hour < 19:
                kylie.say "Good afternoon [hero.name]."
            else:
                kylie.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Kylie."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                kylie.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Kylie."
            elif game.hour < 19:
                hero.say "Good afternoon Kylie."
            else:
                hero.say "Good evening Kylie."
    return

label kylie_kiss:
    scene expression "bg "+game.room
    if kylie.love() + hero.charm() < 30 and not kylie.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 50:
        show kylie
        "Kylie quickly takes a step back, and turns away."
        if kylie.love < 40:
            kylie.say "Sorry but... I don't really feel comfortable with that."
            $ kylie.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                kylie.say "Sorry [hero.name], but let's just not."
                $ kylie.love -= 1
            else:
                kylie.say "I'm sorry, but I have to go..."
            "Before I can react, Kylie turns and rushes away."
        hide kylie
    elif kylie.love() + hero.charm() < 50  or (game.get_flag_value("datescore") >= 75 and not kylie.love() + hero.charm() < 50):
        hide kylie
        show expression "kylie kiss "+kylie.get_clothes()
        if not kylie.get_flag_value("kiss"):
            "I watch Kylie's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "kylie kiss "+kylie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kylie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_113
            elif kylie.love >= 60:
                show kylie
                kylie.say "Um, I think we should talk about this later, alright?"
            else:
                show kylie
                kylie.say "Oh uh... I've got to go..."
                "Before I can object, Kylie begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ kylie.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Kylie, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "kylie kiss "+kylie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kylie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_114
        $ kylie.love += 1
    else:
        hide kylie
        show expression "kylie kiss "+kylie.get_clothes()
        if not kylie.get_flag_value("kiss"):
            "I feel my lips passing over Kylie's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Kylie with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "kylie kiss "+kylie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kylie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_115
            elif kylie.love() >= 60:
                show kylie
                kylie.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show kylie
                kylie.say "Um... I should go..."
                "Before I can object, Kylie turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Kylie's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Kylie with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Kylie, close enough that our bodies are very nearly touching."
                "I bring one hand to Kylie's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Kylie's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "kylie kiss "+kylie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != kylie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_116
            if hero.charm() >= 160 - kylie.love():
                show kylie
                kylie.say "Stop doing that."
        hide kylie
        $ kylie.love += 2
    return

label kylie_fuck_date:
    scene bg livingroom
    "Even as I open the front door and usher Kylie into the hallway, I'm still not sure that I'm doing the right thing by inviting her back to my place."
    "Don't get me wrong, I'm no prude and it's not like she's twisted my arm to get herself invited over the threshold for some post-date action."
    "But there's always that feeling of her being somehow a little different to most of the girls that I tend to meet and get to take out on dates."
    "It's hard for me to put my finger on the precise word for it, and maybe I'm guilty of overthinking the whole thing."
    "I just keep remembering that she's still Alexis's little sister."
    "Not to mention the crazy stories that she's told me about being into me since she was pretty much a young girl."
    "And when I say crazy, I obviously mean amazing, not insane!"
    scene bg secondfloor
    "Standing in the middle of the hallway, Kylie seems to be taking her time to have a good look around the place."
    show kylie
    kylie.say "So this is it - the house of [hero.name]!"
    "Not prepared in the least for such a strange comment, I try to shrug it off before I become too embarrassed."
    hero.say "Ah...there's no need to talk about it like you're on a tour of the Vatican or something!"
    hero.say "It's just your average rental in the suburbs - nothing to write home about..."
    "At this, Kylie spins on her heel and treats me to one of those odd, beguiling smiles that she's capable of pulling off."
    "The kind of smile that I can never tell whether she's being genuine and innocent, or condescending towards me."
    kylie.say "But it's not just any house, [hero.name] - it's YOUR house."
    kylie.say "You don't know how often I imagined the place where you'd live..."
    hero.say "Yeah, well...I don't live here alone."
    hero.say "I'm pretty sure my housemates are out for most of the night."
    hero.say "But maybe we should be quiet all the same, just in case I'm wrong?"
    "At the mention of my housemates, Kylie's expression darkens a shade, and her mouth curls into something approaching a frown."
    kylie.say "Oh yeah - Flea and Rasher, right?"
    hero.say "Bree and Sasha, actually..."
    "Sensing that we're in danger of drifting away from the matter at hand, I clear my throat, perhaps a little too loudly."
    hero.say "Ahem, anyway...I don't think that we've got time for the grand tour right now."
    hero.say "So I was thinking that maybe you'd settle for an extended visit to my room instead?"
    "I turn my head towards the stairs, looking upwards and then back at Kylie so as to leave no room for confusion."
    "The effect is almost instantaneous, like a switch just flipped inside of her head."
    "All trace of her distaste at the mention of Bree and Sasha seems to vanish."
    "And she becomes suddenly bashful in a manner that makes me want her more than ever."
    kylie.say "Oh, [hero.name] - you lure me back to your lair, and then you make me an offer that you know I just can't refuse!"
    if not kylie.get_flag_value("sex"):
        kylie.say "This is literally a dream come true!"
        kylie.say "Drinks, a meal and now you're finally going to make a woman out of me - I'm so excited!"
        "Her hand is in mine and I'm leading her up the stairs before something that she just said truly registers in my mind."
        hero.say "Kylie...when you say 'make a woman out of me' - what do you mean, exactly?"
        "Kylie looks a little surprised at this question."
        "Her eyes are telling me that she assumes I should already know the answer."
        kylie.say "Well...I...I saved myself for you, [hero.name]."
        kylie.say "I always knew that you were the only guy for me."
        kylie.say "So I could never have slept with someone else..."
        "Oh shit - I'm sneaking a virgin with a complex about me up to my room with the intention of deflowering her!"
        "I hide my trepidation about what Kylie's just told me behind what I hope is a confident smile."
        "After all, there's nothing illegal about taking the virginity of a girl who's legal."
        "And besides, she's practically begging me to do the act as well."
        "I have to get all of this stuff about her holding a candle for me under control in my own mind."
        "If I don't, then I'm going to blow it with her, big time!"
        hero.say "I'm glad you told me that, Kylie."
        hero.say "It's...pretty romantic of you!"
        "I seem to have managed to say just the right thing, as Kylie beams at me and allows herself to be led straight to my bedroom door."
        "Looking at that face and the body that goes with it, knowing that she's saved herself just for me - it's all I can do to open the door and show her inside."
    scene bg bedroom1
    "It's right about now that I remember what a state I left my room in before I rushed out to meet Kylie earlier."
    "There are clothes strewn across the floor and books piled on the desk from when I was last studying up here."
    "Instead of turning on the ceiling light, I dart over and flick the switch for he lamps at the side of my bed."
    "I figure that I can explain this away as mood lighting, and hope that it'll obscure, or at least soften the view of my mess."
    show kylie
    "Luckily for me though, it seems that Kylie's too caught up in the moment to either notice or care what state my room's in."
    "She smiles as I turn my back for a moment, trying to at least make the bed for her benefit."
    show kylie underwear
    "But when I turn back to face her, I see that she's already unbuttoned her shirt and is sliding in off of her shoulders."
    if not kylie.get_flag_value("sex"):
        "I slump down onto the bed, eyes wide as I see her almost naked to the waist for the first time."
    "And if I hadn't fallen down, she could have tapped me and sent me reeling backwards."
    "Hell - she could have blown me down!"
    "Kylie smiles, clearly delighted with the effect her beginning to strip off has had on me."
    "Next, she pulls down the straps of her bra, reaching back to unhook it and free her breasts."
    "They stand proud of her chest, large and inviting, and all I can think of doing is burying my head deep between them."
    "Kylie lets her skirt and panties drop next, stepping out of them neatly while rolling down her stockings."
    show kylie naked
    "And this is the girl that insists I'm the man of HER dreams?!?"
    "Right now I'd be hard pressed to dream up anything more desirable than what I can see before me!"
    if not kylie.get_flag_value("sex"):
        kylie.say "I guess this is the point where I'm supposed to ask you be gentle with me."
        kylie.say "But I'd really rather you weren't..."
    else:
        kylie.say "Please don't be gentle..."
    "Before I can even manage a response to that, she walks over and starts to pull of my own clothes."
    "I struggle to catch up, and between us I'm as naked as she is within what must be less than a minute."
    "And then she's just standing there before me, waiting for me to make the next move."
    $ CONDOM = False
    menu:
        "Use protection" if hero.has_condom():
            "If I'm going to be the guy of her dreams and take her virginity as she's always dreamed, the least I can do is not knock her up in the act!"
            "I reach over and pluck one of the condoms off of the bedside table."
            if kylie.get_flag_value("yandere") < 50 or kylie.love < 180:
                "Kylie stops for a moment, watching as I roll the condom over my fast rising cock."
                "While she doesn't applaud me for taking the time to do so, she doesn't complain about it either."
            else:
                kylie.say "No - no protection!"
                "I look at her in askance, totally astounded by a girl refusing to let me use protection."
                if not kylie.get_flag_value("sex"):
                    kylie.say "That was never part of how this is supposed to happen, [hero.name]."
                    kylie.say "It has to be just how I imagined it!"
                    $ CONDOM = True
                menu:
                    "Insist":
                        hero.say "I don't care how you imagined it, Kylie."
                        hero.say "I'm not fucking you without it!"
                        kylie.say "Then I guess you're not fucking me at all!"
                        "With that, she begins to gather up her clothes and pull them on while making for the door."
                        return
                    "Accept":
                        "I'm not going to be denied now, not when I'm this close!"
                        "So I just shrug and toss the condom away."
                        "Which sees a wicked smile spreads across Kylie's face in response."
        "Don't use protection":
            "I know that I should be taking precautions, but I'm also getting swept along in Kylie's whole dream scenario at the same time."
            "I want this to be as perfect as possible, to live up to her expectations."
            "And so I reason that doing it without a condom would come closest to how she's imagined this whole thing playing out."
    "As soon as I reach out and place my hands on Kylie's curvy thighs, intent on pulling her down onto me, I realise I have no idea what position would be best."
    "I guess that I have a couple of seconds at most to make a decision, as Kylie beams down at me, waiting for my next move."
    menu:
        "Missionary" if (kylie.sub > 25 and kylie.sub < 75) or kylie.love >= 180:
            $ p = "M"
            hide kylie
            show kylie missionary out
            if not kylie.get_flag_value("sex"):
                "As this is her first time, I want to ease Kylie into it, and be able to do most of the work myself."
            "I gently pull her down onto the bed and don't stop until she's laid flat on her back."
            "Then I straddle her, pushing her thighs apart so that she's laid bare and vulnerable before me."
            "Kylie smiles up at me, her eyes full of anticipation and looking so innocent that it's almost distracting."
            "Maybe I should have thought of trying some kind of foreplay before getting to this point."
            "But from the way that the even the subdued light in the room is making Kylie's neat little pussy glisten, I don't think it'll be an issue."
            show kylie missionary pussy
            if CONDOM:
                show kylie missionary condom
            "Lowering myself onto her, I guide my cock between her legs with one hand while holding myself up with the other by her head."
            if not kylie.get_flag_value("sex"):
                "Kylie wraps her legs around me as I begin to push inside of her, only making it a short way before I feel the obstruction of her hymen."
                "Now here comes the tricky part."
                "I may have more experience in the bedroom than Kylie, but I confess this is the first time that I've had to deal with a hymen."
                "I know that I have to break through it, but my instinct is not to hurt Kylie too much if I can avoid it."
                kylie.say "Ah...shit..."
                "I glance up at her, worried that she's in too much pain as the head of my cock presses against the natural seal inside of her pussy."
                "But she bites her lip and nods vigorously, urging me to go on and ignore her cries of pain."
                show kylie missionary blood
                "So I push on, soon feeling the sensation of something tearing within Kylie's body."
            else:
                "Kylie wraps her legs around me as I begin to push inside of her"
                "But she bites her lip and nods vigorously, urging me to go on."
                "So I push on, soon feeling the sensation of something wet and silky pussy around my cock."
            show kylie missionary ahegao
            kylie.say "Oh god...oh...god..."
            kylie.say "[hero.name]...I can feel you..."
            kylie.say "You're inside of me...for real!"
            "Suddenly I feel kylie clamp her legs around me, pulling me closer to her."
            "My belly is pressed against her's, my chest against her large breasts."
            "And if that's what she wants, then I'm more than willing to oblige her."
            "I begin to thrust in and out of Kylie then, giving her all of my attention and energy."
            "Sure, I've fucked girls plenty of times in the past."
            if not kylie.get_flag_value("sex"):
                "But never while knowing for certain that I was the first guy to put his cock inside of them."
            else:
                "But never while knowing for certain that I was the only guy to ever put his cock inside of them."
            "That thought turns the act of fucking Kylie from an incredible lay into a truly memorable experience."
            if not kylie.get_flag_value("sex"):
                "And the fact that every move she makes and sound that comes out of her mouth is new only serves to make it more so."
            else:
                "And the fact that every move she makes and sound that comes out of her mouth is mine alone only serves to make it more so."
            "I'm actually making her dreams come true right now!"
            "And maybe it's that very thought that makes me realise that I'm about to cum myself..."
        "Cowgirl" if kylie.sub < 50 or kylie.love >= 180:
            $ p = "C"
            hide kylie
            show kylie cowgirl out
            if not kylie.get_flag_value("sex"):
                "It might be her first time, but that doesn't mean things have to be boring for Kylie or myself."
            "I take hold of Kylie's hands and guide her onto the bed, making her climb atop me as she comes."
            "Once she's straddling my thighs, I bring her to a halt, my erect cock mere inches from the lips of her pussy."
            "Kylie eyes it with what I can only describe as hunger, and she fingers herself down there in anticipation."
            "Any thought of her needing foreplay leaves my head when I see how slick and slippery this makes her fingertips."
            "I pull her forwards the last little bit of the way and have her raise herself up a little."
            show kylie cowgirl pussy
            if CONDOM:
                show kylie cowgirl condom
            "Just enough so that the head of my cock is pressing on her pussy."
            kylie.say "Ooh...fuck..."
            "I take a firmer hold of her hands, both to reassure her and keep her from pulling away."
            if not kylie.get_flag_value("sex"):
                hero.say "It'll only hurt a little to begin with, trust me."
                "Kylie nods, biting her lip against the pain as her own weight and gravity take over."
                "I feel the sensation of her hymen against the head of my cock, and then something gives way."
                show kylie cowgirl blood
            "And she literally sinks down onto me, casting her head back from the intensity of the experience."
            "Kylie doesn't stop until her groin meets mine, putting the palms of her hands on my belly, as though afraid of sinking further still."
            "I find myself looking up into her eyes, wide and full of emotion."
            show kylie cowgirl ahegao
            kylie.say "You're...you're inside of me, [hero.name]!"
            kylie.say "I can feel you...like...like you're a part of me..."
            kylie.say "Please...please fuck me!"
            "With my hands all over her, caressing every inch of her sweat-slick skin that I can reach, I'm more than happy to oblige."
            "Holding Kylie just below her breasts, I begin to thrust in and out of her, using the weight of her own body to add more force to each movement."
            "I can't believe that I'm actually making a girl's dreams come true by doing this!"
            "And it seems totally crazy that each sigh and moan that Kylie lets out is a sign that she's getting what she's always desired."
            "I always thought that granting someone's fondest wish would be much harder work and far less pleasant of an experience."
            if not kylie.get_flag_value("sex"):
                "I just hope that her first time riding a cock is as memorable as she always hoped it would be."
            "But now, with her blonde locks flying and her breasts bouncing, Kylie's about to make me cum..."
        "Doggy" if kylie.sub >= 50 or kylie.love >= 180:
            show kylie doggy out
            $ p = "D"
            if not kylie.get_flag_value("sex"):
                "This migth well be Kylie's first time, but there's still a pecking order in our relationship that I'm keen to maintain."
                "With this in mind, I take her hands and get up from the bed myself, guiding her onto it in my place."
            else:
                "I take her hands and get up from the bed myself, guiding her onto it in my place."
            "She obligingly crawls onto it, but when she makes to lie down on her back, I take a firmer hold to keep her on her hands and knees."
            "Rather than being alarmed or annoyed by the fact that I'm asserting myself over her, Kylie merely looks back over her shoulder and smiles."
            "Which I choose to interpret as a silent acceptance of the position in which I've put her and the fact that I'm the one in control here."
            "With her spread and the way this in turn parts her buttocks, it's easy to see that Kylie's not putting on a brave face right now."
            "The lips of her pussy are already wet and glistening in the subdued light of the room."
            "I climb onto the bed behind her, letting my cock lead the way and enjoying her reaction when it brushes against her thighs and then goes further still."
            "Putting both hands on her buttocks, I take the time to let the head slide up and down the slick folds, teasing Kylie with every single movement."
            "I can hear her beginning to whimper in anticipation, her body almost shivering at the prospect of what's to come next."
            "But she's a good, obedient girl that knows her place, and she never once opens her mouth to question or demand of me."
            show kylie doggy pussy
            if CONDOM:
                show kylie doggy pussy condom
            "When I suddenly dig my fingers into her buttocks and thrust myself into her, those whimpers become actual cries and almost screams."
            if not kylie.get_flag_value("sex"):
                show kylie doggy blood
                "I feel the resistance of her hymen for no more than mere seconds before it tears away and my cock sinks deeply into her."
            "Kylie's cries become long, almost agonised moans as I allow her no chance to recover."
            if not kylie.get_flag_value("sex"):
                "Instead I fuck her with a vigour that comes from knowing that this is her first time."
                "A vigour that also knows what kind of a lasting impression being taken so hard and fast will leave upon her."
            show kylie doggy ahegao
            "Kylie has handfuls of the bedclothes clutched in her hands and her head pushed down into them, drooling into the sheets."
            "When I manage to catch a glimpse of them, her eyes seem to be almost glazed over from the pleasure of being fucked so hard and so fast."
            "I can see her large breasts swaying beneath her and the ripples along her curvaceous thighs as I continue to pound her without mercy."
            "A small part of me can't help worrying that this moment is something that Kylie always told me she'd dreamed about."
            "And I wonder if she saw herself in a position like this when she did so."
            "But then I remember that she's a big girl now, and there's nothing at all to keep her from crying out for me to stop."
            "So while ever she's consenting to all of this by way of her silence, there's nothing at all to keep me from enjoying myself."
            "It's then that I manage to catch Kylie's eye, as a glimmer of awareness returns to it for what may only be a brief moment."
            "She looks at me not with anger or fear, but rather with an acceptance of what I'm doing to her that says she'll take all I have to give and more."
            "Knowing that I have her complete submission, I feel a wash of emotion that pushes me over the edge..."





























    "My muscles stiffen and I thrust my cock as deeply into Kylie's pussy as I can manage."
    "She groans in anticipation, knowing that she's about to make me cum."
    menu:
        "Cum inside" if CONDOM:
            hide kylie
            "The effects of me going off are enough to make Kylie cum a few moments later, adding a new dimension to her cries."
            "But even though I've supposedly made her dreams come true by making love to her just now, I can see that there's a hint of dissatisfaction in her eyes."
            "I can't understand what could be upsetting her, and I don't want to ruin the moment by prying, so I simply try to forget it."
        "Pull out" if not CONDOM:
            "I manage to pull my cock out of Kylie no more than a second before I shower her with cum."
            if p == "C":
                show kylie cowgirl out cum
            elif p == "D":
                show kylie doggy out cum
            elif p == "M":
                show kylie missionary out cum
            "She yelps in surprise, both at the sensation and the spattering she gets straight afterwards."
            "But from the way she tried to cling to me and the look of melancholy in her eyes, I can't help thinking she was disappointed that I didn't cum inside of her just now."
        "Cum inside" if not CONDOM:
            if not kylie.get_flag_value("sex"):
                "I didn't wear protection because I wanted the experience to be as natural as possible for Kylie her first time."
            if p == "C":
                show kylie cowgirl pussy cum
            elif p == "D":
                show kylie doggy pussy cum
            elif p == "M":
                show kylie missionary pussy cum
            if (randint(1,3) == 1 or "hung" in hero.skills) and not kylie.get_flag_value("pregnant") and not kylie.get_flag_value("pill"):
                $ kylie.set_flag("pregnant",1)
            "I push in as deep as possible and feel myself cum mere moments later."
            "The look on Kylie's face as she realises what I've done is simply ecstatic, beaming at the sensation filling her insides as she rides me to the very last."
    hide kylie
    show kylie naked blush
    "Later, as she begins to idly dress herself from the piles of clothes scattered around the room, Kylie looks at me and smiles."
    kylie.say "I feel like the princess in a fairy tale right now!"
    hero.say "Really?"
    hero.say "I guess I should take that as a compliment!"
    "I fall silent for a moment, trying to think of the best way to say what's on my mind."
    hero.say "You were amazing too, Kylie."
    if not kylie.get_flag_value("sex"):
        hero.say "I feel...well, I feel pretty honoured to have been your first..."
        "At this, Kylie smiles sweetly and waves away my comments as if they're nothing at all."
        kylie.say "Oh, that's okay - you were always destined to be the one anyway."
        kylie.say "I just never imagined it'd be so much fun!"
        "I nod and offer her a weak smile in return."
        "Honestly, I had been hoping that our relationship becoming physical might cure Kylie of her more eccentric notions about our story being written in the stars."
        "But it seems that, if anything, it's only served to make her all the more convinced of the fact."
        "Perhaps sensing my slight feelings of unease, Kylie sits by me on the bed and wraps her arms around me."
    kylie.say "It's okay, [hero.name] - everything's working out just how it's supposed to for us."
    kylie.say "You don't have to worry about anything, becasue it's just you and me now."
    if not kylie.get_flag_value("sex"):
        kylie.say "Together forever, just how it should be!"
        "What exactly does she mean by that?"
        "All we did was fuck just now!"
        "Sure, I popped her cherry - but that's not like a declaration of marriage!"
        "I think Kylie and I are going to have to sit down and have a long, very frank talk about where we're headed."
        "But I don't think now would be a good time..."
    $ kylie.set_flag("sex",1,"permanent","+")
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
