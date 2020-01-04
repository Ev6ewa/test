label bree_talk_love:
    show bree
    $ result = randint(1,8)
    if bree.get_flag_value("collared") and bree.love >= 150:
        bree.say "I love you Master."
        bree.say "Will you have the time to fuck your little pet today?"
    elif result == 1:
        bree.say "I am ugly."
        if hero.charm >= 20:
            $ result = renpy.display_menu([("Agree",1),("Disagree",2),("Joke",3)])
        else:
            $ result = 1
        if result == 1:
            hero.say "On that we agree."
            "Bree looks hurt by my answer."
            bree.say "Jackass."
            $ bree.love -= 2
        elif result == 2:
            hero.say "I am pregnant."
            bree.say "What ???"
            hero.say "I thought we were stating impossible things."
            "Bree smiles at my pathetic joke."
            bree.say "Thx."
            $ bree.love += 1
        else:
            hero.say "You are insulting my tastes."
            bree.say "?"
            hero.say "I wouldn't have an ugly sex slave."
            bree.say "Lol"
            $ bree.sub += 1
    elif result == 2:
        bree.say "It's very easy to be cynical about love until you've had that instant connection. If you're lucky, it happens once in a lifetime."
        if hero.charm >= 20:
            $ result = renpy.display_menu([("Agree",1),("Disagree",2),("Joke",3)])
        else:
            $ result = 2
        if result == 1:
            hero.say "I hope it will happen to me sometime."
            $ bree.love += 1
        elif result == 2:
            hero.say "What a load of crap."
            "Bree looks very sad at my answer."
            $ bree.love -= 1
        else:
            hero.say "Your describing a sex slave's relationship to her master."
            "Bree blushes madly."
            $ bree.sub += 1
    elif result == 3:
        bree.say "Can't you say something deep and meanigfull for once ?"
        if hero.knowledge >= 10:
            $ result = renpy.display_menu([("Joke",2),("Be serious",1)])
        else:
            $ result = 2
        if result == 1:
            hero.say "You've gotta dance like there's nobody watching,\nLove like you'll never be hurt,"
            hero.say "Sing like there's nobody listening,\nAnd live like it's heaven on earth."
            bree.say "Okay, that will do."
            $ bree.love += 1
        else:
            hero.say "Bet you 100 quid you can't turn me hetero."
            "Bree looks pissed and leave me there."
            $ bree.love -= 1
    elif result == 4:
        bree.say "What is true love?"
        if hero.charm >= 20:
            if bree.love() >= 50:
                hero.say "True love is finding someone who matches you kink for kink."
                hero.say "I for once wnat to find a woman that I can slap and choke in bed but still cuddle in the morning."
                bree.say "It's oddly hot."
                $ bree.sub += 1
            else:
                hero.say "True love is your soul's recognition of its counterpoint in another."
                bree.say "It's a little cheesy but I like it."
                hero.say "I read it on a bumper sticker!"
                $ bree.love += 2
        else:
            hero.say "I really don't know."
    elif result == 5:
        bree.say "You know you're in love when you can't fall asleep because reality is finally better than your dreams."
        $ bree.love += 1
    elif result == 6:
        hero.say "If you can make a woman laugh, you can make her do anything."
        $ bree.love += 1
    elif result == 7:
        bree.say "Do you want a happy ending ?"
        hero.say "True love stories don't have endings."
        $ bree.love += 1
    else:
        bree.say "I know what's in store for me. No one will ever have passion for me."
        bree.say "People all around me will be falling in love, and making love, and getting married and having kids."
        bree.say "The closest thing I'll ever have to that is someone inviting me to their Christmas dinner because they feel guilty I might be spending the holiday alone."
        bree.say "Or if I'm lucky, my male counterpart, an obese man or a guy with a harelip, will invite me to coffee; and we'll pretend to love each other and tie the knot because we're so desperately afraid of growing old alone."
        if hero.charm >= 20:
            hero.say "I better get to eating more pizza then..."
            hero.say "I need to get fat quick"
            $ bree.love += 1
        else:
            hero.say "..."
            $ bree.love -= 1
    hide bree
    return

