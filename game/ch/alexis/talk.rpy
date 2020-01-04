label alexis_talk_love:
    hero.say "Do you even believe that love exists, Alexis?"
    show alexis
    alexis.say "People like to get all flowery and poetic about it."
    if alexis.get_flag_value("pregnant") >= 9:
        "Alexis puts her hands to her belly, her face showing a sudden surge of emotion."
        alexis.say "I didn't...but things like this can really change the way you look at things."
        $ alexis.love += 1
    elif alexis.love >= 50:
        alexis.say "I'd like to - but sometimes life makes you lose faith in happy endings."
        $ alexis.love += 1
    else:
        alexis.say "But they all really know it's really just a matter of getting what you want."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_sex:
    hero.say "What's sex all about for you, Alexis?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "I used to think that sex was just a weapon that I could use against people."
        alexis.say "But now I can see how wrong I was..."
    elif alexis.love >= 50:
        alexis.say "You can use it as a too...or like a weapon."
        alexis.say "To defend yourself or lash out at people..."
        $ alexis.sub += 1
    else:
        show alexis blush
        alexis.say "It's a transaction between two people, just like any other."
        alexis.say "I have something they want, so they have to offer me something in return."
    hide alexis
    return

label alexis_talk_politics:
    hero.say "Alexis, do you have a political stance?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "I never really engaged with politics before now."
        alexis.say "But with a kid on the way, I keep finding it pressing on my mind all the more."
    elif alexis.love >= 50:
        alexis.say "I find it hard to trust most people...so how can I trust a damn politician?"
    else:
        alexis.say "I'm a Libertarian - I believe in survival of the fittest, every man or woman for themselves."
        $ alexis.love += 1
    hide alexis
    return

label alexis_talk_food:
    hero.say "Any special dietary requirements, Alexis?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "I used to be real picky - but now I seem to want to eat anything put in front of me!"
        $ alexis.love += 1
    elif alexis.love >= 50:
        alexis.say "I've spent so long eating what I think people should believe I like..."
        alexis.say "I feel as though I don't remember what I really do like anymore."
        $ alexis.love += 1
    else:
        alexis.say "None - so long as it's up to my standards."
        alexis.say "Let's just say I won't be taken anywhere with less than four stars."
    hide alexis
    return

label alexis_talk_travels:
    hero.say "I think I have enough stashed away for a foreign holiday this year - any tips, Alexis?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "Don't ask me - I can't go too far afield in this condition!"
    elif alexis.love >= 50:
        alexis.say "All I really want is to be alone somewhere quiet...with someone that loves me."
        $ alexis.love += 1
    else:
        alexis.say "You need to book somewhere that's exclusive and fashionable."
        alexis.say "And not let the expense put you off making a real statement."
    hide alexis
    return

label alexis_talk_tv:
    hero.say "I'm not watching anything on TV right now, how about reccomending something, Alexis?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "I have the same problem now that I can't get out as much."
        alexis.say "Maybe we could find something to watch together?"
        $ alexis.love += 1
    elif alexis.love >= 50:
        alexis.say "I used to always end up watching TV alone...it still reminds me of being so lonely."
        $ alexis.love -= 1
    else:
        alexis.say "I don't watch too much TV...I have better things to do with my time."
    hide alexis
    return

label alexis_talk_sports:
    hero.say "You were always quite keen on sports, Alexis - or at least the sporting type when it came to guys..."
    hero.say "Did you keep that up after we left school?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "[hero.name], seriously - I already look like a football and I'm getting kicked all the time."
        alexis.say "The last thing I want is to watch a real one being kicked around!"
    elif alexis.love >= 50:
        alexis.say "I really don't like sports and I don't want to talk about it!"
        alexis.say "It's not a good subject for me...please let's talk about something else?"
        $ alexis.love -= 2
    else:
        alexis.say "No...no, I didn't."
        alexis.say "I don't...it's not something I want to talk about."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_fashion:
    hero.say "I don't think I've seen you in the same outfit twice, Alexis."
    hero.say "How can you afford it?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "Nothing fits me anymore."
        alexis.say "At one time it would have bothered me - but now I have bigger things to worry about."
    elif alexis.love >= 50:
        alexis.say "I've always used clothes kind of like armour...like a shield."
        alexis.say "If people only see your clothes, they tend to ignore the person beneath them..."
    else:
        alexis.say "I've never been shy of accepting genuine generosity from an admirer."
        alexis.say "If you value yourself, others will see value in you too."
        $ alexis.love += 1
    hide alexis
    return

label alexis_talk_books:
    hero.say "What's on your bookshelf, Alexis?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "Just stuff on caring for the baby."
    elif alexis.love >= 50:
        alexis.say "I read a lot of stuff to try and help with my demons."
        alexis.say "Sometimes it helps - but not always..."
        $ alexis.love += 1
    else:
        alexis.say "I don't have time for fiction."
        alexis.say "Most of what I read is self-help and books on psychology."
    hide alexis
    return

label alexis_talk_people:
    hero.say "You have a general philosophy for dealing with other people, Alexis?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "I hope there really are good people in the world, for the baby's sake."
    elif alexis.love >= 50:
        alexis.say "When people hurt me in the past, I always pushed them away."
        alexis.say "In the end I started doing the same to people that didn't want to hurt me too."
        alexis.say "Maybe, with your help, I can break that cycle?"
        $ alexis.love += 1
    else:
        alexis.say "People are basically shit - you need to keep that in mind in order to get what you want out of them."
    hide alexis
    return

label alexis_talk_computers:
    hero.say "Alexis - are you up to speed with computers, the internet and all that stuff?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "No, but I figure I can just wait for the baby to get a bit older and then start educating me."
    elif alexis.love >= 50:
        alexis.say "I know as much as anyone - but I'm no computer expert!"
    else:
        alexis.say "I know as much as I need to know in order to get by."
        alexis.say "And that's about all I care to know too."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_music:
    hero.say "Have you got a playlist of your favourite music, Alexis?"
    show alexis
    if alexis.get_flag_value("pregnant") >= 9:
        alexis.say "I want to listen to something soothing - I don't care what!"
    elif alexis.love >= 50:
        alexis.say "I've spent so long liking things to make people like me that I can't remember what I like for real!"
    else:
        alexis.say "No, but I like to have the latest tech to play it on."
    hide alexis
    return

label alexis_talk_birthday:
    hero.say "Happy birthday, Alexis!"
    show alexis
    if alexis.love >= 50:
        alexis.say "Oh, [hero.name] - you're the only person that remembered!"
        alexis.say "And that's the best gift I can imagine."
        $ alexis.love += 1
    else:
        alexis.say "Ah, how sweet of you to remember!"
        alexis.say "Now, what did you get for me?"
    hide alexis
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
