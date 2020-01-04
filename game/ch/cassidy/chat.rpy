label cassidy_desire_0:
    if cassidy.get_status() == 'mistress':
        cassidy.say "You need to get more interesting or I'm going to start hurting you just to hear you scream."
        hero.say "That's not very nice."
        cassidy.say "News flash!"
        $ cassidy.sub -= 1
    elif cassidy.get_status() == 'pet':
        cassidy.say "I can't believe I let you do this to me."
        hero.say "You fucked up pretty hard, didn't you?"
        cassidy.say "Yes."
        hero.say "Just like I'm going to fuck you pretty hard."
        "Cassidy sighs."
    else:
        cassidy.say "What do you want, [hero.name]?"
    return

label cassidy_desire_1:
    call cassidy_desire_0
    return

label cassidy_desire_2:
    if cassidy.get_status() == 'mistress':
        cassidy.say "I have to say, you look fuckin' fantastic on your knees."
        hero.say "So do you!"
        cassidy.say "You don't deserve me on my knees."
        hero.say "Ouch! That hurts."
        cassidy.say "Good, you need to know your place. Conveniently, you look good there."
        $ cassidy.sub -= 1
    elif cassidy.get_status() == 'pet':
        if hero.fitness > 60 and hero.charm > 60:
            cassidy.say "[hero.name], the only thing that makes this bearable is that you're fucking hot."
            hero.say "I'm also hot fucking."
            cassidy.say "Of course, you're also a giant dork."
        else:
            cassidy.say "It's hard getting used to our...arrangement. I used to travel everywhere, now I have to stay here, spending all day in your office."
            hero.say "There are a lot worse things."
            cassidy.say "Oh yeah, name ten?"
            hero.say "Spending all day in my office with your hands tied behind your back and a buttplug in your mouth. You can guess the other nine."
        $ cassidy.sub += 1
    $ cassidy.love += 1
    return

label cassidy_desire_3:
    if cassidy.get_status() == 'mistress':
        if cassidy.get_flag_value('sex') > 5:
            cassidy.say "I've been thinking about letting you be on top for a change."
            cassidy.say "But only if you tell me what a Goddess I am!"
        else:
            cassidy.say "You need to put out more, [cassidy.heroname]"
            hero.say "What do you mean?"
            cassidy.say "For being my slave, I haven't had nearly enough of your cock."
            cassidy.say "You'd better take me out and feed me some dick, and soon."
            hero.say "Yes, Mistress!"
        $ cassidy.sub -= 1
    elif cassidy.get_status() == 'pet':
        cassidy.say "You know what's weird? I went to bed the other night -- at home, I mean -- and I was actually thinking about you."
        hero.say "Good thoughts or bad thoughts?"
        cassidy.say "Well, I was crying."
        hero.say "When I said I wanted to make you cry, I meant things like crying out \"More!\" or \"Oh God!\"."
        cassidy.say "I think I cried out \"Oh God\" too, actually."
        hero.say "I'm afraid to ask."
        cassidy.say "Yes, it was followed but \"What have I done!\""
        hero.say "You're playing with me."
        cassidy.say "A little!"
        $ cassidy.love += 1
        $ cassidy.sub += 1
    return

label cassidy_desire_4:

    cassidy.say "[hero.name], do you still talk to your parents at all?"
    hero.say "I guess, sure."
    cassidy.say "I mean, my Mom left when I was little, and Daddy is always busy with work. And, ugh, my step-mom. She's barely older than I am."
    hero.say "So you basically don't talk to any of them?"
    cassidy.say "Not really."
    hero.say "That's kind of sad. Look on the bright side. You've got me, and I talk to you all the time!"
    cassidy.say "It's true. I do and you do. That shouldn't make me feel better, but it kind of does."
    $ cassidy.love += 1
    if cassidy.get_status() == 'mistress':
        $ cassidy.sub -= 1
    else:
        $ cassidy.sub += 1
    return

label cassidy_desire_5:
    if hero.fitness > 60 and hero.charm > 60:
        cassidy.say "What did I ever do to deserve a hot, charming guy like you?"
    else:
        cassidy.say "What did I ever do to deserve a wreck like you? I mean, a sweet wreck, sure, but a wreck."
    hero.say "You tried to blackmail me by making it look like I stole 3 million dollars from my company."
    if cassidy.get_status() == 'mistress':
        hero.say "And it worked, so I guess crime does pay."
        $ cassidy.sub -= 1
    else:
        hero.say "But you you sucked at it, so you got busted, and now you suck me."
        $ cassidy.sub += 1
    cassidy.say "And you're also as romantic as a tree stump."
    $ cassidy.love += 1
    return

