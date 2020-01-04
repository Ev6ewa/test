label mike_birthday_gift:
    show mike
    if mike.get_flag("birthdayknown"):
        hero.say "Happy birthday Mike."
        mike.say "How sweet, you remembered my birthday !"
    else:
        mike.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ mike.set_flag("birthdayknown")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
