label samantha_desire_0:

    $ result = randint(1,5)
    if result == 1:
        hero.say "So, do you think you'll ever get married ?"
        samantha.say "Well, maybe eventually some fall day, possibly in a big park."
        samantha.say "Simple ceremony."
        samantha.say "We'll write our own vows."
        samantha.say "Band, no DJ."
        samantha.say "People will dance..."
        if not samantha.get_flag_value("storyA"):
            samantha.say "I'm not gonna worry about it, but I am not sure Ryan will be up to it."
            hero.say "That's something you sould discuss with him."
        elif samantha.get_status() != "girlfriend":
            samantha.say "Nothing hotter than a girl planning out her own imaginary wedding, huh ?"
            hero.say "Actually, I think it's cute."
        else:
            hero.say "Let's hope I'll stand beside you."
    elif result == 2:
        samantha.say "I totally wanted to come."
        hero.say "Maybe I could help you with that."
        if not samantha.get_flag("storyA"):
            samantha.say "Lol."
        else:
            if not samantha.get_flag_value_value("storyA"):
                samantha.say "Stop joking around."
            else:
                samantha.say "Anytime you want."
                $ samantha.sub += 1
            $ samantha.love += 1
    elif result == 3:
        $ c = randchoice(["trouser","shirt","cap","vest"])
        $ color1 = randchoice(["blue","red","yellow"])
        $ color2 = randchoice(["green","orange","pink"]).capitalize()
        samantha.say "Nice [c]."
        hero.say "Right? Right?"
        hero.say "Look at those colors."
        hero.say "[color1] and [color2], together at last."
        samantha.say "Is it new?"
        hero.say "That's the crazy part."
        hero.say "I've had this [c] for like six years."
        hero.say "Until this morning, I wasn't into it at all, but now, it's like my tastes have changed."
        $ samantha.love += 1
    elif result == 4:
        if samantha.get_status() != "girlfriend":
            hero.say "Maybe it's time to start forming some second impressions."
            samantha.say "You're finally gonna watch Big Trouble in Little China again?"
            hero.say "Not Goonies-- girls."
            hero.say "What if there's someone from my past who I thought was wrong for me at the time, when in fact she is actually a perfect fit?"
            samantha.say "Hold up."
            samantha.say "You know, this isn't a bad idea."
            samantha.say "Let's think [hero.name]'s greatest hits."
            samantha.say "What about Chelsea?"
            "I had so many fond memories of her: The scented oils on her dresser..."
            "The teddy bear collection on her bed..."
            "That one Aladdin song she always listened to..."
            "Her smile..."
            hero.say "Man, I haven't seen her in, like, maybe four years."
            samantha.say "Well, why'd you guys break up?"
            hero.say "I just wasn't looking for a big commitment at the time."
            hero.say "Maybe I should call her."
            hero.say "Wonder if she even remembers me."
        else:
            hero.say "You know, I am glad we found each other."
        $ samantha.love += 1
    else:
        if randint(1,2) == 1:
            if not samantha.get_flag_value("storyA"):
                samantha.say "Ryan and I went to the pool the other day."
                $ what = randchoice([
                    "He spent the whole time looking at other girls",
                    "He is so sexy in a swimsuit.",
                    "Don't tell anyone but I blew him in the lockers",
                    "He made me come with his fingers in the water."
                    ])
                samantha.say "[what]"
                hero.say "Poor you..."
            elif samantha.get_status() != "girlfriend":
                samantha.say "Even if he cheated on me, I kind of miss my time with Ryan."
                hero.say "Don't worry, there are plenty of snakes in the wood."
                samantha.say "Isn't the expression about fishes?"
                hero.say "Yes, but we both know what you really need is a big snake."
                samantha.say "Lol"
            else:
                samantha.say "I don't know why I am dating you."
        else:
            if not samantha.get_flag_value("storyA"):
                samantha.say "I hope you'll manage to find someone soon."
            elif samantha.get_status() != "girlfriend":
                samantha.say "I hope we'll manage to find someone soon, we are damaged goods you know."
            else:
                samantha.say "I am glad we found each other."
    $ samantha.love += 1

    return

