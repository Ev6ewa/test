label shiori_birthday_gift:
    show shiori
    if shiori.get_flag("birthdayknown"):
        hero.say "Happy birthday Shiori."
        shiori.say "How sweet, you remembered my birthday !"
    else:
        shiori.say "How do you know my birthday ?"
        hero.say "I didn't, it's just pure luck."
        $ shiori.set_flag("birthdayknown")
    return

label shiori_gift_collar:
    show shiori
    shiori.say "A gift, for me?!?"
    "I nod indulgently at her genuine enthusiasm, producing a small box from where I've had it concealed this whole time."
    hero.say "It's nothing much, I admit."
    hero.say "Really it's a token of my affection."
    hero.say "And let's just say it's also something to let people know that you're mine..."
    "Shiori's smile endures as she opens the wrapping and reaches inside the box."
    "But when she pulls out what's inside, it isn't replaced by a frown."
    "Rather a confused expression as she cocks her head on one side and holds it up to me."
    "Her mouth hangs open, as if silently asking for an explanation."
    "In Shiori's hand is a leather collar, patterned black and white like the coat of a Friesian cow."
    "The collar bears no tag or other means of identification save for a tin cattle bell, which dangles from the middle."
    "I meet Shiori's uncomprehending gaze with an indulgent smile, pointing at the collar in her hands."
    hero.say "When I saw that, Shiori, I just couldn't help instantly thinking of you."
    shiori.say "R...really?"
    shiori.say "This is like...like the kind of bell you'd put on a...a cow!"
    "I nod again, gesturing to her as I explain my thinking."
    hero.say "Sure, Shiori, it's exactly that."
    hero.say "And it suits you down to the ground, don't you think?"
    "Shiori blinks and stutters in response, as though she can't quite process what I'm saying."
    hero.say "Face it, Shiori - a cow is pretty much what people think of when they look at you."
    hero.say "You're sweet and docile, with your udders swaying as you chew the cud."
    hero.say "Sure, you can call them breasts and say that you work in an office for a living, but in the end it's pretty much the same thing."
    "Her cheeks redden noticeably, and she puts her hands over her breasts in an unconscious motion."
    hero.say "We both know you're no modern, independent career woman, Shiori."
    hero.say "What you really want in life is for someone to come along and make all of the decisions just disappear."
    hero.say "Someone to put a collar on you and lead you off like the cow you've always wanted to be."
    "At this, she looks up at me almost desperately."
    hero.say "Put that collar on, and that's just what'll happen."
    hero.say "You'll be my little pet cow..."
    if shiori.sub <= 75:
        "Shiori nods her head slowly, holding my eye the entire time."
        "Her nervous smile puts me in mind of the way someone might look at a lunatic as they indulge them in the hope of escaping at the right moment."
        shiori.say "Thank you, [hero.name] - it's a very nice gift, very thoughtful..."
        shiori.say "If you don't mind though...I think I'll wait until I get home to try it on?"
        "I try to put a brave face on things, shrugging and acting as though it's no big deal."
        hero.say "Erm, yeah...whatever you think's best, Shiori!"
        "My smile must be turning into a rictus by now, and I'm wishing that the ground would open and swallow me up."
        "Shiori's trying her best to be polite with me now."
        "But I can already feel her looking for the first opportunity to make her excuses and leave."
    else:
        "Shiori, looks into my eyes for a long, lingering moment."
        "I can tell without the need for words that she's weighing up all that I've said, trying to come to a decision."
        "And then she raises the collar and proceeds to strap it in place around her neck."
        hide shiori
        $ shiori.set_flag("collared")
        $ shiori.set_flag("status", "sex slave")
        show shiori
        "The blush that was on her cheeks before has become a riot of red by the time she looks up at me with the collar around her neck."
        "Shiori's hands linger around the bell for a couple of seconds, and then she clasps together tightly in her lap."
        "As strange as it might sound, somehow the collar and bell look just so natural on her."
        "In fact, they almost look like the missing element of her being that's been absent up to this point."
        "Reading the approval in my eyes, Shiori giggles suddenly and shakes her chest so that the bell clangs gently."
        shiori.say "I don't know if I should say 'moo'...or would that be just too silly?"
        hero.say "I think a moo from you would be a pretty sexy sound!"
        hero.say "Especially from such a hot little cow!"
        "At this, Shiori giggles again, putting a hand over her mouth."
        "She looks away for a moment, as if gathering her courage."
        shiori.say "M...M...Moo!"
        "I nod approvingly, and she gives me a coy, sideways glance."
        shiori.say "Mooooo!"
        hero.say "That's right, Shiori - you're my little pet now, so there's no need to worry any more."
        hero.say "You can even call me 'Master', from now on."
        "Something seems to spark in Shiori's eyes at the mention of the word."
        shiori.say "Oh, yes...M...Master!"
        $ shiori.sub += 10
    "Once Shiori's gone, taking the collar with her, I can finally breath a sigh of relief."
    "Just being able to present her with it feels like a load off of my mind."
    "And I really think that this is going to be the point at which I look back and remember when things changed for us in a very real way."
    return

label shiori_gift_swimsuit:
    show shiori happy
    shiori.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if shiori.love >= 150 or shiori.sub >= 50:
        show shiori blush
        shiori.say "Thank you [hero.name]."
        $ shiori.set_flag("sexyswimsuit")
    else:
        show shiori sad
        shiori.say "I am sorry, I am not ready to wear that [hero.name]..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
