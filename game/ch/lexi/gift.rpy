label lexi_birthday_gift:
    show lexi
    if lexi.get_flag("birthdayknown"):
        hero.say "Happy birthday Lexi."
        lexi.say "How sweet, you remembered my birthday !"
    else:
        lexi.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ lexi.set_flag("birthdayknown")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
