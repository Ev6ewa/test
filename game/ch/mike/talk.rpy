label mike_talk_love:
    hero.say "What about you, Mike - got any good war stories about your past conquests?"
    show mike
    mike.say "Ah, geez...not really - I've never been all that lucky in love..."
    $ mike.love -= 1
    hide mike
    return

label mike_talk_sex:
    hero.say "I love the fact that we're becoming more liberated these days, that we can talk about sex whenever we want."
    show mike
    mike.say "Yeah, it's pretty neat - I mean, I love having sex!"
    "I have to chuckle at his two-dimensional response."
    hero.say "Yeah, Mike - I already got that!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_politics:
    hero.say "It's not long until the campaigning starts for the local elections."
    hero.say "But I'm still not sure which of the candidates I trust the most."
    show mike
    "Huh - candidates for what now?"
    $ mike.love -= 1
    hide mike
    return

label mike_talk_food:
    hero.say "It's like I WANT to eat healthy, but there are only so many hours in the day."
    hero.say "What about you, Mike?"
    show mike
    mike.say "It's all about convenience for me - junk food all the way."
    $ mike.love += 1
    hide mike
    return

label mike_talk_travels:
    hero.say "Sometimes I feel like a failure when I look at how many of my friends have gone off and travelled the world."
    show mike
    mike.say "It's no big deal."
    mike.say "Hell, I've never even been outside the country."
    $ mike.love += 1
    hide mike
    return

label mike_talk_tv:
    hero.say "Urrgh...everyone keeps on telling me about what new series I need to watch when I'm only halfway through the last one!"
    show mike
    mike.say "I know, I know - so many decent TV shows out there and so little time."
    $ mike.love += 1
    hide mike
    return

label mike_talk_sports:
    hero.say "Hey, the new football season's starting this weekend - wanna catch a game?"
    show mike
    mike.say "Nah...not really my cup of tea."
    $ mike.love -= 1
    hide mike
    return

label mike_talk_fashion:
    hero.say "What do you think of this outfit, Mike?"
    show mike
    mike.say "Whatever...less is more, I guess..."
    $ mike.love -= 1
    hide mike
    return

label mike_talk_books:
    hero.say "I just finished this book that my friend recommended."
    hero.say "I swear that I clould not put it down!"
    show mike
    mike.say "What's it called?"
    mike.say "Maybe I could borrow it?"
    mike.say "I love books."
    $ mike.love += 1
    hide mike
    return

label mike_talk_people:
    hero.say "It's so important to get out and meet new people every now and again."
    hero.say "People that'll actually listen to what you have to say."
    show mike
    mike.say "Who's listening to who say what now?"
    $ mike.love -= 1
    hide mike
    return

label mike_talk_computers:
    hero.say "My laptop's been playing up recently."
    hero.say "You work with computers, don't you, Mike?"
    show mike
    mike.say "Please, Bree - I don't want to talk about work."
    mike.say "I'd rather talk about you."
    $ mike.love += 1
    hide mike
    return

label mike_talk_music:
    hero.say "Sasha always seems to be playing heavy metal as loud as she can!"
    show mike
    mike.say "I know, Bree - I do have ears, and she's going to make them bleed!"
    $ mike.love += 1
    hide mike
    return

label mike_talk_birthday:
    show mike
    hero.say "Happy birthday, Mike!"
    mike.say "Aw, thanks, Bree - feels like you're the only one that thinks about me around here."
    $ mike.love += 1
    hide mike
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
