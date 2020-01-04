label kylie_desire_0:
    kylie.say "I'm bored."
    return

label kylie_desire_1:
    $ result = randint(1,3)
    if result == 1:
        kylie.say "I always thought you were too good looking for Alexis."
    elif result == 2:
        kylie.say "Do you think I should dress sexier?"
    else:
        kylie.say "I would do anything for you..."
    $ kylie.love += 1
    return

label kylie_desire_2:
    kylie.say "You're so smart..."
    $ kylie.love += 1
    return

label kylie_desire_3:
    kylie.say "You know what would be great?"
    kylie.say "Me bearing your child."
    kylie.say "Having a cute mini-you would be so awesome."
    $ kylie.love += 1
    return

label kylie_desire_4:
    kylie.say "When I’m around you, I kind of feel like I’m on drugs."
    kylie.say "Not that I do drugs."
    kylie.say "Unless you do drugs, in which case I do them all the time."
    kylie.say "All of them."
    $ kylie.love += 1

    return

label kylie_desire_5:
    kylie.say "Promise me you will never leave me or cheat on me."
    $ kylie.love += 1
    return

label kylie_love_0:
    kylie.say "I think we are soulmates."
    $ kylie.love += 1
    return

label kylie_love_1:
    kylie.say "What would you like me to be?"
    kylie.say "I can be anything or anyone for you."
    $ kylie.love += 1
    return

label kylie_love_2:
    kylie.say "I hate when we are not together."
    $ kylie.love += 1

    return

label kylie_love_3:
    kylie.say "Without you life would be intolerable."
    $ kylie.love += 1
    return

label kylie_love_4:
    kylie.say "What do you say we just get married right now."
    $ kylie.love += 1
    return

label kylie_love_5:
    kylie.say "You are probably the best guy ever."
    $ kylie.love += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
