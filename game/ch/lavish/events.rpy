init python:

    Event(**{
        "name":"lavish_init",
        "label": ["lavish_init"],
        "game_conditions": {"not_done":'office_party'},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "lavish_give_christmas",
        "label": ["lavish_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas"},
        "girls_conditions": {"lavish":{"min_love":50,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "lavish_give_birthday",
        "label": ["lavish_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday"},
        "girls_conditions": {"lavish":{"min_love":40,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "lavish_give_valentine",
        "label": ["lavish_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine"},
        "girls_conditions": {"lavish":{"min_love":100,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name":"lavish_start",
        "label": ["lavish_start"],
        "game_conditions": {"done":'office_party', "activity":["work","workhard","work_personal","workhard_personal"]},
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name":"lavish_event_02",
        "label": ["lavish_event_02"],
        "game_conditions": {"done":'lavish_start', "activity":["work","workhard","work_personal","workhard_personal"]},
        "girls_conditions": {"lavish":{"min_love":40,"room":"office"}},
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name":"lavish_fix",
        "label": ["lavish_fix"],
        "game_conditions": {"done":'lavish_event_02'},
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name":"lavish_fix_2",
        "label": ["lavish_fix_2"],
        "game_conditions": {"done":'lavish_fix'},
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "lavish_investigation_callback",
        "label": ["lavish_investigation_callback"],
        "game_conditions": {"hours":(15,21)},
        "girls_conditions": {"lavish":{"countermin_investigationcallback":2, "present": False}},
        "do_once": True
        })

label lavish_fix_2:
    $ lavish.set_flag("nodate",False)
    $ lavish.set_flag("nokiss",False)
    return

label lavish_fix:
    $ lavish_love_max = 200
    return

label lavish_start:
    $ lavish_love_max = 40
    $ if "lavish" in HIDDEN: HIDDEN.remove("lavish")
    show aletta work
    "There’s a knock that breaks me from my concentration, and I’m happy to tear my eyes off my blinding white computer screen for a moment to glance over to Aletta behind me."
    aletta.say "Hey."
    "I roll myself back in my seat a bit, stretching my arms and arching my back as I turn my chair away from my desk to face her."
    hero.say "What’s up?"
    aletta.say "I wanted to introduce you to the new intern."
    "I stifle a sigh, forcing a thin smile instead."
    "Great. Another intern around the office to be bombarding me and everyone in earshot with stupid questions, and mucking things up that, eventually, will get back around to me to fix."
    "The last kid that interned here, I was about ready to push out the window by the time he was heading back to classes and leaving us for good."
    "But, I mean, I should have known better, at this point."
    show aletta work at left
    show lavish work at right
    "Of course the face that stares back at me when Aletta steps aside is a stunning, doe-eyed young woman that immediately makes my heart skip a beat."
    aletta.say "This is Lavish, you already met her at the party. She’s going to be around the office for now, and I told her she could come to you if she needed help."
    "Lavish gives me a soft, demure smile that’s sophisticated and classic in its beauty."
    lavish.say "It’s nice to meet you."
    aletta.say "Lavish, this is your manager."
    "I get out of my seat quickly, eager to step forward and extend my hand to her."
    "Her fingers are baby soft, warm, and delicate when she extends her hand to shake mine. I find myself wishing I didn’t have to let go, savoring the feeling of it there, small, in my palm."
    "Something about the soft, pretty curve to her face makes me want to spin her around by that hand, pull her in, and dance with her."
    "A whiff of something drifts to me -- some kind of deep, spicy perfume that almost entices me in closer to her. Almost."
    "My boss is watching, after all."
    "Maybe some other time."
    "Aletta folds her arms across her chest, and I realize that maybe I have been shaking the intern’s hand for a moment too long, quickly letting it go and stepping back."
    "Lavish doesn’t seem to mind. She’s got her gaze fixed on me, the smile curling at her lips remaining."
    "In those deep, dark eyes, I could almost swear I see stars."
    "Why’s she looking at me like that?"
    aletta.say "I trust you’re going to take care of her,"
    "Aletta says strictly, stepping forward and ushering Lavish a step backwards with a gentle, maternal hand on the arm. She shoots me a sharp glance from behind her glasses."
    aletta.say "No distractions."
    "I flash a grin."
    hero.say "What, me?"
    aletta.say "Hmm."
    "The two of them turn from me and head back into the heart of the office, though I could swear Lavish lingers just a split second longer than she needed to, glancing once more back over her shoulder at me."
    "I almost expect her to tip me a seductive wink when she does. But she turns back around, collected, and follows Aletta away, the two of them speaking something to each other that I can no longer hear."
    "Nice."
    "Can’t complain at all about seeing a goddess like that around the office."
    "There’s a stupid smile on my face when I turn back to my computer, breathing an airy sigh and flopping myself back into my seat."
    "No distractions, Aletta said. But how am I supposed to focus on work, now?"
    return

label lavish_event_02:
    $ lavish_love_max = 200
    "I roll myself back from my computer desk, leaning back into my seat and pinching the bridge of my nose."
    "I need to find a file for the project I’m working on, but it’s not scanned. Of course it’s not."
    "The office is so behind on that, even though they were supposed to hire temp workers to get it done months ago."
    "A brilliant idea strikes me, and my eyes light back up as I lean myself forward, snatching my phone from its cradle."
    "Who needs temp workers when you’ve got that new, sexy intern, anyway?"
    "I punch in the extension to her desk, and to my disappointment it rings… and rings… and goes to her voicemail."
    "As soothing and sensual as her voice is on the prerecorded message, it’s not what I wanted to hear."
    "I frown as I set my phone back down and push myself to my feet."
    "Fine. Do some legwork myself."
    "The file room isn’t far from my desk, anyway, and I turn the corner and push open the heavy door, slipping inside and letting it click closed behind me."
    show bg office with fade
    show lavish files at bottom_to_top
    "I realize right away that I’m not in here alone. I can hear shuffling and the rattling metal sound of drawers being pulled open that probably drowned out the sound of my arrival."
    "Just to make sure I don’t give some middle-aged lady a heart attack, I make my way over to the rows of cabinets that the sounds came from, raising a fist to knock on one and announce my presence."
    "But I freeze."
    "Lavish didn’t answer my call because she’s already here."
    "A pair of long, silky-smooth legs greets my vision, rubbing together with an innocent sensuality as she shifts her weight, focused on digging through the folders."
    "Her ass is plump and rounded beautifully by the heels she’s got on today, and though she’s a few feet down the aisle it’s so prominently in my face it feels like I could take a bite from where I stand."
    "Her stockings cling desperately to the meat of her thighs, pinching the flesh in at the elastics with an alluring sheen under the fluorescent lights. I can see a set of puffy lips between her thighs, clearly visible from beneath her skirt, the panties she’s wearing so thin they’re nearly sheer, and I just about lose it."
    "Ideas of making my way over to her and taking her, right there in that position, flood my mind so suddenly I feel like I could drown in them."
    "I quickly adjust myself through my pocket and clear my throat to dismiss the thoughts before this gets out of hand."
    hide lavish files
    show lavish blush
    "Lavish jumps a little bit at the sound, straightening herself quickly and looking back at me."
    show lavish normal
    lavish.say "Oh,"
    "She sighs the word, as if in relief."
    "Her gaze seems to trail down me for a moment, lingering a moment near my waistline before snapping back up to my face."
    "It’s only you."
    hero.say "‘Only’ me?"
    "I’m teasing her, but a faint blush scatters attractively across her cheeks anyway."
    lavish.say "Did you need something?"
    hero.say "Actually, yeah. I came here to look for the Reynholm files."
    lavish.say "Oh. I could have grabbed those for you."
    hero.say "I called your desk, actually, but I must’ve just missed you."
    lavish.say "My apologies,"
    "I don’t know if I’m imagining it, but her voice seems to have softened and deepened a bit, like the voice a woman uses in the bedroom."
    "I can almost feel my heartbeat quicken in response, trained like Pavlov’s dogs."
    lavish.say "Let me get that for you now."
    show lavish files at bottom_to_top
    "If she was bent over that way out of innocence the first time, I’m hard-pressed to believe she is now."
    "Clutching the files she’s already holding to her breasts, she bends over again, slow, and reaches down to the very bottom drawer, pulling it out and flicking her fingertips along the papers inside."
    "I’m not interested in the drawer at all. My gaze stays fixed on the show she’s obviously putting on for me."
    "This time when she shifts her weight, making the muscles in her ass and thighs flex and her thighs glide together in her stockings, it’s a much more exaggerated motion, and I pulse appreciatively in response, keeping one hand tactfully in my pocket."
    "I realize all at once that she wants it. She glances back at me, subtly, over her shoulder, and though it’s beneath her full lashes I catch it anyway."
    "But this is work, and I can’t make assumptions. Maybe she’s just one of those office teases. I have to get to know her, first."
    "If she wants it, she can absolutely get it."
    lavish.say "Got it."
    hide lavish files
    show lavish normal
    "She straightens herself again, and just like that, the show’s over."
    "Holding the file I was looking for in her free hand, she makes her way over to me, setting it down gently into mine."
    hero.say "Thanks."
    "I clear my throat again, to make sure I don’t sound as breathless as the throbbing tension in this isolated room is making me feel."
    hero.say "I appreciate the help."
    show lavish happy
    lavish.say "My pleasure."
    "I’m sure I’m not imagining it now that she practically purrs the words."
    show lavish blush
    lavish.say "Please don’t hesitate to give me a call if you ever need anything at all."
    "She slips past me, and I catch a whiff of that perfume again."
    "I know I’m never going to be able to smell it in any mall or on any stranger ever again without remembering this moment."
    "I hear the door click shut behind me and exhale a whooshing sigh, waiting for the tension in me to go down, too, before I go back to my desk."
    "Back to work."
    return

label lavish_give:
    if not "lavish's tie" in hero.inventory.keys() and lavish.love >= 100:
        $ gift = Equip("lavish's tie", money_cost = 150, type = "accessory", effects = {"lavish":100,"charm":10,"princess":20})
        "She hands me a pretty nice tie."
        hero.say "Wow !\nThanks!"
        lavish.say "It's nothing..."
    if not "Lavish's lucky panties" in hero.inventory.keys() and lavish.sub >= 50 and lavish.love >= 100:
        $ gift = Item("lavish's lucky panties", money_cost = 500)
        "She hands me a pair of panties."
        hero.say "Wow !\nThanks!"
        show lavish blush
        lavish.say "They are my lucky ones..."
        if not "luck" in hero.skills:
            $ hero.skills.append("luck")
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label lavish_give_valentine:
    show lavish
    "Lavish walks hesitantly towards me."
    call lavish_greet from _call_lavish_greet_7
    show lavish blush
    lavish.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Lavish hands me a box of chocolates."
    hero.say "Thank you, Lavish."
    $ hero.gain_item(gift)
    hide lavish
    return

label lavish_give_birthday:
    show lavish
    "Lavish walks towards me."
    call lavish_greet from _call_lavish_greet_8
    show lavish happy
    lavish.say "Happy birthday [hero.name]!"
    call lavish_give from _call_lavish_give
    return

label lavish_give_christmas:
    show lavish
    "Lavish walks towards me."
    call lavish_greet from _call_lavish_greet_9
    show lavish happy
    lavish.say "Merry christmas [hero.name]."
    call lavish_give from _call_lavish_give_1
    return

label lavish_init:
    if "lavish" not in HIDDEN:
        $ HIDDEN.append("lavish")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
