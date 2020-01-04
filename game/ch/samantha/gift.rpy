label samantha_birthday_gift:
    show samantha
    if samantha.get_flag("birthdayknown"):
        hero.say "Happy birthday Samantha."
        samantha.say "How sweet, you remembered my birthday !"
    else:
        samantha.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ samantha.set_flag("birthdayknown")
    return

label samantha_gift_swimsuit:
    show samantha happy
    samantha.say "Oh, [hero.name], is it for me?"
    "She unwrap the sexy swimsuit."
    if samantha.love >= 100 or samantha.sub >= 50:
        show samantha blush
        samantha.say "It's so pretty, thank you so much [hero.name]."
        $ samantha.set_flag("sexyswimsuit")
    else:
        show samantha annoyed
        samantha.say "I am sorry I can't wear that..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
