layeredimage bg personal:
    if game.hour >= 20 or game.hour <= 5:
        "personal_night"
    else:
        "personal_day"

init -2 python:
    Room(**{
        "name":"personal",
        "hours": (8,20),
        "display_name": "My office",
        "exits": ["office", "alettaoffice"],
        "alternate_exits": ["office"],
        "days": "123456",
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "valid":False,
        "outfit":"work"
        })

    Activity(**{
        "name": "work_place_spy_camera",
        "duration": 1,
        "display_name": "Place spy camera",
        "game_conditions": {"room":["personal"], "flag_underinvestigation":True, "flag_cassidycameraplaced":False, "done": "cassidy_setup_meeting"},
        "required_item": "spy camera",
        "label": ["work_place_spy_camera"],
        "icon":"spycamera",
        "once_day": True
        })

    Activity(**{
        "name": "work_call_the_accountant",
        "duration": 1,
        "display_name": "Call Jeff the accountant",
        "game_conditions": {"room":["personal"], "flag_underinvestigation":True, "flag_toldjeff": True, 'flagmax_workinvestigation': 99},
        "label": ["work_call_the_accountant"],
        "icon":"investigate",
        "do_once": True
        })

    Activity(**{
        "name": "work_personal",
        "money_gain": (["charm","knowledge"],("promoted",1)),
        "duration": 4,
        "game_conditions": {"min_energy":2,"min_hunger":2,"min_grooming":2,"min_fun":2,"room":["personal"], "flag_suspended":False},
        "display_name": "Work",
        "label": ["work"],
        "icon":"work",
        "say": [
            "All work and no play makes [hero.name] a dull boy."
            ]
        })

    Activity(**{
        "name": "workhard_personal",
        "money_gain": (["charm","knowledge"],("promoted",2)),
        "fun":-2,
        "duration": 4,
        "game_conditions": {"min_energy":4,"min_hunger":4,"min_grooming":4,"min_fun":4,"room":["personal"], "flag_suspended":False},
        "display_name": "Work hard",
        "label": ["workhard"],
        "icon":"work_hard",
        "say": [
            "All work and no play makes [hero.name] a dull boy."
            ]
        })

    Event(**{
        "name":"shiori_teaser",
        "label": ["shiori_teaser"],
        "duration": 0,
        "game_conditions": {
            "activity":["work","workhard","work_personal","workhard_personal"],
            "chances":20,
            "room":["personal"],
            "flag_female":0
            },
        "do_once": True,
        })

label work_place_spy_camera:
    "It takes a little while, but I find a good spot for the camera that can see the entire office, and is nearly impossible to see if you're not looking for it."
    $ game.set_flag('cassidycameraplaced', True)
    $ hero.lose_item('spy camera')
    return

label work_call_the_accountant:
    "I pick up the phone to call the accountant, but before I do I go over in my head what I know about him."
    "I know that according to Cassidy, he's the guy who rigged this whole thing."
    "I know that Cassidy has blackmail material on him."
    "I'm pretty sure he's sleeping with Cassidy."
    "That means my best course of action is to start off nice, but threaten to tell his wife about his girlfriend. That will put him in a rough spot."
    "It could make things worse, but I'm feeling desperate here."
    "I take a deep breath and call his extension."
    jeff_say "Hello, Jeff in accounting."
    "Judging from his voice, Jeff is older than I realized. At least 50, unless he's just spent too much of his life smoking and drinking."
    hero.say "Hi, Jeff! My name is [hero.name] [hero.family_name]. I think you might know what this is about."
    "There is a pause, and I can hear him swallow."
    jeff_say "Mr [hero.family_name], we should only be speaking if we have questions for you. At this time we do not have questions for you."
    hero.say "No? No questions for me at all? You mean, you don't want to ask me where the money went? Oh right, it's because you already know."
    jeff_say "I'm sure I don't know what you're talking about."
    hero.say "I'm quite sure you do, Jeff."
    jeff_say "I'm going to hang up now. Goodbye, Mr [hero.family_name]."
    hero.say "Wait, Jeff. Before you do, Cassidy sends her regards. I was just wondering, how do I reach your wife?"
    "There is another pause, and I can feel my blood pressure skyrocketing while I wait to see if he takes this bait."
    jeff_say "W-w-w-why would you want to reach my wife?"
    hero.say "Oh, I just thought your wife and your lover might have something to talk about."
    jeff_say "NO! No it's not like that!"
    hero.say "No? Then what is it like?"
    jeff_say "That's none of your business!"
    hero.say "Jeff, listen to me very carefully. Your slampiece is trying to nail my balls to the wall, and she's using you to do it."
    hero.say "She already threatened to tell Caroline -- that's your wife's name, isn't it?"
    jeff_say "I--I--I'm not going to answer any of these questions."
    hero.say "Fine, Jeff. Don't answer. But what will Caroline say? Aren't you old enough to be Cassidy's father?"
    jeff_say "Please don't do this!"
    hero.say "Then stop this!"
    jeff_say "I--I can't. I can't stop any of this."
    hero.say "Look, Jeff. I can't make this any more clear: If I go down, I'm taking you with me. You can stop this."
    jeff_say "I. Please!"
    "Jeff's voice breaks, and I can hear a sob."
    "Please, Mr [hero.family_name], she won't let me stop. It was just once, but then she had pictures, and she makes me...oh God I can't talk about it."
    hero.say "Then help me stop her. I have something on her. With your help, I can get us both out of this."
    "Where Jeff's voice was confident and at the beginning of the conversation, by now he sounds desperate. I'm pretty sure I have him, and I just need to reel him in."
    jeff_say "I don't believe you."
    hero.say "You don't have to believe me. If you don't help me, you're going down. Do you believe that?"
    jeff_say "W-w-what do you want me to do?"
    hero.say "I just need you to throw off the investigation. I'm going to find out where the money actually went, and the fucker who did this is going to pay."
    jeff_say "I already know who did this, and you can't make him pay."
    hero.say "You do? Who!?"
    jeff_say "You can do whatever you want to me, but he can do worse. I'm not saying."
    hero.say "Damn it, Jeff! Don't wimp out on me here. Your family is at stake!"
    jeff_say "Look, I'll do what I can. I'll push some different numbers. But I can't do too much. He'll figure it out, and he'll screw me worse than you possibly can."
    jeff_say "You can take my family from me, but he can take everything. Everything."
    hero.say "You'd better. You'd better fix this for me. Or else."
    jeff_say "No promises, Mr [hero.family_name]. But I'll see what I can do."
    "I hang up the phone. I can only hope and pray that he puts enough wrenches in the investigation to at least make it inconclusive."
    $ game.set_flag("workinvestigation", 20, mod="+")
    return

