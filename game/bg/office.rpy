layeredimage bg office:
    if game.hour >= 20 or game.hour <= 5:
        "office_night"
    else:
        "office_day"

layeredimage bg breakroom:
    always:
        "breakroom"

init -1 python:
    Room(**{
        "name":"office",
        "hours": (8,20),
        "display_name": "Office",
        "exits": ["map", "personal", "alettaoffice"],
        "alternate_exits": ["map", "personal", "alettaoffice"],
        "days": "123456",
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"work"
        })

    Activity(**{
        "name": "work",
        "money_gain": (["charm","knowledge"],(1,)),
        "duration": 4,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"flag_promoted":False,"room":["office"], "flag_suspended":False},
        "display_name": "Work",
        "icon":"work",
        "label": ["work"],
        "say": [
            "All work and no play makes [hero.name] a dull boy."
            ]
        })

    Activity(**{
        "name": "workhard",
        "money_gain": (["charm","knowledge"],(2,)),
        "fun":-2,
        "duration": 4,
        "game_conditions": {"min_energy":4,"min_hunger":4,"min_grooming":4,"min_fun":4,"flag_promoted":False,"room":["office"], "flag_suspended":False},
        "display_name": "Work hard",
        "label": ["workhard"],
        "icon":"work_hard",
        "say": [
            "All work and no play makes [hero.name] a dull boy."
            ]
        })

    Activity(**{
        "name": "coffee_break",
        "fun": 1,
        "energy": 1,
        "duration": 0,
        "game_conditions": {"min_energy":0,"min_hunger":0,"min_grooming":0,"min_fun":0, "flag_hasworked":True,"room":["office","personal"], "flag_coffee":False, "flag_suspended":False},
        "display_name": "Take a break",
        "icon":"coffee",
        "label": ["coffee_break"],
        "once_day": True
        })

    Event(**{
        "name":"work_random_events",
        "label": ["work_random_events"],
        "duration": 0,
        "priority": 0,
        "game_conditions": {
            "activity":["work","workhard","work_personal","workhard_personal"],
            "chances":20,
            },
        "do_once": False,
        "once_week": True,
        "quit": True
        })

    Event(**{
        "name":"work_promoted",
        "label": ["work_promoted"],
        "duration": 0,
        "game_conditions": {
            "activity":["work","workhard","work_personal","workhard_personal"],
            "flagmin_worksatisfaction":50,
            },
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name":"work_promoted_2",
        "label": ["work_promoted_2"],
        "duration": 0,
        "game_conditions": {
            "activity":["work","workhard","work_personal","workhard_personal"],
            "flagmin_worksatisfaction":100,
            },
        "do_once": False,
        "once_week": False,
        "quit": True
        })

label work_promoted:
    show aletta teaser
    aletta_say "[hero.name], the management has decided to give you a promotion."
    hero.say "Thanks, I am grateful."
    aletta_say "Don't be, it comes with greater responsibilities and higher expectations, welcome to management."
    aletta_say "As a consequence, you will have your own office from now on."
    $ HIDDEN.remove("personal")
    $ game.set_flag("promoted", 4)
    $ game.set_flag("worksatisfaction", game.get_flag_value("worksatisfaction")-50)
    hide aletta
    return

label work_promoted_2:
    "My salary has been raised !"
    $ game.set_flag("promoted", 1, mod="+")
    $ game.set_flag("worksatisfaction", game.get_flag_value("worksatisfaction")-100)
    return

