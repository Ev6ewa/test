label hanna_desire_0:
    if hero.fitness >= 10:
        hanna.say "I like how you take care of your body."
        $ hanna.love += 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_1:
    if hero.fitness >= 20:
        hanna.say "Those abs looks good on you."
        $ hanna.love += 1
    elif hero.fitness < 10:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_2:
    if hero.fitness >= 30:
        hanna.say "You look good today."
        $ hanna.love += 1
    elif hero.fitness < 20:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_3:
    if hero.fitness >= 40:
        hanna.say "Sometimes I wanna reap your shirt off."
        $ hanna.love += 1
    elif hero.fitness < 30:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_4:
    if hero.fitness >= 50:
        hanna.say "Can I see you naked?"
        $ hanna.love += 1
    elif hero.fitness < 40:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_desire_5:
    if hero.fitness >= 50:
        hanna.say "Can I see you naked?"
        $ hanna.love += 1
    elif hero.fitness < 40:
        hanna.say "I don't like men who don't take care of their body."
        $ hanna.love -= 1
    else:
        hanna.say "You should work out more."
    return

label hanna_love_0:
    "I kind of like your smile."
    $ hanna.sub += 1
    return

label hanna_love_1:
    "You look great in that shirt."
    $ hanna.sub += 1
    return

label hanna_love_2:
    "You should go topless."
    $ hanna.sub += 1
    return

label hanna_love_3:
    "I love your pecs."
    $ hanna.sub += 1
    return

label hanna_love_4:
    "Your abs are so sexy."
    $ hanna.sub += 1
    return

label hanna_love_5:
    "I wanna eat you alive."
    $ hanna.sub += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
