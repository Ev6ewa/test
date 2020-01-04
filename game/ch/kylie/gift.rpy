label kylie_birthday_gift:
    show kylie
    if kylie.get_flag("birthdayknown"):
        hero.say "Happy birthday Kylie."
        kylie.say "How sweet, you remembered my birthday !"
    else:
        kylie.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ kylie.set_flag("birthdayknown")
    return

label kylie_gift_swimsuit:
    show kylie happy
    kylie.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if kylie.love >= 150 or kylie.sub >= 50:
        show kylie blush
        kylie.say "It's so pretty, thank you [hero.name]."
        $ kylie.set_flag("sexyswimsuit")
    else:
        show kylie angry
        kylie.say "Thanks but no thanks [hero.name]."
        kylie.say "You think I would wear that?"
    return

label kylie_gift_collar:
    show kylie happy
    kylie.say "Oh, hey, [hero.name]."
    "Kylie gives me a smile of her own, one that barely manages to keep from becoming a rictus thanks to her insatiable curiosity."
    "It's when my hand reaches into my pocket and I see Kylie begin to absently play with the ring finger of her left hand that everything finally begins to make sense."
    "She thinks that I'm going to produce a ring and propose to her!"
    "Well, I suppose this is what you get for jumping to conclusions like that..."
    hero.say "Okay, Kylie, no more beating about the bush."
    hero.say "I really wanted to ask you something."
    "By this time, I can see that Kylie's eyes are almost burning with a manic intensity, as she leans forward to hear what I have to say next."
    hero.say "Since we first got reaquainted with each other, you've made me very happy, Kylie."
    hero.say "But I've always felt like there was something missing between us."
    hero.say "That you were almost crying out for some kind of gesture form me, some kind of commitment."
    hero.say "And not something shallow or frivolous either - a serious commitment, one that would fill a gaping void that you have inside of yourself."
    "While I'm apparently in the act of pouring my heart out to her, Kylie nods faster and with more intensity with each passing second."
    "And after all, why the hell not - I'm telling her everything that I'm sure she wants to hear from me."
    hero.say "So that's why I went out and had this made, especially for you."
    hero.say "And I'd be honoured if you'd wear it, day and night, together and apart, as a symbol of my feelings for you?"
    "I choose that moment to finally whip out what's been concealed in my pocket and dangle it in front of Kylie's wide, almost glazed over eyes."
    kylie.say "Oh, [hero.name], I've dreamed of this day ever since I was a girl!"
    show kylie surprised
    kylie.say "You just can't imagine how many times I've pictured the day that you ask me to wear your...DOG COLLAR?!?"
    "See, I told you that I had a surprise in store for her, even if it wasn't the kind she was expecting."
    "I continue to ignore the flabbergasted look on Kylie's face and push straight on with my patter."
    hero.say "Let's face it, Kylie - you're more than a little wild at times!"
    hero.say "Well...if I'm honest, you're seriously wild most of the time!"
    hero.say "But don't get me wrong - I'm really into that craziness."
    hero.say "I just think that, if you're honest, what you're actually crying out for is someone to put a leash on you, figuratively and literally."
    "Kylie's eyes keep darting from my face and down to the collar, where the tag clearly reads 'CRAZY'."
    hero.say "Like I already said, Kylie - I want to make a commitment to you."
    hero.say "And I think I can do that best if you'll consent to take me as your master and be my bitch."
    hero.say "So what do you say?"
    "Kylie says nothing at first, and at the same time her face is almost impossible to read."
    "But the way her eyes are darting here and there and the time she's taking makes me certain that she's weighing up her options and considering all of the angles."
    "We both know that she wanted a marriage proposal and a ring from me, but essentially what she wants is to have me commit myself to her."
    "And what I'm offering does just that, even if it's not strictly in the way that she anticipated."
    show kylie happy
    kylie.say "If it means that I get to be with you, [hero.name], then I'll be whatever you want me to be."
    "Kylie smiles as she lifts her hair and lets me fasten the collar around her neck."
    $ kylie.set_flag("collared")
    hide kylie
    show kylie blush
    "And when it's in place, I can't help but think that it actually looks really good, like it's the missing part of her personality."
    "On another girl, a more normal and well-balanced type of girl, it would probably look downright weird."
    "But somehow it just works as an early warning that Kylie's quirky and more than a little crazy - but of course, in a good way!"
    kylie.say "So, when do we get to start the obedience training?"
    hero.say "Hold on there, girl!"
    hero.say "You're getting a bit ahead of yourself there."
    hero.say "We need to teach you to walk to heal befoe we get into any of that!"
    "I can see Kylie warming to idea more as each second passes and her mind considers the possibilities."
    "And a part of me wonders how responsive she'll be to obedience training after all."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
