label aletta_talk_love:
    hero.say "How about you, Aletta - do you believe in true love and all that stuff?"
    show aletta
    if aletta.get_flag_value("pregnant") >= 9:
        "Aletta rubs her swelling belly, smiling as she does so."
        aletta.say "I used to think it was all just chemicals screwing with the brain."
        aletta.say "That was before I had a symbol of our love growing, right here inside of me!"
        $ aletta.love >= 1
    else:
        aletta.say "Love is an outdated concept, nothing more than a chemical reaction in the most primitve parts of the human brain."
        aletta.say "Passion, now there's something much more interesting to me!"
        menu:
            "Agree":
                hero.say "Couldn't have said it better myself."
                hero.say "Who wants to be a slave to a chemical reaction when you could be one to passion instead!"
                "Aletta eyes me like a satisfied cat, seeming to know I'm trying to impress her, yet intrigued all the same."
                $ aletta.love += 1
            "Disagree":
                hero.say "That's not very romantic, now is it?"
                hero.say "I like to think that there's always the one out there, just waiting to sweep you off of your feet."
                aletta.say "Well, I hope you find the man of your dreams one day soon!"
    hide aletta
    return

label aletta_talk_sex:
    hero.say "We're all modern, emotionally mature adults here - so what do you say to us talking about sex?"
    show aletta
    if aletta.love < 40:
        "Aletta pulls down her glasses to regard me with one raised eyebrow."
        aletta.say "You really think that's something you want to chat to your boss about?"
        aletta.say "Because you could be opening up a whole new can of worms there."

    elif aletta.love < 80:
        "Aletta chuckles, shaking her head in amusement before she'll look me in the eye and answer the question."
        aletta.say "You should be careful what you ask, for [hero.name]."
        aletta.say "I really don't think you'd be able to handle a woman like me!"
    elif aletta.love < 120:
        "Aletta looks me up and down for a moment, like I'm a piece of meat that's been offered up to her."
        aletta.say "I like my men to be savage and strong, able to handle a woman of my calibre."
        aletta.say "I don't normally go for little shrimps like you!"
    else:
        "Aletta removes her glasses, chewing on one of the arms as she looks me up and down."
        aletta.say "You might be worth a try at some point...if I'm ever in genuine need."
        $ aletta.love += 1
    hide aletta
    return

label aletta_talk_politics:
    hero.say "Hey, Aletta - did you see what that jackass in the White House said this time!"
    show aletta
    if aletta.sub >= 75:
        aletta.say "If you say so, [hero.name] - you know more about that kind of thing that me!"
        $ aletta.sub += 1
    else:
        aletta.say "Politics doesn't interest me the slightest - it's just a pissing contest for impotent, middle-aged white men."
        menu:
            "Agree":
                hero.say "Yeah, it's a bit of a pasty sausage party all right!"
                aletta.say "Urgh...are you just saying that to try and impress me?"
                $ aletta.love -= 1
            "Disagree":
                hero.say "That's just the kind of thing a reactionary femi-Nazi would say!"
                aletta.say "Femi-what?!?"
    hide aletta
    return

label aletta_talk_food:
    show aletta
    aletta.say "Let's say I like to get my food directly from the source."
    hide aletta
    return

label aletta_talk_travels:
    show aletta
    aletta.say "I don't think that I need to travel very far to find what I crave."
    $ aletta.love += 1
    hide aletta
    return

label aletta_talk_tv:
    show aletta
    aletta.say "I am bored, goodbye."
    hide aletta
    return

label aletta_talk_sports:
    show aletta
    aletta.say "Speaking about sports, maybe you should work out a little more."
    hide aletta
    return

label aletta_talk_fashion:
    show aletta
    aletta.say "I could spend my whole life trying clothes on."
    hide aletta
    return

label aletta_talk_books:
    show aletta
    aletta.say "I don't read that much - print is a dead medium."
    hide aletta
    return

label aletta_talk_people:
    show aletta
    aletta.say "Don't you have something interesting to say ?"
    hide aletta
    return

label aletta_talk_computers:
    show aletta
    aletta.say "Not interested."
    hide aletta
    return

label aletta_talk_music:
    show aletta
    aletta.say "Go away now."
    hide aletta
    return

label aletta_talk_birthday:
    show aletta
    hero.say "Happy birthday Aletta."
    aletta.say "Thank you [hero.name]."
    $ aletta.love += 1
    hide aletta
    return

label aletta_talk_subjects(subjects=[]):
    if game.get_flag_value('underinvestigation') and game.get_flag_value('workinvestigation') < 100:
        $ subjects.append('investigation')
    return

label aletta_talk_investigation:
    show aletta
    hero.say "Can we talk about this investigation?"
    aletta.say "[hero.name], I really should not be talking to you about it."
    hero.say "But I'm being set up! And aren't I a good employee? Don't you want to get to the truth here?"
    show aletta sad
    "Aletta sighs."
    aletta.say "Look, [hero.name], there are rules. I have to follow those rules. We cannot discuss this."
    "Damn it."
    hero.say "Fine, but remember that I could go to jail over this. And I didn't steal the money."
    aletta.say "I know. I'm sorry this is happening."
    $ aletta.set_counter('investigationcallback')
    hide aletta
    return

label aletta_investigation_callback:
    play sound "sd/cell_vibrate.mp3"
    "My phone buzzes. It's Aletta. I answer it quickly, this could be important."
    aletta.say "Hi, [hero.name]. I'm sorry we couldn't talk earlier."
    hero.say "Thanks for calling. I really need some help here."
    aletta.say "I may have found something. Look into a subsidiary named Deewah Holdings, Limited. I think that has something to do with the money."
    aletta.say "And most important, that has nothing to do with you. If you can prove the money went through there and you didn't have any control, it might help."
    hero.say "Oh my God, Aletta! That's brilliant! Amazing! Thank you so much for the help! I love you for this!"
    if aletta.love > 160:
        aletta.say "I love you too!"
    hero.say "I owe you for this. If this all works out, anything you want."
    if aletta.love > 120 and aletta.sub < 5:
        aletta.say "Anything, really? I just might take you up on that..."
    else:
        aletta.say "Of course, [hero.name]. Happy to help."
    $ game.set_flag("workinvestigation", max(aletta_love / 8, 5), mod='+')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
