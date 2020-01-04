init python:
    Event(**{
        "name": "morgan_event_01",
        "label": ["morgan_event_01"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"flag_female":0, "room":["date_cinema"]},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "morgan_event_02",
        "label": ["morgan_event_02"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"flag_female":0, "room":["pub"], "done":"morgan_event_01"},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name":"morgan_init",
        "label": ["morgan_init"],
        "girls_conditions": {"morgan":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "morgan_give_christmas",
        "label": ["morgan_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"morgan":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "morgan_give_birthday",
        "label": ["morgan_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"morgan":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "morgan_give_valentine",
        "label": ["morgan_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"morgan":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "morgan_pregnant_flag",
        "label": ["morgan_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"morgan":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "morgan_preg_talk",
        "label": ["morgan_preg_talk"],
        "duration": 0,
        "girls_conditions": {"morgan":{"flagmin_pregnant":6, "flag_toldpreg":False, "present":True}},
        "game_conditions":{"flag_dateinprogress":False, "flag_female":0},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "morgan_fix",
        "label": ["morgan_fix"],
        "duration": 0,
        "conditions": ["'morgan_event_02 in DONE'"],
        "do_once":True,
        "quit": False,
        })

label morgan_fix:
    $ morgan.set_flag("nodate", False)
    $ morgan.set_flag("nokiss", False)
    return

label morgan_event_02:
    "I guess it's down to the law of attraction, or something similarly weird and unknowable working away silently behind the scenes."
    "But when I bump into Jack in the pub a day or so later, my equally random encounter with Morgan is still very much on my mind."
    "Jack looks his usual self, upbeat and untroubled as he smiles at the sight of me and stops in his tracks."
    show jack normal
    jack_say "Hey, [hero.name] - how you doing, man?"
    hero.say "Not too bad - and you?"
    "Jack gives me one of his characteristic nonchalant shrugs and snorts a little."
    jack_say "You know me...as good as I can be, right?"
    "We chat about everything and nothing for a couple of minutes, and then I drop my titbit of nostalgic news."
    hero.say "Hey, you'll never guess who I bumped into at the cinema the other night!"
    jack_say "Don't tell me...it was Ozzy Osbourne?"
    "I give Jack a withering look, and he holds up his hands in surrender."
    jack_say "Okay, okay, Captain Serious - who did you see at the cinema the other night?"
    hero.say "Morgan - you remember the dude, right?"
    "Jack looks at me a little oddly as he nods."
    jack_say "Yeah, of course I remember Morgan."
    jack_say "Little younger than us, used to follow you around like your shadow at school."
    hero.say "That's the guy."
    hero.say "I bumped into him on a date a couple of nights ago."
    "Jack keeps nodding as I go on, but now he's kind of looking at me with narrowing eyes."
    "It's as though something's puzzling him more and more as I speak."
    "Whatever it is, I try to ignore it and press on with my account of the trip to the cinema."
    hero.say "Anyway, he's looking good - had a girl with him that was really pretty hot too!"
    "Jack realises that I've finished delivering my story and it's now time for him to offer a response."
    "He tilts his head to one side, clearly considering his words carefully before speaking."
    jack_say "Dude, seriously - we're adults now, so you need to drop all that stuff we used to joke about back when we were kids!"
    "Of all the responses I could have imagined, that might just be one of the most unexpected."
    "I look at him blankly, genuinely not knowing what he's talking about."
    jack_say "It was funny when we were messing around in the playground, man."
    jack_say "But you really should let it go now!"
    hero.say "Jack...seriously, what in the hell are you even talking about?"
    "Jack looks at me like he's having to explain why I should wash my hands after using the bathroom."
    jack_say "Calling Morgan a dude...dude!"
    jack_say "I know she was always a tomboy when we were kids."
    jack_say "But if she's gay or bi or something like that now, you need to respect that."
    jack_say "Keeping on calling her a guy just isn't cool."
    "My expression is still blank, and I feel like I've just stepped into a strange, alternate reality."
    hero.say "Jack...Morgan's a guy, he's always been a guy for as long as we've known him!"
    hero.say "Are you telling me he had a sex-change or something?"
    jack_say "Erm, no, [hero.name]...Morgan's always been a girl - well, now I guess she's technically a woman."
    "I feel like I've been staring at one of those magic eye pictures for years, always thinking that I knew what it depicted."
    "But now someone's told me to take a step forwards and to the left, revealing that I'd been looking at it from the wrong angle the whole time."
    hero.say "Morgan's a girl?!?"
    "Jack's expression is showing genuine concern now, and he leans forward to put a steadying hand on my shoulder."
    jack_say "Dude, please tell me that you haven't just realised, this very moment, that Morgan was always a girl?"
    "I'm genuinely stunned, left with nothing to say."
    "All I can do is nod slowly."
    "Jack laughs uproriously, not really helping the situation all that much."
    "But how can I blame him?"
    "If the roles were reversed, I'd no doubt find it as amusing as he does."
    jack_say "Wait a minute...didn't you...yes, yes you did!"
    "Oh god, what's he remembered now?"
    jack_say "You remember when we all thought Morgan had that crush on you, back in high school?"
    "I can feel my stomach already beginning to churn at the mention of the subject he's about to dredge up from our collective past."
    jack_say "We all thought it was pretty cool, but you...you were all weirded out by the idea."
    hero.say "Jack..."
    jack_say "Yeah, everyone thought you were creeped out at the idea because she was a friend or because of the age difference."
    hero.say "Jack, please..."
    jack_say "It never made sense before now."
    hero.say "Jack, please don't say it..."
    jack_say "No, no...it was because you thought she was a guy, wasn't it?"
    jack_say "Oh, dude - that's so funny!"
    jack_say "After all this time...I finally know what that was all about!"
    hide jack
    "Well, there's an episode from my youth that I thought was pretty much buried and forgotten about."
    "Now it looks like the whole thing's been dug up, had a bolt of lighting run through it and reanimated like Frankenstein's Monster!"
    "Jack and I talk for a little while longer, but despite my best efforts, I simply can't change the subject."
    "In the end we say goodbye and go our separate ways, with him still chuckling away at my expense."
    "Jack quips that he hopes to see Morgan before me, just so that he can tell her the whole embarrassing story and see her reaction for himself."
    "While I nod and laugh as best I can manage, I sincerely hope that I'm the one to see her first."
    "But I have no idea what I'm actually going to say to her, if and when I actually do see her again."
    $ morgan_love_max = 120
    $ if "morgan" in HIDDEN: HIDDEN.remove("morgan")
    $ morgan.set_flag("nodate", False)
    $ morgan.set_flag("nokiss", False)
    return

label morgan_event_01:
    $ date_girl = game.get_flag_value("dateinprogress")
    "It was supposed to be nothing more than an evening out at the local multi-plex cinema, watching the latest big-budget superhero movie."
    "The whole decision process must have taken [date_girl.name] and I less than a couple of minutes to chew over and agree to."
    "Tickets bought on my phone, Uber booked the same way to take us there and back again - nothing more to it."
    "And all seemed to be going to plan, until we walked into the cavernous lobby and I saw something that instantly caught my eye."
    show morgan casual
    "I've always been one to notice dyed hair, even in passing, and want to take a second glance."
    "It's not a massive thing for me, like a fetish or anything that serious."
    "But I do think it's one of those little things that can get your attention and add an element of interest to a person's appearance."
    "Though the exact reason that this person caught my attention wasn't just because they had dyed hair."
    "It was actually more on account of the fact that I was sure I'd seen that exact shade of electric blue somewhere before."
    hide morgan
    show expression date_girl.id
    date_girl.say "Hey, [hero.name], what's up?"
    hero.say "I thought I just recognised someone...over there."
    hero.say "Yeah, that's them alright!"
    "I make to weave through the crowd and towards the person in question, [date_girl.name] following close behind me."
    hero.say "Hey...hey, Morgan!"
    hide expression date_girl.id
    show morgan casual
    "At first the familiar figure hears me calling, but doesn't seem to see me for the bodies still between us."
    "They turn around, looking this way and that for the person calling their name."
    "Just as they turn to face my general direction, the crowd parts enough for them to pick me out."
    morgan.say "[hero.name]...is that you?"
    hero.say "Yeah, you bet it is!"
    hero.say "How are you, man?"
    "For all that I'm happy to see Morgan, I'm not sure the same is true in reverse."
    "Morgan's face looks more confused and uneasy than pleased to have bumped into an old school friend at random."
    morgan.say "Oh, I'm good...I guess!"
    "Morgan shifts uncomfortably, even more so when [date_girl.name] steps up to my side and nudges me in the elbow."
    hero.say "Oh, right - Morgan, this is [date_girl.name]."
    hero.say "[date_girl.name], this is Morgan - he's one of the guys I used to hang out with at school."
    show morgan casual blush
    "For some odd reason, this statement seems to embarrass Morgan, who flushes red and begins to say something."
    "The words are drowned out, however, as a girl hovering close by (who I now realise must be Morgan's own date) suddenly starts chuckling loudly."
    "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
    "Morgan seems to regain a enough composure to introduce the chuckling girl, but her name doesn't lodge in my memory for as much as a second."
    "I'm more concerned with the odd way in which Morgan is behaving, wondering if there was any reason I could recall for it."
    "Had I done or said something back in the day that I'd forgotten all about?"
    "What could be so bad that Morgan would still be nursing a grudge over it?"
    "Especially if had no memory of it whatsoever!"
    "Whatever the case, I can sense the mood becoming ever more awkward, and so I make my apologies and claim our film is about to start."
    morgan.say "Oh, yeah...our's too!"
    hero.say "Good to see you again, Morgan."
    hero.say "We should meet up for a drink or something, man."
    hero.say "You know, catch up with each other - make it a guy's night out?"
    morgan.say "Uh, okay...I guess we could do that."
    hide morgan
    "Weirdly, I see Morgan's date, giggling away at us again."
    "I can't quite put my finger on it, but I'm sure that the girl knows what's making Morgan edgy and bugging me at the same time."
    "Try as I might, I can't figure it out, or stop myself from taking an instinctive dislike to her because of that same reason."
    "As we walk off and find the screen where our film is being shown, I find myself talking about Morgan to [date_girl.name]."
    "Most likely I'm unconsciously trying to distance myself from the memory of his annoying date with more agreeable ones about Morgan instead."
    show expression date_girl.id
    hero.say "I can't believe we just bumped into that guy at random."
    hero.say "It's been years since I saw him last."
    "Every time I make a statement about Morgan, [date_girl.name] seems to look at me in a strange manner."
    "It's almost like I think that I'm speaking in English, but something is a little off when she hears it come out of my mouth."
    hero.say "Hey, look...what's up?"
    date_girl.say "What do you mean?"
    hero.say "Every time I mention Morgan or something about the guy, you look at me like I have steaming turds hanging out of my mouth!"
    date_girl.say "Isn't it obvious?"
    "I shrug my shoulders and shake my head, not knowing what she means."
    date_girl.say "If you need someone to spell it out for you, then I'm not going to be the one that does!"
    "With that, the lights in the theatre go down and the film begins."
    "But all I can think about is the weird encounter with Morgan and the way everyone seems to know something I don't."
    menu:
        "It's nothing...":
            "As the trailers roll by and the movie begins, I just can't concentrate on what's happening on the screen."
            "It still bugs me that what should have been a good chance to reconnect with an old friend ended up feeling so awkward."
            "But then I find myself thinking back to my memories of Morgan from when we were kids."
            "Always a little younger than the rest of us, Morgan never quite fitted in as well as most of us did."
            "I guess that all that time that passed since we last met must have added to that, maybe even made it more pronounced."
            "Most likely that was what lay at the root of my worries, and we could always iron that out when we met up in the near future."
        "Something's up":
            "I don't take anything in, from either the trailers or the fisrt part of the film."
            "All I can think about is how oddly Morgan came across and how I was the only one that missed the reason why."
            "Maybe there really were things from our past that I'd assumed didn't amount to anything."
            "Maybe they were still bugging Morgan, even after all this time had passed?"
            "But I realised I was juts ruminating on things and getting nowhere."
            "We'd agreed to meet up soon enough, and I could always get to the bottom of the mystery then."
    "Even though I tried, there was no way I could tune back into the movie now."
    "And so I spent the rest of the time in my seat just trying to keep my mind occupied until the time came to leave for home."
    hide expression date_girl.id
    return

label morgan_pregnant_flag:
    $ morgan.set_flag("pregnant",1,mod="+")
    return

label morgan_preg_talk:
    show morgan casual
    hero.say "Morgan...hey there."
    hero.say "Are you okay?"
    if morgan.get_flag_value("male") >= 75:
        "She looks at me whilst shaking her head and making a resigned sighing sound."
        morgan.say "There's no easy way to say this, [hero.name], so I'm just going to come out and say it."
        morgan.say "I'm pregnant, and it's yours."
        "There are times when Morgan's blunt nature makes things so much easier than they might otherwise be."
        "But suffice to say, this isn't one of those time."
        "The bald nature of the statement leaves me feeling like I've been punched in the gut."
        morgan.say "Well, aren't you at least going to say something?!?"
        hero.say "Sorry, Morgan - you just kind of took me by surprise..."
    elif morgan.get_flag_value("male") >= 25:
        "Now that she's looking me straight in the eye, I can see a measure of fear that wasn't apparent beforehand."
        morgan.say "[hero.name]...I was late this month, so I took a pregnancy test, just to be sure..."
        "I wait for her to go on, feeling my mouth go dry as the silence stretches by seconds to a minute."
        hero.say "And...what did it say?"
        morgan.say "It was...it was positive - I'm pregnant!"
        "All that I can do at first is puff out my cheeks and then blow the air out of my lungs in a long sigh."
        "I want to say something that will reassure Morgan and make everything alright."
        "But the news is so monumental that I'm having enough trouble processing it myself right now."
        hero.say "Morgan...I...I don't know what to say!"
    else:

        "Morgan all but throws herself into my arms and begins to sob into my shoulder."
        morgan.say "Oh, [hero.name], it's so not fair!"
        morgan.say "I'm too young and pretty to be a mommy!"
        "It takes me a moment to get over her histrionic outburst."
        "But then the truth of what she's saying dawns on me."
        hero.say "Morgan, are you saying that you're pregnant?!?"
        "At this, she looks up from my shoulder, eyes red and puffy as she nods her head."
        morgan.say "Uhuh, [hero.name] - you went and put a baby inside of me!"
    show morgan normal
    "I want to come over as the strong, masculine type, really I do."
    "But after all that I've been through with Morgan already, the emotional roller-coaster it's been, discovering there's another time around the loops is really making that almost impossible to manage."
    hero.say "What...what do you want to do, Morgan?"
    "Morgan looks at me hard for a moment, but then her expression softens by a couple of degrees."
    "I think that she was expecting me to step up and take control, but now realises the enormity of it all has hit me hard too."
    if morgan.love >= 150:
        morgan.say "I think that I want to keep the baby, [hero.name]."
        morgan.say "But I can't do it on my own..."
        "There's no need for Morgan to complete that last statement."
        "I already know what she meant to say and just what it means for me."
        menu:
            "Refuse":
                $ HIDDEN.append("morgan")
                $ morgan_love_max = 0
                hero.say "Morgan...I can't be a father right now."
                hero.say "I'm not prepared for that kind of responsibility..."
                "I hate myself even as I say the words, but I have to be brutally honest."
                if morgan.get_flag_value("male") >= 75:
                    show morgan angry
                    "Morgan looks at me as though she's disgusted at first."
                    "But then she looks away and shakes her head."
                    morgan.say "Huh...I guess I was hoping that you'd be more of a man about this."
                    morgan.say "But then I suppose it does take some balls to admit that you're not up to it too."
                    "She shakes her head again and turns her back on me as she does so."
                    morgan.say "I'm not sure I know where this leaves me...or us!"
                elif morgan.get_flag_value("male") >= 25:
                    "There's the slightest hint of tears in Morgan's eyes as she nods, her lip quivering just a little."
                    morgan.say "Well, I guess that's that..."
                    morgan.say "We should have been more careful and used a..."
                    "She stops before she can speak the last few words, something seeming to break inside of her."
                    morgan.say "Fucking hell, [hero.name] - I really thought there was more to us than this!"
                    "She shakes her head and looks away, as though she can't bring herself to as much as look at me right now."
                else:
                    "Morgan bursts into another flood of tears and hammers my chest with ineffectual punches."
                    "Her cries are almost pathetic by now, small yelps of frustration that actually hurt my ears."
                    morgan.say "How could you, you bastard?!?"
                    morgan.say "You had your fun with me, and now you just want to toss me into the trash!"
                    "She spins on her heel and refuses to look me in the eye any longer."
                    morgan.say "How could I have been so wrong about you?!?"
            "Accept":
                $ morgan.set_flag("toldpreg")
                hero.say "Morgan...of course I'll be there, for you and the baby!"
                hero.say "How could you even think that I wouldn't want that?"
                $ morgan.love += 10
                "I haven't had time to really think about what I'm saying or practise the lines."
                "I'm just saying what comes naturally to me on the spur of the moment."
                if morgan.get_flag_value("male") >= 75:
                    "Morgan's eyes widen a little, almost as though she's surprised at my enthusiasm."
                    "I see her relax just enough to let the worry and weariness that must have been eating at her show through."
                    morgan.say "You...you really mean that?"
                    hero.say "Of course I mean it, Morgan."
                    hero.say "How could you even think that I'd not be serious about something like this?"
                    "Morgan wraps her arms around me suddenly, pulling me into a tight embrace."
                    "It feels to me like she's accepted something deep inside, something that means she doesn't need to act so tough anymore."
                elif morgan.get_flag_value("male") >= 25:
                    "Morgan's eyes show her emotions, small tears forming in the corners that she wipes away quickly."
                    morgan.say "Is that the truth - do you really want to make a go of this with me?"
                    hero.say "Morgan, of course I do."
                    hero.say "I don't think we should see this as an accident, but a chance to do something amazing together."
                    "Morgan wraps her arms loosely around my waist and leans her head into my shoulder."
                    morgan.say "I don't know how you do it, [hero.name] - but you make this whole thing sound simply wonderful."
                    hero.say "Don't worry, it will be - because we'll make it wonderful together."
                else:
                    "I watch with some measure of surprise myself as Morgan claps her hands together and literally jumps for joy."
                    morgan.say "Oh, [hero.name] - my hero!"
                    morgan.say "We're going to make such a perfect little family together!"
                    "She jumps up and wraps her arms around my neck, pulling me down to her level as she does so."
                    "Her lips are right next to my ear as she almost purrs her next words to me."
                    morgan.say "I'm gonna make you so happy that you'll never want to let me go!"
                    "Right now, I'm not so sure I even have a choice in the matter!"
    else:
        morgan.say "I don't know about you, [hero.name], but I'm just not ready to be a parent, not right now."
        morgan.say "I've thought long and hard about this before I told you, and I think that I want to have a termination."
        "Things seem to be happening so fast, I feel as though I can't keep up."
        "First Morgan tells me she's pregnant, and now she hits me with the fact that she wants to get rid of it!"
        menu:
            "Agree":
                $ morgan.set_flag_value("pregnant", 0)
                hero.say "I...I suppose that it's your decision, Morgan."
                hero.say "I can't tell you what to do when it comes to your own body..."
                "I feel like I'm taking the easy way out by not challenging her on this one."
                "But do I really want a fight on my hands over something like this?"
                if morgan.get_flag_value("male") >= 75:
                    "Morgan's expression hardens, and she nods a little whilst looking away from me for a moment."
                    "I get the distinct feeling that she was preparing herself for a fight on this one."
                    morgan.say "It is, but I...I just, wanted to hear what you had to say about it first, that's all."
                    morgan.say "I feel better knowing that we're both on the same page."
                    "She clasps my hand, and I return the gesture."
                    "Neither of us speaks, but that's a relief as, under the circumstances, I have no idea what to say."
                elif morgan.get_flag_value("male") >= 25:
                    "Morgan gives me a smile at this, but it's a hard one and I can see that it's concealing her deeper emotions."
                    "She almost starts to break down, and then fights back the urge and wipes a tear from the corner of her eye."
                    morgan.say "I...I really think it's for the best, don't you?"
                    hero.say "Yeah...I mean, yes - yes it is, Morgan."
                    hero.say "We can't just sleepwalk into something like this."
                    "Morgan looks up at me, and I can't keep the emotion out of my own face either."
                    "At the sight of this, she clasps both of my hands in her own and offers me a fragile, but somehow more bitter-sweet smile."
                else:
                    "Morgan all but collapses into my arms, like a marionette with severed strings."
                    "She's sobbing the whole time, her cries racking her body and yet muffled by my chest."
                    hero.say "There, there...it'll be okay, Morgan..."
                    "I must sound like an idiot coming out with a line like that, but I don't know what else to say."
                    "Morgan herself says nothing, just keeps on sobbing away the whole time."
                    "By now, I can actually feel her tears starting to soak through my shirt."
            "Protest":
                $ morgan.set_flag("toldpreg")
                hero.say "Morgan, no - you can't do that...I won't let you!"
                hero.say "The child that you're talking about is a part of me too."
                "I don't know where this will to fight for the life of an unborn child is coming from."
                "All I do know is that it feels totally wrong to end a life before it's even begun."
                if morgan.get_flag_value("male") >= 75:
                    morgan.say "Maybe you should have thought about all of this before you went and knocked me up, huh?"
                    "The aggression and anger with which Morgan spits her initial response soon drains out of her face once the words are spoken."
                    morgan.say "Urrggh...I'm sorry, [hero.name] - but this is such a fucking mess!"
                    hero.say "You're right, Morgan - but we both made that mess."
                    hero.say "What kind of people are we if we just turn tail and run from it?"
                    morgan.say "I hear what you're saying..."
                    "I take hold of her hand and squeeze it, trying to show that even though I don't have an answer, I'm not going anywhere."
                elif morgan.get_flag_value("male") >= 25:
                    "Morgan regards me with what looks like surprise at my sudden outburst against her plan to have a termination."
                    morgan.say "I...I suppose you're right, [hero.name]."
                    morgan.say "I guess I just assumed that you'd be a typical guy and freak out at the idea."
                    morgan.say "I'm sorry...I should have asked you first."
                    "I nod my head slowly."
                    hero.say "It's okay, Morgan, I understand - you're scared, and so am I."
                    hero.say "Can we just talk this over before we make such a massive decision?"
                else:
                    "Morgan instantly bursts into a flood of tears and almost collapses until I manage to catch her."
                    morgan.say "Oh, [hero.name] - I'm so scared!"
                    morgan.say "I don't really want to have an operation - but I'm terrified of having a baby too!"
                    "I find myself patting her on the back as she clings onto me, almost stunned by her emotional outburst."
                    hero.say "It's...it's going to be okay, Morgan."
                    hero.say "Don't worry about anything...I'll make sure that you're alright."
    "There's a part of me that wonders if any of this would have come to pass had my relationship with Morgan been different back in the day."
    "Was it the years of her holding a candle for me and my own thinking that she was a guy cause us to be this emotionally volatile when we finally came together?"
    return

label morgan_give:
    if not "cool sunglasses" in hero.inventory.keys():
        $ gift = Equip("cool sunglasses", money_cost = 100, type = "accessory", effects = {"submissive":20,"rebel":20,"charm":5})
        "She hands me a small box."
        hero.say "Wow !\nIs those glasses looks great!"
        hero.say "Thank you so much."
    elif morgan.love() >= 25 and not "military boots" in hero.inventory.keys():
        $ gift = Equip("military boots", money_cost = 100, type = "accessory", effects = {"submissive":20,"gourmand":20,"charm":5})
        "She hands me a pair of boots."
        hero.say "They look fantastic."
        morgan.say "Your welcome [hero.name]."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label morgan_give_valentine:
    show morgan
    "Morgan walks hesitantly towards me."
    call morgan_greet from _call_morgan_greet_7
    show morgan
    morgan.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Morgan throws a box of chocolates towards me."
    hero.say "Thank you, Morgan."
    $ hero.gain_item(gift)
    hide morgan
    return

label morgan_give_birthday:
    show morgan
    "Morgan walks towards me."
    call morgan_greet from _call_morgan_greet_8
    show morgan happy
    morgan.say "Happy birthday [hero.name]!"
    call morgan_give from _call_morgan_give
    return

label morgan_give_christmas:
    show morgan
    "Morgan walks towards me."
    call morgan_greet from _call_morgan_greet_9
    show morgan happy
    morgan.say "Merry christmas [hero.name]."
    call morgan_give from _call_morgan_give_1
    return

label morgan_init:
    if "morgan" not in HIDDEN:
        $ HIDDEN.append("morgan")
    $ morgan.set_flag("nodate")
    $ morgan.set_flag("nokiss")
    $ morgan.set_flag("male",100)
    return

label morgan_fuck_date:
    $ morgan.set_flag("sex",1,"permanent","+")
    scene bg bedroom1
    if morgan.get_flag_value("sex") == 1:
        "I'm still reeling from the series of revelations that have come from Morgan's unexpectedly walking back into my life all of a sudden."
        "Not so long ago, Morgan was a guy that I'd lost touch with, then all of a sudden he turned out to be a she."
        "As if that wasn't enough, I discovered that this female friend I never knew I had, always carried a torch for me."
        "The next thing I know, we're out on a date together, and things are going amazingly well."
        "So well, in fact, that we've already decided to skip the formalities and take it to another level."
        "I suppose that if I ever wanted proof positive that I was wrong about Morgan being a guy, this is the point where I get it!"
        "All of this seems so crazy, like one of those weird dreams that you're convinced are reality, for a while even after you wake up."
        "The counterpoint to the craziness is the fact that this new version of Morgan I'm getting to meet for the very first time is something else."
        "The Morgan I remember was a slight, awkward-looking guy that never seemed the least bit comfortable in his...I mean her, skin."
        "By way of contrast, the Morgan that I'm getting to know now is petite, elfin and moves with a grace that finally makes sense of her body."
        "She's so cute and sexy that I honestly keep forgetting the person that I used to think she was."
        "I suppose tonight must have been pretty weird for her too."
        "I mean, she not only found out that I used to think she was a guy, but she's supposedly always had a thing for me too."
        "If I've felt the strain of wanting to discover the real her and also trying not to fall short of her expectations - imagine the pressure on her too!"
        "But in a way, maybe the two things have kind of balanced the whole thing out a bit?"
        "Maybe there being something making this a little weird for both of us means that we're tryign that little bit harder?"
    show morgan
    "Either way, when we're standing on my doorstep and I invite her in, she's the one that pulls me in for a kiss."
    "The fact that I have to almost stoop down to kiss her back just makes it all the more spontaneous and exciting."
    "It's the first time I've been this close to Morgan, this intimate."
    "The kiss is electric, thanks to the trepidation that we're both feeling at this moment in time."
    "And the sensation of her body against mine is something else."
    "Morgan's as slender as she is petite, her body almost all firm lines and slight curves."
    "I don't think there's a spare ounce of weight on her frame."
    "Breaking the kiss is next to impossible, but I so desperately want to peel off her clothes and see what lies beneath."
    "I hurriedly open the door and lead her into the hallway."
    "We race up the stairs, neither of us speaking."
    "Almost as soon as the door to my bedroom shuts behind us, I can't help myself."
    show morgan naked
    "Morgan yelps and laughs in surprise as I instantly begin to strip her clothes from her."
    "She does nothing to stop me, but I can see that she wasn't expecting me to be so bold."
    "I can't read her mind, only interpret her feelings from her expression and body-language."
    "But I hope that she's thrilled to be able to inspire such hopeless desire in me, especially after hiding that crush for so many years."
    "For my part, I simply can't wait to see her naked."
    "It's not that I still doubt her femininity, more that I've been so turned on by her that I want to see it as the culmination of my desire."
    "Finally I step back a little and see what I've been longing to see."
    "Morgan stands before me, utterly naked now."
    "She knows that she's on show, and she bites her lip in bashful amusement at the feeling."
    "All I can think is that she makes sense to me now, she makes so much sense where before she only caused me awkward confusion."
    "Her skin is smooth and pale, her limbs slender and yet feminine, breasts petite and in perfect scale."
    if morgan.get_flag_value("sex") == 1:
        hero.say "Morgan...you're...you're beautiful."
        hero.say "I feel like I know you...for the first time ever."
        "I feel like I'm babbling, just talking pure crap."
        "But she smiles up at me, stepping forward to begin pulling off my own clothes."
        morgan.say "Don't stop now - there's a whole lot more of me still to get to know!"








































































































    show morgan missionary
    "With Morgan pinned to the bed and myself firmly atop her, I'm eager to take things to the next logical step."
    "Beneath me, Morgan looks flushed and more than willing to let me have my way with her."
    menu:
        "Use protection" if hero.has_condom():
            "Before I go any further, I snatch up a condom from the bedside table and slip it onto my cock."
            "Morgan sighs at the delay in the proceedings, but it's only a couple of seconds lost."
            "And the consequences for not taking precautions would be much worse than losing a little of our momentum."
            $ CONDOM = True
        "Don't use protection":
            if morgan.get_flag_value("male") >= 50 and morgan.love <= 150:
                morgan.say "Whoa...what the fuck!"
                "I come to a complete halt as Morgan's tone and expression make it clear I can go no further."
                morgan.say "You're not sticking that thing inside of me without a condom, man!"
                "She reaches for her jacket, which just so happens to be within grabbing distance."
                "Her hand comes back a moment later, clutching a condom."
                morgan.say "If you'd be so kind?!?"
                $ CONDOM = True
            elif morgan.love <= 150:
                morgan.say "Oh, [hero.name]...you bad boy!"
                "I stop dead in my tracks, suddenly aware of the chiding tone in Morgan's voice."
                morgan.say "You can't come in without protection!"
                "She reaches for her jacket, which is atop a pile of clothes within grabbing distance."
                "And then she offers me the condom she's recovered."
                morgan.say "You can come on in once you're properly dressed!"
                $ CONDOM = True
            else:
                "I'm too lost in the moment to be thinking about anything other than sinking down atop Morgan right now."
                "She seems to feel the exact same way, eagerly welcoming me as I come to her, wrapping herself around me."
                "I can't imagine how long she's been waiting for this moment, and the last thing that I want is to deny it to her any longer."
                $ CONDOM = False
    "Here goes - this is it."
    "Not only have I had the revelations of rediscovering an old friend and then being told that he was a she all along."
    "She's also on the brink of becoming something far more to me than a face newly returned from the past."
    if morgan.get_flag_value("male") >= 75:
        "If I was in any doubt as to what Morgan wanted of me, she makes it clear by pulling me towards her."
        "One hand grips me around the neck, while the other fumbles around below, guiding me into her."
        "All the time she thrusts her groin towards me, as if desperate to feel me slip inside."
        show morgan missionary vaginal
        if CONDOM:
            show morgan missionary vaginal condom
        "When I make it and finally sink into her, Morgan feels incredible - tight and yet welcoming."
        morgan.say "Oh, shit...that's it...give it to me!"
        "I'm already deep inside of Morgan and more than committed to the act when she makes this demand of me."
        "But still I do my best to oblige, setting a quick rhythm and enjoying the immediate rewards in terms of sensation."
        "I'm used to being the one that makes most of the groans and grunts during sex, but Morgan soon puts me to shame in this respect."
        "Every thrust into her is met with a satisfied noise that makes me think that she's about to begin growling and clawing at any moment."
        "Indeed, I can feel her nails as she runs them down my back and scratches me in the throes of her passion."
        "My only answer to this is to become even more forceful myself, making Morgan's entire body shudder as I fuck her with all I have to give."
        "Her petite breasts are literally bouncing up and down by now, and she's slick with sweat."
        morgan.say "I don't care if you have to break me in half, [hero.name]."
        morgan.say "Just keep fucking me like this 'til I cum!"
        "I sincerely hope that won't be something that takes too long to happen."
        "My stamina's not the problem here, it's more the almost savage way that Morgan seems to like to make love."
        "She's driving me to such a degree that I can't keep going for much longer without cuming myself."
    elif morgan.get_flag_value("male") >= 25:
        "For all that my journey towards discovering the truth about Morgan felt strange and challenging, this moment is the complete opposite."
        "We seem to come together without a second of hesitation or the need for one person to show the other the way."
        "In that moment, everything just feels right."
        show morgan missionary vaginal
        if CONDOM:
            show morgan missionary vaginal condom
        "I feel myself brush against the lips of Morgan's pussy, and then I'm inside of her."
        "Just like that we come together and there's nothing between us."
        morgan.say "Oh, [hero.name]...I never thought...that I'd have this..."
        morgan.say "It feels...so good."
        "I lean in and kiss Morgan passionately then, wanting to be as close to her as I can manage to be."
        "Before now, I don't think that I'd fully understood what being with me meant to her."
        "Sure, I've been the guy that's longed for a girl so badly, but I've never had someone want me for so long as Morgan has."
        "The intensity of her passion and the way it's enflaming her desire is almost intoxicating to me."
        "For all that her body is making me come alive with my own pleasure, I feel the need to give her as much as I can in return."
        "My kisses have spilled onto her neck by this time, and I can't keep from nipping and biting on occasion too."
        "It feels like in the same way that Morgan has become almost an entirely new person to me now, I want the same for myself."
        "I want to live up to the image that she's carried of me for all those years, to be the man that she wants me to be in her fantasies."
        "My body reflects this same desire, as I continue to push myself into Morgan with every ounce of stamina that I still possess."
        morgan.say "[hero.name]...I'm going to cum!"
        "I almost fail to hear Morgan's breathless words, as I feel myself succumbing to the very same thing."
    else:
        morgan.say "Ooo, [hero.name]...you're so big!"
        morgan.say "You're going to fill me up until there's no room left inside of me!"
        "Morgan's chuckles and giggles are becoming less frequent now, replaced instead with panting and sighing instead."
        "She wraps her hands around my neck and seems to hold on for dear life as I lower myself down atop her."
        show morgan missionary vaginal
        if CONDOM:
            show morgan missionary vaginal condom
        "Though I feel my cock pushing into her without too much resistance, still Morgan rolls her eyes and moans intensely all the same."
        "I begin to move inside of her, and she seems happy to abandon herself to my attentions, simply letting me have my way with her."
        "But that's not any kind of problem, as the feeling of having her entire body laid open to my attentions is something quite irresistible."
        "Morgan writhes beneath me, responding with all of her being to the pleasure that she takes from my taking my own from her."
        "It's as though the years that she must have spent nursing her affections for me have rendered her helpless now that she has her heart's desire."
        "All that she wants to do is lie back and let me use her like a living doll, like a human sex-toy."
        "And I'm more than happy to oblige her in that particular desire."
        "Her petite form is almost folded in half beneath me now, and I can feel her small breasts rubbing against my chest, her nipples stiff and erect."
        "I can't remember a single thing about the person that I once thought Morgan to be."
        "His memory is almost gone from my mind, erased in favour of the woman that I'm making love to right now."
        "Like Morgan's sentiments about my cock entering her pussy - there's simply no room for him inside of my head."
        "And I feel like the moment that I cum, his memory will be washed away forever."
    "This is it, I can't hold on for a moment longer."
    menu:
        "Cum inside" if CONDOM:
            "As I feel my climax taking over, I begin to thrust more deeply into Morgan than I thought was possible."
            "Even though she can't feel everything, there's still no way that she can fail to be effected by this doubling of intensity."
            "Her head thrashes from side to side as she's pulled into her own orgasm a few seconds later."
        "Cums inside" if not CONDOM and not morgan.get_flag_value("pill"):
            show morgan missionary vaginal cum
            "Morgan feels the full and unadulterated force of my orgasm as I lose myself inside of her."
            show morgan missionary vaginal cum orgasm
            "There'll be consequences later, but for the moment we're both lost in it and nothing else matters."
            "All that I can hear is my own horse panting for breath and the sound of Morgan moaning as she cums in turn."
            if morgan.get_flag_value("male") >= 50 and morgan.love <= 180:
                hide morgan
                show morgan naked angry
                morgan.say "Ah...ah...aaah, fuck!"
                "Morgan's words are almost indistinguishable from the gasps she makes as I thrust into her."
                morgan.say "You...you came in me...you stupid bastard!"
                morgan.say "You came inside of me without a damn rubber!"
                $ morgan.love -= 20
            elif morgan.love <= 180:
                hide morgan
                show morgan naked angry
                morgan.say "Oh god, oh god, oh god...you came in me!"
                "I can feel her beginning to shudder from something other than the sensation of my cock inside of her."
                "At the same time, she starts to let out little sobs that are barely even audible."
                morgan.say "In me...with no condom!"
                $ morgan.love -= 20
            if not morgan.get_flag_value("pill") and not morgan.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills):
                $ morgan.set_flag("pregnant",1)
        "Cums inside" if not CONDOM and morgan.get_flag_value("pill"):
            show morgan missionary vaginal cum
            "Morgan feels the full and unadulterated force of my orgasm as I lose myself inside of her."
            "There'll be consequences later, but for the moment we're both lost in it and nothing else matters."
            "All that I can hear is my own horse panting for breath and the sound of Morgan moaning as she cums in turn."
        "Pull out" if not CONDOM:
            show morgan missionary out cum
            "I have all the proof I need to believe that Morgan is and always has been a girl."
            "I don't need to get her pregnant to prove it beyond any shadow of a doubt."
            "At the last second, I pull out of Morgan and send my load showering over her stomach and already slick thighs."
            "She can't help but groan in disappointment, but she'll thank me for it once the dust has settled and he heart has stopped hammering in her chest."
    hide morgan
    show morgan naked
    "No one speaks as we lie together on my bed, panting for breath is all that we seem to be able to manage."
    "All I can think is how ludicrous this situation would have seemed to be back in the day - or even a couple of weeks ago."
    "I'm sure Morgan is feeling something similar right now."
    "But I also hope that she's thinking that it's something that could become the new normal."
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
