label shiori_talk_love:
    hero.say "Shiori, what do you think true love actually is?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        "I think that true love is having someone's child growing inside of you, nuturing it and bringing it into the world!"
    else:
        shiori.say "I think that love is being able to do anything for your man, no matter what he asks."
        shiori.say "It's having him dictate every aspect of your life..."
        $ shiori.sub += 1
    hide shiori
    return

label shiori_talk_sex:
    hero.say "What's your preference when it comes to sex, Shiori?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        "I hear that you can still have sex while you're pregnant..."
    else:
        shiori.say "Well...I can't imagine pleasure without at least a touch of pain..."
    $ shiori.sub += 1
    hide shiori
    return

label shiori_talk_politics:
    hero.say "Opinions on politics are like assholes everyone's got one - what are your politics, Shiori?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "I don't know anything about politics."
        shiori.say "But you won't vote for anyone that'd hurt our baby, would you, [hero.name]?"
    else:
        shiori.say "Oh, I wouldn't know anything about all of that!"
        shiori.say "I just nod and smile when people start talking about politics."
    hide shiori
    return

label shiori_talk_food:
    hero.say "Most people tend to eat out these days - how about you, Shiori?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "Since I got pregnant, I just can't stop eating!"
        shiori.say "If this keeps up, I'll be the size of a whale by the time the baby's due!"
    else:
        shiori.say "Oh no, I love making food!"
        shiori.say "I think that a woman should be able to cook a hearty meal for her man at the end of the working day."
    hide shiori
    return

label shiori_talk_travels:
    hero.say "I've always wanted to be able to take a year off and travel, you know - see the world."
    show shiori
    shiori.say "Not me, I'm happy as can be right were I am."
    $ shiori.love += 1
    hide shiori
    return

label shiori_talk_tv:
    hero.say "I need to start watching that new series on Netflix that everyone's talking about, tonight if I can."
    hero.say "You'v heard about it, right, Shiori?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "I'm usually so tired by the time I flop down on the sofa, I'm asleep in just a couple of minutes!"
    else:
        shiori.say "Nope - I mainly watch soaps, sometimes Reality TV shows."
    hide shiori
    return

label shiori_talk_sports:
    hero.say "All anyone's talking about in the office is the big game that's going to be on TV tonight."
    hero.say "Will you be watching it too, Shiori?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "I'm usually so worn out by the time I collapse on the sofa, I'm snoring away in just a few minutes!"
    else:
        shiori.say "Oh no, I don't watch sports on TV, sorry."
    hide shiori
    return

label shiori_talk_fashion:
    hero.say "You're always pretty well dressed when you walk into the office, Shiori."
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "Erm...nothing really fits me anymore, and I need to buy some maternity clothes, real soon!"
    else:
        shiori.say "Aw, thank you for saying so - I just love clothes and shopping!"
    hide shiori
    return

label shiori_talk_books:
    hero.say "Aletta was telling me about this pretty hardcore new adult novel that apparently everyone's reading."
    hero.say "Have you heard of it...or read it?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "No...but I did pick up this adorable book of baby names!"
    else:
        "Shiori giggles and shakes her head."
        shiori.say "Oh no...I don't read all that much."
        shiori.say "I think I might be too dumb to understand it!"
    hide shiori
    return

label shiori_talk_people:
    show shiori
    shiori.say "Mr.[hero.family_name], what do you think about children?"
    menu:
        "I hate them":
            hero.say "I really don't have much time for children."
            $ shiori.love -= 1
        "I love them":
            hero.say "I love them, Shiori - who doesn't?"
            $ shiori.love += 1
    hide shiori
    return

label shiori_talk_computers:
    hero.say "How are you coping with the latest software upgrades on your work computer, Shiori?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "I can't even think about computers, not when I already have babies on the brain!"
    else:
        shiori.say "I'm not really very good with computers, they make my brain hurt!"
    hide shiori
    return

label shiori_talk_music:
    hero.say "I was going to play some music - do you have any preferences, Shiori?"
    show shiori
    if shiori.get_flag_value("pregnant") >= 9:
        shiori.say "Could you play some classical music?"
        shiori.say "It's supposed to be good for the baby!"
    else:
        shiori.say "Not really - I don't listen to music all that much."
    hide shiori
    return

label shiori_talk_birthday:
    hero.say "Happy birthday, Shiori!"
    show shiori
    shiori.say "Ah you remembered - that makes me feel so special!"
    $ shiori.love += 1
    hide shiori
    return

label shiori_talk_subjects(subjects=[]):
    if game.get_flag_value('underinvestigation') and game.get_flag_value('workinvestigation') < 100:
        $ subjects.append('investigation')
    return

label shiori_talk_investigation:
    show shiori
    hero.say "Shiori, do you know anything about this investigation?"
    shiori.say "I'm sorry, Mr [hero.family_name], nobody talks to me about things like that."
    shiori.say "I'm sure it's just some kind of mistake and everything will be fine."
    hero.say "No, Shiori. Somebody set me up, and if I don't find out who and how, I'm going to get fired, and maybe go to jail!"
    shiori.say "Oh no, that's terrible, Mr [hero.family_name]! Is there anything I can do to help?"
    "I could ask Shiori to ask around, but she's about as subtle as those giant, milky melons she has. Maybe she could trade favors or something."
    "But on the other hand, I can't remember her ever getting anything right. Do I trust her to do this?"
    menu:
        "Ask her to help":
            $ shiori.set_counter('investigationcallback')
            hero.say "Maybe you could ask around the accountants and see if you can find anything out? Maybe if you...show off your assets."
            shiori.say "Whatever do you mean, Mr [hero.family_name]?"
            hero.say "I mean...ugh, never mind. Just ask around?"
            shiori.say "Sure, I'll ask around, sir. People like me!"
            hero.say "Thanks for the help. Let me know what you find out."
        "She would only mess it up":
            hero.say "I don't think there's anything you can do, Shiori. But thank you very much for the offer."
            shiori.say "Okay, sir. If you think of anything I can do, you'll let me know?"
            hero.say "I will."
    hide shiori
    return

label shiori_investigation_callback:
    play sound "sd/cell_vibrate.mp3"
    "My phone buzzes. It's Shiori. She said she'd get in touch, maybe she's got some good news?"
    hero.say "Shiori!"
    shiori.say "Hello, Mr [hero.family_name]. I asked around the accountants, like you asked. Can you believe one of them asked to see my boobs in exchange for information?"
    hero.say "No. I can't believe anyone would ask you that."
    "What I can't believe is that it was only one."
    hero.say "I hope you...well, did you get anything?"
    shiori.say "Yes, Sir! I got a whole bunch of information! I sent it to you in an email."
    "Huh, she really got something? That's great!"
    hero.say "Thanks, Shiori! I really owe you one!"
    shiori.say "I'm here to serve, Sir! Anything I can do for you makes me happy!"
    hero.say "Great! I'm going to look into this information now."
    "After I hang up, I look in my email. It's a dizzying array of accounting information, and none of it matches anything I already have."
    "It's really interesting, and it's going to take me hours to sort through it."
    "Unfortunately, as I will find out later, it's all fake, and it actually sets my investigation back."
    $ game.set_flag("workinvestigation", 10, mod='-')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
