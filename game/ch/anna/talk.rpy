label anna_talk_love:
    hero.say "I guess it's kind of a cliche - but what's your take on love, Anna?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "Of course I believe in love - how couldn't I with our baby growing inside of me?"
    else:
        anna.say "I think love is all around you - ha, there's another cliche!."
        anna.say "Seriously though, you should be able to love whoever you choose."
    $ anna.love += 1
    hide anna
    return

label anna_talk_sex:
    hero.say "You're a modern kind of girl, Anna - you're liberated when it comes to sex, right?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        "Anna's face shows a comically exaggerated amount of concern and gravity."
        anna.say "It's such a shame that the baby means my pussy's out of bounds for a while."
        anna.say "Ah well - I guess you'll just have to find somewhere else to fuck me!"
    elif anna.love < 40:
        "Anna blushes and refuses to meet my eye."
        anna.say "I don't think I know you well enough to feel comfortable talking about it."
        $ anna.love -= 1
    elif anna.love < 80:
        "Anna smiles and raises her eyebrows."
        anna.say "Oh yeah - my last serious partner was a girl...I swing both ways!"
    elif anna.love < 120:
        "Anna smiles, a little glimmer of naughtiness showing in her eyes as she does so."
        anna.say "Well, I'm not exactly what you'd call conservative..."
        "She adds in a whisper."
        anna.say "I kinda like it up the butt!"
    else:
        "Anna looks both ways to check that no one else is listening."
        anna.say "Don't tell anyone...but I kind of prefere it in the butt."
    $ anna.love += 1
    hide anna
    return

label anna_talk_politics:
    hero.say "Who's gonna get your vote the next time the elections come round, Anna?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "I used to just think that they were all shits."
        anna.say "But now that we're going to be parents, I'm scared for our kid's future with them running things."
    else:
        "Anna crosses her arms over her considerable chest and frowns."
        anna.say "They're all the same - just out to fuck us, and not in the good way, either!"
    hide anna
    return

label anna_talk_food:
    hero.say "I just can't think of what I want to eat tonight - how about you, Anna?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "Erm, I think the cravings have started."
        anna.say "I still want sushi, but now I can't have it without peanut butter or ice cream!"
    else:
        anna.say "I just love japanese food - sushi, ramen, whatever!"
        anna.say "It's all good!"
    hide anna
    return

label anna_talk_travels:
    hero.say "I'm tired of staring at the same four walls - wouldn't it be great to get away, Anna?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "I can't even walk across the street, my feet are so swollen!"
        "She flutters her eyelids at me, clearly wanting something."
        anna.say "Will you give me a foot-rub, [hero.name]?"
    else:
        "I can see the stars in Anna's eyes as she begins to daydream."
        anna.say "Oh, [hero.name] - wouldn't it be wonderful if the band went on a tour?"
    $ anna.love += 1
    hide anna
    return

label anna_talk_tv:
    hero.say "I feel like chilling out and watching some TV - any recommendations, Anna?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "I used to be crazily into horror movies."
        anna.say "But since we got pregnant, I just can't stomach them anymore."
    else:
        anna.say "Oh, it has to be horror movies, all the way."
        anna.say "The more likely to make me jump and scream, the better!"
    hide anna
    return

label anna_talk_sports:
    hero.say "There's just so much sport around these days, it kinda passes me by - how about you, Anna?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "I can't even see my toes right now, [hero.name], never mind touch them!"
    else:
        "Anna wrinkles her nose in apparent distaste for the subject."
        anna.say "Eww, no - I hate sports, and I am so not into jocks..."
    hide anna
    return

label anna_talk_fashion:
    hero.say "You never seem to be interested in the latest fashions, Anna."
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "I saw these really cool maternity tops with band logos on them the other day!"
    else:
        anna.say "I believe that fashion is a statement of who you are and what you think."
        anna.say "If you follow the heard, you're pretty much saying you're a sheep."
    hide anna
    return

label anna_talk_books:
    hero.say "I've never seen you with a book, Anna - do you read much?"
    show anna
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "I try to read in bed at night."
        anna.say "But I'm usually so burnt out that I fall straight to sleep."
    else:
        anna.say "Oh yeah, I just don't carry books around with me all the time."
        anna.say "I love reading philosophy, Spinoza is my favorite right now."
    hide anna
    return

label anna_talk_people:
    hero.say "Is it just me, Anna, or are most of the people in the world assholes?"
    show anna
    "Anna frowns a little at my comment."
    if anna.get_flag_value("pregnant") >= 9:
        anna.say "I used to think that people were basically good."
        anna.say "But now I have the baby to worry about, I keep seeing the worst in everyone."
    else:
        anna.say "Hey, [hero.name], that's a pretty negative thing to think!"
        anna.say "I think that everyone is basically good deep down, they just hide it well"
    hide anna
    return

label anna_talk_computers:
    hero.say "I just got a new laptop - are you into computers, Anna?"
    show anna
    anna.say "Oh no - I am not good with computers!"
    anna.say "It's like they know it too, and hold some kind of grudge against me."
    hide anna
    return

label anna_talk_music:
    show anna
    anna.say "I LOVE music, what's your favorite band?"
    menu:
        "Disturbed":
            hero.say "Disturbed are probably right up there, maybe my favourite."
            anna.say "Oh my god, David Draiman is so hot!"
            $ anna.sub += 1
        "One direction":
            hero.say "One Direction of course - what else!"
            anna.say "Eww...sorry I asked!"
            $ anna.love -= 1
        "Tenacious D":
            hero.say "And blasting forth with three part haromny!"
            hero.say "Tenacious D of course."
            anna.say "Oh man are so funny - I nearly pissed myself the first time I heard that album, honestly."
            $ anna.love += 1
        "Metallica" if "guitar" in hero.skills:
            hero.say "Metallica - no one else even comes close."
            anna.say "Best...metal...band...ever!"
            anna.say "Up to the Black album, at least."
            hero.say "I don't know - I have a soft spot for some of the tracks off of Load and Re-Load..."
            "Anna looks at me with an expression of mock outrage, grinning all the same."
            $ anna.love += 1
            $ anna.sub += 1
    hide anna
    return

label anna_talk_birthday:
    show anna
    hero.say "Hey - Happy birthday Anna!"
    anna.say "Aw, thanks [hero.name] - you remembered!"
    $ anna.love += 1
    hide anna
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
