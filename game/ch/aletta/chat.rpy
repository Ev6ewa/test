label aletta_desire_0:
    if randint(1,2) == 1:
        aletta.say "You should try harder at work."
        menu:
            "Yes boss":
                hero.say "Yes boss."
                aletta.say "Good boy."
                $ aletta.sub -= 1
            "I work enough":
                hero.say "I work hard enough."
                aletta.say "Lazy ass..."
                $ aletta.love -= 1
            "You can trust me":
                hero.say "You can trust me Aletta."
                aletta.say "Thank you [hero.name]."
                $ aletta.love += 1
            "Let me handle things":
                hero.say "You should step back and let me handle things."
                aletta.say "..."
                $ aletta.sub += 1
    else:
        aletta.say "Did you get the reports done?."
        menu:
            "Yes boss":
                hero.say "Yes boss."
                aletta.say "Good boy."
                $ aletta.sub -= 1
            "I'll do them later":
                hero.say "I'll get them done when I get them done."
                aletta.say "..."
                $ aletta.love -= 1
            "Of course":
                hero.say "Of course I did Aletta."
                aletta.say "Great."
                $ aletta.love += 1
            "Don't worry":
                hero.say "You should mind your own business and not worry about me."
                $ aletta.sub += 1
    return

label aletta_desire_1:
    if randint(1,2) == 1:
        aletta.say "What do you think of Audrey."
        menu:
            "She's lazy":
                hero.say "She's too lazy, not doing her share of work if I can say so."
                $ aletta.love += 1
            "She's hot":
                hero.say "She's hot as fuck."
                $ aletta.love -= 1
            "I prefere older women":
                hero.say "She's too young to know what a woman should be."
                $ aletta.love += 1
            "I prefere willful women":
                hero.say "She's too meek for my tastes."
                $ aletta.sub -= 1
    else:
        aletta.say "What do you like to do for fun?"
        menu:
            "Working out":
                hero.say "Working out mostly. I like to stay fit."
                $ aletta.love += 1
            "Picking up chicks":
                hero.say "Picking up chicks at the local bar."
                $ aletta.love -= 1
            "Reading":
                hero.say "I love to read for hours."
                $ aletta.love += 1
            "Watching T.V.":
                hero.say "Watching T.V. and being lazy."
                $ aletta.sub -= 1
    return

label aletta_desire_2:
    if randint(1,2) == 1:
        aletta.say "Why don't you try being more manly."
        menu:
            "Yes":
                hero.say "Yes ma'am."
                $ aletta.sub -= 1
            "Fuck off":
                hero.say "Fuck off."
                $ aletta.love -= 1
            "I am manly already":
                hero.say "I am manly enough."
                $ aletta.love += 1
            "Let me show you":
                hero.say "Why don't you get on my knees so that I can show you manly."
                $ aletta.sub += 1
    else:
        aletta.say "Would you like to see the new gun I just got?"
        menu:
            "Be Intrigued":
                hero.say "That sounds interesting."
                $ aletta.sub -= 1
            "Don't Care":
                hero.say "Not interested."
                $ aletta.love -= 1
            "Maybe later":
                hero.say "I'm busy right now, but you can show me later."
                $ aletta.love += 1
            "I'll protect you":
                hero.say "You don't need a gun as long as you have me to protect you."
                $ aletta.sub += 1
    return

label aletta_desire_3:
    if randint(1,2):
        aletta.say "Men are such pussies."
        menu:
            "Women are our leaders":
                hero.say "We need women to lead us."
                $ aletta.sub -= 1
            "What crap":
                hero.say "What crap."
                $ aletta.love -= 1
            "Some maybe":
                hero.say "Some more than others."
                $ aletta.love += 1
            "Not me":
                hero.say "I am no pussies Aletta, wan't me to show you ?"
                $ aletta.sub += 1
    else:
        aletta.say "Are you seeing someone?"
        menu:
            "No":
                hero.say "No, I don't get many dates."
                $ aletta.sub -= 1
            "A lot":
                hero.say "Yeah, anyone I want, when I want."
                $ aletta.love -= 1
            "It's not your business":
                hero.say "I don't see how that is any of your bussiness."
                $ aletta.love += 1
            "I can date you":
                hero.say "I still have some time for you."
                $ aletta.sub += 1
    return

