label kleio_birthday_gift:
    show kleio
    if kleio.get_flag("birthdayknown"):
        hero.say "Happy birthday Kleio."
        kleio.say "How sweet, you remembered my birthday !"
    else:
        kleio.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ kleio.set_flag("birthdayknown")
    return

label kleio_gift_swimsuit:
    show kleio happy
    kleio.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if kleio.love >= 150 or kleio.sub >= 50:

        kleio.say "Thank you [hero.name]."
        $ kleio.set_flag("sexyswimsuit")
    else:
        show kleio annoyed
        kleio.say "Thanks but no thanks [hero.name], it's objectifying..."
        kleio.say "Even worse than being naked..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