label bree_talk_sex:
    show bree
    $ result = randint(1,4)
    if bree.get_flag_value("collared") and bree.love >= 150:
        bree.say "I need your cock in my mouth Master."
        bree.say "Pretty please..."
    elif result == 1:
        bree.say "What do you think about kids?"
        hero.say "I think about makin' 'em all the time."
        if hero.charm >= 20:
            $ bree.love += 1
        else:
            $ bree.love -= 1
    elif result == 2:
        hero.say "What's the definition of a Yankee?"
        bree.say "Oh ! I know that one !"
        bree.say "Same thing as a 'quickie',only you do it yourself."
        $ bree.love += 1
    elif result == 3:
        hero.say "Give me a blow job!"
        bree.say "Can you be more romantic?"
        hero.say "Fine, give me a blow job in the rain."
        if bree.love() > 20 - hero.charm()/2:
            $ bree.love += 1
            $ bree.sub += 1
    elif result == 4:
        if not bree.get_flag_value("anal"):
            hero.say "Have you ever tried to... You know... Take it up the ass ?"
            if bree.love() > 120 - hero.charm()/2:
                bree.say "No, but do tell me when you get the urge, I'll be delighted."
                $ bree.sub += 1
                $ bree.love += 2
            elif bree.love > 80 - hero.charm()/2:
                bree.say "That's pretty personal [hero.name]..."
                $ bree.love += 1
            else:
                bree.say "Keep this kind of questions to yourself..."
                $ bree.love -= 1
        else:
            hero.say "Hi, I'm Andy. Wanna play with my Woody?"
            if bree.love > 80 - hero.charm()/2:
                "Bree giggles and gently slaps my hand."
                $ bree.love += 1
            elif not hero.charm >= 80 - bree.love():
                bree.say "Keep this kind of jokes to yourself please..."
                $ bree.love -= 1
    else:
        bree.say "It's not always about sex, sometimes the best type of intimacy is where you just lay back,"
        bree.say "laugh together at the stupidest things, hold each other, and enjoy each others' company."
        if bree.love() > 80 - hero.charm()/2:
            bree.say "But who am I kidding, I love sex."
            "She says that with a bright and playful smile on her face."
            $ bree.love += 1
        elif not hero.charm >= 20:
            hero.say "What a load of crap."
            $ bree.love -= 1
    hide bree
    return

label bree_talk_politics:
    show bree
    $ result = randint(1,4)
    if result == 1:
        bree.say "Whats Michelle Obamas favorite vegetable?"
        bree.say "Barackoli!"
        $ bree.love += 1
    elif result == 2:
        hero.say "Political language... is designed to make lies sound truthful and murder respectable,"
        hero.say "and to give an appearance of solidity to pure wind."
        bree.say "That's so true, who said that ?"
        if not hero.knowledge >= 10:
            hero.say "I don't remember"
            $ bree.love += 1
        else:
            hero.say "George Orwell"
            bree.say "I love that writer."
            $ bree.love += 2
    elif result == 3:
        bree.say "What is Barack Obamas favorite TV show?"
        bree.say "Game of Drones!"
        $ bree.love += 1
    else:
        bree.say "How is Barack Obama going to get Republicans to cross party lines and support health care reform?"
        bree.say "By giving their mistresses free breast implants!"
        $ bree.love += 1
    hide bree
    return

label bree_talk_food:
    show bree
    $ result = randint(1,3)
    if bree.get_flag_value("collared") and bree.love >= 150:
        bree.say "Your cum is the most tasty food in the world Master."
        bree.say "Give me some please..."
    elif result == 1:
        bree.say "If more of us valued food and cheer and song above hoarded gold, it would be a merrier world."
        $ bree.love += 2
    elif result == 2:
        bree.say "Ask not what you can do for your country. Ask what’s for lunch."
        $ bree.love += 1
    else:
        bree.say "All you need is love."
        bree.say "But a little chocolate now and then doesn't hurt."
        hero.say "LOL"
        $ bree.love += 1
    hide bree
    return

label bree_talk_travels:
    show bree
    $ result = randint(1,4)
    if result == 1:
        bree.say "The world is a book and those who do not travel read only one page."
    elif result == 2:
        bree.say "To travel is to live."
    elif result == 3:
        bree.say "It can hardly be a coincidence that no language on earth has ever produced the expression, 'As pretty as an airport."
    else:
        bree.say "Not all those who wander are lost."
        if hero.knowledge >= 10:
            hero.say "Oh, My God !\nDid you just quote the lord of the ring ?"
            bree.say "Dare I say yes ?"
            hero.say "Marry me !"
            if bree.love >= 120 - hero.charm()/2:
                bree.say "Be careful, I could say yes again."
                if bree.get_flag_value("sex"):
                    hero.say "As long as I can fuck and slap your ass for the rest of my life please do."
                $ bree.sub += 1
            "She giggles and walk away."
            $ bree.love += 2
    hide bree
    return