label samantha_desire_1:

    $ result = randint(1,5)
    if result == 1:
        if game.room == "nightclub":
            samantha.say "These clubs are supposed to be fun, right?"
            samantha.say "Why do I hate them so much?"
            hero.say "Because all of the stuff you're supposed to like usually sucks."
            samantha.say "Like these clubs or cruises."
            hero.say "Or New Year's Eve."
            samantha.say "Or the Super Bowl."
            hero.say "Or parades."
            samantha.say "The Rockettes."
            hero.say "Or parades."
            samantha.say "You said that already."
            hero.say "I really hate parades."
            samantha.say "Okay."
        else:
            samantha.say "You know I hate sundays..."
            hero.say "Why?"
            samantha.say "It's like the whole world is dead."
            hero.say "But on monday it's resurection day!"
    elif result == 2:
        samantha.say "You know, I found sleeping deeply relaxing."
        hero.say "Yeah?"
        samantha.say "And interesting too."
        samantha.say "I find out a lot about myself by sleeping."
        samantha.say "Dreams, they are who I am when I’m too tired to be me."
        hero.say "You may be tired of yourself, but I never get to that point."
        hero.say "You are way too much fun."
    elif result == 3:
        hero.say "I tell you, Samantha you should try new things..."
        samantha.say "I don't know..."
        samantha.say "I heard that if you're too open-minded; your brains will fall out."
        hero.say "Very funny..."
    elif result == 4:
        hero.say "The female mind is certainly a devious one."
        samantha.say "Well, of course it is. It has to deal with the male one."
    else:
        if randint(1,2) == 1:
            if not samantha.get_flag_value("storyA"):
                samantha.say "Ryan and I went to the park yesterday."
                $ what = randchoice([
                    "I can't believe he hit on that girl while I was here.",
                    "I couldn't stop looking at his ass.",
                    "We fucked behind a tree.",
                    "He ate my pussy behind a bush."
                    ])
                samantha.say "[what]"
                hero.say "Poor you..."
            elif samantha.get_status() != "girlfriend":
                samantha.say "Ryan was really an ass."
                hero.say "Yes but you were the best half of it."
                samantha.say "What?"
                hero.say "Your ass was the best part of your couple's butt."
                samantha.say "Lol"
            else:
                samantha.say "You should try harder to be sexy, make me feel desired."
        else:
            if samantha.love() >= 120:
                samantha.say "I wonder why you never tried to get in my pants."
                samantha.say "Am I not sexy?"
            else:
                samantha.say "Nice talking to you."
    $ samantha.love += 1

    return

label samantha_desire_2:

    $ result = randint(1,5)
    if result == 1:
        samantha.say "Last night I was seriously considering whether I was a bisexual or not, but I don’t think so."
        samantha.say "Though I’m not sure if I’d like to be and..."
        hero.say "I don’t think there’s anything wrong with that, if you like a person, you like the person, not their genitals."
        hero.say "But if you are, I definitly want to be a part of it."
    elif result == 2:
        hero.say "If I had a dollar for every time a random woman walked up to me and tried to seduce me, I'd have 50 cents."
        hero.say "That's assuming drag queens are half price."
        samantha.say "I am pretty sure you are exagerating."
    elif result == 3:
        samantha.say "The most enjoyable book in the world is the phone book."
        samantha.say "Because think of all the sex that went into creating the content."
    elif result == 4:
        hero.say "Yesterday I saved a baby, a boy, a man, and an old man from death, and all by simply not impregnating anybody."
        hero.say "But I don't consider myself a hero."
        hero.say "Merely heroic, and also unable to reach any of my lady friends on the phone."
    else:
        "Samantha is looking at me, biting her lips."
        if randint(1,2) == 1:
            if not samantha.get_flag_value("storyA"):
                samantha.say "Ryan told me that you were in love with me when we lived together."
                hero.say "That traitor..."
                hero.say "It was more a crush than anything else."
                hero.say "And I am totally over it."
                samantha.say "Oh, really?"
                $ samantha.love += 1
            elif samantha.get_status() != "girlfriend":
                samantha.say "Are you really over it?"
                hero.say "Over what?"
                samantha.say "Me."
                $ result = renpy.display_menu([("Yes",1),("No",2),("Not sure",3)])
                if result == 1:
                    hero.say "Yes completly."
                    samantha.say "Too bad..."
                    $ samantha.love -= 1
                elif result == 2:
                    hero.say "Not really."
                    samantha.say "Good to know."
                    $ samantha.love += 1
                else:
                    hero.say "I am no sure."
                    samantha.say "Tell me when you are."
                    $ samantha.love += 1
            else:
                samantha.say "You are pretty good looking you know..."
                hero.say "Thanks, you are a fine piece of ass yourself."
                $ samantha.love += 1
        else:
            samantha.say "Maybe I made a mistake last year..."
            hero.say "What do you mean ?"
            samantha.say "Nothing."
    $ samantha.love += 1

    return

