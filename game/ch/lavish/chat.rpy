label lavish_desire_0:
    "Lavish is happily humming."
    $ lavish.love += 1
    return

label lavish_desire_1:
    if lavish.love > 75:
        $ result = randint(1,3)
        if result == 1:
            lavish.say "I love your smile."
        elif result == 2:
            lavish.say "I think someone on the scond floor is watching my ass when I pass by..."
            lavish.say "What a creep."
        else:
            lavish.say "I wish we worked together more."
        $ lavish.love += 2
    else:
        lavish.say "How are you doing today?"
        hero.say "Fine."
        $ lavish.love += 1
    return

label lavish_desire_2:
    lavish.say "I love working with you."
    $ lavish.love += 1
    return

label lavish_desire_3:
    lavish.say "Do you think you will be promoted soon?."
    $ lavish.love += 1
    return

label lavish_desire_4:
    $ result = randint(1,4)
    if result == 1:
        lavish.say "It's crazy how good you are at your job."
    elif result == 2:
        lavish.say "Do you think I should let my hair grow?"
    elif result == 3:
        lavish.say "What do you think about office relationships?"
    else:
        hero.say "How are you doing today Lavish?"
        lavish.say "Fine, thanks for asking."
    $ lavish.love += 1
    return

label lavish_desire_5:
    $ result = randint(1,2)
    lavish.say "I think I am in love with you."
    $ lavish.love += 1
    return

label lavish_love_0:
    lavish.say "Aletta is such a great boss."
    $ lavish.love += 1
    return

label lavish_love_1:
    lavish.say "What do you think about Shiori?"
    menu:
        "She's cute":
            $ lavish.love -= 1
            hero.say "I think she's cute."
        "She's very professional":
            $ lavish.love += 1
            hero.say "She's very good at her job and has a very professional attitude."
    return

label lavish_love_2:
    $ nbr = randint(1,2)
    if not lavish.get_flag("birthdayknown") and nbr == 1:
        hero.say "Hey Lavish, when is your birthday ?"
        lavish.say "It's on the [lavish.birthday[1]] of [lavish.birthday[0]]."
        lavish.say "Are you planning on getting me a gift ?"
        hero.say "Maybe..."
        $ lavish.set_flag("birthdayknown")
    else:
        lavish.say "I love my work, but when I was little I dreamed about being a princess."
        hero.say "Your childhood dreams are so cute."
    $ lavish.love += 1
    return

label lavish_love_3:
    lavish.say "You only make that job better and more fun."
    $ lavish.love += 1

    return

label lavish_love_4:
    lavish.say "I hope one day we will work together 24/7."
    $ lavish.love += 1

    return

label lavish_love_5:
    lavish.say "You are probably the best coworker ever."
    $ lavish.love += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
