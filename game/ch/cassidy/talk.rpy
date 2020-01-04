label cassidy_talk_love:
    show cassidy
    if cassidy.love < 120:
        cassidy.say "Love? Who cares about love. I care about having fun. If it isn't fun it isn't worth my time."
    elif cassidy.love < 160:
        cassidy.say "[hero.name], you've been in love before. What does love feel like?"
        hero.say "That's hard to put into words."
        if cassidy.get_status() == 'mistress':
            cassidy.say "Try."
        else:
            cassidy.say "That's it?"
        hero.say "Well. It's when you care about someone's well-being as much or more than your own. When you see little things and want to tell the other person."
        hero.say "When their presence is comfortable and their absence is uncomfortable."
        hero.say "I guess? I don't know if that really does it justice, but it's what I got."
        cassidy.say "Oh. I've never been in love before."
        hero.say "That's kind of sad."
        cassidy.say "Maybe."
    else:
        cassidy.say "I don't know what love is, really, but I think I love you."
        if cassidy.get_status() == 'pet':
            cassidy.say "Especially when I'm on my knees."
        else:
            cassidy.say "Especially when you're on your knees."
    hide cassidy
    return

label cassidy_talk_sex:
    show cassidy
    if cassidy.get_status() == 'mistress':
        cassidy.say "Sex is what you do when I tell you to."
        hero.say "Yes, but do you like it?"
        if cassidy.love < 80:
            cassidy.say "Enh, it's okay. You should do better."
            hero.say "Ouch, that hurts."
            cassidy.say "Sex isn't supposed to hurt! Well maybe it should hurt you a little bit. Maybe that would make it better!"
            hero.say "I'd better shut up now."
            cassidy.say "Smart boy."
        elif cassidy.love < 120:
            cassidy.say "Well, I do like cumming on your face."
            if cassidy.get_flag_value('sex') < 5:
                cassidy.say "I think you need just a little more practice, though. You should get to work on that."
            else:
                cassidy.say "All that practice has really improved your tongue work, I have to admit. I'm kind of looking forward to next time!"
        else:
            cassidy.say "I love wrapping my thighs around you and squeezing until you cum like a grape that's about to pop."
            hero.say "For something that should be sexy, you make that sound awfully unappealing."
            cassidy.say "Really, did you just say having my thighs around you is unappealing?!"
            if cassidy.sub < -50:
                hero.say "No, Mistress, I'd never say anything like that!"
            else:
                hero.say "I...have to admit I do like being between your thighs."
            cassidy.say "Good boy."
    elif cassidy.get_status() == 'pet':
        if cassidy.love < 80:
            cassidy.say "I used to like sex."
            hero.say "Oh yeah? What happened?"
            cassidy.say "You did."
            hero.say "You have only yourself to blame."
            "Cassidy sighs."
        elif cassidy.love < 120:
            cassidy.say "It used to be that when I had sex, I preferred being on top."
            hero.say "Used to be? And now?"
            if cassidy.get_flag_value('sex') < 5:
                cassidy.say "I still prefer being on top."
            else:
                cassidy.say "You've taught me that being on the bottom isn't so bad."
        else:
            cassidy.say "Once upon a time, sex was just a thing I did to pass the time."
            hero.say "Has that changed?"
            cassidy.say "Well, I still want to have sex with you, so I guess it has changed."
            hero.say "That's actually kind of sweet, in a weird way."
    else:
        cassidy.say "Oh, you trying to get in my panties already?"
        hero.say "No, I just wanted to know what you thought about it. What you like?"
        cassidy.say "That's for me to know and you not to find out."
        "She pauses a moment, giving me a sideways look."
        cassidy.say "Well, you might get to find out, but you'll have to be on your knees."
    $ cassidy.love += 1
    hide cassidy
    return

label cassidy_talk_politics:
    show cassidy
    cassidy.say "Last week, Daddy and my step-mom and I had dinner with our Senator at our house."
    hero.say "Wow, do you have dinner with senators often?"
    cassidy.say "Oh, I guess, every few months or something? Daddy is a big contributor to his campaign."
    hero.say "What's he like?"
    cassidy.say "Boring. He didn't even look when I flashed him. Though maybe it was just because his wife was there."
    hero.say "Wait, isn't that guy like 70?"
    cassidy.say "So?"
    hero.say "Gross! You want an old lech drooling over you?"
    cassidy.say "An old lech who happens to be a senator? Oh yeah, powerful men are sexy! And he's not Sean Connery or anything but he's still sexy in that oily kind of way."
    hide cassidy
    return

label cassidy_talk_food:
    show cassidy
    cassidy.say "Which three Michelin star restaurants have you been to?"
    hero.say "What's that?"
    cassidy.say "You don't know what the Michelin stars are?"
    hero.say "Don't they make tires or something?"
    cassidy.say "No -- well maybe but they also rate restaurants. Only the best in the world even get 1 star. There's only a hundred or so three star restaurants."
    hero.say "Ahh, fancy. I bet they're all expensive."
    cassidy.say "Oh I don't know. Maybe? I don't really pay attention to that kind of thing."
    hero.say "That must be nice. So which 3 star restaurants have you been to?"
    cassidy.say "About fifty of them, I think."
    menu:
        "Take me to one some time":
            $ cassidy.love += 1
            hero.say "Maybe you should take me to one some time."
            cassidy.say "Would you even be able to appreciate the food?"
            if hero.check_skill("cooking"):
                hero.say "Oh heck yeah, I love good food. It's just places like that are too expensive."
                cassidy.say "Well, maybe I will."
            else:
                hero.say "Hey if they've got a good steak, I'm in."
                cassidy.say "That would be a no, then."
        "Too fancy for me":
            $ cassidy.love -= 1
            hero.say "I'm not big on places that fancy. You probably need a jacket and tie just to walk into one of those places."
            cassidy.say "Well, yes, they have standards. They probably wouldn't even let you in."
    hide cassidy
    return

