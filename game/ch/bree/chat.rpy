label bree_desire_0:
    if config.console == True and not bree.get_flag_value("consoleconfig"):
        if not bree.get_flag_value("collared"):
            bree.say "Do you think it would be right to use some kind of 'console command' to controle a girl's mind and try to have sex with her?"
        else:
            bree.say "Master...."
            bree.say "Could you not use console command and cheat ?"
        hero.say "eerrrrrh....."
        menu:
            "Apologize":
                hero.say "I am sorry Bree."
                if not bree.get_flag_value("collared"):
                    bree.say "You should be."
            "Don't apologize":
                hero.say "So what, it's not my fault it's so grindy to get you to bed."
                hero.say "Go complain to you game dev !"
                bree.say "..."
        $ bree.set_flag("consoleconfig",True)
    else:
        $ result = randint(1,3)
        if result == 1:
            if not bree.get_flag_value("collared"):
                bree.say "I was just thinking about you."
            else:
                bree.say "I love you Master."
            "I chat with Bree for a while."
            $ bree.love += 1
        elif result == 2:
            hero.say "I forgot to pay my internet bill, now I can't go online."
            bree.say "Don't you mean on youporn ?"
            hero.say "What a funny joke, Ha Ha Ha"
            bree.say "Don't be mad, you'll get your fix back at some point"
            hero.say "I know but still..."
            bree.say "And don't forget the saying : It is fruitless to become lachrymose because of scattered lacteal fluid."
            "Bree's joke manage to make me feel better"
            $ hero.fun += 1
            $ bree.love += 1
        else:
            hero.say "So, what do you do at the university exactly ?"
            bree.say "Well, I study about anything science related, but mostly biology and computer science."
            $ score = hero.knowledge()/20
            if score < 1:
                hero.say "That sound quite boring..."
                $ bree.love -= 1
            elif score == 1:
                hero.say "Wow, it sound pretty difficult."
                $ bree.love += 1
            else:
                hero.say "Computer science is a noble calling"
                bree.say "I want to be a scientist...\nThat's my dream since I was 3."
                bree.say "Science is the art of answering the tough questions, and questioning the easy answers."
                bree.say "That quote guide my student life."
                $ bree.love += 1
    return

label bree_desire_1:
    $ result = randint(1,3)
    if result == 1:
        "I catch Bree's gaze in my direction."
        bree.say "Stop looking at me like a golddfish in a bowl."
        $ score = hero.charm()/20
        if bree.get_flag_value("collared"):
            hero.say "Don't raise your voice when speaking to your Master pet."
        elif score < 1:
            hero.say "What a fucking bitch you are..."
            $ bree.love -= 1
        elif score == 1:
            hero.say "ok..."
        else:
            hero.say "You looked first, I just gave back what you sent me."
            $ bree.sub += 1
            $ bree.love += 1
    elif result == 2:
        hero.say "What are you thinking about?"
        if randint(1,2) == 1:
            bree.say "Singin' a song in my head."
            if hero.charm >= 20:
                hero.say "Well at least you're not listening to the voices."
                bree.say "Oh, they're singing."
                $ bree.love += 2
            else:
                $ bree.love += 1
        elif bree.love >= 100:
            bree.say "You."
            $ bree.love += 2
        else:
            bree.say "Nothing in particular."
    else:
        hero.say "Who ever called geeks anti-social, we have a social life!!!"
        hero.say "Haven't you ever played world of warcraft?"
        if hero.charm() >= 40 - bree.love():
            bree.say "I'm not anti-social"
            bree.say "I'm just not user friendly."
            $ bree.love += 2
        else:
            $ bree.love += 1
    return

label bree_desire_2:
    $ result = randint(1,2)
    if result == 1:
        if hero.charm >= 20:
            bree.say "Shall we shag now or shag later?"
            if hero.knowledge >= 10:
                hero.say "Yeah, baby, yeah!"
                $ bree.love += 1
                $ bree.sub += 1
            else:
                hero.say "What ?"
                $ bree.love -= 1
        else:
            bree.say "You know sometimes I think you would look great if you made an effort."
    else:
        if hero.charm >= 30 and hero.knowledge >= 30:
            bree.say "I wish I was an Ion so I could form an exothermic bond with you."
            $ bree.love += 2
        elif hero.knowledge >= 30:
            bree.say "If only your looks was as good as your brain..."
            $ bree.love += 2
        else:
            hero.say "I chat with Bree for a while."
            $ bree.love += 1
    return

