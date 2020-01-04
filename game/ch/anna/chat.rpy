label anna_desire_0:
    if "guitar" in hero.skills:
        anna.say "Oh, I'm so happy you joined the band."
        menu:
            "I just hope I will not screw up":
                hero.say "Same here - I just hope that I don't screw it up!"
                anna.say "Don't worry - I'm sure you'll be great."
            "It was on a whim":
                hero.say "I kind of did it on a whim."
                anna.say "Erm...okay."
                $ anna.love -= 1
            "We will make great music":
                hero.say "I think we're gonna make some great music together, Anna."
                anna.say "Aw, thank you [hero.name]!"
                $ anna.love += 1
            "I'll take us to legendary status":
                hero.say "I'm going to take us all the way to being rock legends!"
                anna.say "Wow!"
                $ anna.sub += 1
    else:
        anna.say "So, did you like our music?"
        menu:
            "It was shitty":
                hero.say "Nah - it was pretty shitty."
                anna.say "Erm...okay."
            "I prefer pop music":
                hero.say "To be honest, it wasn't my kind of thing."
                hero.say "I normally listen to pop music."
                anna.say "Jesus wept..."
                $ anna.love -= 1
            "Yes":
                hero.say "Of course I did - you guys are great."
                anna.say "Oh, thank you!"
                $ anna.love += 1
            "You should practice more":
                hero.say "You sound pretty raw - practice some more and you'll be great."
                $ anna.sub += 1
    return

label anna_desire_1:
    if "guitar" not in hero.skills:
        anna.say "[hero.name]...what do you think of Sasha."
        menu:
            "She's mean":
                hero.say "She's pretty mean - I don't think she should talk to you like that."
                $ anna.love += 1
            "She's hot":
                hero.say "Phew - she's hot as fuck!"
                $ anna.love -= 1
            "She's fun":
                hero.say "She's pretty fun to be around - I really like snarky women."
                $ anna.love -= 1
            "Not much":
                hero.say "Ah...I don't really like her all that much."
                hero.say "Confession time - I like you a lot better."
                $ anna.sub += 1
    else:
        anna.say "So, what is it you like to do for fun?"
        menu:
            "Working out":
                hero.say "I like to work out mostly - you know, trying to keep in shape?"
                $ anna.love -= 1
            "Picking up chicks":
                hero.say "I like to cruise round the local bars, picking up babes."
                $ anna.love -= 1
            "Reading":
                hero.say "I tend to find that I read, often for hours at a time."
                $ anna.love += 1
            "Watching T.V.":
                hero.say "I tend to just vegetate in front of the TV."
    return

label anna_desire_2:
    if "guitar" not in hero.skills:
        anna.say "[hero.name]...what do you think of Kleio?"
        menu:
            "She's annoying":
                hero.say "Christ the girl's annoying as hell!"
                $ anna.love -= 1
            "She's hot":
                hero.say "Wow - she is just as hot as hell!"
                $ anna.love -= 1
            "She's fun":
                hero.say "She's pretty fun to hang around with."
                $ anna.love += 1
            "Not much":
                hero.say "To be honest, I don't like her all that much."
                hero.say "I much prefer hanging around with you."
                $ anna.sub += 1
    else:
        anna.say "You wanna listen to the new album I just got?"
        menu:
            "Be Intrigued":
                hero.say "Yeah, Anna - you have great taste in music, so it should be interesting."
                $ anna.love += 1
            "Don't Care":
                hero.say "Nah...not interested."
                $ anna.love -= 1
            "Maybe later":
                hero.say "I'm busy right now, Anna - but I'd love for you to show me later."
                $ anna.love += 1
    return

label anna_desire_3:
    if "guitar" not in hero.skills:
        anna.say "I just love metal - no other music comes close to that feeling of sheer raw power!"
        menu:
            "It's just noise":
                hero.say "It's just noise, not music - makes my ears bleed."
                $ anna.love -= 1
            "What crap":
                hero.say "What load of crap!"
                $ anna.love -= 2
            "Me too":
                hero.say "Me too - I agree with you one hundred percent."
                $ anna.love += 1
            "Power metal is the metal of metal":
                hero.say "Power metal is the shit - metal turned all the way up to eleven!"
                $ anna.sub += 1
    else:
        anna.say "Erm, [hero.name]...are you seeing someone right now?"
        menu:
            "No":
                hero.say "No, not really - I never seem to get many dates."
            "A lot":
                hero.say "Hell yeah - who I want and when I want to see them!"
                $ anna.love += 1
            "It's not your business":
                hero.say "Is that really any of your business, Anna?"
                $ anna.love -= 1
            "I can date you":
                hero.say "Don't worry, Anna - I can always make time for you..."
                $ anna.sub += 1
    return

