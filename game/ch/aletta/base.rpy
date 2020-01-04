init -1 python:
    Event(**{
        "name":"aletta_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "aletta",
        "girls_conditions": {"aletta":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"aletta_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "aletta",
        "girls_conditions": {"aletta":{"contact":"aletta","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(10,11),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"aletta_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "aletta",
        "priority":100,
        "girls_conditions": {"aletta":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"aletta_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "aletta",
        "priority":100,
        "girls_conditions": {"aletta":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"aletta_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "aletta",
        "priority":100,
        "girls_conditions": {"aletta":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_aletta_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"aletta_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "aletta",
        "priority":100,
        "girls_conditions": {"aletta":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"aletta_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "aletta",
        "girls_conditions": {"aletta":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_aletta_hint:
    $ story = aletta.get_flag_value("story")
    if story == 0:
        if hero.charm < 30:
            "I need to look better."
        else:
            "I heared that Aletta is often smoking during breaks."
    elif not aletta_love == aletta_love_max:
        "I should get to know Aletta better."
    elif story == 1 and hero.charm < 40 or story == 2 and hero.charm < 50 or story == 3 and hero.charm < 60:
        "I am not charming enough"
    elif story in [1, 2, 3]:
        "I should go to work."
    else:
        "I reached the end of Aletta's story for now."
    return

label aletta_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = aletta.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = aletta.get_activity(bye_hour)
    if not activity == aletta.activity:
        if day != game.week_day:
            $ aletta.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ aletta.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "aletta "+bye_outfit
        if activity["activity"] == "sleep":
            aletta.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            aletta.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            aletta.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            aletta.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            aletta.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            aletta.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            aletta.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            aletta.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            aletta.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            aletta.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            aletta.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            aletta.say "I ll go get dressed."
        hide expression "aletta "+bye_outfit
    return

label aletta_cheated:
    show aletta
    "I see Aletta looking at me kissing someone else with envy and lust in her eyes."
    $ aletta.love += 1
    hide aletta
    return

label aletta_greet:
    if not aletta.get_flag_value("greeted"):
        $ aletta.set_flag("greeted",True,1)
        show aletta
        $ result = randint (1,3)
        if result == 1:
            aletta.say "Hello, [hero.name]."
        elif result == 2:
            aletta.say "Hi, [hero.name]."
        elif result == 3:
            aletta.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                aletta.say "Good morning [hero.name]."
            elif game.hour < 19:
                aletta.say "Good afternoon [hero.name]."
            else:
                aletta.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Aletta."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                aletta.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Aletta."
            elif game.hour < 19:
                hero.say "Good afternoon Aletta."
            else:
                hero.say "Good evening Aletta."
    return

label aletta_kiss:
    scene expression "bg "+game.room
    if aletta.love() < 25 and not aletta.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show aletta
        "It can be hard to get a handle on just how a girl as strong-willed and forceful as Aletta is feeling from one moment to the next."
        "And it's harder still to be sure of what she wants me to do as a man when we're together."
        "With a less intimidating girl, I probably wouldn't think twice about taking a chance on being wrong."
        "But there's always that sense of fear with Aletta, worrying that doing the wrong thing at the wrong time could result in disaster."
        "All of which is made so much worse by the fact that she's already got me so desperate to take things to the next level with her."
        "This all comes to a head when I feel the insatiable urge to lean forward and try to give Aletta what I hope will be our first kiss."
        "I feel like the moment is right, everything feels right - at least from my point of view."
        "The first indication I get to tell me that I'm very wrong is the feeling of something firm and hard thumping me in the middle of the chest."
        "My mouth still stupidly poised to kiss Aletta, I look down in surprise to see her hand placed in the centre of my ribcage."
        "A moment later, the other hand is pushed into my face, turning my head away from her and puckering my lips at the same time."
        "And there I have perhaps the most neat evidence of my miss-reading Aletta, as well as the consequences for doing so."
        $ aletta.love -= 5
        $ aletta.sub -= 5
        hide aletta
    elif not aletta.get_flag_value("kiss"):
        hide aletta
        $ aletta.love += 5
        show expression "aletta kiss "+aletta.get_clothes()
        "I don't want to find that I've mistimed this, picked the wrong moment and misread the cues that I think Aletta's been sending me just now."
        "But I just can't keep sitting on the feelings that she inspires in me any longer, and so to hell with the consequences."
        "At some point in my life, I need to actually stand up and make an effort to grab what I want, even if it might mean missing when I do so."
        "Normally I'd try to gently lean in to kiss a girl, with subtlety and a light touch being required."
        "But while I know that Aletta's certainly not made of steel and stone, she's also wilful and stubborn as well."
        "So this is why I choose to make the bold (and possibly also disastrous) move of cupping her cheeks in my hands."
        "Even as I do this, I can already see the look of surprise and then sudden indignation spreading across Aletta's face."
        "Well, it's now or never!"
        "I pull her closer and kiss her, full on the lips and with no attempt to be gentle."
        "I feel her twist and her muscles tense instinctively, but I choose to ignore these phsysical cues and press on."
        "For a moment I fear that I've totally misjudged the situation."
        "But then I almost literally feel Aletta melt in my arms."
        "It's not that the fight goes out of her, rather than the same strength and passion is suddenly channelled into our embrace instead."
        "Now her arms are wrapping around me and she's returning the kiss with a passion that almost overwhelms me!"
        hide expression "aletta kiss "+aletta.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag_value("kiss") or g.get_flag_value("sex")) and g != aletta and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_63
        $ aletta.set_flag("kiss",1,"permanent","+")
    else:
        hide aletta
        $ aletta.love += 1
        show expression "aletta kiss "+aletta.get_clothes()
        "If I was under the impression that breaking the ice with Aletta and having our first kiss together was going to be like bursting a damn, then I was proven wrong pretty quickly."
        "The ice queen of the office didn't seem about to melt quite that easily, and she was keen on the idea of rationing kisses even after that."
        "But then there is something to be said for keeping things a little special, and Aletta was a revelation when she did give into her urges."
        "We quickly got into the habit of ducking into doorways and behind obstacles that would hide us sight, and then she would all but pounce on me."
        "Aletta was no prude, just careful to preserve the image that she had spent so long cultivating, that of being an iron bitch."
        "It was well hidden, but her insides were metal too - only they were liquid metal, hot, glowing and able to burn you up in a second."
        "If I wasn't forceful enough when we kissed, Aletta would become the one to make the demands and push until she got what she wanted."
        "She would claw, slap and even bite at me if I were not giving her what she wanted, quickly enough or in sufficient amounts to satisfy her."
        "But you can get used to cuts and bruises around the mouth, and you can always deal with the pain."
        "Especially when it's being inflicted right along with the kind of kisses that Aletta gives to me."
        hide expression "aletta kiss "+aletta.get_clothes()
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag_value("kiss") or g.get_flag_value("sex")) and g != aletta and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_62
        $ aletta.set_flag("kiss",1,"permanent","+")
    return

label aletta_fuck_date:
    $ aletta.set_flag("sex",1,"permanent","+")
    scene bg bedroom1
    show aletta
    "Aletta isn't putting on too much of an act when she strides around, being a forceful bitch at the office throughout the working day."
    "She shows the exact same amount of dominance in the bedroom too, practically dragging me in through the door and beginning to strip me off the moment it closes behind us."
    "I try to return the favour, in between catching sudden and intense kisses that she plants on me at random instants and totally without warning."
    "It feels like all of Aletta's haughtiness and arrogance outside of the bedroom has suddenly been transformed into an insatiable hunger inside of it."
    show aletta underwear
    "And the more layers that I manage to strip off of her, the more aroused and determined Aletta seems to become."
    "But it's when I finally pull off her top and scramble to unhook her bra that she really starts to get delightfully aggressive with it."
    show aletta naked
    "Almost as soon as her sizable breasts are released to stand proud upon her chest, Aletta thrusts them towards me, literally pressing them against me."
    aletta.say "Don't keep me waiting, [hero.name]..."
    aletta.say "I want to feel your hands all over me...starting right here!"
    "I'm more than happy to oblige, taking one of the heavy orbs in each of my hands."
    "As I begin to squeeze and caress her breasts, Aletta almost desperately pulls of the rest of her clothes."
    "I can't keep from staring at her nipples as they stiffen beneath my fingers and move under my thumbs."
    "But at the same time I can hear Aletta starting to pant and moan, as my playing with her makes her want more."
    "She shoves me backwards so that I collapse onto the bed, and then follows me down onto it."
    "I seem to fall back with Aletta atop me the whole time, rather than having her land upon me."
    "And she's clambering over me the whole time, trying to keep a hold."
    if aletta.get_flag_value("collared"):
        "I reach out instinctively and grab hold of the lead dangling from Aletta's collar."
        "She instantly feels the first yank that I give it, stopping her efforts to take the upper hand."
        "Instead, she sits up on her haunches, straddling me just below the waist and awaits further instructions."
        hero.say "That's a good girl, Aletta."
        hero.say "Enthusiasm's all well and good, but you need to wait for my orders first."
        "Aletta looks a little downcast, though she nods her head in submission."
        show aletta blush
        aletta.say "Yes, Master...I'm sorry, Master."
        hero.say "Apology accepted, Aletta."
        hero.say "I'm going to fuck you now, Aletta - would you like that?"
        aletta.say "Oh, yes, Master - I'd like that very much!"
    elif aletta.get_flag_value("sex") == 1:
        "I can't recall how many times I've day-dreamed about fucking Aletta in the past."
        "While watching her bending over the photocopier or crossing her legs in the middle of a boring meeting."
        "Pressing her up against the glass of my office window and making her scream for mercy."
        "But nothing could have prepared me for the experience of having her climb atop me, naked and intent upon having her way with me."
        "I can't help but run my hands up and down her pale-skinned body, tracing her curves."
        "Likewise I keep trying to kiss and nibble at her erect nipples as her breasts sway invitingly above me."
        aletta.say "[hero.name] - I want you to fuck me now."
        aletta.say "And I want you to fuck me hard."
        aletta.say "Have you got that?"
        "What can I possibly do, other than nod frantically and try to do as I'm told?"
    else:
        "Aletta entwines her fingers with mine, and we begin to play a game of each trying to overpower the other."
        "She tries to hold me down, while I try to push upwards and take her nipples in my mouth as she dangles them over me."
        "At the same time, I can feel the moments when the head of my now stiff cock rubs against her lips."
        "She's already slick and I can sense the desire in her each and every time we tease ourselves in this way."
        aletta.say "Ah...[hero.name]...I want you inside of me..."
        aletta.say "Please...don't make me wait for you!"
    "All I can feel right now is the heat of Aletta's slick pussy as it presses against my cock."
    menu:
        "Fuck her pussy":
            $ p= "p"
            show aletta cowgirl
            "It'd be just as easy to slip by dick into Aletta's ass, she's already so well lubricated with sweat."
            "But her pussy just seems to be calling out to me right now, and it's not something that I'm going to ignore."
            if hero.has_condom():
                menu:
                    "Use a condom":
                        $ c = True
                        $ hero.use_condom()
                        "At the last moment, I remember to reach out and grab a condom from the ashtray on the bedside table."
                        "I hand it to Aletta, and she nods without saying a word as she tears open the packet."
                        "I can't what she's doing as she reaches down to slip it over my cock."
                        "But the feeling is more than ample compensation for wearing the thing as she wriggles around and takes me inside of her."
                    "Don't use a condom":
                        $ c = False
                        "My mind's not able to focus on anything apart from the amazing feeling of Aletta's slick crotch as she slithers around atop me."
                        "All it takes is one or two subtle moves on her part, and she has me just where she wants me."
                        "I suppose it's a happy coincidence that's right where I want to be right now too."
                        "With a little twist of her waist that's translated into a movement of her buttocks, Aletta sinks down onto my cock."
            else:
                $ c = False
                "My mind's not able to focus on anything apart from the amazing feeling of Aletta's slick crotch as she slithers around atop me."
                "All it takes is one or two subtle moves on her part, and she has me just where she wants me."
                "I suppose it's a happy coincidence that's right where I want to be right now too."
                "With a little twist of her waist that's translated into a movement of her buttocks, Aletta sinks down onto my cock."
            "Don't take this the wrong way, but Aletta's pussy is a lot like the girl herself."
            "It's impressive and more than a little intimidating at first."
            "But once you get into it, you discover a sensuality that's just as intense hiding beneath."
            "Aletta lowers herself slowly onto me, moaning a little more with each successive inch that enters her body."
            "She's tight, gripping me like a fist at times, but that just makes the sensation all the more intense and enjoyable."
            "Once she's taken me as deep into her as possible, she leans forwards, so that my cock is almost horizontal."
            "Then she begins to move back and forth, slowly at first, but with increasing speed as she uses me to get herself off."
            "Aletta's heavy breasts are being dragged up and down my chest the whole time, their nipples stroking my skin as they go."
            "I hardly have to move a muscle, as Aletta's doing enough to make me pant from the sheer pleasure on her own."
            show aletta cowgirl cum
            "So I keep my hands occupied by stroking her thighs and squeezing her firm buttocks as she works herself towards her climax atop me."
        "Fuck her ass" if aletta.sub >= 75:
            $ p = "a"
            $ c = False
            show aletta cowgirl
            "Maybe it's the devil in me, but as soon as I get the notion of taking Aletta up the ass, I can't think of anything else."
            "I just have to see what the expression on that haughty, arrogant face of hers will look like."
            "So as she reaches down to line my cock up with her pussy, I reach out and grab hold of her wrist."
            "She tries to fight me, but I'm just that bit too strong for her, and I manage to force her hand backwards by the exact amount needed."
            "And then I thrust with the entirety of my weight behind the effort."
            "I know that I've hit the target more from the expression that explodes onto Aletta's face than actually feeling my cock go up her ass."
            "At first it's shock at the sensation, then comes indignation, followed by a wave of embarrassment."
            "But then, finally, her face melts into an almost delirious expression of pleasure."
            show aletta cowgirl cum
            aletta.say "Oh...oh...[hero.name]..."
            aletta.say "You're in my ass!"
            "I can feel the muscles clenching in protest, squeezing my cock in a way that only makes me want to push still further in."
            hero.say "Tell me how it feels, Aletta?"
            "I've begun to thrust in and out of her now, meaning that Aletta can't help but writhe as I fuck her ass."
            show aletta cowgirl ahegao
            aletta.say "It...it feels...incredible!"
            hero.say "Do you like it, Aletta?"
            hero.say "Do you like having my cock up your ass?"
            "She moans again, as I push harder."
            aletta.say "Yes...yes..."
            hero.say "Tell me what you like, Aletta."
            aletta.say "I...I like having your cock up my ass..."
            aletta.say "Please...don't stop...fuck my ass harder!"
            "The combination of being inside of her and hearing those words from her is almost too much for me."
            "I can feel myself cuming a few moments later."
    "I bite my lip and try to remember where I am and what I'm doing."
    "But all I can feel is the approaching climax."
    if p == "p":
        if c:
            "With nothing to hold me back, I feel myself let go inside of Aletta."
            "She makes the moment that much more intense by cuming a second later herself."
            "It's almost too hard to hold onto one another, with us bathed in each other's sweat."
            "But somehow we manage to cling together and ride it out with our faces pressed together, side by side."
        elif not c:
            menu:
                "Cum inside":
                    "I'm no more than seconds away from cuming when I realise that Aletta seems to be struggling with me."
                    "With no way to tell if she's reaching her own peak or trying to separate herself from me, I choose to hold onto her."
                    "I cum no more than a heartbeat later, feeling myself burst inside of Aletta and not moving until it's all over."
                    aletta.say "[hero.name]...you...you came inside me - without a rubber!"
                    "I'm somehow more worried about the tone of her voice than the reality of what I just did."
                    "As I honestly can't remember hearing even a hint of fear in Aletta's voice before this moment."
                    if (randint(1,3) == 1 or "hung" in hero.skills) and not aletta.get_flag_value("pregnant") and not aletta.get_flag_value("pill"):
                        $ aletta.set_flag("pregnant",1)

                "Pull out" if hero.fitness >= 25:
                    "Somehow I still have the presence of mind to pull out before I cum inside of her."
                    "But she's not going to make it easy for me, as Aletta is effectively pinning me down with her entire body."
                    "I wrestle with her for a few seconds, all the time expecting to cum at any second."
                    "Mistaking my efforts for some kind of final embrace, Aletta playfully grapples with me, frustrating my efforts."
                    "In the end I'm forced to twist sideways, casting her off me as I slip out of her and cum at the same instant."
    else:
        "Still burning with shame and arousal, Aletta casts her head back as I cum deep inside of her ass."
        "I can't see her face, but the evidence is clear that she's almost overwhelmed by the sensation."
        "One hand kneads and massages her breasts as if to release some of the pent up energy."
        "The other slides down to her pussy and begins to stroke away in earnest for much the same reason."
    hide aletta
    show aletta naked
    "Aletta collapses into a panting heap, falling half across me as she does so."
    "I don't have the energy to turn her over, and so I do my best to turn our mess of slippery limbs into an embrace."
    "For once, Aletta is still and utterly silent, and I can only assume that she's utterly satiated."
    "And exhausted too - as she slowly begins to make a curious noise that I take a while to identify as snoring."
    "Deep, long and satisfied - Aletta snores a little like a bustling sawmill."
    "Not that I'm complaining, as I quickly discover that I find the sound quite soothing."
    "And it's making me feel sleepy too..."
    hide aletta
    call aletta_sleep_date_fuck from _call_aletta_sleep_date_fuck
    return

label aletta_sleep_date_fuck:
    scene bg bedroom1
    show aletta naked
    aletta.say "[hero.name], what would you say to me staying the night with you?"
    menu:
        "No":
            hero.say "Ah...I don't think that'd be a good idea..."
            hero.say "We both have work tomorrow, and coming in together would look a bit weird."
            "I want Aletta to stay, but I'm also not ready to handle everyone in the office knowing we slept together!"
            "Aletta tuts in a disapproving manner and begins to pick up her clothes."
            aletta.say "If that's what you think's best, I won't force myself on you!"
            "She raises an eyebrow at me and shakes her head before walking out."
            $ aletta.love -= 3
        "Yes":
            hero.say "Are you kidding, Aletta?!?"
            hero.say "I'd love you to say!"
            "A look of triumph and satisfaction spreads across Aletta's face as she wraps herself around me like an amorous python."
            aletta.say "Why, thank you, [hero.name]...I promise you won't regret it."
            "I can only wonder at that Aletta plans to do to back those words up."
            "But for now, it's enough to know that I've made her happy as she curls up against me to sleep."
            aletta.say "Good night, [hero.name]."
            hero.say "Good night to you too, Aletta."
            "I fall asleep soon after, unable to keep from nestling my head into the comfortable pillow of her breasts."
            $ aletta.love += 3
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
