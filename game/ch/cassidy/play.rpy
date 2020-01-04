init python:
    Activity(**{
        "name": "cassidy_tittyfuck",
        "display_name": "Demand bj",
        "label":["cassidy_tittyfuck"],
        "duration": 1,
        "game_conditions": {"activity":"interact", "room":['personal']},
        "girls_conditions": {"cassidy":{"flag_status":"pet"}},
        "once_day": True,
        "icon": "blowjob",
        })

    Activity(**{
        "name": "cassidy_remove_top",
        "display_name": "Demand remove top",
        "label":["cassidy_remove_top"],
        "duration": 0,
        "game_conditions": {"activity":"interact", "room":['personal']},
        "girls_conditions": {"cassidy":{"flag_status":"pet", "flag_topless": False}},
        "icon": "caressboobs",
        })

    Activity(**{
        "name": "cassidy_wear_top",
        "display_name": "Demand wear top",
        "label":["cassidy_wear_top"],
        "duration": 0,
        "game_conditions": {"activity":"interact", "room":['personal']},
        "girls_conditions": {"cassidy":{"flag_status":"pet", "flag_topless": True}},
        "icon": "caressboobs",
        })

    Activity(**{
        "name": "cassidy_grope_boobs",
        "display_name": "Grope boobs",
        "label":["cassidy_grope_boobs"],
        "duration": 1,
        "game_conditions": {"activity":"interact", "room":['personal']},
        "girls_conditions": {"cassidy":{"flag_status":"pet", "flag_topless": True}},
        "icon": "boobnobra",
        })

    Activity(**{
        "name": "cassidy_finger",
        "display_name": "Finger",
        "label":["cassidy_finger"],
        "duration": 1,
        "game_conditions": {"activity":"interact", "room":['personal']},
        "girls_conditions": {"cassidy":{"flag_status":"pet"}},
        "icon": "finger",
        })







label cassidy_tittyfuck(topless=False):
    "Cassidy gets down on her knees and slowly unzips my fly. It takes only the barest touch and my cock roars to life in her fingers."
    if not topless:
        show cassidy tittyfuck
        "She takes my cock and puts it beneath her top, cradling it between her delicious breasts. Oh, those beautiful breasts. It's really too bad they're covered up."
        hero.say "Take your top off."
        "Wordlessly, she obeys."
    else:
        "She slides those beautiful breasts around my cock, hugging it with her warmth. I couldn't keep from having a full erection if I wanted to, and I don't want to!"
    show cassidy tittyfuck topless
    "She moves her entire body, caressing my shaft up and down with her tits. Her eyes focus on mine the entire time, and the more I enjoy myself, the bigger her smile gets."
    cassidy.say "Do you like this?"
    hero.say "Oh yeah. Don't stop."
    show cassidy open
    cassidy.say "Are you ready for what's next?"
    show cassidy dickhead
    "I don't have to answer in words; my cock is warm and the precum is mixing with her sweat to lubricate her. I'm clearly ready."
    show cassidy suck
    "She leans her head forward and takes the tip of my shaft into her mouth. Her tongue flicks around, while her tits continue to massage me."
    hero.say "Faster!"
    show cassidy closed
    "She complies, speeding up and taking just the head into her mouth."
    hero.say "Oh, fuck, Cassidy, you were right about this being the best damn blowjob I've ever had!"
    cassidy.say "Mf, mmmf mmf mf!"
    "I have no idea what she tried to say, and it doesn't matter. I'm about to explode."
    menu:
        "Cum in her mouth":
            show cassidy tittyfuck mouthcum
            $ cassidy.love += 1
            "I don't have the time or inclination to pull out, and I explode between her lips, filling her mouth so much that it leaks all over me."
            "She doesn't stop, though, instead she just slows down. With every caress I can feel the muscles in my dick spasm, half objection and half ecstasy."
            "Until finally, I can't take it anymore, and I go completely limp between her tits."
            hide cassidy tittyfuck
            show cassidy topless casual normal blush wet
            $ cassidy.set_flag('topless', True, 1)
            $ cassidy.set_flag('wet', True, 1)
            if cassidy.sub > 75:
                cassidy.say "Did I do a good job, Master?"
            else:
                cassidy.say "I hope it was good for you."
            hero.say "Yes, absolutely!"
            $ cassidy.set_flag('humiliation', 1, mod='+')
        "Cum on her face":
            $ cassidy.sub += 1
            hero.say "I'm going to cum!"
            show cassidy tittyfuck up cum
            "I pull back a little, and Cassidy raises her head."
            "At first it's just a spurt, but when I look into her eyes, it just keeps coming and coming, dousing her face in sticky, gooey wetness."
            show cassidy tittyfuck facecum
            cassidy.say "Well, I don't think you enjoyed that at all, Sweetie."
            hero.say "Mmmm."
            hide cassidy tittyfuck
            $ cassidy.set_flag('topless', True, 1)
            $ cassidy.set_flag('facecum', True, 1)
            $ cassidy.set_flag('humiliation', 1, mod='+')
            show cassidy topless casual normal blush facecum
            "I wanted to be more eloquent. I was thinking \"Yeah, that was fucking awesome\", but that was all I could get out."
    return

