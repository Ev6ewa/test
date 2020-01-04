label kleio_desire_0:

    if kleio.love < 30:
        kleio.say "What do you want dumbass?"
    else:
        kleio.say "What's up [hero.name]?"

    return

label kleio_desire_1:

    if kleio.love < 60:
        kleio.say "You think because your not half bad looking you deserve something special?"
    else:
        kleio.say "You know, I think your not half bad looking..."

    return

label kleio_desire_2:

    if kleio.love < 90:
        kleio.say "Don't go thinking I'll fall for you just because you know how to smile."
    else:
        kleio.say "Stop smiling like that, it's embarassing."
    $ kleio.love += 1

    return

label kleio_desire_3:

    if kleio.love < 120:
        kleio.say "I love Disturbed, such a great band..."
    else:
        kleio.say "You should take me to a Distubed concert sometime."
    $ kleio.love += 1

    return

label kleio_desire_4:

    if kleio.love < 150:
        kleio.say "I feel nervous around you sometimes."
    else:
        kleio.say "Why isn't your dick in my pussy right now?"
    $ kleio.love += 1

    return

label kleio_desire_5:

    if kleio.love < 180:
        kleio.say "What do you say we go somwhere quiet?."
    else:
        kleio.say "I miss the feeling of you fucking me."
    $ kleio.love += 1

    return

label kleio_love_0:

    if kleio.love < 30:
        kleio.say "Get the hell away from me."
    else:
        kleio.say "What are you listening to those days?."
    $ kleio.love += 1

    return

label kleio_love_1:

    if kleio.love < 60:
        kleio.say "Fuck off."
    else:
        kleio.say "I am glad I met you, your quite the nice guy for a dork."
    $ kleio.love += 1

    return

label kleio_love_2:

    if kleio.love < 90:
        kleio.say "So you play World of Warcraft or what?"
    else:
        kleio.say "Fuck I am bored."
    $ kleio.love += 1

    return

label kleio_love_3:

    if kleio.love < 120:
        kleio.say "Is there a school for guys like you to learn how to talk to girls like me?"
    else:
        kleio.say "I know I am too good for you, but I might make an exception."
    $ kleio.love += 1

    return

label kleio_love_4:

    if kleio.love < 150:
        kleio.say "So are we a couple?."
    else:
        kleio.say "I think I might be falling for you..."
    $ kleio.love += 1

    return

label kleio_love_5:

    if kleio.love < 180:
        kleio.say "Yeah, yeah, I am in love, so what?."
    else:
        kleio.say "Please fuck me as soon as we are alone..."
    $ kleio.love += 1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