label work_random_events:
    $ r = randint(1,13)
    if r == 1:
        show aletta teaser
        "Aletta walks toward me."
        aletta_say "[hero.name], we have to finish this by tomorrow, I want you to stay for more two hours."
        aletta_say "Of course you will have a bonus."
        menu:
            "Accept":
                hero.say "Ok, no problem boss."
                "I work for two more hours."
                $ game.pass_time(2, needs = True)
                aletta_say "Well done [hero.name], we finished just in time."
                $ game.set_flag("worksatisfaction",5,mod="+")
                if "work" in hero.skills:
                    $ game.set_flag("worksatisfaction",5,mod="+")
                $ hero.money += 50
            "refuse":
                hero.say "Sorry boss, I have plans."
        hide aletta
    elif r == 2:
        show aletta teaser
        "Aletta walks toward my desk."
        aletta_say "[hero.name], we have an emergency we have to correct this bug as soon as possible."
        aletta_say "I want you to stay until you solve it."
        aletta_say "Of course you will have a bonus."
        if hero.knowledge < 25:
            menu:
                "Accept":
                    hero.say "Ok, no problem."
                    "I work for two more hours."
                    $ game.pass_time(2, needs = True)
                    aletta_say "Well done [hero.name], we finished just in time."
                    $ game.set_flag("worksatisfaction",5,mod="+")
                    if "work" in hero.skills:
                        $ game.set_flag("worksatisfaction",5,mod="+")
                    $ hero.money += 100
                "Refuse":
                    hero.say "Sorry boss, I have plans."
                    $ game.set_flag("worksatisfaction",1,mod="-")
        else:
            hero.say "I already solved it boss."
            aletta_say "Wow, as impressive as ever [hero.name]."
            $ hero.money += 100
            $ game.set_flag("worksatisfaction",10,mod="+")
            if "work" in hero.skills:
                $ game.set_flag("worksatisfaction",10,mod="+")
        hide aletta
    elif r == 3:
        show audrey teaser
        "Audrey comes to my desk with an apologetic look on her face."
        audrey_say "I messed up big time."
        audrey_say "I erased all the data and I can't find the backup, could you help me?"
        menu:
            "Accept":
                hero.say "Ok, no problem."
                "I work for 2 hours, trying to clean Audrey's mess."
                $ game.pass_time(2, needs = True)
                audrey_say "Thanks, you saved my life."
                if "audrey" in GIRLS:
                    $ audrey.love += 1
            "Refuse":
                hero.say "Sorry Audrey, I don't have time."
        hide audrey
    elif r == 4:
        "My attention's focused on my computer screen as the phone on the desk rings."
        "I fumble for it and try to hold it to my ear with my shoulder as continue to type."
        hero.say "Hello, [hero.name] here?"
        man_say "Yeah, this is the IT department - we've got reports that someone's been downloading porn on the desktop in your office."
        "Oh shit, I can already feel my arsehole puckering up in fear!"
        menu:
            "Admit it":
                hero.say "Erm...yeah...that might have been me."
                hero.say "I was an honest mistake...I can explain..."
                man_say "Hey, man - my job is to deal with the facts, not the shades of grey!"
                man_say "Look out for it being brought up in your next quarterly review, okay?"
                $ game.set_flag("worksatisfaction",1,mod="-")
            "Deny it":
                hero.say "Geez, I wouldn't know anything about that!"
                man_say "Really...well, in that case, does anyone else have access to your desktop?"
                hero.say "Erm...yeah - a member of my team called Shiori uses it quite a lot."
                man_say "Hmm...okay, you should warn her to look out for it being brought up at her next quarterly review, yeah?"
                $ game.set_flag("worksatisfaction",2,mod="-")
        hero.say "Yeah...sure."
        "I put the phone down slowly, vowing to myself that I'll never look at porn in the office again."
        "Or at least until I can figure out a means of getting away with it..."
    elif r == 5:
        "It's getting pretty close to lunchtime, and I can already hear my stomach growling in anticipation."
        "But the only problem is that I'm way too busy to leave my desk and go out to grab something to eat."
        "Even worse, I can't see anyone else around right now that'd nip out and pick me up some lunch either."
        "Desperate to find something edible, I hurry over to the break room and start rooting around in the fridge."
        "It's then that I see a pretty nice-looking sandwich jammed in there alongside the milk."
        "Home-made and stuffed with the kind of fillings that I'd never even have in at my house, I'm instantly tempted..."
        menu:
            "Eat the sandwich":
                "There might have been a note pinned to the cellophane the sandwich is wrapped in declaring it someone's property."
                "But I can't see one anywhere on it, or even on the shelf that it's sitting on."
                "Trying to ignore the guilt I'm feeling right now, I grab the sandwich and skulk back to my desk."
                "Eat the whole thing as fast as I can, almost giving myself indigestion in the process."
                $ hero.hunger += 10
                $ game.set_flag("worksatisfaction",1,mod="-")
            "Don't eat the sandwich":
                "I want to eat the thing, really I do."
                "But what happens when its true owner finds out and goes on the hunt for his missing sandwich?"
                "Who's going to look more suspicious than the guy who was ravenous five minutes ago, but swears he's fine right now?"
                "I walk back to my desk, resigning myself as I do so to an afternoon of hunger pangs and a grumbling stomach."
    elif r == 6:
        "I swear that I had no idea that it was about to happen, even as I was waiting for the lift and then stepping into it."
        "Now I'm trapped in here, cheek by jowl with more than a dozen other people that work in the same building as me."
        "I feel like everyone's deliberately pressing against me, that if they just gave me space, I could keep a lid on things."
        "But then, between floors, there's the inevitable sound, like an balloon's drawn out death-rattle."
        "Oh god - why doesn't it end?"
        "And why does it smell like a burning tyre?"
        "I honestly haven't eaten Mexican or Indian food in weeks!"
        "People are covering their noses now, muttering and mumbling in disgust."
        menu:
            "Admit it":
                "I don't know why I feel compelled to confess to being the one that dealt it."
                "I just feel like any moment someone will finger me as the culprit anyway."
                hero.say "I...I'm sorry..."
                "I get a round of harsh stares and hard looks as people get out at the next floor."
                "How am I ever going to live this down?!?"
                python:
                    for g in ["aletta","audrey","lavish","shiori"]:
                        if g in GIRLS and not g in HIDDEN:
                            GIRLS[g].love -= 2
            "Keep quiet":
                "It's only a couple of floors until I get out of the lift - I just need to keep quiet."
                "All around me, people are still complaining, some even choking and making retching sounds."
                "I find myself joining in, perhaps with a little too much enthusiasm, in the hope of looking innocent."
                "As soon as the lift reaches my floor, I pile out and take a deep, exquisite breath of pure air."
                $ hero.fun -= 5
    elif r == 7:
        "The last thing that I need to have happen, even on an average day at work, is my computer screwing up."
        "It's not that I dread being unable to work on the thing, more that I loathe having to call the IT department to get it fixed."
        "Picking up the phone, I grit my teeth and prepare to hear the disagreeable tones on the other end."
        man_say "Hello, IT department."
        hero.say "Yeah, hi - listen, my computer's playing up..."
        man_say "Urrggh...have you tried turning it off and on again?"
        "Here we go again!"
        if hero.charm >= 50:
            hero.say "Well...no, actually, I haven't."
            man_say "Then you should, as that can usually fix like ninety nine percent of problems, you know?"
            "I moderate my breathing and bite my lip at his arrogant reply."
            hero.say "Okay, thanks...I'll give that a try and call you back if it doesn't work."
        else:
            hero.say "Of course I've tried that, what kind of a moron do you think I am?"
            man_say "Erm, the kind that needs to bug me with calls to fix something an average pre-school kid could figure out?"
            hero.say "Look here, you glorified nerd - just send someone up here to fix my damn computer, okay?"
            "I can almost hear his colleagues snickering in the background."
            "Has he actually got me on speaker-phone for them to listen in?"
            man_say "Take a pill, man - I'll send someone up, as soon as we can spare them..."
            $ game.set_flag("worksatisfaction",1,mod="-")
    elif r == 8:
        "While I'm not sitting on the board of directors at work, I'm not exactly the bottom of the heap either."
        "That means I'm not usually the person in the office that ends up doing the really shitty jobs, like photocopying and shredding."
        "Unless, that is, almost everyone happens to be on annual leave, off sick or for whatever reason just isn't around when it needs doing."
        "And right now, I'm all alone here, looking like I've tried to make a fort out of the stacks of paper on my desk that should already have been shredded."
        "There's no point putting it off any longer, so I grab as much as I can carry and make for the shredder."
        "I shove the first load in and start the machine."
        "But then I feel something suddenly pulling me down towards the razor-sharp blades below."
        "Shit, my tie's caught in there - why couldn't I have waited until dress-down day!"
        if hero.knowledge <= 50:
            "Grabbing desperately at what's left of my tie, I brace myself against the shredder and pull with all my might."
            "It's touch and go for a while, and I can see the whirring blades getting ever closer."
            "But then the adrenaline finally kicks in and I somehow find the strength to pull so hard that I hear something strain and then break inside the machine."
            "Mercifully it grinds to a stop, leaving me alive, but also needing to explain how I just managed to break an expensive office appliance thanks to my own stupidity."
            $ game.set_flag("worksatisfaction",1,mod="-")
        else:
            "I can feel myself starting to panic, but then I suddenly recall that the power switch for the shredder is at chest level for just this very reason."
            "Flailing a hand out towards the wall, I manage to flip the switch off just as I feel myself being dragged downwards."
            "The shredder grinds to a halt, and I can finally breathe a sigh of relief as I reach out to grab a nearby pair of scissors."
            "Snipping the remains of my tie in order to free myself, I reflect that I never really liked it that much anyway."
    elif r == 9:
        "I don't know how it always manages to happen, but it does, every time there's a departmental meeting to sit through."
        "It's either that I've been out and overdone it the night before, or else I've had to pull an all-nighter to get shit done for the meeting itself."
        "Either way, the day of the meeting always finds me utterly exhausted and struggling to stay awake."
        "Today's a perfect example, nothing to look forward to but hours of boring presentations and slides of info-graphics turning my brain to mush."
        "Luckily, I've managed to bag a seat where no one can really see me that well, and I can already feel my head starting to droop forwards."
        "I'm going to have to fight hard if I want to stay awake."
        if hero.fitness <= 50:
            "Ah, screw it - I haven't got a presentation of my own to give and nobody can see me."
            "I make no effort to fight off the drowsiness, and soon I'm lost in a fuzzy-headed dream."
            "This goes on until I swear that I can hear someone calling my name."
            hero.say "Wha...what...what the...I am awake...I have got my pants on!"
            "I wake up to the sight of the entire room looking at me in amused horror, as people try to stifle the urge to laugh."
            $ game.set_flag("worksatisfaction",1,mod="-")
        else:
            "No, this is a matter of personal pride - I won't fall asleep in front of these people!"
            "I fight with all of my will to stay awake, almost nodding off a couple of times only to jerk back into wakefulness."
            "A couple of my colleagues in the meeting note what's happening, and I get elbowed in the ribs more than once."
            "In the end, I manage to struggle through the entire meeting, even getting a little round of applause at the end."
            "It seems my efforts were appreciated by someone, even if it wasn't me."
    elif r == 10:
        "I don't normally snack between meals, it's a bad habit to get into and it really screws with your diet in the long-run."
        "But today I had to run out of the house without eating breakfast, and it's hours before lunchtime."
        "I can feel my stomach growling, and it's keeping me from being able to concentrate on anything in the slightest bit work-related."
        "That's how I find myself in the corridor, desperately stuffing bills into the vending machine to get something to stuff into my face."
        "I punch the buttons for some kind of granola energy bar, thinking that it's not as shameful as chocolate or other sugary junk."
        "But then the nightmare happens - the bar drops forwards and wedges against the glass, an inch from my face."
        "It's like I'm being mocked!"
        if hero.charm >= 50:
            "I could lose my shit, but it's just a cheap granola bar and lunch really isn't that far away."
            "Taking a deep breath, I resolve to tough it out for just a little bit longer."
            "After all, I'd only have felt guilty about snaking anyway."
        else:
            "That's the last straw, really it is!"
            "In a fit of hunger-induced rage, I set to attacking the vending machine, pounding on the glass with my fists and trying to shake the granola bar loose."
            "Suddenly the alarm built into the machine to deter just such an act of primitive violence goes off, turning every head on the floor in my direction."
            "Still hungry and now thoroughly ashamed of myself, I hurry back to my desk, even the sound of the alarm not being enough to drown out the growls of my stomach."
            $ game.set_flag("worksatisfaction",1,mod="-")
    elif r == 11:
        "It's bad enough that my team had to provide cover for one of the women who works on another while she went off on maternity leave for what seemed like a decade."
        "But now she seems to want to compound the inconvenience and irritation that she caused by turning up at the office in order to show off the ultimate result of her efforts."
        "I mean, if I went around showing people the things that came out of my body and expecting to get praised for it, they'd lock me up and throw away the key!"
        "And then, of course, as soon as her bladder (which has apparently been destroyed by the pregnancy) demands her attention, she looks around for someone to hold the baby."
        "I will her to choose one of the women currently standing around and cooing, but she looks straight at me."
        if hero.charm <= 50:
            "I instantly shake my head and begin to back away from the proffered infant as though it had the plague."
            hero.say "Oh no...no, no, no...I'd be afraid of...of dropping it...that's it - I might drop your baby!"
            "The mother shrugs at my odd outburst, and mercifully moves on to choose someone else instead."
            $ game.set_flag("worksatisfaction",1,mod="-")
        else:
            "What harm can holding a baby do for a couple of minutes?"
            hero.say "Okay, hand the little bugger over!"
            "The baby is more than half-asleep anyway, and does little more than stare around and wriggle until its mother comes back to claim it from me."
            "But what I do note is the number of interested glances this little act of paternal indulgence is winning me from many of the other women in the office right now."
    elif r == 12:
        "I'm not proud to have to confess this, but I've gotten into the habit of waiting until I get to work on a morning to visit the bathroom for a sit down - if you know what I mean."
        "It dates back to being a student and having so little money that I had to seriously think about how much toilet roll I could afford to buy every week."
        "Usually it's not a problem, but this morning I go through my usual routine and go to leave after the necessary flush."
        "But then I just happen to look back and notice that this hasn't managed to do the trick."
        "Embarrassed and beginning to panic a little, I hastily grab handfuls of toilet roll to cover up the evidence while I think of what to do."
        menu:
            "Walk away":
                "I know what happens when something like that refuses to take the hint after one flush."
                "Repeating the same course of action won't shift it, and more drastic measures need to be taken."
                "And that's not something that I'm prepared to even contemplate at my place of work."
                "So I duck out of the bathroom as quickly and casually as I can possibly manage."
            "Flush it again":
                "As soon as I hear the sound of the cistern refilling come to a cease, I begin to hammer away at the flush once again."
                "But in the meantime, I've been stuffing so much toilet roll down there that it immediately causes a blockage."
                "As the bowl begins to overflow and water spreads across the tiled floor, I flee the scene of the crime."
                "All I can do is slink back to my desk, hoping that no one can link me to the monster currently flooding the bathroom."
                python:
                    for g in ["aletta","audrey","lavish","shiori"]:
                        if g in GIRLS and not g in HIDDEN:
                            GIRLS[g].love -= 2
    elif r == 13:
        "I don't usually make a habit of getting dressed in the dark, but today I overslept and was in such a hurry to get out of the house that I did just that."
        "Nothing seems out of place at first, but as I'm waiting for the lift in the lobby, I can hear people beginning to laugh as they walk past and glance down."
        "This starts a snowballing of the attention I'm getting, until everyone seems to be staring at my feet and trying to suppress their amusement at what they're seeing."
        "I look down and find myself stunned and horrified to see that I'm wearing odd shoes - not just that, but one has laces and the other is a slip-on!"
        menu:
            "Bear with it":
                "I step into the lift, trying to ignore the laughter around me and focus on the day ahead."


                $ hero.fun -= 5
            "Removes your shoes":
                "I make an immediate dash for the nearest bathroom, running into a cubicle and pulling off my odd shoes."
                "The rest of the day I spend walking here and there in nothing but my socks."
                "Which attracts some odd looks too, but is infinitely preferable to the ones I was getting beforehand."
    return

