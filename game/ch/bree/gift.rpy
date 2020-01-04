label bree_birthday_gift:
    show bree
    if bree.get_flag_value("birthdayknown"):
        hero.say "Happy birthday Bree."
        bree.say "How sweet, you remembered my birthday !"
    else:
        bree.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ bree.set_flag("birthdayknown")
    return

label bree_christmas_gift:
    show bree
    hero.say "Merry Christmas Bree."
    bree.say "Thanks !"
    $ bree.love += 2
    return

label bree_valentine_gift:
    show bree
    hero.say "Happy valentine's day Bree."
    bree.say "Thank you."
    $ bree.love += 2
    return

label bree_gift_swimsuit:
    show bree happy
    bree.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if bree.love >= 150 or bree.sub >= 50:
        show bree blush
        bree.say "It's so pretty, thank you so much [hero.name]."
        $ bree.set_flag("sexyswimsuit")
    else:
        show bree annoyed
        bree.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        bree.say "Even worse than being naked..."
    return

label bree_gift_collar:
    show bree
    bree.say "Oh... I.. Is it for me?"
    "Bree sits up, reaching for the wrapped gift."
    "I lean down and give her the box"
    $ bree.love += 2
    "After a few moments of looking at the box she starts unpacking it and get the collar out."
    "I wish I could see her expression, but with her head lowered, I can't see her face."
    if bree.sub < 50:
        show bree angry
        bree.say "What the fuck!"
        "Bree throw the collar away and leave"
        $ bree.love -= 10
        $ bree.set_flag("gone")
        $ bree.set_flag("goneDelay",1)
        $ HIDDEN.append("bree")
    else:
        bree.say "Oh... it's beautiful. Do you have the key?"
        "I nod, dipping my fingers into my pocket to flash the key at her briefly before putting it away, already feeling a little thrill at how she's reacting to her gift."
        "And, of course, anticipation of putting it on her."
        bree.say "Can I wear it now?"
        "I go over and take the collar, then step behind the couch to loop it carefully around her neck and buckle it."
        "She lets out a little sigh as she hears the lock click."
        $ bree.love += 2
        $ bree.sub += 5
        $ bree.set_flag("collared")
        $ bree.set_flag("status", "sex slave")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
