label palla_birthday_gift:
    show palla
    if palla.get_flag("birthdayknown"):
        hero.say "Happy birthday Palla."
        palla.say "How sweet, you remembered my birthday !"
    else:
        palla.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ palla.set_flag("birthdayknown")
    return

label palla_gift_flowers:
    $ palla.set_flag('gaveflowers', True)
    show palla
    if palla.love < 40:
        "Palla looks at the flowers like I just handed her a can of worms."
        palla.say "Do you really think you're going to get on my good side with these?"
        "Then she rolls her eyes and looks away. When she thinks I'm not looking, she smells the flowers and smiles."
    elif palla.love < 80:
        "Palla looks at the flowers and cracks a very slight smile."
        palla.say "I hope you don't think you're going to get into my pants with just these?"
        hero.say "Oh no, you're much too bitchy for that."
        "Palla snorts, but doesn't look offended."
    elif palla.love < 120:
        "Palla looks at the flowers, then at me, then back at the flowers and smiles."
        palla.say "Good try, [hero.name] but it's going to take more than these to get...this."
        hero.say "See, I get a pretty smile and then you gotta be a bitch about it."
        palla.say "Yep, that's what you get with me."
    else:
        "Palla smiles brightly at the flowers."
        palla.say "Why [hero.name], does this mean you like LIKE me?"
        hero.say "Sure, when you're not being a bitch."
        "Palla laughs and flips me off."
    return

label palla_gift_sweets:
    $ palla.set_flag('gavesweets', True)
    show palla
    if palla.love < 40:
        "Palla looks at the sweets I just gave her and rolls her eyes."
        palla.say "If I eat this I'm going to have to work out an extra 30 minutes. Is that really what you're after?"
        hero.say "Sure, I like the thought of you all sweaty."
        "Her eyes widen for a moment. Then she catches herself and turns it into an exaggerated eyeroll."
        palla.say "What a creep."
    elif palla.love < 80:
        "Palla looks at the sweets. First she smiles, then sighs."
        palla.say "Seriously, now I'm going to need an extra half hour in the gym. You're not worth that."
        hero.say "I think you meant to say \"Thank you.\""
        palla.say "No, I meant to say \"Fuck you.\""
        hero.say "Yup, that's what I get for giving nice things to a world class bitch!"
        "Palla snorts, but doesn't disagree."
    elif palla.love < 120:
        "Palla looks at the sweets and cracks a smile, though she's clearly trying not to."
        palla.say "Oh fuck I know I said I like the romance and candy and flowers and crap but at the time I wasn't thinking about the extra half hour in the gym these things cost me."
        hero.say "Tell you what, I'll go to the gym and spot and count for you."
        palla.say "I bet you're the kind of asshole that will count 1, 2, 3, 4, 3, 3, 3, 4. No thanks."
        hero.say "Oh fuck yeah. I definitely like the idea of making you pump extra hard."
        show palla blush
        palla.say "Ok, that's enough of that, you creep!"
    else:
        "Palla smiles brightly at the sweets."
        palla.say "You better help me work off these extra calories later!"
        hero.say "On the dance floor or just on the floor?"
        show palla blush
        palla.say "On the dance floor. Yes. That's what I meant."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
