init -1 python:
    Event(**{
        "name":"cassidy_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "cassidy",
        "girls_conditions": {"cassidy":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"cassidy_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "cassidy",
        "girls_conditions": {"cassidy":{"contact":"cassidy","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(12,13),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"cassidy_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "cassidy",
        "priority":100,
        "girls_conditions": {"cassidy":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"cassidy_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "cassidy",
        "priority":100,
        "girls_conditions": {"cassidy":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"cassidy_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "cassidy",
        "priority":100,
        "girls_conditions": {"cassidy":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_cassidy_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"cassidy_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "cassidy",
        "priority":100,
        "girls_conditions": {"cassidy":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"cassidy_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "cassidy",
        "girls_conditions": {"cassidy":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

label smartphone_cassidy_hint:
    if game.get_flag_value('underinvestigation'):
        if "cassidy_setup_meeting" in DONE and "cassidy_hold_meeting" not in DONE and not game.get_flag_value('cassidycameraplaced'):
            "I need to find a way to record my meeting with Cassidy. I should see if I can find something to use in the electronics shop."
        if game.get_flag_value('workinvestigation') < 100:
            "I need to focus on the investigation. I should talk to everyone at the office and maybe there's data on Aletta's computer."
        else:
            "I just need to wait for this investigation to be complete now."
        return
    if "cassidy_bad_day" in DONE and "cassidy_overhear_argument" not in DONE:
        "You need a coffee break."
    elif "cassidy_new_assistant" in DONE and "cassidy_aletta_fight" not in DONE:
        "Spend time with Cassidy in the office."
    elif "cassidy_new_assistant" in DONE and "cassidy_needs_comfort" not in DONE:
        "Wait for Cassidy to return."
    else:
        "Cassidy's story will continue in a future release."
    return

label cassidy_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = cassidy.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = cassidy.get_activity(bye_hour)
    if not activity == cassidy.activity:
        if day != game.week_day:
            $ cassidy.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ cassidy.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "cassidy "+bye_outfit
        if activity["activity"] == "sleep":
            cassidy.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            cassidy.say "I have to go to the bathroom, don't you dare peek!"
        elif activity["activity"] in ["meal"]:
            cassidy.say "I am so hungry..."
        elif activity["activity"] in ["watch"]:
            cassidy.say "I think I'm going to go catch a movie."
        elif activity["activity"] in ["drink"]:
            cassidy.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            cassidy.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            cassidy.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            cassidy.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            cassidy.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            cassidy.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            cassidy.say "I ll go get dressed."
        hide expression "cassidy "+bye_outfit
    return

label cassidy_cheated:
    show cassidy
    if cassidy.get_status() == 'pet':
        if cassidy.love > 120 and cassidy.sub < 75:
            "Cassidy stares at me hard, but I can't tell if she's angry or intrigued. Maybe both."
            $ cassidy.sub += 1
            $ cassidy.love -= 1
    else:

        "Cassidy gives me an angry look and mouths the words \"You're going to regret that\" at me."
        $ cassidy.love -= 5
    hide cassidy
    return

label cassidy_greet:
    if not cassidy.get_flag_value("greeted"):
        $ cassidy.set_flag("greeted",True,1)
        show cassidy
        if cassidy.get_status() == 'pet':
            if cassidy.love < 120:
                cassidy.say "Hi, [hero.name]."
                hero.say "Hello, my pet!"
            else:
                cassidy.say "Hello, my master!"
                hero.say "My sweet pet!"
        elif cassidy.get_status() == 'mistress':
            cassidy.say "Hello, [cassidy.heroname]!"
            hero.say "Hello, Mistress."
        else:
            $ result = randint (1,3)
            if result == 1:
                cassidy.say "Hello, [hero.name]."
            elif result == 2:
                cassidy.say "Hi, I guess, [hero.name]."
            else:
                cassidy.say "Oh, it's you, [hero.name]."
            $ result = randint (1,3)
            if result == 1:
                hero.say "Hello, Cassidy."
            elif result == 2:
                hero.say "Hi."
            else:
                if game.hour < 6:
                    cassidy.say "Hello [hero.name]."
                elif game.hour < 12:
                    hero.say "Good morning Cassidy."
                elif game.hour < 19:
                    hero.say "Good afternoon Cassidy."
                else:
                    hero.say "Good evening Cassidy."
    return

label cassidy_kiss:
    scene expression "bg "+game.room

    if cassidy.get_flag_value('nokiss'):
        if cassidy.get_status() == 'mistress':
            show cassidy angry
            "Cassidy lightly slaps me across the cheek and pushes me away."
            $ cassidy.sub -= 1
            cassidy.say "Did I say you could try to kiss me, [cassidy.heroname]?"
            hero.say "Sorry, Mistress."
        else:
            show cassidy
            "Cassidy quickly takes a step back and turns away."
            cassidy.say "Who do you think you are?!"
            $ cassidy.love -= 1
        hide cassidy
        return
    if cassidy.get_status() == 'mistress':
        if not cassidy.get_flag_value("kiss"):
            "I step up to Cassidy, slightly afraid she's going to push me away."
            "But she doesn't; instead she stands there passively while I embrace her."
            "When I try to kiss her, though, she pulls her head back, away from me. She puts one finger against my lips."
            call cassidy_kiss_dom from _cassidy_kiss_dom
        else:
            "When I try to kiss her, she pulls her head back, away from me. She puts one finger against my lips."
            call cassidy_kiss_dom from _cassidy_kiss_dom_2
    else:
        hide cassidy
        show expression "cassidy kiss "+cassidy.get_clothes()
        if cassidy.love > 120:
            "I step up to Cassidy and pull her into my arms."
            "She doesn't resist, allowing me to pull her against the length of my body."
            "Her lips open when mine touch hers, allowing my tongue into her mouth to tease and explore."
            hide cassidy kiss
            "After a moment the kiss ends, and I step back. She gives me a soft, happy smile."
        else:
            "I step up to Cassidy and pull her into my arms."
            "She seems stiff and mildly resistant, so I am firm with her, and she complies."
            "Her lips open when mine touch hers, allowing my tongue into her mouth to tease and explore."
            hide cassidy kiss
            "After a moment the kiss ends, and I step back. She looks at me with some amount of discomfort."
            "She clearly enjoyed it, but I think she needs more encouragement."
    call kiss_check_cheat from _cassidy_kiss_sub
    $ cassidy.set_flag("kiss",1,"permanent","+")
    $ cassidy.love += 1
    hide cassidy
    return

label cassidy_kiss_dom:
    if cassidy.sub > -75:
        cassidy.say "Have you been a good boy lately?"
        hero.say "I suppose...I could be better, Mistress?"
        cassidy.say "That's right. Are you going to be better?"
        hero.say "Yes, Mistress. I'll be a better boy."
        $ cassidy.sub -= 1
    else:
        cassidy.say "Who's been a good boy. You have! You've been a very good boy."
        hero.say "Yes, Mistress."
    hide cassidy
    show expression "cassidy kiss "+cassidy.get_clothes()
    "Then she relaxes. Her arms wrap around my neck, pulling me close."
    "Our lips touch, and we drink hungrily from each other. Her grip around my neck is so tight it almost hurts, and I return the gesture."
    "My arms, wrapped around her, pull her as tightly to me as I can. I feel her ample breasts smashed against my chest."
    "Her hips press against mine."
    hide cassidy kiss
    "And then it's over. She steps back and gives me a wry smile, followed by a wink."
    return

label cassidy_ask_fuck_date:
    if game.get_flag_value("datescore") >= (100 - cassidy.get_flag_value("drinks")*5):
        if cassidy.get_status() == 'mistress':
            cassidy.say "This is the part where you take me home and please me all night long, [cassidy.heroname]."
            hero.say "I don't know..."
            cassidy.say "Did you have fun?"
            hero.say "Yeah, I guess I did."
            "She takes ahold of my hand and gives it a squeeze."
            if cassidy.love > 120:
                cassidy.say "Don't worry, Sweetie, I'll make sure you have fun too. This won't be {b}just{/b} about me. Only mostly."
                "I look at her and she smiles at me with genuine affection."
                hero.say "Okay."
            else:
                cassidy.say "I promise it'll feel good. I'm pretty good at this, you know, and no one has ever complained when I was done with them."
                "I have to laugh at that."
                hero.say "Fine, then. It might be the one perk of this arrangment is getting to fuck you."
        else:
            hero.say "Come home with me, my pet."
            if cassidy.love < 120:
                cassidy.say "Do I have to?"
                menu:
                    "You do not have a choice":
                        hero.say "You do not have a choice. You are coming home with me."
                        $ cassidy.love -= 5
                        $ cassidy.sub -= 1
                        "Cassidy looks down at the ground and nods."
                        cassidy.say "Yes, Master."
                    "Only if you want to":
                        hero.say "Look, I like what we have, but if you really don't want to, I guess you can go home."
                        $ cassidy.love += 5
                        $ cassidy.sub += 1
                        cassidy.say "Thank you, Master."
                        hero.say "But if you do, I think you'll have fun."
                        cassidy.say "I guess I had a good time tonight. Okay, I'll go."
            else:
                cassidy.say "Take me home, Master, and ravish me!"
                hero.say "Gladly!"
        return True
    else:
        if cassidy.get_status() == 'mistress':
            cassidy.say "You know, [cassidy.heroname], I was looking forward to a good shag tonight, but you were really kind of dull, so I think I'm going to go home and masturbate, instead."
            cassidy.say "Do better, next time. Don't make me punish you."
        else:
            hero.say "Come home with me, my pet."
            cassidy.say "That date was not great. Do I really have to?"
            menu:
                "You do not have a choice":
                    hero.say "You do not have a choice. You are coming home with me."
                    $ cassidy.love -= 20
                    $ cassidy.sub -= 5
                    "Cassidy looks down at the ground and nods."
                    cassidy.say "Yes, Master, if I must."
                    return True
                "Only if you want to":
                    hero.say "Look, I like what we have, but if you really don't want to, I guess you can go home."
                    $ cassidy.love += 5
                    $ cassidy.sub += 1
                    cassidy.say "Thank you, Master."
                    hero.say "But if you do, I think you'll have fun."
                    cassidy.say "I...please, can I go home? I don't feel good. I promise I'll be good next time."
                    hero.say "Okay, Cassidy. This time."
                    cassidy.say "Thank you, Master. I won't forget it!"
        return False

label cassidy_fuck_date:
    if cassidy.get_status() == 'mistress':
        call cassidy_fuck_date_dom
    else:
        call cassidy_fuck_date_sub
    return

label cassidy_fuck_date_sub:

    $ cassidy.set_flag('sex', 1, mod='+')
    "I take Cassidy's hand and we meander back to my house. I'm not in any hurry."
    scene bg bedroom1
    show cassidy
    "We get to the house and wordlessly, I take Cassidy down into my bedroom. She looks around without much interest at my stuff."
    "This can't be anything like what she's used to. She's got the best of everything, and I've got...well, it's my place and I like it."
    if cassidy.love < 120:
        cassidy.say "What would you like me to do?"
    else:
        show cassidy happy
        cassidy.say "How may I serve you, Master?"
    hero.say "You can start, my sexy slave, by taking off that your clothes and showing me your incredibly sexy body."
    if cassidy.love < 120 or cassidy.sub < 75:
        "Without any ceremony, she slips quickly and efficiently out of her clothes, leaving them on the floor."
        show cassidy naked
    else:
        "She smiles at me and works slowly, slipping her top off just enough that I can see her breasts sticking out."
        "She cups her hands beneath them and shows them off."
        show cassidy naked happy
        cassidy.say "Do you like what you see?"
        hero.say "Oh fuck yeah, I do. Damn, girl, you are fine, so fine."
        $ cassidy.love += 1
    show cassidy normal
    cassidy.say "Now what?"


label cassidy_fuck_date_sub_loop:
    $ cassidy_sad = False
    menu:
        "Titty job":
            hero.say "Get down on your knees and suck my fat cock."
            if cassidy.love > 160 or cassidy.sub > 80:
                cassidy.say "Yes, Master!"
            call cassidy_tittyfuck (topless=True)
        "Slave play":
            hero.say "Lie down on my bed and spread your legs."
            if cassidy.love > 160 or cassidy.sub > 80:
                cassidy.say "Yes, Master!"
            "She does as instructed, lying on her back. I get on my knees next to her and grab her ankles to spread her legs as wide as I can."
            show cassidy miss
            hero.say "Are you comfortable, my slave"
            cassidy.say "No, I mean yes. I mean my legs hurt just a little."
            hero.say "Only a little?"
            cassidy.say "Only a little bit."
            cassidy.say "Do you want me?"
            if cassidy.love < 80:
                "She doesn't answer."
                hero.say "Cassidy, tell me you want me."
                $ cassidy.sub += 1
                "She closes her eyes."
                cassidy.say "I...want you."
                "It doesn't sound like her heart is in it."
                "I don't believe you. Tell me again, and make me believe you."
                cassidy.say "Yes, Master. I want you."
                hero.say "I want you do, my beautiful slave."
                $ cassidy.love += 1
            elif cassidy.love < 160:
                $ cassidy.sub += 1
                "She closes her eyes."
                cassidy.say "I...want you."
                "It doesn't sound like her heart is in it."
                "I don't believe you. Tell me again, and make me believe you."
                cassidy.say "Yes, Master. I want you."
                hero.say "I want you do, my beautiful slave."
                $ cassidy.love += 1
            else:
                "She answers without any hesitation."
                cassidy.say "I want you! I want you so much! I want you right now!"
                hero.say "Tell me you love me!"
                if cassidy.love < 180:
                    "She answers, but not before hesitating just for a second."
                cassidy.say "I love you, Master! I need you, Master! Fuck me now, Master!"
                $ cassidy.love += 1
                $ cassidy.sub += 2
                return
        "Fuck her":
            hero.say "Lie down on my bed and spread your legs."
            if cassidy.love > 160 or cassidy.sub > 80:
                cassidy.say "Yes, Master!"
            "She does as instructed, lying on her back. I get on my knees next to her and grab her ankles to spread her legs as wide as I can."
            show cassidy miss
    menu:
        "Fuck her pussy raw":
            if cassidy.love < 200 or cassidy.sub < 100:
                if not cassidy.get_flag_value('pill'):
                    "Cassidy's eyes get big when she realizes what I'm doing."
                    cassidy.say "No! I can't get pregnant! Please don't do this to me! I'm begging you!"
                    menu:
                        "Use a condom" if hero.has_condom():
                            call cassidy_fuck_pussy_sub (condom=True)
                        "Ignore her":
                            hero.say "No, bitch. You're going to take my cock raw and you're going to like it!"
                            call cassidy_fuck_pussy_sub (condom=False, sad=True)
                        "Fuck her ass instead":
                            call cassidy_fuck_anal_sub
                        "I don't have to fuck her" if not hero.has_condom():
                            hero.say "I don't have any condoms with me. I'll let it go this time, but only this time. If you don't want my baby you'd better go on the pill."
                            cassidy.say "Oh yes, Master, thank you Master. I'll go get the pill tomorrow!"
                            $ cassidy.set_flag('pill', True)
                            $ cassidy.love += 3
                            $ cassidy.sub += 3
                else:
                    call cassidy_fuck_pussy_sub
        "Fuck her pussy with a condom" if hero.has_condom():
            call cassidy_fuck_pussy_sub (condom=True)
        "Fuck her ass":
            call cassidy_fuck_anal_sub
    call cassidy_sleep_date_fuck_sub
    return

label cassidy_fuck_pussy_sub(condom=False, sad=False):
    $ cassidy_sad = sad
    if condom:
        $ hero.use_condom()
        show cassidy miss vaginal condom
    else:
        show cassidy miss vaginal
    if cassidy.love < 80 or sad:
        show cassidy miss pain
        "Cassidy whimpers softly as I push my cock into her pussy. There is some resistance as she isn't really wet yet."
        if not sad or cassidy.love > 150:
            show cassidy miss normal
            "It doesn't take long, however, for her juices to flow, and I am able to press deeply into her with ease."
    elif cassidy.love < 160:
        "Cassidy takes a sharp breath as I enter her, the sound of the air through her teeth almost a spasm of anticipation."
        cassidy.say "Oh! Oh my God!"
    else:
        "Cassidy moans as soon as I enter her, her cunt wet and swollen, ready for me."
        cassidy.say "Fuck me, Master! Fuck me hard!"

    "Holding her legs as far apart as I can, I slowly thrust my dick into her, going a little deeper very stroke until I can feel the tip of my head pressing against her cervix."
    if sad or cassidy.love < 100:
        "She makes little noises, a mix of pain and pleasure. She isn't particularly enjoying this, but she doesn't have to. This is what she gets for what she tried to do to me!"
    elif cassidy.love < 160:
        "She makes little noises, moans in the back of her throat that grow louder with each thrust."
        cassidy.say "Oh! Oh! Ohhhhhhh!"
        "Each moan comes in time with my thrust, the loudest sound coming while I'm deepest inside her."
    else:
        "She makes little noises, moans in the back of her throat that grow louder with each thrust."
        show cassidy miss ahegao
        cassidy.say "Oh yes! Yes, Master, that's...oh God yes!"
        "I can feel her pussy spasm repeatedly as she orgasms, and then she goes goes limp, smiling at me while I finish."
    "Just a few more thrusts and I'll be ready to blow!"
    if not condom:
        menu:
            "Pull out":
                show cassidy miss outside cum
                "Just when I can't take any more, I pull out and blow my load all over her tits and belly."
                show cassidy miss -cum bellycum
                if sad:
                    $ cassidy.love += 2
                    $ cassidy.sub += 1
                    "The relief on Cassidy's face that I didn't cum inside her is massive."
                    cassidy.say "Oh, thank you, Master, thank you so much."
                    if cassidy.sub > 80:
                        cassidy.say "I promise to be a good girl for you! I swear I will!"
            "Cum inside":
                "I can't take any more, and my cock explodes with full fury, filling her up with my cum."
                show cassidy miss cum
                if sad:
                    $ cassidy.love -= 10
                    $ cassidy.sub -= 10
                    "Cassidy cries out in anguish, clearly hurt and upset that I ignored her pleas."
                elif cassidy.love > 160:
                    "Cassidy relaxes and stares at me with a soft, happy smile on her face."
                    cassidy.say "I love you, Master!"
                $ cassidy.impregnate()
    else:
        "When I finally can't take anymore, I orgasm, filling the condom up with my sticky cum."
        show cassidy miss cum
    "When it's all over, I pull out of her and go limp."
    hide cassidy miss
    if not sad and cassidy.love > 120:
        show cassidy naked happy
    else:
        show cassidy naked

    if cassidy.love > 160:
        cassidy.say "Will you come snuggle with me for a bit?"
        "I do so, crawling into bed beside her and wrapping my arms around her."
        cassidy.say "I love you, Master! You're the best thing that ever happened to me."
    return

label cassidy_fuck_anal_sub:
    $ renpy.dynamic('hurt', 'hurtsogood')

    $ hurt = 20 - (4 * cassidy.get_flag_value('anal')) - (cassidy_love / 5)

    $ hurtsogood = cassidy.get_flag_value('anal') < 3 and hurt <= 0
    show cassidy miss anal
    "I pull her legs apart, spreading her cheeks and pressing the tip of my cock against her asshole."
    if cassidy.get_flag_value('anal') < 1:
        "Cassidy yelps in surprise as her rectum parts for my swollen head."
        cassidy.say "Wait! I've never been fucked there before!"
        "I don't wait, though, and I push my cock further in."
    if hurt:
        show cassidy miss pain
        cassidy.say "It hurts!"
        menu:
            "Go slow and gentle":
                hero.say "Give it a moment, honey. I know it hurts right now, but it will feel good soon, I promise! I'll be gentle!"
                "And as I promised, I do go slow, pushing in just a little, then back out. Rocking gently and stopping as soon as it looks like the pain will be too much."
                $ cassidy.love += 1
                $ cassidy.sub += 2
            "A little pain is good for her":
                $ cassidy_sad = True
                hero.say "Get used to it, bitch! Your ass is mine for what you did to me, and I want your sexy ass!"
                $ cassidy.love -= 5
                $ cassidy.sub -= 5
                "I push my way as deep into her anus as I can go, which isn't all the way. As soon as I do, Cassidy nearly screams."
                cassidy.say "But you promised!"
                "She's right, I did promise. So I slow down a little."
                hero.say "You're right, I did promise. I'll go slower."
    else:
        if hurtsogood:
            show cassidy miss pain
            "My cock goes in deeper than it did last time, but not all the way. Cassidy's expression looks pained, but she doesn't make any noise."
            hero.say "Are you okay?"
            cassidy.say "It hurts but don't stop!"
            $ cassidy.sub += 2
        else:
            "I push my cock into her ass, which is ready and opens for me easily. I can fit it almost all of the way in there."
            "And now that she's loose enough that it no longer hurts, Cassidy looks like she's enjoying herself too!"
    "I gently thrust in and out of Cassidy's anus."
    if hurt and not hurtsogood:
        "Cassidy whimpers softly, but as she loosens up, this passes, and by the time I'm ready to explode, she's starting to get into it."
    elif hurtsogood:
        "Cassidy whimpers softly, but every time she does, it's accompanied by a half-choked shout of \"More!\""
    else:
        "Cassidy moans softly, enjoying "
    show cassidy miss outside cum normal
    "Just when I'm about to cum, I pull out."
    show cassidy miss outside -cum bellycum
    "Which showers her tits and belly with my hot, sticky cum, mixed with all the secretions that came from her anus."
    if hurt and not hurtsogood:
        cassidy.say "Oh thank God that's over."
    elif hurtsogood:
        cassidy.say "I love you, Master, even if it hurts!"
    else:
        cassidy.say "That was so good!"
    $ cassidy.set_flag('anal', 1, mod='+')
    return

label cassidy_sleep_date_fuck_sub:
    scene bg bedroom1
    show cassidy naked
    if cassidy_sad or cassidy.love < 120:
        if cassidy_sad:
            show cassidy sad
        cassidy.say "Can I go home now?"
        hero.say "You don't want to stay and cuddle?"
        if cassidy_sad:
            cassidy.say "Not after what you did."
        else:
            cassidy.say "I guess, if that's what you want, Master."
        menu:
            "You may go":
                show cassidy normal
                hero.say "Fine, you were a good pet. You can go."
                $ cassidy.love += 1
                "Cassidy gathers her things and without any other words and heads up the stairs."
            "Stay":
                show cassidy sad
                hero.say "No, stay. I want to use those big, beautiful boobs as pillows tonight."
                $ cassidy.love -= 3
                $ cassidy.sub += 1
                cassidy.say "Very well, Master."
                "Cassidy stretches out on my bed and makes herself available. I curl up next to her and fall asleep with my head between those two gorgeous tits."
    else:
        cassidy.say "Would you like me to stay the night, Master?"
        menu:
            "You should go":
                hero.say "I have an early morning tomorrow, I'm sorry."
                $ cassidy.love -= 1
                if cassidy.love > 160:
                    "Cassidy gathers her things, and gives me a goodbye kiss before leaving."
                else:
                    "Cassidy gathers her things and without any other words, heads up the stairs."
            "I'd love that":
                hero.say "Yes, my darling, you should stay here."
                $ cassidy.love += 1
                $ cassidy.sub += 1
                show cassidy happy
                cassidy.say "Thank you, Master."
                if cassidy.love > 160:
                    cassidy.say "I love you so much, Master!"
                    hero.say "I love you too, my beautiful pet!"
                "Cassidy stretches out on my bed and makes herself available. I curl up next to her and fall asleep with my head between those two gorgeous tits."
    call sleep from _cassidy_sleep_date_fuck_sub
    return

label cassidy_fuck_date_dom:
    $ cassidy.set_flag('sex', 1, mod='+')
    scene bg livingroom
    show cassidy
    cassidy.say "Wow, [hero.name], you have a good job. Why do you live...here? You could afford something really nice!"
    hero.say "Perhaps you overestimate how much I make."
    cassidy.say "Maybe. Whatever. Take me to your bedroom."
    scene bg bedroom1 with dissolve
    show cassidy
    menu:
        "Get on the bed":
            hero.say "Get on the bed."
            $ cassidy.love -= 5
            $ cassidy.sub += 5
            cassidy.say "Just who do you think is in charge here, [cassidy.heroname]?"
            hero.say "I, uh."
            cassidy.say "Yeah, it's not you."
        "What do you want me to do?":
            hero.say "What would you like me to do?"
            $ cassidy.love += 1
            $ cassidy.sub -= 1
    $ result = randint(1, 2)
    if cassidy.love < 160 or result == 1:
        call cassidy_dom_oral
    else:
        cassidy.say "Tonight I'll let you fuck my pussy, if you use a condom."
        menu:
            "Agree" if hero.has_condom():
                call cassidy_fuck_pussy_dom
            "No":
                cassidy.say "Well, in that case..."
                call cassidy_dom_oral
    return

label cassidy_fuck_pussy_dom:
    $ hero.use_condom()
    show cassidy miss outside
    "Cassidy lays down on the bed while I'm putting on the condom requested."
    "This is quite a step for her, allowing herself to be vulnerable, even though she still sees herself as in charge."
    "It's possible this relationship could work out after all."
    show cassidy miss condom vaginal
    cassidy.say "Do me now before I change my mind, [cassidy.heroname]!"
    "Cassidy takes a sharp breath as I enter her, the sound of the air through her teeth almost a spasm of anticipation."
    cassidy.say "Oh! Oh my God!"
    "Holding her legs as far apart as I can, I slowly thrust my dick into her, going a little deeper very stroke until I can feel the tip of my head pressing against her cervix."
    "She makes little noises, moans in the back of her throat that grow louder with each thrust."
    show cassidy miss ahegao
    cassidy.say "Oh yes! Yes, [hero.name], that's...oh God yes!"
    "I can feel her pussy spasm repeatedly as she orgasms, and then she goes goes limp, smiling at me while I finish."
    "Just a few more thrusts and I'll be ready to blow!"
    "When I finally can't take anymore, I orgasm, filling the condom up with my sticky cum."
    show cassidy miss cum
    "When it's all over, I pull out of her and go limp."
    hide cassidy miss
    show cassidy naked happy
    return

label cassidy_sleep_date_fuck_dom:
    if cassidy.love > 160:
        cassidy.say "Oh, that was so good. Snuggle me tonight and keep me warm, [cassidy.heroname]."
        "I do as she bids, pressing my body alongside hers and pulling the blankets over both of us."
        "As she drifts off to sleep, she says sleepily..."
        cassidy.say "I love you."
        hero.say "I love you too, my Mistress."
        "We drift off to sleep, spooning for the entire night."
        $ cassidy.love += 5
        $ cassidy.sub -= 2
    else:
        cassidy.say "That was fun, [cassidy.heroname]! See you tomorrow!"
        menu:
            "Demand she stay":
                hero.say "No, stay!"
                $ cassidy.love -= 5
                $ cassidy.sub += 2
                show cassidy angry
                cassidy.say "[hero.name], you're the bitch in this scenario, not me. You heel, not me. Sit, stay, bark? That's you."
                "She grabs her things and departs quickly, leaving no argument. I hear the front door slam on her way out."
            "Beg she stay":
                hero.say "Please, Mistress! Stay with me for the night?"
                $ cassidy.love += 5
                $ cassidy.sub -= 2
                if cassidy.love > 120:
                    cassidy.say "Well, you have been a good boy. I suppose I can stay. Promise you'll be good?"
                    hero.say "Yes, Mistress, of course I'll be good!"
                    "We drift off to sleep, spooning for the entire night."
            "Let her go":
                $ cassidy.sub -= 1
                hero.say "Good night, Mistress!"
                "She gives me a quick kiss and then disappears up the stairs. I go to sleep, satisfied with my work."
    call sleep from _cassidy_fuck_pussy_dom
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
