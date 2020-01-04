label scottie_birthday_gift:
    show scottie
    if scottie.get_flag("birthdayknown"):
        hero.say "Happy birthday Scottie."
        scottie.say "How sweet, you remembered my birthday !"
    else:
        scottie.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ scottie.set_flag("birthdayknown")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
