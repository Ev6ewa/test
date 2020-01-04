label scottie_talk_love:
    hero.say "You believe in love, right Scottie?"
    show scottie
    scottie.say "Love...seriously?"
    scottie.say "Could you be any more more boring?"
    $ scottie.love -= 1
    if scottie.sub <= 25:
        scottie.say "The only thing you should worry about loving is having my cock inside of you!"
    if scottie.sub >= 75:
        scottie.say "I know that I love it when you give me an order, mistress!"
    hide scottie
    return

label scottie_talk_sex:
    hero.say "What about sex, Scottie - are you spontaneous, or do you like to plan ahead?"
    show scottie
    scottie.say "I'm cool with whenever and wherever you want babe."
    if scottie.sub <= 25:
        scottie.say "You better put out when and where I say, bitch!"
    if scottie.sub >= 75:
        scottie.say "Yes, mistress...ready and willing to please."
    hide scottie
    return

label scottie_talk_politics:
    hero.say "I'm not sure who to vote for in the local elections this year."
    show scottie
    scottie.say "Meh, I'm not that interested in politics and all that kind of stuff."
    $ scottie.love -= 1
    if scottie.sub <= 25:
        scottie.say "What are you wasting your time on that stuff for?"
        scottie.say "If I wanted you to have an opinion on politics, I'd have told you what it should be already!"
    if scottie.sub >= 75:
        scottie.say "I wouldn't know about any of that...would you like to tell me who to vote for?"
    hide scottie
    return

label scottie_talk_food:
    hero.say "I'm getting kinda hungry."
    show scottie
    scottie.say "Me too - say, you wanna cook something for me?"
    if scottie.sub <= 25:
        scottie.say "Well don't be a dumbass - make us something or else order it in!"
        scottie.say "God, I have to tell you to do every damn thing."
    if scottie.sub >= 75:
        scottie.say "You should have told me earlier!"
        scottie.say "I could knock you something up myself, or should I order you take-out?"
    hide scottie
    return

label scottie_talk_travels:
    hero.say "I really wonder if I'm missing out by not travelling more..."
    show scottie
    scottie.say "Hey, baby - I can take you someplace fun without leaving the room!"
    $ scottie.love += 1
    if scottie.sub <= 25:
        scottie.say "You're going nowhere without me or my say so!"
    if scottie.sub >= 75:
        scottie.say "Are you plannning to go away?!?"
        scottie.say "Please, take me with you - don't leave me!"
    hide scottie
    return

label scottie_talk_tv:
    hero.say "I fancy watching a documentary tonight - how about you?"
    show scottie
    scottie.say "I love that show where they fix cars."
    scottie.say "You know, the one with the guy that's got the beard and the other with the hair?"
    if scottie.sub <= 25:
        scottie.say "If by that you mean a show where guys buy a car, fix it and then sell to other guys, then okay."
        scottie.say "Anything else and you can forget it."
    if scottie.sub >= 75:
        scottie.say "Whatever you want."
        scottie.say "If I like your choice, then great."
        scottie.say "If not, then I can just keep my mouth shut the whole time."
    hide scottie
    return

label scottie_talk_sports:
    hero.say "I'm thinking of taking up some sports classes at the gym."
    show scottie
    scottie.say "Good idea - you need to stay in shape, can't let that body of your go getting all flabby now."
    if scottie.sub <= 25:
        scottie.say "You can exercise here, in front of me."
        scottie.say "It's cheaper, and plus, I get a free floor-show."
    if scottie.sub >= 75:
        scottie.say "You don't need to shape up - you're perfect, just as you are."
    hide scottie
    return

label scottie_talk_fashion:
    hero.say "What do you think of this season's trends, Scottie?"
    show scottie
    scottie.say "Don't care - as far as I'm concerned, the less a girl wears the better."
    $ scottie.love += 1
    if scottie.sub <= 25:
        scottie.say "What do you care?"
        scottie.say "If I like something, then you wear it."
        scottie.say "If not, then you don't."
        scottie.say "Simple as."
    if scottie.sub >= 75:
        scottie.say "You look great in whatever you wear!"
    hide scottie
    return

label scottie_talk_books:
    hero.say "What's your favourite book, Scottie?"
    show scottie
    scottie.say "Never read one in my life - books are so boring it's unreal."
    $ scottie.love -= 1
    if scottie.sub <= 25:
        scottie.say "I don't want you reading anything without my say so from now on."
        scottie.say "Can't have you getting any crazy ideas into your head."
    if scottie.sub >= 75:
        scottie.say "I don't read because big words always confuse me..."
    hide scottie
    return

label scottie_talk_people:
    hero.say "What's your philosophy for getting on with people, Scottie?"
    show scottie
    scottie.say "I don't have one."
    scottie.say "Fuck them all, that's what I say!"
    if scottie.sub <= 25:
        scottie.say "Fuck other people - and you shouldn't be talking to anyone, unless I say you can!"
    if scottie.sub >= 75:
        scottie.say "I'm scared that people will see through my bravado and say mean things that I won't understand."
    hide scottie
    return

label scottie_talk_computers:
    hero.say "You much into computers, Scottie?"
    show scottie
    scottie.say "Nah...not interested."
    $ scottie.love -= 1
    if scottie.sub <= 25:
        scottie.say "What the hell are you doing on the internet, anyway?"
        scottie.say "There are other guys on there - so you keep off of it, you hear?"
    if scottie.sub >= 75:
        scottie.say "Computers scare me, because I'm afraid that I'll break them..."
    hide scottie
    return

label scottie_talk_music:
    hero.say "What's on your playlist, Scottie?"
    show scottie
    scottie.say "Gotta be metal, all the way baby!"
    if scottie.sub <= 25:
        scottie.say "Metal, metal and more metal - so you'd better get to like it!"
    if scottie.sub >= 75:
        scottie.say "I like K-Pop, but I always say metal, because I'm scared people will call me gay..."
    hide scottie
    return

label scottie_talk_birthday:
    show scottie
    hero.say "Happy birthday, Scottie."
    scottie.say "hey, thanks babe!"
    $ scottie.love += 3
    hide scottie
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
