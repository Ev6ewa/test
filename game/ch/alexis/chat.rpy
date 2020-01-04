label alexis_desire_0:
    alexis.say "[hero.name], do you ever wish we could just go back to when we were in high school together?"
    alexis.say "You know, like have all that time over again?"
    menu:
        "Agree":
            hero.say "Yeah, it'd sure be nice to know then what I know now."
        "Disagree":
            hero.say "What - are you kidding me?!?"
            hero.say "I hated school, every damn minute of it until I got out of that place!"
            $ alexis.love -= 1
    return

label alexis_desire_1:
    alexis.say "What do you think of the cut on my top, [hero.name]?"
    alexis.say "I hope you don't think I'm showing off too much skin..."
    menu:
        "Admire the view":
            hero.say "N...no...no way, Alexis..."
            hero.say "I think it's very...flattering on you!"
            $ alexis.love += 1
        "Disapprove":
            hero.say "Now that you come to mention it, Alexis."
            hero.say "There is something to be said for a bit of modesty..."
            $ alexis.sub += 1
    return

label alexis_desire_2:
    alexis.say "Urgh, I'm so jealous of guys sometimes - you always grow into your looks."
    alexis.say "Like you, [hero.name] - you just seem to get better with age!"
    menu:
        "Be flattered":
            hero.say "Aww, I'm not really that good looking, Alexis - am I?"
            $ alexis.love += 1
        "Be offended":
            hero.say "Oh, thanks, Alexis!"
            hero.say "Am I supposed to take that as you're saying I was an ugly kid, or that I'm past it now?"
            $ alexis.sub += 1
    return

label alexis_desire_3:
    alexis.say "I've always been kinda jealous of Kylie."
    alexis.say "Younger siblings always seem to have an easier ride in life - don't they?"
    menu:
        "Disagree":
            hero.say "I think Kylie must have envied growing up in your shadow, Alexis."
            hero.say "She's a sweet girl, but she can't hold a torch to you."
            $ alexis.love += 1
        "Agree and compliments Kylie":
            hero.say "It's no wonder Kylie seems to waltz through life, Alexis."
            hero.say "Expecially when you consider that she was the one of you that got all of the looks!"
            $ alexis.sub += 1
            $ kylie.love += 1
    return

label alexis_desire_4:
    alexis.say "You know, back when I first called you up, I wasn't sure I was doing the right thing."
    alexis.say "But since then, I've come to realise it was one of the best decisions I could have made."
    menu:
        "Agree":
            hero.say "Well, I'm certainly glad that you didn't give in to your doubts, Alexis."
            hero.say "I feel like we were always supposed to hook up again, even after all this time."
            $ alexis.love += 1
        "Disagree":
            hero.say "Meh - I think I'm still back where you were when you called me, if I'm honest."
            hero.say "Things are never as good in the flesh as you remember them being."
            $ alexis.sub += 1
    return

label alexis_desire_5:
    alexis.say "Oh, [hero.name] - I can't believe that we're together again."
    alexis.say "I feel like there's nothing that could tear me away from you a second time!"
    menu:
        "Agree":
            hero.say "Whatever tried to tear us apart would have to deal with me hanging onto you too, Alexis!"
            $ alexis.love += 1
        "Disagree":
            hero.say "I dunno, Alexis - I feel like I'm just getting a nostalgia kick out of all of this."
            hero.say "Where's the fun in living in the past all of the time?"
            $ alexis.love -= 1
    return

label alexis_love_0:
    alexis.say "Hey, [hero.name] - you remember that dumb dance that was all the craze one summer back in high school?"
    "Alexis demonstrates what she claims to be the dance in question, though it seems to be more of an excuse to flash her breasts and backside at me."
    menu:
        "Flirt back":
            hero.say "Vaguely - but I think you need to come closer and show me that again."
            hero.say "Maybe come real close and show me..."
            $ alexis.love += 1
        "Blow her off":
            hero.say "Yes, I do."
            hero.say "And the only thing that could look more stupid than you did doing it back then is you doing it now!"
            $ alexis.sub += 1
    return

label alexis_love_1:
    alexis.say "Mmm...I think I have a kink in my shouders or something."
    alexis.say "[hero.name], would you be a lifesaver and give it a rub for me?"
    menu:
        "Give Alexis a massage":
            hero.say "Sure, just pull down the straps of your top - best to do the same with your bra too."
            hero.say "I'm sure I have some oil around here somewhere..."
            $ alexis.love += 1
        "Refuse to give Alexis a massage":
            hero.say "Oh no, I don't have any idea what I'm doing when it comes to that kind of thing."
            hero.say "I could make it ten times worse - you should really go see a professional."
            $ alexis.love -= 1
    return

label alexis_love_2:
    pass
    alexis.say "Brr...I'm really feeling cold, [hero.name]!"
    alexis.say "Can I cuddle up to you - just for the warmth?"
    menu:
        "Agree to let Alexis cuddle":
            hero.say "You should have said so sooner, Alexis."
            hero.say "Come over here, as close as you like - maybe I could give you a quick rub to get the blood flowing again?"
            $ alexis.love += 1
        "Refuse to let Alexis cuddle":
            hero.say "Erm, no...I don't think so - I like my personal space to stay uninvaded."
            hero.say "Maybe put on a sweater or something?"
            $ alexis.love -= 1
    return

label alexis_love_3:
    alexis.say "[hero.name]...you told me that you lived with two girls."
    alexis.say "But you never told me that they were both so hot..."
    menu:
        "Reassure Alexis":
            hero.say "What - you mean Bree and Sasha?!?"
            hero.say "I'm guessing you've never seen either of them first thing in the morning!"
            hero.say "Or had to use the bathroom after one of them either..."
            $ alexis.love += 1
        "Don't reassure Alexis":
            hero.say "Oh, I know exactly what you mean, you don't need to tell me about it!"
            hero.say "It's even harder when they're wandering around in their skimpy little pyjamas before going to bed!"
            hero.say "And when they decide to go for a dip in the pool - forget it!"
            $ alexis.sub += 1
    return

label alexis_love_4:
    alexis.say "You know, even a year ago, if someone had told me I'd be back in a relationship with you, I wouldn't have believed them!"
    alexis.say "I'd have called it a miracle...or a dream."
    menu:
        "Agree with Alexis":
            hero.say "Well, I hope that two people can share a dream."
            hero.say "Because I never want to be without you, awake or sleeping."
            $ alexis.love += 1
        "Disagree with Alexis":
            hero.say "Hah, what a dream - a nightmare, more like!"
            $ alexis.love -= 1
    return

label alexis_love_5:
    alexis.say "You know, part of me never truly believed that you could ever forgive me for what I did to you."
    alexis.say "But another part of me never stopped loving you, no matter what."
    menu:
        "Agree with Alexis":
            hero.say "I think the part of you that hurt me died a long time ago, Alexis."
            hero.say "And I love every other part of you that's come back to me."
            $ alexis.love += 1
        "Disagree with Alexis":
            hero.say "Sicky sweet little speech about how you feel, Alexis."
            hero.say "Problem is that's only how things are inside of your empty little head."
            $ alexis.sub += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
