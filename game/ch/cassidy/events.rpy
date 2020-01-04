init python:
    Event(**{
        "name":"cassidy_init",
        "label": ["cassidy_init"],
        "game_conditions": {"not_done":'office_party'},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "cassidy_give_christmas",
        "label": ["cassidy_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas"},
        "girls_conditions": {"cassidy":{"min_love":50,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "cassidy_give_birthday",
        "label": ["cassidy_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday"},
        "girls_conditions": {"cassidy":{"min_love":40,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "cassidy_give_valentine",
        "label": ["cassidy_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine"},
        "girls_conditions": {"cassidy":{"min_love":100,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "cassidy_preg_talk",
        "label": ["cassidy_preg_talk"],
        "duration": 0,
        "girls_conditions": {"cassidy":{"countermin_pregnant":3, "flag_toldpreg":False, 'present': True}},
        "game_conditions":{"flag_dateinprogress":False, "flag_female":0},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "cassidy_preg_finish",
        "label": ["cassidy_preg_finish"],
        "duration": 0,
        "girls_conditions": {"cassidy":{"countermin_pregnant":7, "flag_toldpreg":True}},
        "game_conditions":{"flag_dateinprogress":False, "flag_female":0},
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name":"cassidy_start",
        "label": ["cassidy_start"],
        "game_conditions": {"done":'office_party', "activity":["work","workhard","work_personal","workhard_personal"]},
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "cassidy_fix",
        "label": ["cassidy_fix"],
        "game_conditions": {"done": "cassidy_start"},
        "do_once": True,
        "quit": False,
    })

    Event(**{
        "name": "cassidy_piercing_fix",
        "label": ["cassidy_piercing_fix"],
        "game_conditions": {"done": "cassidy_start"},
        "do_once": True,
        "quit": False,
    })

    Event(**{
        "name": "cassidy_start_investigation",
        "label": ["cassidy_start_investigation"],
        "duration": 0,
        "priority": 1000,
        "girls_conditions":{"cassidy":{"countermin_start_investigation": 7}},
        "game_conditions":{"activity":["work_personal","workhard_personal"],"done":'cassidy_start', "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_setup_meeting",
        "label": ["cassidy_setup_meeting"],
        "duration": 0,
        "priority": 1000,
        "girls_conditions":{"cassidy":{"countermin_finish_investigation": 2, "present": False}},
        "game_conditions":{"hours": (6, 14)},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_hold_meeting",
        "label": ["cassidy_hold_meeting"],
        "duration": 0,
        "priority": 1000,
        "game_conditions":{"room": "map", "hours": (0, 0), "done": "cassidy_setup_meeting", "flag_underinvestigation":True},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_investigation_complete",
        "label": ["cassidy_investigation_complete"],
        "duration": 0,
        "priority": 1000,
        "girls_conditions":{"cassidy":{"countermin_finish_investigation": 7}},
        "game_conditions":{"hours": (8, 20)},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_new_assistant",
        "label": ["cassidy_new_assistant"],
        "duration": 0,
        "game_conditions":{"done": "cassidy_investigation_complete", "room":["personal"]},
        "girls_conditions":{"cassidy":{"present": True, "flag_assistantdelay":False}},
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_bad_day",
        "label": ["cassidy_bad_day"],
        "duration": 0,
        "game_conditions":{"done": "cassidy_new_assistant", "room":["personal"]},
        "girls_conditions":{"cassidy":{"present": True, "min_love": 80}},
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_overhear_argument",
        "label": ["cassidy_overhear_argument"],
        "duration": 0,
        "game_conditions":{"done": "cassidy_bad_day", "activity":"coffee_break"},
        "girls_conditions":{"cassidy":{"countermin_dwaynefight":1}},
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_dwayne_fight_fallout",
        "label": ["cassidy_dwayne_fight_fallout"],
        "duration": 0,
        "game_conditions":{"done": "cassidy_overhear_argument", "room":["personal"]},
        "girls_conditions":{"cassidy":{"present": True, "countermin_dwaynefallout": 1}},
        "priority": 1000,
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_dwayne_visit",
        "label": ["cassidy_dwayne_visit"],
        "duration": 0,
        "game_conditions":{"done": "cassidy_overhear_argument", "room":["personal"]},
        "girls_conditions":{"cassidy":{"present": False, "countermin_dwaynevisit": 7}},
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_aletta_fight",
        "label": ["cassidy_aletta_fight"],
        "duration": 0,
        "game_conditions":{"done": "cassidy_overhear_argument", "room":["personal"]},
        "girls_conditions":{"cassidy":{"present": False, "countermin_alettafight": 7}},
        "priority": 1000,
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_needs_comfort",
        "label": ["cassidy_needs_comfort"],
        "duration": 0,
        "game_conditions":{"done": "cassidy_overhear_argument", "room":["livingroom"]},
        "girls_conditions":{"cassidy":{"countermin_needscomfort": 3}},
        "priority": 1000,
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_aletta_make_nice",
        "label": ["cassidy_aletta_make_nice"],
        "duration": 0,
        "game_conditions":{"activity":["work_personal","workhard_personal"], "done": "cassidy_needs_comfort", "room":["personal"]},
        "girls_conditions":{"cassidy":{"countermin_makenice": 1}},
        "priority": 1000,
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "cassidy_dom_boredom",
        "label": ["cassidy_dom_boredom"],
        "duration": 1,
        "girls_conditions":{"cassidy": {"countermin_boredom": 45, "present": True}},
        "quit": True,
        "do_once": True,
        })

    Event(**{
        "name": "cassidy_dom_oral",
        "label": ["cassidy_dom_oral"],
        "duration": 1,
        "girls_conditions":{"cassidy": {"max_sub": -50, "present": True}},
        "game_conditions":{"chances": 5, "room":["personal"]},
        "quit": True,
        "once_day": True,
        })

    Event(**{
        "name": "cassidy_humiliation_decay",
        "label": ["cassidy_humiliation_decay"],
        "duration": 0,
        "girls_conditions": {"cassidy":{"flagmin_humiliation":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "cassidy_humiliation_growth",
        "label": ["cassidy_humiliation_growth"],
        "duration": 0,
        "girls_conditions": {"cassidy":{"present":True, "flag_status": 'pet'}},
        "conditions": ['cassidy.get_flag_value("facecum") or cassidy.get_flag_value("wet") or cassidy.get_flag_value("topless") or cassidy.get_flag_value("bottomless")'],
        "once_day":False,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "cassidy_humiliation_check",
        "label": ["cassidy_humiliation_check"],
        "duration": 0,
        "girls_conditions": {"cassidy":{"flagmin_humiliation":50, "flag_status": 'pet'}},
        "once_day":False,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "cassidy_humiliated_01",
        "label": ["cassidy_humiliated_01"],
        "duration": 0,
        "girls_conditions": {"cassidy":{"flag_humiliated":1}},
        "game_conditions":{"room":["personal"]},
        "do_once":True,
        "quit": True,
        })

    Event(**{
        "name": "cassidy_humiliated_02",
        "label": ["cassidy_humiliated_02"],
        "duration": 0,
        "girls_conditions": {"cassidy":{"flag_humiliated":2}},
        "game_conditions":{"room":["personal"]},
        "do_once":True,
        "quit": True,
        })

    Event(**{
        "name": "cassidy_outfit_picker",
        "label": ["cassidy_outfit_picker"],
        "duration": 0,
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

label cassidy_piercing_fix:
    $ p = cassidy.get_piercings()
    if p['tongue']['expressions'] == ['surprised']:
        $ p['tongue']['expressions'] = ['happy']
        $ cassidy.set_flag("newpiercings", p)
    return

label cassidy_outfit_picker:
    if randint(1, 3) == 1:
        $ cassidy.set_flag('gold', True)
    return

label cassidy_humiliation_check:
    $ cassidy.set_flag('humiliated', 1, mod='+')
    return

label cassidy_humiliation_decay:

    $ cassidy.set_flag('humiliation', min(cassidy.get_flag_value('humiliation'), 5 + cassidy_love / 10), mod='-')
    return

label cassidy_humiliation_growth:
    if cassidy.get_flag_value('topless') and (cassidy.love < 80 or cassidy.sub < 60):
        $ cassidy.set_flag('humiliation', 1, mod='+')

    if cassidy.get_flag_value('bottomless') and (cassidy.love < 100 or cassidy.sub < 70):
        $ cassidy.set_flag('humiliation', 1, mod='+')

    if cassidy.get_flag_value('wet') and (cassidy.love < 120 or cassidy.sub < 80):
        $ cassidy.set_flag('humiliation', 1, mod='+')
        if randint(1, 3) == 1:

            $ cassidy.set_flag('wet', False)

    if cassidy.get_flag_value('facecum') and (cassidy.love < 160 or cassidy.sub < 90):
        $ cassidy.set_flag('humiliation', 1, mod='+')
        if randint(1, 3) == 1:

            $ cassidy.set_flag('facecum', False)
    return

label cassidy_humiliated_01:
    show cassidy sad
    cassidy.say "I'm sorry, [hero.name], but I can't take this anymore."
    hero.say "Take what?"
    cassidy.say "Being your sex slave! You're humiliating. You make me hang around in here with cum on my face, or without my top, suck you whenever you want."
    cassidy.say "I can't take it anymore. I need out."
    hero.say "Well, you know what will happen."
    show cassidy cry
    cassidy.say "Please, please don't do that!"
    menu:
        "Offer to back off":
            hero.say "Okay, maybe I'll back off a little, if you stay?"
            "Cassidy sniffles a little bit, while giving me a look filled with mistrust."
            cassidy.say "I don't know."
            hero.say "Well, what do you need?"
            cassidy.say "I don't know. Just...be nicer to me, maybe?"
            hero.say "That's it? Be nicer?"
            cassidy.say "Maybe not quite so many blowjobs?"
            hero.say "There still has to be blowjobs."
            cassidy.say "Fine, but come on."
            hero.say "Okay, fewer blowjobs."
            cassidy.say "And don't make me walk around with cum on my face. That gets nasty and gross really fast."
            hero.say "You'd rather swallow?"
            cassidy.say "Oh God, yes I would."
            hero.say "Fine."
            cassidy.say "You promise?"
            hero.say "I promise."
            show cassidy normal
            cassidy.say "Okay. I'm trusting you, [hero.name]."
            hero.say "You still have to call me Master, though."
            cassidy.say "Fine, I'm trusting you, Master."
            $ cassidy.love += 1
            $ cassidy.sub += 1
            $ cassidy.set_flag('humilation', 0)
        "Refuse":
            hero.say "Nope, this is your punishment for being a bitch. Take it or leave it. I have no problem turning your father in."
            cassidy.say "Fuck you, [hero.name]. Do whatever you want."
            "Cassidy heads for the exit. I grab her arm as she goes by and she yanks it away from me."
            cassidy.say "{b}Don't touch me, [hero.name]{/b}. Don't touch me {b}ever again{/b}!!"
            "And with that she runs for the exit. I guess I have to figure out what to do about Dwayne, now."
            $ game.set_flag('firedwayne', True)
            $ HIDDEN.append('cassidy')
    return

label cassidy_humiliated_02:
    show cassidy sad
    cassidy.say "You {b}promised{/b}, [hero.name]! You promised me you'd back off, but, ugh! I'm done with this! Done!"
    hero.say "Cassidy, wait!"
    cassidy.say "Fuck you, [hero.name]. Do whatever you want."
    "Cassidy heads for the exit. I grab her arm as she goes by and she yanks it away from me."
    cassidy.say "{b}Don't touch me, [hero.name]{/b}. Don't touch me {b}ever again{/b}!!"
    "And with that she runs for the exit. I guess I have to figure out what to do about Dwayne, now."
    $ game.set_flag('firedwayne', True)
    $ HIDDEN.append('cassidy')
    return

label cassidy_fix:
    $ cassidy.set_counter('start_investigation')
    return

label cassidy_start:
    $ cassidy_love_max = 40
    $ cassidy.set_counter('investigation_start')
    $ cassidy.set_flag('nokiss', True)
    $ cassidy.set_flag('nodate', True)
    $ if "cassidy" in HIDDEN: HIDDEN.remove("cassidy")
    "I am deep in the middle of the last thing I need to do on this task when my door bursts open and a stunning brunette walks right in, as though it was her office, not mine."
    show cassidy casual normal
    "She slams the door closed behind her, and for a moment I am too stunned -- both by her boldness and by her beauty -- to say anything."
    cassidy.say "You, what's-your-name, my valet is sick and I need a replacement."
    hero.say "What do you -- I'm sorry, what?"
    cassidy.say "Well you're obviously not that bright. Should I use smaller words?"
    "The conversation is definitely getting weirder, but I have to get it together and say something intelligible or this is going to go from weird to embarassing."
    hero.say "I understand the words, whoever you--"
    "Oh shit. I was halfway through that sentence when I recognized her from the office party. That's Cassidy. The daughter of the CEO."
    hero.say "--I mean Cassidy."
    cassidy.say "Oh good. The car is downstairs, we can run by my house and then go to the airport and then we can go to Switzerland. The jet's scheduled to leave in an hour, so there's no time to waste, and we've got a busy schedule there. Get moving!"
    "Cassidy places her hands at her hips and taps her foot, waiting for me to go to the car, I guess."
    hero.say "Switzerland?!"
    "I really should be able to do better than that."
    cassidy.say "Yes, Switzerland. Are you hard of hearing or just stupid?"
    hero.say "Cassidy, I think there's a misunderstanding here."
    cassidy.say "Oh yes? What is it that you don't understand?"
    hero.say "No, it's you that doesn't understand. I'm not your valet. I don't work for you."
    "Cassidy points one long finger at me, and then my desk."
    cassidy.say "You work at this company, right?"
    hero.say "Yes, this is my desk and my office."
    cassidy.say "Right. And Dwayne runs this company, right?"
    hero.say "Yes, he's the CEO."
    cassidy.say "Good, then you work for Dwayne which means you work for me. Now get moving!"
    hero.say "Okay look if you really need, I'll drive you to the airport, but I'm not going to Switzerland."
    show cassidy angry
    cassidy.say "Did you just disobey me?"
    "Cassidy does not look like the sort who is used to having someone tell her no. I need to find a way to get out of this without losing my job."
    hero.say "Look, let me find you a valet. I know a service I can call..."
    show cassidy happy
    cassidy.say "No, I want YOU. Look, if it's about the money I'll tell Daddy to give you a bonus. And if you're really good maybe I'LL give you a bonus."
    hero.say "No, it's not about the money, it's--"
    "Wait, what did she mean by giving me a bonus herself?"
    cassidy.say "Well, what's it about then?"
    "I take a deep breath and think as fast as I can."
    hero.say "I have a lot of work to do here. I can't leave, there's nobody else here who can do it, and it has to be done by tomorrow. Or the company could lose a lot of money, and Dwayne will be pissed."
    "I really hope my skill at lying is up to the task, because that is one of the biggest lines of bullshit I've ever fed a girl."
    show cassidy angry
    cassidy.say "Nobody says no to me...whatever your name is. Nobody. Call yourself, have someone meet me downstairs in 10 minutes. And he'd better be as hot as you are."
    cassidy.say "And I'm going to make you regret this."
    "With that, she turns on her heel and marches back out of my office, slamming the door behind her."
    hide cassidy
    "I quickly call a car service and it costs a lot of money, but I got someone to agree to it."
    "There's no way anyone will be down there in ten minutes, though. This...this could come back to haunt me."
    return

label cassidy_give:

    $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "She hands me box, obviously from a pastry shop."
    hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label cassidy_give_valentine:
    show cassidy
    "Cassidy walks hesitantly towards me."
    call cassidy_greet from _call_cassidy_greet_7
    show cassidy blush
    cassidy.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Cassidy hands me a box of chocolates."
    hero.say "Thank you, Cassidy."
    $ hero.gain_item(gift)
    hide cassidy
    return

label cassidy_give_birthday:
    show cassidy
    "Cassidy walks towards me."
    call cassidy_greet from _call_cassidy_greet_8
    show cassidy happy
    cassidy.say "Happy birthday [hero.name]!"
    call cassidy_give from _call_cassidy_give
    return

label cassidy_give_christmas:
    show cassidy
    "Cassidy walks towards me."
    call cassidy_greet from _call_cassidy_greet_9
    show cassidy happy
    cassidy.say "Merry christmas [hero.name]."
    call cassidy_give from _call_cassidy_give_1
    return

label cassidy_init:
    if "cassidy" not in HIDDEN:
        $ HIDDEN.append("cassidy")
    return

label cassidy_preg_talk:
    $ cassidy.set_flag('toldpreg')
    show cassidy
    cassidy.say "Hey, [hero.name], can we talk?"
    hero.say "Sure, Cassidy. What's up?"
    cassidy.say "So you know how a few days ago you didn't use a condom? Well, you know how it works."
    "Cassidy puts her hand on her belly."
    cassidy.say "There's a little [hero.name] growing inside of me."
    hero.say "Oh, oh. Oh wow. I mean..."
    if cassidy.love < 200:
        cassidy.say "Look, [hero.name], I don't want it. I'm not ready to have a baby. I'm going to have an abortion."
        menu:
            "No! You can't!":
                if cassidy.get_status() == 'pet':
                    show cassidy sad
                    cassidy.say "No, [hero.name], our arrangement doesn't cover this. I'm not giving you a choice."
                    "Do I really want her to keep the child? She seems pretty adamant, but...it's my baby! And she's my pet!"
                    menu:
                        "Insist":
                            hero.say "No, Cassidy. you can't abort the baby. I forbid it."
                            show cassidy cry
                            cassidy.say "[hero.name], you can do whatever you want, then. I quit."
                            if cassidy.get_flag_value('collared'):
                                $ cassidy.set_flag('collared', False)
                                "She reaches toward her neck and unfastens the collar from her neck, tossing it roughly aside."
                            cassidy.say "We are done."
                            "And then she runs past me as quickly as she can. Gone. Just like that. Cassidy AND my baby."
                            $ HIDDEN.append('cassidy')
                            call cassidy_preg_abort
                            $ game.set_flag('firedwayne', True)
                        "Let it go":
                            hero.say "Okay. I guess. It's your body, but...damn it."
                            show cassidy cry
                            "Cassidy steps toward me and puts her hand on my face. She speaks through tears that slowly drip down her cheeks."
                            cassidy.say "Look, maybe...someday, okay? But not today. Not now."
                            $ cassidy.love += 10
                            call cassidy_preg_abort
                            cassidy.say "And thank you for being reasonable. I'm sorry this happened. Next time, wrap it up, okay?"
                            hero.say "Yeah, I guess."
                else:
                    show cassidy angry
                    cassidy.say "Fuck off, [cassidy.heroname]. My body, my rules. I don't want kids, and if you don't like it, you can fuck right the hell off."
                    "Cassidy's vehemence takes me by surprise, though I guess it really shouldn't surprise me all that much."
                    hero.say "Fine, I guess. You're in charge. But just know that it makes me sad."
                    show cassidy normal
                    $ cassidy.love += 2
                    $ cassidy.sub -= 2
                    cassidy.say "Fine, it makes you sad. Use a fucking rubber next time."
                    hero.say "Yes, Mistress."
                    call cassidy_preg_abort
            "It's for the best":
                hero.say "I guess it's for the best. Our arrangement would be a little weird, with kids."
                if cassidy.love > 120:
                    "Cassidy launches herself at me and wraps her arounds around my neck. There's a long, slow kiss."
                    $ cassidy.love += 5
                    cassidy.say "Maybe someday, [hero.name]. Okay?"
                    hero.say "Sure."
                else:
                    cassidy.say "Yeah, can you imagine what our kid would be like? Would probably be a troll."
                    hero.say "Hey, a sexy troll, at least."
                    if hero.fitness > 60:
                        cassidy.say "Okay, yes, two sexy parents, how could it not?"
                    else:
                        cassidy.say "Only if it takes after me. If it takes after you, it'd be the ugly troll."
                        hero.say "Harsh, Cassidy. Harsh!"
                call cassidy_preg_abort
    else:
        cassidy.say "Sweetie, I don't...I don't know if I'm ready for a baby."
        hero.say "But--"
        cassidy.say "Let me finish!"
        hero.say "Okay."
        cassidy.say "Look, I didn't ever see myself as a mom. It's just not something I ever wanted. But the thing is..."
        cassidy.say "I love you, [hero.name]. I think...I might. I might be willing to, you know."
        cassidy.say "Be a mom. With you. If you want?"
        if cassidy.get_status() == 'mistress':
            hero.say "You're giving me a choice?"
            cassidy.say "What we have is fun, but this...this would be forever. So yeah, I want your complete and unconditional buy-in."
        menu:
            "Yes":
                hero.say "Yes, my love. Yes. Yes!! Let's do this, let's have a baby. Let's be a family."
                show cassidy happy
                "Cassidy throws herself at me and envelops me in a hug. I can feel the wet from the tears streaming down her face as she presses against me."
                cassidy.say "You'll make a great dad, [hero.name]!"
                hero.say "I love you!"
            "No":
                hero.say "Cassidy, I don't think...I don't think this is a good idea."
                show cassidy cry
                cassidy.say "I know, it's not, but...no, you're right. I thought maybe if you wanted, but you're right."
                "I step up and wrap my arms around Cassidy while she babbles. Her words go incoherent as her face presses against my shoulder, and we hold each other tight."
                hero.say "Maybe another time, when we're both more mature?"
                "She nods into my chest, sobbing, but in agreement."
                call cassidy_preg_abort
    return

label cassidy_preg_abort:
    $ cassidy.set_flag('pregnant', 0)
    $ cassidy.set_counter('pregnant', None)
    $ cassidy.set_flag('toldpreg', False)
    return

label cassidy_preg_finish:
    $ cassidy.set_counter('pregnant', None)
    $ cassidy.set_flag('pregnant', 10)
    $ cassidy.set_flag('toldpreg', False)
    return

label cassidy_start_investigation:
    $ game.set_flag('suspended', True)
    $ game.set_flag('underinvestigation', True)
    $ cassidy.set_counter('start_investigation', None)
    $ cassidy.set_counter('finish_investigation')
    show aletta sad
    "Aletta comes into my office with a worried expression on her face. I know it's serious when she closes the door softly behind her."
    aletta.say "[hero.name], I've got some bad news for you."
    "I stand up from my chair. The look on her face and the tone of her voice has me especially worried now."
    hero.say "What's going on, Aletta?"
    if aletta.love > 100:
        $ game.set_flag("workinvestigation", 20)
        "Aletta hands me a folder."
        aletta.say "I'm not supposed to give you this, but, you're one of my best people..."
        "I open the folder and quickly flip through it. I'm quickly lost in a sea of numbers, row upon row of transactions."
        "But then things start to look familiar. These are accounts for my department's purchases and expenses."
        "Some of the numbers are circled, and at the bottom of the page I see the number $2,787,000 written in red ink."
        hero.say "What the hell is this?"
        aletta.say "[hero.name], there's some money missing from this department's accounts. A lot of money missing. And your accounts have been flagged."
        hero.say "Missing? Wait, that's what this...holy shit. Are you telling me they think I stole almost three million dollars?"
        aletta.say "They dont know, [hero.name]. But until they find out, I have to put you on an administrative leave."
        "I nearly shout, my voice filled with a combination of surprise, anger, and a feeling of betrayal. How could Aletta think I'd do this?"
        hero.say "What?!"
        aletta.say "Calm down, [hero.name]!"
        hero.say "You don't seriously think I did this, Aletta?!"
        aletta.say "No, [hero.name], I do not. But someone thinks you might have."
        "I sink back into my chair, deflated."
        hero.say "What are my options here?"
        aletta.say "If the investigation reveals that you stole the money, you could be fired. They would refer the matter to the district attorney."
        aletta.say "For numbers this big, you could go to jail, [hero.name]."
        hero.say "Jail? I didn't do anything? I certainly didn't steal three million dollars!"
        aletta.say "I know, and I'll tell them that, but I don't think that will be enough. You're going to have to figure out what happened."
        "I sigh."
        aletta.say "And you don't have much time. If I had to guess, I'd say they'll finish the investigation in a week. If you're cleared, you'll get your job back."
        hero.say "And if not, I go to jail."
        hero.say "Well, this sucks."
        aletta.say "I don't know how this happened. But I promise I'll find out."
        aletta.say "In the mean time, I'll cover for your work here as much as I can."
        hero.say "Thanks, I guess. I suppose if I get fired, I won't care much about that, will I?"
        "Aletta chuckles ruefully."
        aletta.say "No, I suppose not."
        "After Aletta leaves, I look through the folder she gave me. At least having the list of accounts and the numbers they're investigating will be a start."
    else:
        aletta.say "[hero.name], accounting has found some irregularities in your purchase and expense reports."
        hero.say "Irregularities? What does that mean?"
        aletta.say "It means the numbers don't add up, [hero.name]. A lot of numbers aren't adding up."
        hero.say "What kind of numbers?"
        aletta.say "Two point seven million numbers."
        "Whoa. That's a lot of numbers."
        hero.say "In my accounts? How is that even possible?"
        hero.say "Missing? Wait, that's what this...holy shit. Are you telling me they think I stole almost three million dollars?"
        aletta.say "They dont know, [hero.name]. But until they find out, I have to put you on an administrative leave."
        "I nearly shout, my voice filled with a combination of surprise, anger, and a feeling of betrayal. How could Aletta think I'd do this?"
        hero.say "What?!"
        aletta.say "Calm down, [hero.name]!"
        hero.say "You don't seriously think I did this, Aletta?!"
        aletta.say "I don't know, [hero.name], I really don't."
        hero.say "What are my options here?"
        aletta.say "If the investigation reveals that you stole the money, you could be fired. They would refer the matter to the district attorney."
        aletta.say "For numbers this big, you could go to jail, [hero.name]."
        hero.say "Jail? I didn't do anything? I certainly didn't steal three million dollars!"
        aletta.say "I'd like to believe you didn't, [hero.name], but I don't know. You're going to have to figure out what happened."
        "I sigh."
        aletta.say "And you don't have much time. If I had to guess, I'd say they'll finish the investigation in a week. If you're cleared, you'll get your job back."
        hero.say "And if not, I go to jail."
        hero.say "Well, this sucks."
        aletta.say "I don't know how this happened. But I promise I'll find out."
        aletta.say "In the mean time, I'll cover for your work here as much as I can."
        hero.say "Thanks, I guess. I suppose if I get fired, I won't care much about that, will I?"
        "Aletta chuckles ruefully."
        aletta.say "No, I suppose not."
        aletta.say "Well, good luck with it. I'm rooting for you."
        "After Aletta leaves, I take a long look at my desk. I have to figure out a way to head this off before I get fired."
    return

label cassidy_setup_meeting:
    if "cassidy" not in hero.smartphone_contacts:
        $ hero.smartphone_contacts.append("cassidy")
    play sound "sd/cell_vibrate.mp3"
    "My phone buzzes, and when I pull it out to look at it, the caller ID says that it's Cassidy."
    "The daughter of the CEO is calling me. In the middle of this investigation."
    "And when we met in my office, she told me I was going to regret spurning her."
    hero.say "Hello?"
    cassidy.say "Hey, [hero.name]. What's happening?"
    "Her voice is cheerful and mischievous. There is suddenly no doubt in my mind that she is related to this investigation."
    hero.say "Uh, nothing, much."
    cassidy.say "Oh good, that means you've got time to meet me."
    hero.say "I can't, I have...work to do."
    cassidy.say "Oh, Sweetie, we both know that's not true."
    "Her voice absolutely drips with delight. I play innocent."
    hero.say "What do you mean?"
    cassidy.say "Sweetie, you really have to stop pretending."
    "And then her voice drops, and turns...husky. It's somehow evil and sexy at the same time."
    cassidy.say "Do you want to keep your job?"
    hero.say "Uh, yes, yes I do."
    cassidy.say "Good. If you want to keep your job, then I might be able to help you. If, of course, you're willing to help me out."
    hero.say "Uh, what kind of help do you need?"
    cassidy.say "From what I hear about you, it's the kind of help you're very, very good at. Let's talk about this...in person."
    hero.say "Okay. Where at?"
    cassidy.say "Let's say...your office. At midnight. Tonight."
    hero.say "Midnight? Can you make this sound any sketchier?"
    cassidy.say "Oh, don't worry Sweetie. You won't have to anything illegal. Well, much. And you'll enjoy it, too. I know I will."
    hero.say "Does it involve Switzerland?"
    cassidy.say "It might! Well, we'll see when we get that far. Now, are you going to meet me or do you kiss your job good-bye?"
    "For emphasis, Cassidy makes an exaggerated kissing sound into the phone."
    "I really have to think about this. If she's got a hand in this investigation, the truth may not matter. I almost certainly will lose my job."
    "But if I do what she wants, I could end up in worse trouble. Is it worth it?"
    menu:
        "No":
            hero.say "No, I think I'll pass on your help."
            "She doesn't answer immediately, and when she does she sounds disappointed."
            cassidy.say "Are you sure? I promise I'll make it all worth your while, Sweetie. I saw you staring at my ass the other day. I know what you want."
            hero.say "Wait, are you offering--"
            cassidy.say "Meet me in your office at midnight tonight and find out. Otherwise, I hope you can find those millions of dollars."
        "Yes":
            hero.say "Fine, Cassidy. I'll meet you tonight."
            cassidy.say "Good. Oh I can't wait for this, it's going to be so much fun!"
            cassidy.say "Remember, Sweetie. Tonight. Midnight. Your office."
    cassidy.say "Come alone. And wear something...sexy."
    "And with that she hangs up."
    "This situation just gets worse and worse. But maybe there's an opportunity here. If she's up to something, maybe she'll give some some evidence I can use."
    "I just need to find a way to get that evidence, before the meeting."
    return

label cassidy_hold_meeting:
    "It's time for my meeting with Cassidy. Should I go?"
    if game.get_flag_value('cassidycameraplaced'):
        "I've already set up the spy camera, so I probably should go, but I can't help but be nervous."
    else:
        "I didn't come up with a way to record the meeting, so anything she says will probably just be my word against hers."
    menu:
        "Go to the meeting":
            pass
        "Skip the meeting":
            "I decide it's better to not go. I don't know what I missed, but at least I won't be under her thumb."
            return
    $ game.room="personal"
    call enter_room (room_present_girls=["cassidy"]) from _cassidy_hold_meeting
    show cassidy casual normal
    "When I open the door, she's already there, looking like the proud cat that caught the proverbial mouse. In this case, me."
    if game.get_flag_value('cassidycameraplaced'):
        "Knowing that this is being recorded, I try to keep my expression neutral. I throw in a touch of fear, but that's not hard. I really am afraid."
        $ game.set_flag('cassidyrecorded')
    cassidy.say "Oh, you came, Sweetie! I was worried you weren't going to take my offer seriously."
    "Once again, her voice turns sultry."
    cassidy.say "And it would be so unfortunate if you decided not to take me...seriously."
    "Was that an innuendo?"
    hero.say "Yes, Cassidy. I'm taking you seriously. What do you want?"
    cassidy.say "Before we get to that, don't you want to know what I can...do to you? Or for you?"
    hero.say "Uh, let's start with...what can you do for me?"
    "Cassidy rests her shapely ass against the edge of my desk and relaxes."
    show cassidy casual happy
    cassidy.say "Well, my dear. My daddy owns this company. And I can make this whooooole investigation go away."
    hero.say "Just like that?"
    "She snaps her fingers."
    "Just so."
    hero.say "Okay, ah. And what's the catch?"
    show cassidy casual normal
    cassidy.say "The catch, of course, is that we change your job description around just a leeetle bit. In addition to your normal work, you'll become my personal valet."
    "Sigh. She's still on that valet thing."
    "...and my personal sex toy."
    hero.say "Say what now?"
    cassidy.say "You know. My toy. My cabana boy. My personal massager. You'll make that big dick of yours available to me, when I want, how I want, where I want."
    hero.say "I don't think--"
    cassidy.say "No, thinking is definitely not part of your job, Sweetie."
    hero.say "No I mean that doesn't seem like--"
    show cassidy angry
    cassidy.say "Shut up. It's this or be fired and maybe go to jail."
    hero.say "Uh."
    if game.get_flag_value('cassidycameraplaced'):
        "Crap. This isn't going to be enough to nail her. I need to get her to talk more or this is not going to work."
        "Also did I just say nail her? Because despite being terrified, this is also kind of turning me on."
        call cassidy_meeting_loop
        return
    show cassidy normal
    cassidy.say "Now you've got two choices, Sweetie."
    cassidy.say "One, don't believe me, walk out of here, and prepare your ass for jail."
    cassidy.say "Or two, get down on your knees, kiss my feet, call my Mistress, and beg me to make this all go away for you."
    menu:
        "Refuse":
            "There is no way I'm going to get on my knees for this bitch, I don't care what happens."
            "So without another word, I turn and walk out."
            hide cassidy
            "As I walk out, I can just faintly hear her call out after me."
            cassidy.say "Enjoy jail, bitch! I hope you like getting fucked in the ass, because you're going to get a lot of it!"
            "Ugh. That's not a pleasant thought."
        "Accept":
            $ cassidy.set_flag("acceptedoffer", True)
            "I hesitate, but after a moment I nod and agree to her demands."
            call cassidy_first_dom
    return

label cassidy_meeting_loop(done_items=[]):
    menu:
        "Why should I believe you?" if "why" not in done_items:
            hero.say "Look, why should I believe you?"
            cassidy.say "I don't see that you have a choice. But for what it's worth, I'm a girl of my word, as long as you're a boy who will do as he is told."
            $ done_items.append("why")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items)
                return
        "What do you know about the investigation?" if "what" not in done_items:
            cassidy.say "I know that you're in a whole lot of trouble."
            hero.say "Oh come on, you know more than that."
            cassidy.say "I do."
            hero.say "Well, if you want this, tell me what you know. Because right now, I don't believe you can stop this, and I'll just get fucked for nothing."
            show cassidy casual angry
            cassidy.say "Fine. You want to know? I set this all up."
            hero.say "Why?"
            show cassidy happy
            cassidy.say "Because you need to be on your knees."
            hero.say "What the hell for?"
            show cassidy angry
            cassidy.say "Nobody says no to me. Nobody. Especially not someone like you."
            hero.say "Damn, you're one fucked up bitch."
            show cassidy normal
            cassidy.say "I'm going to put that one on your tab. You'll pay for it. Later."
            $ done_items.append("what")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items)
                return
        "Does your daddy know?" if "what" in done_items and "daddyknows" not in done_items:
            hero.say "Does your Daddy know what your hobbies are? Ski trips to Switzerland and coercing young men into doing sexual favors for you?"
            cassidy.say "Oh, well. Maybe not the sexual favors part. I don't think he wants to know about that."
            cassidy.say "But other than that, Daddy gives me whatever I want."
            show cassidy happy
            cassidy.say "And I want you!"
            show cassidy normal
            $ done_items.append("daddyknows")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items)
                return
        "You didn't just ask daddy" if "what" in done_items and "daddy" not in done_items:
            hero.say "You didn't just ask your daddy to do all this for you. Are you trying to tell me you set all this up yourself?"
            cassidy.say "Oh, well. I have had a bit little help. Here and there. A girl like does have to have a few minions, after all."
            "She leans toward me and uses the sultry, sexy voice again."
            cassidy.say "Like you!"
            $ done_items.append("daddy")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items)
                return
        "Who are you working with?" if "what" in done_items and "who" not in done_items:
            if "daddy" not in done_items:
                cassidy.say "What makes you think I'm working with anyone?"
                hero.say "Because I don't think you know enough about the business to pull this off yourself. Sure you're the CEO's daughter."
                hero.say "You have a lot of money and power, but I don't see you here every day, really in the system. No you have to have someone on the inside."
            cassidy.say "Why should I tell you?"
            hero.say "Because you'd rather get what you want than have me walk out of here and get fired, and it doesn't cost you anything."
            "As soon as the words are out of my mouth, I can't imagine there's any way she'll buy that. But..."
            cassidy.say "Fine, Jeff, the accountant doing the investigation. He's married, you know. And he doesn't want his wife to know about...us."
            hero.say "So, you're banging an accountant? Is that as boring as it sounds?"
            "She shrugs."
            cassidy.say "Well, he certainly isn't you, that's for sure. I mean to look at."
            cassidy.say "He's one hell of a lot smarter than you, though."
            "Oh, that bitch. She has no idea."
            hero.say "I see, so I'm just the dumb cute guy, huh?"
            cassidy.say "Pretty much!"
            $ game.set_flag('toldjeff')
            $ game.set_flag("workinvestigation", 10, mod="+")
            $ done_items.append("who")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items)
                return
        "Where is the money?" if "what" in done_items and "where" not in done_items:
            hero.say "So where's the money? I didn't steal it. Did you steal 3 million dollars and set me up just to put me in my place?"
            cassidy.say "No! I didn't steal anything!"
            hero.say "Where is it, then?"
            show cassidy angry
            cassidy.say "How should I know?"
            show cassidy normal
            hero.say "What? You set all this up, that money is missing. Are you telling me you set me up and you don't even know who really took the money?"
            hero.say "It seems like that's a great recipe to get fucked."
            cassidy.say "It doesn't matter, okay? That money was already gone, and they promised me it would be handled, and that I don't want to know about it."
            hero.say "They, huh? So you're not the mastermind here. You're just the patsy!"
            show cassidy angry
            cassidy.say "No, Sweetie. You're the patsy here. Unless you do exactly what I tell you."
            $ game.set_flag("workinvestigation", 10, mod="+")
            $ done_items.append("where")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items)
                return
    show cassidy angry
    cassidy.say "Enough of your questions! I'm the one in charge here!"
    show cassidy normal
    cassidy.say "Now you've got two choices, Sweetie."
    cassidy.say "One, don't believe me, walk out of here, and prepare your ass for jail."
    cassidy.say "Or two, get down on your knees, kiss my feet, call me Mistress, and beg me to make this all go away for you."
    "I should have enough in the recording to deal with her, but I don't really know for sure."
    "If I refuse, they might push the 'investigation' through. Maybe I have enough, maybe I don't."
    "If I accept, I don't know what she'll ask me to do. Can I handle begging a little?"
    menu:
        "Refuse":
            "There is no way I'm going to get on my knees for this bitch, I don't care what happens."
            "So without another word, I turn and walk out."
            hide cassidy
            "As I walk out, I can just faintly hear her call out after me."
            cassidy.say "Enjoy jail, bitch! I hope you like getting fucked in the ass, because you're going to get a lot of it!"
            "Ugh. That's not a pleasant thought."
        "Accept":
            $ cassidy.set_flag("acceptedoffer", True)
            "I hesitate, but after a moment I nod and agree to her demands."
            call cassidy_first_dom
    return

label cassidy_first_dom:
    cassidy.say "Good, good. Now, for a down payment on our little arrangement, I want you to strip out of your clothes."
    hero.say "What?"
    cassidy.say "None of that! No hesitating, no acting incredulous. Get out of your fucking clothes right now, bitch."
    "I grit my teeth but accede to her demand and start taking my clothes off."
    "First my shirt."
    "Then my pants."
    show cassidy happy
    "Finally my underwear."
    "Cassidy looks me up and down, approvingly."
    cassidy.say "Oh, I do like a man who's well hung. Now, get down on your knees."
    "I stand there for a moment."
    show cassidy angry
    cassidy.say "Now, bitch! And while you're down there, call me Mistress."
    "Fuck, this is actually starting to turn me on."
    "I get down on my knees, as asked. But I take my time about it."
    show cassidy normal
    cassidy.say "And? What else did I tell you to do?"
    hero.say "Call you Mistress."
    cassidy.say "Well?"
    hero.say "Yes, Mistress."
    cassidy.say "Good. Now I want you to jerk yourself off for me."
    hero.say "Wh--"
    cassidy.say "If you persist in that behavior, I'm going to have to really punish you. Do as you're told, bitch."
    "I sigh, and put my hand on my cock. It's only half erect, so it comes up fairly slowly."
    hero.say "It would help, if...it would help, Mistress, if you would maybe, give me a hand?"
    cassidy.say "Fuck that, I'm in charge here, you don't get to ask me for a handy."
    hero.say "I meant, maybe...give me something to look at? To help get its attention?"
    cassidy.say "I see. Well. Are you being a good boy?"
    hero.say "Yes, Mistress, I'm being a good boy!"
    show cassidy casual topless
    "Cassidy removes her top and casually casts it aside. Will this do?"
    "My cock immediately stiffens in my hand."
    hero.say "Yes, Mistress."
    cassidy.say "Sweetie, do better than that."
    hero.say "Yes, Mistress, thank you, Mistress. I love seeing your boobs, Mistress."
    "It's true. I do love seeing her boobs."
    show cassidy happy
    "And while I work my now fully erect cock, she watches with no small amount of lust. After a few moments if this, her hand goes under her skirt."
    "She starts to finger herself where I can't see."
    hero.say "Can I watch, Mistress?"
    cassidy.say "No. You have enough to go on."
    hero.say "Yes, Mistress. Thank you, Mistress."
    "After a few more strokes, pre-cum starts to leak out the tip, getting my fingers wet."
    "The extra wetness makes my cock slippery, which adds to the sensation. Almost unexpectedly, a big, thick burst of semen shoots out and hits the floor, near her feet."
    "Damn. I really wanted to get it up to her chest, but I wasn't fast enough."
    "Cassidy bends over, touches the glop of goo on the floor with her finger and touches it to her mouth."
    show cassidy casual topless wet
    "And where she pulled her hand out from under her skirt is quite wet."
    cassidy.say "Mmm. That's what I'm talking about."
    show cassidy normal
    cassidy.say "You may go."
    hero.say "That's it?"
    cassidy.say "Go. Now. Don't worry we'll talk again later."
    "I want to argue, but think better of it. Like it or not, she has my balls in her hands now. Literally and figuratively."
    $ cassidy.sub -= (cassidy_sub + 10)
    $ cassidy.love += 2
    return

label cassidy_investigation_complete:

    $ cassidy.set_flag('assistantdelay', True, 1)
    play sound "sd/cell_vibrate.mp3"
    "My phone buzzes. It's the office. A voice I don't recognize tells me to come into Aletta's office right away."
    "I'm on my way to Aletta's office when I spy Cassidy in my office. When she sees me, she beckons me to come in by curling one finger towad her."
    show bg personal with fade
    show cassidy casual happy
    cassidy.say "Good morning, Sweetie!"
    cassidy.say "I just wanted to give you one last chance, before you meet with Daddy. Are you going to play nice? Are you going to be my sweet, delicious boy?"
    if game.get_flag_value('workinvestigation') > 99:
        if game.get_flag_value('cassidyrecorded'):
            call cassidy_investigation_good_ending
        else:
            call cassidy_investigation_successful
    else:
        if game.get_flag_value('cassidyrecorded'):
            call cassidy_investigation_blackmail
        else:
            call cassidy_investigation_bad_ending
    return

label cassidy_investigation_good_ending:
    hero.say "Funny, I was actually going to say the same thing to you."
    show cassidy normal
    "Her expression drops."
    cassidy.say "Whatever do you mean, Sweetie?"
    hero.say "You see, it turns out I know three things, and I can prove them all."
    show cassidy angry
    hero.say "First, that your daddy is an embezzling criminal, and once I show the data to everyone, this won't be his company anymore."
    hero.say "Second, that your much-too-old-for-you sex toy named Jeff in accounting set all this up, and I can show where he personally moved the money that they claim I stole."
    show cassidy normal
    hero.say "Third, that you're a blackmailing bitch who's too stupid to look for cameras, and I have our midnight meeting on video. I think that one is going to play really well."
    hero.say "So, *Sweetie*, are you going to play nice? Or do I send your whole criminal family to jail."
    cassidy.say "You're lying."
    "I toss a file onto my desk."
    hero.say "The proof is right there."
    "Cassidy picks up the file and starts to flip through it. It's apparent she has no idea what she's looking at, until she gets to the pictures of herself in my office."
    cassidy.say "Fuck."
    hero.say "Yes. Fuck indeed."
    cassidy.say "Fine. What do you want?"
    hero.say "You're going to do whatever I want. You're going to break up with all of your boyfriends. Every single one of them."
    hero.say "You're going to get a job here at the office as my personal assistant. And then you're going to...assist me."
    cassidy.say "No! No way, fuck you and fuck that."
    "I shrug, then take the file from her hands."
    hero.say "If that's the way you want it."
    "I start walking toward the door, but I only get two steps before she stops me."
    cassidy.say "Wait! Please don't get Daddy fired."
    "I turn back around and look at her."
    hero.say "So we have a deal? I'll put this data away, and in exchange, you'll go in there, get your Daddy to end this investigation right here. Pin it on Jeff and give him an early retirement."
    hero.say "And you'll do whatever the fuck I want."
    "Cassidy purses her lips, but doesn't say anything."
    hero.say "Well?"
    cassidy.say "Nothing painful. No blood. I wouldn't have done anything to hurt you, I ask...I just ask the same."
    hero.say "Done."
    cassidy.say "So...I guess. I guess I'll go see Daddy now and..."
    hero.say "I wouldn't tell him too much about what you're doing. He doesn't need to know you're saving his ass. Just make it clear I keep my job, or he goes to jail."
    cassidy.say "Fine, yes."
    hero.say "You mean, 'Yes, Master'. You should get used to calling me Master right now."
    "Cassidy winces and looks like she's going to say something rude, but thinks better of it."
    cassidy.say "Yes...Master."
    $ cassidy_sub_max = 100
    $ cassidy_sub = 50
    $ cassidy_sub_min = 50
    $ cassidy.set_flag('status', 'pet')
    $ cassidy.set_flag('schedule', 'assistant')
    $ cassidy.set_flag('nokiss', False)
    "Cassidy walks out. After a few moments, I'm called in to Aletta's office."
    scene bg alettaoffice with dissolve
    show aletta work happy a at left
    show dwayne teaser at right
    dwayne_say "So, [hero.name], Aletta here tells me that you're her best employee."
    hero.say "Well, one of her best employees. She has quite a few good employees."
    aletta.say "Oh don't undersell yourself, [hero.name]. This company is much better off with you here."
    dwayne_say "Well, then. In any case, the investigation has come up inconclusive. While there is some evidence that you might have stolen the money, we think it could have been someone else."
    dwayne_say "So effective immediately, you are reinstated to your position. Accounting is going to keep a very, very close eye on your reports from here on out."
    dwayne_say "But since it seems you're most likely innocent, you have nothing to worry about as long as you keep your nose clean."
    hero.say "Thank you, Dwayne. I'm glad to hear that."
    "It's pretty clear to both Aletta and me that he's not happy about how this situation has turned out, and is doing his best to put on a good face."
    dwayne_say "Mm, yes. Well, I think I'm done here. Carry on."
    dwayne_say "And it goes without saying, [hero.name], neither of us will talk to anyone outside this room about this?"
    hero.say "Yes, sir."
    dwayne_say "Good, good."
    "As Dwayne leaves, looks troubled and...maybe a little bit scared."
    hide dwayne
    aletta.say "Well, [hero.name], I don't know how you pulled that off. And I don't want you to tell me, whatever happened it's best I don't know anything."
    aletta.say "But I'm happy to have you back, [hero.name]. Seriously!"
    $ aletta.love += 5
    $ game.set_flag('underinvestigation', False)
    $ game.set_flag('suspended', False)
    $ cassidy.set_counter('finish_investigation', None)
    $ game.room='personal'
    call enter_room
    return

label cassidy_investigation_successful:
    hero.say "Funny, I was actually going to say the same thing to you."
    show cassidy normal
    "Her expression drops."
    cassidy.say "Whatever do you mean, Sweetie?"
    hero.say "You see, it turns out I know two things, and I can prove them all."
    show cassidy angry
    hero.say "First, that your daddy is an embezzling criminal, and once I show the data to everyone, this won't be his company anymore."
    hero.say "Second, that your much-too-old-for-you sex toy named Jeff in accounting set all this up, and I can show where he personally moved the money that they claim I stole."
    show cassidy normal
    hero.say "So, *Sweetie*, are you going to play nice? Or do I send your whole criminal family to jail."
    cassidy.say "You're lying."
    "I toss a file onto my desk."
    hero.say "The proof is right there."
    show cassidy angry
    "Cassidy flips through it. Her eyes quickly glaze over at the rows and rows of numbers. She doesn't know anything about business."
    "She turns back to look at me."
    cassidy.say "Go ahead, do what you want. My Daddy is much smarter than you. You'll never make any...whatever this is stick."
    "She throws the file back down onto my desk, and walks out in a huff."
    hide cassidy
    "I wasn't expecting that. I mean, I know she doesn't have any idea what was actually in this file, but I had hoped to come to an arrangement without using it. Now...well I guess we'll see."
    scene bg alettaoffice with dissolve
    show aletta work angry a at left
    show dwayne teaser at right
    dwayne_say "[hero.name], the investigation has determined your complicity in theft from my company. You are terminated, effective immediately."
    hero.say "Aletta, before you act on that, I think you should look in this file."
    "I hand Aletta the file, who quickly thumbs through the sheaf of papers. After a brief moment, her eyebrows shoot up."
    aletta.say "Dwayne, according to this, you're the one who's been embezzling the money. This shows how a subsidary...Deewah holdings. Deewah? Really Dwayne?"
    dwayne_say "I have no idea what you're talking about, Aletta."
    aletta.say "It doesn't matter. When the board of directors sees this, and if this data holds up, you're going to be fired, Dwayne."
    dwayne_say "That's...that's not possible."
    aletta.say "You'd better go deal with this, Dwayne."
    hide dwayne
    show aletta happy
    aletta.say "Oh, and [hero.name], you can ignore what he said about you being fired. I'm taking charge of this investigation, as of now."
    aletta.say "If this turns out to be true, you're going to get a nice promotion."
    hero.say "Thanks, Aletta."
    aletta.say "Oh, no, thank {b}you{/b}. This, this is some of your best work. I hope you can keep this up."
    $ game.set_flag("promoted", 5, mod="+")
    $ game.set_flag('worksatisfaction', 0)
    $ aletta.love += 5
    $ game.set_flag('underinvestigation', False)
    $ game.set_flag('suspended', False)
    $ cassidy.set_counter('finish_investigation', None)
    $ HIDDEN.append('cassidy')
    $ game.set_flag('dwaynefired', True)
    return

label cassidy_investigation_blackmail:
    hero.say "Funny, I was actually going to say the same thing to you."
    show cassidy normal
    "Her expression drops."
    cassidy.say "Whatever do you mean, Sweetie?"
    hero.say "I have you on video, trying to extort me into playing your twisted little game. And on this video, you admit this whole thing is a setup."
    hero.say "I'm going to send this video to everyone in the company, and a few of your dad's friends. Maybe a Senator or two."
    "Cassidy blanches."
    hero.say "Of course, I might be willing to avoid all that...ugliness."
    cassidy.say "Really. And what do you want?"
    hero.say "To turn the tables. You do for me what you wanted me to do for you."
    cassidy.say "Huh. You want me to be your personal valet?"
    hero.say "Let's call it assistant. You can...assist me."
    cassidy.say "Hm. Yeah, let's see. You can release that and the fallout will blow over inside a year. I'll be fine, and a few people will know how ruthless I am and appreciate that."
    hero.say "Really? That easy?"
    "Cassidy shrugs, carefully keeping her expression neutral. I do my best to judge if she's bluffing or not."
    hero.say "I'm pretty sure this will put you in jail."
    cassidy.say "Nah, I didn't steal anything."
    hero.say "Fine, but your pet accountant will take the fall. Then you won't have him to entertain you anymore."
    cassidy.say "Fuck him."
    hero.say "I see. Well, I guess that's that, then, because I'm not getting fired for you."
    cassidy.say "Well, wait a second now. I'm sure there's...some other arrangement we could come to."
    "I take a moment to think about that. I can think of all kinds of things I wouldn't mind doing to this gorgeous woman, but I'm not sure how willing I am to negotiate."
    cassidy.say "Give me the video and I'll get the investigation called off. You'll get your job back."
    hero.say "After all this, that's it? Status quo? This week has been hell. Thank you, but no, I'd rather see you pay for this."
    "Cassidy looks at me for a second, thoughtful."
    cassidy.say "Okay, fine. You deserve a little payback. What do you want. Me on my knees?"
    "I lick my lips, and try not to tip my hand, but I can't hide how much that thought appeals to me."
    "She takes a step toward me, swaying her hips exaggeratedly as she does so."
    cassidy.say "I can do that. I'll give you the best damn blowjob you've ever had. I'll tell Daddy to call off the investigation. And you'll hand over the video."
    hero.say "I think I'll be holding onto the video. I have no way of knowing if you'll find some other way to screw me once that's gone."
    cassidy.say "And how do I know you won't keep extorting me for more?"
    hero.say "I guess we're at an impasse, then."
    show cassidy angry
    cassidy.say "Come on, Sweetie. Be reasonable."
    hero.say "Fuck reasonable. You did this. I don't see any reason to be reasonable."
    "Cassidy stares at me intently for a few moments. I swear if she had superpowers, my head would burst into flames."
    show cassidy normal
    cassidy.say "Fine, you can keep your video. But if you release that even after I've given you what you asked for, I will spend the rest of my life destroying you."
    cassidy.say "And I have the money and power to do a lot worse to you than just cost you your job."
    hero.say "Great, it sounds like we have a deal then."
    cassidy.say "I'll go get your meeting fixed up. You wait here."
    "Cassidy walks out. After a few moments, I'm called in to Aletta's office."
    scene bg alettaoffice with dissolve
    show aletta work happy a at left
    show dwayne teaser at right
    dwayne_say "So, [hero.name], Aletta here tells me that you're one of her best employees."
    hero.say "That's very kind of her."
    aletta.say "Don't sell yourself short, [hero.name]. You absolutely are."
    dwayne_say "Anyhow, [hero.name], I've got news for you. It seems that the investigation is inconclusive. There isn't enough evidence to take action."
    dwayne_say "Effective immediately, you're reinstated to your position. We will continue to investigate as needed, but as of now we are looking in other areas."
    dwayne_say "But be warned: if any other irregularities occur in your accounts, we'll be keeping a very, very close eye on you."
    hero.say "Ah, of course. Thank you."
    hide dwayne
    aletta.say "Well, [hero.name], I don't know how you pulled that off. And I don't want you to tell me, whatever happened it's best I don't know anything."
    aletta.say "But I'm happy to have you back, [hero.name]. Seriously!"
    $ aletta.love += 5
    $ game.set_flag('underinvestigation', False)
    $ game.set_flag('suspended', False)
    $ cassidy.set_counter('finish_investigation', None)
    "I thank Aletta, but I admit I'm in a bit of a hurry to get back to my office, and see if Cassidy is really going to pay up."
    scene bg personal
    show cassidy casual
    cassidy.say "Well, hello again, Sweetie."
    hero.say "Hello yourself, sexy. I believe we had a deal. Get down on your knees."
    cassidy.say "Of course. Why don't you sit down in your chair here?"
    call cassidy_tittyfuck from _cassidy_investigation_blackmail
    cassidy.say "And now, Sweetie, I think we're even. Good luck with the job."
    "And without another word, and without even cleaning herself up, she marches out of my office."
    "As awesome as that was, I find myself wondering if I could have done better. Having those lips and those tits on my dick every day would be...amazing."
    $ HIDDEN.append('cassidy')
    return

label cassidy_investigation_bad_ending:
    "I don't have any evidence to save me. If I tell her no, I'll certainly get fired. If I tell her yes, I don't know that she won't play with me and get me fired anyway. But what am I going to do?"
    menu:
        "I can always get another job":
            hero.say "No, Cassidy, you can go fuck yourself. I don't need this job badly enough to be your bitch."
            cassidy.say "Are you sure? How about if I promise it won't be painful. No blood, no pain, just you getting on your knees."
            "She leans forward and her voice turns husky."
            cassidy.say "I promise I'll take good care of you, Sweetie, as long as you take good care of my needs."
            cassidy.say "So. Last chance!"
            menu:
                "No, not worth it":
                    hero.say "No, you're not worth it."
                    call cassidy_mike_fired
                "Fine, you win":
                    call cassidy_dom_path
        "How bad can being her bitch be?":
            call cassidy_dom_path
    return

label cassidy_mike_fired:
    scene bg alettaoffice with dissolve
    show aletta work angry a at left
    show dwayne teaser at right
    "Aletta and Dwayne both look grim."
    dwayne_say "Hello, [hero.name]. Thanks for coming in."
    hero.say "Sure."
    dwayne_say "The investigation has shown conclusively that you're responsible for the money disappearing. The good news for you is that we've determined that this is due to negligence, and not embezzling."
    hero.say "How is that good news?"
    dwayne_say "It means we won't be suing you to recover the money."
    hero.say "Ahh. And my job?"
    dwayne_say "You're terminated, effective immediately."
    hero.say "Oh."
    dwayne_say "Aletta, please escort Mr. [hero.family_name] from the premises."
    aletta.say "I'm sorry, [hero.name]. I really am."
    "I nod. Aletta walks me to the exit, but there doesn't appear to be much for either of us to say."
    $ game.room='map'
    scene bg map
    show aletta a work sad
    aletta.say "Keep in touch, [hero.name], okay? I hope we can still be friends."
    hero.say "Yeah, sure. I guess."
    "I'm not really trying to brush her off, but this is pretty depressing."
    "She gives me a brief hug, then disappears back into the office building."
    $ HIDDEN.append('office')
    $ HIDDEN.append('cassidy')
    $ game.set_flag('fired', True)
    $ aletta.love -= 10
    $ lavish.love -= 10
    $ shiori.love -= 10
    $ game.set_flag('underinvestigation', False)
    $ game.set_flag('suspended', False)
    $ cassidy.set_counter('finish_investigation', None)
    "Now what am I going to do? Maybe I can get a job in the mall to keep the rent paid, or something."
    return

label cassidy_dom_path:
    $ cassidy_sub_max = 0
    $ cassidy_sub_min = -100
    $ cassidy.set_flag('status', 'mistress')
    $ cassidy_sub = 0
    $ cassidy.sub -= 10
    $ cassidy.set_flag('schedule', 'assistant')

    $ cassidy.set_counter('boredom')
    "I take a deep breath. This sucks, but I have to do it."
    hero.say "Yes, Cassidy. I'll be your valet."
    show cassidy happy
    cassidy.say "Oh good! We're going to have so much fun! I promise, this will be fun for you. I mean, you get to fuck the CEO's daughter, right?"
    "She's not wrong. That part might be fun, but honestly I'm used to being the one in charge for that."
    hero.say "Sure. It'll be fun, I guess."
    show cassidy angry
    cassidy.say "Wrong answer! Try something better, like 'Yes, Mistress, it will be fun!'"
    "Ugh."
    hero.say "Yes, Mistress, it will be fun."
    "Clearly I didn't sound terribly into it."
    cassidy.say "Try that again, with more enthusiasm, slave."
    "That one makes me scowl."
    hero.say "I'm not your slave. I'll be your valet but I'm not your slave."
    show cassidy normal
    cassidy.say "Would you rather be my bitch?"
    menu:
        "Bitch":
            hero.say "Yes, I'd rather be your bitch."
            $ cassidy.set_flag('heroname', 'Bitch')
        "Slave":
            hero.say "Fine, slave is better than bitch."
            $ cassidy.set_flag('heroname', 'Slave')
    cassidy.say "Now that we've got that cleared up, try that with more enthusiasm, {b}[cassidy.heroname]{/b}"
    "I work up all the enthusiasm I can."
    hero.say "It will be fun, Mistress!"
    cassidy.say "Great. Wait here, I'll go get this fixed."
    hide cassidy
    "After a few moments, I'm called into Aletta's office."
    scene bg alettaoffice with dissolve
    show aletta work happy a at left
    show dwayne teaser at right
    dwayne_say "So, [hero.name], Aletta here tells me that you're one of her best employees."
    hero.say "That's very kind of her."
    aletta.say "Don't sell yourself short, [hero.name]. You absolutely are."
    dwayne_say "Anyhow, [hero.name], I've got news for you. It seems that the investigation is inconclusive. There isn't enough evidence to take action."
    dwayne_say "Effective immediately, you're reinstated to your position. We will continue to investigate as needed, but as of now we are looking in other areas."
    dwayne_say "But be warned: if any other irregularities occur in your accounts, we'll be keeping a very, very close eye on you."
    hero.say "Ah, of course. Thank you."
    hide dwayne
    aletta.say "Well, [hero.name], I don't know how you pulled that off. And I don't want you to tell me, whatever happened it's best I don't know anything."
    aletta.say "But I'm happy to have you back, [hero.name]. Seriously!"
    $ aletta.love += 5
    $ game.set_flag('underinvestigation', False)
    $ game.set_flag('suspended', False)
    $ cassidy.set_counter('finish_investigation', None)
    $ cassidy.set_flag('nokiss', False)
    $ hero.smartphone_contacts.append('cassidy')
    "I thank Aletta, and head back to my office."
    $ game.room='personal'
    scene bg personal
    show cassidy casual normal
    cassidy.say "Well, hello again, Sweetie."
    hero.say "Hello, Cas--Mistress."
    cassidy.say "Oh very good, you caught yourself! I hope that means you'll be a quick learner."
    "I shrug."
    cassidy.say "So, how good are you with your tongue?"
    hero.say "What do you mean?"
    cassidy.say "You look like a dude who's licked a few pussies in your life. Are you any good at it?"
    menu:
        "I'm great at it":
            hero.say "Oh yeah, I'm great at it. I love eating a girl out! They always squirm with delight!"
            $ cassidy.love -= 2
            cassidy.say "Oh yeah? Let's see if you can live up to your big words."
        "I need more practice":
            hero.say "If I'm being strictly honest, I probably could use more practice."
            $ cassidy.love += 2
            cassidy.say "Well then, let's do it."
    call cassidy_dom_oral
    return

label cassidy_dom_oral:
    cassidy.say "Get over here and get down on your knees, [cassidy.heroname]!"
    menu:
        "Obey":
            "I do as I'm told without a word, walking right up to her and dropping to my knees."
            $ cassidy.sub -= 3
            $ cassidy.love += 1
            "I look up at her, expectantly."
        "Resist, playfully":
            "I smile, just slightly, but don't move."
            cassidy.say "Now, [cassidy.heroname], or do I have to punish you?"
            hero.say "Oooh, punishment? What're you going to do to me if I don't play nice?"
            cassidy.say "Are you looking for a spanking, Sweetie?"
            hero.say "Oh, you going to spank me?"
            cassidy.say "Would you rather get fired?"
            "I grin, and I figure I've pushed that one as far as I dare to. So I walk up to her--slowly--and put my hands on her hips."
            $ cassidy.sub -= 1
            $ cassidy.love += 3
            "Then I sink down to my knees and look up at her."
        "Resist, impudently":
            "I stand where I am. Maybe if I make this hard for her, she won't have any fun and will give up."
            cassidy.say "Now, [cassidy.heroname], or do I have to punish you?"
            hero.say "Really? You're going to punish me?"
            cassidy.say "Do you want to keep your job?"
            hero.say "Yes."
            show cassidy angry
            cassidy.say "Then get down on your fucking knees and do what you're fucking told."
            "I narrow my eyes and calculate just how far it's safe to push her. I decide this is far enough...for now."
            "So I walk up to her and sink to my knees, glaring at her the entire time."
            $ cassidy.love -= 5
            $ cassidy.sub += 1
    "Cassidy sits on my desk and hikes her skirt up around her hips, giving me a very close up view of her pussy."
    show cassidy lick
    "She puts her hands on the back of my head and pulls me roughly toward her. I have to put my hands on her thighs just to keep from losing my balance, but it also has the effect of pushing her legs further apart."
    "I have to close my eyes as she pushes me right in; my nose gets covered with her juices, and her pubes feel kind of funny across my cheeks and forehead."
    "Her thick, musty scent fills my nose. It's almost overpowering at first, but that sensation subsides in just a moment."
    "Since she seems to want to be in control, I let her. She moves my face up and down against her, and her soft pussy lips open up for me."
    cassidy.say "Use your tongue!"
    "I tighten my grip on her thighs and stick my tongue out. She's wet and ready, and I'm filled with her unique flavor."
    "I find her clitoris and focus the tip of my tongue there, pulling it between my lips and sucking on it, just for a second, before letting it go again."
    "She moans softly at that, her hands pushing me tighter into her. I repeat the motion, and her second moan is even louder."
    "While I go at her, I release my primary hand from her thigh and slide it underneath her, sliding in between her ass cheeks."
    "She yelps when I stink my finger into her anus, but doesn't stop me."
    "I continue to eat her out, while pushing my finger in first to one knuckle, then the other, careful to keep my fingernail from scraping her delicate flesh."
    "She lets out another gasp."
    cassidy.say "More. More, [cassidy.heroname]! {b}More!{/b}"
    "I can't really use my tongue any more, as she's pushing my head up and down with her hands, so it's all I can do just to keep everything in a good place, making sure I stimulate her clit when I can."
    cassidy.say "YES!!"
    "I push my finger all the way into her anus."
    show cassidy lick cum
    "And then she orgasms; if I thought she was wet before, this was almost like having a bucket of sticky goo thrown right in my face. It drips off me, staining my clothes and her thighs."
    "She lets go of me and I pull back so I can look up at her."
    hero.say "Wow."
    "Cassidy's chest heaves in mighty breaths while she looks down at me. Her face is an expression of pure delight."
    if cassidy.love < 120:
        cassidy.say "Fuck, [hero.name], you are just about the second best I've ever had."
        hero.say "{b}Second{/b} best?"
        "She winks at me."
        "Maybe you can work your way up to being all best."
    else:
        cassidy.say "Fuck, [hero.name], you are the best I've ever had. I'm going to keep you forever."
        cassidy.say "Oh God, maybe you can move in with me."
        hero.say "Maybe someday."
        "She smiles down at me, an expression filled with love and unexpected kindness."
    hide cassidy lick
    show cassidy normal wet bottomless
    "I stand up and work on cleaning her love juices off my face."
    cassidy.say "Oh that was so good. I can't wait to do that again!"
    return

label cassidy_new_assistant:
    $ hero.smartphone_contacts.append('cassidy')
    $ cassidy.set_flag('nodate', False)
    $ cassidy.set_flag("birthdayknown")
    $ cassidy_love_max = 80
    show aletta happy at left
    if cassidy.get_status() == 'pet':
        show cassidy casual normal at right
    else:
        show cassidy casual happy at right
    aletta.say "Hi [hero.name]! I got a call from Dwayne last night, and he's decided he wants his daughter to get some business training."
    aletta.say "So as of today, Cassidy is your new personal assistant. You're going to be showing her the ropes, and training her on everything there is to know about the company."
    if cassidy.get_status() == 'mistress':
        aletta.say "And if she does a good job, she will eventually be our new boss."
        aletta.say "She'll also be keeping a bit of an eye on you, to make sure nothing funny happens with your accounts again."
        "Cassidy gives me a big smile. She already knows who the boss is."
    else:
        aletta.say "And if she does a good job, there may be a permanent place for her at the company."
    hero.say "Wow, Aletta, that was quick!"
    "I turn to Cassidy."
    hero.say "I guess we'll have to see what you can do, right?"
    aletta.say "Right, I'll let you get to it."
    "As Aletta heads past me out the door, she puts her hand on my arm and leans close to whisper."
    aletta.say "Be careful, [hero.name]. She's got a reputation."
    hero.say "I know. It'll be okay, Aletta. And thanks, I appreciate the warning. It's good to know you care."
    $ aletta.love += 2
    hide aletta
    show cassidy at center
    if cassidy.get_status() == 'mistress':
        show cassidy normal
        cassidy.say "Oh yes, [cassidy.heroname]. You're definitely going to have your work cut out for you for the next few months."
        cassidy.say "I look forward to your training."
        menu:
            "I'm doing the training":
                hero.say "Aletta just said I'm the one doing the training."
                $ cassidy.love -= 1
                $ cassidy.sub += 1
                cassidy.say "I think I already know all I need to know about business. It's you that needs to learn. You don't know your place yet."
                cassidy.say "But you will. If you know what's good for you."
                show cassidy happy
                cassidy.say "I hold your life in my hands!"
            "Yes, Mistress":
                $ cassidy.sub -= 1
                $ cassidy.love += 1
                hero.say "Yes, Mistress. I look forward to the training too."
        cassidy.say "Now, lesson one. Who is your mistress?"
        hero.say "You are."
        cassidy.say "Excellent. Are you going to be an obedient boy?"
        hero.say "Yes."
        cassidy.say "Yes, what?"
        hero.say "Yes...Mistress."
        cassidy.say "Very good. Keep this up and I'll reward you."
        hero.say "What kind of reward?"
        show cassidy happy
        cassidy.say "We'll see! Trust me, you'll like it. But that's for another time."
    else:
        show cassidy sad
        cassidy.say "So. So now what?"
        hero.say "Are you okay? You look upset."
        "With visible effort, the slightly sad look she had disappears."
        show cassidy normal
        cassidy.say "Yeah, I'm fine. I just...I was going to go to Paris today."
        hero.say "Ah. Yes, I expect with this new job, your schedule is going to be very different."
        "She sighs."
        menu:
            "It'll be okay.":
                hero.say "Hey, it'll be okay. This job will be good for you. You've never had to work a day in your life, have you?"
                cassidy.say "What do you know about my work? Keeping up appearances to all of Daddy's social friends is a full time job!"
                hero.say "Ah, I guess it is."
                cassidy.say "I have no idea how I'll manage that."
                hero.say "You're doing exactly what your Daddy needs you to do, right now. So forget about all that for now."
                hero.say "Just stick around here, learn the job, and do what I ask. I promise I won't hurt you."
                $ cassidy.love += 1
                $ cassidy.sub += 1
                cassidy.say "Okay, I guess."
            "Suck it up, Buttercup":
                hero.say "Suck it up, Buttercup! You did this to yourself."
                $ cassidy.love -= 1
                $ cassidy.sub -= 1
                show cassidy angry
                cassidy.say "No, you're doing this to me!"
                hero.say "None of this would be happening if you didn't try to fuck with me. Otherwise we could be sitting in a bar, getting drinks, swapping stories."
                hero.say "You made your bed, now you're going to fuck me in it."
                show cassidy normal
                "Cassidy squirms at that."
                cassidy.say "Yeah, but do you have to be such an asshole about it?"
                hero.say "Learn to behave and maybe I'll be nicer."
                cassidy.say "Fine."
        hero.say "Now, how about a kiss?"
        "Almost reluctantly, Cassidy steps up to me. I put my hands on her hips and pull her close."
        "She tries to make the kiss short, but I hold her close, adding some heat to the kiss. After a few moments, she finally responds in kind."
        "And just about then, I decide that's enough for the moment."
        hero.say "Mm, that's excellent. We'll definitely be wanting more of that in the future."
        cassidy.say "Of course, Master."
    return

label cassidy_dom_boredom:
    $ cassidy.set_counter('boredom', None)
    show cassidy casual
    cassidy.say "You know, [hero.name], I may not have told you this, but I only ever intended our little arrangement here to be temporary."
    cassidy.say "I usually get bored with a guy after a couple of months."
    hero.say "You never mentioned that."
    if cassidy.love < 160:
        cassidy.say "And I'm going to be honest, you've been kind of fun but I think I'm pretty much done with you."
        hero.say "What are you saying, Mistress?"
        cassidy.say "You don't have to call me that any more. You're free. I'm quitting this \"job\"."
        menu:
            "No, don't go!":
                hero.say "But Mistress, wait! Please don't go! Have I not been good enough for you?"

                $ cassidy.love += 10
                if cassidy.love > 160 and cassidy.sub < -80:
                    cassidy.say "Well, you have been fun. And you have been a good boy."
                    cassidy.say "You really want me to keep you?"
                    hero.say "Oh yes, Mistress. This has been the best thing that's ever happened to me."
                    "Cassidy wraps her arms around me and pulls me in close for a kiss, which I am happy to oblige."
                    cassidy.say "Ok, [cassidy.heroname], you've earned yourself another few weeks."
                    hero.say "Thank you, Mistress! You won't regret it!"
                    return
                cassidy.say "That's sweet, [hero.name], but I'm just losing interest in you. It's me, not you. You know what, fuck that, I suck at the breakup speech. We're done, you need to move on."
                "She walks out the door, leaving me absolutely speechless. What did I do wrong? Would she have stayed if I had been done a better job? I guess I'll never know."
            "Free at last!":
                hero.say "Oh thank God, I'm free of you!"
                cassidy.say "Oh, well now, if you're going to be like that, maybe I'll stick around and keep you on your knees for a little bit longer."
                hero.say "Oh, uh. I mean, thank you for my freedom, Mistress?"
                show cassidy happy
                "Cassidy laughs."
                show cassidy normal
                "She steps up to me and wraps her arms around my neck, pulling me in for a kiss. It is deep and long, one of the most passionate she's ever given me, and in that moment, I'm actually just a little bit said."
                "Whatever was going on, she is always fantastic in bed."
                cassidy.say "I guess this is goodbye. Thanks for everything, [hero.name]. And good luck with the job."
                "And with that, she's gone from my life, just as swiftly as she entered it. A tornado, probably off to wreak havoc on some other dude's life. I don't know if I envy or pity him. Maybe both."
        $ HIDDEN.append('cassidy')
        hide cassidy
        $ cassidy.set_flag('schedule', None)
    else:
        cassidy.say "But you know what? Something's different with you. I've never been with anyone that I've actually come to care about."
        cassidy.say "So I've decided I'm going to keep you. That is...if you want me to."
        call cassidy_dom_boredom_keep
    return

label cassidy_dom_boredom_keep(bg=True):
    menu:
        "Yes!":
            hero.say "Yes, my Mistress, I want that. I want to be yours. I didn't at first, but my time with you...I cherish this."
            cassidy.say "Tell me you love me."
            "I answer without hesitation."
            hero.say "I love you, Mistress. With all my heart and my soul."
            "She practically throws herself at me, wrapping her arms around my neck and hugging me so tightly it's hard to breathe."
            cassidy.say "I love you too, [hero.name]!"
            cassidy.say "And you'll always, always be mine."
            "I reflect, while being held too tightly in her embrace, on the path that led to this. Did I just commit my entire life to her?"
            "I did, and I think that it's going to be okay."
            return
        "No thanks":
            hero.say "Cassidy, you're amazing, and this thing we had has actually been fun. But...I've got goals and dreams, and being your sex slave isn't compatible with that."
            show cassidy sad
            hero.say "Sooner or later I'd have found a new job. And then you wouldn't have anything to hold over me."
            hero.say "And I'd be gone then anyway. If you're...getting attached, maybe it's better we end this now."
            show cassidy cry
            cassidy.say "I'm...I'm sorry, [hero.name]. I thought...I was sure you felt the same way I did."
            hero.say "Only because I had to, hon. Look, if it helps, when this started I thought you were a total conniving bitch, and I've learned that you're just a girl who has everything and that's not enough."
            hero.say "Whatever it is you're looking for, it's not me. I'm sorry."
            "She sobs, then nods. She tries to speak, but the noises that come out aren't words."
            "This seems to upset her even more, and she runs out the door."
            "I guess this means I'm free, now?"
            $ HIDDEN.append('cassidy')
            hide cassidy
            $ cassidy.set_flag('schedule', None)
        "Boyfriend/girlfriend instead?" if bg:
            hero.say "How about we do this as boyfriend/girlfriend instead of this master/slave thing?"
            cassidy.say "I don't think I'm interested in just being one of your girlfriends. I want to keep you, but only if you want that."
            call cassidy_dom_boredom_keep (False)
    return

label cassidy_bad_day:
    show cassidy
    cassidy.say "[hero.name], what do you know about Aletta?"
    hero.say "Aletta, as in our boss?"
    cassidy.say "Yeah, her."
    hero.say "Why do you want to know?"
    "Cassidy shrugs and waves her hands. She's being evasive."
    cassidy.say "Just...it's not important, I guess. I want to know more about the company?"
    "That's probably the worst lie I've ever heard her tell, but it doesn't seem a big deal to humor her."
    menu:
        "She's my sex slave" if aletta.get_flag_value('collared') and aletta.sub > 50:
            hero.say "Well, she's kind of my sex slave."
            if cassidy.get_status() == 'mistress':
                cassidy.say "So wait, if you're my sex slave, and she's your sex slave, does that make her my sex slave?"
                hero.say "I...don't think she'll see it that way."
                cassidy.say "Huh. Maybe I should find out."
            cassidy.say "Are you the only one she's banging?"
            hero.say "I better be!"
            cassidy.say "But you don't know for sure?"
            hero.say "I guess I'm not with her every minute. Why?"
        "She's someone I care about very much" if aletta.love > 160:
            hero.say "Well, she's someone I care about very much. It's weird to say that about your boss, but..."
            cassidy.say "Are you sleeping with her?"
            hero.say "None of your business!"
            if cassidy.get_status() == 'mistress':
                cassidy.say "Oh yes, where your dick goes is very much my business, [hero.name]!"
                if aletta.get_flag_value('sex'):
                    hero.say "Fine, yes, I've fucked her. Happy?"
                else:
                    hero.say "No, I'm not sleeping with her."
            cassidy.say "Do you know if she's sleeping with anyone else?"
            hero.say "No, I don't think so. At least, I hope not!"
        "She's a total bitch":
            hero.say "She's an overbearing, mean-spirited bitch of a boss."
            cassidy.say "Huh. Do you know if she has a boyfriend?"
            hero.say "Why, are you looking for a girl?"
            cassidy.say "Haha, fuck off. Seriously, is she seeing anyone?"
            hero.say "Honestly, I have no idea."
        "She's a great boss":
            hero.say "She's a great boss. She's hard, sure, but she keeps the department running well, she doesn't let people slide by on nothing, and she rewards those who do good work."
            cassidy.say "Huh. Do you know if she has a boyfriend?"
            hero.say "Why, are you looking for a girl?"
            cassidy.say "Haha, fuck off. Seriously, is she seeing anyone?"
            hero.say "Honestly, I have no idea."
    cassidy.say "But you don't know for sure?"
    hero.say "I guess I'm not with her every minute. Why?"
    cassidy.say "It's just...it's something I overheard. It's probably nothing."
    hero.say "Tell me."
    cassidy.say "Let me find out if it's real first, okay?"
    $ cassidy.set_counter('dwaynefight')
    hide cassidy
    return

label cassidy_overhear_argument:
    "I'm on my way to the break room when I walk by Dwayne's office. Usually the door is closed and locked, because he's never actually here."
    "But today it's open, just a crack, and I can hear raised voices coming from inside the room."
    dwayne_say "I don't understand what's wrong, Cassidy."
    cassidy.say "What's wrong? You're cheating on her!"
    dwayne_say "I thought you'd be happy. You always hated Cherie."
    cassidy.say "Sure, Cherie's a giant bitch but you're supposed to be better than that."
    "The voices drop, and then I hear footsteps. I decide to hightail it away before either of them realize I've overheard that conversation."
    $ hero.activity.set_flag('canceled')
    $ cassidy.set_counter('dwaynefight', None)
    $ cassidy.set_counter('dwaynefallout')
    return

label cassidy_dwayne_fight_fallout:
    $ cassidy.set_counter('dwaynefallout', None)
    if cassidy.get_status() == 'pet':
        $ cassidy.set_counter('dwaynevisit')
    else:
        $ cassidy.set_counter('alettafight')
    show cassidy angry
    "Normally when we're not busy playing, Cassidy hangs around the office, mostly kind of bored, but actually doing something resembling the work she's supposed to be doing."
    "But right now she's sitting in her chair, just glaring at the paperwork in front of her. Not touching it, just glaring."
    hero.say "Hey, Cassidy, are you okay?"
    if cassidy.get_status() == 'pet':
        "Cassidy doesn't answer."
        hero.say "Hey! Earth to Cassidy, are you there?"
        cassidy.say "Oh. Yeah, I'm okay, I guess."
    else:
        cassidy.say "Fuck off, [hero.name]."
        hero.say "I just...I might have overheard something earlier and you seem upset. Do you need someone to talk to?"
        cassidy.say "No."
    $ cassidy_love_max = 120
    menu:
        "Leave her alone":
            "I decide in the mood she's in to just give her some space. Maybe she'll talk about it later, or maybe she won't."
        "Insist":
            hero.say "Hey, Cass..."
            cassidy.say "Don't call me that."
            hero.say "What, Cass?"
            cassidy.say "Yeah, that's what...that's what Daddy calls me."
            hero.say "Oh. I can't call you that?"
            cassidy.say "You haven't earned it."
            hero.say "I see. You're right. Cassidy, then. I don't mean to pry or be nosey, but you really seem like you need someone to talk to."
            "Cassidy sighs."
            cassidy.say "Fine, if it'll shut you up."
            "She turns and looks at me directly for the first time."
            cassidy.say "I just found out my dad is cheating on my step-mom. I went to confront it, and...I don't know what I expected. Maybe him to lie about it, or to be sorry about it, but he's not."
            cassidy.say "He told me he thought I'd be happy."
            hero.say "Why would you be happy?"
            cassidy.say "Because Cherie -- his wife -- is kind of a bitch. She tried to come in and replace my Mom and she was terrible at it. She spends half her time stoned, and the other half making sure her makeup is perfect."
            cassidy.say "And, well, she wasn't {b}my{/b} Mom, you know?"
            hero.say "Yeah. So what happened to your Mom, anyway?"
            cassidy.say "I don't know. She left. Packed up her stuff one day, told me she had to go away, and I never heard from her again."
            cassidy.say "Daddy said it wasn't my fault, but. She never called. She never answered when I called her. Didn't answer my letters."
            cassidy.say "Daddy said she was sick, and she had to. But I always wondered."
            cassidy.say "I think he was cheating on her with Cherie, and that's why she left. But I never understood why she left me too."
            show cassidy cry
            cassidy.say "How could any mother just leave her daughter like that? Even if she was sick!"
            hero.say "I don't know. I wish I knew. Is there any way to find out?"
            cassidy.say "Maybe. I guess I'd have to find her and make her talk to me."
            hero.say "You should do that."
            "Cassidy nods, slowly, then wipes the tears off her cheeks."
            show cassidy sad
            $ cassidy.love += 5
            cassidy.say "I guess. Yeah, maybe I'll do that. Thanks, [hero.name]."
            hero.say "Let me know what happens."
            cassidy.say "Sure."
    return

label cassidy_dwayne_visit:
    $ cassidy.set_counter('dwaynevisit', None)
    $ cassidy.set_counter('alettafight')
    "I'm working at my desk when I hear a knock at the door. Without waiting for me to reply, Dwayne opens the door and steps in."
    show dwayne teaser
    dwayne_say "[hero.name], I need to speak with you."
    hero.say "Uh, sure Dwayne."
    dwayne_say "Look, [hero.name], I agreed to put Cassidy in this position to train her up in how to do business. I thought that finally she'd come around and she's going to focus on important things."
    dwayne_say "Instead, you're using her as some kind of sex toy, I hear. All while she's yelling at me about my indiscretions."
    if cassidy.get_flag_value('collared'):
        dwayne_say "For God's sake, you've got her, my daughter, running around in a collar like she's some kind of pet!"
    dwayne_say "I think the way you're treating her is inhuman, and I won't stand for it."
    hero.say "I see. Well, Dwayne, you're missing a couple of really important facts here."
    hero.say "The first one, of course, is that I know exactly what was really going on in that cooked-up investigation you ran a few weeks ago."
    hero.say "And what you may or may not know is that your innocent daughter was trying to get {b}me{/b} to be {b}her{/b} sex toy by blackmailing me into doing favors for her or else you'd fire me."
    hero.say "But more important, I know--and can prove--that you're the one who stole that money, Dwayne."
    hero.say "So really, you should be thanking her."
    hero.say "Every time I cum into your daughter's mouth, that's one more day that you get to keep this company."
    hero.say "Every time she calls me Master, that's her way of saying how much she loves you."
    hero.say "Frankly, you don't deserve her, what she's doing for you."
    "Dwayne pales as I speak. If my proof weren't rock solid already, the look in his eyes absolutely confirms what I already knew: Dwayne is guilty as sin."
    hero.say "Well, boss, do you have anything to say for yourself?"
    dwayne_say "I should fire you."
    hero.say "Go ahead. Send me packing. I'll sue you for every penny you have. And I'll win. And you know it."
    "He scowls at me, then turns toward the door."
    hero.say "You'd better keep her happy, Dwayne. She's the only thing standing between you and oblivion."
    hero.say "I'd like to think that every time I fuck her, I'm really fucking you."
    if cassidy.sub > 75 and cassidy.love > 100:
        hero.say "But you know what? I think she's coming around to liking it."
    "Dwayne has nothing more to say, apparently. He slams the door on the way out."
    "I'd better watch myself. I have rock solid proof, but he's got gobs of money."
    return

label cassidy_aletta_fight:
    "When I enter my office, I'd normally expect Cassidy to be there. But she's not. Maybe she's just taking a break, I figure."
    "But then I hear muffled voices from Aletta's office, and one of them is Cassidy's. And they sound angry."
    "Given the conversation we had about Aletta a couple weeks ago, it might be prudent for me to intervene. So I steel myself up and go into Aletta's office."
    scene bg alettaoffice
    show cassidy angry at right
    show aletta angry at left
    cassidy.say "...be sleeping with a married man!"
    aletta.say "Why do you even care?"
    cassidy.say "Because he's my father!"
    aletta.say "He was barely there for you, Cassidy! In an average week, when you were in a teenager, how often did you see him? Twice? Once? Did you even see him at all during the week?"
    cassidy.say "Don't try to sidetrack me! This is about you stealing my father from my step-mother!"
    aletta.say "I'm not stealing him! She can keep that asshole for all I care."
    "The two girls finally notice me."
    aletta.say "Oh fuck, [hero.name]. I didn't hear you come in."
    hero.say "Do I need to call a timeout?"
    cassidy.say "You need to keep this bitch away from my Daddy, is what you need to do!"
    hero.say "Whoa, Ca--"
    aletta.say "You don't know what the fuck you're talking about, Cassidy!"
    cassidy.say "The fuck I don't! You're fucking my Dad, my Dad's going to divorce my step-mom and it's {b}all your fault{/b}!"
    show aletta sad
    aletta.say "Oh, Cassidy, you really don't know your father at all, do you?"
    aletta.say "I'm not fucking your father because I want to! I'm fucking your father because I don't have a choice."
    if cassidy.get_status() == 'pet':
        aletta.say "I don't have any more choice than you have with [hero.name]."
    else:
        aletta.say "I don't have any more choice than you give [hero.name] here."
    aletta.say "If I don't put out for him, that's it, I'm done here. And he can make sure I never work in the industry again."
    aletta.say "Do you have any idea what it's like?"
    show cassidy sad
    cassidy.say "Seriously? You're saying Daddy is using you as his personal sex toy?"
    hero.say "Wow. The apple doesn't fall far from the tree, does it, Cassidy?"
    "Cassidy shoots me a look. It's angry at first, but as she thinks about it, she realizes it's absolutely true."
    "She then looks back at Aletta."
    cassidy.say "Why should I believe you?"
    aletta.say "Fuck, do you think I'd make something like that up just to get you to stop yelling at me?"
    "Aletta turns and looks at me."
    aletta.say "[hero.name], does that sound like something I'd do?"
    hero.say "None of it sounds like you, Aletta. Bending over for a guy like that?"
    aletta.say "Dwayne knows how much I love my job. That's how this all started. I thought...well, at first it was kind of fun. But..."
    "She sighs."
    aletta.say "Cassidy, I'd dump your father tomorrow if I could. But know that there's no way the divorce is because of me. I'm not the sort he wants to marry. I'm not a young fashion model. I'm too smart to make good wife material for him."
    cassidy.say "Did you just call my mother dumb?!"
    aletta.say "No! No, that's not what I meant. But they're not..."
    "Aletta waves her hand at her office."
    aletta.say "...capable of this."
    "Cassidy glares at Aletta for a few long, seconds. She doesn't speak, and the tension starts to get really uncomfortable."
    "Then she turns and stomps out of Aletta's office."
    hide cassidy
    show aletta at center
    aletta.say "You'd better go talk to her, [hero.name]. She might do something...not very smart."
    hero.say "Yeah."
    scene bg personal
    show cassidy cry
    hero.say "Hey, Cassidy. You okay?"
    cassidy.say "Leave me alone, [hero.name]!"
    "I start to say something, but she glares daggers at me, and I decide I'm only liable to make it worse."
    cassidy.say "I'm taking a break for awhile. I'll be back in a couple of days."
    $ HIDDEN.append('cassidy')
    $ cassidy.set_counter('alettafight', None)
    $ cassidy.set_counter('needscomfort')
    return

label cassidy_needs_comfort:
    $ cassidy.set_counter('needscomfort', None)
    "The doorbell rings unexpectedly. When I answer it, I'm surprised to see Cassidy."
    scene bg house car with dissolve
    show cassidy sad
    cassidy.say "Hi, [hero.name]."
    hero.say "Cassidy! I was starting to think maybe you were gone for good. Are you okay?"
    cassidy.say "Yeah, I'm fine. No. I'm not fine. I don't...fuck."
    menu:
        "Comfort her":
            hero.say "You're not okay. Why don't you come in?"
            scene bg livingroom
            show cassidy sad
            "When Cassidy comes in, she wraps her arms around me and gives me a tight hug, burying her face into my shoulder. I put my arms on her back and caress her gently."
            hero.say "Hey, hon. Wow, this is really bad, isn't it."
            show cassidy cry
            "She nods into my shoulder, then sobs."
            hero.say "Okay. Listen, you just let it out, okay? I'm here for you right now."
            "When I say that, the dam bursts and she cries for real. I hold her for a good long time, doing my best to be comforting."
            "Eventually, the sobs start coming less often, and her breathing gets more under control."
            cassidy.say "I found my mom."
            hero.say "Oh. Was it bad?"
            cassidy.say "Yeah. It was terrible."
            hero.say "What happened?"
            cassidy.say "She...Daddy told me she just left, that she was sick and needed help."
            cassidy.say "It wasn't entirely a lie. She was sick, and she did go into rehab. And when she got out, she found out that Daddy was cheating on her."
            cassidy.say "And she got a lawyer, and was going to sue him. And then...I didn't really understand this part, but his lawyer did something, and she said she was going to go to jail."
            cassidy.say "And they worked something out so she left. He gave her a lot of money, and made her promise to never speak to me again."
            cassidy.say "And she {b}did it{/b}, that bitch! She took his money and left."
            "With those words, she starts to cry again."
            hero.say "Hey, it sounds like things were pretty bad for her."
            cassidy.say "I asked her if she thought about taking me with her. And you know what she said?"
            hero.say "What's that?"
            cassidy.say "She said she tried, and I didn't want to go! But that's not true! She never tried!"
            hero.say "Are you sure?"
            cassidy.say "What do you mean, am I sure? I'd remember something like that!"
            hero.say "How old were you?"
            cassidy.say "Eleven. Just eleven years old."
            hero.say "Memory is a funny thing. Maybe she tried but she couldn't tell you what was really going on. So she didn't ask you the right questions."
            cassidy.say "No! No way. She didn't...no."
            hero.say "None of that matters, now. Now you know what happened."
            cassidy.say "Yeah, my father is a guy who uses women and throws them away. Like dolls. Or like pets."
            hero.say "What are you going to do?"
            cassidy.say "I don't know."
            if cassidy.get_status() == 'pet':
                hero.say "I can destroy him, you know. You're the only thing stopping me from doing that. All you have to do is say the word."
                "She looks up at me with big, red-rimmed eyes."
                cassidy.say "I need to think about it."
                hero.say "Okay."
            else:
                hero.say "We need to do something about him."
                cassidy.say "I guess. What do we do, though?"
                hero.say "I don't know, yet. Let's think about it, and see what we can come up with."
                cassidy.say "Okay."
            hero.say "And I think maybe you should talk with Aletta. She's hurting too. Maybe that would help?"
            cassidy.say "That bitch!"
            hero.say "Is she, though? If she's a bitch, it's only because she's {b}his{/b} bitch. And you know what? That's killing her."
            cassidy.say "Fuck. You're right."
            "Cassidy turns her face up and gives me a long, passionate kiss. This one isn't our usual dom-sub thing, but it's almost like we're equals, maybe even loving partners."
            "Maybe it's just because she's so distraught right now, but this is seriously the closest to her I've ever felt."
            cassidy.say "I'm going to go check on some things. I'll see you at the office?"
            hero.say "So you're coming back?"
            cassidy.say "Yeah. I'm coming back."
            $ cassidy_love_max = 160
            $ if "cassidy" in HIDDEN: HIDDEN.remove('cassidy')
            $ cassidy.love += 5
            $ cassidy.set_counter('makenice')
            "For the first time tonight, she smiles, albeit weakly. And then she grabs my butt before running out through the front door."
            hide cassidy
            hero.say "Cheeky."
        "Get rid of her":
            hero.say "Cassidy, what are you doing? I don't think this is what our relationship really is."
            cassidy.say "I know, it's just...I don't have anyone else to talk to."
            hero.say "Maybe if you didn't try to turn every guy you like into your personal fucktoy you'd have more friends."
            if cassidy.get_status() == 'pet':
                cassidy.say "Yes, you've very effectively taught me that lesson already, {b}Master{/b}."
            else:
                cassidy.say "I guess you're right."
            hero.say "Look, I'm sorry you're fighting with your father, but given who he is and who I am, I feel I shouldn't be involved in that."
            cassidy.say "Fine."
    return

label cassidy_aletta_make_nice:
    $ cassidy.set_counter('makenice', None)
    show aletta angry at left
    show cassidy angry at right
    "I look up from my desk, and Aletta and Cassidy are both standing there together. They both look very angry."
    if aletta.get_flag_value('sex') > 2 and aletta.love > 120:
        aletta.say "[hero.name], I just figured out that either you're cheating on me with Cassidy, or you're cheating on Cassidy with me."
        hero.say "To be fair, I can't cheat on Cassidy, that's how our arrangement works."
        aletta.say "So you're cheating on me, then."
        if cassidy.get_status() == 'mistress':
            hero.say "Like you with Dwayne, I don't really have a choice."
        else:
            hero.say "And you're cheating on me with Dwayne."
            aletta.say "And I don't have a choice."
        aletta.say "Fine, there's difficult circumstances. And we've got more important things to talk about right now. But...we will talk about this later."
    aletta.say "Cassidy came to me early this morning, and we had a long talk."
    aletta.say "I need to get out from under Dwayne's thumb."
    if cassidy.get_status() == 'pet':
        aletta.say "And you have the means to make that happen."
    else:
        aletta.say "And so do you."
    hero.say "For my part, Cassidy is the one holding the cards there. That's why we're in this...arrangement."
    show aletta normal
    show cassidy normal
    cassidy.say "The more I find out about what he's done, the more I need to be free from him."
    if cassidy.get_status() == 'pet':
        hero.say "What if I don't want to let you go, Cassidy?"
        cassidy.say "Well, what's holding me to you is Dwayne, and I want Dwayne to suffer. I don't see how you could stop that."
        if cassidy.love > 120 and cassidy.sub > 75:
            cassidy.say "But this hasn't been all bad. Maybe when this is over, I'll listen to your pitch about why I should stay with you."
            if aletta.get_flag_value('sex') > 2 and aletta.love > 120:
                show aletta angry
                "Aletta glares at Cassidy, obviously jealous."
                show aletta normal
    else:
        hero.say "You're willing to let me go?"
        cassidy.say "When this is over, I won't have your job as leverage, it's true. But...well, we'll talk when it's over, okay?"
        if aletta.get_flag_value('sex') > 2 and aletta.love > 120:
            show aletta angry
            aletta.say "We might have to have words about that too."
            show aletta normal
    hero.say "Okay, Aletta. What's your plan?"
    aletta.say "It's pretty simple. I go to the board of directors with everything you and Cassidy both have."
    cassidy.say "I don't think that will be enough. Just getting him in trouble with the board might cost him his position here, but...I think we need him in jail."
    aletta.say "Really?"
    cassidy.say "Yeah. He's got politicians in his pocket, he's got expensive lawyers, and he'll get revenge. If you want this to work, you need enough to put him in jail."
    hero.say "We might have enough for that."
    cassidy.say "Maybe, but it's a big risk. But I think I know how to get what we need. He has a safe in his office, and he keeps a lot of dirty secrets in that safe."
    cassidy.say "I'm not sure what's really in there, but he's said he can blackmail a lot of people with it."
    hero.say "Huh. Okay. How do we get into a safe?"
    aletta.say "That's out of my wheelhouse. I don't know anything about brekaing into safes."
    cassidy.say "Cherie can get into it."
    hero.say "Your step-mom."
    cassidy.say "Yeah. But I don't think she'll do it for me. She doesn't trust me."
    cassidy.say "You'll have to talk her into it, [hero.name]."
    hero.say "I don't even know her!"
    cassidy.say "We can set something up. You can use your charms. You do have charms, right?"
    if hero.charm < 75:
        aletta.say "He might have to work on that."
        "I ignore Aletta."
    hero.say "Okay, so let me get all this right. I need to meet Cherie, charm her, and get her to get me into Dwayne's private safe, so I can look at his secrets and see if there's enough to bring him down?"
    cassidy.say "That's about it."
    hero.say "I'm not sure I should be doing this..."
    aletta.say "[hero.name], God help me, you're going to do this or I'll shoot you myself. Every day I have to touch that man's dick is going to be on you."
    hero.say "Your argument is compelling."
    cassidy.say "Great. I'll figure out how to set something up with Cherie. It might take a little while."
    hero.say "And until then?"
    aletta.say "Status quo, sadly. Until we can take him down completely, I'm still his bitch."
    if cassidy.get_status() == 'mistress':
        cassidy.say "And you're still mine."
    else:
        aletta.say "And she's still yours."
    hero.say "Okay then."
    $ hero.activity.set_flag('canceled')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