label bree_talk_tv:
    show bree
    bree.say "I don't watch tv that much."
    if bree.get_flag_value("porn"):
        bree.say "But I do love watching porn with you."
        $ bree.sub += 1
    hide bree
    return

label bree_talk_sports:
    show bree
    bree.say "You know, I work out a little, a girl has to."
    if bree.love >= 25:
        bree.say "It's not that easy to keep that houglass figure you seem to like so much, you weasel man."
    hide bree
    return

label bree_talk_fashion:
    show bree
    if bree.get_flag_value("collared") and bree.love >= 150:
        bree.say "I'll wear whatever you want Master."
    else:
        bree.say "I prefere to wear confortable clothes than fashionable ones."
    $ bree.love -= 1
    hide bree
    return

label bree_talk_books:
    show bree
    $ result = randint(1,5)
    if result == 1:
        bree.say "A room without books is like a body without a soul."
    elif result == 2:
        bree.say "Books are a uniquely portable magic."
    elif result == 3:
        bree.say "I can never read all the books I want; I can never be all the people I want and live all the lives I want."
        bree.say "I can never train myself in all the skills I want."
        bree.say "And why do I want?"
        bree.say "I want to live and feel all the shades, tones and variations of mental and physical experience possible in my life."
        bree.say "And I am horribly limited."
    elif result == 4:
        bree.say "I’m a book lover."
        bree.say "I’ve probably already fucked a whole library."
        $ bree.sub += 1
    else:
        hero.say "Have you red HG2G ?"
        bree.say "Don't Panic."
    $ bree.love += 1
    hide bree
    return

label bree_talk_people:
    show bree
    if bree.get_flag_value("collared") and bree.love >= 150:
        bree.say "If you really want me to fuck one of your friends I guess I'll do it Master."
        $ bree.sub -= 1
    else:
        bree.say "Sorry, I have things to do."
    $ bree.love -= 1
    hide bree
    return

label bree_talk_computers:
    show bree
    if not bree.get_flag_value("pregnant") >= 9:
        $ result = randint(1,4)
        if result == 1:
            bree.say "Computers are like Old Testament gods; lots of rules and no mercy."
        elif result == 2:
            hero.say "I think it's fair to say that personal computers have become the most empowering tool we've ever created."
            hero.say "They're tools of communication, they're tools of creativity, and they can be shaped by their user."
            bree.say "Yes but, man is still the most extraordinary computer of all."
            bree.say "Or should I say woman ?\nBecause a computer that freeze when it sees boobies is worth nothing."
            $ bree.love += 1
            if hero.knowledge >= 10:
                hero.say "Well, women don't have our transfer rate..."
                bree.say "Transfer rate?"
                hero.say "A single sperm has ~37.5MB of DNA information in it."
                hero.say "That means a normal ejaculation represents a data transfer of 1587GB in about 3 seconds."
                hero.say "I must have accidentally uploaded an insane amount of data to my laptop over the years."
                $ bree.love += 2
        elif result == 3:
            bree.say "Don't explain computers to laymen. Simpler to explain sex to a virgin."
            $ bree.love += 2
        else:
            bree.say "No one messes around with a nerd’s computer and escapes unscathed."
            $ bree.love += 2
    else:
        bree.say "Hey [hero.name], I discovered this great website to find advices on pregnancy."
        hero.say "What is it called?"
        bree.say "Preger-net"
    hide bree
    return

label bree_talk_music:
    show bree
    bree.say "You know, I listen to whatever is on the radio..."
    hide bree
    return

label bree_talk_birthday:
    show bree
    hero.say "Happy birthday Bree."
    bree.say "Thank you [hero.name]."
    $ bree.love += 5
    hide bree
    return

label bree_talk_date:
    show bree
    hero.say "Let's go on our date Bree."
    bree.say "Sure."
    $ bree.love += 1
    hide bree
    call date from _call_date_2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
