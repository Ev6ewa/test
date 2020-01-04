label morgan_talk_love:
    hero.say "What's your take on love, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "I think this baby is proof enough that it's real."
        $ morgan.love += 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "I'm not into all of that sappy stuff!"
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "I don't know if I believe in finding Mr Right...but I believe you can find happiness if you look for it."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "I think that there's someone for everyone."
        morgan.say "But if you're not prepared to look, then you won't find them!"
        $ morgan.love += 1
    else:
        morgan.say "Everyone should try to find true love!"
        $ morgan.love += 1
    if morgan.love >= 50:
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    hide morgan
    return

label morgan_talk_sex:
    hero.say "Have you got a philosophy when it comes to sex, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "It can lead you down some pretty life-changing roads."
        $ morgan.sub += 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Keep it fun and keep it casual - no one needs to be tied down when they can be having fun instead!"
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        $ morgan.set_flag("male",1,mod="+")
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "I've tried to be laid back about it in the past."
        morgan.say "But I definitely get more out of it when it's with someone I care about."
    elif morgan.sub < 75:
        morgan.say "Oh, [hero.name] - that's so rude!"
    else:
        morgan.say "Girls might try to pretend that they don't like it as much as guys do."
        morgan.say "But they're almost always lying!"
        $ morgan.love += 1
    if morgan.sub <= 25:
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_politics:
    hero.say "Elections are coming round again - will you be voting, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "Yeah, of course - I have someone else's future to think about now."
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "They're all a bunch of pricks and liars!"
        $ morgan.love += 1
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "They all talk like they want to do good, but you can't trust them once they're in office."
    elif morgan.sub < 75:
        morgan.say "I think the problem with politics is that the women in office try to sound like the men!"
    else:
        morgan.say "Phht...no way - politics is so boring!"
        $ morgan.love -= 1
    hide morgan
    return

label morgan_talk_food:
    hero.say "Think quickly, Morgan - eat out or takeout?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "If you want to take me out anytime soon - make it one of those all-you-can-eat buffets."
        morgan.say "This baby's got me eating like a horse!"
        $ morgan.love += 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Takeout, every time - less fuss more food!"
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "Depends on my mood - sometimes I wanna be wined and dined, sometimes I just want a dirty slice of pizza."
    elif morgan.sub < 75:
        morgan.say "I'm a modern girl - but I still like to be taken out for a surprise meal every now and then."
        $ morgan.love += 1
    else:
        morgan.say "Ooh, I love to be taken out to a fancy restaurant!"
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_travels:
    hero.say "If you could jet off anywhere in the world, where would it be?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "I'd like for us to go somewhere nice as a family, once the baby's here."
        $ morgan.love += 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "I'd like to do one of those extreme hiking holidays, like throught the desert or mountains, or something like that."
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        $ morgan.set_flag("male",1,mod="+")
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "Hmm...I guess I've always wanted to see Europe - like Paris and Berlin, that sort of thing."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "I'm sure you can soak up the culture of a place as well as soaking up some rays on the beach!"
        $ morgan.love += 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    else:
        morgan.say "Oh, there's so much fun stuff you can do at Disneyland Paris!"
        $ morgan.love += 1
    hide morgan
    return

label morgan_talk_tv:
    hero.say "There's fuck all on TV right now."
    hero.say "I don't know why I bother with it!"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "I try to watch it, but I fall asleep whenever I lay down on the sofa."
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Don't be such a pussy, man!"
        morgan.say "There's always a game or a fight on one of the channels."
        $ morgan.love -= 1
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "Just sign up for a streaming service, then you can please yourself."
    elif morgan.sub < 75:
        morgan.say "I always prefer to watch TV when I have someone worth snuggling down with..."
        $ morgan.love += 1
    else:
        morgan.say "I just watch Reality TV!"
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_sports:
    hero.say "Sports, sports, sports - that's all some people ever seem to talk about!"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "Those steriod-brained jocks want to try being pregnant - that'd show how tough they really are!"
        $ morgan.love -= 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "What do you mean you don't like sports?"
        morgan.say "You're a guy, aren't you?"
        $ morgan.love -= 1
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "I know - it's like they don't have anything else in their lives of any significant meaning."
        morgan.say "Sad, really."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "I know it's a cliche, but I don't get anything out of them."
        morgan.say "And before you say it - yes, I have tried!"
        $ morgan.love += 1
    else:
        morgan.say "Oh, I don't understand sports!"
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_fashion:
    hero.say "Do you keep up with what's supposed to be in fashion, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "Don't talk to me about fashion - it's the twenty-first century, and maternity clothes are still basically sacks with head and arm holes!"
        $ morgan.love -= 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Fuck that - fashion's for sheep!"
        $ morgan.love -= 1
        $ morgan.sub -= 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        $ morgan.set_flag("male",1,mod="+")
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "I always thought that fashion was just something designers cooked up to sell shitty clothes."
        morgan.say "There are classics that never go out of style - you just have to be able to spot them for what they are."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "Sure, I really want to be a feminist and reject all of that stuff."
        morgan.say "But there's still a real thrill to knowing that you look good!"
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    else:
        morgan.say "Oh yeah, it's important to always look your best!"
        $ morgan.love += 1
        $ morgan.sub += 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    hide morgan
    return

