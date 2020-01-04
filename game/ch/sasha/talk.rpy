label sasha_talk_love:
    show sasha
    $ result = randint(1,5)
    if sasha.get_flag_value("collared") and sasha.love >= 150:
        sasha.say "I love you Master."
    elif result == 1:
        hero.say "Why don't they ever a make a movie about what happens after they kiss?"
        sasha.say "They do, it's called porn."
    elif result == 2 and sasha.love() > 80 - hero.charm()/2:
        sasha.say "Have you ever been in love?"
        hero.say "Sure."
        sasha.say "Horrible isn't it?"
        hero.say "Why?"
        sasha.say "It makes you so vulnerable."
        sasha.say "It opens your chest and it opens up your heart and it means that someone can get inside you and mess you up."
        $ sasha.sub += 1
        $ sasha.love += 1
    elif result ==3:
        sasha.say "There is only one thing worse than a boy who hates you: a boy that loves you."
    elif result == 4 and not game.get_flag_value("female"):
        sasha.say "You're not gay, are you?"
        hero.say "If I were, I would dress better."
    else:
        hero.say "Why do women think the only way to get men to do what they want is to manipulate them?"
        sasha.say "Lot's of reason, really : "
        sasha.say "History, personal experience, romantic comedies."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_sex:
    show sasha
    $ result = randint(1,5)
    if sasha.get_flag_value("collared") and sasha.love >= 150:
        sasha.say "Please use me anyway you want Master."
    elif result == 1:
        hero.say "Why did God give men penises?"
        sasha.say "So they'd have at least one way to shut a woman up."
    elif result == 2:
        sasha.say "Which of the following words does not belong: meat, eggs, wife, blowjob."
        hero.say "Blowjob. You can beat your meat, eggs, and wife; but you can't beat a blowjob."
    elif result == 3:
        sasha.say "How do you circumcise a hillbilly?"
        hero.say "I don't know."
        sasha.say "Kick his sister in the jaw."
    elif result == 4:
        sasha.say "I don't know the question, but sex is definitely the answer."
    else:
        hero.say "What is the difference between oral and anal sex?"
        sasha.say "Dunno..."
        hero.say "Oral sex makes your day and Anal sex makes your whole week."
        $ sasha.sub += 1
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_politics:
    show sasha
    sasha.say "You're not to be so blind with patriotism that you can't face reality."
    sasha.say "Wrong is wrong, no matter who does it or says it."
    $ sasha.love -= 1
    hide sasha
    return

label sasha_talk_food:
    show sasha
    sasha.say "I don't understand dieting."
    sasha.say "Seize the moment."
    sasha.say "Remember all those women on the 'Titanic' who waved off the dessert cart."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_travels:
    show sasha
    sasha.say "Not all journeys seek an end."
    sasha.say "Some are their own purpose.."
    $ sasha.love += 2
    hide sasha
    return

label sasha_talk_tv:
    show sasha
    sasha.say "To attract a lover, you need to craft the perfect Craigslist ad."
    sasha.say "Here’s mine: Free TV with purchase of potato chips and couch."
    if hero.charm >= 30:
        $ sasha.sub += 1
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_sports:
    show sasha
    hero.say "The problem with winter sports is that -- follow me closely here -- they generally take place in winter"
    $ sasha.love += 2
    hide sasha
    return

label sasha_talk_fashion:
    show sasha
    $ result = randint(1,10)
    if result == 1:
        sasha.say "You can never be overdressed or overeducated."
    elif result == 2:
        sasha.say "A girl should be two things: classy and fabulous."
    elif result == 3:
        sasha.say "I don't know who invented high heels, but all women owe him a lot!"
    elif result == 4:
        sasha.say "Dress shabbily and they remember the dress; dress impeccably and they remember the woman."
    elif result == 5:
        sasha.say "The most beautiful makeup of a woman is passion. But cosmetics are easier to buy."
    elif result == 6:
        sasha.say "I love new clothes."
        sasha.say "If everyone could just wear new clothes everyday, I reckon depression wouldn’t exist anymore."
    elif result == 7:
        sasha.say "A woman who doesn't wear perfume has no future."
    elif result == 8:
        sasha.say "Whoever said that money can't buy happiness, simply didn't know where to go shopping"
    elif result == 9:
        sasha.say "A woman's dress should be like a barbed-wire fence: serving its purpose without obstructing the view."
    elif result == 10:
        sasha.say "It's a good thing I was born a girl, otherwise I'd be a drag queen."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_books:
    show sasha
    if hero.knowledge() > 20 and sasha.love() > 40:
        sasha.say "You get a little moody sometimes but I think that's because you like to read."
        sasha.say "People that like to read are always a little fucked up."
    else:
        hero.say "If you go home with somebody, and they don't have books, don't fuck 'em!"
    $ sasha.love -= 1
    hide sasha
    return

label sasha_talk_people:
    show sasha
    if not game.get_flag_value("female"):
        hero.say "I love women, but I feel like you can't trust some of them. Some of them are liars, you know?"
        hero.say "Like I was in the park and I met this girl, she was cute and she had a dog."
        hero.say "And I went up to her, we started talking. She told me her dog's name."
        hero.say "Then I said, 'Does he bite?' She said, 'No.' And I said, 'Oh yeah? Then how does he eat?' Liar."
    else:
        hero.say "I was never that good with people..."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_computers:
    show sasha
    sasha.say "I think computer viruses should count as life ..."
    sasha.say "I think it says something about human nature that the only form of life we have created so far is purely destructive."
    sasha.say "We've created life in our own image."
    $ sasha.love -= 1
    hide sasha
    return

label sasha_talk_music:
    show sasha
    if randint(1,2) == 1:
        sasha.say "Pop and metal aren't friends."
        sasha.say "Each knows exactly where the other lives and tries to keep its distance."
        sasha.say "They choose different streets, neighborhoods, zip codes."
    else:
        sasha.say "Heavy Metal would not exist without Led Zeppelin, and if it did, it would suck."
    $ sasha.love += 1
    hide sasha
    return

label sasha_talk_birthday:
    show sasha
    hero.say "Happy birthday Sasha."
    sasha.say "Thank you!"
    $ sasha.love += 5
    hide sasha
    return

label sasha_talk_date:
    show sasha
    hero.say "Let's go on our date Sasha."
    sasha.say "Ok."
    $ sasha.love += 1
    hide sasha
    call date from _call_date_4
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
