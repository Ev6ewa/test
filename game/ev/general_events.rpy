init python:
    Event(**{
        "name": "samantha_event_01",
        "label": ["samantha_event_01"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["map"],"hours":(10,17),"days_played":7, "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "hanna_event_01",
        "label": ["hanna_event_01"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["gym"],"hours":(10,17),"days_played":7, "min_fitness":20, "activity":["train_hard", "train"], "flag_female":0},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "kylie_event_01",
        "label": ["kylie_event_01"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["university"],"hours":(10,17),"days_played":7, "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "alexis_event_01",
        "label": ["alexis_event_01"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"flagmin_promoted":6,"hours":(10,20),"flag_dateinprogress":0, "flag_female":0},
        "do_once":True,
        })

    Event(**{
        "name":"3bj_birthday",
        "label": ["bj_birthday"],
        "duration": 0,
        "priority":250,
        "girls_conditions": {"sasha":{"flagmin_sex":1,"flagmin_lesbian":5,"min_love":150},"bree":{"flagmin_sex":1,"flagmin_lesbian":5,"min_love":150}},
        "game_conditions": {"date":"birthday","hours":(14,18),"room":["livingroom"], "flag_female":0, "flagmin_homeharem":1},
        "do_once": True,
        "quit": True
        })











    Event(**{
        "name": "lexi_event_01",
        "label": ["lexi_event_01"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["map"],"hours":(22,4),"days_played":7, "min_money":250,"flag_dateinprogress":False, "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "harmony_event_01",
        "label": ["harmony_event_01"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["church"],"activity":"attend_mass","flagmin_morality":1, "flag_female":0},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "harmony_event_02",
        "label": ["harmony_event_02"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["church"],"activity":"attend_mass","flagmin_morality":1, "flag_female":0, "flag_harmonystart":1},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "palla_event_01",
        "label": ["palla_event_01"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["mall"], "days_played":10, "hours":(14,18), "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "office_party",
        "label": ["office_party"],
        "duration": 4,
        "priority": 500,
        "required_item": "fancy clothes",
        "game_conditions":{"room":["map"], "hours":(20,22),"flageq_officeparty":True, "days":"5", "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "office_party_set_up",
        "label": ["office_party_set_up"],
        "duration": 0,
        "priority": 500,
        "game_conditions":{"activity":["work","workhard","work_personal","workhard_personal"],"days":"123","flagmin_promoted":5, "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "office_party_missed",
        "label": ["office_party_missed"],
        "duration": 0,
        "priority": 500,
        "game_conditions":{"days":"6","flageq_officeparty":True, "flag_female":0}
        })


    Event(**{
        "name": "bree_sasha_showdown",
        "priority": 500,
        "label": ["bree_sasha_showdown"],
        "duration": 0,
        "game_conditions":{"flag_dateinprogress":False},
        "girls_conditions": {"bree":{"present":True,'valid':True,"flagmin_sex":3},"sasha":{"present":True,'valid':True,"flagmin_sex":3}},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name":"fix_init",
        "label": ["fix_init"],
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

label fix_init:
    python:
        if not game.get_flag_value("female"):
            if not "mike" in HIDDEN: HIDDEN.append("mike")
            if not "bedroom6" in HIDDEN: HIDDEN.append("bedroom6")
            if not "bedroom4" in HIDDEN: HIDDEN.append("bedroom4")
        else:
            if not "bree" in HIDDEN: HIDDEN.append("bree")
            if not "office" in HIDDEN: HIDDEN.append("office")
            if not "bedroom2" in HIDDEN: HIDDEN.append("bedroom2")
            if not "bedroom1" in HIDDEN: HIDDEN.append("bedroom1")
    return


label bree_sasha_showdown:
    scene bg livingroom
    "Yet another lazy day finds me, just another that I spend lounging around the living room, spread across the couch and staring at the television screen blankly."
    "The girls are off doing something or another, the last I saw them in fact, Bree was heading into Sasha's room as the two whispered about something."
    "I'm glad the two are getting along, they're very different but seem to like each other well enough at least."
    "It's only when my attention begins to drift idly back towards the television that I hear a door open and two sets of footprints approaching."
    show bree angry at left
    show sasha angry at right
    "Glad for the company, I turn to watch both Sasha and Bree enter the room, although I quickly realise something here is very, very wrong."
    "Sasha looks furious, something or someone has clearly upset her greatly, while Bree is a wreck, her eyes a crimson red, the telltale sign that she's just stopped crying."
    "I immediately snap to attention, standing up and quickly glancing between the two of them, wondering what they could have been talking about that devastated them so much."
    hero.say "What? What's wrong?"
    "Sasha's glare is terrifying, and before she even opens her mouth, I clue into exactly why the two of them seem to be confronting me."
    sasha.say "How the hell did you think you'd get away with this?"
    hero.say "What? Get away with what?"
    "I feign ignorance in the desperate hope that I'm wrong."
    bree.say "Please Don't lie No more lying"
    "She's audibly on the verge of tears once more, practically biting herself to bide them away."
    sasha.say "You're sleeping with BOTH of us?"
    sasha.say "We live together, genius! Or did you forget?"
    sasha.say "Of course we're going to figure it out."
    hero.say "Oh. That."
    sasha.say "Yes, 'THAT'! What the fuck were you thinking?"
    hero.say "I..."
    if "bree_preg_talk" in DONE and "sasha_preg_talk" in DONE:
        sasha.say "You even got us pregnant moron!"
        show bree sad
        "Bree's eyes are welling up with tears."
    elif "sasha_preg_talk" in DONE:
        sasha.say "You even got me pregnant moron!"
        show bree sad
        "Bree's eyes are welling up with tears."
    elif "bree_preg_talk" in DONE:
        sasha.say "You even got Bree pregnant moron!"
        show bree sad
        "Bree's eyes are welling up with tears."
    if sasha.get_flag_value("lesbian") >= 10 and bree.get_flag_value("lesbian") >= 10:
        hero.say "I'm sorry. I should have said something."
        hero.say "It's just I like you both."
        hero.say "I thought I'd be able to decide eventually, but the more time I spent with both of you, the harder it got to cut it off with one and"
        show bree sad
        bree.say "You should have just said something."
        bree.say "Are we the only ones?"
        menu:
            "Yes":
                hero.say "Yes! Of course you are."
                hero.say "I don't go around fucking everything I see."
                if game.get_flag("bandharem") >= 1:
                    sasha.say "What about the band?"
                    $ sasha.love -= 15
                    $ bree.love -= 15
                    if not game.get_flag("bandharem") >= 2:
                        sasha.say "come on..."
                    else:
                        sasha.say "Oh yeah, they had a lot to tell me about you."
                    hero.say "I, Right, and the band."
                    bree.say "You can't keep lying about this stuff,"
                    hero.say "I know, I'm just..."
                elif sasha.get_flag_value("cheated"):
                    $ g = sasha.get_flag_value("cheated")
                    sasha.say "What about [g]?"
                    $ sasha.love -= 15
                    $ bree.love -= 15
                    hero.say "I, Right, [g]."
                    bree.say "You can't keep lying about this stuff,"
                    hero.say "I know, I'm just..."
                elif bree.get_flag_value("cheated"):
                    $ g = bree.get_flag_value("cheated")
                    bree.say "What about [g]?"
                    $ sasha.love -= 15
                    $ bree.love -= 15
                    hero.say "I, Right, [g]."
                    show sasha wtf
                    sasha.say "Fucking manwhore..."
                    hero.say "I know, I'm just..."
                else:
                    sasha.say "You could have fooled me, jackass!"
                    sasha.say "How the hell are we supposed to trust anything you say?"
                    hero.say "I don't know. I really don't."
            "No":
                hero.say "You, No, you aren't the only ones."
                $ sasha.love -= 5
                $ bree.love -= 5
                sasha.say "Just how many people are you fucking?"
                hero.say "I-"
                sasha.say "Save it, I don't want to know actually."
                sasha.say "If you tell me, I feel like I'm going to throw up on you."
        hero.say "I fucked up, I know, but I'll do anything to make it up to the both of you."
        bree.say "It isn't easy to build up shattered trust"
        hero.say "I know, but I'm going to try."
        hero.say "I don't expect you to forgive me, I don't know if I can forgive myself, but just know that the last thing I wanted was to hurt either of you."
        sasha.say "And you did a *great* job with that, well done."
        sasha.say "Really, just look at how happy the both of us are."
        "She's still clearly furious, but unless it was simply my wishful thinking talking, some of the edge seems to have slipped out of her words."
        "An awkward silence falls on the room. I've said my piece, tried my best, but now it's up to the girls to decide my metaphorical fate."
        "The two stare at me for a while, Sasha's glare terrifying while Bree's almost pathetic puppy dog eyes almost outright painful."
        "Eventually, the silence is unbearable, and I'm forced to break it."
        hero.say "So What now?"
        sasha.say "I don't know."
        bree.say "Neither do I"
        sasha.say "I should kick your ass for what you did."
        bree.say "I should just Leave"
        hero.say "Yeah Both of those would be fair."
        sasha.say "But."
        sasha.say "I don't *want* to go anywhere."
        bree.say "You really hurt me, [hero.name]"
        bree.say "You betrayed my trust and It's going to take a long time to repair that."
        "I nod solemnly along to their words."
        bree.say "But I don't want to leave you either."
        hero.say "So"
        sasha.say "Sounds like you're in luck, [hero.name]."
        sasha.say "Neither of us are going anywhere. You'll have plenty of time to make it up to us."
        bree.say "So, are we going to Share him?"
        sasha.say "Why not? Apparently we've already been doing so, and we've been happy enough."
        bree.say "Well, like, sure, but it's a little Weird?"
        sasha.say "The only thing that's changed is we're being more honest with each other."
        bree.say "Yeah Yeah! You're right."
        "I feel like I don't have any say in the situation anymore, with Sasha easily convincing Bree to her side."
        "It isn't as though the outcome is a bad one for me though, so I just keep my mouth shut."
        sasha.say "Of course I'm right."
        sasha.say "So, [hero.name]. It looks like you're getting a second chance."
        bree.say "From like, both of us."
        sasha.say "If you dare cheat on either of us again, it's over for good. You're lucky you're so charming."
        hero.say "Heh, I guess I am."
        hero.say "Never again, I swear."
        bree.say "Good! But like, you've still got a long way to go before things will really be the same again"
        sasha.say "Damn right. I can't stress enough how much you need to make this up to us."
        hero.say "Anything I can do, I will."
        sasha.say "We'll think of something."
        sasha.say "In fact, we'll do that right now. Bree, come on."
        bree.say "Now? Well like, sure I guess!"
        bree.say "Um, I'm glad we're going to work this out, [hero.name]."
        bree.say "It might be hard, but I do really like you, just please Not again?"
        hero.say "Of course not."
        bree.say "I'll just have to try and trust you then! See you later!"
        "With a wave, Bree turns and rushes off down the corridor that Sasha escaped down, the two headed into one of their bedrooms and quickly filling the hallway with hushed voices."
        "Try as I might, I can't figure out what they're saying to one another, and eventually decide it's probably better that way."
        "My heart pounding, I'm frozen in place for a little while, wondering just how I'd managed to pull off not only cheating on two girls with one another, but having them find out and both agree to stay with me anyway."
        "Both relieved, and curious about what might be just around the corner in my relationship with the two, I get back to my day, trying to ignore the incessant whispering from behind their closed doors."
        $ game.set_flag("homeharem",1)
    elif sasha.love >= 175:
        hero.say "I don't know what I was thinking."
        hero.say "I don't have any excuse. I fucked up. I deserve anything you can throw at me."
        sasha.say "Damn right you do!"
        sasha.say "Are we the only ones?"
        hero.say "Yeah, of course you are."
        bree.say "Well we don't know, [hero.name]"
        bree.say "How are we supposed to believe you?"
        hero.say "I I don't know."
        bree.say "Was I really asking so much of you, [hero.name]?"
        bree.say "I just I just wanted to be with you."
        bree.say "If I wasn't enough, you should have just told me I could have just"
        "She's crying again, tears streaming freely down her face as her voice barely breaks through to barely form her words."
        hero.say "It isn't that you aren't enough Bree."
        bree.say "Then why? Why would you do this? *How* could you do this?"
        "I stammer over my words a few times before falling silent. I don't have an explanation for her, and I can't bring myself to lie to Bree's face. Not now."
        bree.say "I think I need to go"
        sasha.say "Yeah, go calm down Bree."
        bree.say "I don't mean calm down"
        hero.say "Wait, you can't-"
        bree.say "I'm going to move back home I'll um, be gone by tomorrow morning."
        sasha.say "You're moving?"
        "Sasha looked as shocked as I was. Bree couldn't make eye contact with either of us, instead preferring the spot on the carpet that her steady stream of tears stained."
        bree.say "Yeah I can't stay here anymore"
        sasha.say "Look, [hero.name] fucked up, I agree, but you don't have to move away."
        bree.say "Yes I do, Sasha!"
        "The outburst was sudden, almost violent."
        bree.say "You don't get it! This was supposed to be a fresh start, a new beginning."
        bree.say "[hero.name] ruined that."
        bree.say "I can't I can't just pretend like it never happened and move on, my brain doesn't work like yours does, Sasha!"
        bree.say "Not while I still live in this city"
        bree.say "I can't move on until I've moved."
        hero.say "Aren't you being a bit drastic? Just, sleep on it, alright?"
        bree.say "I'm not being drastic!"
        bree.say "I just"
        bree.say "I'll go call a cab."
        "I try again to stop her, plead for her to stay, but she ignores me and marches away to her room. I don't need to try the handle to know it's locked."
        "Not everything she said made sense to me, but it's clear that she's confused right now."
        "I am too. I can't tell if she's making a mistake, or the right decision."
        sasha.say "I didn't think she'd actually go."
        hero.say "Neither did I"
        hero.say "You aren't going too, right?"
        sasha.say "Maybe. I haven't decided yet."
        hero.say "...Please don't."
        sasha.say "Why shouldn't I, [hero.name]? What can you possibly do to convince me?"
        hero.say "I have no idea, but I'll try anything."
        hero.say "I can't lose both of you."
        "There's a short silence. I can tell that Sasha is thinking, hard, but her expression is so muddled, a cocktail of so many different emotions, I've no idea which way she's leaning."
        "Eventually, with a sigh, she throws herself onto the couch, and motions for me to sit next to her."
        sasha.say "You're pathetic."
        "Her words might have hit me hard, were it not for the overwhelming sense of relief washing over me as I readily sat besides her."
        sasha.say "If you ever, and I mean *ever*, pull anything like this again, you'll regret it."
        hero.say "Never again. I promise."
        sasha.say "You've got a long way to go before the word 'promise' means anything to me again."
        sasha.say "Just shut up for a while now. I'm still mad at you."
        "I open my mouth to confirm I'll be quiet, before realising how stupid that'd be, and just fall silent."
        "The two of us sit there for a while, the tension in the air eventually beginning to dissipate."
        "Sasha eventually leaves me to go help Bree pack her things, before returning to escort me out of the room while she helps Bree get to the cab."
        "I don't know where Bree got the money for a flight so soon, but it doesn't even give me chance to say goodbye."
        "The closest I get is staring after her as her cab disappears into the distance."
        "I doubt I'll ever see Bree again."
        "At the very least, there's still hope for Sasha and I, I just need to prove to her I can be loyal."
        "It won't be easy, but she's worth it."
        $ bree_love = 0
        $ bree_love_max = 0
        $ HIDDEN.append("bree")
        $ HIDDEN.append("bedroom2")
    elif bree.love >= 175:
        hero.say "I don't know."
        hero.say "I don't want to make excuses and lie, claim it's because of something it wasn't."
        hero.say "I just Can't explain why I did it."
        sasha.say "You're so full of shit."
        hero.say "I-"
        sasha.say "Save it. I'm done."
        hero.say "Sasha, wa-"
        sasha.say "I told you to save it, [hero.name]."
        sasha.say "What the hell do you expect? That we'll continue like nothing happened?"
        sasha.say "That in a few weeks the three of us will be looking back at this and having a good old chuckle at the whole thing?"
        sasha.say "You're a piece of shit. The sooner I get away from you, the better."
        hero.say "Get away?"
        sasha.say "I'll get my things tomorrow."
        bree.say "W-wait, are you moving out?"
        sasha.say "Yeah, I am."
        sasha.say "What, I'm supposed to live with *him*?"
        sasha.say "I can't stand the thought of standing next to him for any longer, let alone sleeping under the same roof as them."
        bree.say "But where are you going to go?"
        sasha.say "I'll crash on someone's couch for now. Shouldn't take too long to find a place of my own."
        hero.say "But-"
        sasha.say "Shut up, you. You should consider yourself lucky that I'm leaving it at moving out."
        sasha.say "I'll hail a cab. Later."
        "The goodbye is so abrupt I almost don't have time to object, try as I might."
        "Sasha is gone before I have a chance to stop her, having been unable to really get a word in for a little while now."
        "Slowly, I slump back down onto the couch, cursing myself for hurting her so much."
        "I almost don't notice Bree sitting besides me until I feel her hand on my back, slowly rubbing it in an attempt to console me."
        bree.say "Um, you really liked her, didn't you?"
        hero.say "...Yeah, I think I did."
        "I don't see any point in lying at this point, even taking into account who I'm talking to."
        "A silence follows, one that I can tell that Bree is using to consider what her reaction should be."
        "I can't bring myself to break it, letting the hand on my back calm me down surprisingly effectively, before Bree practically whispers to me."
        bree.say "I was going to leave too"
        hero.say "You were?"
        bree.say "Yeah I um"
        bree.say "You remember when I told you that trust was important to me, right?"
        hero.say "Of course I remember."
        bree.say "I was so upset when I figured it out, it was like my worst fears had come true, but"
        bree.say "I think I'll stay"
        "She hardly seemed convinced in her own words, but they were enough to send relief coursing through my veins."
        hero.say "Really?"
        bree.say "Um, yeah But like, you can't do this ever again."
        bree.say "Please Please don't do this again"
        bree.say "I want to trust you, that you'll be better, but that's really hard right now"
        bree.say "I don't think I could handle it if you ever cheated on me again"
        hero.say "Bree, I promise, I'll never do it again."
        hero.say "Consider the lesson learned, I swear."
        hero.say "If there's anything I can do to try and get things back to normal, I will."
        bree.say "I don't know if things can ever really go back to normal anymore, [hero.name]"
        bree.say "But um, we can try at least"
        "I nod, thankful that Bree's at least trying to be so understanding. My arms wrap around her on their own, holding her close."
        "Apparently, that was enough to open the floodgates, as the tears that she'd been holding back for so long begin pouring into my shoulder."
        "We stay like that for a while, before eventually Bree calms down."
        "After a little longer of sitting in silence, she announces that the evening has worn her out, and she's going to head to bed, leaving me alone to think about the two girls."
        $ sasha_love = 0
        $ sasha_love_max = 0
        $ HIDDEN.append("sasha")
        $ HIDDEN.append("bedroom3")
    else:
        "I fall silent."
        "I don't know what I can say to make this better. I can't tell if trying and failing might even be worse, so I just hang my head in shame."
        sasha.say "You're pathetic."
        bree.say "Aren't you even going to try and explain yourself?"
        hero.say "What can I say to make this better?"
        sasha.say "It's too late for words, jackass."
        hero.say "Then what do you want from me?"
        hero.say "I'm sorry, I really am."
        sasha.say "I don't believe a word of that. You're only sorry because we caught you."
        bree.say "How could you do this, [hero.name]?"
        hero.say "I don't know, alright?"
        hero.say "I don't know why I cheated on you both."
        sasha.say "Well that just makes everything better then, doesn't it?"
        hero.say "Of course it doesn't."
        sasha.say "Then try. Put in some sort of effort to prove that you're actually sorry."
        hero.say "I just"
        hero.say "I don't know what to tell you."
        "Bree is crying again, her tears streaming to the floor as I struggle to talk my way out of the situation."
        sasha.say "Well I know what to tell you."
        sasha.say "We're moving out."
        hero.say "Wait, you're what?"
        bree.say "We're moving out, [hero.name]"
        sasha.say "We just finished the details. We leave tonight."
        hero.say "Where are you going?"
        sasha.say "I'm crashing on a friend's couch and Bree's taking their guest room."
        bree.say "I'll um Probably go home tomorrow"
        hero.say "Home? You mean out of the city?"
        sasha.say "We can't live with you anymore, [hero.name]."
        sasha.say "I can barely stand just talking to you right now."
        bree.say "You betrayed my trust, even after I told you how important it was to me"
        bree.say "I can't stay here any more. You've Tainted this place"
        hero.say "You don't have to move out though!"
        sasha.say "Yeah, we do. Just be glad we gave you warning."
        sasha.say "We were just going to leave a note."
        hero.say "I Thanks?"
        "The sound of a car pulling up outside, then beeping it's horn, interrupts the conversation."
        bree.say "I think that's for us"
        sasha.say "He's a little early, but alright."
        sasha.say "Let's go get our bags Bree. Leave [hero.name] here."
        bree.say "Yeah Um, let's go"
        "I wasn't expecting it to be so sudden, and for a moment I'm shocked."
        hero.say "Wait!"
        bree.say "Why?"
        bree.say "What's the point, [hero.name]?"
        bree.say "You're just going to lie to me again"
        hero.say "Bree, no, I-"
        bree.say "[hero.name], please Just stop"
        bree.say "I'm sick of the lying If you aren't sorry, just say so."
        bree.say "I know you never liked me, that you just wanted sex"
        hero.say "Bree, that isn't true."
        bree.say "...That's what it feels like"
        sasha.say "Bree! He isn't going to wait forever!"
        bree.say "I um I should go."
        hero.say "You don't even have your things. Just stay, one night, let's talk about this, Bree."
        "My words give her pause, and for a brief second I'm hopeful as she turns away from the door to her room, but instead of walking towards me, she walks straight past me towards the door."
        bree.say "I'll um Send someone for my things tomorrow"
        "And with that, I was left alone."
        "The door slammed shut behind Sasha, and seconds later the vehicle outside drove away, vanished past a corner before I could get to the door to even see it leave."
        "I got the nasty feeling that I would never see either of them again."
        $ bree_love = 0
        $ bree_love_max = 0
        $ HIDDEN.append("bree")
        $ HIDDEN.append("bedroom2")
        $ sasha_love = 0
        $ sasha_love_max = 0
        $ HIDDEN.append("sasha")
        $ HIDDEN.append("bedroom3")
    return

label office_party_missed:
    $ game.set_flag("officeparty",False)
    if "office_party_set_up" in DONE:
        $ DONE.remove("office_party_set_up")
    return

label office_party_set_up:
    $ game.set_flag("officeparty",True)
    show aletta teaser
    aletta_say "[hero.name], there is an office party this Friday, I expect you to be there."
    hero.say "Count me in Aletta."
    aletta_say "Dress accordingly or you will not be able to get in..."
    hide aletta
    return

label office_party:
    $ game.set_flag("officeparty",False)
    scene bg street
    "I'd be lying if I said I want to attend."
    "Hanging out with coworkers outside of work feels too much like... work."
    "It takes a lot to get myself ready and out the door, but I manage with the knowledge that Bree will nag me all night for being antisocial if I don’t."
    "Besides, I figure the worst case scenario is I get a few free drinks, wedge myself into a corner somewhere, and observe everyone else making idiots out of themselves for an hour or two before heading home."
    "My feet scuff the cold pavement as I drag them toward the restaurant, looming posh and intimidating before me."
    "Le Magnifique is scrawled over the doorway in illuminated, pretentious calligraphy."
    "Ugh."
    "At least it wasn't held in the office, anyway. I’m not sure I’d be able to force myself there after hours to pretend to socialize, whether Bree nagged me or not."
    "Drawing a deep breath, I raise my hand and press it to the the ornate door handle."
    "The cold metal bites against my palm. After one final, torturous moment of hesitation, I pull the door open and allow myself inside."
    scene bg highclassrestaurant
    "The pessimism clouding my head dissipates like a fine mist almost immediately under the warm atmosphere and uptempo music that greets me."
    "Familiar faces pepper the dim red mood lighting, laughing and sipping casually at their drinks."
    "They look completely different when they aren’t staring at computer screens under bleak fluorescent bulbs."
    "Almost like... people who could be friends, rather than the lifeless mannequins that I’ve come to think of as coworkers."
    "Bodies that I’ve only ever seen in frumpy office attire sway before me in slinky evening dresses, curves accentuated by the hot red accents of light."
    "Before I can become too entranced by the sight, something snaps me abruptly back to attention."
    show cassidy teaser
    unknown_girl_say "Hey there, stranger."
    "I jump at the sound of an unfamiliar voice, coming clear and confident from what feels like just over my shoulder."
    "I manage to get my mind back together enough to turn to the source, realizing all at once that I had frozen, staring, in the doorway."
    unknown_girl_say "You're letting in all the cold air."
    hero.say "Oh."
    "I step forward from the door, allowing it to swing closed behind me with a final chilly gust."
    hero.say "Right, sorry about that. Uh, long day."
    "The girl in front of me just hums a breezy note, though her expression doesn’t change."
    "I can’t tell if it’s a sound of amusement or just dry acknowledgement. "
    "She stands leaning against the wall beside the doorway, looking luxurious in the shadows between two ornate pillars with a wineglass held delicately between two of her slender fingers."
    "Her dark eyes look me up and down, shamelessly sizing me up like an object on a shelf."
    "For some reason, my mouth has gone completely dry standing there before her. I swallow and manage to make myself speak."
    menu:
        "Ask if she's a new employee":
            "I don't think I recognize you from the office. Are you new?"
            "She gives a soft and smoky laugh that is almost lost beneath the bass of the music. I expect her to step forward from the wall and address me, but she doesn’t."
            unknown_girl_say "I've never been in your office."
            "She takes a long, purposeful drink of her wine to punctuate the sentence, watching me with eyes as fierce and determined as an animal over the brim of the glass."
            "I say nothing, and she casually lowers her gaze to the ruby liquid as she finishes her sip, shading those hawk's eyes beneath thick, dark lashes."
            unknown_girl_say "My daddy is your CEO."
            "Oh."
        "Compliment her" if hero.charm >= 25:
            "Hello, beautiful. I didn't catch your name."
            if "cassidy" in GIRLS:
                $ cassidy.love += 1
            "She seems unimpressed, watching me for another second before dropping her gaze to the ruby liquid in her glass, swirling it idly."
            unknown_girl_say "That's because I didn't give it."
            "One of those kinds of girls. That’s fine, I've dealt with them before. I give my most charming smile in return, refusing to let her break me."
            hero.say "Consider this my formal request, then. You must be new in the company. I'm positive I would remember you if I'd seen you around."
            "Her dark eyes turn up to me. I expect her to step forward from the wall to shake hands, or at least smile at my charm, but she does neither."
            "I get the immediate impression that she does not consider us peers at all, which is only further cemented by her reply."
            unknown_girl_say "My daddy owns your company."
            "Oh."
        "Ask if she crashed the party" if hero.charm >= 25:
            "You're not from the office, right? You just here to get some free wine?"
            if "cassidy" in GIRLS:
                $ cassidy.sub += 1
            "I smile, hoping that my negging comes across as charming despite my nerves."
            "She doesn’t seem particularly charmed. Not so much as a hint of a smile touches the corners of her lips, though I watch almost desperately for one."
            unknown_girl_say "My daddy's company paid for this wine."
            "Daddy's company?"
    hero.say "Dwayne?"
    "She takes a long, slow sip of her drink, watching me with eyes as cutting and calculating as a hawk's over the rim of her glass."
    "Her silence, her body language, and the distinct impression of being talked down upon were all answer enough."
    "She seems to enjoy the discomfort I’m obviously doing a poor job of concealing, finding myself suddenly face to face with the daughter of my boss’s boss’s boss, intimidating and gorgeous."
    "The first trace of amusement curls at one corner of her full lips, and I feel some of the panic inside of me soften."
    unknown_girl_say "It’s Cassidy."
    hero.say "Cassidy."
    "I have to swallow again before I can regain some composure. I need to get it together -- it isn’t like she’s a celebrity or anything."
    "No… it’s worse than that."
    "A celebrity has less looming, imposing power over my livelihood."
    "I remind myself that she isn’t my boss -- just a family member of the CEO, who I’d never even met -- and try to act like a part of me isn’t withering inside before her."
    hero.say "Nice to meet you. My names [hero.name]."
    "I hold out my hand."
    "She looks down at it for only a moment, though it feels like an awkward eternity, before she finally deems me worthy, stepping forward from the wall and taking it with the hand not still cradling her wine glass."
    cassidy_say "Pleasure."
    "I breathe a silent sigh of relief, and my smile spreads until it’s nearly beaming as I give the soft grip of her hand a single shake."
    hero.say "Pleasure’s all mine."
    "I release her hand and step back."
    "The music is pulsing through the room like a heartbeat, and though I know there are people all around us, my attention is fixed ahead of me."
    "She folds her arm back beneath the one holding her wineglass and seems to wait for me to say something."
    if hero.charm >= 25:
        menu:
            "Compliment her" if hero.charm >= 50:
                if "cassidy" in GIRLS:
                    $ cassidy.love += 1
                hero.say "You look stunning, have I mentioned that?"
                "She doesn’t blush or giggle, shifting her weight and looking almost bored."
                "I get the impression she gets told that a lot, whether by horny guys or just people trying to suck-up to the princess."
                "Either way, though, this time I do detect the tiniest hint of a smile on her primly pursed, full lips. I think it’s satisfaction, though, more than swooning."
                cassidy_say "You haven’t."
                "She replies, locking eyes with me and tilting her wine glass slightly in my direction as she continues..."
                cassidy_say "But thank you."
                hero.say "That dress is amazing."
                "I give a vague nod back over my shoulder toward the crowd."
                hero.say "Definitely makes you stand out."
                "Her smile spreads a little further. My eyes lock on her lips, and I wonder how soft they are beneath the velour of her lipstick."
                cassidy_say "It’s Chanel."
                "I nod and look impressed, though all I really understand about that is that it means the scrap of fabric covering her body cost more than my rent… probably a couple months’ rent."
            "Joke":
                "So what’s someone like you doing mingling with the commoners?"
                "She exhales a soft laugh, quirking her brows slightly, as if surprised to find me amusing."
                cassidy_say "Daddy was here, he told me I might as well come down with him, since I had nothing else to do."
                cassidy_say "Make an appearance, you know."
                "She raises her empty hand and gives a slow, regal wave, one a queen might give while standing at an ornate railing, overlooking her subjects."
                "It’s my turn to snort a laugh."
                hero.say "‘Was’ here?"
                "She nods, giving her eyes a slight roll and glancing irritably to the side."
                cassidy_say "I lost sight of him. He could be in the back in some VIP lounge or down the road with some business colleagues that stopped by, buying each other drinks."
                cassidy_say "He’s impossible to keep track of. Social butterfly."
                "I give my best look of sympathy."
                hero.say "So you’re stranded here."
                "She shrugs one bare shoulder."
                cassidy_say "Someone will eventually swoop in to rescue me and take me home."
                "I must have let something devious glint in my eyes, because she shoots a lidded look back to me and gave a single, small, curt shake of her head."
                cassidy_say "Don’t hold your breath."
    else:
        "Don’t you have better places to be, then?"
        if "cassidy" in GIRLS:
            $ cassidy.love -= 1
        "Her lip curls, slightly but perceptibly, as though she’s suddenly found herself looking at some kind of unpleasant animal."
        cassidy_say "Yes, I do."
        "She turns her gaze away from me purposefully and won’t reply to anything else I say to her. Eventually I give up and wander away, thoroughly and totally ignored."
    hero.say "Well, I guess I should make my way over to the actual party."
    cassidy_say "I guess you should."
    hero.say "Maybe I’ll see you around more often?"
    "I do my best to only sound hopeful enough to be flattering, and not desperate."
    "I think I succeed, but as always, her mild and unmoved expression makes it hard to tell."
    cassidy_say "If you look in the right places."
    "I think I might have to go out of my way to figure out what those right places are."
    hero.say "I’ll look forward to it, then."
    "She only smiles faintly, maybe a little amused. I hope she’s laughing with me, and not at me."
    "She curls the fingers of her free hand in a wave, dismissing me, and I turn back to the rest of the party, stepping away from her shadowed corner of the room."
    hide cassidy
    if not "cassidy" in GIRLS:
        show screen message(title="Teaser",what="Cassidy is only a teaser right now, she will be fully added to the game later on.")
        pause
        hide screen message
    if "aletta" not in GIRLS or aletta.love <= 150:
        if "aletta" in GIRLS:
            show aletta date
        else:
            show aletta teaser
        "I sigh and decide to make the most of it, looking to find some cute female to flirt with when suddenly I spot Aletta from across the way."
        "We make eye contact and I quickly look away but it is too late."
        "She excuses herself and starts to come over to me."
        "I hope to find someone to quickly talk to, because who really wants to talk to their boss outside of work? But don’t have any such luck."
        aletta_say "Hello [hero.name], nice of you to come. We have had a wonderful turnout this year."
        hero.say "Um yes. It looks like it."
        "I look into my drink and then all around and it is quiet for a moment before continues."
        aletta_say "Anyway, I just wanted to let you know I think you have been doing an amazing job at work lately."
        aletta_say "I don’t know what’s changed, but you have really stepped up your game. Keep up the good work."
        "I’m not sure what to say."
        menu:
            "Say Thank you.":
                hero.say "Thank you Aletta, that means a lot. I’ll do my best."
                "I see a flash of a small smile."
                aletta_say "I’m sure you will."
                if "aletta" in GIRLS:
                    $ aletta.love += 1
            "Say about time you noticed.":
                hero.say "Well, it’s about time you noticed how hard I work."
                "She makes a displeased face."
                aletta_say "Just because it isn’t said, doesn’t mean I don’t notice."
            "Say nothing.":
                if "aletta" in GIRLS:
                    $ aletta.sub += 1
                "I simple nod and take a drink."
        aletta_say "Well anyway, I also came over here to let you know that cameras will be going into the old copier room next week because supplies has been going missing so..."
        "You can imagine how embarrassing getting caught on camera doing anything... personal... with another employee would be."
        "I nearly choke on my drink."
        "Before I can say anything she holds up her hand."
        aletta_say "No need to say anything. I didn’t see anything, hear anything, or say anything. I just thought you would like to know."
        "She takes a drink of her glass and I feel myself start to sweat. Was it getting hotter in here?"
        aletta_say "Come on, there is someone I would like you to meet. She is new to the company. She has been making eyes at you all night."
        "That gets my attention."
        hero.say "Really who?"
        "Aletta waves her hand."
        aletta_say "Come on, follow me."
        aletta_say "She’s been with us a few months, but works in a different department."
        hero.say "Oh, makes sense why I haven’t noticed her tonight."
        "We make our way over to the other side of the restaurant."
        aletta_say "This is Lavish, Lavish this is [hero.name]."
        if "aletta" in GIRLS:
            show aletta date at left
        else:
            show aletta teaser at left
        show lavish teaser at right
        "Lavish suddenly blushes and reaches out to shake my hand."
        lavish_say "Nice to meet you [hero.name] I have heard a lot about you."
        "She flashes a smile to Aletta and I wonder what is going on."
        hero.say "You do look familiar, have we meet before?"
        lavish_say "Oh um not really. Just in passing."
        hero.say "Oh oh right! I knocked all those files out of your hands… Sorry about that."
        "I give a nervous laugh but she gives a laugh of her own."
        lavish_say "That’s alright."
        aletta_say "So, [hero.name] Lavish starts work in your area soon."
        "I thought if she needed anything you would be a good one to help her out until she gets the hang of things."
        "Lavish beams at this and nods her head."
        "By now I realize that this girl as a crush on me, and I have to admit she is cute."
        "Wait, did my boss just set me up with someone?"
        hero.say "Of course, I wouldn’t mind helping out at all. My desk is fairly easy to find."
        aletta_say "[hero.name] has been doing rather well lately. I’m sure you two could learn from each other."
        lavish_say "Oh yes! Aletta has told me how you have been leaving others in the dust."
        hide lavish
        if "aletta" in GIRLS:
            show aletta date
        else:
            show aletta teaser
        "I quickly turn to Aletta who looks like she has been put on the spot."
        hero.say "Has she now? Well I don’t know if I would say that."
        hide aletta
        show lavish teaser at center
        lavish_say "Don’t be modest! Your numbers have been great this last month!"
        "The only way for her to know that is if Aletta had shown her."
        "I turn to say something to her but she is no where to be found."
        "I shake my head."
        hero.say "Would you like to go get another drink with me?"
        "She gives me a look like I just made her night."
        lavish_say "Sure."
        hide lavish
        if not "lavish" in GIRLS:
            show screen message(title="Teaser",what="Lavish is only a teaser right now, she will be fully added to the game later on.")
            pause
            hide screen message
    return

label palla_event_01:
    show palla teaser at left
    show audrey teaser at right
    "As I walk down the mall, I notice Audrey talking to a cute redhead."
    audrey_say "Hey."
    hero.say "Hola"
    "The redhead glances over at me, her eyes judgmental."
    palla_say "Hi..."
    audrey_say "This is Palla. We’ve been friends for, like, forever!"
    palla_say "It’s... nice... to meet you, [hero.name]. Audrey can’t seem to stop talking about you."
    audrey_say "Hey, I talk about more than, you know!"
    palla_say "Certainly hyping him up, though. If you like him, you like him. I can’t account for your... tastes."
    audrey_say "Look, we gotta go. See you at work."
    "After Audrey leaves, Palla smirks."
    palla_say "Yes... hope to see you real soon."
    "I’m left wondering just what the heck is going on with this Palla girl."
    "Was she being condenscending... or was she flirting?"
    $ game.set_flag("pallastart",1)
    hide palla
    hide audrey
    if not "palla" in GIRLS:
        show screen message(title="Teaser",what="Palla is only a teaser right now, she will be fully added to the game later on.")
        pause
        hide screen message
    return

label alexis_event_01:
    play sound "sd/cell_vibrate.mp3"
    "Oh, looks like a new number."
    "Maybe someone calling in regards to work?"
    hero.say "Hello? This is [hero.name] [hero.family_name]."
    alexis_say "[hero.name]? [hero.name], do you remember me? OMG, it’s me, Alexis!"
    hero.say "A... Alexis!? Wow, yeah, it has been awhile!"
    scene bg black with fade
    show alexis teaser
    "Alexis... she was my girlfriend back in high school."
    "I was close to her family."
    "She and her sister Kylie were both pretty close back then, but after the ‘incident,’ all three of us kinda just fell apart."
    "I mean, the fact that she cheated on me with the PE teacher wasn’t exactly good for our relationship, either."
    show expression "bg "+game.room
    hide alexis
    with fade
    hero.say "So, uh, how’d you get this number?"
    if game.get_flag_value("kyliestart"):
        alexis_say "Hehe, silly."
        alexis_say "Kylie told me she saw you the other day and told me all about that promotion you had."
    else:
        alexis_say "I found out from the company’s directory, of course."
        alexis_say "I heard from a friend of a friend online that you got that big-time promotion."
    alexis_say "So, I thought I’d congratulate you."
    hero.say "Oh, thank you!"
    "In reality, it’s really nice to hear from her again, but I got to make sure."
    hero.say "You’re not just calling to say ‘congrats,’ are you?"
    "She giggles, the amount of times she’s laughed during this conversation tells me she most certainly has an ulterior motive."
    "Time to see if it will be in my favor or not."
    alexis_say "You know me too well. Don’t you?"
    alexis_say "You got me."
    alexis_say "Here’s the deal: You got that cushy new job."
    alexis_say "I got myself a new dress."
    alexis_say "I was thinking we’d meet for dinner. What do you say?"
    menu:
        "No":
            hero.say "Yeah, no."
            hero.say "Alexis. You had your chance."
            hero.say "I gave you my high school years, and you repaid me by cheating on me the first chance you could get."
            hero.say "In fact, Kylie has been cooler than you were."
            hero.say "I’m sorry, but I’m not going to fall for your trap again."
            alexis_say "Kylie!?"
            alexis_say "That psycho bitch? You don’t know what you’re messing with. She’s-"
            hero.say "I’m not listening to you anymore, Alexis. Good bye."
            alexis_say "Wait. [hero.name]!"

            "I can’t believe she had the nerve to try and scam me into paying her dinner."
            "Guess only one of us has moved on with our lives."
            "How pathetic."
            return
        "Yes":
            $ game.set_flag("alexisstart",1)
            hero.say "Dinner? Yeah, actually that sounds great."
            hero.say "I haven’t been able to properly celebrate yet. Where were you thinking?"
            alexis_say "Oh, just a little place called Tres Riche"
            hero.say "T... Tres Riche!? That’s expensive!"
            alexis_say "Not for someone in your tax bracket, it isn’t."
            "Well, that’s certainly true, now..."
            "I am about to get into a lot of expendable riches."
            "I could splurge and impress my old girlfriend."
            hero.say "Well, when would you like to go?"
            "She pauses for a moment, her extended 'hmmmmm...' makes me feel she’s just playing it up."
            alexis_say "I'll call you to let you know."
    hero.say "Works for me. Will I pick you up, or..."
    alexis_say "That’s fine. I’ll just meet you there."
    alexis_say "Let’s take baby steps getting back into each other’s lives."
    alexis_say "You know? Not like I’m gonna bang you on our first date, haha."
    hero.say "Well, it wouldn’t be the first time..."
    alexis_say "Hm?"
    hero.say "Nothing, nothing. I’ll see you there, okay?"
    alexis_say "Sounds great to me. See ya, lover boy."
    play sound "sd/dialtone.mp3"
    "Heh... ‘lover boy.’ It’s been a long time since someone’s called me that."
    "Well, new position, old girlfriend."
    "Things seem to be looking up for [hero.name]!"
    if not "alexis" in GIRLS:
        show screen message(title="Teaser",what="Alexis is only a teaser right now, she will be fully added to the game later on.")
        pause
        hide screen message
    return

label kylie_event_01:
    $ game.set_flag("kyliestart",1)
    "Hurrying from one lecture to the next, my mind's already tuned into the subject that awaits me."
    "That means the noise of the other students around me is nothing but a meaningless hubbub of sound."
    unknown_girl_say "Hey, hey - you over there!"
    "I don't know why that one shout reaches my ears over all the others, but I ignore it and keep going all the same."
    "It's not that I don't have any friends around here, but one of them would just have shouted my name if they wanted to get my attention."
    unknown_girl_say "[hero.name]?"
    unknown_girl_say "[hero.name] [hero.family_name]?"
    "Well, maybe they'd start to shout my name after I'd walked past and ignored them like an ignorant sod!"
    show kylie teaser
    "I stop and turn on my heel in the general direction of the calls, seeing a pretty young-looking girl waving at me almost frantically as she hurries over."
    "She's got a beaming smile on her face and an innocence in her eyes that only makes her seem even younger."
    "But as she comes closer, I can see that her body gives the exact opposite impression, the tight shirt and short skirt she's wearing emphasizing this as well."
    "Coming to a halt before me, she holds her hands behind her back and literally bounces up and down on her toes with what I take to be eager enthusiasm."
    "This motion makes her long, platinum blonde hair sway and her chest, which is straining the buttons of her shirt, bob distractingly."
    "I've no idea who this girl is, or what she wants with me - so I just give her a weak smile and wait for her to speak."
    "Though the longer I look at her, the more aware I become of just how cute she is..."
    unknown_girl_say "Aww, come on - don't tell me you've forgotten all about me, [hero.name]?"
    hero.say "Erm...I...well..."
    unknown_girl_say "I'm Kylie!"
    unknown_girl_say "Kylie - Alexis's sister?"
    hero.say "Oh, shit - Kylie!"
    hero.say "Is that really you?!?"
    "Suddenly my memory kicks in, and I can almost see time running backwards before my eyes."
    "I can recall her, without all of the changes that growing up has obviously made to her, wearing a pink T-shirt that has ponies or unicorns on the front."
    "I remember braces and acne, skinny legs and pig-tails - Alexis's little sister that always bugged her back in high-school."
    hero.say "Wow...Kylie...you grew...UP...you grew up!"
    kylie_say "Yeah, well - I'm definitely not a kid anymore..."
    hero.say "I can see that, Kylie."
    hero.say "You look..."
    menu:
        "Inappropriate":
            hero.say "...inappropriate."
            hero.say "You know what people think about girls who dress like that, right?"
            "Kylie's mouth opens wide in surprise, and she ceases bouncing on the spot."
            kylie_say "Don't be such a prude, [hero.name]."
            kylie_say "We're at college now - I can dress how ever I want to."
            kylie_say "You know, you sound just like my Mom - always nagging at me!"
            "I hold up both hands in a gesture of surrender."
            hero.say "Okay, okay, Kylie - point taken!"
            hero.say "I guess I just remember you as a kid, from back when I was dating Alexis..."
            "At the mention of her sister's name, an odd intensity seems to begin to burn in Kylie's eyes."
            kylie_say "Oh, I wondered when you'd mention HER!"
            kylie_say "Aww...I can see you're still hurt from when she cheated on you."
            kylie_say "Even after all this time, too."
            kylie_say "What a fucking bitch - she never appreciated you, [hero.name]."
            "More than a little taken aback by the venom in Kylie's voice, I try to calm things down."
            hero.say "It was a long time ago, Kylie - and she is your sister, after all..."
            kylie_say "Whatever - who wants to talk about Alexis, anyway?"
            kylie_say "I came over to see how YOU were doing."
        "Stunning":
            hero.say "...REALLY good!"
            hero.say "That skirt and the shirt...well...they really...flatter you!"
            "Suddenly, Kylie's not smiling innocently, but rather grinning at me with a knowing look in her eyes."
            kylie_say "Aww...thank you so much, [hero.name]."
            kylie_say "Coming from you, that means SO much to me."
            kylie_say "You have no idea how much it means to me."
            kylie_say "Everyone sees me as Alexis's helpless little sister."
            kylie_say "I've been waiting for someone to come along that can see me for what I really am!"
            "Kylie keeps on staring at me for a moment, an odd intensity burning in her eyes."
            "But then she seems to catch herself, and begins to speak again."
            kylie_say "But that's far too much chatter about me!"
    kylie_say "I want to hear all about you and your life - I want to hear everything about you that I've missed!"
    "I shake my head for a moment, finding the experience of talking to Kylie oddly disorienting."
    hero.say "What, me?"
    hero.say "Okay, I guess - I can't complain."
    "At this, Kylie leans in closer, putting me in mind of a cat that's just seen a mouse."
    kylie_say "Hmm, well - from what I heard, you've landed yourself a pretty decent job..."
    "For a moment I just shrug, as if weighting up an answer."
    "But then I can't help frowning as a thought suddenly occurs to me."
    hero.say "Wait a minute, Kylie - why would you know anything at all about my job?"
    "Kylie's eyes open wide at my question, and she looks this way and that, as if for a moment she can't meet my eye."
    kylie_say "Huh...what...why would I..."
    "I screw up my face as I try to figure out why Kylie has suddenly become so shifty and evasive all of a sudden."
    hero.say "Hang on, did Bree tell you about what's going on in my life?"
    kylie_say "Bree?"
    hero.say "Yeah, Bree - you know, my housemate?"
    hero.say "She goes here too."
    kylie_say "Bree...yeah, that's who told me about you."
    kylie_say "She was in one of my lectures, and we got talking."
    kylie_say "Kept going on and on, telling me about this great guy that she lived with called [hero.name] - and so I figured it might be you."
    kylie_say "I've been keeping an eye out for you around the campus ever since."
    kylie_say "It's just SOOOO great to finally see you again!"
    "It sounds like a strange coincidence to me."
    "But then you hear about stuff like this happening all the time to other people, right?"
    hero.say "You're serious - Bree talks about me that much?"
    kylie_say "Yeah, it was pretty weird!"
    kylie_say "Maybe she was just stoked to have such a great place to live and a nice housemate to go with it?"
    kylie_say "I gotta say, the way she described it, I am kinda jealous."
    kylie_say "She made it sound so great."
    kylie_say "Hey - while I mention it, would you let me know if you ever have a room free there?"
    hero.say "I'll try to keep it in mind, Kylie..."
    hero.say "Anyway, it's good to know that you're here and doing okay."
    "Kylie's eyes widen and she smiles in that same innocent and yet slightly odd manner."
    kylie_say "Are you REALLY glad I'm here?!?"
    hero.say "Well, they always said you were the smart kid in your family..."
    kylie_say "Aww, that's so sweet of you to say!"
    kylie_say "Kind of a put-down for Alexis - but then she proved she was pretty dumb by cheating on a great guy like you!"
    play sound "sd/cell_vibrate.mp3"
    kylie_say "Ooooh, look at the time - I gotta get going!"
    kylie_say "Can’t be late for class AGAIN - but we should meet up soon, really catch up, yeah?"
    kylie_say "I study in the library most nights, so maybe find me there?"
    hero.say "Erm, okay, I guess - see you there some time."
    hide kylie
    "I stand and watch Kylie hurry off for a couple of seconds, and then remember that I have a lecture to get to as well."
    "But now I'm preoccupied by thoughts of Kylie and her elder sister, rather than the academic subject at hand."
    "I haven't thought about that period in my life for quite some times, and it instantly raises mixed emotions for me."
    "Alexis and I dated when we were in high-school and Kylie herself was just a kid."
    "We had some wonderful times back then - I even snuck into her house a couple times while her parents were out."
    "Even then, the sex was amazing."
    "But Alexis ended up hurting me so badly that the wounds have never fully healed."
    "Do I really need either of them back in my life now that I'm supposedly a responsible adult?"
    "Maybe I'm being unfair though, dumping Kylie in with my bad memories of her sister."
    "Perhaps Kylie really is as sweet and innocent as she seems, and wouldn't as much as hurt a fly?"
    if not "kylie" in GIRLS:
        show screen message(title="Teaser",what="Kylie is only a teaser right now, she will be fully added to the game later on.")
        pause
        hide screen message
    return

label harmony_event_02:
    scene bg church
    "I almost can't bring myself to go back to church after what happened in the men's bathroom last time."
    "Aside from the sheer embarrassment of it all, did it have to be a girl like that that walked in on me?"
    "Whenever I close my eyes, all I can see is her face as she got the entire load at almost point-blank range."
    "She's so innocent and pure that it felt as wicked as stabbing a puppy with a kebab skewer."
    "But in the end, I force myself to go back and sit in the same pew, trying to keep my head down."
    "I figure that if I can make it through the entire service without anyone cornering me, then I'm safe."
    "Because if they were going to confront me about it, why would they wait for their chance to do so?"
    "I mumble my way through the entire thing, nodding furiously whenever the priest mentions the idea of sin and going to Hell."
    "The passage of time seems to stop for me, and I'm just staring a hole in the floor between my feet like my life depends on it."
    "But then the sound around me changes to people mumbling and the tread of feet."
    "I look up to see that everyone on the same pew as me is getting up and filing out of the church."
    "That's it - the service is finally over!"
    "I hurry to follow the example of my fellow service-goers, shuffling out of the place as quickly as I can manage."
    "The fresh air outside never tasted so good, like freedom at long last..."
    show harmony teaser
    unknown_girl_say "Erm...hello..."
    "I recognise the voice instantly, as my blood runs chill in my veins."
    "Turning around slowly, I see the same curvy figure, the same cheery dress and the same open, innocent face."
    hero.say "H...Hello..."
    "I can see that the smile on her face is pained, as if this is every bit as hard for her as it is for me."
    "I suppose that's something at least, I know she's not confronting me to get angry or show me up in front of the rest of the congregation."
    hero.say "Look...about last week, I don't..."
    "A flush of resolution suddenly crosses her face, and she holds up a firm hand to keep me from going any further."
    unknown_girl_say "PLEASE..."
    "She almost leaps at the realisation of just how loud and shrill her own voice is."
    "After coughing demurely, she gathers herself and tries again."
    unknown_girl_say "Please, don't feel the need to mention it - I mean really, please don't."
    unknown_girl_say "The good book tells us that it is only he without sin that shall cast the first stone of condemnation."
    unknown_girl_say "John, chapter eight, verse seven."
    "I blink in surprise as she adds the source of the quote almost under her breath, like it's an unconscious tic."
    "Managing a weak smile, I try to console myself with the fact that she's apparently not mad at me cuming right in her face."
    hero.say "That's very Christian of you..."
    unknown_girl_say "Well, that is why we're both here, after all!"
    "All I can offer is a slight chuckle in way of response."
    hero.say "Okay...if there's nothing else..."
    "I begin to turn away, and then I feel a hand suddenly grabbing my wrist."
    "Looking down, I see that the hand belongs to Harmony, and her grip's surprisingly strong."
    "Casting my gaze back up at her, she almost jumps and lets go as she realises that she's technically manhandling me right now."
    unknown_girl_say "Sorry...I just wanted to ask you something, if that's okay?"
    "God, her eyes are so huge, and her body..."
    "I find myself nodding as I feel drawn in my the gravitational pull of her unfeasibly huge breasts."
    unknown_girl_say "Oh, that's great!"
    unknown_girl_say "I was wondering if you'd like to join me for some private Bible study classes?"
    unknown_girl_say "You know, seeing as you're obviously such a terrible sinner and in serious danger of becoming a lost soul!"
    "What - Bible study, sinner, lost soul!"
    "My head snaps up and I look her straight in the eye."
    menu:
        "Refuse":
            hero.say "Ah, no...I don't think that would be a good idea."
            unknown_girl_say "But..."
            "I cut her off before she can come up with a perfectly sensible reason to disagree with me."
            hero.say "I'm actually undertaking an intense course of biblical study myself, in order to purge myself of my particular demons."
            unknown_girl_say "Those would be the same ones you were busy purging yourself of last week in the toilet?"
            "I try to ignore the barbed nature of her question and press on regardless."
            hero.say "And as good book tells us - 'God helps those who help themselves'."
            hero.say "Hezekiah, chapter six, verse one."
            "she frowns at my quote, wrinkling her nose in the cutest way imaginable."
            unknown_girl_say "I think that verse is apocryphal!"
            "By now, I've managed to break away and escape into the crowd."
            hero.say "Thanks for the compliment, I made it up myself!"
        "Accept":
            $ game.set_flag("harmonystart",2)
            hero.say "Urm, yeah...sure, why not."
            "She positively beams at me, and I find myself returning the smile before it even dawns on me that I just said yes."
            unknown_girl_say "Oh, that's just wonderful news!"
            harmony_say "I shall introduce myself then, Harmony, pleased to meet you."
            harmony_say "When you did...what you did to me last week, I was convinced it was the work of the Devil!"
            harmony_say "But somehow, I couldn't get the image of your face out of my thoughts...and my dreams..."
            harmony_say "So I spent time in quiet prayer and contemplation, asking God to show me the truth."
            "Her eyes are beginning to shine with a zealous light that's really becoming quite unnerving as she goes on."
            harmony_say "And he's revealed to me that it was all a clever plan to test my faith and charge me with the task of saving your soul for him!"
            "Jesus, does she ever stop talking about God?"
            "Especially when there are so many more enjoyable uses I can already think of putting her mouth to!"
            "Ah, yes...well maybe she does kind of have a point about me there..."
            "Who knows, I might actually get something out of these classes that makes me a better person?"
            "And even if not, it's an excuse to spend some one-on-one time with her under legitimate circumstances."
    "As I walk away through the rapidly thinning crowd of the congregation, I can't help but shake my head in confusion."
    "Am I not supposed to come to church so that I can feel better about myself?"
    "Not accumulate even more hang-ups and desires of a carnal nature?"
    if not "harmony" in GIRLS:
        show screen message(title="Teaser",what="Harmony is only a teaser right now, she will be fully added to the game later on.")
        pause
        hide screen message
    return

label harmony_event_01:
    scene bg church
    "As I am waiting for the church service to start I am having trouble remembering why I came here again."
    "My dress clothes are itchy and hot, not to mention the fact that I had woken up late and with a serious personal problem and had had no time to take care of it."
    "It isn’t really noticeable in these pants, but I still can’t wait to go home and take care of it."
    "And with it taking so long for service to start I don’t know if I am going to last."
    "How guilty would I feel for jacking off in a church bathroom?"
    "I look forward then as something catches my eye and my mouth drops open."
    show harmony teaser
    "This beautiful- no gorgeous- little curvy red head had just walked up to the choir and was passing out the music."
    "My eyes follow her and I can’t seem to look away."
    "That’s when I notice my little problem in my pants just became a big one."
    hide harmony
    menu:
        "Masturbate in the bathroom":
            "Quickly excusing myself I hurry off to find the nearest restroom."
            "I am sure God would forgive me, after all, it was a human need after all."
            "I can’t help it."
            "To my much annoyance though, I reach the only discrete bathroom and an out of order sign is hanging on the door."
            "I groan loudly."
            "I am not walking in front of everyone with a hard on in church to go jack off in the bathroom."
            "Looking around I find a spare room and quickly step inside."
            "I check the time and then quickly undo my pants and free my member."
            "If I make it quick and then use some hand sanitizer that is everywhere in this place I will be fine."
            "I try to stay quiet but I am so horny I can’t hold back the moan has I move my hand up and down my cock."
            "I didn’t know what it is about that girl but she really has me going."
            menu:
                "Imagine her sucking you off":
                    "I start to imagine her cute lipstick less mouth around my cock, bobbing up an down."
                    "The picture in my head is so pretty, but something just doesn’t feel right about imagining someone I don’t know giving me a blow up while I jack up in a church"
                "Imagine getting to know her":
                    "I start to imagine what it would be like to meet her."
                    "She seems really sweet from what I saw of her interacting with the others."
                    "She might be a goody-two-shoes, but I find myself wanting to know more about her than just what she looks like."
            "Seeing that time is getting away from me I start moving my hand up and down my cock as fast as I can as my breathing picks up."
            "It just feels so good I can’t help myself."
            "Suddenly I hear the door knob turn and panic flows over me, knowing that whoever opens that door is about to see me with my hand around my cock jerking off at the speed of light."
            unknown_girl_say "Is someone in here? Is everything okay?"
            show harmony teaser
            "The door swings open and to my horror it is the redhead freckle faced girl I was admiring earlier."
            "The sight of her is too much and before I can stop myself or turn I cum, and some of it lands on her."
            "She looks horrified at me and quickly looks to me to her arm where my cum is at, back to me and then off to the side."
            unknown_girl_say "I’m... I’m so sorry to walk in on you sir!"
            unknown_girl_say "I... I didn’t realize!"
            hide harmony
            "And with that she was off."
            "My heart pounding but for a whole different reason now, I quickly stuffed myself back in my pants and went to go find some place to clean up."
            "As I wash up I think about how weird it is that I was the one in the wrong but yet she is the one who apologized."
            "Whatever her reason why, I was sure I’m not dating a date with her now anytime soon."
            $ game.set_flag("harmonystart",1)
        "Wait until you get home to masturbate":
            "I decide I don’t have the guts to go take care of my needs in a church so I just sit there and try to hide my erection the best I can."
            "I don’t realize I am staring until the second time she glances my way, and instead of a cute smile I get a uncertain frown and then she walks away."
            "I wait but I never see her come back, and I am not sure where she went."
            "Great going, idiot. I think. You scared her off."
            "So much for getting a date with the cutie now."
    return

label lexi_event_01:
    $ game.set_flag("lexistart",1)
    scene bg alley
    "I start making my way down the street, feeling another presence lingering nearby."
    "So I look over."
    "That’s...when I see her."
    show lexi teaser happy
    "She definitely stands out, leaning against the wall with her arms folded like she was just waiting for me to come along."
    "Bleached blonde hair, an outfit leaving little to the imagination. Taut denim shorts, from which I can clearly see a pink thong saying hello."
    "The top she is wearing is white and near transparent, I can see her nipples even from a distance."
    "She has a nice face, coupled with some silver piercings."
    "Frankly...she looks like a bit of a slut."
    "But! I suppose I can’t judge on first glance..."
    unknown_girl_say "Hi there stranger."
    "I fix my collar instinctively, fidgeting."
    "I wasn’t expecting her to be interested in talking with me."
    "After all...I don’t think I stand out all that much compared to other guys."
    "But maybe to her..."
    unknown_girl_say "Well? Cat got your tongue or somethin’?"
    hero.say "No I...I’m not."
    unknown_girl_say "Clearly..."
    "Her painted lips curl into a dark smile."
    unknown_girl_say "What’s your name?"
    "I didn’t even realize it, but I’m already standing before her, talking with her casually like this."
    "I find myself telling her anyway."
    hero.say "[hero.name]...and yours?"
    "She tilts her head a little."
    unknown_girl_say "The name’s Lexi, love."
    lexi_say "Were you out with your friends tonight then?"
    hero.say "Yeah, basically."
    lexi_say "Did you have fun?"
    "I barely noticed it before, but she’s gravitating closer towards me with every passing second."
    lexi_say "Did you, eh?"
    hero.say "Well uh...yeah. Yeah it was fun..."
    lexi_say "But I bet I could show you something a lot more enjoyable..."
    "Wondering what on earth she means, I find myself being lured anyway."
    "Lexi waggles the fingers on one hand to encourage me along, while she backs up step by step into a nearby alleyway."
    "There’s a smart part of me that’s screaming ‘STAY AWAY’."
    "Yet there’s also a part of me that can’t resist one bit..."
    "Before I even really know what I’m doing, I’m halfway down the path with her."
    "She keeps on beckoning me more, and I can’t resist, I have to follow."
    "What I don’t see is the hidden menace in her eyes."
    lexi_say "I think this should be private enough for us, right? Neat little spot."
    hero.say "Private enough for what?"
    "I’m only playing dumb. She knows and I know."
    "Just like that she comes sauntering closer, deliberately thrusting her chest forward."
    "Now that I feel I have a pass to look at her assets, I can acknowledge how stacked she is."
    "Lexi only confirms that by pressing up against my front and groaning just a little bit, as if she’s already getting off on this."
    lexi_say "I know they were the first thing that you looked at. It’s okay, you don’t have to be shy..."
    hero.say "...Are you...sure about this?"
    lexi_say "Sure about what, big guy?"
    "‘Big guy’? I’ve always felt kinda lanky, so I can only guess she means..."
    hero.say "Well...I mean we don’t even know each other-"
    lexi_say "Oh come on, do we have to?"
    "She winks and brings her bottom lip beneath her teeth."
    "I glance down a little shyly, noting the piercing she has in her bellybutton."
    lexi_say "Why don’t you just hush up and let me give you a night to really remember?"
    "Well, she’s inviting it, so how can I resist? We both seem to want this."
    "So I let her start to feel me up, and meanwhile my own hands raise to her..."
    "Only...I don’t even get a chance to touch her. And her hands are only at my shoulders when she suddenly pulls back."
    "As I look at her, startled, I can see her eyes aren’t focusing on me anymore."
    "Something...behind me?"
    "Slowly...uneasily...I turn."
    hide lexi
    show danny
    thug_say "Hey buddy, what you doin’?"
    if not game.get_flag_value("thugfight"):
        "Behind me, standing at the exit of the alleyway, is a tough looking guy. And I mean tough."
        "He’s about as buff as they come, and stands tall at what must be over 6’4..."
        "Tan skinned with a biker’s sort of hairdo."
        "Plus he’s wearing a leather jacket, and that’s all I really need to know."
        hide danny
        show lexi teaser annoyed
        lexi_say "Danny, thank God you’re here."
        "Surprised again, I look back at Lexi after hearing that."
        "She’s leaning against the alley wall like some sort of damsel in distress, arm above her head and everything."
        hero.say "Lexi!? What are you doing? What are you saying!?"
        lexi_say "What do you mean, creep!?"
        "...’Creep’?"
        hero.say "Lexi..."
        hide lexi
        show danny
        $ thug_name = "Danny"
        thug_say "Okay, I think it’s about time we get this over with."
        $ result = game.get_flag_value("thugfight")
        if result > 0:
            thug_say "And this time it won't go your way fucking prick."
        "Wondering what he means by such an ominous statement, I turn around, only for him to snatch my collar with both hands and hoist me up."
        "Guy must be strong, I wouldn’t say I’m short."
        "Either way, I hit the wall hard and groan."
        "The back of my head blooms with pain, my vision weakening momentarily."
        "When it clears again I can look down and see him grinning up at me."
        "In the background, Lexi has a similar expression."
        "So...she really set me up then?"
        "Maybe I should have expected this. I should have seen it coming, it was just too good to be true."
        show danny fist angry
        thug_say "Any last words before I pummel you into the ground?"
        "So this is it."
        "I die getting beaten in an alleyway by some mobster and his sly fox of a girlfriend."
        "At the very least I got to feel her boobs against me before it happened, but I don’t know how much better that makes me feel."
        "Last words, eh?"
        "Do I have any regrets? Probably. Probably many, but I haven’t got a time machine have I?"
        hero.say "...I guess...not..."
        thug_say "Great, saves me some time. Maybe if you get lucky you’ll still be alive."
        "So it really is finished."
        "He might not finish me off completely, but I have a feeling that if I come to after this, I won’t have a wallet anymore."
        "Sneaky little scheme they’re running, must earn them a lot."
        "...But...is it truly the end?"
        "Am I really going to let myself get humiliated like this?"
        "I feel a sudden rush of adrenaline. Am I really giving up?"
        "How could I do it so easily after everything I’ve been through in my life before this?"
        "No...this is nothing, right? All I have to do is stop him."
        python:
            d = 25
            if not "martial_arts" in hero.skills:
                d += 25
        if not hero.fitness >= d:
            "I swing my fist and hit him right between the legs. That should work, right?"
            "The toe of my shoe hits him hard, it almost hurts me too with how firmly I kick him."
            "I expect it to make him crumple."
            "Except...he doesn’t even flinch. Just stares back at me mockingly."
            thug_say "Oh? Was that supposed to tear me down?"
            hero.say "Wai-!!"
            show danny fight win lexi
            "Before I can even beg, he slams my head hard with his fist."
            "Pain throbs. I black out immediately..."
            "It was so easy for him. Proof I was definitely outmatched."
            hide danny
            scene bg black with fade
            $ renpy.pause(1)
            scene bg alley with fade
            "I don’t know how long I’m left lying there. Eventually I wake up again though."
            "My skull feels fit to burst, but I manage to sit up. Immediately my hands go for my pockets."
            "Gone. My wallet is gone."
            if hero.money > 500:
                $ hero.money -= 500
            else:
                $ hero.money = 0
            $ hero.grooming -= 5
            $ hero.energy -= 5
            $ hero.fun -=5
            hero.say "Dammit!"
            "I slam my free hand down on the wet concrete, and look up above."
            "Rain spits down upon me like I’m being mocked or something."
            "I guess it must have started while I was knocked out. I’m not even sure how long I was."
            "At the very least it’s still dark, the only light coming from the street lamps that reflect in the puddles too."
            "Either way, I force myself to stand up and groan, clutching the crown of my head and feeling a little blood there."
            "Of course, I did hit the wall pretty fucking hard. In a way I actually am lucky to be alive."
            "With strength like that, he could have done a lot worse..."
            "But I am alive, and I can move forward from this. And hopefully forget."
            "Especially Lexi."
            "I hope I never have to see her ever again."
        else:
            show danny fight lose lexi
            "All the training I had at the gym is not for nothing."
            "I take a karate stance and hit him right in the stomach..."
            "He falls to the ground like a sack of beans, vomiting his lunch..."
            thug_say "Urgh..."
            hide danny
            show lexi teaser angry
            lexi_say "Danny!!"
            "I quickly make a break for it, still clenching my sore fist."
            "That’s right. Like hell I’m getting mugged tonight!"
            "I press on, eyeing the exit of the alleyway like it’s the finish line for a race."
            lexi_say "Wait! [hero.name] wait!!"
            "Hearing Lexi calling me, I turn and glare over my shoulder at her. She’s rushing after me, and she looks desperate now."
            "It’s bizarre. Only minutes ago she was acting like I was some kind of stalking pervert that she wanted to shake off her shoe."
            "Yet now she thinks she can run after me and expect me to stop for her?"
            hero.say "If you think I’m driving your accomplice to the hospital you can forget it. I don’t even have a car."
            "I scoff, and start moving again."
            "I wish I had never even met her in the first place. For sure, I shouldn’t have followed her in here so willingly."
            "I can feel myself sobering up with all the adrenaline, and realizing what a mistake I made."
            "I only hope that I never see her again..."
            $ game.set_flag("thugfight",1)
            $ game.set_flag("dannyvictory",1)
    else:
        thug_say "Oh, it's you.."
        thug_say "Sorry sir, I didn't reconise you."
        thug_say "Come on Lexi, let's get out of here."
        $ game.set_flag("dannyvictory",2)
    if not "lexi" in GIRLS:
        show screen message(title="Patreon Edition",what="Lexi is only available in the Patreon Edition of the game.\nVisit {a=https://www.patreon.com/Andrealphus}patreon.com/Andrealphus{/a} to become a patron and get to know her better.")
        pause
        hide screen message
    return

label bj_birthday:
    "I enter the living room."
    "Nothing crazy could happen here, right?"
    bree_sasha "Hey, [hero.name]"
    show bree underwear at left
    show sasha underwear at right
    "Suddenly, I'm bombarded with the sight of both of my roomates standing right before me, down to their lingerie. "
    hero.say "Whoa! Bree!? Sasha!? The the hell is all this about?"
    sasha.say "Hey, [hero.name]"
    sasha.say "You know what day it is."
    bree.say "I, like, don't think he could have forgotten, right...?"
    hero.say "Today?"
    "I think about it a moment."
    hero.say "Wait... did you two... did you remember my birthday?"
    sasha.say "Remember it?"
    "Sasha asks, scoffing, her hands on her hips."
    sasha.say "I think we did a lot more than that!"
    bree.say "Or... I mean technically..."
    sasha.say "We're GOING to do a lot more than that."
    sasha.say "Go ahead, [hero.name] strip."
    bree.say "Um, take your time if you want... I mean, it's your day, do whatever you want...?"
    "The two are like Yin and Yang, Sasha seems happy to be stood there, confident, while Bree seems more embarassed about the situation."
    "I don't bother with questions though, and simply do as I'm told, and soon, I'm naked before them, intrigued and excited."
    sasha.say "Now, sit on the couch."
    "Sasha's fingers hooks over the straps of her bra then she slides the straps over her shoulders."
    bree.say "Yeah, just um... Relax."
    "Bree stammers her line, almost as though it was rehersed, while shimmying out of her panties."
    show bree naked at left
    show sasha naked at right
    "When I glance at them again, Bree and Sasha stand on either side of the couch."
    "Both of my roomates have removed their clothes and smile down at me with lust and intent."
    bree.say "I hope you enjoy this, [hero.name]..."
    sasha.say "Now then!"
    sasha.say "Let's get down to business shall we?"
    "The two nod at each other."
    "They must have rehearsed this, or at least planned it out."
    "For a moment, I imagine the two of them alone, nude, and if my cock wasn't already standing as straight as a candle, I'd immediately get hard from that."
    "The two of them lean in over the couch, each of them giving me their fluttering bedroom eyes."
    "As they climb up onto the couch, Sasha on my left and Bree on my right, the soft words whisper gently to my ears."
    sasha.say "Happy Birthday to you..."
    "The song continues as they synchronize themselves, sliding their fingers down my body."
    "Soon, the two lay their, their warm bodies up agianst my own, pressed against my spread legs."
    "I reach up and hold onto both of them, sliding my own fingers over their smooth skin."
    hide bree
    hide sasha
    show 3bj2 bree sasha
    "Together, they wrap their fingers around my shaft, and also together, they roll their tongues out, licking up along my length."
    hero.say "O... oh wow..."
    show 3bj2 bree sasha breesuck
    hero.say "You two... you work great together."
    sasha.say "Only the best for the birthday boy..."
    hide 3bj2
    show 3bj2 bree sasha sashasuck
    bree.say "I just wanted to repay you, for how good roommates you both have been."
    hide 3bj2
    show 3bj2 bree sasha both sashaclosed breeclosed
    "Again, they lick up my shaft, up over the glans and over the tip."
    "Their tongues touch, and they both stare up at me, a chuckled shared between the two of them before they wrap their lips around the head."
    "The two best roomates in the world make out with my cock in the middle of it all, their tongues dancing over my skin as their hands move in sync to jerk me off."
    "What did I do to deserve the greatest roomates in the world?"
    "I wonder this as the excitement of their actions tingles up through my body."
    hide 3bj2
    show 3bj2 bree sasha cumshot
    "I can't hold back and, with a groan, I release, shooting up onto them."
    "Cum sprays up onto their faces, getting them nice and covered by my birthday jizz."
    hide 3bj2
    show 3bj2 bree sasha breefacial sashafacial
    "The girls smile up at me, batting their half-lidded eyes up in my direction."
    sasha.say "Enjoy this view, birthday boy,"
    "Sasha takes a finger and slips a drop of my cum off of her face."
    "She hands it to Bree, who wraps her lips around my cock, moaning quietly in delight at the taste."
    bree.say "Alright [hero.name], um, I've got another surprise for you now."
    hide 3bj2
    show bree naked at right
    show sasha naked at left
    hero.say "Something else?"
    bree.say "Yeah..."
    bree.say "The Cake!"
    hide bree
    hide sasha
    return

label hanna_event_01:
    $ game.set_flag("hannastart",1)
    "While I’m working on my set, I have the strangest notion that I’m being watched."
    "I glance around the gym, watching as others workout without paying attention to anyone else in the facility."
    "After all, it’s only polite to keep to yourself when you’re working out."
    "What kind of weirdo would just be watching people instead of working out."
    "But that’s when my eyes catch them."
    show hanna teaser treadmill
    "Hotpants."
    "Running on the treadmill."
    "How can a girl wear such tight, short shorts and still be able to run."
    "I may have not found the one checking me out, but I have stopped all things to check her out."
    "A sports bra, too? This girl is practically wearing nothing while out in public."
    "Is it possible she wants people to see her dressed like this? I know she’s distracting me."
    "I feel light-headed as the blood rushes down from my face to regions further south."
    "Shit, I need to make sure no one notices the tent in my shorts, but-"
    show hanna teaser sweaty
    "She turns her head, her large gray green eye catching mine a moment."
    "Her short blond hair practically blinds me as it reflects off of the light of the room, but I keep my glance upon her."
    "She smiles and waves. First contact, yes! Over her sun-kissed skin, I can still see the blush that forms as she sees me."
    "As on reflex, she wipes the sweat from her brow, but a moment later, she looks down over her sweaty, hardly-dressed body, her deep red blush covering all of her face before she finally stops her machine and jobs back to the locker rooms, disappearing."
    hide hanna
    "Who is that girl...?"
    "She’s not bad looking at all, but... can someone who wears something like THAT be so shy?"
    "Or, is she hiding something?"
    "Will it be a good idea to try to find out, I wonder as I finish up my set and take a swig of my water."
    "Maybe, just maybe..."
    if not "hanna" in GIRLS:
        show screen message(title="Teaser",what="Hanna is only a teaser right now, she will be fully added to the game later on.")
        pause
        hide screen message
    return

label samantha_event_01:
    $ game.set_flag("samanthastart",1)
    samantha_say "..."
    samantha_say "Oh my gosh! Hey old roomie!"
    show samantha teaser happy
    "I turn to see Samantha rushing up to me, a sweet smile on her face."
    "A touch of bitterness rises in me at the sight of her, but I suddenly feel bad- I couldn’t be mad at her."
    "After all, I’d found my roommates pretty quickly, so I suppose everything was alright."
    hero.say "Hey, Sam."
    "She’s carrying a steaming cup of coffee, which I can only assume is filled to the brim with sugar."
    show samantha teaser normal
    samantha_say "It’s good to see you! I’m sorry I didn’t get to say goodbye when we moved out."
    hero.say "Oh, well..."
    menu:
        "It’s alright, I understand.":
            hero.say "If I know Ryan, he probably popped the question on you out of nowhere. I get it."
            samantha_say "Thanks. You always know what to say, don’t you?"
            if "samantha" in GIRLS:
                $ samantha.love += 1
        "You should really tell me before you run off next time.":
            hero.say "You really had me panicking there for a minute. I wish you would have talked to me first."
            samantha_say "... I’m sorry. You’re right."
    samantha_say "Anyway~"
    if game.hour < 12:
        samantha_say "What are you doing out so early? Last I checked, you loved your sleep."
        hero.say "My roommates wake up pretty early, so I might as well be useful to society too."
        "I can see Samantha’s scepticism at my words, but I would never admit my newfound... enthusiasm for my roommates."
    else:
        samantha_say "Where are you headed at this time of day?"
        hero.say "Just looking for something to do I guess- it was lucky I ran into you!"
    hero.say "So, how’s that whole thing going? Did you guys find a nice apartment?"
    show samantha teaser normal
    samantha_say "Oh yeah! It’s a lot smaller than the house, but really cozy. Ryan can be so romantic sometimes."
    "I could see the hearts rise in Samantha’s eyes. Pushing down the urge to roll my eyes at their fluffy relationship, I couldn’t help but admire her passion and commitment."
    "Still, I desperately try to move the conversation before she can start talking nonstop about her boyfriend."
    hero.say "You’re still moving in, right? You left a few things back at our old place. You should come get them before Sasha and Bree end up finding them."
    show samantha teaser happy
    samantha_say "Sasha and Bree? You got two girls! Ryan didn’t tell me that part about the replacements."
    "She raises her eyebrows at me suggestively with a spark of playfulness in her eyes."
    samantha_say "You can finally get a girlfriend!"
    "I groan."
    hero.say "Don’t say that! They're just there to help me pay for rent."
    samantha_say "Aw, don’t deny it! I know there’s love hiding somewhere in that heart of yours."
    "The eye roll finally comes. Even though I knew she was teasing me, I couldn’t help but feel a little irritated. Samantha suddenly elbows me."
    show samantha teaser normal
    samantha_say "C’mon, you know I’m just kidding. Even though it wouldn’t hurt to get out there."
    "Samantha giggles, but I choose to ignore that last part. Finally, the conversation dies down a little."
    menu:
        "Ask about university":
            hero.say "How’s uni going for you?"
            samantha_say "It’s alright. I should really find a tutor for some of it though."
            hero.say "I can always help you with some of that."
            samantha_say "Oh, that’s okay. Ryan said he would study with me soon!"
            hero.say "..."
            hero.say "That’s good."
            "Samantha smiles and squints at me with warm eyes."
            samantha_say "You remember my major, right?"
            hero.say "Um..."
            menu:
                "Literature":
                    hero.say "You want to write books."
                    samantha_say "Yeah! Thanks for remembering."
                    if "samantha" in GIRLS:
                        $ samantha.love += 1
                "Nursing":
                    "I could tell by the look on her face that I was wrong."
                    samantha_say "Nope! You know I’ve always wanted to write children’s books. English literature!"
                    hero.say "Oops..."
                "Education":
                    samantha_say "Haha! I love kids, but not that much. I’d rather make stories for them- English literature!"
        "Ask about work":
            hero.say "Is the bakery far from your new apartment?"
            samantha_say "It’s not too bad. I can still walk there!"
            hero.say "That’s good, at least."
            samantha_say "I could be across town and still get there! Anything is worth those tasty discounts."
            "Ever since Samantha told me about her job at the bakery, I knew the only reason she went there was for the neverending sweets."
        "Ask about Ryan":
            show samantha teaser happy
            samantha_say "Ryan!"
            "Her face lit up when I mentioned her boyfriend’s name. She clasped her hands together in adoration."
            samantha_say "I still can’t believe we’re living alone now. It’s like all my dreams are coming true so fast!"
            hero.say "At least you’re happy."
            samantha_say "Aw, thanks. You should find happiness too, you know! When you find a sweet girl of your own and settle down, maybe we can trade some stories and advice!"
            hero.say "Trade stories? It feels like I already know everything about your boyfriend just from talking to you all the time."
            samantha_say "Well, we can do something else then. You know I can’t help it!"
    "Samantha abruptly perks up and I hear her cell phone ring. She took it out from her back pocket and keenly put it to her ear."
    samantha_say "Hey, Ryan!"
    "I hold back a groan. Everything would be about Ryan now- not that it wasn’t before, but it seemed to be weighing down on me even more than usual in this moment."
    samantha_say "Yeah, of course I did!"
    samantha_say "I’ll be over as soon as I can!"
    samantha_say "Alright, love you too. See you in a bit!"
    "She pressed one of the bright buttons on her phone screen and waved it around with excitement."
    show samantha teaser normal
    samantha_say "I’m sorry! I have to go; Ryan’s taking me out!"
    "I chuckle with no real emotion behind my tone."
    hero.say "Ryan always takes you out."
    samantha_say "I know! Isn’t he a sweetheart?"
    menu:
        "Have fun.":
            samantha_say "Thanks! We definitely will. Make sure you find something to do today! I don’t wanna come back and find you still wandering around!"
            hero.say "I’m not wandering!"
            "Samantha giggles, but turns to leave, waving back at me with a look of fondness in her deep blue eyes."
            "I give a single wave back and watch as she skips away to get ready for her date."
            if "samantha" in GIRLS:
                $ samantha.love += 1
        "Make sure you come to pick up your stuff.":
            samantha_say "I will, I will! Stop worrying about it, I promise I’ll get to it by the end of the week."
            "Before I can say anything else, she’s already checking her phone as it buzzes with life."
            samantha_say "Sorry, but I’ve really gotta go! I don’t want to miss anything! See you later!"
            "With that, she turned and sped her way back to her new house to meet her boyfriend."
    if not "samantha" in GIRLS:
        show screen message(title="Patreon Edition",what="Samantha is only available in the Patreon Edition of the game.\nVisit {a=https://www.patreon.com/Andrealphus}patreon.com/Andrealphus{/a} to become a patron and get to know her better.")
        pause
        hide screen message
    hide samantha
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