label anna_desire_4:
    anna.say "Can I ask how many women you've slept with?"
    menu:
        "That's too personal":
            hero.say "Wow - that's kind of a personal question, don't you think?"
        "Dozens":
            hero.say "There were dozens before I met you, and there'll be dozens more after you."
            $ anna.love -= 1
        "Tell me about you":
            hero.say "I'll show you mine if you'll show me yours - tell me how many men you've been with, and I'll spill my guts."
            $ anna.love += 1
        "Enough":
            hero.say "Don't worry, I've been with enough to know what'll make you scream..."
            $ anna.sub += 1
    $ anna.love += 1
    return

label anna_desire_5:
    anna.say "Hey, [hero.name] - what's your favorite sex toy?"
    menu:
        "Anything you like":
            hero.say "I'm cool with anything that you want to use on me."
            $ anna.sub -= 1
        "You":
            hero.say "I have this cute little sex-doll that I like to call 'Anna'!"
            if anna.sub >= 125:
                $ anna.love += 2
            elif anna.sub >= 75:
                $ anna.love += 1
            else:
                $ anna.love -= 1
        "Let me show you":
            hero.say "Let me give you a practical demonstration..."
            $ anna.love += 1
        "Whatever keeps you in line":
            hero.say "Whatever the hell keeps your little ass in line."
            $ anna.sub += 1
    $ anna.love += 1
    return

label anna_love_0:
    anna.say "What do you think of girls that like to sleep with...girls?"
    menu:
        "It's your choice":
            hero.say "Hey, you do you - if that's what you like, that's what you like."
        "That's hot":
            hero.say "Oh yeah - I think it's fucking hot!"
            $ anna.love -= 1
        "Love is love":
            hero.say "Love is love, you can't keep it from taking whatever form it need to in order to flourish."
            $ anna.love += 1
    return

label anna_love_1:
    anna.say "Erm...do you like piercings?"
    menu:
        "Not much":
            hero.say "Ah...they're not really my kind of thing."
        "You shouldnt defile your body":
            hero.say "The almighty shaped you in his own image, so you shouldn't defile his creation."
            $ anna.love -= 1
        "It's hot":
            hero.say "Yeah, very much so - piercings look really hot on a girl."
            $ anna.love += 1
        "The more the better":
            hero.say "Oh yes indeed - the more the better!"
            $ anna.sub += 1
    return

label anna_love_2:
    anna.say "[hero.name], what do you think of girls that date a lot of different guys?"
    menu:
        "I don't judge":
            hero.say "Nobody would judge a guy for dating a lot of different girls - and it's not really for me to judge, either."
            $ anna.love += 1
        "They're sluts":
            hero.say "Huh...sounds like you're talking about some real big slut right there!"
            $ anna.love -= 1
        "They would be better with me":
            hero.say "Trust me, if the girl you're talking about had been with me, then she wouldn't need another man."
            $ anna.sub += 1
    return

label anna_love_3:
    anna.say "Ah...sometimes I wish I was so much smarter..."
    menu:
        "You are plenty smart":
            hero.say "You might not be joining MENSA anytime soon, Anna - but you're smart enough for me."
            $ anna.love += 1
        "Me too":
            hero.say "Yeah, I know where you're coming from there - I wish you were smarter too!"
            $ anna.love -= 1
    return

label anna_love_4:
    anna.say "Hey, [hero.name] - when are you going to get your act together and ask me out?"
    menu:
        "You should ask me":
            hero.say "Well, I was kinda waiting for you to ask me!"
        "When I do":
            hero.say "I'll ask you out when I feel like it, and not before."
            $ anna.love -= 1
        "Be patient":
            hero.say "Hey, Anna - you just be patient now!"
            $ anna.love += 1
        "When you are ready":
            hero.say "I'll ask you out on a date just as soon as I think you're ready for one."
            $ anna.sub += 1
    return

label anna_love_5:
    anna.say "[hero.name] - what would you say if I...I don't know, maybe asked you over for drinks?"
    menu:
        "I would accept":
            hero.say "I'd make sure to be there, Anna - if that'd make you happy."
        "I'd check my schedule":
            hero.say "Ah...I'd need to check my diary first, make sure I didn't have someplace better to be."
            $ anna.love -= 1
        "I am the one who would ask":
            hero.say "Hey, are you calling me a bad friend?"
            hero.say "Isn't it me that's supposed to be the one asking you over?"
            $ anna.love += 1
        "It would be the best night for you":
            hero.say "I'd use the excuse of drinks to come over, sure."
            hero.say "But what I'd really want is to show you the night of your life!"
            $ anna.sub += 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