label aletta_desire_4:
    if randint(1,2) == 1:
        aletta.say "Why don't you try being more manly."
        menu:
            "Sure":
                hero.say "Yes ma'am."
                $ aletta.sub -= 1
            "Fuck off":
                hero.say "Fuck off."
                $ aletta.love -= 1
            "I am more than enough":
                hero.say "I am manly enough."
                $ aletta.love += 1
            "On your knees, bitch":
                hero.say "Why don't you get on your knees so that I can show you manly."
                $ aletta.sub += 1
    else:
        aletta.say "How many women have you slept with?"
        menu:
            "That's too personal":
                hero.say "Oh that's too personal."
                $ aletta.sub -= 1
            "Dozens":
                hero.say "Dozens before you, and dozens after you."
                $ aletta.love -= 1
            "Tell me about you":
                hero.say "I'll tell you if you tell me how many men you have been with."
                $ aletta.love += 1
            "Enough":
                hero.say "Enough to know how to make you scream..."
                $ aletta.sub += 1
                $ aletta.love += 1
    return

label aletta_desire_5:
    aletta.say "What's your favorite sex toy?"
    menu:
        "Anything you like":
            hero.say "Anything you want to use on me."
            $ aletta.sub -= 1
        "You":
            hero.say "You."
            if aletta.sub >= 125:
                $ aletta.love += 2
            elif aletta.sub >= 75:
                $ aletta.love += 1
            else:
                $ aletta.love -= 1
        "Let me show you":
            hero.say "How about I show you instead?"
            $ aletta.love += 1
        "Whatever keeps you in line":
            hero.say "Whatever keeps you in line the best."
            $ aletta.sub += 1
            $ aletta.love += 1
    return

label aletta_love_0:
    aletta.say "How do you feel about smoking?"
    menu:
        "It's your choice":
            hero.say "If you enjoy it I don't have a problem with it."
            $ aletta.sub -= 1
        "I only smoke while drunk":
            hero.say "I only smoke when I get drunk."
            $ aletta.love -= 1
        "It's bad for the health":
            hero.say "You should care more about your health if you smoke."
            $ aletta.love += 1
        "You shouldn't smoke":
            hero.say "Smoking isn't lady like at all."
            $ aletta.sub += 1
    return

label aletta_love_1:
    aletta.say "What do you think of career minded women?"
    menu:
        "We need women to lead us":
            hero.say "Men need women to lead us."
            $ aletta.sub -= 1
        "I am better than any woman":
            hero.say "I could probably do a better job than her and earn more money either way."
            $ aletta.love -= 1
        "She's flawed":
            hero.say "I think she would be someone who hasn't been cared for properly."
            $ aletta.love += 1
        "It's not her place":
            hero.say "If she was with me she would have to become a housewife."
            $ aletta.sub += 1
    return

label aletta_love_2:
    aletta.say "How do you feel about women who date married men?"
    menu:
        "I don't judge":
            hero.say "It isn't my place to judge."
            $ aletta.sub -= 1
        "She's a slut":
            hero.say "She sounds slutty."
            $ aletta.love -= 1
        "The man is at fault":
            hero.say "A better question is why is a married man dating someone else?"
            $ aletta.love += 1
        "She would be better with me":
            hero.say "If she were mine she wouldn't need anyone else."
            $ aletta.sub += 1
    return

label aletta_love_3:
    aletta.say "What do you think of Audrey"
    menu:
        "She's lazy":
            hero.say "She's too lazy, not doing her share of work if I can say so."
            $ aletta.love += 1
        "She's hot":
            hero.say "She's hot as fuck."
            $ aletta.love -= 1
        "I prefere older women":
            hero.say "She's too young to know what a woman should be."
            $ aletta.love += 1
        "I prefere willful women":
            hero.say "She's too meek for my tastes."
            $ aletta.sub -= 1
    return

label aletta_love_4:
    aletta.say "When are you going to ask me out?"
    menu:
        "You should ask me":
            hero.say "I was waiting for you to ask me."
            $ aletta.sub -= 1
        "When I do":
            hero.say "When I feel like it."
            $ aletta.love -= 1
        "Be patient":
            hero.say "Be patient Aletta."
            $ aletta.love += 1
        "When you are ready":
            hero.say "When I feel you are ready for a date."
            $ aletta.sub += 1
    return

label aletta_love_5:
    aletta.say "How would you feel if I asked you over for drinks?"
    menu:
        "I would obey":
            hero.say "I would come if it would make you happy."
            $ aletta.sub -= 1
        "I'd check my schedule":
            hero.say "I would have to make sure I don't have something better to do."
            $ aletta.love -= 1
        "I am the one who would ask":
            hero.say "Isn't it my job to ask you over for drinks?"
            $ aletta.love += 1
        "It would be the best night for you":
            hero.say "I would come over to show you the best night of your life."
            $ aletta.sub += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
