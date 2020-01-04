layeredimage bg studio:
    if game.hour >= 20 or game.hour <= 5:
        "studio_night"
    else:
        "studio_day"

init -2 python:
    Room(**{
        "name":"studio",
        "hours":(18,23),
        "days": "35",
        "display_name": "Recording studio",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "music": "music/TeknoAXE/simple_metal.mp3",
        "valid":False,
        "outfit":"casual"
        })

    Activity(**{
        "name": "practice_band",
        "duration": 2,
        "game_conditions": {
            "room":["studio"],
            "min_grooming":1,
            "min_fun":0,
            "min_hunger":3,
            "min_energy":3,
            "flagmin_band":2
            },
        "icon":"guitar",
        "fun": 2,
        "display_name": "Practice",
        "label": ["practice_band"],
        "once_day":True
        })

    Event(**{
        "name": "kleio_anna_showdown",
        "priority": 500,
        "label": ["kleio_anna_showdown"],
        "duration": 0,
        "game_conditions":{"flag_dateinprogress":False},
        "girls_conditions": {"anna":{"present":True,'valid':True,"flagmin_sex":3},"kleio":{"present":True,'valid':True,"flagmin_sex":3}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "date_set_up",
        "priority": 500,
        "label": ["date_set_up"],
        "game_conditions":{"done":"kleio_anna_showdown","flag_dateinprogress":False},
        "girls_conditions": {"anna":{"present":True,'valid':True, "min_love":170},"kleio":{"present":True,'valid':True, "min_love":170}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "first_gig",
        "priority": 500,
        "label": ["first_gig"],
        "duration": 4,
        "game_conditions":{"activity":["bandpractice"],"flageq_gigready":True},
        "do_once":True,
        "quit": True
        })

label kleio_anna_threesome:
    scene bg livingroom
    "The taxi drops the three of us off outside my house, and I try to look confident as I let the girls inside."
    "But the truth is that I'm already sweating at the realisation that I didn't check beforehand that nobody else would be in tonight."
    show anna date at left
    show kleio date at right
    "We enter the living room, Anna and Kleio already giggling and making suggestive comments as they pinch and tickle me in what should be an agreeable manner."
    "I put my finger to my lips, in the vain hope of keeping them quiet for a moment."
    hero.say "Hello...anyone home?"
    $ rooms = ["secondfloor","kitchen","pool", "bedroom1","bedroom2","bedroom3","bathroom"]
    if not bree.get_room() in rooms and not sasha.get_room() in rooms:
        "All I get in answer is silence, allowing me to let out a sigh of relief."
        anna.say "What's up, [hero.name], did you think someone was home?"
        kleio.say "Doesn't matter either way - I'm gonna make you guys come so hard they'll hear it all the way down the block!"
    elif not sasha.get_room() in rooms:
        "Much to my horror, Bree's head appears around the livingroom door."
        hide kleio
        hide anna
        show bree
        bree.say "Hi, [hero.name], have you - oh, hello to your friends as well!"
        hero.say "We're...erm...going to my room, just so you know...in case you hear anything wierd."
        "Bree can't help sniggering as she closes the door, knowing full well what's going on between the three of us."
        hide bree
    elif not bree.get_room() in rooms:
        hide kleio
        hide anna
        show sasha
        "I'm left gaping as Sasha opens her bedroom door and smiles at me."
        sasha.say "Oh, hey, [hero.name] - been out at the..."
        "She pauses as she sees her bandmates in a state of dishevelled amusement behind me."
        sasha.say "Is this a band thing...or a side-project you three are working on behind my back?"
        "Anna and Kleio both burst into filthy laughter, making me think I'm the only one nervous about doing this thing."
        sasha.say "Don't look so paranoid, [hero.name] - they already warned me about it!"
        "Before I can protest, Anna and Kleio barge me into my room."
        hide sasha
    else:
        hide kleio
        hide anna
        show sasha at left
        show bree at right
        "Bree's head appears around the livingroom door, and then Sasha's from behind the door to her bedroom."
        "My mouth starts moving, but there's nothing coming out as I realise both my housemates are seeing me come home with two other girls."
        bree.say "Hey, [hero.name] - are we having a party?"
        sasha.say "Or a band practice?"
        show kleio date
        kleio.say "No and no again...but you might want to put some headphones on pretty soon!"
        "Both Bree and Sasha chuckle knowingly as they disappear back into other rooms."
        "I'm left wondering if I'm the only person in the world that's not so blase about the idea of a threesome."
        hide sasha
        hide bree
    show kleio date at left
    show anna date at right
    "The girls almost pull me off of my feet as they each take one of my hands and lead me into my bedroom."
    scene bg bedroom1
    show kleio date at left
    show anna date at right
    "I try to collect myself and say something, but they give me a look that shuts me right up."
    "As Kleio pushes me down onto the bed and Anna starts to unzip my flies, I get the distinct feeling they've planned this beforehand."
    "Anna soon has my pants and underwear down around my ankles, stripping me completely below the waist with characteristic eagerness."
    "Kleio, on the other hand, takes her time removing my top, running her hands over me as she does so and even giving me the occasional kiss as she goes."
    anna.say "Oh wow, Kleio - come look at this!"
    kleio.say "Well hello there, little [hero.name]...I think he likes us, Anna!"
    "Anna's already kneeling on the floor in front of me, and now Kleio slides down to kneel beside her."
    "Both girls are looking up at me now, fingers reaching out to tap my rapidly stiffening cock."
    "Their touches send it wobbling like a fleshy Jack-in-the-Box, much to their amusement."
    kleio.say "Wait a minute, Anna - we're all equals here, so let's get on an even footing."
    anna.say "Huh?"
    show kleio naked
    "Without explaining herself to Anna, Kleio strips off her leather jacket and then pulls her cropped top off over her head."
    "As she unhooks her bra and frees her petite breasts, Anna giggles in realisation and follows her lead."
    show anna naked
    "Moments later, her much larger and heavier breasts are also bared before me, and both girls are naked to the waist."

















    "I was never too big on classical mythology, but I think I know how an ancient Greek guy might have felt when he was presented with the sirens right now."










    "I take a deep breath and reach out for one of the two girls before me."
    menu:
        "Fuck Kleio":












            $ n = "Kleio"
            $ b = "Anna"
            "Good girls may go to heaven, but bad girls win for me everytime, and I pull Kleio towards me while I lay on my back."
            "But she comes of her own volition, refusing to pulled and instead crawling onto of me like an alley cat on heat."
            "Kleio looks into my eyes, and her almost mocking come on makes me thrust in her a second later."
            hide kleio
            hide anna
            show threesome ak fuck
            "Kleio almost purrs with satisfaction as I fill her up and mounts me like she was a bitch, her tightness making me go harder and stronger than I would normally dare."
            anna.say "Hey, guys...don't forget about me!"
            show threesome ak suck
            "If Kleio's a feral alley cat, then Anna's a mischeivous she takes my cock out of Kleio and into her mouth."
            "Kleio beigns to play with her petite breasts, whilst grinning wickedly at making Anna pleasure us both at once."
            "Anna begins to kiss the base of my shaft, gently at first and then with more intensity."
            "As she work her way upwards, she starts to caress and then fully lick at my length with her tongues."
            show threesome ak fuck
            "After a while she angle my cock toward, then inside Kleio's pussy."
            "Kleio starts to groan and buck from our combined efforts, and her movements mean that I can feel myself about to come."
    menu:
        "Cum inside [n]'s pussy":
            "We're sweating so much from the exertion and shared bodyheat that [n] almost slips out from under me."
            show threesome ak fuck cum
            "But I hold her in place, feeling the wave of my orgasm finally take hold."
            "The sensation inside of [n] pushes her over the edge too, and she cums a moment later."
        "Cum inside [b]'s mouth":
            "I grip the back of Anna's head with one hand as tremors start to rock through me, and I push deeper; she makes no protest though her eyes tear up a bit."
            show threesome ak suck cum
            "Groaning, I gasp for breath as my cock twitches and throbs, forcing her to swallow quickly as pleasure sends spurts of hot cum straight down her throat."
            "It takes several moments for my climax to pass, and when it does, I drop back to the bed, panting, trying to catch my breath."
            "Dimly, I feel Anna licking at my cock lightly before she pulls away."



    hide threesome
    show anna naked at left
    show kleio naked at right
    "As all three of us lay there, bathed in sweat and slippery from our collective efforts, I start to feel wierdly proud of what we've just done."
    "Everyone, even Kleio, has a satisfied smile on their face, and seems to be happy enough simply to keep quiet and enjoy the afterglow."
    "Slowly we end up laid together on the bed, curled up almost as close as we were whilst having sex a moment before."
    "Suddenly, Anna jumps at the sound of someone snoring loudly."
    anna.say "Ooh - what's that noise!"
    hero.say "I think we tired Kleio out!"
    "Anna and I gaze over at the sight of Kleio, dead to the world and making a sound like a sawmill."
    anna.say "Aww, doesn't she look sweet when she's asleep?"
    "I just chuckle quietly, but I can't help admitting that she's right."
    hide anna
    hide kleio
    $ renpy.call_in_new_context("sleep")
    return

label kleio_and_anna:
    $ game.set_flag("sashathreesomedelay",True,duration=7)
    $ DONE.append("kleio_and_anna")
    scene bg highclassrestaurant
    $ s = 0
    "A big part of me still can't quite believe where I am right now with Kleio and Anna."
    "That after figuring out I was seeing each one behind the other's back, they've decided that they're going to share me."
    "On the one hand, I'm giddy at the prospect of being involved in what you might call a 'three-way dance'."
    "But I'm also in uncharted territory here, and it's actually quite terrifying."
    "We all decide that we should start slowly, with dinner at a new and pretty hip Chinese restaurant in the centre of town."
    "I find myself waiting on the sidewalk, checking the time while I wait for the girls to arrive."
    show anna date at right
    anna.say "Hi!"
    show kleio date at left
    kleio.say "Hey, guy!"
    "That they've arrived together should make me instantly paranoid, but instead I'm too busy admiring the sight of them both."
    "Anna's wearing colourful tights that make her look like an achingly hot little pixie and a t-shirt that shows off her impressive chest."
    "Kleio, on the other hand, is wearing a short tartan skirt, fishnets and a cropped top under her leather jacket, and looks like the perfect punk princess."
    hero.say "Hi girls...you look amazing tonight."
    if hero.equipment["clothes"] and hero.equipment["clothes"].name in ["fancy clothes"]:
        "Anna and Kleio take in that I'm wearing a dress shirt, pants and shoes."
        kleio.say "Well, aren't we mister fancy pants tonight!"
        anna.say "Aww, don't be mean, Kleio...[hero.name] went all out for us - it's totally sweet."
        kleio.say "Whatever you say - but if someone thinks you're our pimp, I'm totally playing up to it for the laughs."
        $ kleio.love -= 2
        $ anna.love += 2
    elif hero.equipment["clothes"] and hero.equipment["clothes"].name in ["military fatigues",]:
        "Anna and Kleio take in that I'm wearing a polo shirt and khaki pants."
        kleio.say "Come here straight from the cube farm, did you?"
        anna.say "I think I forgot what Sasha told me you did in the day time, but now I think it involved IT, right?"
        kleio.say "Don't worry - maybe the restaurant will need their WiFi fixing, and you'll be the hero of the day!"
        $ kleio.love += 2
        $ anna.love -= 2
    elif hero.equipment["clothes"] and hero.equipment["clothes"].name in ["leather jacket"]:
        "Anna and Kleio take in that I'm wearing a leather jacket, band t-shirt and ripped jeans."
        anna.say "Ooh...I LOVE that band!"
        kleio.say "One of us, one of us, one of us!"
        "I can't help grinning, realising that my choice of attire makes us look like a trio set against the rest of the normal, mainstream world."
        $ kleio.love += 5
        $ anna.love += 5
        $ s += 2
    else:
        kleio.say "Whoa, [hero.name] - way to push the boat out and make a girl feel special!"
        anna.say "Don't listen to her, [hero.name]...we're already bandmates, friends and...well, a bit more than that too."
        anna.say "It's not like you're making a first impression or anything."
        $ kleio.love -= 5
        $ anna.love -= 5
        $ s -= 1
    "We walk inside and the waiter on the door checks our reservation and then shows us to our table in a plush booth."
    "The waiter is a young and pretty handsome Asian guy, and I can feel him checking Anna and Kleio out in silence."
    "His obvious admiration makes me feel all the more flushed at my sheer luck to be out with both these girls at once."
    "Supplied with menus, the waiter asks me to order drinks for the table."
    menu:
        "Order fruity cocktails":
            hero.say "Three Raspberry Cosmopolitans, please."
            anna.say "Ooh, that sounds delicious...and strong."
            kleio.say "Yeah, but I'm not sure they're the only fruity thing around here!"
            $ anna.love += 5
            $ s += 1
        "Order beers":
            hero.say "Three beers, please."
            kleio.say "Hell yeah, and keep 'em coming too!"
            anna.say "Aww, those cocktails looked all nice and colourful."
            $ kleio.love += 5
            $ s += 1
        "Order spirits":
            hero.say "Three vodkas, with ice."
            anna.say "Ooh, I can't remember the last time I had vodka...mainly 'cos of the amount of vodka I had then."
            kleio.say "Geez, - you don't mess about...and I like that in a man!"
            $ kleio.love += 2
            $ anna.love += 2
            $ s += 1
        "Order tap water":
            hero.say "Jug of tap water and three glasses, please."
            kleio.say "Wow, check out mister big spender here!"
            anna.say "Well, it's only the start of the night...maybe [hero.name] likes to start off slow and hit his stride later on?"
            $ kleio.love -= 5
            $ anna.love -= 5
            $ s -= 1
    "The waiter returns with our drinks, and it's time to order the food."
    "The menu's so large and complex that I'm baffled, and so to save face, I suggest that we just order one of the set banquets for three."
    anna.say "Great idea, [hero.name] - that way we can try a little of everything."
    kleio.say "Suits me...too much of one thing's bound to get boring sooner, rather than later."
    "The food soon arrives, and I'm surprised by the sheer number of dishes covering the table, unsure of where to start."
    "I can't help but see the parallel between the meal and my new relationship with Anna and Kleio."
    menu:
        "Reach for a knife and fork":
            "I begin to eat with a knife and fork, as I've never gotten the hang of chopsticks."
            kleio.say "Jeez, [hero.name] - when in Rome, and all that crap!"
            "Kleio laughs, letting me know that she's fucking with me for the fun of it."
            "Anna coughs nervously and leans in closer before speaking."
            anna.say "Don't feel bad...I could never use them either!"
            $ kleio.love += 2
            $ anna.love -= 2
        "Reach for chopsticks":
            "I snatch up some chopsticks and get stuck into the food."
            kleio.say "Whoa...look at the sophisticated eater we're out with tonight!"
            "Kleio's laugh and the twinkle in her eye tells me that she's just fucking with me for fun."
            anna.say "[hero.name], you're a natural!"
            anna.say "Can you show me how to do it...or maybe you could feed me a few morsels?"
            $ kleio.love -= 2
            $ anna.love += 2
    "As time goes on, the date seems to be going pretty well."
    "I'm really enjoying the banter between Anna and Kleio as they loosen up and let go a little."
    "If this is what a real threesome is like, then it feels just the same as going out with good friend...only with the prospect of group sex at the end of it all."
    "Suddenly I feel the sensation of something touching my left thigh."
    "Glancing to my left, I see Anna, flushed from the food and drink, smiling invitingly as she squeezes my left leg with her free hand."
    "A second later, I feel a similar sensation on my right thigh."
    "My head spins around to see Kleio, licking her lips suggestively, as she pinches at my right leg, as close to the groin as she can manage."
    menu:
        "Try to calm both girls down":
            "I feel hot and not a little panicked at the prospect of being stroked by both girls in a public place."
            hero.say "Wow...I don't know about you two, but I feel like my pants are fit to burst right off of me!"
            "I overemphasize my words, trying to glance down at my groin to get the true meaning of my words across."
            "Kleio raises a quizzical eyebrow, seeming to catch my meaning."
            "But Anna looks dejected, clearly thinking that she's being rebuffed."
            anna.say "Aww...I was still kinda hungry."
            kleio.say "Anna, you ditz - he's saying you can take it home...in a DOGGY BAG!"
            "Anna takes a moment to understand, and then blushes, laughing a little too loudly in aroused amusement."
            $ kleio.love += 2
            $ anna.love += 2
            $ s += 1
        "Return Anna's attentions":
            "Maybe it's the alcohol, or the nerves doing the thinking for me...but I suddenly want to see Anna even more aroused and turned on in a public place."
            "I turn to face her, slipping my hand up the inside of her thigh at the same time."
            "The feel of the tights she's wearing and the heat of her thigh is only made all the more amazing by the look on her face as she begins to melt."
            "I reach the top of her thigh, and just stroke the beginnings of her crotch as lightly as I can."
            "Anna's cheeks are visibly red and she's almost panting now, making me feel she could be made to beg like a dog, right there in the restaurant."
            "I glance across at Kleio, and see that she's wearing a slight frown at being ignored."
            "But I also notice that her free hand is hovering somewhere around her own groin, suggesting that being neglected is making her long for the balance to be redressed."
            $ kleio.love -= 5
            $ anna.love += 5
        "Return Kleio's attentions":
            "I feel like Kleio's rebellious spirit is infecting me too, making me forget the consequences as I instinctively return her advances."
            "I turn my head to look her in the eye, my right hand roughly grabbing at the hem of her short skirt and climbing upwards like a giant spider."
            "But it's me that gets a surprise, as the tips of my fingers discover that she's already warm and slick to the touch."
            "And that she's not actually wearing any panties tonight."
            "I can't keep the shock off of my face, and Kleio's wicked look in return makes me want her more than ever."
            "At last I manage to tear my gaze off of Kleio and look at Anna, more from the need to calm myself down than genuine concern for the other girl present."
            "Anna looks downcast at the attention that I'm giving to Kleio, but somehow the sulkiness in her expression only makes her look all the more desirable."
            $ kleio.love += 5
            $ anna.love -= 5
        "Return both girls' attentions" if hero.charm >= 50:
            "I'm torn as I look from one of the girls to the other, wanting to sample the sweetness of Anna and the tart allure of Kleio all at once."
            "Thinking I must be mad, I put a hand on the closest thigh of each girl, then begin to squeeze and slide my way upwards."
            "The contrast of Anna's pantyhose and Kleio's fishnets feels incredible against the warmth of their thighs."
            "I steal glances at both their faces, seeing that they're gazing at one another, visibly turned on at the feeling of being played with by the same man."
            "A moment later, I have both their skirts hitched up just enough to stroke them between the legs."
            "Anna feels incredible through her tights and panties, but I realise with some genuine shock that Kleio has outdone her by not wearing any at all."
            $ kleio.love += 5
            $ anna.love += 5
            $ s += 2
    "An unsubtle cough breaks the spell, and I look up to see the waiter standing by our table."
    "All three of us snap out of it and try to make it look like we're just more than a little drunk and sleepy, rather than worked into a lather and heading for a threesome later on."
    "I have no idea if the waiter realised what was going on, or how our relationship is supposed to work."
    hero.say "Erm...could be get the cheque, please?"
    menu:
        "Offer to pick up the bill" if hero.money >= 150:
            "When the bill arrives, I decide to make a gesture and pay for the meal."
            hero.say "Don't worry, guys - it's on me."
            anna.say "Aww, thanks, [hero.name]...what a gentleman."
            kleio.say "Whoopie doo...my knight in shining armour!"
            $ kleio.love += 2
            $ anna.love += 2
            $ s += 1
        "Claim to have no money":
            "When the bill arrives, I realise that I've forgotten my wallet."
            hero.say "Ah, shit...I must've left my wallet at home!"
            anna.say "Oh no, [hero.name]...we'll get this one, and you make it up next time."
            kleio.say "Fuck me, [hero.name] - you must have a mind like a goddamn Swiss cheese!"
            $ kleio.love -= 2
            $ anna.love -= 2
            $ s -= 1
        "Suggest they split the bill" if hero.money >= 50:
            "When the bill arrives, I remember that we're all supposed to be equals in this relationship, even when it comes to paying for stuff."
            hero.say "Let's go Dutch."
            anna.say "Sounds fair to me."
            kleio.say "Fine...I don't need to be coddled by anyone."
    if s >= 3:
        "With the bill settled, we call a cab and head back to my house, hoping to pick up where we so recently left off."
        call kleio_anna_threesome from _call_kleio_anna_threesome
    return


label date_set_up:
    "During our training session, Kleio and Anna come talk to me."
    show kleio at left
    show anna at right
    kleio.say "You are taking us to dinner."
    hero.say "... ok ..."
    python:
        choices = []
        if game.hour == 20 or (game.hour == 14 and game.week_day in [6,7]):
            choices.append(("Now",("now",0)))
        if game.hour <20:
            choices.append(("Today",(game.days_played,game.week_day)))
        if game.week_day != 7:
            choices.append(("Tomorrow",(game.days_played+1,game.week_day+1)))
            start = 1
        else:
            choices.append(("Tomorrow",(game.days_played+1,1)))
            start = 2
        if game.week_day + 2 <=7:
            
            for i in range(game.week_day+2,8):
                
                choices.append(("Next "+game.get_day_str(i),(game.days_played-game.week_day+i,i)))
        if game.week_day > 1:
            
            for i in range(start,game.week_day):
                
                choices.append(("Next "+game.get_day_str(i),(game.days_played-game.week_day+i+7,i)))
        day, week_day = renpy.display_menu(choices)
        if day == "now":
            renpy.call("kleio_and_anna")
        else:
            if (week_day in [6,7] and not game.days_played == day) or (week_day in [6,7] and game.days_played == day and game.hour < 14):
                choices = [("Afternoon",14),("Evening",20)]
                hour = renpy.display_menu(choices)
            else:
                hour = 20
            
            
            
            
            s = "Let's do this "
            if day == game.days_played and hour == 20:
                s += "tonight."
            elif day == game.days_played and hour == 14:
                s += "this afternoon."
            elif day == game.days_played+1 and hour == 20:
                s += "tomorrow night."
            elif day == game.days_played+1 and hour == 14:
                s += "tomorrow afternoon."
            elif hour == 20:
                s += "next "+game.get_day_str(week_day)+" evening."
            elif hour == 14:
                s += "next "+game.get_day_str(week_day)+" afternoon."
            hero.say(s)
            hero.set_appointment(day,hour,"kleio_and_anna")
    anna.say "This is gonna be so fun."
    return

label first_gig:
    $ hero.activity.set_flag("canceled")
    $ game.set_flag("bandpractice",5,mod="+")
    "The Battle of the Bands was now literally a week away, and I thought things couldn't get any more tense."
    "But then, out of the blue, Sasha turned up at the practice room and dropped a bombshell."
    show sasha at right
    sasha.say "Grab your shit, guys - we've got a gig!"
    show anna at left
    anna.say "Huh?"
    hide anna
    show kleio at left
    kleio.say "What the hell?!?"
    hero.say "Sasha, what on earth do you mean, not an actual gig?"
    sasha.say "No, not a real gig, a pretend one in front of an audience of cardboard cut-outs!"
    sasha.say "Of course I mean a real one."
    "Kleio made enough noise as she stormed around the room to almost cover up her swearing."
    "Anna did the opposite, staying sat on her drumstool in silence, but her expression betrayed her trepidation at the thought of the surprise gig."
    sasha.say "Come on, people - this is the perfect opportunity to put all that practice into...well, practice!"
    sasha.say "If we can't play a gig now, then how can we play one in a week's time?"
    "Sasha looks at me expectantly, and then I realise Kleio and Anna are too."
    "I realise that, while Kleio's thrown her usual tantrum and Anna's gone characteristically quiet, I still haven't said my piece in the issue."
    if not game.get_flag_value("bandcrossdress"):
        menu:
            "Try to be positive":
                hero.say "Sure it's a shock, but carpe diem, and all that shit - let's do it!"
                "Sasha seems glad to have my support, but Kleio and Anna still don't look convinced."
                hero.say "You two might not believe in yourselves, but I do - Kleio, Anna, you've owned everything we've practiced today."
                hero.say "I say we grab this gig by the scruff of the neck and shake it till it screams for mercy!"
                $ anna.love += 5
            "Try to remain neutral":
                hero.say "TBH, Sasha, I think it sucks a little you dropping this on us."
                "Sasha looks a little wounded at the dig, clearly hoping for more support from me."
                hero.say "I'm not shitting on you, or the idea though - I think we can do it, and that we probably should."
                hero.say "I just wish we'd had some warning so that we could at least prepare."
                $ sasha.love += 5
            "Be negative":
                hero.say "Fuck sake, Sasha - as if we haven't got enough shit on our plates already?!?"
                "Sasha looks surprised at the way I tear into her, and then her face darkens with her mood."
                hero.say "All of us are wrapped up in practicing, but now we've got to snap out of it and deal with a live audience too?"
                $ kleio.love += 5
    else:
        "Suddenly Kleio and Anna stop their complaining and start to give me sly glances and knowing winks, laughing to each other."
        "Sasha's mood lightens too when she realises what's got them so amused."
        hero.say "Wait a minute - you don't expect me to do the gig in drag, seriously?"
        sasha.say "It's supposed to be a dress rehearsal, [hero.name]."
        kleio.say "Yeah, so in your case, that makes it a drag rehearsal too!"
        "I'm already panicking about cross-dressing in front of complete strangers, but at least my discomfort seems to have smoothed things over with the girls for the moment."
        $ kleio.love += 5
        $ anna.love += 5
        $ sasha.love += 5
    sasha.say "Whatever to all that, we need to get our shit downstairs and into the van - RIGHT NOW!"
    "For a moment at least the nerves and recriminations are forgotten as we scurry around gathering up instruments and gear."
    "In less than fifteen minutes, we're packed, panting and sweating into the van with everything we should need to play the gig."
    hide sasha
    show anna at right
    anna.say "Oh, Sasha - you didn't say where we're going."
    hide kleio
    show sasha at left
    sasha.say "The Leadmill - some guy on my course knows the manager, and he was desperate for a band to fill in at short notice."
    hide anna
    show kleio at right
    kleio.say "Wow, tough crowd...I heard tell one band got their singer pulled off stage and roughed up by the crowd 'cos they thought he sucked."
    hero.say "WHAT?!?"
    show sasha
    sasha.say "Don't have a cow, [hero.name]...that's just an urban legend."
    hide sasha
    hide kleio
    if game.get_flag_value("bandcrossdress"):
        hero.say "So you say, Sasha...but if they do that kind of thing to people that suck, what are they gonna do when they realise I'm a dude in pantyhose and a stuffed bra?"
        sasha.say "I already said don't worry about it, the lights will be so bright that even you'll look hot in a dress."
    "With Kleio behind the wheel of the van, we make it to the venue with time to spare, but also almost as shaken from the journey as we were from the prospect of the surprise gig itself."
    "I have to change into my gig clothes in the back of the van during the journey, wrestling with my rock-chick outfit while tumbling around the loose equipment."
    "Mercifully, the venue has hired a couple of stagehands, and they unload our gear while we troop to a tiny dressing-room with our band's name written in marker-pen on what looks like a napkin and stuck to the door."
    "A member of backstage staff clues us in that we're replacing the second support band for a group I've never heard of, but the girls seem to know, as they nod with enthusiasm."
    "Time seems to shoot by in a blur, and before I know it, we're standing in the wings, waiting to be ushered onstage."
    if game.get_flag_value("bandcrossdress"):
        show kleio
        kleio.say "Hello there...we are the Deathless Harpies, and we're gonna make your ears bleed!"
        "Any lingering worries I have about being in drag are pushed aside as I start playing."
        "The urge to perform takes over, and somehow the clothes that I'm wearing start to feel weirdly liberating."
        "I have no clue if the audience know I'm a man or a woman, and that ambiguity frees me to make the music do the talking."
        "My enthusiasm seems to spread to the girls as well, and they up their game accordingly, with audible results."
        "When we wrap up the set and step off stage, only then do I remember what I'm wearing and start to come back down to earth."
        if game.get_flag_value("bandpractice") >= 50:
            $ a = 1
        elif game.get_flag_value("bandpractice") >= 25:
            $ a = 2
        else:
            $ a = 3
    elif game.get_flag_value("bandpractice") >= 50:
        $ a = 1
        show kleio
        kleio.say "Hello and how the hell are you doing?"
        kleio.say "We are the Deathless Harpies, and we want to entertain you!"
        "I don't know where Kleio's words come from, but they seem to set the audience off straight away."
        "The rest of the set is a haze, as everything just clicks, and we become a tight-knit unit, more than the sum of its parts."
        "Adrenaline takes over, and everyone plays like their lives depend upon it."
        "When we come off stage, we're soaked and exhausted, but grinning like four clowns at the cheers from the audience."
    elif game.get_flag_value("bandpractice") >= 25:
        $ a = 2
        show kleio
        kleio.say "We are the Deathless Harpies, and...we...we're here to rock."
        "Kleio stumbles a little as she introduces us, and her nerves quickly spread to the rest of us on stage."
        "We start off unsure of ourselves and it shows, but somehow the mixed reaction of the audience spurs us on."
        "Sasha, Kleio, Anna and I start to remember our cues, and our individual efforts inspire us to drag ourselves together as a band."
        "By the time the set ends and we troop off stage, we're not celebrating, but nods and smiles say we know that we salvaged something."
    else:
        $ a = 3
        show kleio
        kleio.say "Hello all of you bitches and male chauvanist pigs!"
        kleio.say "We are the Deathless Harpies, and we're the next big thing!"
        "Kleio's words go down with the crowd like a lead balloon, earning us shocked stares and even hurled abuse before we even start to play."
        "The negative emotion infects the rest of us, and it's like we've somehow forgotten what our instruments are actually for."
        "Every song sees at least one of us fuck up, and by the end of the set we almost run off stage to keep from hearing the boos aimed at us."
    hide kleio
    "Everyone keeps quiet as we walk back to the dressing room and the stagehands load our gear back into the van."
    "We're all clearly wired from the gig, Sasha and Kleio looking like they want to share their opinions on how things went."
    "But somehow we all keep up an unconscious silence until we're alone in the van and driving back to the practice room."
    if a == 1 and game.get_flag_value("bandcrossdress"):
        show sasha
        sasha.say "So, some good, some bad - plenty that we can work on in time for the competition."
        show sasha at left
        show kleio at right
        kleio.say "Way to ignore the elephant in the van, Sasha!"
        "I frown, not knowing what Kleio's talking about, but then I hear Anna giggling beside me."
        hide kleio
        show anna at right
        anna.say "She means you, [hero.name]...you know that you forgot to get changed, right?"
        "I look down in genuine surprise, realising for the first time that I'm still dressed in drag."
        hero.say "Shit...I must have forgotten, you know - in the fuss after the gig!"
        anna.say "Whatever you say - don't worry, I think you look adorable like that!"
        hide anna
        show kleio at right
        kleio.say "Yeah, with a swamp-donkey like you around, we all look ten times better by default!"
        sasha.say "Don't listen to her...I think you pulled it off well, and it kinda added something to the band as well."
        $ kleio.love += 5
        $ anna.love += 5
        $ sasha.love += 5
    elif a == 1:
        show sasha
        sasha.say "See, you guys - I told you we needed this!"
        show kleio at right
        show sasha at left
        kleio.say "Geez, Sasha...don't let it go to your head or anything!"
        hide kleio
        show anna at right
        anna.say "Wow, Kleio's not going for the jugular - that means she thinks you're right, Sasha!"
        "I can't help but laugh at Anna's ability to interpret Kleio's rudeness and guess her deeper meaning."
        "In that moment, I feel a real fondness for all three of the girls, seeing their redeeming qualities shine through."
        hero.say "I'm just gonna come out and say it - you girls were amazing...I think we all were."
        $ kleio.love += 5
        $ anna.love += 5
        $ sasha.love += 5
    elif a == 2:
        show sasha
        sasha.say "I can't say we couldn't have done better - but I think, on balance, it was more good than bad."
        show sasha at left
        show kleio at right
        kleio.say "Huh...well, yeah...I guess you're right."
        kleio.say "Just remember to warn us next time you do something like that, okay?"
        hide kleio
        show anna at right
        anna.say "Ah well, back to the grind for us all!"
        "Everyone's tired, and there are some seriously bruised egos, but I can't help smiling at the fact we still managed to pull through in the end."
        $ kleio.love += 2
        $ anna.love += 2
        $ sasha.love += 2
    else:
        show sasha
        sasha.say "I'm just gonna say it, Kleio - what the fuck was that shit about at the start of the set, huh?"
        show sasha at left
        show kleio at right
        kleio.say "Do I have to run everything I say past you now?"
        sasha.say "If you're gonna spout that kind of BS, then maybe you need to!"
        show anna
        anna.say "Well, I think that..."
        "Anna's words are lost in the mix, as Sasha and Kleio tear into each other over the disastrous gig."
        "I feel that I should jump in, defend Anna or at least plead for them to stop."
        "But I'm feeling so tired and down from the shitty performance, that I just end up staring out of the window at the passing streetlights."
    "An odd, tired silence falls over us all after that, and no one speaks until the van pulls up outside the practice room."
    "I guess we're all just mulling over our thoughts on the way the gig went, and what it'll mean when the day of the competition finally comes around."

    $ game.room = "pub"
    return

label kleio_anna_showdown:
    scene expression "bg "+game.room
    "I hear footsteps coming towards me..."
    show kleio at left
    show anna at right
    "A quick glance over my shoulder reveals Kleio and Anna, both making a beeline for me."
    "Kleio has her usual nonchalant look about her, but by now I can read the sarky look of confidence on her face, and know that she's after something intimate from me."
    "Anna, as usual, is the complete opposite, almost bouncing towards me like an enthusiastic puppy, clearly buzzing and wanting to share that energy with me as soon as possible."
    "I smile at them both, while internally grimacing."
    "This could be awkward, as I'm sure neither knows that I've also been screwing the other at every available opportunity."
    anna.say "Hey, You are great at practice those days."
    anna.say "Almost like a guitar wizard...you know - the kind that has a magic wand!"
    "She winks in a way that's as close to lascivious as Anna gets, coming off more as cute and needy, making reference to the pillow talk we made during our last sexual encounter."
    kleio.say "God, Anna - why don't you just paw at his crotch like a Chihuahua on heat!"
    kleio.say "Didn't anyone ever tell you that some guys prefer a feisty alley-cat to a little lap-dog?"
    "She cocks her head and smiles wickedly, knowing that I can't help but know she's referring to the time we fucked in an alleyway after a night out drinking together."
    anna.say "Huh, well - he didn't mention anything like that when he gave me..."
    hero.say "Woah, slow down there, Anna!"
    kleio.say "He certainly wasn't complaining when I let him..."
    hero.say "Hang on a second, Kleio!"
    "It's a little like watching one of those videos online, where someone's smashed something and then played the footage back in slow motion."
    show kleio angry
    show anna angry
    "Confusion spreads across both of the girl's faces, followed soon afterwards by realisation, and then the inevitable horror and outrage."
    "As one, they round on me, arms crossed and faces filled with indignation."
    hero.say "Girls, I can explain..."
    if "kleio_say_preg" in DONE:
        kleio.say "For fuck's sake you even knocked me up!"
        "I can read some king of distress in Anna's eyes."
    else:
        anna.say "Can you?"
        kleio.say "This should be fucking good!"
    "They look at me expectantly, but I can only shrug and sigh."
    hero.say "No...I guess I can't explain it."
    hero.say "I'm sorry...I guess I just found myself having fun with two mindblowing girls at once, and I couldn't help myself."
    "Both of the girls still look visibly upset and angry, but my honesty has at least softened them a bit."
    "I go to speak, but Kleio cuts me off."
    kleio.say "You shut the hell up!"
    kleio.say "You said your piece, and this is all down to you thinking with your dick, so thanks for that!"
    kleio.say "As usual, the solution's gonna be down to someone with a vagina."
    "Anna doesn't add to Kleio's verbiage, but she nods in solemn silence to show her agreement."
    "So I keep my peace, waiting for the girls to decide my ultimate fate."
    "Kleio and Anna put their heads together, speaking loud enough for me to hear, but with their backs turned to remind me I'm not the one making the decisions on this matter."
    show kleio normal
    show anna normal
    if (kleio.love < 150 or kleio.get_flag_value("lesbian") < 10) and not (anna.love < 150 or anna.get_flag_value("lesbian") < 10):
        kleio.say "You know me, Anna - I'm a pretty open-minded kind of girl."
        kleio.say "But I've been hurt too many times and too hard in the past to let this prick do it to me all over again."
        show anna sad
        anna.say "I'm sorry, Kleio - but I really like him."
        "Snorts and rolls her eyes in frustration at Anna's words."
        anna.say "You know, Kleio, you talk about how sex is just two people coming together."
        anna.say "So how come you crap on me for still wanting [hero.name]?"
        kleio.say "Anna, that's not the same thing, I..."
        anna.say "Why is it different when it's me?"
        anna.say "So what if he's had sex with you too?"
        anna.say "We've all had sex with lots of people...and I like having it with him."
        show anna happy
        kleio.say "Okay, Anna - if that's the way you feel, you can keep him, with my blessing!"
        $ kleio_love_max = 0
        $ kleio_love = 0
        $ HIDDEN.append("kleio")
    elif not (kleio.love < 150 or kleio.get_flag_value("lesbian") < 10) and (anna.love < 150 or anna.get_flag_value("lesbian") < 10):
        show anna sad
        anna.say "I can't share a guy with someone else, Kleio."
        anna.say "Maybe if it was a girl, it'd be different...but I haven't been with a guy for so long...and it felt special."
        kleio.say "I hear that, Anna...thing is...I really like this prick...don't ask me why!"
        "Anna blushes, clearly recalling the time we spent together in bed."
        show anna normal
        anna.say "What's up, Kleio - are you too much of a tough bitch to admit that you like to feel his cock inside of you?"
        "Both Kleio and I are shocked to hear Anna talk like that in public, but I manage to keep quiet...unlike Kleio."
        show kleio
        kleio.say "Jesus, Anna - you're not taking any prisoners tonight, are you?"
        anna.say "I'm just being honest, Kleio...can't you be honest for once, too?"
        kleio.say "Alright, alright...fuck sake, I admit it - I like this prick...and this prick's prick."
        show anna happy
        "Anna smiles, clearly taking some consolation from having extracted such a confession from Kleio."
        $ anna_love_max = 0
        $ anna_love = 0
        $ HIDDEN.append("anna")
    elif (kleio.love < 150 or kleio.get_flag_value("lesbian") < 10)  and (anna.love < 150 or anna.get_flag_value("lesbian") < 10):
        show kleio sad
        show anna sad
        kleio.say "I had no idea he was fucking you too, Anna."
        anna.say "Same here...sorry."
        kleio.say "Hey, don't beat yourself up - that jerk was the only one of the three of us that knew!"
        kleio.say "I know I get on my high-horse about sex sometimes, but that doesn't feel right when it's a friend like you."
        anna.say "Yeah, I feel pretty much the same...maybe if it was some other girl neither of us knew, it'd be different."
        show anna happy
        show kleio happy
        "Get the distinct feeling that, whatever fun the girls had with me, they're closing ranks as their friendship wins out."
        kleio.say "We're still friends, right?"
        anna.say "Yeah, I guess so...what's a prick between friends?"
        kleio.say "Exactly -fucking nothing!"
        "The girls exchange a pinkie shake and ignore me with deliberate pleasure in doing so."
        $ kleio_love_max = 0
        $ kleio_love = 0
        $ anna_love_max = 0
        $ anna_love = 0
        $ HIDDEN.append("anna")
        $ HIDDEN.append("kleio")
    else:
        kleio.say "You know what, Anna - your playing's gotten much better since that prick came along with his prick!"
        anna.say "Speak for yourself, Kleio - your guitar's not the only thing that's been better tuned thanks to [hero.name] as well!"
        "Suddenly they're both looking at me, and I know how a wounded gazelle under the gaze of two lionesses must feel."
        show kleio
        kleio.say "This is the twenty-first century, Anna...and we're pretty good friends, aren't we?"
        show anna blush
        anna.say "Yeah, Kleio, we are...and good friends share things, right?"
        kleio.say "Sure they do...things like make-up, clothes, vibrators...and a decent dick, when one finally shows up."
        anna.say "Oh, believe me...I know how long that takes to happen!"
        "Anna's giggling uncontrollably now, enjoying my discomfort."
        "Kleio looks equally amused, but something in her eyes tells me she's already imagining the possibilities that might lie ahead."
        show kleio happy
        show anna happy
        kleio.say "Like I always say, Anna - sex is just an encounter between two people...or three."
        anna.say "Well, if he's going to screw other girls, then I'd rather it be you...and me!"
        "I can't help gulping in trepidation and more than a little excitement at the prospect."
        "It seems like, without a care for my own feelings, the girls have decided that they're going to keep me!"
        $ game.set_flag("bandharem",1)
    "No one addresses the metaphorical elephant in the room ..."
    "But I can see knowing glances passing between Kleio and Anna, an unspoken code that I'm not to be let in on."
    "For my own part, I can't honestly decide if what's happened is for good or bad."
    "But I'm sure it'll have serious consequences for me before too much time has passed."
    hide kleio
    hide anna
    return

label practice_band:
    "We practice together."
    if not game.get_flag_value("nextgig"):
        $ game.set_flag("nextgig",True,game.days_played+41,"gig_ready")
    $ game.set_flag("bandpractice",10,mod="+")
    return

label gig_ready:
    $ game.set_flag("gigready",True)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