label samantha_desire_3:

    $ result = randint(1,5)
    if result == 1:
        samantha.say "I’m a Pisces, and people say that Pisces make the best lovers."
        samantha.say "That’s because Pisces are fish, and it’s like my grandpa always used to say :"
        samantha.say "'The next best thing to making love to a mermaid, is having sex with a fish.'"
        $ samantha.love += 1
    elif result == 2:
        samantha.say "I could really suck a dick right now.."
        hero.say "Ergh?"
        samantha.say "Did I say that out loud?"
        $ samantha.love += 1
    elif result == 3:
        if not samantha.get_flag_value("storyA"):
            samantha.say "Ryan is always looking at other girls 's asses..."
            samantha.say "Is my ass that bad?"
        else:
            "Samantha looks fidgetty, she is doing weird motions."
            hero.say "What are you doing?"
            samantha.say "Exercises to tighten my pussy..."
    elif result == 4:
        hero.say "My throat is sore..."
        hero.say "I tried to eat a banana in one go earlier, I couldn't but I learnt something valuable: Girls that can deep throat are fucking under appreciated!"
        samantha.say "Thanks for the compliment."
    else:
        samantha.say "I am thinking of changing my look."
        if randint(1,2) == 1:
            samantha.say "What do you think I should try."
            $ result = renpy.display_menu([("Changing your hair color",2),("Getting pierced",3),("Getting tatoos",4),("Getting cum on your face",1)])
            if result == 1:
                hero.say "I think you would look great with my cum all over your lips."
                if not samantha.get_flag_value("storyA"):
                    samantha.say "Oh, really..."
                    if samantha.love() >= 100:
                        if samantha.get_flag_value("story") == 8:
                            samantha.say "I am a married woman, you know... To your friend."
                        else:
                            samantha.say "I have a boyfriend, you know... Your friend."
                        hero.say "A blowjob from you is worth a tousand friends."
                        $ samantha.love += 1
                    else:
                        samantha.say "Better not tell Ryan about that comment."
                        $ samantha.love -= 1
                    $ samantha.love += 1
                elif samantha.get_status() != "girlfriend" and samantha.love() >= 120:
                    samantha.say "I should try it sometime."
                    hero.say "Just send me a text when you are ready."
                    samantha.say "Ok."
                    $ samantha.love += 1
                else:
                    samantha.say "Next time we are alone, we must do that then."
                    hero.say "Let's get to my room."
                    samantha.say "Lol."
                    $ samantha.love += 1
            elif result == 2:
                hero.say "Maybe you could try to dye your hair red..."
                samantha.say "Like my friend Jessica?"
                if "jessica" not in GIRLS or "jessica" in HIDDEN:
                    hero.say "I don't know her."
                    samantha.say "She's a nice girl, she works at the flower shop, in the mall."
                samantha.say "Anyway, I think I look best as a blond."
                hero.say "And like this nobody can be fooled into thinking that you have a brain."
                samantha.say "Ha, Ha , Ha... Jerk."
                $ samantha.love += (randint(0,2) - 1)
            elif result == 3:
                hero.say "Maybe you could try to get a piercing."
                samantha.say "I don't know..."
                if samantha.love() >= 80:
                    samantha.say "I already got my navel pierced..."
                    hero.say "I know, and that's damn sexy if you ask me."
                    $ samantha.love += 1
                    if samantha.love() >= 100:
                        "Samantha's cheek get a little red."
                        samantha.say "...And both my nipples..."
                        "I swallow slowly..."
                        $ samantha.love += 1
                        if samantha.love() >= 120:
                            "Samantha's breath get faster."
                            samantha.say "...And my clit too."
                            "I can feel my pants tightening."
                            $ samantha.love += 1
                    samantha.say "So, I am not sure anymore would be good."
                    samantha.say "It might get too much."
                    "She looks delighted by the effect she had on me."
                $ samantha.love += 1
        else:
            samantha.say "Maybe I'll shave my head."
            if samantha.get_flag_value("story") <= 4:
                hero.say "No, you'd better lose a boyfriend, you would look great without one."
            elif samantha.get_flag_value("story") == 8:
                hero.say "No, you'd better lose a husband, you would look great without one."
            else:
                hero.say "Yeah, and I'll wear makeup."
            samantha.say "stop kidding..."

    return