label bree_desire_3:
    $ result = randint(1,2)
    if result == 1 and bree.love >= 120:
        bree.say "If I looked like you, I’d want to have sex with myself."
        bree.say "All the time."
        if hero.charm >= 20:
            hero.say "I know, why do you think I spend all this time in the toilets."
            $ bree.love += 1
        else:
            hero.say "Thank you I guess..."
            $ bree.love += 1
    else:
        bree.say "Today I caught myself smiling for no reason..."
        if bree.love >= 120 or hero.charm >= 30:
            if not bree.get_flag_value("collared"):
                bree.say "Then I realized I was thinking about you."
            else:
                bree.say "Then I realized I was thinking about you Master."
            $ bree.sub += 1
            $ bree.love += 2
        else:
            $ bree.love += 1
    return

label bree_desire_4:
    $ result = randint(1,2)
    if result == 1 or bree.love >= 120:
        bree.say "I have something to tell you about Alexis and Samantha ."
        hero.say "What ?!?"
        bree.say "So you failed..."
        bree.say "You wanna be really great?"
        bree.say "Have the courage to fail big and stick around."
        bree.say "Make them wonder why you're still smiling."
        bree.say "Because you know, there are fun oportunities in this very house."
        hero.say "Thank you."
        if hero.charm() >= 30:
            hero.say "Are you by any chance talking about a certain perky little blonde girl ?"
            bree.say "Maybe."
            $ bree.sub += 1
            $ bree.love += 1
        else:
            $ bree.love += 1
    else:
        "Bree seems to have something to say."
        $ result = renpy.display_menu([("Go talk to her",1), ("Wait for her to talk",2)])
        if result == 2:
            bree.say "I heard your bed squeeking all night, it looks like you didn't sleep well."
            hero.say "Yeah, I had a tough time last night."
            hero.say "Thank you."
            if bree.love() + hero.charm() >= 120:
                bree.say "Next time it happens you can come to my bed, it's comfy."
                hero.say "You shouldn't make that kind of jokes, you greatly overestimate my self-control."
                bree.say "I’m not looking for self-control."
                $ bree.sub += 1
                $ bree.love += 1
            else:
                $ bree.love += 1
        else:
            hero.say "Is your name Rapunzel, cause I need a girl who never leaves the bedroom and constantly wants me to pull her hair."
            if bree.love >= 120 or hero.charm >= 20:
                bree.say "I’m not Rapunzel, but I’ll still let you pull my hair."
                $ bree.love += 2
            else:
                bree.say "No, I am not"
                $ bree.love += 1
    return

label bree_desire_5:
    $ result = randint(1,2)
    if result == 1 and bree.get_status() != "girlfriend":
        bree.say "I’m living with a self talking creep who can't stop trying to hit on me."
        hero.say "I’m not hitting on you."
        bree.say "No?"
        if hero.charm >= 20:
            hero.say "Believe me, you’d know if I was hitting on you."
            hero.say "You wouldn’t be able to stop yourself from succumbing to my charms."
            $ bree.sub += 1
            $ bree.love += 1
        else:
            hero.say "No"
            $ bree.love -= 1
    else:
        bree.say "So, when are you planning to solve all that sexual tension building between us ?"
        $ result = renpy.display_menu([("Never",2), ("Soon",1)])
        if result == 2:
            hero.say "I’m not going to, I enjoy your suplice too much."
            $ bree.sub += 2
        else:
            hero.say "Soon, I have just been pretty busy lately."
        bree.say "Don't make me wait too much, I might get bored."
        $ bree.love += 1
    return

