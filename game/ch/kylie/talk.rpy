label kylie_talk_love:
    show kylie
    kylie.say "Love is the deep feeling of needing someone else more than air."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_sex:
    show kylie
    kylie.say "Sex..."
    kylie.say "Can we do it?"
    kylie.say "Do you want to do it?"
    kylie.say "You can fuck me here and know if you want..."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_politics:
    show kylie
    kylie.say "I am not that interested in politics."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_food:
    show kylie
    kylie.say "I like whatever you like."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_travels:
    show kylie
    kylie.say "The only place I wanna go is where you are."
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_tv:
    show kylie
    kylie.say "I don't really care about TV..."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_sports:
    show kylie
    $ result = randint(1,2)
    if result == 1:
        kylie.say "It's important to take care of your health."
    else:
        kylie.say "Do you want me to exercise more?"
        kylie.say "Do you like sporty chicks?"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_fashion:
    show kylie
    $ result = randint(1,2)
    if result == 1:
        kylie.say "Should I dress slutty?"
    else:
        kylie.say "Should I dress less slutty?"
    $ kylie.love += 1
    hide kylie
    return

label kylie_talk_books:
    show kylie
    kylie.say "Boring."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_people:
    show kylie
    kylie.say "You are the only one I need."
    kylie.say "And I am the only girl you'll need."
    hide kylie
    return

label kylie_talk_computers:
    show kylie
    kylie.say "Not interested."
    $ kylie.love -= 1
    hide kylie
    return

label kylie_talk_music:
    show kylie
    kylie.say "A little bit of this, a little bit of that."
    hide kylie
    return

label kylie_talk_birthday:
    show kylie
    hero.say "Happy birthday Kylie."
    kylie.say "Thank you [hero.name]."
    $ kylie.love += 3
    hide kylie
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
