init -1 python:
    Event(**{
        "name":"lavish_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "lavish",
        "girls_conditions": {"lavish":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lavish_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "lavish",
        "girls_conditions": {"lavish":{"contact":"lavish","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(12,13),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lavish_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "lavish",
        "priority":100,
        "girls_conditions": {"lavish":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lavish_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "lavish",
        "priority":100,
        "girls_conditions": {"lavish":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"lavish_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "lavish",
        "priority":100,
        "girls_conditions": {"lavish":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_lavish_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"lavish_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "lavish",
        "priority":100,
        "girls_conditions": {"lavish":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"lavish_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "lavish",
        "girls_conditions": {"lavish":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

label smartphone_lavish_hint:
    "No hints for Lavish yet"
    return

label lavish_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = lavish.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = lavish.get_activity(bye_hour)
    if not activity == lavish.activity:
        if day != game.week_day:
            $ lavish.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ lavish.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "lavish "+bye_outfit
        if activity["activity"] == "sleep":
            lavish.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            lavish.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            lavish.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            lavish.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            lavish.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            lavish.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            lavish.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            lavish.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            lavish.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            lavish.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            lavish.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            lavish.say "I ll go get dressed."
        hide expression "lavish "+bye_outfit
    return

label lavish_cheated:
    show lavish
    "I see Lavish looking at me kissing someone else with envy and lust in her eyes."
    $ lavish.love += 1
    hide lavish
    return

label lavish_greet:
    if not lavish.get_flag_value("greeted"):
        $ lavish.set_flag("greeted",True,1)
        show lavish
        $ result = randint (1,3)
        if result == 1:
            lavish.say "Hello, [hero.name]."
        elif result == 2:
            lavish.say "Hi, [hero.name]."
        elif result == 3:
            lavish.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                lavish.say "Good morning [hero.name]."
            elif game.hour < 19:
                lavish.say "Good afternoon [hero.name]."
            else:
                lavish.say "Good evening [hero.name]."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Lavish."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                lavish.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Lavish."
            elif game.hour < 19:
                hero.say "Good afternoon Lavish."
            else:
                hero.say "Good evening Lavish."
    return

label lavish_kiss:

    scene expression "bg "+game.room
    show lavish
    if lavish.love() + hero.charm() < 80 and not lavish.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        "Really, what else was I supposed to think?"
        "I've caught Lavish gazing at me so many times since she started working with me in the office."
        "Always with those huge, innocent eyes looking at me so intently."
        "And then darting away again the moment that she realises I've noticed her watching me."
        "And the blushes that spread across her cheeks when she does that too!"
        "So when we're alone together, and I feel the time is right - why wouldn't I lean in and try to kiss her?"
        "It's always a gamble when someone's not laid it on the line and told you their intentions."
        "But isn't being prepared to take that leap a good thing?"
        "Well, evidently not in this particular case, as all it earns me is a flat palm meeting my questing lips."
        "She ducks underneath me and twists deftly out of the way."
        "Before I can recover my balance, let alone explain or even think of apologising, Lavish is gone."
        "So there I am, left all alone and wondering how I could have misread her coy glances as badly as I just did."
        "Have I crossed a line with Lavish thanks to what I just tried to do?"
        "Is she on her way to HR right now, setting the wheels in motion for my ultimate downfall?"
        $ lavish.love -= 1
    else:


        $ lavish.set_flag("kiss",1,mod="+")
        if lavish.get_flag_value("kiss") == 1:
            "I feel so self-conscious as I reach out to take Lavish's hand."
            "But as she looks up at me in response, I suddenly feel much of my trepidation being washed away."
            "She's just so different to the other women that I work with."
            "So quiet and retiring that I almost failed to see how utterly beautiful she actually is."
            "Lavish isn't loud and arrogant like Aletta, manipulative like Audrey or needy like Shiori."
            "But the most amazing thing of all is that she actually seems to be genuinely attracted to me."
            "There's no freaky behaviour or emotional bullshit involved either."
            "Tentatively, I reach out and smooth her hair away from her eyes with my other hand."
            "But she surprises me by gently taking hold of it and pressing it to her lips."
            "Encouraged by this show of affection, I lean in and kiss her softly."
            "Lavish sighs happily, returning the kiss with equal tenderness."
            "Only when I feel her arms wrap themselves around me do I dare to kiss her with more vigour."
            "She folds herself into me almost totally, the rest of the world seeming to fade away into nothingness."
            "Really, while I'm holding her and feeling her lips against mine like this, what else is there?"
            "I honestly don't know what turns me on more about her..."
            "The fact that she's finally mine to hold and kiss, or the feeling of her amazing body as she moves against me."
            "Either would be incredible, but both together is almost enough to blow my mind."
        else:
            "I manage to catch Lavish gently around the waist as she walks past me."
            "She's not expecting it, and suddenly finds herself pulled into my arms and looking me in the eye."
            "Her cheeks flush with colour at the surprise of it all, but she's smiling all the same and not fighting me in the slightest."
            "I pause for a couple of seconds, enjoying the sensation of her body pressed against mine and the smell of her hair so close to me."
            "As I finally kiss her, I can feel Lavish knot her hands at the base of my spine and hold onto me."
            "It's such a small gesture to look at, but I know that it's just her own subtle way of returning my affections, of binding herself to me."
            "I really should keep this whole thing brief, but in that moment, she comes alive in my arms."
            "Lavish's tongue darts between my lips, as though she's only now realised how much she wants to be kissed and is afraid of the chance being taken away from her."
            "When I make the mistake of trying to ease off before ending the kiss, she makes a sighing noise, almost like a distressed puppy and tries to press herself on me with yet more intensity."
            "What can I do in the face of that, knowning that she's so keen to keep herself in my arms?"
            "All I can do is return her affections with the same amount of enthusiasm."
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != lavish and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated"
        $ lavish.love += 1
    hide lavish
    return

label lavish_fuck_date:
    $ lavish.set_flag("sex",1,"permanent","+")
    scene bg livingroom
    show lavish
    "We make it back to my bedroom."
    "Her hand is in mine, her delicate fingers laid soft and warm across my palm, with mine curled protectively over them as I use them to lead her through my doorway."
    "The both of us know why we’re here."
    "Reluctantly, I let her go and shut the door behind us, missing the warm of her skin the moment it’s gone."
    "I know it’ll be back."
    "When I turn back around, I see her facing me, her hands trailing up her body to the top button of her shirt."
    show lavish naked blush
    "Lavish locks her eyes on me, watching me from beneath seductively lowered lashes as she tantalizingly undoes her top and then her bra, dropping the both of them aside to the floor."
    "My pulse is racing already as I step forward and cup a hand hungrily to one of her breasts, massaging it against my palm as I use the other hand to pull her forward and nip one of her full lips into mine."
    "She’s willing and eager, kissing me back immediately with a fire that I know I lit in her. Her hands make their way up my back, fingertips pressing into my shoulder blades as we make out and I lead her with careful steps back toward the bed, our mouths never parting."
    "Her tongue glides over mine, slick and sweet, and I feel her draw a brief, cold breath from my mouth in a gasp as I flick my thumb over her pert nipple, eliciting goosebumps over her flesh that drive me wild."
    hide lavish
    show lavish missionary normal
    "The back of her knees hit the bed, and she lays herself down onto it without a word, only a breathless pant as our mouths part."
    "Something’s burning in her eyes as she slides her hands down to her hips and removes the rest of her clothing, making me throb there before her. Her curves, her hips, the silky perfection of her skin makes me almost dizzy."
    "She draws her legs up and spreads them, reaching down a graceful hand to rub a moment over the soft mounds of her pussy."
    "Then, using two fingers, she spreads them, giving me a clear show of the slick, pink folds waiting for me."
    "She’s glistening, almost dripping wet. My heart gives a hard thud in my chest."
    menu:
        "Don't use a condom" if lavish.love >= 175 and lavish .sub >= 75:
            $ CONDOM = ""
        "Don't use a condom" if lavish.love < 175 or lavish .sub < 75:
            "I want her now, just as she is. I don’t think I could wait a single second longer."
            "I undo my jeans and strip down within seconds, ready to pounce on her."
            "But as I take my cock into my hand and step toward her, her lips curl into a wolvish smirk, and she lifts one finger from her wet folds and wags it back and forth."
            "Nuh uh."
            lavish.say "Not yet."
            "She throws me a condom while saying that."
            "I almost groan out loud, but I respect the boundary, quickly catching the condom and sliding it on."
            $ CONDOM = " condom "
        "Use a condom" if hero.has_condom():
            $ hero.use_condom()
            "It’s hard to focus on anything but the flower before me, flushed bright pink and gleaming."
            "My eyes stay locked on it as I strip out of my clothes, a man in a daze."
            "It takes me two seconds flat to retrieve a condom and slide it on."
            "I’m not wasting any time."
            $ CONDOM = " condom "
    "My cock gives an eager, appreciative throb at her presentation as I step forward over her, positioning myself at her entrance."
    hide lavish
    show expression "lavish missionary normal vaginal" + CONDOM
    "A soft, mewling moan escapes her when I press the tip against her clit, guiding it up and down her slick folds for a moment, coating myself in her silky nectar."
    "She’s wanted this from that first moment she laid eyes on me at my cubicle."
    "Her lips part in her flushed, knit-browed panting as she looks up at me with puppy dog eyes that beg for my entrance."
    "I’m more than happy to comply."
    "With a grunt, I slide myself into her, gliding myself deep into her, and she utters a low, musical moan, tilting her head against the bed and letting her eyes roll back before closing."
    lavish.say "Ohhh, yes."
    "She’s breathless already, and I haven’t even thrust."
    "I’m yours."
    hero.say "I know."
    "I slam myself in to the hilt, and she yelps, her hands flying up to her breasts, squeezing them together for me, digging her fingers in deep to her own flesh."
    "I’m taking what’s mine."
    "Unable and unwilling to hold back any longer, I take one of her full thighs in my hand and pull it against my body, using it as leverage as I draw back and slam myself back into her."
    "She’s louder than I thought."
    "I expected reserved and modest from her, but she’s letting loose, full-lunged gasps and moans and yelps as I fuck her, intermittently calling my name."
    "I can tell she’s dreamed of this moment for a while."
    "To be honest, so have I."
    "I throb deep inside of her as I drive the both of us further and further into the throes of our pleasure, pounding her with every ounce of strength I have, losing myself as I watch her tits bounce in her hands,"
    "her tongue lolling out occasionally in the pure pleasure against her full bottom lip as she tries futilely to catch her breath."
    "I’m not going to last much longer like this, but it’s obvious that neither is she."
    "Her moment comes first, her fingernails digging first into her breasts, then aimlessly down to her hips, one moving up to her mouth to press against her bottom lips as the other clutches desperately into my bedsheets."
    "I feel her spasming around my cock, twitching, and I know she’s losing her mind even before she tells me so."
    show expression "lavish missionary orgasm vaginal" + CONDOM
    lavish.say "Yes... Yes! I’m cuh… cum… cumming…"
    "Her gasps reach a feverish pitch and she yelps, her legs latching forward and around me as her back arches sharply, both hands slapping down into my mattress to dig in deep as she shudders, grinding her hips greedily against my thrusts as she rides out her orgasm on my pulsing rod."
    "I’m about there with her, especially with her squirming, screaming, and drawing me in deeper, deeper into her as she cums."
    if not CONDOM:
        show expression "lavish missionary orgasm vaginal creampie"
    "It takes only a few more solid thrusts before I bust, too, groaning and gripping the flesh of her thighs as I pump my load deep inside of her, her spasming walls milking what feels like every last drop out of me."
    "Her breaths are shuddered whimpers as I pull out, collapsing onto the bed next to her."
    "Within seconds she’s magnetized to my side, the soft skin of her palm sliding across my chest as her beautiful face nestles in to my shoulder."
    "Her full, long lashes are closed, resting daintily against her cheeks, her expression that of peaceful, dreamy bliss."
    "I feel it flood through me, too, at the sight, and, sighing contentedly, I curl my arm around her and let my eyes fall closed, too."
    scene bg bedroom1
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