label samantha_desire_4:

    $ result = randint(1,5)
    if result == 1:
        samantha.say "I lost a little weight over the weekend."
        samantha.say "I cut my fingernails."
    elif result == 2:
        samantha.say "A guy and a girl can be just friends, but at one point or another, they will fall for each other..."
        samantha.say "Maybe temporarily, maybe at the wrong time, maybe too late, or maybe forever"
    elif result == 3:
        samantha.say "Man may have discovered fire, but women discovered how to play with it."
    elif result == 4:
        samantha.say "Well, it seems to me that the best relationships - the ones that last - are frequently the ones that are rooted in friendship."
        samantha.say "You know, one day you look at the person and you see something more than you did the night before."
        samantha.say "Like a switch has been flicked somewhere. And the person who was just a friend is..."
        samantha.say "suddenly the only person you can ever imagine yourself with."
    elif result == 5:
        samantha.say "I would give anything if you were two people, so I could call up the one who is my friend and tell her about the one I like so much."
    $ samantha.love += 1

    return

label samantha_desire_5:
    $ result = randint(1,5)
    if result == 1:
        samantha.say "I suffer from girlnextdooritis where the guy you love is friends with you and that's it."
    elif result == 2:
        samantha.say "Try not to think about me sucking you."
    elif result == 3:
        samantha.say "I had a naughty dream last night and guess who was in it?"
        samantha.say "I'll give you a hint. I'm talking to him right now."
    elif result == 4:
        samantha.say "Have you ever had a wet dream with me in it? Be honest..."
    else:
        samantha.say "If you could do anything you want to me, what would you do?"
    $ samantha.love += 1

    return

label samantha_love_0:
    $ result = randint(1,6)
    if game.get_flag_value("gaymistake") == 1:
        hero.say "Do you believe one of my colleagues thought I was gay..."
        hero.say "Couldn't do any work after that. I mean, is that ridiculous? Can you believe she actually thought that?"
        samantha.say "Um... yeah. Well, I mean, when I first met you, y'know, I thought maybe, possibly, you might be..."
        hero.say "You did?"
        samantha.say "Yeah, but then you spent Ryan's entire birthday party talking to my breasts, so then I figured maybe not."
        hero.say "Well, this is fascinating. So, uh, what is it about me?"
        samantha.say "I dunno, 'cause you're smart, you're funny..."
        hero.say "Ryan is smart and funny, d'you ever think that about him?"
        samantha.say "Yeah! Right!"
        hero.say "WHAT IS IT?!"
        samantha.say "Okay, I-I d'know, you-you just- you have a quality."
        hero.say "Oh, oh, a quality, good, because I was worried you were gonna be vague about this."
        $ game.set_flag("gaymistake",2)
    elif result == 1:
        hero.say "Sometimes, my neck gets sore."
        samantha.say "Why?"
        hero.say "Because my brain is so big."
        "Samantha smirks a little."
    elif result == 2:
        samantha.say "When you stop expecting people to be perfect, you can like them for who they are."
    elif result == 3:
        hero.say "Why is it, I feel I've known you so many years?"
        samantha.say "Because I like you, and I don't want anything from you."
    elif result == 4:
        samantha.say "Every man I meet wants to protect me."
        samantha.say "I can't figure out what from."
    elif result == 5:
        samantha.say "What did Cinderella do when she got to the ball?"
        hero.say "Gagged."
    else:
        hero.say "The most painful thing is losing yourself in the process of loving someone too much, and forgetting that you are special too."
    $ samantha.love += 1

    return

