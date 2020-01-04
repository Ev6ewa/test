init -1 python:
    Event(**{
        "name":"audrey_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "audrey",
        "girls_conditions": {"audrey":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"audrey_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "audrey",
        "girls_conditions": {"audrey":{"contact":"audrey","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(12,13),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"audrey_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "audrey",
        "priority":100,
        "girls_conditions": {"audrey":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"audrey_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "audrey",
        "priority":100,
        "girls_conditions": {"audrey":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"audrey_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "audrey",
        "priority":100,
        "girls_conditions": {"audrey":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_audrey_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"audrey_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "audrey",
        "priority":100,
        "girls_conditions": {"audrey":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"audrey_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "audrey",
        "girls_conditions": {"audrey":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_audrey_hint:
    $ story = audrey.get_flag_value("story")
    if story == 0:
        if hero.charm < 20:
            "I need to look better."
        elif hero.fitness <20:
            "I need to get in shape."
        else:
            "I should go see if Audrey is at the pub."
    elif not audrey_love == audrey_love_max:
        "I should get to know Audrey better."
    elif story == 1:
        "I should talk to Audrey at the office."
    elif story == 2:
        "I should see if Audrey is at the gym."
    elif story == 3:
        "Audrey will call me for our date at the waterpark, probably on saturday."
    else:
        "I reached the end of Audrey's story for now."
    return

label audrey_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = audrey.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = audrey.get_activity(bye_hour)
    if not activity == audrey.activity:
        if day != game.week_day:
            $ audrey.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ audrey.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "audrey "+bye_outfit
        if activity["activity"] == "sleep":
            audrey.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            audrey.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            audrey.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            audrey.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            audrey.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            audrey.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            audrey.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            audrey.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            audrey.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            audrey.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            audrey.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            audrey.say "I ll go get dressed."
        hide expression "audrey "+bye_outfit
    return

label audrey_cheated:
    show audrey
    "I see Audrey looking at me kissing someone else with envy and lust in her eyes."
    $ audrey.love += 1
    hide audrey
    return

label audrey_greet:
    if not audrey.get_flag_value("greeted"):
        $ audrey.set_flag("greeted",True,1)
        show audrey
        $ result = randint (1,3)
        if result == 1:
            audrey.say "Hello, [hero.name]."
        elif result == 2:
            audrey.say "Hi, [hero.name]."
        elif result == 3:
            audrey.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                audrey.say "Good morning [hero.name]."
            elif game.hour < 19:
                audrey.say "Good afternoon [hero.name]."
            else:
                audrey.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Audrey."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                audrey.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Audrey."
            elif game.hour < 19:
                hero.say "Good afternoon Audrey."
            else:
                hero.say "Good evening Audrey."
    return

label audrey_kiss:
    scene expression "bg "+game.room
    if audrey.love() + hero.charm() < 80 and not audrey.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show audrey
        "Sometimes when you look back on a situation that you misread, it's pretty obvious, in retrospect, just what you did wrong."
        "But at the same time there are still those incidents that you find yourself genuinely scratching your head over hours, even days later."
        "Audrey just put me in that very situation, making me wonder how I could have elicited such a reaction from her, especially based on the tone of her behaviour towards me."
        "She leans in close to me, making one of her typically outrageous and obviously provocative comments."
        "Normally I would have tried my best to either ignore the flirtation or take her to task over some other imagined transgression."
        "But for some reason that I can't readily explain, I just feel the urge to stop pushing back on this occasion."
        "So instead of protesting and telling Audrey that he behaviour isn't appropriate, I lean in closer too."
        "All I had in mind was kissing her quickly, maybe just a peck on the lips."
        "But she surprises me by instantly sensing my intentions and jerking her head back, moving her lips well out of range."
        audrey.say "Uh-uh...I don't think so!"
        "And with that, she skips away, wagging her finger at me and tutting in a disapproving manner."
        "All of which leaves me more confused than I was when the whole thing began."
        "I always thought that the point of Audrey's flirting was to entice me into her web."
        "Is it possible that there's more too it than that?"
        "Or is she just swinging from one extreme to the other in order to further confuse me?"
        $ audrey.love -= 1
        hide audrey
    elif not audrey.get_flag_value("kiss"):
        hide audrey
        show expression "audrey kiss "+audrey.get_clothes()
        "I feel like I can only keep on fighting the same fight over and again for so long before I start going mad."
        "And it feels like I've been battling against Audrey for as long as she's been a part of my life, without a pause in the hostilities."
        "It seems as though this antagonism between us has become the main source of consternation in my daily life."
        "The constant flirting and provocative behaviour is probably better described as a form of sexual harassment."
        "But even though it's the twenty-first century, I'd still feel like an idiot were I to report it to human resources."
        "I guess that's why one day I just think, fuck it."
        "And rather than shying away from her as she makes her usual round of manipulative statements and thinly veiled threats, I decide to call her bluff."
        "When Audrey leans forwards to rub in the latest one of her manipulative tricks, I simply mirror her move and place my lips firmly against her own."
        "Instantly, I see her eyes grow wide and almost swell with shock."
        "In fact, she seems to be so taken by surprise that it's almost a full minute before I can feel her begin to relax and return the kiss."
        "I can't guess what the consequences of finally giving in to Audrey are going to be."
        "But for the moment, I have to admit that by keeping on resisting the temptation that she represented, I've been denying myself something that feels really sensational."
        hide expression "audrey kiss "+audrey.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != audrey and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_53
        $ audrey.set_flag("kiss",1,"permanent","+")
        $ audrey.love += 1
    else:
        hide audrey
        show expression "audrey kiss "+audrey.get_clothes()
        "I'm not sure what really changed once I finally gave in and Audrey's games of teasing and little threats became a thrill in my life, rather than a constant source of torture and torment."
        "But whenever the point that it all changed did come, things have been getting steadily better for me ever since then."
        "Of course, Audrey still seems to be intent upon playing the very same kind of games with me as she did before."
        "Yet now I'm a more than willing participant, and I actually look forward to discovering what mischief she has planned for me when I see her next."
        "Where before I would have been cringing away or else at the very least trying to shout her down, I now can't wait to have the chance to catch Audrey and pull her into my arms for a passionate kiss whenever the chance arises."
        "All of the spite and spice that used to be channelled into her antics around trying to seduce me can now be diverted into making our stolen moments together something to remember afterwards."
        "There are even times when the girl that was once using all of her slyness and seductive charms to try to draw me into her web is actually the one that finds herself now seeking to avoid being caught."
        "I guess there's something to the idea of being careful what you wish for, as well as realising that what you really want is sometimes right in front of you the whole time."
        hide expression "audrey kiss "+audrey.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != audrey and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_56
        $ audrey.love += 1
    return

label audrey_fuck_date:
    $ audrey.set_flag("sex",1,"permanent","+")
    scene bg livingroom
    show audrey
    "As soon as the door is closed I pick Audrey up and she wraps her legs around my waist as I kiss her heavily."
    menu:
        "Lay her on the couch":
            "I quickly take her over to the couch and lay her down."
            "I climb on top of her and start to kiss her deeper and leave bite marks on her neck."
            "Suddenly she puts put hands on my chest to stop me."
            audrey.say "This is a little bit to open for me... What if your roommates come home?"
            "I sigh."
            "She's right."
            "If one of the girls walk it we will have to stop and it will ruin the night."
            hero.say "Okay, we can go to my room."
            "I lean down and start to kiss he again."
            "After she has her arms and legs wrapped around me a carry her to the bedroom."
        "Go to the bedroom.":
            "I press my tongue into her mouth and she runs her fingers through my hair trying to make the kiss even deeper."
            "Hardly being able to see what I am doing I carry her to my bedroom almost falling into the wall once."
    "Luckily my door wasn’t locked and we go right in, pausing long enough for me to lock it behind us so we won’t be interrupted."
    "I carry her to the bed and lay her down as we continue to make out."
    "I lose track of anything else around me when suddenly she pulls away for air."
























    hero.say "Take your clothes off"
    show audrey underwear
    "Audrey gets up and submissivly comply to my order."
    show audrey naked
    hero.say "You look amazing."
    show audrey naked blush
    "I see Audrey smile."
    audrey.say "Thanks babe. Does it make you wanta do anything?"
    show audrey naked
    "I nod quickly as she walked back over to be and kneel on the bed."
    audrey.say "Why do you still have so many clothes on? This is looking rather one-sided here."
    hero.say "Oh... right. Why don’t you help me out of some of these?"
    "She smirks and comes closer."
    "She put her hands on my hips and then slowly slide her hands up my shirt until was lifting it up and over my head."
    "She looks over my abs and trails her finger down them."
    audrey.say "The gyms done you some good, babe."
    "The compliment makes me even more eager to get started again."
    "I grab her again and push her back down on the bed."
    "I start nibbling her ear again as she feels for my zipper to undo my pants."
    "As soon as she has succeeded on getting them undone I help her slip them down and off my legs."
    menu:
        "Grind on her":
            "I grind against her slowly at first and then rougher as the kissing gets hotter."
        "Don’t Grind":
            "I continue the kiss but don’t do anything else yet because I am unsure of myself again."
            audrey.say "Do something already!"
    "She bucks her hips up into mine and whispers..."
    audrey.say "What are you waiting for, fuck me you idiot."
    "I look her in the eyes and she seems to be daring me to do it as she lets her legs fall open slowly to either side."
    if hero.has_condom():
        menu:
            "Use a condom":
                $ CONDOM = True
                $ hero.use_condom()
            "Do it raw":
                $ CONDOM = False
    else:
        $ CONDOM = False
    hide audrey
    show audrey spoon penis_b
    "I push her on the bed and slide behind her, my hand caressing her tits."
    show audrey spoon fuck
    "I shove in all the way without warning and she lets out a scream."
    "Finally I thought, I’m what is making her scream."
    "Just like I wanted to on the rollercoaster."
    "I pull out and push back in more gently, realizing how tight she is and trying to find a pace that won’t make me lose it embarrassingly fast."
    "In this position I was able to hit deeper and thrust hard, her hand started rubbing her clit."
    "I can’t help myself though and a few times I buck my hips up wanting to help make friction between us."
    "Suddenly a thought comes to me..."
    show audrey spoon fuck choke
    "My hand goes up from her right tit to her neck and I start choking her."
    "Her breathing start getting heavier and he moaning stronger as I shut down her air pipe."
    "When I release my grip a little she manages to let her voice out."
    audrey.say "More, please be rougher, be brutal..."
    "After that my hand goes back to her neck preventing her from talking and I start slamming myself in her pussy harder."
    "It isn’t long and I feel a pressure building up inside me."
    "We both start panting hard and I can’t seem to make my thrusts fast enough."
    "Just when I think I am about to cum I turn her back around so I can see her face when she does."
    if persistent.xray:
        show audrey spoon fuck choke xray
    "I wait as long as I can, and the moment I she cries out in bliss and I feel her walls tighten around me it was all I could take."
    if not CONDOM:
        menu:
            "Cum inside":
                hide audrey
                if persistent.xray:
                    show audrey spoon fuck choke xray cum
                else:
                    show audrey spoon fuck creampie_a ahegao
                audrey.say "Yes, fill me up, I am yours... [hero.name]!"
                if (randint(1,3) == 1 or "hung" in hero.skills) and not audrey.get_flag_value("pregnant") and not audrey.get_flag_value("pill"):
                    $ audrey.set_flag("pregnant",1)
                show audrey spoon penis_b normal
            "Pull out":
                hide audrey
                show audrey spoon penis_a cumshot ahegao
                audrey.say "Yes, mark me, I am yours... [hero.name]!"
                hide audrey
                show audrey spoon penis_b cum_a cum_b normal
    else:
        hide audrey
        show audrey spoon fuck creampie_a ahegao
        audrey.say "Yes, That's soooo good... [hero.name]!"
        show audrey spoon penis_b normal
    "I pant to catch my breath."
    hero.say "I think that was the most powerful orgasm I have ever had."
    audrey.say "Me... to. Me to."
    hide audrey
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
