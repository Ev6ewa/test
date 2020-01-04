label lavish_talk_love:
    show lavish
    if lavish.love <= 100:
        lavish.say "I hope to fall in love someday..."
    elif lavish.love <= 150:
        lavish.say "I think I am in love with someone."
    else:
        lavish.say "I love you so much..."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_sex:
    show lavish
    if not lavish.get_flag_value("sex"):
        lavish.say "Never been so interested in sex."
    else:
        lavish.say "Sex with you is so fantastic I think I'll end up addicted."
        $ lavish.sub += 1
    hide lavish
    return

label lavish_talk_politics:
    show lavish
    lavish.say "It's our responsibility as citizen to be aware of that!"
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_food:
    show lavish
    lavish.say "I do love a good meal in a nice restaurant."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_travels:
    show lavish
    lavish.say "I wanna see Europe one day."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_tv:
    show lavish
    lavish.say "I don't really care about TV, but I love going to the cinema."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_sports:
    show lavish
    lavish.say "Not so interested in sports, well except for health reasons."
    hide lavish
    return

label lavish_talk_fashion:
    show lavish
    $ result = randint(1,2)
    if not lavish.sub >= 75:
        lavish.say "I love to always look classy."
    else:
        if lavish.get_flag_value("sexyswimsuit"):
            lavish.say "I kind of start liking those slutty clothes you bought me."
            $ lavish.sub += 1
        else:
            lavish.say "I love to always look classy."
    $ lavish.love += 1
    hide lavish
    return

label lavish_talk_books:
    show lavish
    lavish.say "I am not really a bookish girl."
    $ lavish.love -= 1
    hide lavish
    return

label lavish_talk_people:
    show lavish
    lavish.say "Humanity is wonderful."
    hide lavish
    return

label lavish_talk_computers:
    show lavish
    lavish.say "Not interested."
    $ lavish.love -= 1
    hide lavish
    return

label lavish_talk_music:
    show lavish
    lavish.say "A little bit of this, a little bit of that."
    hide lavish
    return

label lavish_talk_birthday:
    show lavish
    hero.say "Happy birthday Lavish."
    lavish.say "Thank you [hero.name]."
    $ lavish.love += 3
    hide lavish
    return

label lavish_talk_subjects(subjects=[]):
    if game.get_flag_value('underinvestigation') and game.get_flag_value('workinvestigation') < 100:
        $ subjects.append('investigation')
    return

label lavish_talk_investigation:
    show lavish
    hero.say "Lavish, do you know anything about this investigation?"
    lavish.say "I'm sorry, I'm just an intern, that's way above my pay grade."
    lavish.say "So, did you do it?"
    hero.say "Steal the money? No! I'd never do anything like that."
    lavish.say "What's going on, then?"
    if 'cassidy_hold_meeting' in DONE:
        hero.say "Someone set me up, and I think the CEO's daughter and someone in accounting is involved."
        if game.get_flag_value('toldjeff'):
            hero.say "There's a guy over there named Jeff, I think he helped change the numbers."
        hero.say "Someone set me up. I don't know who, but whoever it is can make changes in our accounting systems."
    lavish.say "Hmm. I'll do some digging, maybe someone over there knows something. Some of the other interns and I go for drinks."
    hero.say "Okay, but be careful, Lavish. Whatever's going on is serious, and if you aren't careful you could be implicated too."
    lavish.say "Whatever, [hero.name]. I can find a new job -- I don't want to work at a place that does this to their employees."
    hero.say "Thank you, Lavish. I really appreciate it."
    lavish.say "Sure. I'll get in touch."
    $ lavish.set_counter('investigationcallback')
    hide lavish
    return

label lavish_investigation_callback:
    play sound "sd/cell_vibrate.mp3"
    "My phone buzzes. It's Lavish. She said she'd get in touch, maybe she's got some good news?"
    hero.say "Lavish!"
    lavish.say "Hey, [hero.name]. I did some asking around, like you asked. I may have something useful for you."
    hero.say "Spill it!"
    lavish.say "Everyone in accounting has been on edge the last few weeks. A lot of strange requests have come down from the top. Multiple audits, but also some secret budget changes."
    lavish.say "And apparently Dwayne himself has been taking meetings with an accountant named Jeff."
    lavish.say "Word is, Jeff used to be considered a bad employee, and everyone thought he was going to be fired."
    lavish.say "Then, all of a sudden, he ends up promoted. He's a director now, has his own office, and nobody knows who he actually reports to. It's hidden in the system."
    lavish.say "I'll send you some more details my friend dug up too. I hope it helps."
    hero.say "That is really helpful, Lavish! Thank you!"
    lavish.say "No problem, [hero.name]. I really hope you don't get fired. I'll miss you here."
    if lavish.love > 120:
        lavish.say "I mean, REALLY miss you."
    hero.say "Aw, that's sweet! Thanks! And I owe you one, Lavish!"
    lavish.say "Good luck!"
    $ game.set_flag("workinvestigation", 10 + max(lavish_love / 8, 5), mod='+')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
