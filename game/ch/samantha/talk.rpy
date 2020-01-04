label samantha_talk_love:
    show samantha
    $ result = randint(1,4)
    if result == 1:
        hero.say "You know how they say we only use 10 percent of our brains?"
        samantha.say "I think we only use 10 percent of our hearts."
    elif result == 2:
        samantha.say "Love is like jumping out of an airplane with no parachute."
        samantha.say "But there’s no need to be frightened, because that plane is still on the ground."
    elif result == 3:
        hero.say "If love were a dolphin with wings and a unicorn’s horn, being ridden by a blind leprechaun dressed like Rasputin,"
        hero.say "would you believe in second chances for love at first sight?"
    else:
        hero.say "99 percent honesty is the foundation of any relationship."
        samantha.say "What do you do with the 1 percent left ?"
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_sex:
    show samantha
    $ result = randint(1,3)
    if result ==1:
        hero.say "I saw a gay porno once."
        hero.say "I didn't know until halfway in."
        hero.say "The girls never came."
        hero.say "The girls never came!"
    elif result ==2:
        if 4 < samantha.get_flag_value("story") < 8 and samantha.get_status() != "girlfriend":
            "Samantha licks her lips."
            samantha.say "...I miss the taste of cum..."
        else:
            samantha.say "You know I can taste Ryan's cum even if I blew him more than two hours ago."
            samantha.say "Yummy"
            hero.say "Gross, you just kissed my cheek."
    else:
        samantha.say "You could not be any more wrong."
        samantha.say "You could try, but you would not be successful."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_politics:
    show samantha
    $ result = randint(1,4)
    if result == 1:
        samantha.say "You shouldn't take life to seriously. You'll never get out alive."
        hero.say "That's so much like you."
    elif result == 2:
        hero.say "You know the world is going crazy when the best rapper is a white guy,"
        hero.say "the best golfer is a black guy, the tallest guy in the NBA is Chinese,"
        hero.say "the Swiss hold the America's Cup, France is accusing the U.S. of arrogance,"
        hero.say "Germany doesn't want to go to war,"
        hero.say "and the three most powerful men in America are named 'Bush', 'Dick', and 'Colin'."
        hero.say "Need I say more?"
        samantha.say "You are so funny."
    elif result == 3:
        hero.say "Every politician has a promising career."
        hero.say "Unfortunately, most of them do not keep those promises."
    else:
        samantha.say "I am quite worried about those climatic events happening all over the world."
        samantha.say "Our planet is runing toward the apocalypse."
        hero.say "Don't worry..."
        hero.say "The planet will be fine."
        hero.say "...But the people are fucked."
        samantha.say "That doesn't reassure me."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_food:
    show samantha
    $ result = randint(1,2)
    if result == 1:
        samantha.say "Do you know if they make semen flavored food ?"
        hero.say "Yuck..."
        hero.say "But I can be your vending machine if you want."
        $ samantha.sub += 1
    else:
        samantha.say "I cook with wine, sometimes I even add it to the food."
        $ samantha.love += 1
    hide samantha
    return

label samantha_talk_travels:
    show samantha
    $ result = randint(1,2)
    if result == 1:
        samantha.say "I really want to go to Paris some day."
        hero.say "Why would you do that, it's full of french people."
    else:
        samantha.say "How can you ever be late for anything in London?"
        samantha.say "They have a huge clock right in the middle of the town."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_tv:
    show samantha
    samantha.say "I don't watch TV that much."
    hide samantha
    return

label samantha_talk_sports:
    show samantha
    samantha.say "A blonde golfer goes into the pro shop and looks around frowning."
    samantha.say "Finally the pro askes her what she wants."
    samantha.say "'I can't find any green golf balls' the blonde golfer complains."
    samantha.say "The pro looks all over the shop, and through all the catalogs, and finally calls the manufacturers and determines that sure enough, there are no green golf balls."
    samantha.say "As the blonde golfer walks out the door in disgust, the pro asks her, 'Before you go, could you tell me why you want green golf balls?'"
    samantha.say "'Well obviously, because they would be so much easier to find in the sand traps!'"
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_fashion:
    show samantha
    $ what = randchoice([
        "I have a really good fashion sense but i'm just too poor to prove it.",
        "There is a thin line between looking indie and looking homeless."
        ])
    samantha.say "[what]"
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_books:
    show samantha
    samantha.say "I only read children's books."
    hide samantha
    return

label samantha_talk_people:
    show samantha
    samantha.say "It's horrible. Some kid called me 'young lady'."
    hero.say "Ugh, I hate when my father calls me that."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_computers:
    show samantha
    samantha.say "I like video games, but they're really violent."
    samantha.say "I'd like to play a video game where you help the people who were shot in all the other games."
    samantha.say "It'd be called 'Really Busy Hospital."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_music:
    show samantha
    samantha.say "I listen to wahtever is on the radio."
    hide samantha
    return

label samantha_talk_ryan:
    show samantha
    $ story = samantha.get_flag_value("story")
    if story <= 2:
        hero.say "I wanted to talk to you about Ryan."
        samantha.say "He is annoying at times, but so sweet I can't help but forgive him."
    elif story == 3:
        hero.say "Have you chosen a date for the wedding?"
        samantha.say "No, not yet."
    elif story == 4:
        hero.say "Samantha, I have something to tell you..."
        samantha.say "What's up, you look grim."
        hero.say "I saw Ryan at the nightclub."
        hero.say "He was with another girl..."
        samantha.say "WHAT..."
        samantha.say "THAT..."
        samantha.say "Are you sure..."
        samantha.say "Of course you are sure."
        samantha.say "How could I have been so stupid..."
        samantha.say "Believing I was special..."
        hero.say "You are special, he is just an ass and don't deserve you."
        samantha.say "Thanks [hero.name], I'll talk with him."
        $ samantha.set_flag("story",5)
    else:
        samantha.say "Ryan, really is an asshole, I prefere not to talk about him."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_birthday:
    show samantha
    hero.say "Happy birthday Samantha."
    samantha.say "Thank you [hero.name]."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_date:
    show samantha
    hero.say "Let's go on our date Samantha."
    samantha.say "Ok."
    $ samantha.love += 1
    hide samantha
    call date from _call_date_1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
