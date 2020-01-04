label lexi_talk_love:
    show lexi
    if lexi.love < 50:
        lexi.say "Love sucks..."
        lexi.say "That's why I love to do it so much."
        $ lexi.love -= 1
    else:
        lexi.say "I do hope that I will meet my prince in shining armor sometime."
        $ lexi.love += 1
    hide lexi
    return

label lexi_talk_sex:
    show lexi
    lexi.say "Sex on drugs is the best sex there is."
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_politics:
    show lexi
    lexi.say "What?"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_food:
    show lexi
    lexi.say "My favorite food is man milk, straight from the source."
    $ lexi.sub += 1
    hide lexi
    return

label lexi_talk_travels:
    show lexi
    lexi.say "I went to Vegas once, for work."
    $ lexi.love -= 1
    hide lexi
    return

label lexi_talk_tv:
    show lexi
    lexi.say "I love reality shows."
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_sports:
    show lexi
    lexi.say "What? No."
    hide lexi
    return

label lexi_talk_fashion:
    show lexi
    lexi.say "A girl needs to dress to attract the eye."
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_books:
    show lexi
    "Are you kidding me?"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_people:
    show lexi
    "People?"
    hide lexi
    return

label lexi_talk_computers:
    show lexi
    "Seriously?"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_music:
    show lexi
    "RnB I guess..."
    hide lexi
    return

label lexi_talk_birthday:
    show lexi
    "Thank you so much for remembering!"
    $ lexi.love += 3
    hide lexi
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