label coffee_break:
    scene bg breakroom
    python:
        coffee_girls = []
        for g in ['aletta', 'audrey', 'lavish', 'shiori', 'cassidy']:
            if GIRLS.get(g) and g not in HIDDEN and GIRLS[g].room in ["office", "personal", "breakroom", "alettaoffice"]:
                coffee_girls.append(g)
    if coffee_girls and hero.charm >= 20:
        $ g = randchoice(coffee_girls)
        show expression g+" teaser"
        call expression GIRLS[g].get_chat() from _call_expression_52
        hide expression g+" teaser"
    else:
        "I take a coffee break..."
    $ game.set_flag("coffee",True,"day")
    hide bg
    return

label work:
    if game.get_flag_value('suspended'):
        return
    $ r = randint(1,3)
    menu:
        "Chat with Shiori" if r == 1 and "shiori" in GIRLS and "shiori" not in HIDDEN:
            show shiori work
            call expression shiori.get_chat() from _call_expression_76
            hide shiori
        "Chat with Aletta" if r == 2 and "aletta" in GIRLS:
            show aletta work
            call expression aletta.get_chat() from _call_expression_77
            hide aletta
        "Chat with Audrey" if r == 3 and "audrey" in GIRLS:
            show audrey work
            call expression audrey.get_chat() from _call_expression_78
            hide audrey
        "Slack off":
            if randint(1,2) == 1:
                "Nobody notices that I slack off"
                $ hero.fun += 2
                if "work" in hero.skills:
                    $ game.set_flag("worksatisfaction",1,mod="+")
                $ game.set_flag("worksatisfaction",1,mod="+")
            else:
                show aletta teaser
                aletta_say "You think I don't see you slacking off [hero.name]."
                $ game.set_flag("worksatisfaction",1,mod="-")
                hide aletta
        "Work normally":
            hero.say "I work a little."
            if "work" in hero.skills:
                $ game.set_flag("worksatisfaction",1,mod="+")
            $ game.set_flag("worksatisfaction",1,mod="+")
    $ game.set_flag("hasworked",True,"day")
    return