label cassidy_remove_top:
    show cassidy
    hero.say "Take off your top."
    $ cassidy.set_flag('topless', True, 'day')
    show cassidy topless
    if cassidy.sub < 90:
        cassidy.say "Yes, Master."
    else:
        cassidy.say "Anything you want, Master!"
    hide cassidy
    return

label cassidy_wear_top:
    show cassidy
    hero.say "Put your top back on."
    $ cassidy.set_flag('topless', False, 'day')
    show cassidy -topless
    if cassidy.sub < 90:
        cassidy.say "Yes, Master."
    else:
        cassidy.say "Anything you want, Master!"
    hide cassidy
    return

label cassidy_grope_boobs:
    show cassidy
    "I put my hands on Cassidy's bare chest, running my fingers along her skin, making circles around that great bosom until I get to her nipples."
    if cassidy.love > 160:
        show cassidy happy blush
        "She responds immediately, her nipples hardening almost on command."
        "She makes a soft, happy sound."
    elif cassidy.love > 100 or cassidy.sub > 75:
        show cassidy blush
        "It takes a few seconds, but her nipples respond, hardening under my gentle touch."
        "She squeaks just slightly as I pull my hands away."
        if not cassidy.get_flag_value('groped'):
            $ cassidy.love += 1
        $ cassidy.set_flag('humiliation', 1, mod='+')
    else:
        show cassidy sad blush
        "She stands there, quite still, allowing me to touch her freely but not responding."
        "After a few moments, her nipples finally stiffen a little bit under my fingers. I tweak them gently before finishing."
        $ cassidy.set_flag('humiliation', 2, mod='+')
        if not cassidy.get_flag_value('groped'):
            $ cassidy.sub += 1
    hide cassidy
    $ cassidy.set_flag('groped', True, 'day', '+')
    return

label cassidy_finger:
    show cassidy
    "I put one hand beneath Cassidy's skirt, sliding it up her thigh toward her pussy."
    if cassidy.love > 160 or cassidy.sub == 100:
        $ cassidy.set_flag('wet', True, 'day')
        show cassidy happy blush wet
        "She's already wet and ready when I get there. I press first one finger, then two into her warm flesh, separating her lips."
        "I find her clitoris and gently massage it, back and forth inside her vulva, not really penetrating but clearly stimulating her."
        "She wraps an arm around my neck and rests her head against my shoulder, moaning softly."
        if not cassidy.get_flag_value('fingered'):
            "I feel her spasm against me, and a new rush of wetness covers my hand."
        else:
            cassidy.say "I love it when you touch me, Master!"
    elif cassidy.love > 100 or cassidy.sub > 80:
        show cassidy blush
        "When I get there, she is warm but not quite wet. But as soon as I separate her lips and touch her clit, the juices start to flow."
        "As I gently caress her clit, a soft half-hum, half-moan comes from the back of her throat."
        hero.say "Do you like that, my pet?"
        cassidy.say "Yes, yes I do, Master."
        $ cassidy.set_flag('wet', True, 'day')
        show cassidy blush wet
        if not cassidy.get_flag_value('fingered'):
            $ cassidy.love += 1
        $ cassidy.set_flag('humiliation', 1, mod='+')
    else:
        show cassidy sad
        "She stands there, quite still, allowing me access, but not responding. When I reach her pussy it is warm but dry."
        "I separate her pussy lips and gently, carefully slip inside and find her clit."
        show cassidy blush
        "After a few moments, her juices finally start to flow, albeit slowly."
        "I continue working her with my finger until I'm sure she's worked up, and then finally withdraw my hand."
        "I make a show of licking my fingers clean while she watches me."
        if not cassidy.get_flag_value('fingered'):
            $ cassidy.sub += 1
        $ cassidy.set_flag('humiliation', 2, mod='+')
    hide cassidy
    $ cassidy.set_flag('fingered', True, 'day', '+')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