label cassidy_talk_travels:
    show cassidy
    cassidy.say "So where have you been, [hero.name]?"
    hero.say "Um. Here, mostly."
    cassidy.say "Have you ever been to Côte d'Ivoire?"
    hero.say "Where?"
    cassidy.say "So that's a no then. How about New Zealand?"
    hero.say "Well at least I've heard of New Zealand."
    cassidy.say "How about the Bahamas?"
    hero.say "Still no."
    cassidy.say "Um. Argentina?"
    hero.say "Nope."
    cassidy.say "Have you been anywhere?"
    hero.say "I've been to France. Once."
    cassidy.say "You need to get out more."
    hide cassidy
    return

label cassidy_talk_tv:
    show cassidy
    cassidy.say "When I was fourteen, I auditioned for one of those teen singing shows. It was pitched like 'Austin & Ally'."
    hero.say "Uh, never heard of it."
    cassidy.say "Um, like Hannah Montana?"
    hero.say "Yeah, heard of her. Boy did she grow up...different."
    cassidy.say "She did pretty well for herself."
    hero.say "So how did your audition go?"
    show cassidy angry
    cassidy.say "The casting director said I sang like a cat being strangled by a violin."
    hero.say "Ouch, that's harsh."
    show cassidy happy
    cassidy.say "So I got Daddy to get him fired. The whole show got cancelled before they even made a pilot."
    hero.say "Holy shit!"
    "Cassidy smiles at me, with a hint of malice in her eyes."
    hide cassidy
    return

label cassidy_talk_sports:
    show cassidy
    cassidy.say "I don't really like sports."
    cassidy.say "I like athletes, though. I especially like big, muscle-y black athletes, with their big dicks."
    hero.say "Whoa, too much information!"
    "Cassidy shrugs."
    $ cassidy.love -= 1
    hide cassidy
    return

label cassidy_talk_fashion:
    show cassidy
    cassidy.say "I love shopping! There's always so many cute and beautiful things, and trying to find stuff nobody else is wearing is hard work. But worth it!"
    cassidy.say "Do you like shopping, [hero.name]?"
    hero.say "No."
    cassidy.say "Why not?"
    hero.say "I don't have the patience to look at every little thing. I just want to get in, get my stuff, get out."
    cassidy.say "No wonder you dress like that."
    hero.say "Like what?"
    "She casually waves at me, roughly indicating my shirt."
    cassidy.say "Like THAT!"
    hero.say "Uh. But I like how I dress."
    cassidy.say "Yeah, we're going to have to change that."
    hero.say "Say what?"
    cassidy.say "Let's go shopping some time. You can tell me which cute thing makes me look the best, and I can help you find something that makes you look less...like a hobo."
    menu:
        "Sure, sounds like fun.":
            hero.say "Sure, sounds like hours and hours of fun."
            $ cassidy.love += 1
            $ cassidy.set_flag('shopping', True)
            cassidy.say "Sounds great!"
        "No way!":
            hero.say "No way! I'd probably fall asleep."
            $ cassidy.love -= 1
            $ cassidy.set_flag('shopping', False)
            cassidy.say "Your loss."
    hide cassidy
    return

label cassidy_talk_books:
    show cassidy
    cassidy.say "Books? Maybe magazines. There's some really good clothes in magazines."
    hero.say "What, you don't read?"
    cassidy.say "I do! I read! I read...magazines. And, um. Stuff."
    hide cassidy
    return

label cassidy_talk_people:
    show cassidy
    cassidy.say "Most people just get in the way. I could do without them. Except for the ones that drive us around and keep up our house. Oh and Daddy, of course."
    return

label cassidy_talk_computers:
    show cassidy
    cassidy.say "The only computer I use is my phone."
    hero.say "That counts as a computer, these days."
    cassidy.say "Oh then I guess I'm pretty good at computers, at least if it has to do with social media."
    hide cassidy
    return

label cassidy_talk_music:
    show cassidy
    hero.say "So what kind of music do you like, Cassidy?"
    cassidy.say "Mom used to love Broadway, show tunes and stuff like that. Some of it's really good. But I like hip hop and dance."
    cassidy.say "I love going to the club and finding someone to dance with. And whatever happens then."
    hide cassidy
    return

label cassidy_talk_birthday:
    show cassidy
    hero.say "Happy birthday, Cassidy!"
    cassidy.say "What did you get me!"
    "Oh crap. What DID I get her? I need to cover, quick!"
    hero.say "It's a surprise!"
    cassidy.say "It better be a good one!"
    $ cassidy.love += 5
    hide cassidy
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
