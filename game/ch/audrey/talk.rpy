label audrey_talk_love:
    hero.say "What's your take on love, Audrey?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "I know that I love having your baby inside of me."
        audrey.say "Almost as much as I like having you inside of me..."
    else:
        audrey.say "Love?"
        audrey.say "Hah - it's just a longer, more boring word for sex..."
        hero.say "Well, it's only one letter longer..."
        audrey.say "Yeah, but it's whole lot more boring."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_sex:
    hero.say "You have any words of wisdom when it comes to sex, Audrey?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "I can't say that being pregnant has affected my sex-drive."
        audrey.say "If anything, it's made me want it all the more..."
    else:
        audrey.say "Hmm...I always say that sex is the best way to spend an afternoon."
        audrey.say "But kinky sex...that's the best way to spend an entire weekend."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_politics:
    hero.say "What about you, Audrey - what are your personal politics?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "I couldn't care less about politics, except for when it comes to my rights and my body."
        audrey.say "There's only one man that I want having any say over what happens to my body..."
    else:
        audrey.say "I'm not that interested in politics."
        audrey.say "Well, except for office politics, especially when it involves the occasional blowjob."
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_food:
    hero.say "I'm thinking of slipping out to grab some lunch - what's your preference, Audrey?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "Everything's gotten screwed up with my appetite since I got pregnant."
        audrey.say "I got my cravings pretty bad, and all I want to eat is cock!"
    else:
        audrey.say "Well, I love my food as fresh from the source as I can get it."
        audrey.say "That's one of the reasons that I just love blowjobs."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_travels:
    hero.say "Where's that one dream trip to, Audrey - the one you've been planning your entire life?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "You better have a good babysitter lined up for when this kid arrives."
        audrey.say "As I still want to achieve my ambition for each and every continent..."
    else:
        audrey.say "I'd love to travel around the globe."
        audrey.say "That way I could finally achieve my ambition of being fucked at least once on every continent."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_tv:
    hero.say "Seen anything decent on TV recently, Audrey?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "I keep falling asleep on the couch in the evenings - maybe you could help me stay awake?"
    else:
        audrey.say "I don't really care about TV, at least when it comes to actually watching it."
        audrey.say "There's far better things to do on a couch..."
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_sports:
    hero.say "You always struck me as the sporty type, Audrey."
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "The bump might mean that I can't do some of the vertical exercises that I used to like so much."
        audrey.say "But I can still do a whole lot of stuff when I'm horizontal..."
    else:
        $ result = randint(1,2)
        if result == 1:
            audrey.say "Well, it's important to have a good stamina."
            audrey.say "If you want to be able to enjoy every night to the full."
        else:
            audrey.say "I've always loved being able to exercise - I think I like martial arts training the most of all."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_fashion:
    hero.say "You look pretty glamorous today, Audrey - you ever consider becoming a model?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "I wouldn't mind modelling some maternity wear for you."
        audrey.say "The modern stuff is pretty nice, especially the lingerie..."
    else:
        $ result = randint(1,2)
        if result == 1:
            audrey.say "Ew, no - those girls are so skinny it's freaky."
        else:
            audrey.say "No, I'm more of a purse kind of girl."
    $ audrey.love += 1
    hide audrey
    return

label audrey_talk_books:
    hero.say "Read any good books lately, Audrey?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "Have you read that Fifty Shades book?"
        audrey.say "Is there anything in there about kinky sex when you're pregnant?"
    else:
        audrey.say "Yeah, like I'm really going to go out of my way to do something that boring!"
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_people:
    hero.say "What are you up to this weekend, Audrey - catching up with your girlfriends?"
    show audrey
    if audrey.get_flag_value("pregnant") >= 9:
        audrey.say "I was supposed to be going to one of those pregnant mother's groups."
        audrey.say "But after I asked the other mothers-to-be how good of a fuck the guy that got them pregnant was..."
        audrey.say "I get the impression I won't be welcome back there any time soon."
    else:
        audrey.say "I don't really have a lot of female friends...girls kind of avoid me."
        audrey.say "Especially if they've got a boyfriend..."
    hide audrey
    return

label audrey_talk_computers:
    hero.say "know much about computers, Audrey?"
    show audrey
    audrey.say "Nah, nope, nada - not interested."
    $ audrey.love -= 1
    hide audrey
    return

label audrey_talk_music:
    hero.say "What's your thing when it comes to music, Audrey?"
    show audrey
    audrey.say "I'm quite ecclectic - I like a little bit of this, little bit of that."
    hide audrey
    return

label audrey_talk_birthday:
    show audrey
    hero.say "Happy birthday, Audrey - hope you have a good one."
    audrey.say "Thank you, - you're the only one in the office that remembered."
    $ audrey.love += 3
    hide audrey
    return

label audrey_talk_subjects(subjects=[]):
    if game.get_flag_value('underinvestigation') and game.get_flag_value('workinvestigation') < 100:
        $ subjects.append('investigation')
    return

label audrey_talk_investigation:
    show audrey
    hero.say "Audrey, do you know anything about this investigation?"
    audrey.say "I'm sorry, [hero.name]. Everyone is talking about it but nobody knows anything about it."
    audrey.say "Just that everyone says you stole a lot of money."
    hero.say "Steal the money? No! I'd never do anything like that."
    audrey.say "Then what hapened?"
    if 'cassidy_hold_meeting' in DONE:
        hero.say "Someone set me up, and I think the CEO's daughter and someone in accounting is involved."
        if game.get_flag_value('toldjeff'):
            hero.say "There's a guy over there named Jeff, I think he helped change the numbers."
        hero.say "Someone set me up. I don't know who, but whoever it is can make changes in our accounting systems."
    audrey.say "I wish I could help!"
    hero.say "Maybe you can. I bet there are people in accounting who know what's going on. Maybe you could be charming and dig up some information?"
    audrey.say "Sure, [hero.name], I'll try."
    hero.say "Thanks, Audrey! I owe you!"
    $ audrey.set_counter('investigationcallback')
    hide audrey
    return

label audrey_investigation_callback:
    play sound "sd/cell_vibrate.mp3"
    "My phone buzzes. It's Audrey. She said she'd get in touch, maybe she's got some good news?"
    hero.say "Audrey!"
    audrey.say "Hey, [hero.name]. I did some asking around, like you asked. But I got yelled at and they told me if I don't stay out of it I could be fired too."
    hero.say "Oh no! I'm so sorry, Audrey. I didn't mean for you to get in trouble."
    audrey.say "It's okay, [hero.name]. I just wish I could help, but...I need this job."
    hero.say "Okay. Thanks for trying!"
    audrey.say "Good luck!"
    $ game.set_flag("workinvestigation", max(audrey_love / 8, 5), mod='+')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
