label aletta_birthday_gift:
    show aletta
    if aletta.get_flag("birthdayknown"):
        hero.say "Happy birthday Aletta."
        aletta.say "How sweet, you remembered my birthday !"
    else:
        aletta.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ aletta.set_flag("birthdayknown")
    return

label aletta_gift_swimsuit:
    show aletta happy
    aletta.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if aletta.love >= 150 or aletta.sub >= 50:
        show aletta blush
        aletta.say "It's so pretty, thank you [hero.name]."
        $ aletta.set_flag("sexyswimsuit")
    else:
        show aletta angry
        aletta.say "Thanks but no thanks [hero.name]."
        aletta.say "You think I would wear that?"
    return

label aletta_gift_collar:























    hero.say "Okay, okay...Aletta, we've become far more than just a couple of people that happen to work together, haven't we?"
    "She regards me quizzically, but nods in agreement all the same."
    hero.say "In fact, you might say that we've become a couple that works together instead - if you follow?"
    "Aletta rolls her eyes at the cheesiness of the line, and rotates a finger to tell me I need to get to the point more quickly."
    hero.say "I suppose what I'm trying to say is that, when I first met you...I'll be honest - I kinda thought you were a bitch!"
    hero.say "But that changed when I finally got to know the person that you really are."
    hero.say "And then I discovered that, while you weren't really the bitch that you pretended to be, you secretly wanted someone to make you their own bitch for real!"
    "The look on Aletta's face in response to this is hard to read."
    "On the one hand, the colour in her cheeks could be the first signs of anger and outrage."
    "But on the other, it could just as easily be the beginnings of her admitting her true feelings and finally releasing all of those pent up emotions."
    "I've come too far to quit now, so I steel my nerves and press on."
    hero.say "You've been hiding behind the image of a hard-ass that you've created for yourself for too long, Aletta."
    hero.say "I want you to put this on and let people know that you really are a bitch after all."
    hero.say "But I want you to let them know that you're MY, bitch, Aletta!"
    "At this, I pull out a black leather collar from my pocket, with a chain lead attached to it."
    "The collar is unadorned, save for the word 'Bitch', spelt out in golden letters on the front."
    if aletta.sub < 75:
        show aletta angry
        "Aletta's eyes widen in horror at the sight of the collar, and she lets out a fierce shriek that almost pierces my eardrums."
        aletta.say "[hero.name], you ass-hole!"
        aletta.say "Just what kind of a sick mother-fucker are you?!?"
        "She swings for me, hitting the hand that's holding the collar and lead, sending them spinning away."
        aletta.say "To think that I let you close to me!"
        aletta.say "To think that I trusted you!"
        aletta.say "You don't know the first thing about me."
        aletta.say "Not if you think that what I want is to be treated like an animal!"
        "She begins to stalk away from me, turning her head to hurl yet more abuse my way as she leaves."
        aletta.say "If you want someone to put a collar on and call a bitch, then buy a goddamn dog!"
        $ aletta.love -= 20
    else:
        "It seems that I was right, as Aletta tentatively accepts the collar from me and begins to fasten it around her own neck."
        "She says nothing the whole time, but keeps on shooting nervous glances in my direction."
        "Her expression makes me think that she's afraid of either doing something wrong, or else going to slowly as she puts it on."
        "So much so that I'm actually surprised to see that her hands aren't shaking."
        "But once the collar is securely fastened around her neck, Aletta looks up at me with expectant eyes, as if she's awaiting my next command."
        hide aletta
        $ aletta.set_flag("collared")
        $ aletta.set_flag("status", "sex slave")
        show aletta
        hero.say "How does that feel, Aletta?"
        "She puts a hand to her neck, feeling the presence of the collar and seeming to understand what it signifies."
        aletta.say "It...it feels...good, it feels good, [hero.name]..."
        "I frown a little and shake my head."
        hero.say "Now, now, Aletta - I don't remember saying that you could call me that!"
        aletta.say "I'm sorry...M...Master?"
        "I smile at the use of the appropriate title, nodding my head in approval."
    "Things changed significantly between Aletta and myself today, to the degree that I'd be confident to say they'll never be the same again."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