label samantha_love_1:

    $ result = randint(1,5)
    if result == 1:
        samantha.say "Insanity is doing the same thing, over and over again, but expecting different results."
    elif result == 2:
        samantha.say "Women and cats will do as they please, and men and dogs should relax and get used to the idea."
    elif result == 3:
        samantha.say "The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it."
    elif result == 4:
        samantha.say "The statistics on sanity are that one out of every four people is suffering from a mental illness."
        samantha.say "Look at your 3 best friends."
        samantha.say "If they're ok, then it's you."
    else:
        samantha.say "My motto is get out before they go down."
        hero.say "That is so not my motto."
    $ samantha.love += 1

    return

label samantha_love_2:
    $ result = randint(1,5)
    if result == 1:
        hero.say "When you're in jail, a good friend will be trying to bail you out."
        hero.say "A best friend will be in the cell next to you saying, 'Damn, that was fun'."
        samantha.say "No, a best friend would have stopped you from doing a stupid thing altogether."
    elif result == 2:
        samantha.say "Some humans would do anything to see if it was possible to do it."
        samantha.say "If you put a large switch in some cave somewhere, with a sign on it saying 'End-of-the-World Switch. PLEASE DO NOT TOUCH', the paint wouldn't even have time to dry."
    elif result == 3:
        samantha.say "I generally avoid temptation unless I can't resist it."
    elif result == 4:
        samantha.say "How can you tell when a blonde is dating?"
        hero.say "I don't know."
        samantha.say "By the buckle print on her forehead."
        samantha.say "How can you tell who is a blonde's boyfriend?"
        hero.say "Still don't know."
        hero.say "He's the one with the belt buckle the matches the impression in her forehead."
    else:
        if not samantha.get_flag("birthdayknown"):
            hero.say "Hey Samantha, when is your birthday ?"
            samantha.say "It's on the [samantha.birthday[1]] of [samantha.birthday[0]]."
            samantha.say "Are you planning on getting me a gift ?"
            hero.say "Maybe..."
            $ samantha.set_flag("birthdayknown")
        else:
            hero.say "I’m not so good with advices."
            hero.say "Can I interest you in a sarcastic comment?"
    $ samantha.love += 1

    return

label samantha_love_3:

    $ result = randint(1,5)
    if result == 1:
        samantha.say "How does a guy know if he has a high sperm count?"
        hero.say "Don't know."
        samantha.say "If the girl has to chew, before she swallows."
    elif result == 2:
        samantha.say "You know..."
        hero.say "What?"
        samantha.say "Don't tell but I have this weird kink, like sexual..."
        samantha.say "I like sucking dick almost as much as being fucked..."
        hero.say "Interesting."
    elif result == 3:
        samantha.say "I went to the movie theater the other day.."
        samantha.say "There was a girl blowing her boyfriend there..."
        samantha.say "I saw her get his cum splattered all over her face."
        samantha.say "She cleaned it up with her tongue and fingers..."
        samantha.say "That was so hot."
    elif result == 4:
        samantha.say "I could totally eat a banana right now."
    else:
        samantha.say "So do you have a girlfriend?"
    $ samantha.love += 1

    return

label samantha_love_4:

    $ result = randint(1,5)
    if result == 1:
        samantha.say "What's the difference between a blonde and a mosquito?"
        hero.say "Don't know."
        samantha.say "One stops sucking when you smack it."
    elif result == 2:
        samantha.say "I never tried anal sex..."
        hero.say "You know, we could fix that."
    elif result == 3:
        samantha.say "I kind of like blonde jokes."
        hero.say "I noticed."
    elif result == 4:
        samantha.say "Don't you think girls that are honest with there desires are the sexiest?"
    else:
        samantha.say "I would totally eat a twinkie..."
    $ samantha.love += 1


    return

label samantha_love_5:

    $ result = randint(1,5)
    if result == 1:
        samantha.say "What's the definition of trust?"
        hero.say "Don't know."
        samantha.say "Two cannibals giving each other a blowjob."
    elif result == 2:
        samantha.say "You know I don't have any gag reflex?"
    elif result == 3:
        samantha.say "I watched porn the other day, that girl had her whole face covered with the cum from a dozen guys."
        samantha.say "I thought she looked like me a little."
    elif result == 4:
        samantha.say "So, how is life with your roommates?"
    else:
        samantha.say "I don't think I ever had a closer friend than you."
    $ samantha.love += 1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
