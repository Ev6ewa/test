label lavish_birthday_gift:
    show lavish
    if lavish.get_flag("birthdayknown"):
        hero.say "Happy birthday Lavish."
        lavish.say "How sweet, you remembered my birthday !"
    else:
        lavish.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ lavish.set_flag("birthdayknown")
    return

label lavish_gift_swimsuit:
    show lavish happy
    lavish.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if lavish.love >= 150 or lavish.sub >= 75:
        show lavish blush
        lavish.say "Thank you [hero.name] but you really wish me to wear that?"
        hero.say "Yes"
        lavish.say "But all men will be looking at me with lewd eyes..."
        hero.say "That's the point."
        $ lavish.set_flag("sexyswimsuit")
    else:
        show lavish angry
        lavish.say "Thanks but no thanks [hero.name], I am more classy than that..."
        lavish.say "This is vulgar."
        $ lavish.love -= 5
        $ lavish.sub -= 5
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
