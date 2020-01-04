label lexi_desire_0:

    if lexi.love < 30:
        lexi.say "What do you want dumbass?"
    else:
        lexi.say "What's up [hero.name]?"

    return

label lexi_desire_1:

    if lexi.love < 60:
        lexi.say "You think because your not half bad looking you deserve something special?"
    else:
        lexi.say "You know, I think your not half bad looking..."

    return

label lexi_desire_2:

    if lexi.love < 90:
        lexi.say "Don't go thinking I'll fall for you just because you know how to smile."
    else:
        lexi.say "Stop smiling like that, it's embarassing."
    $ lexi.love += 1

    return

label lexi_desire_3:

    if lexi.love < 120:
        lexi.say "I love Disturbed, such a great band..."
    else:
        lexi.say "You should take me to a Distubed concert sometime."
    $ lexi.love += 1

    return

label lexi_desire_4:

    if lexi.love < 150:
        lexi.say "I feel nervous around you sometimes."
    else:
        lexi.say "Why isn't your dick in my pussy right now?"
    $ lexi.love += 1

    return

label lexi_desire_5:

    if lexi.love < 180:
        lexi.say "What do you say we go somwhere quiet?."
    else:
        lexi.say "I miss the feeling of you fucking me."
    $ lexi.love += 1

    return

label lexi_love_0:

    if lexi.love < 30:
        lexi.say "Get the hell away from me."
    else:
        lexi.say "What are you listening to those days?."
    $ lexi.love += 1

    return

label lexi_love_1:

    if lexi.love < 60:
        lexi.say "Fuck off."
    else:
        lexi.say "I am glad I met you, your quite the nice guy for a dork."
    $ lexi.love += 1

    return

label lexi_love_2:

    if lexi.love < 90:
        lexi.say "So you play World of Warcraft or what?"
    else:
        lexi.say "Fuck I am bored."
    $ lexi.love += 1

    return

label lexi_love_3:

    if lexi.love < 120:
        lexi.say "Is there a school for guys like you to learn how to talk to girls like me?"
    else:
        lexi.say "I know I am too good for you, but I might make an exception."
    $ lexi.love += 1

    return

label lexi_love_4:

    if lexi.love < 150:
        lexi.say "So are we a couple?."
    else:
        lexi.say "I think I might be falling for you..."
    $ lexi.love += 1

    return

label lexi_love_5:

    if lexi.love < 180:
        lexi.say "Yeah, yeah, I am in love, so what?."
    else:
        lexi.say "Please fuck me as soon as we are alone..."
    $ lexi.love += 1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
