label alexis_birthday_gift:
    show alexis
    if alexis.get_flag("birthdayknown"):
        hero.say "Happy birthday Alexis."
        alexis.say "How sweet, you remembered my birthday !"
    else:
        alexis.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ alexis.set_flag("birthdayknown")
    return

label alexis_gift_swimsuit:
    show alexis happy
    alexis.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if alexis.love >= 150 or alexis.sub >= 50:
        show alexis blush
        alexis.say "It's so pretty, thank you [hero.name]."
        $ alexis.set_flag("sexyswimsuit")
    else:
        show alexis angry
        alexis.say "Thanks but no thanks [hero.name]."
        alexis.say "You think I would wear that?"
    return

label alexis_gift_collar:
    show alexis
    if game.room == "date_highclassrestaurant":
        hero.say "I've really had a great time tonight, Alexis."
        hero.say "And I feel that we've really come a long way since we were reunited - don't you?"
    else:
        hero.say "I feel that we've really come a long way since we were reunited - don't you?"
    "Again she nods in agreement."
    hero.say "That's why I slipped out of the office this lunchtime and bought this for you."
    "At the mere mention of something being purchased for her, I see a glimmer of the old fire spark into life in Alexis's eyes."
    "She looks up, the confident smile creeping back onto her face as the gold-digger in her is suddenly given an unexpected jolt of life."
    "Her gaze fixes upon the jewellery box that I've pulled out of my jacket pocket and now hold in the palm of my hand."
    "I can almost read the calculations that must be flashing through her cynical little mind right now."
    "The box is perhaps a little too large to contain a ring, which would have been her prime goal in these stakes."
    "But these are modern times, and you can't bank on a proposal any longer."
    "So maybe it's actually a necklace that's worth almost as much instead?"
    alexis.say "Oh, [hero.name]...this is all so sudden!"
    alexis.say "I really don't know what to say!"
    if game.room == "date_highclassrestaurant":
        "By this time the sight of the jewellery box and the undoubtedly beautiful girl filling up with emotion has been noticed by the other diners and staff alike."
        "I can already hear oohs and ahhs, as well as gushing comments about how romantic it all is."
        "Which is exactly what I wanted to have happen at this stage."
        "I stand up to add to the drama of the moment and let more people see what I'm doing."
        "No one seems to find it odd that I'm getting to my feet, rather than going down on one knee."
        "But they're all too swept up in the moment to even notice."
    "I pop open the box and give Alexis a wide and genuine smile."
    hero.say "Alexis...will you do me the inestimable honour of being my bitch?"
    if game.room == "date_highclassrestaurant":
        "For a moment, the imagined magic seems to linger in the air, as no one but Alexis notices what I actually just said."
        "But then, as she looks down at what's sitting in the box, I can hear people beginning to snap out of it and make scandalised comments in hushed whispers."
    "Curled up tightly in the box is a shiny, red collar of leather with a diamond-shaped pendant hanging from it."
    "It's the kind of thing that a person might put around the neck of their dog."
    "Only this one, I know quite well, is a perfect fit for Alexis."
    "And printed on the front is the word 'TAINTED'."
    "Alexis says nothing, but looks up at me, her eyes wide and her lip quivering as if she might begin to cry at any moment."
    hero.say "I'll take your silence as a positive, shall I?"
    if alexis.sub < 75:
        alexis.say "I won't wear that damn thing, and there's nothing that you can do to make me!"
        "She still sounds as though she's on the brink of tears, but now there's a definite shade of anger to her wavering voice."
        alexis.say "I really thought you were different, [hero.name]."
        alexis.say "But I guess I was wrong - you're just a disgusting creep, like all the others!"
        "I don't see the slap coming, and it's a good one too."
        "I see stars as my head snaps to one side, my cheek burning from the blow."
        "By the time I manage to shake myself back into awareness, Alexis is still in the act of storming out of the door."
        "She leaves me alone, with the collar still in my hand, my cheek stinging from her slap and the disapproving sound of the other diner's voices in my ears."
        $ alexis.love -= 20
        $ alexis.sub -= 20
        return
    "When she makes no effort to reach for the collar, I pull it from the box myself and proceed to place it around her neck."
    "Alexis doesn't even try to stop me, the former glimmer of her more confident self collapsing into a sense of defeat and acceptance."
    $ alexis.set_flag("collared")
    $ alexis.set_flag("status", "sex slave")
    hide alexis
    show alexis
    hero.say "There, isn't that better, Alexis?"
    if game.room == "date_highclassrestaurant":
        "I sit back down across the table from her and offer a reassuring smile."
    hero.say "You see, I think what sank our relationship back when we were kids was the fact that I didn't really know who you were."
    hero.say "Sure, I thought you were a cheating bitch at the time."
    hero.say "But since we got back together, I realised that a bitch like that is really just crying out for someone to keep her in line."
    hero.say "So that's what I'm going to do for you, Alexis."
    hero.say "From now on, I'll keep you on a short leash, and teach you how to be good and obedient."
    "Alexis is silent for a while, but then she speaks meekly for the first time."
    alexis.say "Okay, [hero.name]...if that's what you think is best..."
    "I shake my head and wave an admonishing finger in her face at this."
    hero.say "No, no...let's get some ground-rules straight from the start."
    hero.say "It's more appropriate that you call me 'Master' from now on, okay?"
    "Alexis looks up at me and I can see in her eyes that a part of her is still hoping this will all prove to be a joke of some sick and cruel variety."
    "I narrow my own eyes in response, silently urging an answer from her."
    alexis.say "Y...yes...Master..."
    "I smile at her indulgently, as if all is forgiven instantly."
    $ alexis.set_flag("slave")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
