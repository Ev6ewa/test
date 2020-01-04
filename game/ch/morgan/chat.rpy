label morgan_desire_0:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "God, I used to love just hanging out back when we were kids."
        morgan.say "It felt like having nothing to do was actually doing something back then."
    elif morgan.sub <= 75:
        morgan.say "I miss the times we had when we were kids, [hero.name]."
        morgan.say "Life was so much simpler back then."
    else:
        morgan.say "I always loved to spend time chatting and joking when we were kids!"
        morgan.say "You were so funny, even back then, [hero.name]!"
    menu:
        "I just loved to hang":
            hero.say "Just kicking back and wasting time was so sweet back in the day."
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "Those times were great":
            hero.say "Yeah - things certainly seemed less complicated."
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "I always wanted a heart-to-heart":
            hero.say "I had the best of times when he shared our hopes and dreams with each other, Morgan..."
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_desire_1:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "You remember the bike races that we used to have around the neighbourhood?"
        morgan.say "That one time that Jack fell off, scraped his knees up and wailed like a little pussy?"
    elif morgan.sub <= 75:
        morgan.say "Do you still ride a bike, [hero.name]?"
        morgan.say "I sometimes go mountain biking at the weekends."
    else:
        morgan.say "Ah, I can remember riding around on our bikes together forever!"
        morgan.say "I always thought we'd ride away into the sunset together some day..."
    menu:
        "You were some rider!":
            hero.say "You were some mean rider, Morgan - it was you that drove Jack off of the road!"
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "I ride an exercise bike":
            hero.say "No - sad to say the closest I get these days is the exercise bike at the gym!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "Your bike was pink!":
            hero.say "You had a pink bike, with tassels and unicorns on it - which I thought was weird, because I also thought you were a boy!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_desire_2:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "I still have nightmares about that vicious dog that used to live on our walk home from school."
        morgan.say "Remember how we all used to shit ourselves when we had to run past house where it lived?"
    elif morgan.sub <= 75:
        morgan.say "I've never liked dogs - ever since we used to walk past that vicious mutt on the way home from school!"
    else:
        morgan.say "Oh, [hero.name] - do you remember that mean old dog that always frightened me on the way home from school?"
        morgan.say "I still have bad dreams about it, even now!"
    menu:
        "You were never scared":
            hero.say "Huh...you were never scared, Morgan - you looked that mean old mutt straight in the eye and didn't flinch once!"
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "You need to meet the right dog":
            hero.say "I think dogs are like people, Morgan."
            hero.say "Maybe you just haven't met the right one yet?"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "Yeah, you were terrified!":
            hero.say "Yeah, you used to cry the whole way home, Morgan!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_desire_3:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "I guess I was always trying to be as tough as the boys when I was little."
        morgan.say "But it was only because I thought it'd make you notice me more..."
    elif morgan.sub <= 75:
        morgan.say "I feel more at ease in my skin than ever right now."
        morgan.say "And I'm glad that we've reconnected when I'd sorted my shit out!"
    else:
        morgan.say "Ah, I used to follow you around all the time, [hero.name]."
        morgan.say "All I wanted was for you to notice me!"
    menu:
        "Sorry I thought you were a guy":
            hero.say "You were good at it too - I'm just sorry I wasn't smart enough to see you weren't a guy, Morgan."
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "You seem more confident":
            hero.say "It was worth the wait - you're pretty fun to be around these days, Morgan!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "You were like a little puppy":
            hero.say "Aw, I remember you - always at my heels, like an eager little puppy!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_desire_4:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "You know, I'm not that good at talking about my feelings."
        morgan.say "But hooking up with you again's really reminded me of how much I used to have a crush on you!"
    elif morgan.sub <= 75:
        morgan.say "It's weird, but I never thought that I'd have a chance to do all of the things that I always wanted to do with you, [hero.name]!"
    else:
        morgan.say "Oh, [hero.name] - since we met up again, you've rekindled all of the old feelings I used to have for you!"
    menu:
        "I'm no good at this shit either!":
            hero.say "It's hard for me to say it too, Morgan - but I'm loving having you back around too."
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "It's like a second chance":
            hero.say "I feel the same way, Morgan - like we've been given a second chance."
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "I'm all touchy-feely!":
            hero.say "Oh, Morgan - you really should just say what you feel is inside, it'll set you free!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_desire_5:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "[hero.name]...this is hard for me to say...real hard."
        morgan.say "But, I think I love you - more now than I ever did when we were kids..."
    elif morgan.sub <= 75:
        morgan.say "It's hard to say this, [hero.name] - but I think I'm really falling for you!"
    else:
        morgan.say "Oh, [hero.name] - I always loved you when we were young."
        morgan.say "And now that we're together again, I've fallen for you all over again - it's like some kind of fairy-tale come true!"
    menu:
        "Geez, I sorta feel the same way too!":
            hero.say "Ah...this is gonna make me sound stupid, Morgan - but I think I love you too!"
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "I'm so glad you said that first":
            hero.say "I'm kind of glad you came out and said that first, Morgan."
            hero.say "Because I've been struggling to say the same thing too!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "It was simply meant to be!":
            hero.say "I think it's fate, Morgan, destiny - it was written in the stars that we're supposed to be together!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_love_0:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "Do you remember that first summer that Jack started growing his hair and listening to heavy metal?"
    elif morgan.sub <= 75:
        morgan.say "I always felt a bit jealous of Jack, what with him being so into his music and all that."
    else:
        morgan.say "Do you remember when Jack had all that greasy hair and listened to such awful music?"
    menu:
        "He never looked back":
            hero.say "Yeah, and he's never looked back since - that guy'll be metal until the day he dies!"
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "He's still following his vision":
            hero.say "Well, he was always a kind of all or nothing guy - and I guess he still is!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "He's still a greasy slob":
            hero.say "Yeah, he never got any less greasy and spotty - just bigger and fatter!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_love_1:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "You know, I never forgave Alexis for what she did to you back in high school."
        morgan.say "I came real close to punching her in the mouth, more than once..."
    elif morgan.sub <= 75:
        morgan.say "That was really harsh, you know - what Alexis did to you back in high school?"
    else:
        morgan.say "I always hated Alexis after she cheated on you back in high school."
        morgan.say "I would never have done that to you...never!"
    menu:
        "You could have given her one from me":
            hero.say "I wouldn't have stopped you from hitting her, Morgan - in fact, you could have given her one from me, too!"
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "It was a long time ago":
            hero.say "Thanks, Morgan - I appreciate that."
            hero.say "But it was a long time ago, and I'd rather concentrate on the here and now."
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "I don't think violence is the answer":
            hero.say "Don't ever sink to her level, Morgan - or else you'd be as bad as her!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_love_2:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "Kylie always used to freak me out when she was a little kid."
        morgan.say "The way she'd stare at you with those cold, dead eyes!"
    elif morgan.sub <= 75:
        morgan.say "I never liked Kylie - she always gave me the creeps!"
    else:
        morgan.say "Urgh...I was always scared of Kylie."
        morgan.say "She was such a creepy little kid!"
    menu:
        "She hasn't changed much":
            hero.say "You should see her now - she hasn't changed all that much!"
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "She has a strange vibe":
            hero.say "I know what you mean - she's pretty intense!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "Don't worry, I'll protect you":
            hero.say "She's still pretty creepy, Morgan - but don't worry, I'll keep her away from you."
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_love_3:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "You were always such a tearaway when we were kids, [hero.name]."
        morgan.say "I often wonder if that's why you never noticed I was a girl!"
    elif morgan.sub <= 75:
        morgan.say "Be honest, [hero.name]..."
        morgan.say "Did you not realise I was a girl because it was a tomboy?"
        morgan.say "Or because you always had your head in the clouds?"
    else:
        morgan.say "Oh, I could never keep up with you when we were little, [hero.name]!"
        morgan.say "If only you'd slowed down a little, you might have noticed I was a girl!"
    menu:
        "You were a tearaway too!":
            hero.say "Hey, you were a handful too, Morgan - and you still are now!"
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "A little bit of both":
            hero.say "A little bit of both - but I see you clearly enough right now!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "I wish I had slowed down!":
            hero.say "If only I'd slowed down long enough, Morgan - I'd have seen how truly special you are!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_love_4:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "It's pretty weird, [hero.name] - how we went from kids that were friends to adults that are lovers."
        morgan.say "Don't you think?"
    elif morgan.sub <= 75:
        morgan.say "We walked a pretty long and weird path to get here, don't you think, [hero.name]?"
        morgan.say "I don't think I could have dreamed it up, no matter how I tried!"
    else:
        morgan.say "It's like something out of a fairy-tale, don't you think?"
        morgan.say "The little girl that loved the little boy that thought she was a little boy too but then found out she was a girl and then fell in love with each other?"
    menu:
        "You couldn't make it up":
            hero.say "It's kind of fucked up to be sure - but I love the way it all turned out in the end."
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "What are the chances":
            hero.say "I could never have imagined it, Morgan."
            hero.say "I'm just glad that it did."
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "It's like happy ever after!":
            hero.say "It makes me feel like I'm living in an enchanted storybook!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_love_5:
    if morgan.get_flag_value("male") >= 50:
        morgan.say "I like that we were friends before we were lovers, [hero.name]."
        morgan.say "I could never be without you as either, and I want to keep you as both."
    elif morgan.sub <= 75:
        morgan.say "I'm glad I found you again, [hero.name]."
        morgan.say "I got back and old friend...and a whole lot more."
    else:
        morgan.say "It's so cool that my lover and my best friend are less than two people!"
        morgan.say "We can hang out and be on a date at the same time!"
    menu:
        "We'll always be both":
            hero.say "Each one makes the other even stronger, Morgan."
            $ morgan.set_flag("male",1,mod="+")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        "I think we were meant to be":
            hero.say "I'd like to think that we were meant to find each other again."
            hero.say "That's how it feels to me!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "Friends with benefits":
            hero.say "We're like a two-for-one - friends with benefits!"
            $ morgan.set_flag("male",1,mod="-")
            $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
            if morgan.get_flag_value("male") > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
