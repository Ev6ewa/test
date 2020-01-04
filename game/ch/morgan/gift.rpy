label morgan_birthday_gift:
    show morgan
    if morgan.get_flag("birthdayknown"):
        hero.say "Happy birthday Morgan."
        morgan.say "How sweet, you remembered my birthday !"
    else:
        morgan.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ morgan.set_flag("birthdayknown")
    return

label morgan_gift_swimsuit:
    show morgan happy
    morgan.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if morgan.love >= 150 or morgan.sub >= 50:
        show morgan blush
        morgan.say "Thank you [hero.name]."
        $ morgan.set_flag("sexyswimsuit")
    else:
        show morgan angry
        morgan.say "Thanks but no thanks [hero.name], it's objectifying..."
        morgan.say "Even worse than being naked..."
    return

label morgan_gift_collar:
    show morgan
    morgan.say "Well, someone sure took their vitamins this morning!"
    morgan.say "Did you say your prayers too?"
    "Ignoring the gentle gibe and eighties pop-culture reference, I'm already reaching into my pocket as I reply."
    hero.say "Very funny, Morgan."
    hero.say "Well, you remember how I was guilty of having made that little mistake about you, back when we were in high school?"
    "Morgan shakes her head and snorts a quick laugh at my expense."
    morgan.say "[hero.name], how could I ever forget that you thought I was a guy for all that time?!?"
    morgan.say "But I thought we cleared all of that up before now?"
    morgan.say "God knows we've gotten up to things that should have proven I'm a girl since then!"
    "She leans in closer and treats me to a lascivious wink to make her point."
    "I frown in a good-natured way and make a wave to dismiss her comments in an amiable manner."
    hero.say "Thanks very much for stating the obvious, Morgan!"
    hero.say "No, this is more of a gesture to kind of say that's all behind us."
    hero.say "Maybe to say where we're going from here on as well..."
    "I can see that I've got her hooked by now, the intrigue written plainly on her angular little face."
    morgan.say "Come on, [hero.name] - don't leave a girl hanging!"
    "I oblige by holding up what I have in my hand, watching Morgan's expression intently as I do so."
    "At first, I honestly think that she mistakes it for a necklace or choker of some kind."
    "But then she looks a little more closely and realises that it's actually a blue leather dog-collar."
    "The only thing that marks it out as exceptional is the addition of a bronze pendant in the shape of a Venus symbol hanging from it."
    "Morgan looks up at me, puzzlement written all over her face."
    morgan.say "[hero.name], is that...is that a dog-collar?"
    "I shake my head as I try to explain."
    hero.say "Well, you could put it on a dog, certainly."
    hero.say "But this is really a collar for you, Morgan."
    hero.say "What's the matter, don't you like it?"
    "She still looks puzzled, as though my words haven't cleared the matter up for her."
    morgan.say "But...why would you want to put a collar on me?"
    hero.say "The pendant's one reason - to let everyone know that you're a girl."
    hero.say "But the main reason would be to let people know that you're mine, Morgan - that you're my little pet bitch!"
    "I hold out the collar, gesturing for her to take it."
    if morgan.sub < 75:
        show morgan angry
        "Her bemusement soon turns into visible annoyance and then anger."
        "Morgan slaps my hand away, sending the collar flying at the same time."
        "She rounds on me then, shoving a finger up and into my face."
        if morgan.get_flag_value("male") >= 75:
            morgan.say "So that's your perverted little thing, is it?"
            morgan.say "Well let me tell you something, mister - you're not man enough to put a collar on THIS little bitch!"
            "Her eyes are wide and her nostrils flaring as she glowers at me from below."
            "I've never seen Morgan as mad as this, and if I'm honest, it's really kind of scary."
            morgan.say "Why don't you take your damn collar and shove it up your ass, beore I do it for you?!?"
            $ morgan.love -= 20
            $ morgan.sub -= 10
            $ morgan.set_flag("male",10,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+10",2])
        elif morgan.get_flag_value("male") >= 25:
            morgan.say "Let me get this right, [hero.name]..."
            morgan.say "You expect me to put on a dog-collar and let you treat me like a pet?"
            "Morgan shakes her head and turns away from me for a moment, as if she needs to not see me right there and then."
            "She rounds on me a moment later, disappointment replacing puzzlement on her face."
            morgan.say "I really don't know whether to be more disgusted or disappointed, I honestly don't!"
            $ morgan.love -= 20
            $ morgan.sub -= 10
            $ morgan.set_flag("male",5,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+5",2])
        else:
            morgan.say "Eww...you want me to wear a creepy collar and pretend to be a dog?!?"
            morgan.say "[hero.name], I never knew you were secretly such a creep!"
            "Morgan recoils from me, as if she's afraid that touching me will pass on some unpleasant kind of contagion."
            morgan.say "I can't believe you'd think I'm THAT kind of girl!"
            $ morgan.love -= 20
            $ morgan.sub -= 10
    else:
        show morgan blush
        "I can see that I've piqued Morgan's curiosity, as she begins to eye the collar with visible anticipation."
        "Taking a gamble that I'm reading her mood correctly, I lean down and lift the collar to her throat."
        "She makes no effort to stop me, and so I fasten it in place, just tight enough so that she knows it's there."
        if morgan.get_flag_value("male") >= 75:
            $ morgan.set_flag("collared")
            $ morgan.set_flag("status", "sex slave")
            hide morgan
            show morgan blush
            "I can hear Morgan's breathing become that much heavier as I finish fastening the collar in place."
            "She keeps glancing at me sideways, almost like she wants me to see her."
            "But at the same time, she seems not to want to be seen to want it either."
            "She puts her hands up to feel at the collar, almost pulling on the leather strap for the sake of feeling the sensation it causes."
            "Morgan is silent the whole time, but I swear I can almost feel the heat coming off of her."
        elif morgan.get_flag_value("male") >= 25:
            $ morgan.set_flag("collared")
            $ morgan.set_flag("status", "sex slave")
            hide morgan
            show morgan blush
            "I hear the fluttering of Morgan's breath as the collar is finally in place and I remove my hands."
            "She reaches for it almost instantly with one hand, her fingers closing around the leather tightly."
            "At the same time, I see her other hand go unconsciously first to her breasts and then to her groin."
            "It's almost as though she's forgotten that there are other people present in her fascination with the collar."
            "Or else it's somehow made her not care in the slightest that they can see her becoming noticeably aroused..."
        else:
            $ morgan.set_flag("collared")
            $ morgan.set_flag("status", "sex slave")
            hide morgan
            show morgan blush
            "Morgan can hardly keep herself still as I fasten the collar and step back to admire my handiwork."
            "She bounces on the spot and flaps her hands in sheer excitement, not seeming to care that people are watching her the whole time."
            "When she turns to face me, she has a huge grin on her face and looks delighted with the course of events."
            "Even I have to admit to being surprised when she lolls her tongue out and holds up her hands beneath her chin."
            "I realise a moment later, when she makes a barking sound, that she's actually imitating a dog!"
        $ morgan.sub += 10
        $ morgan.set_flag("male",10,mod="-")
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-10",2])
        "Finally relieved of the burden of carrying the collar around in my pocket, I feel like I can relax."
        "For better or worse, Morgan knows all about it now."
        "And I have the feeling that it's going to change our relationship to quite some degree."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