label shiori_teaser:
    "I look to the cheerful looking girl that set in front of me less than impressed."
    "She has been talking for the last fifteen minutes about her qualifications and why she was right for the position of my new secretary."
    "I have barely heard a word she had said."
    "Now she was looking to be with a wide smile waiting for me to say something."
    hero.say "That’s very interesting... Let me go over a few things and you should hear in about a week if you have the job."
    "I flash her a smile and she beams at me, thanking me once again for the opportunity of having the interview. As the door shuts I think she so doesn’t have the job."
    "I groan and rub my face."
    "She had been the fifth interview and they had all been the same."
    "Great test scores, didn’t make mistakes, always on time. Basically, thought they were perfect."
    "The problem is I don’t want someone who is perfect and always wants to kiss my ass."
    "I want someone who acts human and if they make mistakes admits to it and takes the responsibility for it."
    "And someone attractive wouldn’t hurt."
    "I hear a knock at my door and groan."
    hero.say "Yes?"
    show shiori teaser
    shiori_say "Is this where I interview for the new secretary position?"
    "I am about to tell her I’m done for the day when I look up and see her."
    "A cute little Asian woman with dark hair and huge breasts."
    "The biggest I have ever seen."
    hero.say "Uh yes, come right in."
    "She smiles but not in an annoying suck up way like the others."
    "Just in a greeting sort of way."
    "She holds out her hand."
    shiori_say "I’m Shiori. You must be [hero.name]."
    "I realize my mouth is handing open and I am still holding her hand."
    hero.say "Yes, that’s me."
    "I let go of her hand and gesture towards the chair."
    hero.say "Sit down and tell me something about yourself... Shiori."
    "Why do I love her name so much already?"
    shiori_say "Well, I’ll be honest."
    shiori_say "I’m not perfect but I try my best and really need a job."
    shiori_say "I usually do better when I have a good leader over me."
    "I raise an eyebrow."
    hero.say "Is that right?"
    shiori_say "Yes sir."
    "I chuckle. Not only does she say she needs a leader 'over her' she calls me sir."
    "I realize she looks confused as my mind is in the gutter."
    shiori_say "Is something wrong, sir?"
    menu:
        "No":
            hero.say "No, nothing’s wrong."
            "I see she still looks confused and uncomfortable."
            "Crap. I think she thinks I’m making fun of her."
            "I think of something to try to get rid of the awkward feeling in the room."
        "I like it when you call me sir.":
            hero.say "I like it when you call me sir."
            shiori_say "Oh um..."
            "She blushes and laughs."
            shiori_say "Then I guess I can make it a regular thing... sir."
            "Did her voice sound flirtarious now? Or was it my wishful thinking?"
            "Probably wishful thinking."
    hero.say "Anyway, you better get used to calling me sir, because it seems you have the position."
    "She looks to me surprised."
    shiori_say "Really?! But you didn’t ask me any questions?"
    "I shrug."
    hero.say "I can tell you are down to Earth. Just what I need in a secretary. Not someone who thinks they are better than anyone."
    shiori_say "Well I hope I can live up to what you expect of me. When do I start?"
    hero.say "Can you start tomorrow?"
    shiori_say "Of course! Uh... sir!"
    "She jumps up then and her breast bounce as she holds out her hand again."
    shiori_say "See you in the morning, sir."
    "I watch her leave, bouncing boobs and her hips swaying side to side and can’t help but think I can’t wait to see her again in the morning."
    hide shiori
    if not "shiori" in GIRLS:
        show screen message(title="Teaser",what="Shiori is only a teaser right now, she will be fully added to the game later on.")
        pause
        hide screen message
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
