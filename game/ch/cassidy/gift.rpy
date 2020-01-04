label cassidy_birthday_gift:
    show cassidy
    if cassidy.get_flag("birthdayknown"):
        hero.say "Happy birthday, Cassidy!"
        cassidy.say "How sweet, you remembered my birthday!"
    else:
        cassidy.say "How do you know my birthday?"
        hero.say "I didn't, it's just pure luck."
        $ cassidy.set_flag("birthdayknown")
    return

label cassidy_gift_swimsuit:
    show cassidy happy
    cassidy.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if cassidy.love >= 150 or cassidy.sub >= 75 or cassidy.get_status() == 'pet':
        show cassidy blush
        cassidy.say "Thank you [hero.name], but you really want me to wear that?"
        hero.say "Yes!"
        cassidy.say "That seems really...overly sexy, don't you think?"
        hero.say "That's the point. You deserve to show off your beauty."
        $ cassidy.set_flag("sexyswimsuit")
    else:
        show cassidy angry
        cassidy.say "No thanks."
        $ cassidy.love -= 5
        $ cassidy.sub -= 5
        $ hero.activity.set_flag('canceled')
    hide cassidy
    return

label cassidy_gift_collar:
    show cassidy happy
    hero.say "I have something for you."
    cassidy.say "Oh really? I hope it's not some cheap crap."
    hero.say "No, this is...well, maybe not expensive by your standards, but it wasn't cheap."
    "I hand the box to Cassidy, and she opens it, slowly. There is no small amount of avarice in her eyes until she sees the collar in the box."
    show cassidy normal
    "She pulls it out and holds it up, looking at it from every angle, clearly showing off the word 'Princess' etched into it."
    cassidy.say "You expect me to wear this?"
    if cassidy.get_status() == 'mistress':
        cassidy.say "No, this must be for you to wear, and the present is that I get to tug you around on a leash!"
        hero.say "No, that's not what I."
        cassidy.say "Put it on for me, [cassidy.heroname]!"
        "Oh, fuck. I clearly did not think this through, did I?"
        cassidy.say "Put this on right now, or we're going to march down to the piercing shop. We'll pierce your head and get the word [cassidy.heroname] tattooed right there above your public hair. Your choice."
        "I take the collar from her outstretched hands and look at it. This is humiliating."
        cassidy.say "Come on, I want to see you in it."
        "I'm about to say \"fuck this\", but then I remember she'll probably get me fired. So, I grit my teeth and put the collar on."
        cassidy.say "Oh. Yes, [cassidy.heroname], you certainly are a pretty, pretty Princess, aren't you?"
        "I look down at the floor, feeling the anger and humiliation burning at my cheeks."
        "Cassidy laughs at my discomfort."
        $ cassidy.sub -= 10
        cassidy.say "Okay, fine, you can take it off. But from now on, I'm going to call you Princess."
        hero.say "Oh God no."
        cassidy.say "Oh, it's the least I can do."
        "I take the collar off and put it back in the box."
        $ cassidy.set_flag('heroname', 'Bitch')
        cassidy.say "I'm going to save this, though. It might come in handy for some of our play, later on, [cassidy.heroname]."
    elif cassidy.get_status() == 'pet':
        hero.say "Yes, of course. You're my pet. I want everyone to know it."
        show cassidy sad
        cassidy.say "It's humiliating!"
        hero.say "Nonsense, it's beautiful. You {b}are{/b} a bit of a spoiled Princess, and this just advertises that fact a little bit."
        if cassidy.love < 160 or cassidy.sub < 75:
            cassidy.say "Please don't make me wear this."
            hero.say "This one is non negotiable. It doesn't hurt, and frankly you look beautiful in it."
            "She looks at me for a moment, then looks back at the collar in her hands. After a moment--reluctantly--she places it around her neck. The clasp clicks together with a loud, satisfying {b}snap{/b}."
            $ cassidy.set_flag('collared', True)
            hero.say "The only thing more beautiful than you in that collar will be you in that collar, on your knees."
            show cassidy blush
            cassidy.say "Yes, Master. As you wish."
            $ cassidy.sub += 10
        else:
            show cassidy happy
            cassidy.say "It's beautiful, Master. Thank you for this amazing gift."
            "She looks at me for a moment, then looks back at the collar in her hands. After a moment, she places it around her neck. The clasp clicks together with a loud, satisfying {b}snap{/b}."
            $ cassidy.set_flag('collared', True)
            hero.say "The only thing more beautiful than you in that collar will be you in that collar, on your knees."
            show cassidy blush
            cassidy.say "And I look forward to serving you that way, Master."
            hero.say "I'm a lucky, lucky man to get such a beautiful, talented sex slave like yourself. I guess what you put me through to get here was actually worth it."
            cassidy.say "It'll be worth it when your cock is in my mouth, Master, for sure."
            "She gives me a little wink."
    else:
        show cassidy angry
        cassidy.say "You cannot possibly be serious. Why the fuck would I wear such a thing?"
        "Cassidy throws the collar at me. It hits me right in the forehead, bouncing off and clattering to the floor."
        cassidy.say "Fuck you, [hero.name]."
        $ hero.activity.set_flag('canceled')
    hide cassidy
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