label bree_love_0:
    $ result = randint(1,4)
    if result == 1:
        hero.say "Looking cheerful today ?"
        bree.say "You know, I am always looking cheerful."
        $ bree.love += 1
    elif result == 2:
        hero.say "How are you today?"
        if not bree.get_flag_value("collared"):
            bree.say "Fine, you ?"
        else:
            bree.say "I am fine Master, and you?"
        if hero.charm >= 20:
            hero.say "Not bad when I woke up, stellar since I saw your smiling face."
            if not bree.get_flag_value("collared"):
                bree.say "Ain't he sweet."
            else:
                bree.say "You are too good to me Master."
            $ bree.love += 1
        else:
            hero.say "fine too."
            $ bree.love += 1
    elif result == 3:
        bree.say "Don't you get tired of starting almost every conversation in your life?"
        if hero.charm >= 20:
            hero.say "Not really, I like being in charge."
            $ bree.love += 1
            $ bree.sub += 1
        else:
            hero.say "Yeah, a little."
            $ bree.love += 1
    else:
        bree.say "Is the glass half empty or half full ?"
        $ result = renpy.display_menu([("Half full",1),("Half empty",2),("Neither, it's too big",3)])
        if result == 1:
            bree.say "Optimist then, good to know."
            $ bree.love += 1
        elif result == 2:
            bree.say "Wouldn't have thougt you were a pessimist."
            $ bree.love -= 1
        else:
            bree.say "Pragmatic man are you..."
            $ bree.love += 1
    return

label bree_love_1:
    $ result = randint(1,3)
    if result == 1:
        hero.say "So Bree, what do you do for fun ?"
        if bree.get_flag_value("collared") and bree.love >= 150:
            bree.say "I like sucking my Master's cock and be used as it pleases him."
            $ bree.sub += 1
        else:
            bree.say "I like reading books and watching romantic comedies."
            if not hero.charm >= 20:
                hero.say "I don't watch too many of those. The pretty woman, the pretty man, the first kiss, the break up, the make up, they drive off into the sunset. "
                hero.say "Everyone knows it's fake but they watch it like it's real life."
                $ bree.love -= 1
            elif hero.knowledge >= 10:
                hero.say "I love reading books too."
                bree.say "What kind ?"
                hero.say "Any kind actually."
                $ bree.love += 1
            else:
                hero.say "I love rom-coms too."
                $ bree.love += 1
    elif result == 2:
        "Bree is talking to herself."
        bree.say "I must not fear."
        bree.say "Fear is the mind-killer."
        bree.say "Fear is the little-death that brings total obliteration"
        bree.say "I will face my fear."
        bree.say "I will permit it to pass over me and through me."
        bree.say "And when it has gone past I will turn the inner eye to see its path."
        bree.say "Where the fear has gone there will be nothing."
        "She notice that I am listening, stops talking and waits for me to say something."
        $ result = renpy.display_menu([("Only Love will remain.",3),("Only I will remain.",2),("Only the Force will remain.",1)])
        if result == 1:
            bree.say "Wrong answer young padawan."
        elif result == 3:
            bree.say "A little corny don't you think ?"
        else:
            bree.say "Well, well, maybe we will make a Kwisatz Haderach out of you."
            hero.say "Sorry, I forgot my orange catholic bible."
            $ bree.love += 1
    else:
        hero.say "So Bree, what do you do for fun ?"
        if bree.get_flag_value("collared") and bree.love >= 150:
            bree.say "I like being pumped full of cum by my Master."
            $ bree.sub += 1
        else:
            bree.say "It might sound boring but I read a lot."
            if hero.knowledge >= 10:
                hero.say "Not boring at all, what do you read ?"
                bree.say "Mainly sci-fi, fantasy and mystery novels."
                $ bree.love += 1
                if hero.knowledge >= 10:
                    hero.say "Have you red anything by Christopher Moore ?\n it's both funny and mysterious."
                    bree.say "No, but I'll try, thanks."
                    hero.say "I can lend you some if you want."
                    $ bree.love += 1
            else:
                hero.say "Yeah, you are right, it's boring..."
                $ bree.love -= 1
    return

