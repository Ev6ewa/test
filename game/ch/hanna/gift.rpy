label hanna_birthday_gift:
    show hanna
    if hanna.get_flag("birthdayknown"):
        hero.say "Happy birthday Anna."
        hanna.say "How sweet, you remembered my birthday !"
    else:
        hanna.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ hanna.set_flag("birthdayknown")
    return

label hanna_gift_swimsuit:
    show hanna happy
    hanna.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if hanna.love >= 150 or hanna.sub >= 50:
        show hanna blush
        hanna.say "It's so pretty, thank you [hero.name]."
        $ hanna.set_flag("sexyswimsuit")
    else:
        show hanna angry
        hanna.say "Thanks but no thanks [hero.name]."
    return

label hanna_gift_collar:
    show hanna
    hanna.say "So, what's up with you?"
    "I'm doing that thing again, where I start looking at Hanna's lean, athletic body beneath her tight, stretchy sportswear."
    "That thing where she notices that I'm looking at her, and smiles in a knowing manner."
    "That thing where I know that she's smiling in that knowing manner, and it makes me want to stare all the more..."
    "No...I need to focus - damn sexy Hanna!"
    hero.say "What's up with me?"
    hero.say "Nothing's up with me...not really..."
    hero.say "I just had something that I wanted to give to you, that's all!"
    "Hanna's smile is still knowing and slightly amused as she nods her head slowly."
    hanna.say "Well, that is kind of having something up with you, you know?"
    "I shake my head gently, both as a gesture of mild disagreement and in the hope of shaking some sense back into my brain."
    "If I don't assert some control over myself and the situation at hand, this is going to get away from me real soon."
    hero.say "What it is, Hanna, is that I feel I've gotten to know you pretty well recently."
    hero.say "At least well enough to know what it is that you really want from our relationship."
    hero.say "Maybe even well enough to know the things you want that you weren't even aware of yourself..."
    "At this, Hanna looks at me sideways, a little puzzled."
    "But I take her not interrupting me as a sign that she wants me to go on."
    "I already have the collar clutched in my hand, worrying it inside of my pocket."
    "And it takes an actual feat of will to force myself to pull it out and let Hanna see it for the first time."
    hero.say "And I think, Hanna, that one of those things is you wanting to grab the attention wherever you go."
    hero.say "You like to have people looking at you, and this will make sure that all eyes are on you - trust me on this..."
    "I hold up the collar so that she can make it out for what it really is, and not mistakenly think it's nothing more than normal jewellery."
    "The leather of the collar is a deep, royal blue with a silver plate attached."
    "On this is inscribed the word 'Juicy'."
    "Hanna's mouth works silently at first, her eyes widening as she realises the implications of what I'm offering to her."
    "She looks at me, and then quickly back at the collar."
    "And then she finally manages to speak."
    if hanna.sub <= 50:
        $ hanna.sub -= 10
        $ hanna.love -= 10
        show hanna sad
        hanna.say "Oh, [hero.name]...oh no...no..."
        "Hanna begins to shake her head even as I hold the collar out towards her."
        "She pushes it to one side, not aggressively, but as though she can't stand to see me even holding it."
        hero.say "Hanna...I thought..."
        "No matter how I try to explain myself to her, Hanna refuses to meet my eye."
        "She turns away from me, and then turns her back completely."
        "And before I know it, she's jogging steadily away from me again."
        hero.say "Hanna...wait!"
        "She doesn't turn or say a word, just waves me away as she picks up speed."
        "A moment later, I'm left alone and painfully aware of how badly I just screwed up."
    else:
        show hanna blush
        hanna.say "Wh...what is that?"
        hanna.say "It looks like...a dog collar!"
        "I can see from her expression that she's more intrigued than offended."
        "And if she's not rejecting the idea out of hand, then I know that I have sufficient room for manoeuvre."
        hero.say "Sure, it looks like a dog collar, Hanna."
        hero.say "But it's in your size...and I'd like you to wear it."
        "Hanna licks her lips nervously, eyes still fixed on the collar I'm holding."
        hanna.say "You want me to, what - pretend to be your dog?"
        "I make a non-committal sound and tip my head from one side to the other."
        hero.say "It's not so much that I want you to pretend to be a dog, Hanna."
        hero.say "More like I want to show you off to everyone as the prize example of breeding that you are."
        hanna.say "You want to...show me off?"
        hero.say "I want to walk you, like those people walk their expensive dogs."
        hero.say "Loving the fact that people are looking in their direction while they do."
        "Hanna's hands are crossed over her chest now, and she's biting her lip as she ponders my words."
        hero.say "Imagine all of those eyes on you, Hanna, all those people unable to look away until you've passed out of sight..."
        hero.say "You wouldn't need to pretend that you don't want them to look at you anymore."
        hero.say "You could just bask in their attention and leave them wanting more."
        "Slowly, ever so slowly, Hanna reaches out gingerly with one hand to take the collar from me."
        "She turns it over more than once, glancing up at me as she does so."
        "And then finally, she lifts it to her neck and turns around so that I can fasten the strap,"
        hide hanna
        $ hanna.set_flag("collared")
        $ hanna.set_flag("status", "sex slave")
        show hanna blush
        "Once the collar is in place, she turns around to face me, her cheeks flushed and red."
        hanna.say "How do I look, [hero.name]?"
        "I shake my head in a small show of disapproval."
        hero.say "You just let me put a collar on you, Hanna."
        hero.say "It's time you got used to calling me 'Master'."
        "Hanna nods eagerly at this."
        hanna.say "Yes...Master!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
