init python:

    Event(**{
        "name":"scottie_init",
        "label": ["scottie_init"],
        "girls_conditions": {"scottie":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "scottie_give_christmas",
        "label": ["scottie_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas"},
        "girls_conditions": {"scottie":{"min_love":50,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "scottie_give_birthday",
        "label": ["scottie_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday"},
        "girls_conditions": {"scottie":{"min_love":40,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "scottie_give_valentine",
        "label": ["scottie_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine"},
        "girls_conditions": {"scottie":{"min_love":100,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "scottie_event_01",
        "priority": 500,
        "label": ["scottie_event_01"],
        "duration": 0,
        "game_conditions":{"room":["livingroom"], "days_played":7, "flag_female":1, "done":"scottie_init"},
        "girls_conditions": {"sasha":{"present":True,'valid':True}},
        "do_once":True,
        "quit": True
        })

label scottie_event_01:
    scene bg livingroom
    "Sitting slumped on the sofa, all I want to do is zone out and watch some TV."
    "I thought that I was alone in the house, until I hear the usual loud music and stomping that tells me Sasha's home too."
    "I grab the remote and turn up the TV in the hope of drowning her out, but then I hear an equally loud noise from the hallway."
    "It sounds like someone knocking really hard on the door, for some reason ignoring the bell."
    "I'm not expecting any visitors, but I doubt Sasha can even hear herself think over her music."
    "Rather than start a yelling match, I reluctantly haul myself up and slope towards the front door."
    hero.say "All right, all right - I'm coming already!"
    show bg house with fade
    show scottie casual
    "I open the door, only to be confronted by a raised fist that stops within an inch of my surprised face."
    scottie.say "Huh?"
    hero.say "Fucking hell!"
    show scottie casual blush
    scottie.say "Oh...erm...sorry, I guess."
    hero.say "Yeah, you'd better be - who in the hell are you and what do you want?!?"
    "The owner of the fist is a suddenly nervous-looking guy in a baseball cap, band T-shirt and shorts."
    "His long blonde hair is gathered in a scruffy ponytail and I notice he's quite well-built into the bargain."
    "The look on his face going from mad to unsure makes me think he's probably not the sharpest tool in the box."
    scottie.say "Well...I guess I want to know if Sasha's in...is she?"
    "That answers a lot of questions."
    "If this guy had a label, it'd read 'Sasha's Ex' and be plastered all over him."
    hide scottie
    show sasha casual angry at left
    show scottie casual normal at right
    "I'm about to yell that she has a visitor, when I hear the sound of Sasha's door opening behind me."
    sasha.say "Jesus, Scottie - what part of 'fuck off and don't come back' don't you understand?"
    "Scottie seems to take this as an invitation to come inside, and I step neatly aside to clear his path to the apparent object of his intentions."
    scottie.say "I know what that means, Sasha - I'm not as dumb as I look!"
    "I try not to laugh at the implications of what Scottie just said."
    show scottie casual angry
    scottie.say "I don't get how you think you can just dump me like this, you mean bitch!"
    show sasha casual normal
    sasha.say "What's to get?"
    sasha.say "We had a fling, I got bored and I dumped your stupid ass - that's it."
    scottie.say "You're some cold whore!"
    sasha.say "Yeah, whatever - but this is one cold whore that's through putting up with your shit."
    "Scottie scowls at Sasha, and for a moment I wonder if he's going to take a swing at her."
    "Then I wonder if Sasha's assuming I'll help her if he does!"
    "But then he pauses and an odd look comes over his face as he does so."
    "It takes me a moment to realise what's happening, but it actually looks like he's making a visible effort to think."
    scottie.say "Well forget you, bitch - I can get myself some action just like that."
    "He tries to click his fingers, fails on the first attempt and then manages a half-snap on the second."
    hide sasha
    "Then he turns to me, what I suppose he thinks constitutes a suave smile spreading across his face."
    hide scottie
    show scottie casual perv
    scottie.say "Hey there!"
    "Is he actually dumb enough to try hitting on me, right here and in front of Sasha after that messy verbal exchange?"
    show scottie casual normal
    scottie.say "I didn't catch your name before - what is it?"
    hero.say "You mean before when you almost punched me in the face?"
    scottie.say "Yeah, that's right - so what's your name?"
    hide scottie
    show scottie casual normal at right
    show sasha casual normal at left
    sasha.say "Urrgh...this is Bree, my housemate."
    sasha.say "And I don't think her type is a slobbering ape like you!"
    "Suddenly they're both looking at me, waiting for me to take a side."
    menu:
        "Shoot him down":
            "Though he's not bad-looking and too dumb to know he's dumb, I'm still pretty pissed at him barging in here like a blind bull."
            hero.say "I'm sorry, are you actually asking me what I think of you?"
            "Scottie nods, seemingly confused at the notion of being asked a question about a question."
            hero.say "You might have made a better impression if you hadn't come round here, bellowing and letting your cock do all the thinking for you."
            hero.say "Worse still, underneath all of the bravado, you're really just coming crawling back after Sasha dumped you."
            hero.say "Pretty pathetic, all in all."
            scottie.say "Erm...does that mean you like me or not?"
            hero.say "Only if I could find some use for a pitiable moron that has to let his prick do all the thinking because it's so much smarter than his brain."
            scottie.say "Am I hearing a maybe?"
            hero.say "Not unless it's a maybe you'll evolve into something more resembling a human being, you dumbass loser."
            "Scottie seems to finally understand, and makes a defeated noise as he shuffles towards the open door."
            "But as he looks back over his shoulder, I can't help seeing an odd kind of interest in his eye."
            "Could it be that he's actually a little intrigued by the way I just chewed him out in front of Sasha like that?"
        "Lead him on" if 0 <= game.get_flag_value("morality") < 25:
            $ scottie_love_max = 200
            if "scottie" in HIDDEN:
                $ HIDDEN.remove("scottie")
            "I try to put the fact he's currently behaving like an ass aside and weigh Scottie up fairly."
            "He's pretty cute and he's in great shape, so maybe I'm just not seeing him at his best right now."
            hero.say "You're both mad right now, so nobody's seeing things straight."
            hero.say "I'm sure Scottie's not like this all the time."
            hero.say "Otherwise you'd never have dated him in the first place, Sasha."
            "This last comment produces a grin from Scottie and a disgusted frown from Sasha."
            scottie.say "That's right - I'm only mad now 'cos she made me that way!"
            sasha.say "You lying prick!"
            hero.say "Okay, that's enough - I'm sure you were both pricks at one time or another."
            sasha.say "So what are you trying to say, Bree?"
            hero.say "I don't know - maybe that I think it's worth getting Scottie's side of the story...in private some time?"
            scottie.say "Yes, score one for me!"
            sasha.say "Whatever, Bree - it's your funeral."
            hide sasha
        "Lead him on" if game.get_flag_value("morality") < 0:
            $ scottie_love_max = 200
            if "scottie" in HIDDEN:
                $ HIDDEN.remove("scottie")
            "For all that Scottie seems to be dumb as a post and too headstrong for anyone's good, I can't help being attracted to him all the same."
            "I guess it's the idea of being with someone so uncomplicated and impulsive, how exciting that might be."
            hero.say "Maybe I like the idea of being carried off by a big ape like this guy!"
            $ scottie.love += 10
            sasha.say "Tell me you didn't just say that?!?"
            hero.say "Jeez, Sasha - you already made it plain you don't want him anymore."
            hero.say "Move over and give someone else a chance, eh?"
            "I wink suggestively at Scottie, giving him my best approximation of a bimbo's giggle."
            "Scottie looks genuinely shocked, but soon recovers his ludicrous swagger once more."
            scottie.say "Yeah, Sasha - you had your chance, now stop cramping my game here."
            sasha.say "Okay, Bree - but just don't say I didn't warn you about this asshole when he fucks you around, just like he did with me."
            hide sasha
            hero.say "Wow, I thought she'd never leave us alone."
            hero.say "And wow again - how did she ever manage to let go of this body you've got under those clothes?"
            scottie.say "Ah, who cares about her - let's talk more about us."
    hide scottie
    "Scottie leaves soon after the conversation ends, turning on his heel and stopming back out of the front door."
    "I suppose this is what always happens when you live with housemates, their pasts messing with your present."
    if "scottie" not in HIDDEN:
        "But Scottie feels to me like the kind of past that might be more than a little fun to mess with."
        "Or be messed with by."
    return

label scottie_give:
    pass
    return

label scottie_give_valentine:
    pass
    return

label scottie_give_birthday:
    show scottie
    "Scottie walks towards me."
    call scottie_greet from _call_scottie_greet_8

    scottie.say "Happy birthday [hero.name]!"
    call scottie_give from _call_scottie_give
    return

label scottie_give_christmas:
    pass
    return

label scottie_init:
    if "scottie" not in HIDDEN:
        $ HIDDEN.append("scottie")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