label cassidy_love_0:
    $ cassidy.love += 1
    if cassidy.get_status() == 'mistress':
        cassidy.say "I think unless you're actively licking my pussy, the more your mouth stays closed the better."
        hero.say "That's not ve--"
        cassidy.say "Zip it, [cassidy.heroname]! Don't want to hear it."
        $ cassidy.sub -= 1
    elif cassidy.get_status() == 'pet':
        cassidy.say "What do you do for fun?"
        hero.say "You!"
        cassidy.say "Nice. You treat all the girls this way?"
        hero.say "No, only the ones that tried to get me sent to jail and failed. So just you."
        $ cassidy.sub += 1
    else:
        if cassidy.sub < 30:
            cassidy.say "I think I have a collar with your name on it."
            hero.say "Whoa, where did that come from?"
            cassidy.say "I bought it at the pet store."
            hero.say "No I mean why did you even say that?"
            cassidy.say "Oh I was just imagining you wearing it and getting on your knees and begging for a...bone."
            "Holy shit, I can't tell if that's hot or terrifying. Both, probably."
            cassidy.say "It relieves the monotony of what hanging out with you is actually like."
            $ cassidy.sub -= 1
        else:
            cassidy.say "Look, you're cute, [hero.name], but don't think for a second you've got a shot with me."
            hero.say "Then why are you still talking to me?"
            cassidy.say "Good question!"
    return

label cassidy_love_1:
    call cassidy_love_0
    return

label cassidy_love_2:
    cassidy.say "What's the most impressive thing you know how to do?"
    if cassidy.get_status() == 'mistress':
        hero.say "I'd say my pussy-licking skills are pretty damn impressive."
        cassidy.say "Enh, you still need practice. Try again."
        hero.say "Ah, I know how to juggle you and a job and two gorgeous roommates."
        "Cassidy looks at me flatly."
        cassidy.say "Are you fucking them?"
        if bree.get_flag_value('sex') == 0 and sasha.get_flag_value('sex') == 0:
            hero.say "No, I haven't. Why, should I?"
            cassidy.say "Not while you're my slave, you won't!"
            $ cassidy.love += 5
        else:
            hero.say "Um, a few times, I guess, but nothing serious."
            cassidy.say "You stopped, right?"
            hero.say "What?"
            cassidy.say "You stopped fucking them when this started, right?"
            hero.say "I...no, I didn't think this arrangement was exclusive. I'm just your sex toy, right? Are you trying to say I can't have other relationships?"
            cassidy.say "Hmm. Maybe. I'll think about it."
        $ cassidy.sub -= 1
    elif cassidy.get_status() == 'pet':
        hero.say "I know how to get a girl on her knees."
        cassidy.say "By blackmailing her? Threatening to get her Daddy fired if she doesn't do what you want?"
        hero.say "Can you honestly say she doesn't deserve that?"
        "Cassidy opens her mouth to say no, but then stops."
        hero.say "See?"
    return

label cassidy_love_3:
    cassidy.say "Where do you like going for walks?"
    hero.say "That's an odd question."
    cassidy.say "I'm just trying to get to know you."
    hero.say "Well, I like the park. It's quiet, most of the time. Though I guess in the afternoon it's pretty busy, but it's just background people, most of them happy. So either way, it's relaxing."
    hero.say "What about you?"
    cassidy.say "Downtown, in the inner city, especially Spanish and Italian cities. I love to look at the architecture, listen to the people. In Barcelona I can spend hours just going from place to place. I can have a glass of wine and a tapa and just watch people."
    hero.say "What's a tapa?"
    cassidy.say "Seriously, don't you know anything?"
    hero.say "I guess not."
    cassidy.say "In Spain, it's this thing where you get a small plate, or a bunch of small plates if you want. It's casual and they're cheap and delicious, and you put the plate on top of your drink to keep the flies out of it."
    hero.say "Oh, weird."
    cassidy.say "No, it's amazing. You get to take in everything, and it's all so...anything goes."
    cassidy.say "Maybe I'll take you sometime."
    $ cassidy.love += 1
    return

label cassidy_love_4:
    cassidy.say "If you lived in a virtual reality of your own creation, what would it be like?"
    hero.say "I think it'd be a lot like your life. You know, big mansion, swimming pool, all the servants. No need for money."
    cassidy.say "Well, yeah, it's pretty great."
    hero.say "And of course someone -- no, six someones -- whose only job is to give me blowjobs whenever I want."
    if cassidy.get_status() == 'pet':
        cassidy.say "You couldn't handle six of me."
        hero.say "I'd love to try!"
    else:
        cassidy.say "So basically my life, but with six of you. You with tits. Huh. I wonder if I'd still like you with tits."
        hero.say "Let's not find out, shall we?"
    return

label cassidy_love_5:
    $ cassidy.love += 1
    if cassidy.get_status() == 'mistress':
        cassidy.say "I think I might keep you."
        hero.say "Like a kept man? You'll pay for everything and all I have to do is tickle your twat every now and then?"
        cassidy.say "I like the sound of that, don't you?"
        hero.say "It's not bad..."
    elif cassidy.get_status() == 'pet':
        cassidy.say "You know, I'm glad that my plan failed. It would've been fun to top you for awhile, but I always get bored."
        if cassidy.sub > 80:
            cassidy.say "I'm not bored of you. Of this. I...even kind of like it."
        else:
            cassidy.say "I'm not bored of you yet, though I wish you'd let me be on top more."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
