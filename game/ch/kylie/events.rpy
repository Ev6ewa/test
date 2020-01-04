init python:
    Event(**{
        "name": "kylie_event_02",
        "label": ["kylie_event_02"],
        "duration": 1,
        "game_conditions":{"room":["university"], "min_charm":50, "done":'kylie_event_01', "flag_female":0, "days":"5"},
        "do_once": True,
        "once_day": True,
        "quit": True
        })

    Event(**{
        "name":"kylie_init",
        "label": ["kylie_init"],
        "game_conditions":{"not_done":'kylie_event_02'},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name":"kylie_start",
        "label": ["kylie_start"],
        "game_conditions":{"done":'kylie_event_02'},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Activity(**{
        "name":"kylie_event_03",
        "duration": 1,
        "label": ["kylie_event_03"],
        "game_conditions":{"done":'kylie_event_02', "hours":(19,24)},
        "girls_conditions": {"kylie":{"min_love":40,"present":False}},
        "do_once": True,
        "icon":"kylie"
        })

    Event(**{
        "name": "kylie_event_04",
        "duration": 1,
        "game_conditions":{"done":'kylie_event_03', "activity":["talk","sweet_talk"]},
        "girls_conditions":{"ACTIVE":{"min_love":100,"not":"kylie"},"kylie":{"min_love":50,"present":True}},
        "label": ["kylie_event_04"],
        "do_once": True,
        "quit": True,
        })

    Event(**{
        "name": "kylie_event_05",
        "duration": 1,
        "game_conditions":{"done":['kylie_event_04', 'alexis_event_01']},
        "girls_conditions":{"kylie":{"present":True, "flag_nextevent":False, "flag_jealouspath":False}},
        "label": ["kylie_event_05"],
        "do_once": True,
        "quit": True,
        })

    Event(**{
        "name": "kylie_event_06",
        "duration": 1,
        "game_conditions":{"done":'kylie_event_04', "room":["bedroom1"],"hours":(22,4)},
        "girls_conditions":{"kylie":{"present":True, "flag_nextevent":False, "flag_jealouspath":True}},
        "label": ["kylie_event_06"],
        "do_once": True,
        "quit": True,
        })

    Event(**{
        "name": "kylie_yandere",
        "duration": 0,
        "game_conditions":{"activity":["kiss","spank","talk","sweet_talk","offer_a_drink","ask_birthday","ask_number","cinema_with","dance_with","gift"]},
        "girls_conditions":{"ACTIVE":{"not":"kylie"},"kylie":{"valid":True,"present":True, "min_love":25}},
        "label": ["kylie_yandere"],
        "do_once": True,
        })

    Event(**{
        "name": "kylie_give_christmas",
        "label": ["kylie_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"kylie":{"min_love":50,"present":True, "valid":True, "flagmax_yandere":89}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })


    Event(**{
        "name": "kylie_give_christmas_murder",
        "label": ["kylie_give_christmas_murder"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0, "hours":(6,12), "room":["livingroom", "bedroom1", "bathroom", "secondfloor","kitchen","pool"]},
        "girls_conditions": {"kylie":{"min_love":50, "valid":True, "flagmin_yandere":90}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "kylie_give_birthday",
        "label": ["kylie_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"kylie":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "kylie_give_valentine",
        "label": ["kylie_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"kylie":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "bree_mike_meet_kylie",
        "label": ["bree_mike_meet_kylie"],
        "duration": 1,
        "game_conditions":{"flag_female":1, "room":["university"], "days_played":7, "hours":(10,17)},
        "girls_conditions": {"mike":{"min_love":75, "valid":True}},
        "once_day": True,
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name":"kylie_preg_talk",
        "label": ["kylie_preg_talk"],
        "duration": 0,
        "do_once": False,
        "girls_conditions": {"kylie":{"flagmin_pregnant":6,"flag_pregtalk":0, "active":True}},
        "game_conditions": {"activity":"interact"}
        })

    Event(**{
        "name": "kylie_pregnant_flag",
        "label": ["kylie_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"kylie":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

label kylie_pregnant_flag:
    $ kylie.set_flag("pregnant",1,mod="+")
    return

label kylie_preg_talk:
    show kylie happy
    $ kylie.set_flag("pregtalk")
    kylie.say "[hero.name], hi!"
    "At the sound of her voice behind me and close enough to almost whisper in my ear, I can't help jumping almost out of my skin."
    hero.say "SHIT!"
    hero.say "Kylie - why do you have to sneak up on me like that?!?"
    hero.say "Are you trying to give me a heart attack or what?"
    "But from the wide-eyed expression on her face and the sheer width of her smile, I can instantly tell that Kylie's in one of those moods where she's off with the fairies."
    "I know that I shouldn't think things like this about the girl that I'm currently dating, but it always feels like there's a little bit of the crazy about her at times like this."
    "Of course, I mean the cute, kooky kind of crazy."
    "Not the straight-jackets and padded rooms kind of crazy..."
    "Anyway, I soon remember that it was Kylie that wanted this meeting and that she had an announcement to make."
    hero.say "Erm...you said that you wanted to see me, Kylie?"
    hero.say "That you had something you needed to tell me to my face?"
    "I didn't think that it was possible, but all the same I see Kylie's smile become even wider than before."
    kylie.say "Of course, [hero.name]."
    kylie.say "And trust me, you're gonna be so glad that I did!"
    "I nod at Kylie, trying to encourage her to hurry up and spit it out - whatever IT is."
    kylie.say "Oh, [hero.name] - I'm pregnant!"
    "I might have had no clue as to just what Kylie was about to say, but I still didn't expect it to be that!"
    hero.say "You're what?!?"
    kylie.say "I'm pregnant..."
    "She cocks her head on one side and begins to look at me in a puzzled manner, as if this was not the reaction she had been expecting."
    kylie.say "What's the matter, [hero.name]?"
    kylie.say "Aren't you happy to hear that you're going to be a father?"
    kylie.say "Doesn't it make you go all gooey inside just thinking about how this means we can raise them together?"
    kylie.say "How we can get married and settle down, be a proper family?"
    kylie.say "Don't you see?"
    kylie.say "It's like fate intervened and gave us a reason that we HAVE to stay together...forever!"
    "The whole time that she's been telling me this, Kylie's also been leaning ever closer."
    "So by the time she says the word 'forever', she's practically close enough for the tips of our noses to touch."
    "While her eyes just seemed to be wide with enthusiasm before, they now look like there's an intense fire in them."
    "It's almost...well...if I'm honest, it's almost enough to scare me."
    menu:
        "I'll take responsibility":
            "But then I finally manage to give myself a metaphorical shake, realising just how stupid and paranoid I'm being right now."
            "It's pretty obvious that I've been letting my natural fear of commitment colour everything Kylie's said to me."
            "Of course she's going to be crazy - crazily elated at the prospect of having a baby with the man that she loves."
            "And the last thing that she needs at a time like this is to have that same guy acting like a childish, irresponsible jerk!"
            hero.say "I'm sorry, Kylie - you're right...of course you're right."
            hero.say "I am happy, but the news just stunned me for a second, that's all."
            "At this, Kylie shows her delight by leaning in and kissing me, full on the lips."
            "She even goes as far as to slip her tongue in and press her voluptuous body against me as she does so."
            "And I have to admit, at this point I just melt, feeling all of my former misgivings draining away."
            "All I can think about is the image of Kylie with her belly swelling as our child grows inside of her."
            "I can't believe that I've let myself become so paranoid as to be able mistake her genuine love for something more sinister!"
            "And that's certainly a mistake that I won't be making again."
            "When she finally breaks away from the kiss, I see that Kylie has the most gorgeous smile on her face."
            "I honestly don't think that I've ever seen her looking more beautiful and radiant than she does right now."
            show kylie blush
            $ kylie.love += 10
            kylie.say "Oh, [hero.name] - I always knew that this would happen to me one day."
            kylie.say "I always knew that if I waited long enough, I'd have you and we could settle down together."
            kylie.say "And now that my dreams have all come true, I'm NEVER going to let you go again!"
        "I don't want anything to do with it":
            "Fuck sake - I can't be a father, not at this stage in my life, and certainly not without some kind of warning either!"
            "Don't get me wrong, for all of her quirks and odd habits, I adore Kylie."
            "She's fun to be around, and she turns me on like crazy."
            "But as much as I'm not ready to have a kid, I've never thought of her as the family type either."
            hero.say "You...you sound like you've already decided to keep the baby, Kylie."
            show kylie sad
            "Suddenly she looks at me with horror evident in her eyes, clutching at her belly with both hands."
            kylie.say "Oh, [hero.name]...I could never, ever even imagine murdering our child!"
            kylie.say "Please don't tell me you think I'd be capable of that!"
            kylie.say "This baby is a symbol of the fact that we were always meant to be together..."
            hero.say "No, Kylie...you don't understand."
            hero.say "I was trying to say that I can't be a parent right now."
            hero.say "I respect your decision to keep the baby."
            hero.say "But, I'm sorry - I can't be a part of the kid's life, not like you'd want me to..."
            $ kylie.love -= 20
            $ kylie.set_flag("yandere",25,mod="+")
            "Kylie goes quiet for a moment, simply staring at me."
            "I get the impression that she's processing my words, sifting them for meaning."
            "Her eyes seem to glaze over for a couple of seconds, like she's zoned out while thinking about what to do next."
            show kylie happy
            kylie.say "Don't worry, [hero.name] - I understand completely."
            "Surprised to hear her speak so quickly, it takes me a few seconds to realise what Kylie actually just said."
            hero.say "Wait...what...you do?!?"
            "She smiles at me, sweetly and with infinite indulgence."
            kylie.say "Sure I do - I've gone and sprung all of this on you, and you just need some time to make sense of it all."
            kylie.say "So you do that, and the baby and I will be waiting for you as soon as you're ready."
            hero.say "No, Kylie...that's not it - you're twisting my words..."
            "Before I can say any more, Kylie puts a finger to my lips and stops me in my tracks."
            kylie.say "Shhh...it's okay."
            kylie.say "There's no need to say another word!"
            "And with that, she turns and walks away from me, still holding up her finger to keep me silent."
            "Which isn't really that much of a problem, as I'm pretty much lost for words anyway."
        "You should get an abortion":
            "For a moment, I'm genuinely stunned by the both the revelation of Kylie being pregnant and her almost psychotic glee at the situation."
            "Sure, messing around with her was fun, kind of like riding a roller-coaster that terrified and elated me in equal measures."
            "And it's not like I've been using her as a fuck-buddy either - I have a very real affection for Kylie, honestly I do."
            "But I've already pretty much made up my mind that she's not long-term relationship material, let alone a potential wife and mother to my children."
            "I know that I'm not ready to have kids, and that I'd want to be able to plan that kind of thing out once I'm sure that I am."
            "And then there's the obvious matter of Kylie's mental health, which I think it's pretty clear just isn't up to the challenge of raising a child."
            "I can't put this off any longer, not when there's the potential of a new and innocent life being harmed as well."
            hero.say "Kylie, I think we both know that keeping the baby would be the wrong decision to make."
            "The elation and manic happiness drains from Kylie's face in mere seconds as she listens to my words."
            "In its place, I can see a look of confusion that's quickly turning into a dark and even worrying expression of anger."
            show kylie angry
            kylie.say "What did you just say to me, [hero.name]?"
            kylie.say "Please, tell me that I just misheard you - tell me that you didn't say what I thought you just said!"
            "I can hear myself swallowing and coughing in actual fear, my Adam's apple bobbing up and down like a ballcock."
            "But I try as best I can to hold my nerve and press on, confident that Kylie will back down if I just stand up to her."
            hero.say "You heard me well enough, Kylie."
            hero.say "Neither of us is capable of raising a child right now, we're both of us too young and selfish."
            hero.say "I think that the only answer is for you to have a termination, before it's too late..."
            show kylie sad
            "The anger in Kylie's eyes is momentarily replaced with disbelief, as though she truly can't understand why I'm saying these things to her."
            "But all too soon the same anger returns and she looks at me as though she actually wants to kill me."
            show kylie angry
            $ kylie.love -= 20
            $ kylie.set_flag("yandere",50,mod="+")
            kylie.say "How can you say that, [hero.name]?"
            kylie.say "How can you even think it?!?"
            kylie.say "We were always destined to be together, to love each other - and our baby's supposed to be living proof of that!"
            kylie.say "Why, [hero.name] - why don't you want our baby?"
            kylie.say "Why don't you love me like you're supposed to?!?"
            hero.say "Kylie, please - you're upset and emotional, maybe from the hormones."
            hero.say "I do love you, really I do..."
            "I don't want to say it, and I wish I could keep from doing so with every fibre of my being."
            "But I can't...I just can't."
            hero.say "You don't need a baby, Kylie - you need help."
            hero.say "From me, from a doctor, from..."
            "Before I can finish the sentence, I see the barest hint of something catching the light in Kylie's clenched fist."
            "And then she slashes it in an upwards arc, before I even have a chance to react."
            "The blade of the box-cutter is razor-sharp, slicing my throat open before I can feel it doing so."
            "I don't have any sensation of the blood that's now gushing from the gaping wound she's made."
            "All I can hear is the sound of my own ragged breath, as the air in my lungs escapes through the wound instead of my mouth."
            "Kylie keeps on talking as I fall onto my knees and then onto all fours at her feet."
            "I can't make sense of it all, but there's something about me being a monster and a murderer."
            "Something else about how she'll always have the baby, and it'll be someone that loves her and appreciates her like she deserves to be."
            "The last thing I can make out is now she'll never let the kid go and how they'll stay with her forever."
            "But by now the sound of her voice has faded into an indistinct sound that has no meaning to me."
            "And as I finally bleed out and pass into the darkness, I have no idea whether I'm alone or not at the very last."
    return

label bree_mike_meet_kylie:
    "I'm feeling like my brain's pretty frazzled, even after the first lecture of the day, so I head out into the quadrangle to get some fresh air and natural light before the next one."
    "It's not as though I have any particular plan in mind, just the desire to do something unstructured and free to distract me from the intellectual grind for a couple of minutes."
    "A few familiar faces pass me by as I wander aimlessly, but no one seems to want to strike up a conversation, and I'm happy to be alone in my own space right now."
    show mike casual at left
    "I only spot Mike by sheer chance, as he turns in my direction just as I happen to walk past, and I doubt he'd even have noticed if I hadn't waved and started towards him."
    show kylie casual at right
    "Honestly though, it's not my housemate that's really caught my attention, but rather the girl that he's talking to right now."
    "Don't get me wrong, a pretty girl chatting to Mike isn't all that rare of a thing."
    "He's no male model in terms of his looks, but he's cute and a pretty sweet guy to boot."
    "But the girl's more than enough to turn heads, and to keep them turned as well."
    "She's a platinum blonde with one of those bodies that's kept in bombastic shape by its owner being young enough to still get away without needing a gym membership."
    "And even worse, I can instantly see that she's one of those types that's charming to guys and probably a cold-hearted bitch to her fellow girls."
    "Don't ask me how I know, because a woman just knows - she can either spot them a mile off, or else she's one herself."
    "Of course, being a guy, Mike won't realise any of this and will just think that she's sweetness and light."
    "I can see it in the way she leans closer to him, wrapping her hair around her fingers and giggling like a little slut."
    "That's why it's pretty much my duty, as his friend, to check this girl out and see just what her intentions are towards him."
    menu:
        "Talk to them":
            "I decide to play the innocent female friend, not wanting the girl to suspect that I'm checking her out and put on an act of her own."
            hero.say "Hey, Mike!"
            hero.say "Aren't you going to introduce me to your new friend?"
            "Mike's face tells me that he's pretty happy to see me."
            "But to look at the girl's expression, you'd think she'd just found me stuck to the bottom of her shoe."
            "Oh she doesn't show it, but I can tell by the way she narrows her eyes at me."
            mike.say "Oh...hi, Bree."
            mike.say "This is Kylie - I used to know her back in high-school."
            mike.say "I had no idea she went here too until she spotted me just now."
            "Kylie responds to this by nodding and giving Mike a sickly smile."
            kylie.say "Yeah, we go WAY back - so I'm really more like an old friend than anything else!"
            "Wow - that was a nice little jab in the ribs disguised as a casual comment if I ever heard one!"
            mike.say "Kylie, this is Bree...my housemate."
            "Hmm - a pause and then he calls me his housemate, rather than his friend or anything more intimate."
            "I guess Mike's a little confused about his feelings when it comes to this girl."
            hero.say "I have to ask, Kylie - because you just look so young and fresh-faced."
            hero.say "How did you know Mike in high-school?"
            hero.say "He must have been way older than you, right?"
            $ kylye.set_flag("yandere",5,mod="+")
            "Kylie looks annoyed by my question, as though she doesn't want to admit the answer."
            "But of course, Mike's a guy, and so he doesn't pick up on any of that."
            mike.say "Yeah, Kylie was younger than me - I knew her because I was dating her older sister at the time."
            mike.say "But, well...that didn't work out too well for me."
            "Score one for me right there!"
            "She might have grown up to be pure man-bait, but this Kylie was once someone's snotty little sister."
            "No matter what she does in the here and now, that image of her will always be in the back of Mike's mind!"
            "Seeing that Mike's starting to recall more of his memories from back then, and perhaps more about his ex-girlfriend than her sister, I feel my job here is done."
            hero.say "Well, I've gotta run if I want to make it to my next lecture on time."
            hero.say "See you back home later, Mike."
            hero.say "Great to meet you too, Kylie!"
            mike.say "See you tonight, Bree."
            kylie.say "Yeah, whatever..."
            "As I walk away, I can't help feeling a little smug at having put Kylie in her place in front of Mike."
            "Hopefully she'll take the hint and be a bit more wary of me around him in future."
            "And if I'm really lucky, I may not see too much more of her at all."
        "Kiss Mike" if mike.get_flag_value("kiss") and game.get_flag_value("morality") < 25:
            "Call me a slut or a manipulative bitch if you like - it's not like I'll feel any worse about myself for it."
            "But with a girl like this sniffing around, you have to be willing to mark out your territory and defend it from the start."
            "That's why I make no effort to announce myself to either of them, standing there in silence until the girl notices me and glances in my direction."
            "After a moment of looking at her in that typically clueless way he has, Mike turns around too."
            "By the time he's turned to face me, his mouth is already half open to ask a question."
            "Which is all the better for what I have in mind..."
            hide mike
            hide kylie
            show bree kiss casual
            $ kylye.set_flag("yandere",10,mod="+")
            $ mike.love += 5
            "Wrapping my arms around his neck and pulling him down to my level, I pretty much clamp my lips over his."
            "I make sure that the other girl can see my tongue dart in there as well, and then I'm Frenching Mike mercilessly."
            "He's too stunned to even think about resisting, and I think that I can just about guess what his little friend must be thinking right now."
            "In fact, the thought of a 'little friend' gives me all the inspiration I need to kick things up a notch."
            "I press myself against Mike so that we're body to body, making sure that every part of me is in contact with him."
            "And then I take one hand from around his neck and use it to reach down towards his crotch."
            "As I take hold of his cock through his pants and give him a good, hard squeeze, I can feel that he's already standing to attention."
            "It feels pretty good to know that I can have that kind of effect on him from a cold start."
            "Even better when he's just been chatting away to that flirting little harpy too."
            "I can feel that Mike's getting into it now, his initial confusion no longer making him stiff and awkward in my arms."
            "But it's another small victory for me that, even though he's regained his composure, he's not making any effort to pull away from me."
            "I let him enjoy the feeling of being passionately kissed while I stroke his cock for just a little longer."
            "And then I slowly release him, keeping him wanting more."
            hide bree
            show mike casual at left
            show kylie casual angry at right
            hero.say "Hey, Mike...I missed you so much!"
            "Mike looks about as confused and flustered as I'd expect him too."
            "The girl, on the other hand, is clearly looking daggers at me right now."
            "But not at him, which is interesting..."
            hero.say "Well, don't just stand there like a slapped fish."
            hero.say "Aren't you going to introduce me to your little friend here?"
            mike.say "Erm...ah...Kylie, this...this is Bree."
            mike.say "Bree...this is Kylie."
            mike.say "She's someone I used to know...back in high-school."
            mike.say "And you're my..."
            hero.say "That's right, Mike - I'm yours and you're mine!"
            hide kylie
            show kylie casual at right
            "I grab his arm and cling to it, as though I'd rather tear it off at the shoulder than be dragged an inch from his side."
            "By now, Kylie has crossed her arms over her chest and has a distinctly sour look on her face."
            "But as I've not technically done anything that violates the rules of polite conduct, she has no choice but to pretend to be pleasant in return."
            kylie.say "So you go here too, yeah?"
            hero.say "Oh yeah - I go anywhere that Mike goes!"
            hero.say "We're inseparable -aren't we, honey?"
            mike.say "We are?"
            hero.say "Ha ha...of course we are, silly!"
            hero.say "Well, I have to run if I want to get to my next lecture on time."
            hero.say "Nice to meet you, Kylie."
            kylie.say "Likewise."
            hero.say "See you back home tonight, Mike."
            hero.say "I'll be waiting for you..."
            "As I walk away, I can't help feeling a little smug at having put Kylie in her place in front of Mike."
            "Hopefully she'll take the hint and be a bit more wary of me around him in future."
            "And if I'm really lucky, I may not see too much more of her at all."
    hide mike
    hide kylie
    return

label kylie_cookies:
    if kylie.get_room() == game.room:
        $ kylie.love += 2
        $ kylie.sub += 2
        $ kylie.set_flag("yandere",1,mod="-")
        $ NOTIFICATIONS.append(["Kylie {image=ui/icon_yan_vsmall.png}-5",2])
    return

label kylie_give:
    $ gift = Consumable("Kylie's cookies", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day", label=["kylie_cookies"])
    "Kylie gives me home made cookies."
    hero.say "Thank you, Kylie."
    $ hero.gain_item(gift)
    hide kylie
    return

label kylie_give_valentine:
    show kylie
    "Kylie walks hesitantly towards me."
    call kylie_greet from _call_kylie_greet_7
    show kylie
    kylie.say "Happy valentine's day [hero.name]..."
    call kylie_give
    return

label kylie_give_birthday:
    show kylie
    "Kylie walks towards me."
    call kylie_greet from _call_kylie_greet_8
    show kylie happy
    kylie.say "Happy birthday [hero.name]!"
    call kylie_give
    return

label kylie_give_christmas:
    show kylie
    "Kylie walks towards me."
    call kylie_greet from _call_kylie_greet_9
    show kylie happy
    kylie.say "Merry christmas [hero.name]."
    call kylie_give from _call_kylie_give_1
    return

label kylie_yandere:
    $ kylie.set_flag("yandere",1,mod="+")
    $ NOTIFICATIONS.append(["Kylie {image=ui/icon_yan_vsmall.png}+5",2])
    return

label kylie_start:
    $ kylie_love_max = 40
    $ kylie.love += 30
    $ hero.smartphone_contacts.append("kylie")
    $ if "kylie" in HIDDEN: HIDDEN.remove("kylie")
    return

label kylie_init:
    python:
        if "kylie" not in HIDDEN and not kylie.get_flag_value("story"):
            HIDDEN.append("kylie")
    return

label kylie_give_christmas_murder:
    scene bg livingroom
    "You may not be surprised to hear this, but as our house is basically three pretty casual friends under one roof, we don't really have any Christmas traditions as such."
    "Sure, we always talk vaguely about getting together to have a meal so that we can at least do something to mark the occasion and we always swap dumb little gifts."
    "But what usually happens is that we each end up partying on the night Christmas Eve with our own friends and then crawling out of bed later in the day, still reeling from the night before."
    "Then the most that we can manage is to crash out on the sofas, find a takeaway that's delivering and stare at something vaguely seasonal in an amiable silence."
    "Not exactly everyone's ideal image of an average Christmas Day, I know."
    "But then we're not the average househole either."
    "The reason that I'm telling you all of this is to explain why I'm so puzzled to hear someone knocking at the door on this particular Christmas Morning."
    "I glance at the clock on the bedside table, seeing that it's well before midday."
    "That's a small comfort at least, knowing that I haven't overslept."
    "While I'm congratulating myself on this achievement, the knocking at the door begins again."
    "Doesn't look like they're going to get tired of trying to raise an answer and just go away any time soon."
    "And so with a fuzzy head and the threat of a hangover looming, I crawl out of bed and pull on just enough clothes to qualify as decent."
    "On my way down to the front door, I can still hear the knocking as it continues on."
    hero.say "Alright, alright...I'm coming as fast as I can!"
    hero.say "Jesus - who's in this much of a hurry on a national fucking holiday!"
    "I walk past Sasha's room, seeing the shape of her still asleep on the bed thanks to the door being half open."
    "Bree's door, by way of contrast, is wide open, and there's no sign of her in there whatsoever."
    "Then a thought occurs to me - maybe she stayed out later than Sasha and I, then only discovered that she'd lost her keys when she was standing on the doorstep."
    "I admit that this idea makes me hurry a little more than I would have if I suspected it was anybody else out there."
    "After all, I don't want to spend a day trapped in the house with a tired and cranky Bree that's also pissed that I left her standing in the cold for too long."
    hero.say "What happened - you party so hard that you forgot your..."
    scene bg house
    "I trail off as I open the door, expecting to see a worse-for-wear Bree."
    show kylie christmas happy
    "But instead, I'm greeted with the sight of an extremely perky Kylie, positively beaming with the spirit of the festive season."
    kylie.say "Surprise, [hero.name]!"
    kylie.say "Happy Christmas!"
    "I open my mouth to say something appropriate in response, but nothing comes out."
    "Despite the fact that it's damn cold outside and there's snow on the ground, Kylie's not exactly wrapped up against the Winter chill."
    "She has on one of those outfits that's a combination of red and white, showing off as much flesh as possible without being positively indecent."
    "I can't honestly tell if she's supposed to be Mrs Santa Claus reminding her husband that she's all woman, or some kind of over-sexed elf."
    "But either way, the effect is the same and it renders me utterly speechless."
    "Kylie giggles at my evident state of confusion, the sweetness of the sound only serving to make matters worse."
    kylie.say "Oh, [hero.name], what a reaction - I'm so flattered!"
    hero.say "Erm...yeah...you're welcome, I guess."
    kylie.say "Anyway, I suppose you're wondering why I'm here?"
    "I rub the back of my head and nod."
    hero.say "Well...the thought had crossed my mind..."
    "At this, Kylie cocks her head on one side and gives me one of those amused smiles people use when they think the other person isn't all together there."
    kylie.say "Can't you guess?"
    "I have to shake my head, admitting that I'm still stumped on that particular question."
    kylie.say "I came to give you your Christmas present, silly!"
    "As she turns to retrieve something from behind her, bending over to pick it up, the short skirt of her outfit rides up even further and I'm treated to quite a view."
    "Trying to cover up my amazement at Kylie then proceeds to wiggle her backside as she stands back up, I blurt out the first thing that comes into my mind."
    hide kylie
    show kylie gift
    hero.say "You really shouldn't have, Kylie."
    hero.say "I feel really bad, because...because I don't have a gift to give you in return!"
    "Kylie waves away my apologies with one hand, using the other to clutch the box she just picked up."
    "It's maybe a foot on each side and wrapped in typically gaudy paper with a bow and label on top."
    kylie.say "Don't be ridiculous, [hero.name]."
    kylie.say "Knowing that you like my outfit was the best gift you could have given me!"
    kylie.say "Now don't keep me in suspense all morning - open your present!"
    "I nod, trying to shake off the funk that I'm in and focus on doing as she says."
    "The way I see it, that's the easiest way to get out of this rather awkward situation."
    "Whatever's inside the box is quite heavy, and seems to be loose in there, as I can feel it rolling around as I handle the parcel."
    "Trying to make a good show of it, I shake the thing, but no discernible sounds can be heard to reward my efforts."
    "Looks like there's nothing for it but to get on with it and actually open the thing."
    "Holding the box in the crook of one arm, I use my free hand to tear at the wrapping paper and start to pry open the lid."
    "It's at this point that I notice the bottom of the box feels oddly damp against the bare skin of my arm."
    "But then I remember that Kylie just plucked this thing off of the path, so no wonder it feels wet."
    "Struggling with the last of the paper around the lid, I give Kylie what I hope is a positive look, just to show I'm still doing as I'm told."
    "And in return, I get an excited smile and a flapping of her hands that I assume is meant to encourage me to go faster still."
    "When I finally tear away the last of the paper and open the top of the box, the first thing I see is what looks like hair."
    show kylie gift bree
    "What in the hell did she get me - a damn wig?!?"
    "But then I remember the circumstances and that I need to be delighted with it, even if it's a box of roadkill."
    show kylie gift bree yandere
    "Grabbing a handful of the hair, I try to turn whatever it is over and get a better look."
    "There's a flash of something so pale that it's almost white."
    "And then I drop the box, almost tossing it away from me as I see something that stares back."
    "It's an eye - blue, glassy and utterly dead."
    "I fall over my own feet and collapse onto my on the path, struggling ineptly to crawl away from the contents of the box."
    "My foot kicks out and send it rolling out onto the virgin snow that covers the lawn."
    "All at once I get the answer to the two burning questions of the morning."
    "Now I know what was in the box and why Bree never made it back home last night."
    "There on the lawn, staring up at the sky with dead eyes, is Bree's severed head."
    "Her mouth is open, as if in some last terrible scream."
    "Her blonde hair streaked and stained with blood from the ragged stump of her neck."
    "I can't make sense of what I'm seeing, as if my mind refuses to process the evidence of my eyes as it knows what the consequences of doing so will be."
    "Part of me can't understand why someone would put Bree's head in a box and give it to Kylie."
    "Another is worried that Bree's going to come home any moment and be horrified to see her own head tossed out on the lawn like garbage."
    "My mouth starts to work silently, trying to ask Kylie if she knows what's going on."
    hide kylie
    show kylie christmas yandere
    kylie.say "Hey there, hey now!"
    "I feel the sensation of her sitting down behind me, cradling my body against her own."
    kylie.say "It's okay, everything's okay."
    "Still in a state of hopeless confusion, I can't help being comforted by her words and the feeling of her pulling me close."
    kylie.say "This wasn't what I wanted - you know that, right?"
    kylie.say "I love you, [hero.name], and I always will, no matter what."
    kylie.say "But she was in the way, so she had to go - that's all there is to it!"
    "I make an effort to move, the implications of what Kylie's telling me only now starting to sink in."
    kylie.say "Uh-uh, no struggling now."
    kylie.say "You'll ruin this perfect moment!"
    show kylie christmas blush knife
    "I don't feel the blade that she uses to slice open my throat, only hear the gasping sound of air escaping from the gaping hole."
    "My body begins to twitch and spasm, but Kylie clutches me to her all the same."
    show kylie christmas happy knife blood
    kylie.say "You see, after I killed her, I had what you might call an epiphany of sorts."
    kylie.say "I realised that the thing that's kept us apart was never you or me - it was other women, always trying to come between us."
    kylie.say "The only way we can ever be together is if there's no other women to do that."
    kylie.say "But I can't kill every other woman on the face of the Earth."
    kylie.say "Believe me - I would if I could, [hero.name], and all for you!"
    kylie.say "So I decided to do the only other thing that would work, and kill you instead."
    kylie.say "That way you'll always be perfect, just how I remember you."
    kylie.say "And always be mine, because I'll be the last person to hold you close, keep you warm and tell you that I'll always love you..."
    "She keeps on talking, telling me things that I can't hear and wouldn't matter to me even if I could."
    "I'm dying in her arms, getting colder and farther away from the world with every second that passes."
    "Soon there's nothing but blurred colours and incoherent sounds, my own thoughts also losing all meaning."
    "Then there's just a confused mass of sensations that have no beginning or end."
    "And then there's nothing..."
    $ renpy.full_restart()
    return

label kylie_event_06:
    $ target = GIRLS[kylie.get_flag_value("target")]
    "You know that weird feeling of being watched, the one that's something to do with the unconscious parts of your brain?"
    "It's not like you know that's what it is at first, more like it's an uneasy tingling as the hairs on the back of your neck stand up."
    "Only when you finally stop what you're doing and look around do you start to feel like there's someone snooping on you."
    "I look up from my desk after realising that the last sentence I wrote is nonsensical garbage."
    "It's getting stupidly late, and I should have turned in a good few hours ago to keep from feeling like a zombie in the morning."
    "But still, somehow I know that it's not the fact that I've been up, burning the midnight oil, that's distracting me."
    "For some reason, my eyes are drawn to the window, even though the curtains have been drawn all evening."
    "I try to shake off the feeling, telling myself that I'm probably just stressed and tired from all the work I've been doing of late."
    "And yet I keep looking back at the window, as if there's something on the other side of the glass that I won't be able to rest until I've seen."
    "More to prove to myself that this whole thing is just a stupid distraction than anything else, I push back my chair and get up."
    "As I walk the short distance to the window, I have no choice but to stretch out my aching back and listen to the noises that my protesting body makes."
    "That can't be good - surely someone of my age shouldn't creak and crack like that?"
    "I don't do anything so dramatic as throwing the curtains aside, just opening them wide enough to stick my head through the gap."
    "Outside there's nothing remarkable to be seen at first glance, just a typically dark, unremarkable night."
    "This alone should have be enough to convince me that I'm jumping at shadows."
    "But I linger a little longer, enjoying the chance to take a break from my work and stare out of the window instead."
    "And that's when I see the figure, standing beneath one of the street-lights that line the pavement outside my house."
    "A chill runs down my spine, and I jump back away from the window, surprised to have seen anyone out there so late at night."
    "But then I take a second glance down at the figure, and that's when I realise that I recognise the person."
    hero.say "Kylie..."
    "As if she hears me murmur her name, Kylie chooses that exact moment to look up at my window."
    "Her face is a veritable picture of delight as she smiles and waves at me eagerly."
    "Though in the harsh glare of the street-light, Kylie does rather take on the aspect of a leering ghoul thanks to her wide grin and large eyes."
    "Baffled as to just what I should do in this situation, I resort to opening the window and calling down to her."
    hero.say "Kylie - what in the hell are you doing down there?!?"
    "Kylie's brows wrinkle in apparent puzzlement."
    kylie.say "I've come to see you, [hero.name] - isn't it obvious?"
    hero.say "But why - do you even know what time it is?"
    kylie.say "I need your help - that's why."
    kylie.say "Well, are you going to let me in or not?"
    "It seems like she's not going to volunteer anything more than that."
    "And as though my question about the lateness of the hour is just going to be ignored too."
    "I'm reluctant to open the door to anyone that turns up at random and this late at night, no matter what they want from me."
    "But I'm already more than a little concerned about Kylie's stability, so just turning her away seems a pretty harsh thing to do."
    "Plus, I don't want her to cause a scene in the street, maybe even make one of my neighbours call the police..."
    menu:
        "Let her in":
            "How long have I been saying that I wanted to be a friend to Kylie, that I wanted to help her out?"
            "Well, I guess this is the point where I have to put my money where my mouth is..."
            hero.say "Okay - just come to the door and I'll be right down."
            scene bg livingroom
            with fade
            "Hoping that I haven't just made a massive mistake, I hurry downstairs and open the front door for Kylie."
            scene bg house
            show kylie
            with fade
            "Kylie stands in front of me, positively beaming with happiness at being let in."
            kylie.say "Thanks again for inviting me in, [hero.name]!"
            hero.say "Well...what kind of a friend would I be if I left you out there, alone and in the cold?"
            kylie.say "Oh, [hero.name] - I'm so lucky to have a friend like you!"
            hero.say "Erm...so...here we are then..."
            "Kylie remains silent, but she looks at me in a suggestive manner, nodding eagerly."
            hero.say "Just wait here a second - I need to take care of a few things in my room."
            "At the mention of my bedroom, Kylie's smile seems to widen even more."
            scene bg bedroom1
            with fade
            "While Kylie takes off her shoes in the hallway, I race back upstairs and into my room."
            "My tidying basically consists of cramming things into drawers and shoving what's strewn across the floor under my bed."
            "When I've done all I can, the place still looks pretty messy."
            "But hopefully, if I keep the lighting to a couple of lamps, it won't be all that obvious."
            scene bg secondfloor
            show kylie
            with fade
            "I go back out and onto the landing, finding Kylie staring up at me from the bottom of the stairs."
            "She has that open, innocent look on her face that just seems to be designed to make me melt."
            "When she does that, I almost instantly forget any worries that I might have had about her."
            hero.say "All clear - come on up."
            "Nodding as she begins to run up the stairs, Kylie comes as soon as she's called."
            scene bg bedroom1
            show kylie
            with fade
            "It's not like Kylie's the first girl that I've had inside my room."
            "But for some reason, it feels different as she walks in and sits down on the bed beside me."
            hero.say "So...are you going to tell me why you turned up on my doorstep like this?"
            hero.say "Because I have to tell you, it's got me pretty worried for you right now."
            "Though I'm trying to voice my concern for her, Kylie's reaction is more like I'd have expected if I'd told her I was madly in love with her."
            kylie.say "Oh, [hero.name] - you really think that much about me?"
            kylie.say "I just knew you were the right person to turn to!"
            hero.say "Erm...yeah...right..."
            hero.say "Oh, I'm being a bad host."
            hero.say "Can I get you anything?"
            hero.say "It's cold out there tonight - would you like a hot drink?"
            hero.say "Not coffee this late at night, but tea?"
            kylie.say "That'd be lovely!"
            hero.say "Okay, I'll be right back."
            "Kylie watches me until I leave the room, smiling sweetly the whole time."
            "I pause on the landing, pulling out my mobile and logging onto the site from which I can watch the camera that I have set up in my room."
            "Normally I'd only check the feed if I suspected that I'd had a break-in or something like that."
            "But I really do want to see what Kylie gets up to in my absence."
            "Sure, she might spot the camera, but she won't know if it's turned on or not."
            "Watching the screen, I make my way down to the kitchen and begin making her tea."
            "It's not long before I see something that makes me stop what I'm doing and stare at the image before me."
            "Almost as soon as I'm on the stairs, Kylie darts for my laundry pile, rummaging through it like a determined terrier."
            "She surfaces a moment later, a pair of my briefs clutched in her hand."
            "I watch as she lies back on the bed and pulls the dirty underwear over her face, putting the crotch right under her nose."
            "Her breathing is muffled, but I can hear her taking in long, deep breaths all the same."
            kylie.say "Mmm...[hero.name]...ahh..."
            "Kylie lies there like that for about thirty seconds, and then pulls the briefs off of her face."
            "She balls them up and crams them down between her considerable breasts, evidently wanting to keep them as some kind of trophy."
            kylie.say "What else are you hiding, [hero.name]?"
            kylie.say "Let's take a quick peek, shall we?"
            "Kylie slides neatly off the bed and begins to rifle through the contents of my bedside drawers."
            "I have no idea what she's hoping to find in there, as I'm not the kind of guy to keep a secret diary or treasured keepsakes in there."
            "She seems to be getting more than a little frustrated, that is until she happens upon a bundle of old photos in the bottom of one drawer."
            "I know instantly what those are - shots that I took on a disposable camera of myself with an old girlfriend."
            "Back then, most mobile phones only had shitty cameras, and you could still buy that kind of camera and get the shots developed easily."
            "I only keep them for the sake of the pleasant memories they stir in me."
            "But they seem to have quite the opposite effect on Kylie, as she bears her teeth, grinding them in what looks like anger."
            "She roots around in the same drawer until she finds a black marker pen, and begins to scribble all over the girl in the picture."
            "With her free hand, she fishes the soiled briefs out of her bra and shoves them under her skirt."
            "I don't need any help to know what she does with them next, as I can see her hand going up and down under the fabric."
            "And I can clearly see the look of almost manic excitement on her face as she rubs the crotch of the briefs against the lips of her pussy."
            "Kylie combines the act of defacing the image of my former girlfriend with that of frantically pleasuring herself with something that's been against my cock."
            "The message is quite a simple one to figure out..."
            "Once the girl's image has been completely obliterated, Kylie seems satisfied enough to stuff the briefs back into their hiding place once more."
            "She shuffles the photo back into the pile and tosses them back inside the drawer where she found them."
            "By this time, the kettle has boiled and the tea is brewed, so I decide to hurry back upstairs before Kylie can get up to anything else."
            "I open the door to find her sitting on the bed in almost the precise spot that I left her, face a picture of innocence."
            kylie.say "Oh, thank goodness you're back - I was starting to get worried!"
            "I frown a little as I hand over the steaming cup of tea."
            hero.say "Erm...I was only gone like five minutes at the most!"
            kylie.say "Well, it felt like a real long time to me..."
            "Oh god, I can feel her locking onto me with those huge eyes and just pulling me in again."
            "I should be confronting her with what I just saw on the camera, telling her off for stealing my clothes and defacing my photos."
            "But she's just so beguiling somehow - I can't stay mad at her!"
            "And it's not just because she's unbelievably hot - honestly, it's not."
            "The more I get to know about her, admittedly numerous, flaws; the more I want to be the one to save her."
            "She's like some kind of beautiful, broken doll...and I can't help wanting to be the guy that repairs her, that makes her whole again."
            "Kylie leans in closer to me, and I can smell that unique scent that I noticed the last time she was this near."
            "We're alone, in my room, on my bed..."
            hero.say "Kylie..."
            kylie.say "Yes, [hero.name]..."
            hero.say "You still haven't told me why you came here."
            kylie.say "Isn't it obvious?"
            kylie.say "I came because I missed you [hero.name]..."
            kylie.say "And because..."
            "Kylie entwines her fingertips, staring sheepishly down at them in her lap."
            kylie.say "And...I wanted to say sorry...for how I was when I saw you with that girl the other day..."
            "I have to be honest with her, otherwise I won't be able to look her in the face."
            hero.say "Kylie - what I said to you then, about [target.name]..."
            hero.say "It wasn't the absolute truth."
            hero.say "What I'm trying to say is...I don't think I feel as strongly about her as I might have made it sound..."
            "Without missing a beat, Kylie leaps on the opportunity that I've just given her."
            kylie.say "So you're basically saying that you might have stronger feelings for me?!?"
            hero.say "Yes...maybe...I don't really know!"
            kylie.say "Don't worry, [hero.name] - that's good enough for me!"
            kylie.say "All that really matters is that I like you and you like me too."
            kylie.say "We can fill in all the little details along the way!"
            "And with that, she's getting to her feet as though she intends to leave."
            hero.say "You're...you're leaving?"
            kylie.say "I sure am - you'll get nothing more from me tonight, you naughty boy, you!"
            "Still more than a little bewildered, I show her to the door and say goodnight."
            "When I get back to my room, I have the urge to watch back the footage of her in my room."
            "But the password to my phone escapes me, and I can't find the scrap of paper on my desk where I'd scribbled it down for just such an occasion."
            "Dismissing it as unimportant, I climb into bed and finally managed to fall sound asleep."
        "Don't let her come in.":
            "Okay, when did my life become like something out of a horror movie?"
            "Seriously, this girl should have her own sinister theme music, just to warn people when she's around."
            "As hot as she undoubtedly is, Kylie's obviously fallen out of the crazy tree and hit every branch on the way down."
            "If I needed serious motivation to focus my attentions on [target.name], then she just gave it to me in spades."
            "Yanking the curtains closed, I turn off all the lights in the room before crawling into bed."
            "Almost as soon as I'm under the covers, I can feel myself drifting off."
            "Even the memory of Kylie, staring up at me from the street below, seem to fade away..."
            scene bg bedroom1 with fade
            $ game.pass_time(1,True)
            "When I wake up, I'm surprised not to have heard my alarm go off."
            "I roll over and look at the clock on the bedside table, convinced that it must be dawn already."
            "But, much to my surprise, I see that it's not much more than twenty minutes since I got into bed."
            "A moment later I take a breath and cough, feeling just how dry and scratchy my throat feels."
            "No mystery as to what woke me up then."
            "Time for a quick trip to the kitchen for a glass of water..."
            scene bg secondfloor with fade
            "Dragging myself out of bed, I wander across the landing and down the stairs in the general direction of the kitchen."
            scene bg kitchen with fade
            "Padding barefoot across the tiled kitchen floor, I grab a glass and fill it from the tap."
            "As I drink the water, I begin to wake up a little more."
            "The memory of Kylie, standing there in the street comes back to me."
            "I laugh a little and shake my head, still not sure what she was hoping to achieve by turning up at such a late hour."
            "Surely she must have gotten too cold and uncomfortable to still be out there, right?"
            "It's at that very moment that I swear I see something, pale and oval in shape, looking in through the window."
            "The glass falls from my hand, shattering on the floor and I leap back to avoid the shower of shards."
            "When I look back at the window, the shape, whatever it was, is gone."
            "Damn it - I could have sworn that was a face!"
            "Still shaking, I force myself to sweep up the glass and then begin to make my way back to bed."
            "I walk into the hallway, making for the stairs, telling myself the whole time that I was just seeing things that weren't there."
            "But as I reach the foot of the stairs, I hear a slow, heavy knocking at the front door."
            "I freeze in place, only my head turning to stare at the frosted glass panes in the door."
            "By the street-lights, I can just make out a figure standing there, its head frames in a mass of blonde hair."
            "It's Kylie - it has to be!"
            "I try to take comfort from the fact that the door is locked and securely bolted as I turn my head away."
            "Taking the stairs one at a time and making as little sound as possible, I sneak up to my room."
            scene bg secondfloor with fade
            "Feeling like I could hear the sound of breaking glass and splintering wood at any given second, I finally make it to the sanctuary of my bedroom."
            scene bg bedroom1 with fade
            "Once inside, I hastily jam a chair under the door-handle and make sure that my phone is to hand on the bedside table."
            "That done, I crawl back into bed and pull the covers up almost to the level of my nose."
            "Part of me can't believe that I'm this afraid of a girl."
            "But another part of me is hoping and praying that she's gone long before morning comes around."
    return

label kylie_event_05:
    $ target = GIRLS[kylie.get_flag_value("target")]
    "After the last encounter that I had with Kylie and her catching me talking to [target.name], I was worried about how she'd react the next time I saw her."
    "I might not have got my feelings for [target.name] one hundred percent straight yet, but I don't see why that should stop Kylie and I still being friends."
    "She's a hell of a lot of fun to be around, at least when she's in a good mood..."
    "And you can't avoid the fact that she's pretty hot to boot!"
    "So when I bump into her at uni, I'm relived to see that she's all smiles at the sight of me."
    show kylie happy
    "It's almost as though the last encounter we had never happened at all."
    "Weird how she seems to be able to turn things on and off like that..."
    kylie.say "Oh [hero.name] - will you just look at all of this!"
    hero.say "Look at what, Kylie?"
    "Kylie makes a helpless face as she holds up an armful of textbooks, notebooks and other assorted papers."
    "Coursework - that's something anyone taking a class can appreciate!"
    hero.say "Ouch - sorry to see such a mountain of work!"
    hero.say "I know just how you must feel."
    kylie.say "Urgh...it's just so BORING!"
    kylie.say "I feel like I just want to toss them all in the river - or set fire to them, and watch it all burn..."
    kylie.say "Coursework really sucks."
    hero.say "I know, Kylie - we've all been there, wanting to just throw it all away."
    hero.say "But the alternative's failing, which is much worse."
    kylie.say "It's just so overwhelming though!"
    kylie.say "Maybe if I had a little help though, a study parter, or even a mentor of a kind..."
    "Suddenly, Kylie puts the papers down and clasps her hands together in front of me."
    "She's making serious puppy-dog eyes at me now, and she's disturbingly good at it too."
    hero.say "Ah...Kylie - are seriously asking for my help with your studies?"
    kylie.say "Oh, [hero.name] - that's so sweet of you!"
    kylie.say "I accept!"
    "Kylie makes sure to cross her arms under her bosom as she leans forward, plumping up her already impressive chest."
    "If her intention was to distract and confuse me, then she's been very successful indeed."
    hero.say "Ah...I...erm..."
    kylie.say "You have NO idea how grateful I am that you'd help me..."
    kylie.say "That you'd indulge me like this."
    "Indulge her?"
    "Oh yeah - I'd indulge that, all day long!"
    "No, wait a minute - what was the question again?!?"
    menu:
        "Agree":
            "I can't keep on saying that I want to be Kylie's friend with a straight face if I won't help her out when she needs it."
            "Plus, this is going to involve ploughing through all of that coursework she just showed me, and that's pretty dry stuff."
            "Not much chance of things getting out of hand while we're preoccupied with that little lot either."
            hero.say "Okay, I'll help you out as much as I can."
            hero.say "But we're going to need some place quiet."
            "I think through the options that occur to me, and then make a suggestion of venue."
            hero.say "Both of my housemates should be out right now, so how about we go to my place to study?"
            kylie.say "That sounds perfect - let's get going!"
            "Kylie seems very enthusiastic, but then she's just got the help she wanted with her studies."
            "So she's bound to be excited at the prospect - isn't she?"
            scene bg house
            show kylie
            with fade
            kylie.say "Ooh...nice pad, [hero.name]!"
            kylie.say "I should study with you more often..."
            scene bg livingroom
            show kylie
            with fade
            "Once we're in the house and I'm sure Bree and Sasha are out, I show Kylie into the livingroom."
            "We could use the diningroom table, but I want a more relaxed atmosphere, and so I sit down on the sofa in front of the coffee-table."
            "Kylie settles herself down on the sofa beside me, hands neatly folded in her lap."
            "I almost find myself laughing at how refined she looks, almost regal in her aspect."
            "The effect is somewhat spoiled by the size of her chest though!"
            "Not that I don't find them very impressive, especially this close up."
            "Taking such a long glance at her hands in her lap, I can't help but notice the thick, black stockings that Kylie's wearing."
            "Pulled up almost to the hemline of her skirt, I think I finally understand why they figure so prominently in all those porn videos..."
            "They're just stockings, made out of mundane materials, but somehow they're insanely distracting."
            "But then the complete package is more than a little distracting too."
            "It's weird to find myself doing something so everyday and routine with a girl this hot."
            "Almost like I'm living a dream and just waiting for the moment when I wake up."
            "I wonder what we look like, Kylie and I."
            "Do we make a cute couple, or would people just not believe that I even had a chance with a girl this stunning?"
            "But anyway, back to reality..."
            hero.say "Right then - let's have a look at the first of these equations and you can tell me what's got you stumped..."
            "Instictively, I lean over the first page of the textbook open on the coffeetable."
            "And, of course, Kylie almost immediately does the same."
            "It's weird, but you never really take in someone's scent until you're this close to them."
            "Kylie's scent puzzles me a little, in as much as I can't decide if it's a perfume or natural."
            "Either way it's intriguing, in a way I never thought a smell could be."
            "But as usual, there's soon a physical sensation that outdoes it."
            "Something large and very soft is pressing against my arm as Kylie leans in."
            "I think you can guess what it is..."
            hero.say "Do you know what this sign here calls for, what you need to do?"
            kylie.say "No [hero.name], I don't!"
            kylie.say "I think you need to show me..."
            "Kylie's pouting like no student of mathematics ever pouted to be shown the answer before."
            "Time to show her what a real mathematician can do!"
            hero.say "This symbol here indicates that the total can be changed - but in this case, it's not just a case of simple division..."
            "I can see how the problem might baffle a beginner, but this is basic stuff for someone of my level."
            kylie.say "Hmm...I think I get it, [hero.name] - but it's so fucking dull!"
            "Kylie frowns and lets out a cute, pouting sigh as she leans her head in closer still."
            "Her long, blonde hair falls over my shoulder, locks brushing against my cheek."
            hero.say "I...I guess that's...that's true!"
            kylie.say "Hmmm...I'm bored, [hero.name]..."
            "Kylie sits up, just a little straighter, her hand brushing aside my hair by my ear."
            "Her voice is breathy, almost a whisper in my ear as she speaks."
            kylie.say "How about we go do something...else?"
            hero.say "No, I don't think we should...I don't think we should give up quite so quickly!"
            show kylie sad
            "Kylie pulls back a little way, but not so far that I can't see the look in her eyes."
            kylie.say "So...you don't want to..."
            "She strokes the back of her hand down my cheek, and then slips her fingers around the back of my neck."
            hero.say "After...we can go somewhere - after we get finished with this, okay?"
            hero.say "After we finish here though, okay?"
            "At my words, any trace of disappointment disappears from Kylie's face, and she practically beams at me."
            kylie.say "Oh, yes - that sounds really good!"
            "With that cleared up, we get back to the matter at hand."
            "But all too soon, I begin to agree with Kylie - this is pretty boring."
            "Maybe calling an end to it early and doing something else would reinvigorate us?"
            "Our minds - obviously I meant, reinvigorate our minds!"
        "Refuse":
            "I may know my stuff in the areas that I'm studying, but I'm no tutor the likes of which it sounds as though Kylie needs."
            "Plus there's the issue of her clearly wanting to manoeuvre me into a situation where we're all alone with no witnesses."
            hero.say "I would, Kylie, honestly I would."
            hero.say "But those equations are making my eyes spin just to look at them."
            hero.say "On top of that, I have a ton of my own coursework to get done too."
            "Kylie's eyes were doe-like and soft before now, but they suddenly become hard and almost hateful."
            $ NOTIFICATIONS.append(["Kylie {image=ui/icon_yan_vsmall.png}+5",2])
            $ kylie.set_flag("yandere",5,mod="+")
            show kylie angry
            "I was expecting Kylie to be disappointed, maybe even take it badly enough to throw a tantrum in anger."
            "But she almost jumps back from me as if in shock, her jaw hanging open with obvious outrage."
            show kylie sad
            kylie.say "Well, I never expected to get that kind of response from you!"
            kylie.say "I really thought you were my friend, [hero.name] - I thought that you cared about me!"
            hero.say "Ah, look, Kylie...I'm sorry you're disappointed, but..."
            kylie.say "NO...no...it's fine...fine."
            "Kylie looks down and away from me, half her face falling into shadow and looking surprisngly dramatic as a result."
            show kylie angry
            kylie.say "I suppose that you only study with much smarter girls than me, right?"
            "It's now I notice that Kylie is toying with the bracelet around one of her wrists."
            "She pulls and tugs at it constantly, wrapping it around her fingers as if trying to use the motion to bleed off the tension she's feeling."
            "Suddenly, the band snaps, and the beads that were strung on it go flying in every direction imaginable."
            hero.say "Jesus, Kylie!"
            kylie.say "Urgh...I can't believe this is happening to me!"
            "Kylie looks up again, and I'm taken by surprise by the tears welling in the corner of her eyes."
            kylie.say "Would it have been so bad to just spend a little time studying with me?"
            kylie.say "Is the thought of spending time with me really that awful?"
            hero.say "No, Kylie - that's not what I meant at all!"
            "She takes me by surprise then, stepping in close and grabbing me by the collar with an unexpected show of strength."
            kylie.say "Well fuck it - like it or not, you're coming with me anyway!"
            hero.say "What the hell..."
            "Kylie begins pulling me off by the collar, hauling me away against my will."
            hero.say "Kylie...Kylie, stop!"
            hero.say "This is crazy - you can't just force me to do what you want!"
            kylie.say "Oh, can't I now?!?"
            "Kylie spins around and puts her face within inches of mine, almost nose-to-nose."
            "I can see from the look in her narrowed eyes that she's definitely not joking around with me."
            "The sudden burst of strength, the physical force to get what she wants, the almost manic look in her eyes."
            "A large part of me is pretty scared of her right now."
            "But there's a part of me that's oddly excited too..."
            kylie.say "..."
            "Suddenly the fire seems to go out of Kylie's eyes, and I feel the strength of her grip on my collar weaken to almost nothing."
            "She sighs, so deeply and with such emotion that if feels like the weight of the entire world is settling onto her shoulders."
            show kylie sad
            kylie.say "No...you're right - I can't force you to come with me."
            kylie.say "I'm sorry, [hero.name]...sometimes I just get...emotional, I guess."
            "I rub my neck nervously, not really knowing what's the best thing to say or do right now."
            "I want to help Kylie if at all I can, but the truth is that she's staring to scare me a little."
            hero.say "Ah...well...we all get carried away once in a while..."
            kylie.say "No...it's not like that."
            kylie.say "It's...different - but I don't know how to describe just how!"
            "It's hard to get a handle on just what Kylie's talking about."
            "But it sounds like she's keeping some kind of dark secret from the world at large."
            hero.say "We can always study together some other time, Kylie."
            hero.say "Or we can talk about your feelings, if you'd like..."
            kylie.say "Huh?"
            kylie.say "Oh...okay...whatever."
            hide kylie
            "As I watch Kylie turn and walk away from me, I'm distracted by the myriad of thoughts and feelings she's inspired in me."
            "So much so that I'm genuinely not looking where I'm going."
            "Before I know it, I've gone and walked into someone coming the other way."
            show alexis teaser
            "Of all the people in the world - it's Alexis!"
            alexis_say "Oh...[hero.name], long time no see!"
            alexis_say "You feeling okay?."
            alexis_say "As I couldn't help seeing you get into that little tussle with my kid-sister..."
            hero.say "What...that?"
            hero.say "Oh, don't worry about me - I'll be fine, eventually."
            alexis_say "Well, if you say you're okay..."
            "The atmosphere between us is typically frosty, not helped by the fact she crosses her arms over her chest in a disapproving manner."
            alexis_say "I mean...you know that Kylie's always been a bit...volatile, right?"
            "I nod in agreement, recalling my recent encounters with the girl in question."
            alexis.say "She's usually pretty harmless, unless she lets herself get fixated on something."
            alexis.say "Or someone..."
            alexis.say "Anyway, no one knows what makes her tick better than I do."
            alexis.say "So if she causes you any trouble, or you're just worried about her, tell me, yeah?"
            hero.say "Thanks for the advice, Alexis - I'll be sure to keep it in mind."
            alexis.say "Yeah, sure...sure."
            alexis.say "Good to see you again, by the way..."
            hero.say "Good to see you too, Alexis."
            "Only it isn't good to see her, is it?"
            "Alexis looks better than I remember her, with cute, choppy blonde hair and a full, mature figure."
            "All of which I have to force myself to balance against the way that she broke my heart when she betrayed me back in the day."
            "Falling for Alexis all over again is that last thing that I need to happen to me right now."
            "Especially when things are already getting so complicated between me and her younger sister."
            "But, of course, there's always that perennially stupid part of my brain that keeps on marvelling that I was ever with a girl like Alexis at all."
            "And it starts to make me wonder things like if she's changed over the years, and if she's genuinely sorry for what she did to me."
            "Like I already said, it's a stupid part of me."
            "But the worst thing is that I just don't know how to make it shut the hell up..."
            hide alexis
    return
    return

label kylie_event_04:
    $ kylie.set_flag("target",game.active_girl.id)
    $ kylie.set_flag("nextevent",True,duration=3)
    "Try as I might, there's nothing that I can to do to get the telephone conversation I had with Kylie out of my head."
    "Every time my mind wanders or I try to relax and think of nothing, there it is again."
    "The sound of Kylie's voice as she touched herself as vivid as it was in my ear that night."
    "It was a real shock, but I can't lie to myself and say that it wasn't a massive turn-on at the same time."
    "It took all of my will-power not to start touching myself too..."
    "But there was just something that held me back, made me hesitate."
    "I'm damned if I know what to call it, but under all the girlish charm, there's something slightly scary about Kylie."
    "I don't know if you could actually call her dangerous, and yet she did have me in the palm her hand right there..."
    "Ah, maybe I'm just being a little paranoid, reading too much into the whole thing."
    "It's just that I've only had Kylie back in my life for a couple off days, and already it's been a pretty intense experience."
    "I almost feel like she has this grand plan for me in mind, and she wants to rush me into it."
    "In all the confusion she's caused me, I'd almost for gotten about [game.active_girl.name]."
    show expression game.active_girl.id
    "And how could I have forgotten about a girl that makes me feel the way she does?!?"
    "In the end, I'm so wound up in thoughts of both girls that I almost wind up walking straight into one of them."
    "[game.active_girl.name]..."
    "She spots me first, waving enthusiastically to get my attention before hurrying over to begin chatting away."
    "At first, it's a very welcome relief to have someone to talk to, even if it's just to take my mind off of my anxieties."
    "But the feeling doesn't last, and soon I can feel an odd sensation, nagging at the corners of my attention."
    "It makes me feel twitchy, distracted - almost like I'm being watched..."
    "My gaze keeps wandering as we talk, searching for any sign of the unseen watcher."
    "A couple of times the need to keep looking means that I lose track of the conversation."
    "So I have to make awkward apologies for not listening closely enough."
    "This is probably the reason that the conversation winds up well before I'd have like it to."
    "And so, as I say goodbye to the girl that I really wanted to talk to, I'm already scanning the surrounding area for the one that I suspect is spying on me."
    hide expression game.active_girl.id
    $ NOTIFICATIONS.append(["Kylie {image=ui/icon_yan_vsmall.png}+5",2])
    $ kylie.set_flag("yandere",5,mod="+")
    show kylie angry
    "I was right - there she is, watching me from amongst a stand of trees, her expression none too pleasant as she does so."
    "Even from here, I can see that her large eyes are fixated on me as I chat to [game.active_girl.name]."
    "From the expression on her face, you'd think we were breaking some kind of social taboo."
    "And yet all we're doing is having a slightly flirty chat, out in the open and without any attempt to hide it."
    "I'm astonished to see that she's raking her nails down the trunk of a tree, gouging lines of bark as she does so."
    "In fact, her eyes are so wide that I can actually see her pupils, shrinking down to the size of pinpricks."
    "She doesn't move the whole time, I swear that she doesn't as much as blink."
    "I'm pretty sure there's no way she can hear what we're actually saying."
    "Which means that, unless she can lip-read, she's just fixating on us and thinking whatever thoughts are turning over and over in her mind."
    kylie.say "..."
    kylie.say "Why HER?"
    kylie.say "What's so great about HER?!?"
    "Kylie shows her teeth, visibly grinding them together."
    "And then she turns to lean against the far side of the tree, breathing heavily as if overcome with emotion."
    hide kylie
    show expression game.active_girl.id
    hero.say "Ah...so...I'll see you around - yeah?"
    "She nods enthusiastically, apparently not noticing my state of unease."
    "I get what would normally be a very pleasant hug and a squeeze before she walks off, blissfully unaware of Kylie's lurking presence."
    hide expression game.active_girl.id
    "While I'm glad to have had the chance to talk to her, I'm also pretty pissed off at the moment being ruined."
    show kylie angry
    kylie.say "..."
    "But then my thoughts are interrupted by the sight of Kylie, walking out of the trees and slowly towards me."
    "At first, I try not to pay her any attention, but she's sidling ever closer and so I have no choice but to acknowledge her presence."
    "There's only a vague hint of the annoyance that was in her eyes remaining, and as she reaches the spot where I'm standing, it vanishes completely."
    show kylie happy
    "By the time she's standing in front of me, her face is the very image of sweet innocence."
    kylie.say "Hey, [hero.name]!"
    kylie.say "And how are YOU doing today?"
    hero.say "Erm...hey, Kylie..."
    "I almost flinch as she comes even closer, remembering how she's been watching me and the weirdness of the phonecall the other night."
    "It's odd, but there's still a part of me that wonders what would have happened if I'd just given in and gone along with it."
    "Infuriating as it is, Kylie just seems to have that effect on me, making me wonder what it would be like to give in to her insanity for a moment..."
    hero.say "I'm okay...I guess, all things considered."
    hero.say "And you?"
    kylie.say "Excellent, couldn't be better!"
    "But as soon as she's spoken those words, her expression becomes strained and she cocks her head on one side."
    kylie.say "But...ther is something that's been kinda bugging me a teeny, tiny little bit."
    kylie.say "Don't know if I should mention it though..."
    "This is one of those moments that you seem to get with Kylie, where she catches you totally off-guard."
    "I want to know what's up, but I'm instantly afraid that it'll open a whole new bag of worms."
    hero.say "What's the matter, Kylie?"
    hero.say "You can tell me, can't you?"
    kylie.say "Oh, [hero.name] - I know that I can tell you anything!"
    kylie.say "But...I'm just afraid of what you'll think of me if I tell you this..."
    "She clasps her hands behind her back, beginning to shift from one foot to the other."
    kylie.say "Oh, dear...I don't know if I should tell..."
    hero.say "No, no...Kylie, it's okay - you can tell me."
    kylie.say "You want me to be honest, [hero.name]?"
    kylie.say "Is that really what you want?"
    "I have that unsettling feeling again, the one in the pit of my stomach."
    "This should be a perfectly safe and normal conversation between two sane individuals."
    "Yet with Kylie, it always feels like stepping off a precipice into the unknown."
    kylie.say "I...I saw you talking with [game.active_girl.name] just before I came over to say hello."
    kylie.say "And, well...I guess it just got me wondering."
    kylie.say "What do you think of her, [hero.name]?"
    "What do I think of [game.active_girl.name]?"
    "How do I even begin to answer that - especially when it's Kylie asking the question?"
    menu:
        "She's just a friend":
            "Does what I actually feel for [game.active_girl.name] even matter as far as the answer to that question is concerned?"
            "Sure, I could be brutally honest and tell Kylie that I have feelings for [game.active_girl.name]."
            "But it's not like we're engaged or anything, and I have the urge not to hurt Kylie's feelings for no good reason."
            hero.say "She's a friend, you know?"
            hero.say "I like chatting to her now and then."
            kylie.say "So you're saying that you look forward to it?"
            hero.say "Yeah...I guess so."
            "I had hoped that would settle the matter, but instead she keeps on staring at me with those huge, intense eyes."
            kylie.say "I see."
            kylie.say "Do you like talking to her more than to me?"
            kylie.say "Would you like her to call you like I did the other night?"
            kylie.say "Would you like her to touch herself..."
            hero.say "NO...no, it's not like that!"
            "She's doing it again - going from zero to crazy in five seconds flat!"
            hero.say "I...I really liked what you did for me on the phone the other night."
            hero.say "It was just so incredible, and I was so tired..."
            kylie.say "Oh...so, I kind of wore you out, huh?"
            kylie.say "I was worried that you hated me for it."
            kylie.say "I thought you were talking to other girls to punish me!"
            hero.say "No, Kylie, that's not it at all!"
            "I hate that she makes me do things like this - reassuring her by validating her full-on behaviour towards me."
            "But she seems to desperate and needy at times like this, the last thing that I want to do is be guilty of hurting her."
            "And a large part of me isn't lying - that phone-call was enough to leave me breathless."
            kylie.say "Oh, well - that's okay then!"
            kylie.say "I'll be seeing you soon, I hope?"
            hero.say "Sure...I think we have some classes together."
            kylie.say "Hmm...maybe I'll see you sooner."
            kylie.say "Be careful, [hero.name]."
        "I kinda like her":
            $ NOTIFICATIONS.append(["Kylie {image=ui/icon_yan_vsmall.png}+5",2])
            $ kylie.set_flag("yandere",10,mod="+")
            $ kylie.set_flag("jealouspath",True)
            "I can't possibly string someone as obviously fragile and needy as Kylie along."
            "She deserves to know the truth, no matter how much it might hurt."
            hero.say "Kylie - can I be honest with you?"
            kylie.say "Oh, [hero.name] - of course, you can always be brutally honest with me!"
            "Even as I wince at her choice of words, I'm already committed to saying what I have to say."
            hero.say "I...I think that I like her."
            hero.say "Actually, I like her quite a lot..."
            show kylie sad
            kylie.say "I...I see..."
            "Suddenly, her entire body starts to shake and quiver."
            "She doesn't make a sound, but it's uncomfortable to watch all the same."
            hero.say "Kylie, are...are you okay?"
            kylie.say "Oh I'm fine [hero.name] - I'm just fine and dandy!"
            hero.say "Erm...I don't think that you are..."
            kylie.say "Oh, really - what makes you say that?"
            hero.say "Well...you look really upset right now - upset that I find another girl attractive."
            kylie.say "Hah...that's ridiculous - why would I even care about a thing like that?"
            kylie.say "No...it doesn't bother me in the slightest - not one little bit..."
            "I don't need a sixth sense to know so blatant of a lie when I see one."
            kylie.say "I mean really, you guys - how could you think such a thing [hero.name]..."
            "Kylie turns her back on me, like she's about to run away."
            "But instead, she juts stands there, her shoulders tensing and relaxing."
            "It's as though she's fighting to keep something, under control, to keep it from breaking out."
            hide kylie
            "Is it sadness, or rage that she's feeling right now?"
            hero.say "..."
            hero.say "Kylie...hey, talk to me - please?"
            kylie.say "It's...it's fine...really..."
            "That's when I happen to look down and notice that she's digging her nails into the flesh of her palms."
            "I've never noticed before now, but her nails are almost ragged, as if she's been using them to scratch at something."
            "Small points of red are beginning to appear where the nails are digging in..."
            hero.say "Kylie, for god's sake - talk to me!"
            "Unable to think of anything else to do, I take her by the elbow and make her turn to face me."
            "I'm afraid that touching her, let alone manhandling her, will set her off."
            "But otherwise, I'm all out of ideas."
            hero.say "I...I'm sorry if I gave you the wrong siganls."
            hero.say "I know that I let you give me your number, and then I called you the other night..."
            "I trail off, not wanting to dwell on what happened during that call."
            "All the time, I can't help thinking that I'm just digging the hole I'm already in deeper still."
            show kylie happy
            kylie.say "Who said you gave out any signals?"
            "Kylie finally lets me turn her around, meeting my eye as soon as I do so."
            kylie.say "I think it's great that you like her."
            kylie.say "I'm happy for the both of you!"
            kylie.say "So, I hope we get to stay friends, huh?"
            kylie.say "That would be so nice..."
            "The words are coming out of her mouth, but her face is telling me an entirely different story."
            "Her eyes have a dark cast to them, and her brows are getting pretty intense too."
            "Even a typically clueless guy like me can tell that, underneath it all, she's majorly upset."
            "Her pupils look odd, as if they're really narrow - it's weird, but I can't explain it."
            "She's on the brink of freaking me out for real now!"
            kylie.say "So!"
            kylie.say "You run along and have fun with [game.active_girl.name]!"
            kylie.say "I'll just go back to..."
            hero.say "Kylie, wait - please?"
            "Without as much as another word, she sharply jerks her hand away from mine."
            "Free of my grasp, she hurries away, leaving me alone and staring after her."
    hide kylie
    return
    hide kylie
    return

label kylie_event_03:
    $ kylie_love_max = 100
    "The note's been burning a hole my pocket since the moment that Kylie pulled it out and handed it to me in the Library the other day."
    "It's just a string of numbers, written in a cutesy manner, but nothing at all out of the ordinary."
    "I've been given a telephone number by a girl in the past - hell, sometimes, when I called them, they even turned out to be genuine."
    "But for some reason, this time it feels different somehow...weird maybe too strong of a word, though it's edging that way for sure."
    "What happened between her older sister and me is water under the bridge, as it was so long ago."
    "I mean, Kylie was nothing but a little kid back then, and she had nothing at all to do with how much Alexis hurt me."
    "Ah, but then she couldn't have been that much of a kid, not based on the confession that she made to me before handing over the note."
    "That was a pretty intense story that she told, of her sneaking to watch Alexis and me having sex one stormy night."
    "If she'd been older at the time, or a guy, it'd be easy to think of her as a voyeur and a pervert."
    "But as far as I know, it was just the one time and she stumbled upon us completely by accident, so that'd be a harsh judgement to make."
    "In fact, what does the story she told me and her kind of intense manner mean, other than that she's a quirky individual?"
    "Why should everyone have to be perfectly normal and appear sane the whole time?"
    "How boring of a world would that be to live in?"
    "No, I think the root of my worry is more likely to be the fact that she's the little sister of my ex, and nothing more than that."
    "It's like Kylie said herself, she's tired of everyone thinking of her as the kid and treating her like a child."
    "I've fallen into the trap of thinking about her that way too."
    "Chances are that, if she weren't Alexis's sister, I'd just see her as eccentric and write that off as nothing to worry about."
    "So while the nagging doubts about Kylie are still there in the back of my mind, I resolve to call her."
    "That way I can show myself that I'm just being paranoid for no good reason."
    "Pulling out the note, I dial the number into my mobile."
    "The whole time I'm thinking that it'll probably just go to voicemail anyway."
    "But instead she answers almost as soon as the call goes through and the ringtone has begun."
    kylie.say "Oh, [hero.name]...I'm so glad you finally called me!"
    kylie.say "I've been worrying myself sick that you thought I was some kind of weirdo..."
    "Kylie's voice is instantly excited and eager, but with an odd undertone of barely suppressed tension beneath the surface."
    "What on earth is she talking about?"
    "It's only been a couple of days at the most since we last met up."
    hero.say "What...why would you think that?"
    hero.say "Wait - does this have something to do with the story about you watching Alexis and me?"
    kylie.say "Uh-huh...when you didn't call me that night, I was sure you thought I was some kind of sick pervert!"
    hero.say "Oh...I'm sorry if you got that impression, Kylie."
    hero.say "Didn't you remember that I kind of said I thought the whole thing was hot - quite a turn on?"
    "The nervous energy that I could hear in Kylie's voice suddenly dissipates, and she now sounds a lot more sedate, almost sulky in tone."
    kylie.say "But you didn't call and tell me that - did you?"
    kylie.say "I was going round in circles over what I'd said and done."
    kylie.say "I...I was convinced that you hated me..."
    "I can't understand where any of this is coming from, or how I've managed to upset her so badly."
    "Is she really that sensitive, that crazily hung-up on me?"
    hero.say "No, Kylie, it's nothing like that at all, believe me."
    hero.say "I just wanted to leave it a day or two before I called."
    hero.say "Because...because I didn't want you to think that I was too pathetic and needy."
    "What the hell - maybe she'll respond well to flattery?"
    hero.say "You must have so many guys beating down your door."
    hero.say "And all of them must be younger and better looking than me..."
    kylie.say "NO...I mean...no, I really don't!"
    kylie.say "You're the only guy I'm interested in, [hero.name]."
    kylie.say "And that's the truth!"
    hero.say "Okay, okay, Kylie - I do believe you."
    "She goes silent for a moment, and all I can hear is her breathing on the other end of the line."
    hero.say "Kylie, are you still there?"
    hero.say "Are you okay?"
    "She chuckles in a playful manner, instantly reminding me of just how cute and sexy she is in the flesh."
    "Somehow none of the misgivings that I had before seem to matter in the least right now."
    kylie.say "You know, you really should have called me sooner."
    kylie.say "Even if we can't see each other, we can still be intimate over the phone..."
    "Wait a minute - is she telling me that she wants to talk dirty, right here and now?"
    kylie.say "Where are you right now?"
    hero.say "Ah...I guess I was just thinking about getting ready for bed."
    kylie.say "Well, I beat you too it - I'm already under my sheets!"
    kylie.say "And I'm not wearing anything but my little pink panties..."
    "Oh god - her voice is so teasing, so sexy."
    "I get a picture of what she's describing in my mind so vivid that it almost hurts."
    "My breathing must have become heavier too, as Kylie laughs again and begins to tell me more."
    kylie.say "You can picture it, can't you [hero.name]?"
    kylie.say "Don't be ashamed, it's okay...I don't mind that one little bit!"
    kylie.say "In fact, I want you to lie there and fantasise about me - it lets me know just how much you want me..."
    "She begins to sigh in a way so sensuous that I'm almost convinced that she's already touching herself on the other end of the line."
    kylie.say "Do you remember when I told you how I touched myself, while I was watching you fuck my sister?"
    hero.say "Y...y...yes!"
    kylie.say "Well, now I want you to fantasise that I'm touching myself again."
    kylie.say "Only this time, I'm touching myself at the thought of you fucking me instead."
    "What is she doing to me?!?"
    "She's got my cock so hard I could cut glass with the tip, and all she's doing is talking to me!"
    kylie.say "I'm sliding my fingers under the elastic of my panties."
    kylie.say "They're cold, and they feel so good against my pussy."
    kylie.say "You've made it all wet, [hero.name], just the thought of you did that."
    "I don't know if I should tell her to stop or else urge her on."
    "Maybe it's the fact that this feels so wrong that makes me want her to keep going so badly?"
    kylie.say "Ah...I'm slipping them inside of my pussy now, [hero.name]."
    kylie.say "They feel so good."
    kylie.say "But I'm imagining they're your cock, and that makes them so much better..."
    "My hand keeps straying below my waist as her words have the desired effect."
    "I can see everything she described in my mind's eye, every sound suggesting another image of her in a state of desperate arousal."
    "Only when she's actually cuming and the words on the other end of the line are replaced by sensual moans, can I bring myself to hang up."
    "She sounded to be in no condition to continue the conversation, and it would only have been mere moments until there were two of us at it as well."
    "Shaking my head in disbelief, I continue on my way to bed, knowing that whatever happens from here, Kylie has now wormed her way right into my head."
    "And the worst thing is that I really don't think that I want to root her out of there any time soon, either."
    return

label kylie_event_02:
    scene bg university
    show kylie casual
    "I walk into the university library, looking around as though I've never even seen the inside of the place before now."
    "I have, of course - but I'm not looking for directions, rather I'm looking for someone in particular."
    kylie.say "Hey, [hero.name] - over here!"
    "My head's not the only one to turn around at the loud call, even though that many people in the room can't be called [hero.name] too."
    "Not that Kylie seems to be at all concerned with the etiquette of keeping the noise down in a library."
    "She practically slams her book down on the table in front of her as I walk over, trying to ignore the harsh stares she's attracting."
    kylie.say "I didn't think that you'd come to see me here."
    kylie.say "I'm so happy that you did."
    kylie.say "I have something that I need to tell you!"
    menu:
        "That's what friends are for":
            hero.say "Ah, don't mention it - it's just great to get the chance to catch up with you again."
            hero.say "Plus I thought you might need some help getting to grips with this place."
            hero.say "This place can be pretty intimidating for a new kid."
            "Kylie smiles awkwardly and looks down, tracing the spine of the book she was just reading."
            kylie.say "[hero.name]...would you mind not treating me like I'm still a little girl?"
            kylie.say "I'm all grown up now - legally an adult...know what I mean?"
            "The fact that she looks up and almost catches me eyeing her cleavage makes her point for me."
            "Far more forcefully than her words ever could have."
        "I could never say no to a pretty face":
            show kylie casual blush
            $ kylie.love += 1
            hero.say "To be honest, Kylie - I've been itching to see you again since we met the other day."
            hero.say "I know it sounds lame, but I just can't get over what a beautiful woman you've become."
            "That's a pretty bold compliment, I know."
            "And almost instantly I see Kylie's pale cheeks flush red."
            kylie.say "Thank you, [hero.name] - you have no idea how much that means to me."
            kylie.say "I've always wanted to hear someone say that to me."
            kylie.say "Someone just like you..."
            "She's staring at me so intently now that it's getting a little uncomfortable."
    hero.say "So, you wanted to talk to me about something?"
    "My attempt to chance the subject is so sudden that Kylie almost seems to jump at it."
    "Putting her hands flat on the table, she stands up and leans forwards."
    "Kylie narrows her eyes, the thoughtful look on her face making me think that she's weighing up what she's about to say."







    kylie.say "I’ve been carrying this inside of me for so long..."
    "This sounds like it's going to be heavy going - I can already see Kylie's lips quivering as she speaks."
    kylie.say "But, I really want to share it with you."
    kylie.say "Share something that I’ve been holding onto for years now."
    hero.say "Okay, Kylie...what is it that you want to tell me?"
    "Kylie takes in a deep breath and then lets it out in the form of a dramatic sigh, as if preparing herself for what lies ahead."
    kylie.say "I like you, [hero.name]."
    hero.say "Ah...I like you too, Kylie."
    kylie.say "No...I mean I REALLY like you."
    kylie.say "I've liked you ever since the first moment that I saw you."
    hero.say "Erm...is that so?"
    kylie.say "Yes…yes it is!"
    kylie.say "In fact, let me share a story with you, one that'll explain everything!"
    scene bg black with fade
    kylie.say "Picture the scene - it was a dark, stormy Friday night."
    kylie.say "Mom and dad were out and I was sitting at the old computer, the only one we had in the house back then."
    kylie.say "I was reading a romantic story that I'd found - that's something I still do now, reading about women swept off their feet by a handsome hero and saved from a normal, boring life."
    kylie.say "This one was about a man who climbed the walls of a prison where his lover was being held against her will."
    kylie.say "Did I mention that it was in the middle of a dark and stormy night already?"
    kylie.say "Anyway...all the hero was thinking about was the desire he felt for his lady love."
    kylie.say "As my parents were out, and the story was making me feel all funny down there..."
    "Kylie pauses to nod in the direction of her groin, blushing again as she does so."
    kylie.say "I started to unbutton myself and slide my fingers into my pyjama bottoms..."
    kylie.say "But then, there was a huge thunder-crack, and the power went out!"
    kylie.say "I scared me so bad that I wasn't in the mood anymore, and I went off to bed."
    kylie.say "Then there was a lightning flash, and I saw the shape of a man climbing up the drainpipe!"
    kylie.say "I thought he was going to break in and do terrible things to Alexis and me."
    kylie.say "But then there was another flash of lightning, and it showed me the man's face - that it was you."
    kylie.say "Fighting your way through the storm and climbing the wall, all for her!"
    kylie.say "My heart was all aflutter, and I knew that I had to see more."
    kylie.say "I padded across the landing on bare feet to Alexis's door."
    kylie.say "Back against the wall, I turned the doorknob and peered inside."
    kylie.say "And there you were."
    show kylie memory
    kylie.say "You and Alexis..."
    kylie.say "I could see the way the rainwater made your shirt cling to your chest."
    kylie.say "I wanted to gasp, but instead I bit down on my finger and slipped my other hand under the waist of my pyjamas."
    kylie.say "And when she peeled the shirt off of you, then you tackled her to the bed, my fingers curled tightly."
    kylie.say "The lightning flashed, showing up the shape of your bodies as you undressed each other."
    kylie.say "I heard you whisper to her, asking if she wanted you to go slow."
    kylie.say "She said no, muttering something about my playing stupid music too loud to hear a thing."
    kylie.say "I'd only read about things like that before, but now I was watching it for myself."
    kylie.say "I knew how dangerous it was, you and my sister - fucking in our house like that."
    kylie.say "You could have caught sight of me in an instant...and sometimes I even wondered if you might have..."
    kylie.say "Oh, the way she arched her back as you made her scream!"
    kylie.say "You couldn't have known it at the time, but you made both sisters cum at once that night!"
    kylie.say "I drew blood when I bit down on my finger to keep quiet, watching you drench her belly when you came too."
    kylie.say "I'll never forget a moment of it - I have that image forever etched into my memory."
    kylie.say "I'd always thought that I wanted something like that for myself."
    kylie.say "But as I watched you dress and scramble out of the window, I realised that what I wanted more than anything was you..."
    scene bg university
    show kylie casual
    "Once Kylie's finished recounting her tale, I find that I'm seriously confused about how it should make me feel."
    "On the one hand, it's pretty creepy to imagine her skulking around in the shadows, watching teenage me having sex."
    "But on the other, I can't deny that it's flattering to know that a girl could see me in that kind of light and hold a torch for all these years afterwards."
    "Either way, after baring her soul like that, Kylie's looking at me with wide-eyed expectation."
    "I'm going to have to tell her something."
    "But the question is what, exactly?"
    hero.say "Okay, Kylie..."
    menu:
        "It's wrong":
            "I don't want to hurt her feelings, but what Kylie just confessed to me is just plain wrong."
            "If she's been going around doing stuff like that for most of her life, then she could be in serious danger."
            "At the very least she could use some kind of therapy."
            hero.say "You have to realise that you can't watch people like that."
            hero.say "It's a violation of their privacy, and it's wrong."
            hero.say "And...it makes me feel uncomfortable knowing you did that to me."
            "Instantly there's a dramatic change in Kylie, the expression on her face becoming twisted and hate-filled."
            kylie.say "How fucking DARE you!"
            kylie.say "I tell you that I love you, that I've worshipped you my whole life - and you turn around and reject me!"
            kylie.say "What kind of a monster are you?!?"
            python:
                g = "Bree"
                l = 0
                for i in GIRLS.values():
                    if i.love() > l:
                        l = i.love()
                        g = i.name
            kylie.say "What...is it [g] that you’re into, huh?"
            kylie.say "What in the hell does that nasty old hag have that I don't?!?"
            hero.say "Kylie, please..."
            kylie.say "Don't you 'please Kylie' me!"
            "Kylie scrapes her chair out from under the table and stands up, her hair flicking around as she does so."
            "Hands planted firmly on her hips, she looks down at me with disdain in her eyes."
            kylie.say "I really believed that you were like the guy in that story."
            kylie.say "But maybe I just need to figure this out in my head - so see you later, [hero.name]!"
            "With that, Kylie storms out of the library, seemingly intent on making as much noise and creating as big of a scene as possible."
            "I'm starting to wonder if I might have been too harsh on her, failed to see things from any perspective other than my own."
            "She was so young back then, and like most guys, I get super twitchy about the idea of someone that age being in any way sexual."
            "But for now, I really think I need to get out of the library and grab some fresh air."
            hide kylie
            return
        "I liked it":
            "A part of me knows that what she's just confessed to me was more than a little wrong and in more than a few ways."
            "But I still can't help getting all hot under the collar at the image of Kylie doing all of that while nobody knew she was even there."
            hero.say "The thought of you being there, doing that to yourself - it's pretty hot."
            "Kylie smiles broadly and giggles, fluttering her eyelids in a way that makes me feel even hotter."
            kylie.say "You think so?"
            kylie.say "And here I was, afraid that you'd think it was weird and creepy!"
            kylie.say "I mean, wasn't I the little sister?"
            "I swallow nervously at this question, wondering why she wants to labour that point."
            "Is she enjoying watching me squirm?"
            hero.say "You're not so little anymore!"
            hero.say "Urgh...I'm sorry, Kylie - you've gotten me in a bit of a mess."
            kylie.say "Don't worry about it, [hero.name] - it's kinda flattering that you're all mixed up over me!"
            kylie.say "And if you say that you'll take me on a date, then we can work on getting you straightened up nicely."
            hero.say "You...you want to go on a date with me?"
            kylie.say "Ooooh, [hero.name] - I thought you'd never ask!"
            kylie.say "I accept!"
            kylie.say "But I still want to know - What part of my little story did you like the most?"
            "Wait a minute - did I just agree to a date, or what?"
            "But while my mind is still trying to make sense of all that, my mouth is already answering Kylie's latest question without its help."
            menu:
                "I kinda liked thinking that you were watching":
                    hero.say "It's pretty mind-blowing to realise that there was someone watching the whole time."
                    hero.say "It adds a whole new dimension to the memory - makes it feel exciting all over again."
                    "Kylie smirks at my confession, leaning in closer than ever before."
                    kylie.say "It's pretty sexy, isn't it - thinking that someone might be watching?"
                    kylie.say "And today there's so much tech that can help make it happen."
                    kylie.say "You could spy on someone the whole time, and they'd never suspect a thing."
                    "I frown at Kylie, trying to fathom the source of her apparent fascination with spying and voyeurism in general."
                    hero.say "Sounds like you're some kind of expert when it comes to that kind of stuff."
                    kylie.say "Oh, it's nothing like that, really!"
                    "Kylie laughs, trying to wave away the notion, though she seems more edgy than before."
                    kylie.say "I only know so much because I'm considering law enforcement as a career, maybe even intelligence or espionage."
                "I liked how you described me":
                    hero.say "Ah, this is going to sound so like I'm up myself."
                    hero.say "But do you really think I’m like some hero from a romance novel?"
                    hero.say "Despite what you might think, that night wasn't much fun for me."
                    hero.say "I was cold, wet, and Alexis was riding my dick raw without caring at all."
                    hero.say "We were in a bad place - she was practically blackmailing me for sex by then..."
                    "Kylie gives me what I assume she thinks is a sympathetic smile, and pats my hand for a second."
                    kylie.say "Aww...don't you worry about Alexis anymore - that bitch is in your past now."
                    kylie.say "A rotten cheat like her couldn't appreciate a guy like you."
                    kylie.say "Not like I can..."
                "I liked how you described Alexis":
                    hero.say "Humour me on this one, okay?"
                    hero.say "But I was really turned on by how you were describing Alexis back there."
                    hero.say "I mean, it was totally like she wasn't even your sister, just some girl you were getting off on spying on!"
                    "Kylie's expression becomes stony, and she stares at me like I have steaming turds hanging out of my mouth."
                    kylie.say "Huh…?"
                    hero.say "It was the detail that you went into - the positions, her being soaked in cum, and all that."
                    hero.say "Almost like you were more turned on by the girl than the guy!"
                    "Kylie starts to bite nervously at her thumb, looking away as if she can't meet my eye."
                    kylie.say "I...I just remembered all of that, okay!"
                    kylie.say "It was so intense..."
                    kylie.say "I want to be the one being fucked like that...really!"
                    hero.say "Oh...sorry - I thought you got a thrill out of watching?"
                    "Suddenly and without warning, Kylie picks up the book she was studying when I arrived and stares at the open pages before her."
                    kylie.say "I...I hope you know that you're being pretty weird right now?"
                    kylie.say "It's not like I haven't seen Alexis naked before - probably more times than you have too."
                    kylie.say "We did live under the same roof, you know."
                    kylie.say "Why do guys always have to get Freudian over things - pervs!"
                    hero.say "Well, I'm sorry not to have lived up to your image of me as some kind of romantic hero..."
                    "At this, Kylie looks up from the book and sighs."
                    kylie.say "Maybe it's my fault for deciding who you were without actually knowing you for real?"
                    kylie.say "Maybe I need to get to know you better."
    kylie.say "Wait a minute - is that the time?!?"
    kylie.say "I have to get going!"
    hero.say "What, already?"
    hero.say "I feel like we only just started talking..."
    "Kylie seems to ignore me, standing up and pulling a folded piece of paper out of the pocket of her shirt."
    "She pauses just long enough to push it across the table to me and smile."
    kylie.say "Be sure to pick somewhere nice for our first date!"
    "And with that, she's gone."
    hide kylie
    "Left alone, I unfold the piece of paper, finding on it a phone number next to a heart with a smiley face inside."
    "Oh shit - I think I just agreed to call my ex-girlfriends little sister up and take her out on a date!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
