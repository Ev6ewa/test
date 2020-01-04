label audrey_birthday_gift:
    show audrey
    if audrey.get_flag("birthdayknown"):
        hero.say "Happy birthday Audrey."
        audrey.say "How sweet, you remembered my birthday !"
    else:
        audrey.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ audrey.set_flag("birthdayknown")
    return

label audrey_gift_swimsuit:
    show audrey happy
    audrey.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if audrey.love >= 150 or audrey.sub >= 50:
        show audrey blush
        audrey.say "It's so pretty, thank you [hero.name]."
        $ audrey.set_flag("sexyswimsuit")
    else:
        show audrey angry
        audrey.say "Thanks but no thanks [hero.name]."
        audrey.say "You think I would wear that?"
    return


label audrey_gift_collar:
    show audrey happy
    audrey.say "Oh, [hero.name], is it for me?"
    "She unwraps the slave collar."
    if audrey.sub >= 50:
        show audrey blush
        audrey.say "It's so pretty, thank you [hero.name]."
        $ audrey.set_flag("collared")
    else:
        show audrey angry
        audrey.say "Thanks but no thanks [hero.name]."
        audrey.say "You think I would wear that?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