label bree_love_2:
    $ nbr = randint(1,4)
    if nbr == 1:
        hero.say "It's been so much fun since you've been here, I am almost glad Samantha and Ryan left."
        bree.say "I feel the same, we are so good together."
        if bree.love() > 20 - hero.charm()/2:
            bree.say "I mean the three of us..."
            hero.say "Of course."
            $ bree.love += 1
        $ bree.love += 1
    elif nbr == 2 and not bree.get_flag_value("birthdayknown"):
        hero.say "Hey Bree, when is your birthday ?"
        bree.say "It's on the [bree.birthday[1]] of [bree.birthday[0]]."
        bree.say "Are you planning on getting me a gift ?"
        hero.say "Maybe..."
        $ bree.set_flag("birthdayknown")
        $ bree.love += 1
    elif nbr == 3:
        bree.say "What's your favorite video game character."
        $ result = renpy.display_menu([("Ms Pac-Man.",1),("Samus.",2),("Mario.",3)])
        if result == 1:
            hero.say "Ms Pac-Man."
            hero.say "She is special. She's fun. She's cute. She swallows."
            if bree.love() >= 40 - hero.charm()/2:
                bree.say "Lol."
                $ bree.sub += 1
                $ bree.love += 1
            else:
                $ bree.love -= 1
        elif result == 2:
            hero.say "Samus."
            hero.say "She extinguished two breeds of dangerous predators, she blew up an entire planet, she was able to sneak into the mother ship of the space pirates only with a paralyzer (without her armor) and she's just so cool."
            hero.say "She decided to not give a damn about the Space Federation sending reinforcements and to blow up the whole place she was in because there was a major threat inside."
            bree.say "Nice choice."
            $ bree.love += 1
        else:
            hero.say "Mario."
            hero.say "Italian, Obsessed with mushrooms, wears a red hat, wears a pre-schooler uniform, saves princesses every time..."
            bree.say "What's not to like."
            $ bree.love += 1
    else:
        bree.say "Some people can't stand being alone. I love solitude and silence."
        bree.say "But when I come out of it, I'm a regular talking machine."
        bree.say "It's all or nothing for me."
        if hero.charm >= 20:
            hero.say "And it's pretty damn cute."
            $ bree.love += 1
        $ bree.love += 1
    return

label bree_love_3:

    if randint(1,2) == 1:
        hero.say "You snore."
        bree.say "I do not."
        if hero.charm() >= 20:
            hero.say "Oh yeah, you do."
            hero.say "Cute, like baby snores, but still snores by standard definition."
            $ bree.love += 1
        else:
            hero.say "Oh yes you do..."
            hero.say "Like a train or a pig."
            $ bree.love -= 1
    else:
        hero.say "I noticed that you are very good at giving advice."
        bree.say "That's just the trouble with me, I give myself very good advice too, but I very seldom follow it."
        $ bree.love += 1

    return

label bree_love_4:
    $ nbr = randint(1,2)
    if nbr == 1:
        hero.say "Have you ever had a dream that you were so sure was real?"
        bree.say "What if you were unable to wake up from that dream?"
        bree.say "How would you know the difference between the dream world, and the real one?"
        if not hero.charm >= 20:
            hero.say "What a stupid question..."
            $ bree.love -= 1
        elif not hero.knowledge >= 10:
            hero.say "Easy, in a dream you would be in my bed, waiting for me."
            $ bree.love += 1
        else:
            hero.say "Easy, you can't read in dreams."
            hero.say "In addition, in a dream I would be kissing you right now."
            $ bree.love += 2
    else:
        hero.say "I have something to confess Bree..."
        bree.say "I am listening."
        hero.say "Since you moved here, I feel like you became my first girl best friend."
        bree.say "Yeah, it's uncanny right..."
        $ bree.love += 1

    return

label bree_love_5:
    $ nbr = randint(1,2)
    if bree.get_flag_value("collared") and bree.love >= 150:
        bree.say "Could you please pump me full of your tasty cum Master?"
        bree.say "Please..."
    elif nbr == 1:
        bree.say "I think I'd miss you, even if we'd never met."
    else:
        bree.say "[hero.name], I feel like we have known each other for ever, like we are soulmates."
    $ bree.love += 1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
