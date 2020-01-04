init python:
    Event(**{
        "name": "jack_event_01",
        "label": ["jack_event_01"],
        "priority": 500,
        "duration": 1,
        "game_conditions":{"room":["livingroom"],"hours":(14,17),"days_played":14, "days":"67", "flag_female":0},
        "do_once":True,
        "quit": True
        })

label jack_event_01:
    "I hear a knocking at the door and go there to open it."
    scene bg black
    with fade
    scene bg house
    show jack normal
    with wiperight
    "On the other side of the door stands my friend Jack."
    show jack happy
    jack_say "Heeey, [hero.name]!"
    jack_say "How’s it goin!?"
    scene bg livingroom
    jack_say "Sweet place you got here."
    jack_say "It’s perfect!"
    hero.say "Perfect?"
    hero.say "Perfect for what?"
    show jack normal
    jack_say "Running a game, of course!"
    jack_say "We could even play pool side."
    jack_say "Just roll the dice on the edge and stuff, man!"
    hero.say "Haha, yeah, that might be interesting, but why are you bringing this up, now?"
    jack_say "O-oh, I didn’t tell ya? Remember Spencer from the game store?"
    hero.say "Oh, right, the really sweaty guy."
    hero.say "Stunk of B.O."
    jack_say "Yeah, well, he went all neckbeard on me and got the game kicked out of the place."
    jack_say "And, you know, I don’t really have a good place to play and no one else in my group wants to play anywhere else and-"
    "He just keeps rambling on."
    "I know he’s got to get to a point sometime, but he just won’t stop talking."
    "*door opens*"
    "His grievances must have been loud enough to wake the dead, because Bree comes walking out of her room and joins in."
    hide jack
    show bree sleep
    bree.say "Hey, what’s up? Sounds like someone’s really bummed out."
    hero.say "Oh, hey, Bree."
    hero.say "This is Jack. He’s a friend of mine and,"
    hide bree
    show bree sleep at left
    show jack perv at right
    "Jack jumps in, practically salivating."
    jack_say "Holy crap dude, this is your roommate!?"
    hero.say "Y-yeah, one of them."
    jack_say "Wow, hey nice Rainbow Dash shirt!"
    bree.say "Huh? Hey, yeah. Good eye,"
    bree.say "So, you’re the real deal, aren’t ya? Like rpgs?"
    jack_say "Oh hell yeah, I do!"
    jack_say "In fact... maybe you’d like to join me and [hero.name] in a game I’m playing."
    bree.say "What, like co-op?"
    bree.say "What gaming platform?"
    hero.say "Actually, Bree, he’s talking about tabletop roleplaying."
    show bree sleep happy
    bree.say "Ohmygosh, really!? So old school!"
    bree.say "I’ve always wanted to try out one of those games!"
    jack_say "Ooh man, this is going to be soo cool."
    "He’s practically shaking, holding back all of his excitement."
    hide bree
    show jack normal
    "But, then he sighs."
    jack_say "But the game I was planning on running with my buddies requires three players."
    show sasha towel at left
    show jack bleed at right
    sasha.say "What the hell’s going on here?"
    "Sasha walks in, arms over her chest, wearing only a towel."
    sasha.say "Why is everyone standing in the doorway yelling."
    "Some people are trying to take a relaxing bath, you know."
    jack_say "Hey! Whoa, wait, bro. Bro."
    "Jack turns to me, a sly smirk on his face."
    jack_say "This is your other roommate!? She’s perfect!"
    "Sasha quirks an eyebrow at him, her nose wrinkling."
    sasha.say "That's a given."
    hide jack
    show sasha towel at left
    show bree casual happy at right
    "Bree squeals, grinning ear to ear."
    bree.say "We’re going to play a tabletop rpg together! You should totally play with us!"
    sasha.say "Huh... well. Guess it can’t hurt to try something new."
    sasha.say "Sure. Why not?"
    sasha.say "I’ll bite. It just better not be something kiddie."
    hide bree
    show sasha towel at left
    show jack bleed at right
    "Jack snickers."
    jack_say "Oh, believe me. It’s going to be very adult... alright."
    jack_say "I need to get things ready."
    jack_say "I’ll make up stats and everything, so you can just play when we meet."
    jack_say "I’ll give you a call!"
    hide jack
    hide sasha
    "With that, Jack just rushes out the door, slamming it behind him."
    "Guess I need to open up time in my calendar if I want to help him out."
    "I’m not too sure I want him alone in here with Bree and Sasha."
    "Poor guy might just explode from the excitement."
    "But what did he mean, exactly about things being ‘adult...?’"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
