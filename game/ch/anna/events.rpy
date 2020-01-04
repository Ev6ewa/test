init python:

    Event(**{
        "name":"anna_init",
        "label": ["anna_init"],
        "girls_conditions": {"anna":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "anna_start",
        "label": ["anna_start"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"flagmin_performance":2, "flag_female":0},
        "do_once":True,
        })

    Event(**{
        "name": "anna_start2",
        "label": ["anna_start"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"flagmin_band":2, "flag_female":0},
        "do_once":True,
        })

    Event(**{
        "name": "anna_event_01",
        "label": ["anna_event_01"],
        "priority": 500,
        "duration": 4,
        "game_conditions":{"hours":(20,21),"flag_dateinprogress":False, "flag_female":0},
        "girls_conditions": {"anna":{"min_love":40,"present":False, "flageq_story":1,'valid':True}},
        "clothes": "date",
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "anna_give_christmas",
        "label": ["anna_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"anna":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "anna_give_birthday",
        "label": ["anna_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"anna":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "anna_give_valentine",
        "label": ["anna_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"anna":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "anna_practice_01",
        "priority": 500,
        "label": ["anna_practice_01"],
        "duration": 0,
        "game_conditions":{"activity":["practice"],"flagmin_bandpractice":25,"flag_dateinprogress":False, "flag_female":0},
        "girls_conditions": {"anna":{"min_love":50,"present":True,'valid':True}},
        "do_once":True,
        "quit": True
        })

label anna_practice_01:
    "With the Battle of the Bands almost here, it feels like I've been shut in the practice room with the girls every spare moment for the past few days."
    "The stress is building, and being in such close confines means you can almost feel the tension as we go over stuff again and again."
    show sasha at left
    "Sasha is blunter than usual, and it's hard to get anything but grunts and acid glares out of Kleio."
    show anna at right
    "But Anna seems unaffected, blithly hammering away at her drumkit and casting me adoring glances whenever she gets the chance."
    show sasha angry
    sasha.say "Anna, what the fuck?!?"
    anna.say "Huh!"
    sasha.say "You're not keeping time right, it's ruining our sound."
    hide sasha
    show kleio at left
    kleio.say "She's right, Anna - I could hear it too."
    hide kleio
    show anna sad at center
    "Anna looks surprised and more than a little downcast at the accusation."
    "I realise that, unlike Sasha and Kleio, I hadn't noticed Anna's mistake."
    "And then I also realise that was because of the attention she was paying me, and that this probably what made her screw up as well."
    "There's an awkward silence, as the girls are waiting for me to add my opinion as a fellow band member."
    menu:
        "Try to play peacemaker":
            $ a = 1
            hero.say "I didn't hear it, for what it's worth."
            show anna blush
            "Anna's eyes show her thanks for the support, and she seems to cheer up a little."
            show anna at left
            show kleio at right
            kleio.say "Jesus, man - I knew you were tuneless, but you'd have to be stone deaf to miss something like that!"
            hero.say "Back up a bit, Kleio...we're all frazzled and strung out right now, and fighting each other'll only make it worse."
            hide kleio
            show sasha at right
            sasha.say "He's got a point, Kleio - yeah, Anna fucked up, but we are all feeling the strain - let's take a break while we still can."
            $ anna.love += 5
        "Try to stay neutral":
            $ a = 2
            hero.say "Maybe you were a little off, Anna - but not by too much."
            show anna blush
            "Anna's eyes widen as all three of us basically agree she made a mistake, and she looks down at the drumsticks in her hands sadly."
            anna.say "I'm really sorry, guys...I guess I just wasn't trying hard enough."
            show anna at left
            show sasha at right
            sasha.say "Ahh, we're all feeling it, Anna...but we're a team and we can get through this - let's take five and get our heads straight."
        "Side with Sasha and Kleio against Anna":
            $ a = 3
            hero.say "They're right, Anna - you're fucking up your part, and it's screwing with all of us."
            "Anna's eyes are instantly filled with self-doubt, her lips quivering a little, and I can tell she expected me to defend her."
            show anna at left
            show kleio at right
            kleio.say "He's not wrong, Anna - but don't get suicidal over it!"
            hide kleio
            show sasha at right
            sasha.say "Yeah, Anna, we can fix the problem before the contest - but right now, we need to take a breather from this."
            $ anna.love -= 5
    hide kleio
    hide sasha
    hide anna
    "Everyone downs their instruments, and there's an almost palpable sense of relief, as if a weight has been lifted off all four of us."
    "I slip out into the corridor, where there's an open window and the chance of some fresh air."
    "I've only been out there perhaps half a minute, when I hear the door open and see Anna has followed on my heels."
    if a == 1:
        show anna blush
        anna.say "Hey, thanks for sticking up for me back there."
        hero.say "No problem...look, I know you were off because you were into me."
        anna.say "Am I really that obvious?"
        hero.say "Don't feel bad, maybe it's the stress getting to you, that's all."
        hero.say "For what it matters, I'm not mad...actually, I'm flattered."
        "Anna's mood changes suddenly for the better, and she hugs me tightly."
        "Her petite frame means that she barely comes up to my chest, but her grip is intense."
        hero.say "I just want you to know, Anna...you're more important than winning this contest."
    elif a == 2:
        show anna sad
        anna.say "Did you really think I screwed the song up just now?"
        "I take a deep breath and scrub my hand across my face, trying to slough off some of my fatigue."
        hero.say "Look, Anna - I'm sorry for ganging up on you like that, but you were off by a bit."
        hero.say "But I think we all were, if we're honest...you just got both barrels because Sasha spotted it first and we all jumped in."
        "Anna nods, still looking sad, but perhaps a little reassured that she's not the weak link in the band."
        anna.say "Okay, I guess that's something."
        "She hugs me gently, more for the sake of reassuring herself than anything more amorous, and I hug her back weakly."
    else:
        show anna sad
        anna.say "I'm sorry...please don't be mad with me!"
        "I'd expected her to be angry that I'd torn a strip off of her in front of the others."
        "But Anna's clearly more concerned that she's upset me than made a mess of the song we were playing."
        hero.say "God's sake, Anna - I'm not mad at you, I'm mad that the song got fucked up."
        hero.say "The contest's so damn close that we can't afford to miss a beat right now."
        "Anna's silent for a moment, then she sniffles and visibly tries to look stronger, reminding me of a kid trying to look tough and failing."
        anna.say "Okay, got it...I'll keep focussed on the contest, I promise."
    hide anna
    "Anna goes back into the practice room ahead of me, and I can hear her begin to bash the drums."
    "She's tentative at first, but I can hear her confidence slowly growing with each stroke of her drumsticks."
    "I take a deep breath and prepare to follow her in, hoping that my words have had the desired effect."
    return

label anna_give:
    if not "Guitar book" in hero.inventory.keys():
        $ gift = Consumable("Guitar practice book", money_cost = 100, label = ["guitar_practice_book"], uses = 10)
        "She hands me a pretty large book."
        hero.say "Wow !\nIs that a book with guitar tricks?"
        anna.say "It sure is..."
        hero.say "Thank you so much."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label guitar_practice_book:
    "I practice some guitar with Anna's book."
    $ game.pass_time(2)
    $ game.set_flag("bandpractice",10,mod="+")
    return

label anna_give_valentine:
    show anna
    "Anna walks hesitantly towards me."
    call anna_greet from _call_anna_greet_7
    show anna blush
    anna.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Anna hands me a box of chocolates."
    hero.say "Thank you, Anna."
    $ hero.gain_item(gift)
    hide anna
    return

label anna_give_birthday:
    show anna
    "Anna walks towards me."
    call anna_greet from _call_anna_greet_8
    show anna happy
    anna.say "Happy birthday [hero.name]!"
    call anna_give from _call_anna_give
    return

label anna_give_christmas:
    show anna
    "Anna walks towards me."
    call anna_greet from _call_anna_greet_9
    show anna happy
    anna.say "Merry christmas [hero.name]."
    call anna_give from _call_anna_give_1
    return

label anna_start:
    $ anna_love_max = 40
    $ anna.set_flag("story",1)
    $ if "anna" in HIDDEN: HIDDEN.remove("anna")
    return

label anna_init:
    python:
        if "anna" not in HIDDEN and not anna.get_flag_value("story"):
            HIDDEN.append("anna")
    return

label anna_event_01:
    $ anna_love_max = 200
    $ anna.set_flag("story",2)
    scene bg bedroom1
    play sound "sd/cell_vibrate.mp3"
    pause 1.0
    hero.say "Hello?"
    "There is so much noise in the background that it’s hard for me to hear. When I finally make out a voice, I’m shocked to hear that it’s Anna."
    "She’s slurring, and she sounds like she’s very drunk."
    anna.say "Hellooooooo, [hero.name], how are you?"
    "I stifle a laugh, amused by the sound of her high-pitched voice mumbling up letters."
    hero.say "I’m doing pretty well, Anna, how are you?"
    anna.say "Oh, I’m fantastic!"
    hero.say "I’m glad to hear that, dear. Wha are you up to?"
    anna.say "You know, the usual. Getting drunk, getting high, taking the downtown."
    hero.say "Sounds like a super fun time."
    anna.say "Oh, it so totally is. Downtown is my favorite place ever! Everything is soooo great over here."
    menu:
        "Can I join you?":
            hero.say "Really? Well, would you mind if I came and joined you?"
            "Anna gasps."
            anna.say "Oh my god, that would be AMAZING! Here, I’ll text you the address of the bar."
            anna.say "You’d better hurry and get here though!"
            "Quicker than I thought someone who was drunk could, she texted me a flawlessly typed address."
            "I realize with a start that this bar is only a few blocks down the street from my apartment."
            "It must be why Anna called me—even in her alcohol filled stupor, she must have realized I was close."
            hero.say "Alrighty, Anna, I’ll be there in a few minutes. Keep an eye out for me!"
            anna.say "I will, I totally will! See you soon!"
            "Before I have a chance to say goodbye, she hangs up on me, leaving the ghost of a laugh still hanging on my lips."
            $ anna.love += 1
            $ HELP = False
        "Where are you?":
            hero.say "Where are you, Anna?"
            "The background noise gets louder again, and I realize that she must be asking her friends where she is. Yikes. She must be more drunk than I realized."
            "Finally, she returns to the phone, yelling the address in my ear. I pull the phone back slight, her tinny voice grating on my nerves."
            "I realize the bar she’s at is only a few blocks down from me."
            "Whether or not I want to admit it, I am concerned about her, and I don’t want to leave her struggling alone with whoever else she’s with, especially if they’re drunk too."
            "So, against my better judgement, I grab my coat."
            hero.say "I’m glad you’re having fun, Anna! Just to be sure you’re okay, I’m gonna come check in on you, alright?"
            "I can hear her pout through the phone. She starts whining, loud and annoyed."
            anna.say "You’re not my Dad, [hero.name], I can take care of myself."
            "I roll my eyes, starting to make my way out my door anyway."
            hero.say "I know, I know you can. I’m just being a friend, okay? If nothing else, we can party together now instead of separate, yeah?"
            "She sighs."
            anna.say "I guess sooooo."
            hero.say "Alright then, don’t go anywhere. I’ll see you in a minute."
            "Before I get a chance to say goodbye, the line goes dead. Holding back laughter and slight worry, I make my way out into the cool night."
            $ anna.sub += 1
            $ HELP = True
    scene bg street with fade
    "I make my way brusquely down the street, and I realize that it isn’t going to take me that long to find the bar Anna was at."
    "The bass is thumping so loud, I could hear it at the bottom of my street, the howling laughter of drunks and the flashing party lights so obvious that I’m shocked the police haven’t shut it down yet."
    "As I get closer, I see a clump of people who look familiar partying in the outside patio area, downing more tequila shots and laughing about a joke I was too far away to hear."
    "When I scan the crowd, I finally see Anna, laughing with the rest, and I let out a breath I didn’t realize I was holding."
    "Swinging my leg over the short patio fence, I approach her, tapping her on the shoulder."
    show anna happy
    "She swings around drunkenly, stumbling over her own two feet and directly into my arms. Once she got her bearings, she gazes up at me, and then, the biggest smile crosses her face."
    anna.say "[hero.name]! You’re here!"
    "I smile at her, helping her steady herself."
    if not HELP:
        hero.say "What can I say, who could resist a night out with you?"
        "Anna goes into a fit of giggles, a blush rising up on her cheeks as she struggles to contain herself."
        anna.say "Aw, [hero.name]., you’re so fucking sweet. I’m glad you’re here!"
        hero.say "Me too, Anna."
        "I order a beer from the bartender, hoping it would loosen me up a little bit, but I don’t spend long at the bar, instead immediately returning to Anna’s side."
        $ anna.love += 1
    else:
        hero.say "Yeah, I am."
        "Anna rolled her eyes at me, leaning away, trying to grab her shot glass."
        anna.say "Wow, you sound like quite the party pooper tonight. Have a drink or something, it’ll loosen you up."
        "Against my better judgement, I listen to her, ordering a beer from the bartender before returning to her side."
        $ anna.love += 1
    "Anna sways as she struggles to talk, her words getting more and more garbled."
    "Although I can’t help but laugh as she tries to say ‘Battle of the Bands’ for about the eighth time, my concern for her well-being can’t help but grow."
    "She’s wasted, beyond wasted, and her friends didn’t really care that much. They’re drunk too, and more than happy to simply leave her to her own devices."
    "I can’t say the same for myself."
    if not HELP:
        hero.say "Hey, Anna, are you feeling okay?"
        "Anna twists her face up, rocking back and forth in her struggle to remain conscious."
        anna.say "I’m fineeeeee"
        hero.say "Are you sure, dear? You seem really out of it. Let me get you a water, at least."
        "For a moment, I’m afraid that she’s going to reject my care, her eyes narrowing as she finally righted herself."
        "Then, she collapses down into the chair that I had vacated for her, waving her hand."
        anna.say "A water sounds like a good idea, actually. Thank you, [hero.name]."
        "Happy to oblige, I quickly walk off, going to get Anna a water."
        $ anna.love += 1
    else:
        hero.say "Anna, I think we should get out of here"
        "Anna narrowed her eyes, glaring at me, digging her nails into her glass beer bottle."
        anna.say "What are you trying to do, [hero.name]? Are you trying to take advantage of me?"
        hero.say "No! No, goddamn, Anna, I would never do anything like that. I’m just worried about you. You seem really drunk."
        "Anna shuffles her feet, standing down but still defensive."
        anna.say "I’m really not that bad, [hero.name], I don’t know what you’re going on and on about."
        hero.say "I just—I’m just—oh, whatever, Anna. Just sit down, and let me get you a water, at least. Please."
        "Anna huffs, crossing her legs and taking my seat."
        anna.say "Whatever."
    scene bg pub
    "The bartender obliges my request quickly, giving me a large, icy glass of water."
    scene bg map
    show anna normal
    "When I turn, I see Anna, seated, talking with a man who is leaning over her small frame, far too close for my comfort."
    "For a moment, I just hang back and watch, so stunned that I can’t find the energy to pick up my feet."
    "The man leans closer to her, dragging his hand down her jawline, grinning at her, looking like an animal hunting his prey."
    show anna annoyed
    "Anna stiffens, clearly uncomfortable by his advances, but too drunk to realize what is truly going on."
    menu:
        "Interrupt them":
            "Having enough of his behavior, I storm over to her side"
            "Despite the blood boiling underneath the surface, I struggle to maintain calmness in my voice. I don’t want to scare Anna."
            hero.say "Hey, dear. I brought you some water. Who is this?"
            "Anna clings onto my arm, holding me tightly as I carefully hand her her water. She struggles to introduce me, her words slurring together so much I can’t even catch his name."
            man_say "I’m just a friend of Anna’s."
            hero.say "Well, maybe I’m reading into things too much, but she didn’t seem all too happy to see you back there."
            "The Strange Man looks uncomfortable to be called out, and leans away from the two of us."
            man_say "I guess so. I just thought she was hot. My bad, buddy."
            "With one last glance at Anna, he spoke over his shoulder as he walked away."
            man_say "See you later, Anna. Sorry again, dude."
            show anna happy
            "Turning back to Anna, she wasn’t able to say much, but she simply looked at me, and gave me a hug, eyes speaking more than words ever could."
            "I hug her back, enjoying the moment, before once again helping her drink her water."
            $ anna.love += 1
        "Do nothing":
            "I hang back still, finding myself flipping through any conversations I’d had with Anna to see if she had a boyfriend I didn’t know about."
            "After all, I didn’t want to be that guy, especially if she had a boyfriend."
            "The man gets closer to Anna, dragging his hand along her thigh, fingers splayed and grabbing at every empty patch of her skin."
            "His mouth is nearly watering, his eyes hungry, taking every inch of her in. Some small part of me agreed, not blaming him—Anna’s as hot as they come—but something about this situation felt off."
            "I couldn’t quite place the feeling, but something within me left me planted to the floor, unable to tear my eyes away, but unable to drag myself forwards."
            "The Man gets ever closer to Anna, lips nearly brushing hers as she struggles to keep her eyes open."
            "Finally, someone else noticed Anna, one of her friends, her face twisted in the same confusion I felt."
            "However, this time, she decides to step in."
            "She approaches the man with enough drunken swagger to drive him off."
            "The man looks sheepish, ashamed, as though he knew what he was doing was wrong, and I realized with a start that I could’ve done more."
            "I could have helped her, but instead, all I could do was watch, afraid."
            "Ashamed, I quietly make my way to Anna’s side, making sure to give her an extra big hug when I made it to her side."
    show anna normal
    "Anna, seemingly subdued by the water, gently leaned her head into my shoulder."
    anna.say "I’m tired, [hero.name]."
    hero.say "I know, Anna. Do you want to go home?"
    "Anna cries out, upset, sounding almost on the verge of tears."
    anna.say "I live all the way across town, and we can’t drive now. I’ll never be able to get home."
    "Shit, she’s right. We can’t drive, especially not her."
    "I don’’t want to be that guy, but I know I can take her home. Or at least help her get home safely."
    menu:
        "Invite her home":
            hero.say "Anna, I promise I don’t mean this to be weird, but I live right up the street."
            hero.say "Do you want to come home with me?"
            hero.say "Sasha and Bree should be home, and we have a couch in the living room too."
            "Anna’s eyes shimmer, and, wordlessly, she nods, nearly collapsing into my arms."
            "Tossing a few dollars onto the table to cover her tab, and giving a brief goodbye to her friends, I slowly begin to help her back towards my home."
            scene bg street
            show anna normal
            with fade
            "It’s a long, quiet walk home, with only the brief sounds from the busy street to punctuate our walk."
            "Anna is silent, stumbling, barely coherent. I did my best to help her walk, praying that my apartment door would be there soon enough."
            scene bg house
            show anna normal
            with fade
            "Finally, right when I think Anna can’t make it any farther, we finally reach my door. Walking as quietly as I can, I let her into my home."
            scene bg livingroom
            show anna normal
            with fade
            "Almost immediately, she collapsed onto my couch, falling asleep quicker than I thought possible."
            "Stifling a grin, I do my best to put her to bed, placing a blanket over her body and giving her a trash can in case she feels sick later."
            "She looks so peaceful, asleep on the couch, that, for a moment, I simply watch her, cuddled up to the blanket, chest rising and falling, indicative of her deep sleep."
            "She was so beautiful, so unaware, as she slept."
            hide anna
            "Finally, satisfied that she was safe and comfortable, I turn to go to my own room, suddenly aware of the deep exhaustion permeating my bones."
            $ anna.love += 1
            $ game.room = "bedroom1"
        "Call a cab":
            hero.say "Do you want me to call you a taxi? I can ride it with you so I know you’re okay."
            "Anna looks up at me, eyes exhausted. Without a word, she nods before leaning back against my body."
            "I do my best to hail a cab, dialing as many numbers as I can find for cab companies until I find one willing to take us both in the order I need."
            "I wince at the expense, knowing it will take a serious bite out of my wallet, but I know that Anna needs it. In good conscience, I can’t leave her here."
            "She dozes off as we wait for the taxi, and it seems as though it can’t come soon enough."
            scene bg street
            show anna normal
            with fade
            "Finally, I saw the car pull up to the curve, and I slowly help Anna to her feet, guiding her into the backseat."
            "She was silent as the drive goes, the lights from the street flashing in and out of the windows."
            "Finally, we got back to her apartment, and, as best as I could, I steady her outside her door."
            hero.say "Are you going to be okay, Anna?"
            "Anna nods, struggling to keep her bearings. With a soft smile, she slowly made her way towards her complex, leaving me biting my lip, watching her stumble towards her home."
            hide anna
            "Hesitantly, I turn back to the cab, leaving the bit in my stomach to grow bigger and bigger as the cabbie slowly takes me away, stealing my wallet and leaving my heart at the curb."
            $ game.room = "map"
    return

label anna_fuck_date:
    scene bg bedroom1
    $ anna.set_flag("sex",1,"permanent","+")
    "I close the bedroom door behind Anna, still not quite believing we're going to do this."
    "I try to look confident, but my smile ends up being too much."
    show anna happy
    "Anna can't help giggling, which sets me off laughing too."
    menu:
        "Say something to break the ice":
            hero.say "Hope you're not laughing when we're naked."
            anna.say "Sorry, I guess I'm more nervous than I thought."
            anna.say "Don't worry, it's not you, just doing this kind of thing."
        "Kiss her to break the ice":
            "I gently lean in to kiss her, stopping her giggles in their tracks."
            "Anna stiffens for a second, then relaxes, melting into the kiss."
            "She pulls away a few seconds later, her cheeks a little flushed."
    hero.say "Are we going too fast for you?"
    hero.say "If you want to slow down, just say so - I won't be mad."
    show anna normal
    "Anna looks away for a moment, then back to meet my eye."
    anna.say "It's just...it's been a long time since I dated..."
    anna.say "Well, since I dated a guy...or been with one."
    "I know all about her being bi-sexual, and it doesn't bother me in the least."
    "In fact, I've never been with a bi-sexual girl before, and so I'm feeling a little nervous as well."
    menu:
        "Try to sound confident":
            hero.say "Don't worry about it, Anna."
            hero.say "We can go as slow, or as fast as you like."
        "Try to sound sensitive":
            hero.say "Don't laugh at me, Anna..."
            hero.say "But I'm feeling a bit scared too."
    show anna blush
    "Anna nods and gives me a little smile, silently thanking me for my words."
    anna.say "It's not just that, [hero.name]"
    anna.say "I have to show you something before we go any further."
    "I nod, trying to be all woke and understanding."
    "But inside I'm afraid that she's going to show me something that'll freak me out or turn me off."
    "Anna returns my nod and quickly turns her back to me."
    "She yanks off her t-shirt and then pulls down the back of her jeans."
    show anna naked blush
    "There, on the small of her back, is a tattoo which reads ANAL WHORE."
    menu:
        "Gasp in shock" if hero.charm() >= 25:
            "I let out a gasp, genuinely shocked at the tattoo."
            anna.say "Ah shit, I knew you'd hate it!"
            anna.say "I didn't want to show you, but how could I not if we're going to do this?"
            hero.say "I don't hate it."
            hero.say "It's just...a surprise, that's all."
            $ anna.love += 1
        "Laugh in surprise":
            "I laugh before I can stop myself."
            anna.say "You think it's funny?!?"
            hero.say "No...yes...well, maybe a little bit."
            hero.say "It's kind of like something that makes you laugh at an awkward time."
        "Whistle and shake head" if hero.charm() >= 50:
            "All I could do was whistle and then chuckle."
            anna.say "You hate it, don't you?"
            hero.say "Nah, it's just so crazy that it knocked me for six!"
            anna.say "So you think I'm crazy too now?"
            hero.say "Not crazy like a psycho, crazy like a wild thing!"
            hero.say "Anna, I don't know what you're gonna show me next, but I want to find out!"
            $ anna.love += 1
            $ anna.sub += 1
    "Anna looks back at me over her shoulder, a weak smile growing on her face."
    "She seems reassured by my words."
    hero.say "So are you?"
    "Anna looks puzzled at the question."
    anna.say "Am I what?"
    hero.say "An anal whore?"
    "Anna's smile becomes wider, and much more wicked"
    anna.say "Would you like me to be your anal whore?"
    "I feel a geneuine twinge of delight at the way her eyes are sizing me up right now."
    "I realise that I've been let in on one of the most intimate secrets of what turns this girl on in the bedroom."
    "I nod."
    anna.say "Big talk, [hero.name]!"
    anna.say "If you want me to be your little anal whore, then you better show me how you're gonna make into one!"
    "She's taunting me now, wanting me to make good on my promises."
    "I step closer to her, reaching around to unbutton her jeans from behind."
    "I pull them down until they reach her ankles and then leave her standing in only her panties and bra."
    "Leaning in close, I begin to massage her buttocks."
    "Anna moans a little at first, encouraging me to squeeze harder, which makes her moaning become louder in response."
    hero.say "Hello, little ass."
    hero.say "I'm going to have to fuck you now, quite hard."
    hero.say "I'm going to have to fuck you, because the little whore you belong to likes it rough."
    "Anna twists round at this, eyes twinkling with anticipation after my talking dirty to her ass."
    "She takes me firmly by the hand as she kicks off her jeans, using the other to take off her underwear as she leads me quickly to her bed."
    "We struggle for a moment, as she tries to pull off the same clothes as me at the same time, but soon we're both naked and rolling on the unmade bed."
    menu:
        "Use protection" if hero.has_condom():
            "I see a few condoms on the bedside dresser and snatch one when I'm in range."
            "Anna watches me intently as I roll onto my back and slide the condom down over my now very erect cock."
            "It's hard to concentrate, as she's watching me like a hungry animal, waiting for the right moment to pounce."
            $ c = "condom"
            $ hero.use_condom()
        "Take her unprotected":
            "I roll slightly onto my back, and my very erect cock pulls the sheets with it like a tentpole."
            "Anna watches my cock, and not me, eyeing it up like it's all she cares about in the world right now."
            "I can't shake the feeling that she's already imagining how it'll feel once it's inside of her."
            $ c = ""
    if persistent.xray:
        $ x = "xray"
    else:
        $ x = ""
    anna.say "If that thing wants to stick itself in my ass, then it'll have to catch it first!"
    "She turns her back on me, taunting my painfully aroused cock with her ass."
    "I try to pounce on her, but she's too fast and I only manage to grab hold of her with one hand."
    "We roll on the bed until we come up with her on top, my cock just inches from all the possibilties of her ass and vagina."
    menu:
        "Anal sex" if hero.charm() >= 50:
            hide anna
            $ p = "anal"
            show expression "anna cowgirl "+p+" "+c
            "Anna lives up to her tattoo, wasting no time in angling herself so that my cock is rubbing against her buttocks and then pressing herself down suddenly."
            "There's no pause or hesitation as I slip inside of her ass, telling me that she's done this before and knows how to handle it."
            anna.say "Well hello, it looks like you caught me."
            "Even though her ass is spreading to take me in, her muscles are squeezing me tighter all the time."
            anna.say "Now I want you to make your little whore feel sore down there for a week!"
            $ anna.sub +=10
            $ anna.love += 5
        "Vaginal sex":
            hide anna
            $ p = "vag"
            show expression "anna cowgirl "+p+" "+c
            "Anna throws me a curve ball by angling herself forward so that my cock rubs against her clit and then beigns to push inside."
            "She feels tight and it seems like an age as she sinks down onto me, but that only makes it all the more incredible, almost like it's her first time."
            hero.say "Anna...I...I thought you wanted it in your ass!"
            anna.say "Ahh, fuck...it's been so long, since I had a real cock inside of me...couldn't help myself."
            "She's squeezing me so tight already, and knowing she's so desperate for my cock just makes it more intense."
            $ anna.love += 2
            $ f = ""
            if charm >= 50 or "anal beads" in hero.inventory:
                menu:
                    "Finger her ass" if charm >= 50:
                        show expression "anna cowgirl "+p+" "+c+" ass"
                        hero.say "No reason for me to let you miss out on what you love."
                        "I slide my fingers between her legs, using the slickness of her own skin to slip two digits up her ass."
                        "Anna moans as she's penetrated from two different angles, moving in either direction only making the sensation of both more intense."
                        $ anna.sub += 5
                        hide expression "anna cowgirl "+p+" "+c+" ass"
                    "Use anal beads" if "anal beads" in hero.inventory:
                        show expression "anna cowgirl "+p+" "+c+" beads"
                        hero.say "Oh fuck, Anna...that's amazing...but what about your ass?"
                        "She smiles wickedly, clearly enjoying being in control."
                        anna.say "I already thought ahead...give me your hand."
                        "She guides one of my hands under her, where I can feel something hanging below her ass, it feels like anal beads, she must have found them in the drawer..."
                        "Anna's smile turns into a grin, and she nods as I take hold and pull."
                        anna.say "Oh shit, [hero.name]...oh yes...pull my cord, pull this little whore's cord right out of her ass!"
                        $ anna.sub += 10
                        hide expression "anna cowgirl "+p+" "+c+" beads"
    show expression "anna cowgirl "+p+" "+c+" b"
    "She's riding me like a woman possessed now, the shy girl that let me follow her to her bedroom nowhere to be seen."
    "I can't help but believe that she's not been with a man for a long time, as having me inside of her seems to have awoken something that's taking over."
    "Whenever I can spare a hand from trying to hold on, I reach up and caress her breasts as they're hanging above me."
    hero.say "If I ever want to kill myself, Anna, promise you'll smother me with these things!"
    "She giggles frantically, and I realise that it must be a novelty to be fucking someone without breasts of their own, who finds her's so desirable."
    anna.say "Death by anal whore...that'd look so cool on your tombstone!"
    "She's panting by now, and I can sense that I'm soon going to cum."
    "It'd be nice to lie here and let her ride me to the end, but I want to change the balance, to be the one on top at the end."
    "My pace quickens, and soon she's almost yelping in time with my thrusts, arching her back in sympathy."
    show expression "anna cowgirl "+p+" "+c+" cum "+x
    "Finally she wraps her legs around my waist and cries out as I climax inside of her, the waves of her own orgasm already taking hold."
    hide expression "anna cowgirl "+p+" "+c+" cum "+x
    "I stay inside of her as she gives in and cums, enjoying the sensation of it making her twitch and twinge."
    show expression "anna cowgirl "+p+" "+c+" b"
    if p == "anal":
        hero.say "Worth the wait, to have a real cock back inside of you?"
        anna.say "Mmm...more like a magic wand...one that turns me into a little anal whore!"
    hide expression "anna cowgirl "+p+" "+c+" b"
    call sleep from _call_sleep_1
    $ game.room = "bedroom1"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
