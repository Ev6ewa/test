init -1 python:
    Event(**{
        "name":"palla_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "palla",
        "girls_conditions": {"palla":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"palla_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "palla",
        "girls_conditions": {"palla":{"contact":"palla","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(12,13),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"palla_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "palla",
        "priority":100,
        "girls_conditions": {"palla":{"valid":True,"flag_greeting":False,"flag_talksex":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"palla_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "palla",
        "priority":100,
        "girls_conditions": {"palla":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"palla_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "palla",
        "priority":100,
        "girls_conditions": {"palla":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_palla_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"palla_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "palla",
        "priority":100,
        "girls_conditions": {"palla":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"palla_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "palla",
        "girls_conditions": {"palla":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_palla_hint:
    if palla_love != palla_love_max:
        "I should get to know her better."
    elif 'palla_event_03' not in DONE:
        "Palla likes to go shopping, I should look around the mall for her."
    elif 'palla_event_04' not in DONE:
        "I think she might call me late at night."
    elif 'palla_event_05' not in DONE:
        "Palla needs to talk about what happened."
    elif 'palla_event_06' not in DONE and not (palla.get_flag_value('giftflowers') or palla.get_flag_value('giftsweets')):
        "I think she said she likes flowers and candies."
    elif 'palla_event_06' not in DONE:
        "I think she might call me late at night."
    elif 'palla_event_08' not in DONE and palla.sub < 70:
        "I need to train Palla more."
    elif 'palla_event_08' not in DONE:
        "Palla likes to call late at night, doesn't she?"
    elif 'palla_event_09' not in DONE:
        "Palla likes to hang around the nightclub."
    elif 'palla_event_10' not in DONE:
        "I think I've seen that guy she was with hanging around the mall. I should check around there."
    elif not palla.get_flag_value('talkedshawn'):
        "I should talk to Palla about Shawn."
    elif 'palla_event_11' not in DONE:
        "I need to figure out what's going on with Palla. I should look around for her at night."
    elif 'palla_event_12' not in DONE:
        "I guess Palla will call me when she's ready."
    else:
        "Palla's story will continue in a future version."
    return

label palla_talk_subjects(subjects=[]):
    if 'palla_event_10' in DONE and not palla.get_flag_value('talkedshawn'):
        $ subjects.append('shawn')
    return

label palla_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = palla.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = palla.get_activity(bye_hour)
    if not activity == palla.activity:
        if day != game.week_day:
            $ palla.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ palla.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "palla "+bye_outfit
        if activity["activity"] == "sleep":
            palla.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            palla.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            palla.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            palla.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            palla.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            palla.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            palla.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            palla.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            palla.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            palla.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            palla.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            palla.say "I ll go get dressed."
        hide expression "palla "+bye_outfit
    return

label palla_cheated:
    show palla
    "I see Palla looking at me kissing someone else with envy and lust in her eyes."
    $ palla.love += 1
    hide palla
    return

label palla_greet:
    if not palla.get_flag_value("greeted"):
        $ palla.set_flag("greeted",True,1)
        show palla
        $ renpy.dynamic('greeting', 'timeofday')
        $ greeting = randint (1,3)
        if game.hour < 6:
            $ timeofday = 'Hello'
        elif game.hour < 12:
            $ timeofday = 'Good morning'
        elif game.hour < 19:
            $ timeofday = 'Good afternoon'
        else:
            $ timeofday = "Good evening"

        if (palla_love < 40):
            if greeting == 1:
                palla.say "Oh, it's you, asshole."
                hero.say "Yeah, hi to you too, bitch."
            elif greeting == 2 and hero.grooming < 6:
                palla.say "Ugh, you stink, [hero.name], go shower!"
                hero.say "Join me?"
                palla.say "Gross!"
            else:
                palla.say "Hi, I guess."
                hero.say "You guess?"
                palla.say "Fine, I take it back."
        elif palla_love < 120:
            if greeting == 1:
                palla.say "[timeofday], [hero.name]"
                hero.say "Wait you said hello without being mean."
                palla.say "Yeah? Sorry, I meant \"Hi there, fuckface\""
            elif greeting == 2 and hero.grooming < 6:
                palla.say "Ugh, you stink, [hero.name], go shower!"
                hero.say "Join me?"
                palla.say "You'd have to force me."
            else:
                palla.say "'Sup, asshole?"
                hero.say "Nothing much, bitch!"
                "She smiles sweetly."
        elif palla_love < 199:
            if greeting == 1:
                "Palla stares at me hungrily. When I look her way our eyes meet for a split second, then she looks away and pretends not to see me."
            else:
                palla.say "[timeofday], Handsome!"
                hero.say "Hey sexy!"
        else:
            palla.say "[timeofday], Handsome!"
            hero.say "Hey sexy!"
    return

label palla_ask_number:
    if palla.love < 10 or not hero.charm >= 40 - game.active_girl.love():
        if palla.get_flag_value('storeanal'):
            palla.say "After what you did? I don't think I like you that much."
        else:
            active_girl.say "Not a chance!"
    else:
        $ hero.smartphone_contacts.append(game.active_girl.id)
        active_girl.say "I guess."
    return

label palla_ask_date:
    hero.say "Palla, would you like to go on a date with me?"
    if palla.love < 40:
        palla.say "Gross! No!"
        return False
    elif game.active_girl.love() < 50 or game.active_girl.get_flag_value("nodate"):
        palla.say "Sorry [hero.name], we're not there yet."
        return False
    else:
        if palla.get_flag_value('sex') < 3:
            palla.say "Okay, but no promises. When do you want to go?"
        else:
            palla.say "Of course! When do you want to go?"
        return True

label palla_ask_fuck_date:
    if game.get_flag_value("datescore") >= (100 - palla.get_flag_value("drinks")*5):
        if palla.get_flag_value('sex') < 3:
            hero.say "Do you want to come back to my place?"
            palla.say "I don't know..."
            hero.say "Did you have fun?"
            palla.say "I guess. Sure, as long as your place isn't too much of a shithole."
        else:
            palla.say "Let's go back to your place, [hero.name]."
            hero.say "I would love that."
        return True
    else:
        palla.say "It was really nice."
        return False

label palla_kiss:
    scene expression "bg "+game.room
    if palla.get_flag_value('nokiss') or palla.love() < 20 or (palla.love() + hero.charm() < 80 and not palla.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75):
        show palla
        "Palla quickly takes a step back, and turns away."
        if palla.love < 40:
            palla.say "Ugh, no, gross!"
            $ palla.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                palla.say "Nuh uh, you haven't earned that yet."
                $ palla.love -= 1
            else:
                palla.say "I'm sorry, but I have to go..."
            "Before I can react, Palla turns and rushes away."
        hide palla
    elif palla.love() + hero.charm() < 60  or (game.get_flag_value("datescore") >= 75 and not palla.love() + hero.charm() < 60):
        hide palla
        show expression "palla kiss "+palla.get_clothes()
        if not palla.get_flag_value("kiss"):
            "I watch Palla's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "palla kiss "+palla.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != palla and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_128
            elif palla.love >= 60:
                show palla
                palla.say "Um, I think we should talk about this later, alright?"
            else:
                show palla
                palla.say "Oh uh... I've got to go..."
                "Before I can object, Palla begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ palla.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Palla, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "palla kiss "+palla.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != palla and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_129
        $ palla.love += 1
    else:
        hide palla
        show expression "palla kiss "+palla.get_clothes()
        if not palla.get_flag_value("kiss"):
            "I feel my lips passing over Palla's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Palla with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "palla kiss "+palla.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != palla and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_130
            elif palla.love() >= 60:
                show palla
                palla.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show palla
                palla.say "Um... I should go..."
                "Before I can object, Palla turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Palla's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Palla with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Palla, close enough that our bodies are very nearly touching."
                "I bring one hand to Palla's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Palla's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "palla kiss "+palla.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != palla and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_131
            if hero.charm() >= 160 - palla.love():
                show palla
                palla.say "Stop doing that."
        hide palla
        $ palla.love += 2
    return

label palla_dance_with:
    show palla
    $ renpy.dynamic('palla_nick')
    $ palla_nick = "Palla"
    if not palla.get_flag_value("nokiss"):
        $ palla_nick = randchoice(['Sexy', 'Gorgeous', 'Bitch', 'Beautiful'])
    hero.say "Hey [palla_nick], care to dance?"
    if 'dance' in hero.skills:
        palla.say "Fuck yeah!"
        "As we dance together, it's as though the two of us become one. Mostly I lead, and she anticipates my every move."
        if palla.love > 120:
            "When the right music comes by, she presses her body right up to mine, and we dance dirty. She doesn't hesitate to use everything in the dance."
            "And I mean everything."
            "When we dance, it is erotic, it is exhilarating, and it is exhausting."
    elif hero.get_flag("teaching_dance") == -1:
        palla.say "No way, you can't dance for shit."
        menu:
            "Teach me!":
                hero.say "Teach me to dance!"
                palla.say "Maybe, I'll think about it."
                $ hero.set_flag('teaching_dance', 1)
                $ palla.love += 1
                hide palla
                return
            "Forget it!":
                hero.say "Oh forget it, then."
                $ hero.set_flag('teaching_dance', -1)
                $ palla.love -= 1
                hide palla
                return
    elif not hero.get_flag('teaching_dance'):
        palla.say "Sure, I love to dance!"
        "But I'm a terrible dancer, and Palla quickly gets frustrated."
        palla.say "You really need to learn to dance, asshole."
        menu:
            "Okay, teach me!":
                hero.say "Teach me! You're great at this!"
                palla.say "Hmm. Maybe. I'll think it over."
                $ hero.set_flag('teaching_dance', 1)
                $ palla.love += 1
                hide palla
                return
            "Forget it!":
                hero.say "Oh forget it, then."
                $ hero.set_flag('teaching_dance', -1)
                $ palla.love -= 1
                hide palla
                return
    else:
        palla.say "Ready for a dance lesson?"
        hero.say "Yes!"
        if (hero.get_flag_value('dance') == 1):
            "Palla spends the better part of an hour walking me through some of her basic dance moves. That part isn't too hard."
            "The more interesting part is how I need to read her, to anticipate what she's going to do."
            "While at the same time I use subtle cues to communicate to her what I'm going to do. Sometimes it's just the first step."
            "And we both know the routine. But sometimes we get creative."
            "That part I don't do very well at, but I'm definitely learning."
        elif (hero.get_flag_value('dance') == 2):
            "We build on what I learned last time, introducing a few more dance moves and routines. While at first it's hard, one part of it really motivates me."
            "Whenever I get it really right, she gets this hungry look in her eyes, like she just wants to throw me down and fuck me right there."
            "This dancing thing really turns her on, and the more I get into it, the more I start to see why."
        elif (hero.get_flag_value('dance') == 3):
            "When we started, Palla didn't really want to teach me to dance, she clearly thought I would be a burden."
            "But as I get better, she's really taken a shine to it. And I am definitely getting better."
            "And to be honest, this is the nicest to me she has ever been."
        else:
            "Palla shows me a few new moves, and I'm able to work out where they go pretty quickly. After an hour or so she gives me a big smile."
            show palla happy
            palla.say "I think, [hero.name], that your lessons are done, and while you still have a lot to learn, you can dance well enough that I won't say you suck anymore!"
            $ hero.skills.append('dance')

        $ hero.set_flag('teaching_dance', 1, mod="+")

    $ bonus = hero.fitness()/20
    if hero.check_skill("dance"):
        $ bonus += 2
    $ palla.love += bonus
    $ hero.fun += 2
    $ game.pass_time(needs=True)
    hide palla
    return

label palla_fuck_date:
    $ palla.set_flag("sex",1,"permanent","+")
    scene bg street
    show palla
    if palla.get_flag_value('sex') == 1:
        call palla_fuck_date_first
    else:
        call palla_fuck_date_second
    return

label palla_fuck_date_first:
    "I can't help but wonder if Palla actually gets the way she sounds, or is aware of the effect of the words coming out of her mouth."
    "All night she's been tossing out catty comments and downright rude opinions on anything and everything that her gaze happens to fall on."

    "I was just glad she had so many other targets for her vapid bile that I didn't become the focus for it instead."
    "But after we grab a taxi and head back to my place, all of that changes."
    "Palla's comments inevitably turn to how suburban my neighbourhood is, how twee the house looks, and on, and on."
    scene bg livingroom
    show palla
    "Even when we get inside she's still going on, about how cramping it must be to live with housemates and the blandness of the decor."
    "By the time we get to my room, I'm almost fuming."
    "But that's the weird thing - I'm not even thinking of telling her to get lost."
    "It seems the more that Palla winds me up, the more I want to get my hands on her in the most physical way possible."
    "She makes me fume, but it's almost like it affects me in the same way as flirting or foreplay should."
    scene bg bedroom1
    show palla
    "There's just something about the arrogance and haughtiness about her."
    "Combined with the fact that she's physically stunning, it feels like an open challenge to step up and somehow rub her face in it."
    "Palla kicks off her expensive and very uncomfortable looking shoes and sits down on my bed."
    show palla underwear
    "She starts to strip off in an almost desultory manner, her face showing an ironic cast as I begin to follow her lead."
    show palla naked
    "It strikes me that she's very much intent on us getting intimate, despite her constant carping and complaining."
    "I guess she's so used to it that it seems normal...or maybe grousing like that turns her on?"
    palla.say "Well, at least I get treated to an actual bed this time!"
    hero.say "I didn't hear you complaining the last time."
    palla.say "Erm, hello...we were fucking in a three foot square cubicle surrounded by strangers."
    palla.say "At least now we won't have someone walk in on us."
    palla.say "Unless it's one of those two skanks that you live with!"
    "My face must show my exasperation at this last comment, as Palla smiles with sudden relish."
    palla.say "Oh, have I hit a nerve?"
    palla.say "Or is that something you were hoping might happen?"
    "That's it, she's really pushing my buttons now."
    "I'm mad, but not enough to do anything truly stupid - but does she realise that?"
    hero.say "Okay, Palla - it's time I shut you up and gave you just what you're asking for."
    show palla naked angry
    "Palla's expression becomes more than a little shocked, and she begins to say something in protest."
    "But I'm on the bed and onto her before she can get as much as a word out."
    "I know I'm banking on my hunch being right, that Palla's goading me into dominating her more than a little."
    "But I'm committed now, so I'd look like a massive tool if I backed off now."
    "I put a hand in her hair and get a good grip."
    "Not yanking painfully, but firm enough to make her think it might go that way if she struggles."
    palla.say "Hey, - what the hell?!?"
    "From there I guide her onto all fours, facing away from me, buttocks pointed in my direction."
    "Despite my hold on her hair, Palla tries to look back over her shoulder at me."
    "I catch a glimpse of surprise, anticipation and maybe even a little bit of fear in her eyes."
    menu:
        "Fuck her pussy with a condom" if hero.has_condom():
            call palla_fuck_pussy_condom
        "Fuck her pussy raw":
            call palla_fuck_pussy_raw
        "Fuck her ass" if palla.sub >= 25:
            call palla_fuck_ass
    "With Palla's almost ragged cries ringing in my ears, I know it's only going to be a matter of seconds before I inevitably cum."
    call palla_fuck_cum
    "Palla remains silent afterwards, and I don't feel like I have anything to say either."
    "Though she's not speaking to me, she's notably not tearing a strip off of me for what I did to her either."
    "In the silence, I reflect on the fact that, ironically, we seem to have communicated far better just now than ever before."
    "And all without either of us saying a single word."
    hide palla

    $ palla.set_flag('nodate', True)
    $ palla.set_flag('talksex', True)
    call palla_sleep_date_fuck from _call_palla_sleep_date_fuck
    return

label palla_fuck_date_second:
    scene bg house with dissolve
    show palla
    "When we get to the house, Palla looks it up and down."
    palla.say "You live in a suburban wasteland, [hero.name]."
    hero.say "Sure, but it's MY suburban wasteland."
    scene bg livingroom
    show palla
    palla.say "I don't understand why you live here anyway. You make good money, you don't need those bimbo roommates."
    menu:
        "Ignore it":
            pass
        "Roommates are off limits!":
            hero.say "Time out, Palla. Bree and Sasha are off limits. You can say what you want about me, about my house, about my job."
            hero.say "But if you can't come up with something nice to say about them, don't talk about them at all."
            palla.say "What, you going to kick me out?"
            hero.say "They live here, you don't. I've got a good relationship with them."
            if game.get_flag_value("homeharem"):
                palla.say "Oh yes, I know all about your good relationship with them."
                hero.say "Jealous, much?"
                palla.say "No way, like I said before, I think it's kind of hot."
                hero.say "Then be nice to them!"
                "Palla rolls her eyes at me."
            palla.say "Fine, whatever."
            $ palla.sub += 3
    palla.say "Let's just get to your bedroom so I don't have to look at this place any more."
    hero.say "Are you TRYING to piss me off?"
    palla.say "Hey, you know how I said I was hot when I'm angry?"
    show palla happy
    palla.say "Well, same's true for you, [hero.name]. That really gets me wet!"
    palla.say "Now, are you going to come fuck me senseless or what?"
    "And with that, she darts toward my room and I actually have to chase her."
    scene bg bedroom1
    show palla
    "She runs down the stairs and into my bedroom and nearly slams the door in my face. I put my arms up just in time, and it SLAMS back open."
    hero.say "Hey! Be quiet, I have roommates!"
    palla.say "Fuck 'em."
    "That's it. That's absolutely it. I close the door behind me, this time trying not to slam."
    hero.say "No, fuck YOU. Now take your clothes off and shut up, bitch, before I decide to kick your ass out."
    if palla.sub < 30:
        palla.say "Fuck you, [hero.name], don't talk to me like that!"
        menu:
            "Kick her out":
                hero.say "That's it! I've had it with you. Get out!"
                show palla sad
                palla.say "Wait, no! I just got here and we had a good time, and I was just..."
                menu:
                    "I'm serious, get out":
                        hero.say "I'm serious, get the fuck out of my house."
                        "Palla's face goes through a series of expressions: angry, sad, humiliated, and then finally back to angry."
                        "She grabs her stuff and storms out of the house."
                        $ palla.set_flag('nodate', True)
                        $ palla.set_flag('nokiss', True)
                        return
            "Be nicer":
                "It takes some effort, but I decide to be nicer. It's tough, given how much she's been spinning me up."
                hero.say "If you want me to be nicer, don't purposefully make me angry."
                hero.say "Now, please, take your clothes off."
                "Palla does so, but she actually looks a little disappointed. I guess I shouldn't be surprised, it's obvious she wanted me angry."
                $ palla.love += 1
            "Make her":
                hero.say "Take your clothes off, Palla, or I will get the belt out and punish you."
                "Palla's eyes go wide."
                palla.say "Punish me?"
                hero.say "I will whip that ass so red you won't feel it when I stick my dick in your ass."
                "I expect her to fight it more, but she doesn't! She quickly starts undressing."
                $ palla.sub += 5
    else:
        "Palla looks, for a moment, like she's going to object, but then suddenly her clothes start to come off."
    show palla underwear
    hero.say "And now the bra and panties."
    palla.say "You first."
    hero.say "NOW!"
    "Palla does what she is told, and when the bra comes off, I see that her nipples are hard as rocks."
    show palla naked
    hero.say "Now, get down on all fours."
    if palla.get_flag_value('anal'):
        palla.say "Please don't fuck my ass again!"
    else:
        palla.say "Please don't fuck my ass! It'll hurt!"
    hero.say "I will fuck you wherever I please. Now get on all fours!"
    "Palla moves only very slowly to do what she's told, so I step up and help her out, grabbing her hair and roughly moving her into position."
    "She doesn't resist at all, though she does continue pleading me not to do her ass."
    menu:
        "Fuck her pussy with a condom" if hero.has_condom():
            call palla_fuck_pussy_condom
        "Fuck her pussy raw":
            call palla_fuck_pussy_raw
        "Fuck her ass" if palla.sub >= 25:
            call palla_fuck_ass
    "With Palla's almost ragged cries ringing in my ears, I know it's only going to be a matter of seconds before I inevitably cum."
    call palla_fuck_cum
    "Palla moans quietly after I pull out of her, and she rolls over to look up at me."
    if palla.love > 190:
        if palla.sub > 90:
            palla.say "I love you so much. Master."
        else:
            palla.say "I love you so much."
    "I drop myself down and lay next to her. She pulls close and cuddles for a bit, and I see something I rarely see in her: True happiness."
    "I reflect that the thing this haughty and it turns out naughty bitch really wants is to be taken rough."
    "And I admit I do enjoy doing that."
    hide palla
    call palla_sleep_date_fuck from _call_palla_sleep_date_fuck_second
    return

label palla_fuck_pussy_condom:
    show palla doggy
    "I only pause long enough to slip a condom on, before lining myself up with Palla's exposed pussy."
    palla.say "What's going on back there?"
    "Without explaining a single thing to her, I thrust forwards and force myself into her with some considerable urgency."
    palla.say "wha...aaa...aaah!"
    "Despite her protests, Palla's more than ready to take me in."
    "Her pussy is already wet and accommodating, her muscles yielding without similar protests as I begin to push in and out."
    "Palla's arms tremble at first, trying to keep her upright as she begins to quiver from the sensation of being roughly fucked from behind."
    "Then they simply collapse as she sags forwards amongst the sheets, allowing me to get an even more acute angle inside of her."
    show palla doggy orgasm
    "She's still making some small mewling sounds, perhaps the last gasp of her previous protests."
    "But even these are muffled into almost nothing by the sheets."
    "I redouble my efforts, feeling my ardour rise as Palla starts to yelp in response to each more intense thrust into her."
    $ hero.use_condom()
    return

label palla_fuck_pussy_raw:
    $ palla.love += 5
    show palla doggy
    if palla.get_flag_value('sex') < 3 or palla.sub < 40:
        palla.say "Hey, what are you..."
        "That's all she manages to get out before I stroke my cock against the lips of her pussy and begin to slowly push into her."
        palla.say "Ohh...noo...ohh!"
        "While she might have been making sounds of disapproval, the slick feeling of Palla's pussy reveals the truth of the matter."
        "Another time I might have slowed down and really tried to savour the sensation of making Palla twitch and writhe like this."
        "But her queen bitch attitude only makes me want to fuck her ever harder and faster."
        "She's stopped protesting now, and begun to merely moan in response to the ferocity of my thrusts into her."
    else:
        "I hear Palla take a sharp breath as I press my cock up against the lips of her pussy."
        "She cries out in delight as I sink into her."
        "She responds by pressing her ass back into me, and as she does so I pull on her hair, eliciting another cry of joy."
        palla.say "Yes, [hero.name], faster! Harder!"
    "Palla sags forward into the sheets and pillows, the motion of being banged so hard from behind driving her downwards."
    "From this angle there's nothing to stop me pounding her with almost all of my weight, and I do so."
    "I try not to think that I'm punishing Palla, more like disciplining her in a roundabout way."
    show palla doggy orgasm
    "Every thrust that elicits a moan of enforced pleasure feels like an appropriate reply to her earlier catty and annoying jibes."
    return

label palla_fuck_ass:
    $ palla.love += 5
    $ palla.sub += 5
    show palla doggy
    if palla.get_flag_value('anal') < 1:
        "Even though Palla is already on all-fours and fully open to me, it's not enough for what I have in mind."
        "Without asking permission, I push her arms out from under her and send her face tumbling into the piled sheets."
        "This only succeeds in muffling her protests for a moment, as she can already feel just where the head of my cock is probing now that her anus is full exposed."
        palla.say "Oh god, - not that!"
        "I ignore her completely, grabbing a handful of hair on her scalp in my right hand and gripping a ponytail's worth behind her head with my left."
        palla.say "Please, please, please - don't fuck me in the ass!"
        palla.say "Please - I don't even like the thought of it!"
        "By now I have the tip of my dick all lined up and ready to go, and I know she can tell I'm teetering on the brink."
        palla.say "PLEASE, I'm begging you not to!"
        palla.say "I hate it...I hate it...it'll...hurt me..."
        "Were it not for her bitchy comments and acid tongue, I might have been moved by her pleas."
        "But as it is, I think that she's about to get what she so richly deserves."
        "Keeping a firm hold on Palla's hair, I force my cock into her unwilling ass."
        show palla doggy orgasm
        "She shivers bodily as I enter her anus, making a deep moaning sound that turns into quieter whimpers as the full length slides inside of her."
        "I hold myself quite still once I've pushed in as far as I can manage, enjoying the sensation of Palla's muscles quivering around my cock."
        "At first I keep my movements small and slow, only building up speed a little at a time."
        "Palla continues to make incoherent sounds that are part pain and part humiliation."
        show palla doggy ahegao
        "But as my thrusts become more intense and lengthy, the sounds begin to rise in volume and change in tone."
        "They turn back into whimpers, then into moans, and finally evolve into what I can only describe as almost cries of increasing pleasure."
        "The change affects me as well, knowing that the humiliation Palla's feeling has somehow broken through her catty demeanour and laid her wide open."
        "The more she cries in guilty pleasure, the closer I come to losing myself, deep in her anus."
    else:
        hero.say "Ready for another ass-pounding?"
        if palla.sub > 80:
            "Palla spreads her cheeks wide for me, at the same time burying her face and chest into the pillows."
            "I line myself up and press the tip right against her anus, pushing it open just slightly, but not entering."
            hero.say "Tell me you want it."
            palla.say "I...I want it."
            hero.say "Tell me you need it."
            palla.say "I need it, [hero.name], I need it!"
            hero.say "Tell me you LOVE it!"
            "Palla's breathing gets heavier, even though I haven't even started."
            palla.say "I love it, [hero.name]! Oh God, I love it!"
            if palla.love > 190:
                palla.say "And I love you too!"
            "The talk has made me as hard I've ever been, and I press into her anus. It gives way easily and I plunge in."
            "Palla shrieks into the sheets, her muffled cries a combination of pain and pleasure."
            show palla doggy orgasm
            "And on my really hard thrusts, my hands pull her away from the sheets by her hair. It must hurt, but she loves it so much I can't tell."
            "I thrust back and forth, not sparing her at all as I may have in the past."
            "Her cries get louder, and after a few moments, I join her with a gutteral yelp."
            hero.say "Take THAT, bitch!"
            hero.say "And THAT!"
            show palla doggy ahegao
            "Palla's cries might've included a yes, but she is so beyond words it was hard to tell."
            "It doesn't take me long before I'm ready to blow, either."
        else:
            palla.say "No, please! Not again! It hurts! It's torture!"
            hero.say "And you love it, bitch! Open up and take it!"
            "Palla buries her face in the sheets and despite her protestations, her asshole is open and ready for me."
            "I line myself up and press the tip right against her anus, pushing it open just slightly, but not entering."
            hero.say "Tell me you want it."
            palla.say "Mmf! No! I don't want it!"
            "I smack her across one ass cheek; hard enough to make a good snapping sound, but not hard enough to hurt. Much."
            "Palla yelps!"
            hero.say "Tell me you want it."
            palla.say "I don...no...I don...I want it."
            "I press myself into her anus, pushing just the head in to open her up."
            hero.say "Say it again, bitch!"
            "Palla nearly cries out, this time."
            palla.say "I want it!"
            hero.say "You want it!"
            palla.say "I want it!"
            "The talk has made me as hard I've ever been, and I press into her anus. It gives way easily and I plunge in."
            "Palla shrieks into the sheets, her muffled cries a combination of pain and pleasure."
            show palla doggy orgasm
            "And on my really hard thrusts, my hands pull her away from the sheets by her hair. It must hurt, but she loves it so much I can't tell."
            "I thrust back and forth, not sparing her at all as I may have in the past."
            "Her cries get louder, and after a few moments, I join her with a gutteral yelp."
            hero.say "Take THAT, bitch!"
            hero.say "And THAT!"
            show palla doggy ahegao
            "Palla's cries might've included a yes, but she is so beyond words it was hard to tell."
            "It doesn't take me long before I'm ready to blow, either."
    $ palla.set_flag('anal', 1, mod="+")
    return

label palla_fuck_cum:
    menu:
        "Cum inside":
            "After managing to humble Palla like that, the last thing I'm about to do is keep from cumming inside of her."
            "I tighten my grip on her hair and the intensified pain of this goes some way to keeping the tell-tale signs of my muscles twitching from her notice."
            "This means that when I finally lose myself inside of her, Palla is taken almost completely by surprise."
            "She writhes and groans as my climax goes off entirely within one of the most sensitive parts of her body."
            "But my firm grip and her submissive position mean that she can only endure it, even when her own orgasm overtakes her too."






    return

label palla_sleep_date_fuck:
    scene bg bedroom1
    show palla naked
    menu:
        "You should leave":
            hero.say "I am done with you and I have to get up early tomorrow, you should leave."
            "The sex was beyond incredible."
            "Frowning a little, Palla straightens and shrugs, then goes to collect her clothes from where she'd let it fall earlier."
            "She then heads up the stairs."
            $ palla.love -= 1
            $ palla.sub += 1
        "You should sleep here":
            hero.say "You can stay and sleep here."
            "I say, my voice a little shaky."
            "We curl up spooning together in bed, drifting toward sleep."
            $ palla.love += 1
    call sleep from _call_sleep_8
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
