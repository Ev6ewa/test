label scottie_desire_0:
    scottie.say "Oh, it's you...what do you want?"
    return

label scottie_desire_1:
    scottie.say "What do you want now?"
    scottie.say "You really think that you can talk to me?"
    return

label scottie_desire_2:
    scottie.say "Seriously, have you zero fashion sense?"
    $ scottie.love += 1
    return

label scottie_desire_3:
    scottie.say "Ah...you maybe you're not that bad after all."
    $ scottie.love += 1
    return

label scottie_desire_4:
    scottie.say "Fuck...like, do you ever brush your teeth?"
    scottie.say "Your breath smells like a fucking dead cat!"
    $ scottie.love += 1
    return

label scottie_desire_5:
    scottie.say "Sooo...what vibes do you get off of Audrey?"
    $ scottie.love += 1
    return

label scottie_love_0:
    scottie.say "Jesus, I wish I had your casual attitude towards cleanliness and hygeine!"
    $ scottie.love += 1
    return

label scottie_love_1:
    scottie.say "Don't ever try to come closer to me than that!"
    $ scottie.love += 1
    return

label scottie_love_2:
    scottie.say "Hey, Bree - have you seen Audrey anywhere around here?"
    $ scottie.love += 1
    return

label scottie_love_3:
    scottie.say "That Audrey chick can't shut the hell up about you."
    scottie.say "Me - I really don't see what all of the fuss is about."
    $ scottie.love += 1
    return

label scottie_love_4:
    scottie.say "..."
    $ scottie.love += 1
    return

label scottie_love_5:
    scottie.say "You know, you might not be as bad as I used to think."
    $ scottie.love += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