label workhard:
    if game.get_flag_value('suspended'):
        return

    $ r = randint(1,3)
    menu:
        "Chat with Shiori" if r == 1 and "shiori" in GIRLS and "shiori" not in HIDDEN:
            show shiori work
            call expression shiori.get_chat() from _call_expression_79
            hide shiori
        "Chat with Aletta" if r == 2 and "aletta" in GIRLS:
            show aletta work
            call expression aletta.get_chat() from _call_expression_80
            hide aletta
        "Chat with Audrey" if r == 3 and "audrey" in GIRLS:
            show audrey work
            call expression audrey.get_chat() from _call_expression_81
            hide audrey
        "Work fast":
            if randint(1,2) == 1:
                "I manage to do twice the amount of work !"
                $ game.set_flag("worksatisfaction",4,mod="+")
                if "work" in hero.skills:
                    $ game.set_flag("worksatisfaction",4,mod="+")
            else:
                show aletta teaser
                aletta_say "What are you doing [hero.name], you made so many mistakes we have to start over..."
                $ game.set_flag("worksatisfaction",2,mod="-")
                if "work" in hero.skills:
                    $ game.set_flag("worksatisfaction",2,mod="+")
                hide aletta
        "Work normally":
            hero.say "I work a little."
            $ game.set_flag("worksatisfaction",2,mod="+")
    $ game.set_flag("hasworked",True,"day")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