label morgan_talk_books:
    hero.say "Recommend a good book, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "You bet - all I've been doing lately is sprawling around like a whale of an evening and devouring books!"
        $ morgan.love += 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Nope - you should do things in life, not read about them."
        $ morgan.love -= 1
        $ morgan.sub -= 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        $ morgan.set_flag("male",1,mod="+")
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "Yeah, sure - I have far too many books at home."
        morgan.say "I just wish that I had time to read them all!"
        $ morgan.love += 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    elif morgan.sub < 75:
        morgan.say "Would you be mad with me if I said that I sometimes claim to have read pretty heavy classics, just to look smarter?"
        $ morgan.sub += 1
    else:
        morgan.say "If by books you mean beauty and fashion magazines - then yes, lots!"
        $ morgan.love -= 1
        $ morgan.sub += 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    return

label morgan_talk_people:
    hero.say "Are you a people person, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "Not really - the pregnancy's made me kinda anti-social."
        $ morgan.love -= 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Sure, I'm always the life and soul of the party!"
        $ morgan.love += 1
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "Well, that depends rather heavily on the persons involved..."
    elif morgan.sub < 75:
        morgan.say "If I'm honest - I like smaller, more intimate groups of friends."
        $ morgan.sub += 1
    else:
        morgan.say "Oh yeah - I'm always being called bubbly and outgoing!"
        $ morgan.love += 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    hide morgan
    return

label morgan_talk_computers:
    hero.say "Do you keep up to speed with the world of computers, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "I've been getting better since I found myself stuck inside most of the time."
        $ morgan.love -= 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "I know how to turn one on and find some decent porn - what more is there to know?"
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        $ morgan.set_flag("male",1,mod="+")
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "I'm no hacker or anything like that, but I know as much as the next person...maybe a little more, even."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "I know enough - just don't ask me to moonlight as an IT technican!"
        $ morgan.sub -= 1
    else:
        morgan.say "Oh no - I have my mobile phone, but other technology just confuses me!"
        $ morgan.love -= 1
        $ morgan.sub += 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        $ morgan.set_flag("male",1,mod="+")
    hide morgan
    return

label morgan_talk_music:
    hero.say "I'm thinking of going to the record store - you interested, Morgan?"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        morgan.say "Urrgh...count me out if it involves prolonged periods of walking and standing!"
        $ morgan.love -= 1
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Sure - you know a place where they have death metal?"
        $ morgan.love += 1
        $ morgan.sub -= 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}+1",2])
        $ morgan.set_flag("male",1,mod="+")
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "Sure would - does the place you're going have vinyl too?"
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "Okay, but I don't think they'll have the experimental singer-songwriters that I've been listening to online recently..."
        $ morgan.love += 1
    else:
        morgan.say "Yay - I can look for some new pop tunes!"
        $ morgan.love += 1
        $ NOTIFICATIONS.append(["Morgan {image=ui/icon_male_vsmall.png}-1",2])
        $ morgan.set_flag("male",1,mod="-")
    hide morgan
    return

label morgan_talk_birthday:
    hero.say "Happy birthday, Morgan!"
    show morgan
    if morgan.get_flag_value("pregnant") >= 9:
        "Morgan bursts into tears at the mere mention of her birthday."
        morgan.say "Oh god, I'm so old!"
        morgan.say "And there mood swings are no fun either!"
    elif morgan.get_flag_value("male") >= 75:
        morgan.say "Geez, calm down - it happens every year, nothing to get worked up about!"
    elif morgan.get_flag_value("male") >= 25:
        morgan.say "Aw, thanks [hero.name] - it means a lot that you remembered."
    elif morgan.sub < 75:
        morgan.say "You remembered?"
        morgan.say "Well, now I feel really special!"
    else:
        morgan.say "Yay, thanks [hero.name] - I'm so excited!"
    hide morgan
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
