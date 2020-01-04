label anna_birthday_gift:
    show anna
    if anna.get_flag("birthdayknown"):
        hero.say "Happy birthday Anna."
        anna.say "How sweet, you remembered my birthday !"
    else:
        anna.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ anna.set_flag("birthdayknown")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
