label sasha_birthday_gift:
    show sasha
    if sasha.get_flag_value("birthdayknown"):
        hero.say "Happy birthday Sasha."
        sasha.say "How sweet, you remembered my birthday !"
    else:
        sasha.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ sasha.set_flag("birthdayknown")
    return

label sasha_christmas_gift:
    show sasha
    hero.say "Merry Christmas Sasha."
    sasha.say "Thanks !"
    $ sasha.love += 2
    return

label sasha_valentine_gift:
    show sasha
    hero.say "Happy valentine's day Sasha."
    sasha.say "Thank you."
    $ sasha.love += 2
    return

label sasha_gift_swimsuit:
    show sasha happy
    sasha.say "Oh, [hero.name], is it for me?"
    "She unwrap the sexy swimsuit."
    if sasha.love >= 100 or sasha.sub >= 50:
        show sasha blush
        sasha.say "It's so pretty, thank you so much [hero.name]."
        $ sasha.set_flag("sexyswimsuit")
    else:
        show sasha angry
        sasha.say "Thnks but no thanks [hero.name], I am not that eager to fuel your fantasies."
    return


label sasha_gift_collar:
    show sasha
    sasha.say "Oh, [hero.name], is it for me?"
    "Sasha sits up, reaching for the wrapped gift."
    menu:
        "Hand it over":
            "I lean down and give her the box"
            $ sasha.love += 2
        "Tease her":
            "I lean back and look down at her with a smirk."
            hero.say "How bad do you want it?"
            if sasha.sub < 25:
                "Sasha blinks, then quirks a wry eyebrow at me."
                sasha.say "Not bad enough to stroke your ego to get them. The room's already crowded with you, me, and your ego as it is."
                "I snicker at her comment."
                hero.say "Touché."
                "Handing the box over, I enjoy seeing her smile at the gift."
                $ sasha.love += 1
            else:
                "Sasha blinks, then sticks her lower lip out at me playfully."
                sasha.say "So bad. Please can't I have it?"
                "She's so cute when she begs."
                "I hand the box over, pleased to see her happy smile."
                $ sasha.love += 2
                $ sasha.sub += 2
    "After a few moments of looking at the box she starts unpacking it and get the collar out."
    "I wish I could see her expression, but with her head lowered, those big dark eyes are impossible to read."
    if sasha.sub < 0:
        show sasha happy
        sasha.say "Oh! This is beautiful..."
        "Sasha says, unfastening the buckle and unwinding the collar from around the stems. She looks at me with a catlike grin."
        sasha.say "I think it'll just barely fit you. Give me the key and we can go play."
        "she purrs."
        hero.say "That wasn't what I had in mind."
        hero.say "Oh, the collar is for you. The key is for me."
        "Sasha snickers and shakes her head."
        sasha.say "I only do it the other way around. Nice try though."
        $ sasha.love -= 2
    elif hero.charm() + sasha.love() < 150:
        sasha.say "Wow, [hero.name]."
        "She looks at me a little uncertainly."
        sasha.say "This collar is gorgeous. Must have cost a pretty penny."
        "Looks like I presumed a little too much."
        hero.say "Nah, it didn't set me back much. Besides, it'll look awesome on you!"
        "I grin, voice a bit joking."
        hero.say "And it'll match everything you own."
        "I take the key from my pocket and hand it over."
        "Sasha grins happily and takes the key, then cinches the collar around her neck. I was right; it does look amazing on her."
        sasha.say "Thanks so much, [hero.name]! It's gorgeous."
        $ sasha.love += 2
    elif hero.charm() + sasha.love() >= 150 and sasha.sub() < 50:
        "Looks like Sasha's not ready to be a good pet after all."
        "Maybe she can be encouraged in that direction down the line."
        "I don't want her to think poorly of me for pushing, so I pull the key out of my pocket and hold it out to her."
        hero.say "I saw it and thought it would look amazing on you."
        "Sasha grins happily and takes the key, then cinches the collar around her neck. I was right; it does look amazing on her."
        sasha.say "Thanks so much, [hero.name]! It's gorgeous."
        "She gives me a flirtatious wink."
        sasha.say "Maybe you'll get a present from me pretty soon too."
        $ sasha.love += 2
        $ sasha.sub += 2
    else:
        sasha.say "Oh... it's beautiful. Do you have the key?"
        "I nod, dipping my fingers into my pocket to flash the key at her briefly before putting it away, already feeling a little thrill at how she's reacting to her gift."
        "And, of course, anticipation of putting it on her."
        sasha.say "Can I wear it now?"
        "I go over and take the collar, then step behind the couch to loop it carefully around her neck and buckle it."
        "She lets out a little sigh as she hears the lock click."
        $ sasha.love += 2
        $ sasha.sub += 5
        $ sasha.set_flag("collared")
        $ sasha.set_flag("status", "sex slave")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
