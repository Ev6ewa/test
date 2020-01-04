label aletta_eat_a_burger_date:
    "When her burger arrives, Aletta looks less than impressed."
    "She wraps it in a napkin, as if disgusted at the thought of touching it."
    "And then proceeds to nibble at it while looking daggers in my direction the whole time."
    $ game.set_flag("datescore",5,1,"-")
    return

label aletta_date_buy_drink:
    "Aletta accepts her drink with a genuine smile."
    "She takes a sip and places it down before her."
    "Seems that it meets with her approval."
    return

label aletta_date_play_darts:
    "Aletta holds her darts a little awkwardly and throws them without much care."
    "It's almost as though she's trying to show willing."
    "But in reality she couldn't care less about our game."
    return

label aletta_date_pub_play_pool:
    "Almost as soon as she has the cue in her hand, Aletta becomes interested in the course of the game."
    "She's not a bad pool player, inexperienced for sure, but she learns quickly from her mistakes."
    "While I, on the other hand, make more as I get distracted from watching her as she leans over the table."
    $ game.set_flag("datescore",5,1,"+")
    return

label aletta_date_buy_a_round:
    "When I announce that I'm going to the bar and this round's on me, Aletta makes no big fuss about the matter."
    "She just shrugs and nods, as if she has no problem with it, but doesn't expect it all the same."
    "I guess that just comes from being a hard-nosed woman in a man's world."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
