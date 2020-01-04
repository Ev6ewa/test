init -1 python:
    Event(**{
        "name":"alexis_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "alexis",
        "girls_conditions": {"alexis":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"alexis_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "alexis",
        "girls_conditions": {"alexis":{"contact":"alexis","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(12,13),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"alexis_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "alexis",
        "priority":100,
        "girls_conditions": {"alexis":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"alexis_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "alexis",
        "priority":100,
        "girls_conditions": {"alexis":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"alexis_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "alexis",
        "priority":100,
        "girls_conditions": {"alexis":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_alexis_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"alexis_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "alexis",
        "priority":100,
        "girls_conditions": {"alexis":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"alexis_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "alexis",
        "girls_conditions": {"alexis":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_alexis_hint:
    "No hints for Alexis right now."
    return

label alexis_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = alexis.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = alexis.get_activity(bye_hour)
    if not activity == alexis.activity:
        if day != game.week_day:
            $ alexis.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ alexis.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "alexis "+bye_outfit
        if activity["activity"] == "sleep":
            alexis.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            alexis.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            alexis.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            alexis.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            alexis.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            alexis.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            alexis.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            alexis.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            alexis.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            alexis.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            alexis.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            alexis.say "I ll go get dressed."
        hide expression "alexis "+bye_outfit
    return

label alexis_cheated:
    show alexis
    "I see Alexis looking at me kissing someone else with envy and lust in her eyes."
    $ alexis.love += 1
    hide alexis
    return

label alexis_greet:
    if not alexis.get_flag_value("greeted"):
        $ alexis.set_flag("greeted",True,1)
        show alexis
        $ result = randint (1,3)
        if result == 1:
            alexis.say "Hello, [hero.name]."
        elif result == 2:
            alexis.say "Hi, [hero.name]."
        elif result == 3:
            alexis.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                alexis.say "Good morning [hero.name]."
            elif game.hour < 19:
                alexis.say "Good afternoon [hero.name]."
            else:
                alexis.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Alexis."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                alexis.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Alexis."
            elif game.hour < 19:
                hero.say "Good afternoon Alexis."
            else:
                hero.say "Good evening Alexis."
    return

label alexis_kiss:
    scene expression "bg "+game.room
    if alexis.love() + hero.charm() < 80 and not alexis.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show alexis
        "Are you supposed to know when the moment's right for something like this, or is it just a matter of trusting to instinct?"
        "When the time's right, you're supposed to know it, but even that knowledge has to be instinctive!"
        "Either way, I can't keep from leaning in closer towards Alexis right now, turning so that I'm at just the right angle for our lips to meet."
        "She's facing slightly away from me as I do this, meaning that she doesn't see me until the moment that she turns in my direction."
        "All I can see is the fluttering of her blonde hair and the outline of her cheek, and then the shape of her lips."
        "I wonder if they'll feel familiar to kiss after all this time, or if it'll be possible for me to recall their feel at all."
        "I close my eyes in anticipation of feeling them press against mine..."
        "But then all I feel is the curve of her cheek, as Alexis instinctively pulls away from me and pushes me back at the same time."
        "All I get is the scent of her hair and the instant sense of embarrassment that comes with knowing that my advances have been rejected."
        "I mumble something vague about being sorry, and turn away to keep Alexis from seeing that my face has coloured from the experience."
        "And she in turn mutters something equally bland about it not being a big deal, timing and all those other things that don't really help matters."
        hide alexis
    elif not alexis.get_flag_value("kiss"):
        hide alexis
        $ alexis.love += 1
        show expression "alexis kiss "+alexis.get_clothes()
        "Don't ask me how I know - but I know!"
        "There's just something in the way that Alexis's gaze lingers on me as she turns away for a moment."
        "It's not visible desire or anything so obvious, more a warmth in her eyes that tells me she wants something more."
        "I don't say anything, as this isn't a matter of saying the right thing either."
        "This is about instincts and cues that are older far older even than words."
        "When Alexis turns back to me, I lean in and place my lips against hers."
        "This is one of those moments when the world is no larger than the two of you, and it's perfect while something impermanent lasts."
        "She returns the kiss immediately, gently at first, and then with a growing sense of confidence as we come together."
        "I can't remember how we used to kiss when we were teenagers, and truth be told, I don't care to."
        "The Alexis from back then is gone, and I only care about the one that's here, in my arms right now."
        "It seems to last for the longest time, but in truth I guess that we could only have been kissing for perhaps a minute at the most."
        "And in that brief moment, I begin to feel like the years that we were apart were only a brief interlude between then and now."
        "As though I've been waiting for her to come back to me, and now that she has, I can start living again."
        hide expression "alexis kiss "+alexis.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != alexis and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_125
        elif alexis.love >= 60:
            show alexis
            alexis.say "Um, I think we should talk about this later, alright?"
        else:
            show alexis
            alexis.say "Oh uh... I've got to go..."
            "Before I can object, Alexis begins in the opposite direction."
            "She seemed a little uncomfortable, did I do something wrong?"
        $ alexis.set_flag("kiss",1,"permanent","+")
    else:
        hide alexis
        show expression "alexis kiss "+alexis.get_clothes()
        "I know now just when Alexis is leaning into me with that very specific angle to her head and the right look in her eye."
        "I don't hesitate to match her movements so that our lips meet at just the right point for me to feel that spark of excitement."
        "No matter how many times we kiss like this, it never seems to become boring or routine."
        "A part of the thrill that I felt the very first time we kissed after Alexis came back into my life seems to always linger on my lips afterward as well."
        "I seem to be taking every single chance that I can get to kiss her now as well."
        "Now that we're entwined, I risk gently pushing my tongue between her lips."
        "My reward is to have her own tongue come to meet it, caressing and exploring as it slips into my mouth."
        "Our bodies mirror this same movement, as we wrap our arms around each other and pull closer together still."
        "At times like this I find it hard to remember just where we are, as the world around us just seems to lose all importance."
        "We could be alone or in the middle of a crowded room, and the only person on my mind would still be Alexis."
        "I don't know exactly when we became one of those couples that people walk past and tut at for spending all their time kissing."
        "But the reality of the matter is that, when I'm with her, I hardly care."
        hide expression "alexis kiss "+alexis.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != alexis and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_126
        if hero.charm() >= 160 - alexis.love():
            show alexis
            alexis.say "Stop doing that."
        hide alexis
        $ alexis.love += 2
    return

label alexis_fuck_date:
    scene bg bedroom1
    $ alexis.set_flag("sex",1,"permanent","+")
    show alexis
    if not alexis.get_flag_value("sex") >= 2:
        "Reconnecting with Alexis has been an odd kind of experience for me, one that I'd imagined many times in the past."
        "But the most surprising thing is just how little I seem to be able to remember of the girl that I used to know."
        "As well as how different the woman she's become is from the small details that I'm able to recall from back then."
        "It's like discovering new things about someone I thought I knew and meeting an entirely different person all at the same time."
        "And even as I was getting to know Alexis for the second time around and we were feeling each other out, I was always aware of that big question hanging over me."
        "What, exactly, would it be like and probably more importantly, how would I feel the first time we had sex?"
        "Well, let's be honest, it was IF we ended up having sex again."
        "I'm not that cocksure and confident!"
        "But there seems to have been more ups than downs since we started our tentative second attempt at something resembling a relationship."
        "And I don't know if it's the thrill of bedding a former lover on Alexis's part, or that she's mad keen on the guy that I've turned out to be."
        "Either way, we're about to take that next big step and follow up a pleasant date with, I hope, some equally pleasant adult time together."
        "I can also assure you that one of the major things that I don't have an accurate recollection of is just what Alexis looks like naked."
        "This means that I'm totally in the dark as we shut the door to my bedroom behind us and she starts to strip me off with some serious gusto."
        "I return the favour where and when I can, trying to pull off a piece of clothing from what Alexis is wearing."
        "But she always seems to be able to just about twist and turn enough to elude me."
        "Pretty soon I'm totally naked, and she's still looking like she did when we walked in off of the street."
        "Before I can get mad at his blatantly unfair situation, Alexis shoves me in the chest with the flat of her hand."
        "The blow isn't enough to hurt me, but it's more than enough to send me tumbling backwards and onto the unmade bed."
    else:
        "Alexis shoves me in the chest with the flat of her hand."
        "The blow isn't enough to hurt me, but it's more than enough to send me tumbling backwards and onto the unmade bed."
    "I scramble up into a sitting position, about to object..."
    "And it's then that I see the absolutely filthy smile that's spreading across Alexis's face."
    "Still holding my gaze, she begins to pull her top upwards, revealing ever more of her smooth, curving stomach."
    "Well now I feel like a fool - I was about to complain about what turned out to be a private strip-tease, right here in my bedroom!"
    "Alexis winks as quick as a flash before she whips her top off, letting me know that I was right to keep my mouth shut and let her get on with it."
    "As she pulls them free of her top, I see the heavy shape of her breasts moving in sympathy with her arms."
    "They're something that I definitely don't remember, so full and appealing to the eye that I'm sure I simply couldn't have forgotten them."
    "Seeing my eyes widen at the sight of them, Alexis shakes her head in amusement and reaches behind her back to unhook her bra."
    "I swear that they bounce, first down and then back up again as they come free and succumb to gravity."
    "Next she inches down her pants and knickers all at the same time, first one side and then the other until they're bunched up around her ankles."
    "All I can say is that the shape of her legs are well in keeping with her stunning chest."
    show alexis naked blush
    "And her neatly-shaved pussy makes me want to bite my lip in spite of myself."
    alexis.say "I know that you like what you see, [hero.name]..."
    alexis.say "You didn't have to say a word - your little friend went and told on you already!"
    "She comes closer as she says this, casting her gaze down towards my dick, which only now do I see is already painfully erect."
    alexis.say "Aww, look...he's standing to attention for me."



































    "She lays herself across my prone form, belly to belly, and then begins to crawl over me."

    "Alexis only stops when she's straddling my waist and has her back to me so that I can't see what she's doing with my dick."
    menu:
        "Use protection" if hero.has_condom():
            "I can see that Alexis is teasing me now, intent on not letting me know when she intends to let me inside of her."
            "But all the same, I don't want to let the thrill of the moment cloud my judgement and do something we'll both regret later."
            "By stretching my arm out, I can just manage to snatch up a condom from the tray on the bedside table."
            "I toss it to Alexis, who catches it with impressive ease and rips the packet open, before I feel her slide it over my cock."
            $ c = True
            $ hero.use_condom()
        "Don't use protection":
            "Alexis isn't going to let me see what she's doing, and that means I won't know that I'm inside of her until she lets me in there."
            "She's already teased me and got me so unbelievably hot, that I can't think of anything else but actually getting to have her now."
            "Each second that she makes me wait longer feels like a new kind of torture."
            "The only possible relief is to feel myself finally sinking into her."
            $ c = False
    "I can see now why Alexis was so keen to get herself into this particular position before we got to this point."
    "The fact that I can't see a thing of what she's doing save for the motion of her back and buttocks means that I'm constantly guessing just what she'll do next."
    "At first she does nothing more than caress my cock with her hands, hinting that she might not let me inside at all."
    "And then she leans forward and draws the head along the length of her pussy, from the top to the bottom."
    "The sensation is incredible, and I can tell instantly that she's more than slick and ready for me right now."
    "That knowledge only serves to frustrate me even more, as Alexis still refuses to allow me inside."
    "She teases me until I think that I'm going to lose control and simply cum in the palm of her hand."
    "And a sly glance over her shoulder let's her know that's just where she's brought me to."
    menu:
        "Fuck her pussy":
            hide alexis
            show alexis reverse
            if c:
                show alexis reverse condom
            "So only then does she finally raise herself just enough to allow my cock to push against her lower lips."
            "Alexis doesn't have to try hard now, we're both more than ready and her weight means that she takes me in one smooth and sensational movement."
            "The feeling of being inside of Alexis's pussy is incredible, like we're picking up where we left off."
            $ p = True






    "Suddenly, where I'd been kept in suspense for so long, the sense of release and satisfaction is simply immense."
    "I can hear myself groaning with release, uttering words that come totally without conscious effort."
    hero.say "Oh, Alexis...oh, fuck!"
    "She looks back at me once more as she rides my cock mercilessly."
    "The look on her face speaks volumes, as her eyes flash with the exact same kind of ecstasy I can feel in my own body right now."
    "I reach out and take hold of her just below the waist, my hands kneading her buttocks compulsively."
    "Alexis moans in approval, and I respond by squeezing her with more force still."
    "By this point I don't honestly know if I'm trying to make her scream or else drag her down harder onto my cock."
    "All I know is that I couldn't care less in this moment about what Alexis might have done to me in the past."
    "All of the pain and the feelings of betrayal, none of them come close to being as important as what I'm feeling here and now."
    "I feel like every new burst of sensation and pleasure is serving to make me forget about what went before, like it's reminding me of my true feelings for her."
    "That's it, the knowledge that I can't go on any further hits me like an epiphany."
    if p and c:
        "I don't know how close Alexis is to reaching her peak."
        "But right now, all I can think about is the fact that I'm right on top of mine."
        "I feel myself go, and this in turn makes me thrust even more forcefully into Alexis."
        "She almost bucks as she rides my cock now, throwing her head back so that her hair flies this way and that."
        "I can't tell if she came at the same time, as my own head is now buried amongst the pillows, and all I can see is the ceiling."
    elif p and fitness <= 50:
        show alexis reverse pussy
        "Alexis begins to sense that I'm on the verge of cuming, and I feel her try to pull away."
        "Instinctively, my hands shoot out and grab hold of her, preventing any chance of escape."
        alexis.say "Ahh...[hero.name]...you're going to..."
        "It's at that very moment that I lose myself inside of her, my fingers digging into the soft flesh of her buttocks as I do so."
        alexis.say "Oh...oh...[hero.name]...you came inside of me!"
        if (randint(1,3) == 1 or "hung" in hero.skills) and not alexis.get_flag_value("pregnant") and not alexis.get_flag_value("pill"):
            $ alexis.set_flag("pregnant",1)
    elif p:
        menu:
            "Cum inside":
                show alexis reverse pussy
                "Alexis begins to sense that I'm on the verge of cuming, and I feel her try to pull away."
                "Instinctively, my hands shoot out and grab hold of her, preventing any chance of escape."
                alexis.say "Ahh...[hero.name]...you're going to..."
                "It's at that very moment that I lose myself inside of her, my fingers digging into the soft flesh of her buttocks as I do so."
                alexis.say "Oh...oh...[hero.name]...you came inside of me!"
                if (randint(1,3) == 1 or "hung" in hero.skills) and not alexis.get_flag_value("pregnant") and not alexis.get_flag_value("pill"):
                    $ alexis.set_flag("pregnant",1)
            "Pull out":
                "Somehow my common-sense seems to be able to overcome the urge to just keep on going until the inevitable end."
                "At the last moment possible, I take a firm hold of Alexis around the waist and push her forwards whilst pulling myself back."
                "I hear her moan in unconscious disappointment as my cock slides out of her and springs free once more."
                "A split-second later, I finally cum, showering Alexis's back and buttocks."
                "She's left crouching on the bed, panting in exhaustion and covered in my quickly cooling cum."
    else:
        "Somehow my common-sense seems to be able to overcome the urge to just keep on going until the inevitable end."
        "At the last moment possible, I take a firm hold of Alexis around the waist and push her forwards whilst pulling myself back."
        "I hear her moan in unconscious disappointment as my cock slides out of her and springs free once more."
        "A split-second later, I finally cum, showering Alexis's back and buttocks."
        "She's left crouching on the bed, panting in exhaustion and covered in my quickly cooling cum."
    "It's an odd feeling in the aftermath, almost as though I didn't know what to expect once Alexis and I had finally done it together again."
    "There's no sense of anti-climax, just more a stillness and satisfaction that's a surprise after the passion with which we just made love."
    "But maybe that's better than a mad sense of carnal desire, maybe it's a sign that there's more to this than blind passion."
    "I guess that we'll just have to wait and see if I'm right."
    hide alexis
    call alexis_sleep_date_fuck from _call_alexis_sleep_date_fuck
    return

label alexis_sleep_date_fuck:
    scene bg bedroom1
    show alexis naked
    menu:
        "You should leave":
            hero.say "I am done with you and I have to get up early tomorrow, you should leave."
            "The sex was beyond incredible."
            "Frowning a little, Alexis straightens and shrugs, then goes to collect her clothes from where she'd let it fall earlier."
            "She then heads up the stairs."
            $ alexis.love -= 1
            $ alexis.sub += 1
        "You should sleep here":
            hero.say "You can stay and sleep here."
            "I say, my voice a little shaky."
            "We curl up spooning together in bed, drifting toward sleep."
            $ alexis.love += 1
    call sleep from _call_sleep_6
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
