init python:
    Event(**{
        "name": "master_event_01",
        "label": ["master_event_01"],
        "priority": 500,
        "duration": 1,
        "game_conditions":{"flag_female":1, "room":["beach"], "hours":(10,16), "flagmax_morality":0, "flag_MasterBreeStory":0, "done":"bree_meet_the_master"},
        "do_once":False,
        "once_week":True,
        "quit": True
        })

    Activity(**{
        "name":"blowjob_for_money",
        "label": ["blowjob_for_money"],
        "duration": 1,
        "game_conditions": {"min_energy":3,"min_hunger":3,"min_grooming":3,"min_fun":3,"room":["beach"], "flagmax_morality":-25, "flagmin_masterBreeStory":1,"flag_female":1,"hours":(10,16)},
        "display_name": "Help the old man",
        "icon": "master"
        })

label blowjob_for_money:
    scene bg beach
    show master normal glasses
    hero.say "Hey, old man!"
    master_say "Oh Hi!"
    hero.say "Want me to help you out?"
    menu:
        "Offer a handjob" if game.get_flag_value("morality") <= -25:
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            "I tell myself that this isn't so bad - I only have to touch one part of him, and he doesn't get to touch me at all."
            "Again, the old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            "His muscular body once again surprise me on such an old man."
            "I get down on my knees in front of him, my eyes on his cock and not his face."
            "Even just the promise of what I'm about to do and my kneeling in front of him is enough to set his cock to stirring."
            hide master
            show beach bj
            "I oblige by cupping his balls in one hand and taking his shaft in the other, rubbing it up and down roughly."
            "Normally I'd be careful to build up to being this forceful with a guy's cock."
            "But I figure that he doesn't really deserve to be pampered, based on what he's paying for and his unpleasant pass-time here at the beach."
            "All the same, my harsh treatment of his cock seems to be having the desired effect."
            "He's as big as he's going to get without surgery, and the head is already throbbing and red."
            "I try not to look up at his face, which is mostly obscured by his beard anyway, instead listening to him gasp for breath."
            "My hand starts to move up and down his shaft faster still now, and I begin to squeeze at his balls too."
            "I don't know if it's because I'm simply that good at this kind of thing or the fact that he's so old."
            "But he's already starting to twitch and twinge, gasping as I push him ever closer to cumming with each second that passes."
            "I make the mistake of thinking that I still have enough time to get out of the way before I bring him off."
            show beach bj cum
            "And I'm proven spectacularly wrong a couple of seconds later when he shoots his load straight into my unsuspecting face."
            "I have to give it to him, it splatters all over my face like I'd have expected of a man half his age."
            "As I wipe the cum out of my eyes, squinting the whole time, he offers me a helpless grin and hands over a surprisingly pristine handkerchief to speed up the process."
            "He offers to let me keep the handkerchief, and I smile condescendingly, tossing it aside as soon as I'm all cleaned up and a safe distance away."
            "I'm much more satisfied with being able to keep the wad of money he hands over at the same time anyway."
            $ hero.money += 25
            if game.get_flag_value("morality") > -50:
                $ game.set_flag("morality",1,mod="-")
        "Offer a blowjob" if game.get_flag_value("morality") <= -50:
            $ game.set_flag("MasterStory",1)
            hero.say "Tell you what, I'm feeling particularly generous today."
            hero.say "I'll let you blow your load in my mouth."
            hero.say "How does that sound, hmm?"
            "His eyes light up at this, or at least from what his bushy eyebrows are doing above his sunglasses, I assume they do."
            "Without as much as a single word, he shoves the entire wad of notes into my hand, nodding vigorously the entire time."
            "Don't judge me, okay?"
            "He might be an old perv, but he looks like he keeps himself clean and he's not even tried to put a hand on me before this."
            "And who knows - if he got more attention of this kind, then maybe he'd be less inclined to hang about the beach, letching on sunbathing girls?"
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            "Again the old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            hide master
            show beach bj blowjob
            "I kneel down in front of him and give his already twitching cock a few playful strokes."
            "I lick my lips at the same time, letting him get the impression that I'm looking forward to getting my lips around it."
            "Call it insincere if you like, but I just want him to feel like he's getting value for his money."
            "I tickle his balls with one hand while guiding the tip of his cock into my mouth with the other."
            "Not taking it straight in, I kiss and lick at the head for a short while, building his anticipation for what's to come next."
            "And then, when he's already panting and biting his lip, I take him in further and begin to suck away with some gusto."
            "I don't intend to make this either particularly long or complicated, just give him a thrill and make him cum in short order."
            "After all, he's paying for a blow-job, not a six-year relationship."
            "And I don't know if his old man's body could take much more without him having a stroke or something similar."
            "I'm going at him pretty hard now, taking him almost as far in as I can manage and giving his balls a good, hard squeezing."
            "He's gasping with what I assume to be orgasmic pleasure, and not the first flushes of a heart attack, and so I redouble my efforts."
            "Jerking and staying up only because he has the wall for support, he loses himself a couple of seconds later."
            show beach bj blowjob cum
            "True to my word, I keep him in my mouth the whole time, not letting one drop of cum leak out of my mouth."
            "I'm swallowing even as his cock slithers out of my mouth and he slowly slides down the wall to end up sitting in an exhausted heap before me."
            "As he looks to be in no condition to say a word, and as I already have his money, I get to my feet and give him a little wave goodbye."
            "Walking back to my towel and the bottle of water I brought with me, I really don't spare a thought for his fate should anyone discover him in such a state."
            "I took care of my part of the bargain, and now all I have to worry about is soaking up the sun for what's left of the day."
            $ hero.money += 50
            if game.get_flag_value("morality") > -75:
                $ game.set_flag("morality",1,mod="-")
    return

label master_event_01:
    scene bg beach
    "From the weather being fine and there being just enough free time in my schedule for the day, everything fell into line to give me a golden opportunity to slip away to the beach for some much needed me time."
    "And never being the kind of girl to look a gift horse in the mouth, that meant I was feeling the warm sand under my feet as soon as I could make it out of the house and down to the dunes."
    "The fact that it's not the weekend means that the beach is far quieter than I'm used to seeing it, with only a small number of people soaking up the sun or taking a swim in the sea."
    "This means that I can take my pick when it comes to choosing the spot where I dump my stuff and prepare to lie down, taking time to truly appreciate the nicer specimens of the human anatomy on show as I do so."
    "I feel flattered to note that this admiration isn't just a one-sided thing, as several of those that I check out are quick to return the gesture, and with similar sentiments."
    "Though I'm only here to do some relaxing, I make a mental note that the bikini I chose to wear today is one that's worth keeping at the top of the list when I want to make an impression."
    "Pretty soon I'm laid on my towel, sunglasses protecting me against the glaze of the intense rays and allowing the sound of the lapping waves to lull me almost to sleep."
    "At first I try to ignore the funny feeling that keeps nagging at the back of my mind, the strange sensation of being watched."
    "The last thing that I want right now is to be distracted, and so I assume that it's just the admiring eyes that I attracted earlier, still lingering after seeing something they like."
    "But no matter how hard I try, thinking about other things and even trying some mediation exercises that I can remember learning, I can't seem to shake the feeling."
    "It's bugging me like hell, and there's just no way that I'm going to be able to relax properly until I so something about it."
    "Sitting up, I take in all of the beach that I can see form where I'm lying, at first not seeing a single thing that could explain the wierd sensation."
    "Turning my head through three hundred and sixty degrees, all I find are perfectly innocent people doing perfectly inoffensive stuff."
    "But then, as I take a second look at the row of beach-huts that back onto the dunes, something moves enough to catch my eye."
    "Lifting my sunglasses and putting them on top of my head, I scrutinise the spot closely for almost a minute before I see anything at all."
    "What I do see is the sun glinting off of something smooth and shiny, something that seems to be bobbing around behind the beach-huts."
    show master normal glasses
    "A moment later I catch a glimpse of a face below it as well, and I instantly know that I'm actually looking at a bald head."
    "And from where I'm seeing it in relation to the beach and my own recollection of the last time I was here, I think that I can guess exactly who it belongs to as well!"
    "I could just let it go and try to ignore the fact that I know there's a dirty old pervert lurking around back there."
    "But something inside of me seems to just snap, making me suddenly and majorly annoyed that he's ruining my much needed chill-out time with his lecherous antics."
    "Getting up from my towel, I march straight over to where the beach-huts stand and then around the back of them."
    "There's no way he can't have seen me coming, and I see that he has on account of the fact that he's already managed to scuttle perhaps twenty feet into the tall grass when I get there."
    "He can't possibly think that he's fooling me, as it's plain to see the grass shaking and parting as he goes."
    "Planting my hands firmly on my hips, I decide to call the filthy old geezer's bluff."
    hero.say "Hey, you!"
    "Almost immediately I see his progress through the grass come to an abrupt halt."
    hero.say "Yeah, I know it's you."
    hero.say "Get back here, right now - before I scream so loud they'll hear it in the next county!"
    "There's a momentary pause, probably as he mulls over his chances of escape and measures them against the sincerity he can hear in my voice."
    "And then the rustling in the grass begins again, only coming towards me this time and noticeably slower than before."
    "Soon enough the grass at the start of the dunes parts, and the shameless old peeping-Tom emerges into the open."
    "For all of his boldness when actually snooping, he's now looking down at the ground, even kicking at the sand with his feet."
    "He looks like nothing more than a kid that's been caught in the act of misbehaving and how has to face the music."
    hero.say "Well - what have you got to say for yourself this time, hey?"
    "In way of response he mutters something in a tone that's almost too low for me to make out."
    hero.say "What was that - speak up!"
    master_say "I said I was only looking..."
    hero.say "Yeah, I bet you were."
    hero.say "It's a miracle that I didn't catch you with it out and in your goddamn hand!"
    "He keeps on shuffling his feet and avoiding my eye, and it occurs to me that now I've caught him bang to rights, I have no idea what to do next."
    "I cross my arms over my chest and shake my head as he finally musters up the courage to look me in the face for the first time."
    master_say "You know I only do this because I'm frustrated, full of pent up energy?"
    master_say "I'd pay you..."
    hero.say "You'd what?"
    master_say "Pay you...if you were to help me out..."
    "I raise an eyebrow and regard him with a knowing smirk."
    hero.say "And how would you want me to do that - let me guess!"
    hero.say "No, before you even think of asking - I'm not going to fuck you for money!"
    master_say "Well...maybe there's something else you could bring yourself to do...for money?"
    menu:
        "Get the fuck lost!" if game.get_flag_value("morality") >= -75:
            hero.say "Eww, gross - get the hell away from me, you creepy old bastard!"
            hero.say "I don't want your filthy money - it makes my skin crawl just to look at you!"
            "My reaction is so extreme and intense that the old geezer actually leaps away from me a good metre or so."
            hero.say "I thought I made it plain to you the last time I had to tell you off?"
            hero.say "Stop spying on girls around here, or I'll call the cops on you!"
            "He capers in a circle at this, waving his arms as if trying to either get me to calm down or else starting to have some kind of twitching fit."
            master_say "Okay, okay - I get it!"
            master_say "No cops, no cops...I'll stop watching you, I promise?!?"
            "It's only when he's crawled off back into the long grass that I realise he only ever vowed to stop spying on me, rather than all of the other girls on the beach at any given time."
            "As I start to make my way back to where I left my blanket, I can't help shaking my head in grudging admiration of the old geezer's slyness."
        "Offer a handjob" if game.get_flag_value("morality") <= -25:
            $ game.set_flag("MasterBreeStory",1)
            hero.say "Well, I dunno - just how much are we talking about here?"
            "Sensing that I might not be opposed to what he's suggesting, the old codger suddenly perks up."
            "He reaches into the pocket of his shorts and pulls out a wad of notes, nodding and grinning as he does so."
            "I try to guess how much is wrapped up in there, thinking the whole time that I could really use the money."
            hero.say "That'll buy you a hand-job, old man - no mouth and no touching me, okay?"
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            "I tell myself that this isn't so bad - I only have to touch one part of him, and he doesn't get to touch me at all."
            "The old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            "But it does reveal that his body is in pretty good shape for an old-timer."
            "Maybe he wasn't so full of shit as I thought when he claimed he was some kind of martial artist?"
            "Plus, his cock is quite a relief when I finally see it - not a monster, but pretty decent for the junk of an old man."
            "Maybe if I can forget about the rest of him and just concentrate on that, this won't be that bad after all..."
            "I show willing by getting down on my knees in front of him, my eyes on his cock and not his face."
            "He's not getting the full treatment of flirting and teasing, no matter what he's prepared to pay me."
            "And anyway, I know that the old goat is getting a premium view of my cleavage from up there, so he can make do with that."
            "Even just the promise of what I'm about to do and my kneeling in front of him is enough to set his cock to stirring."
            hide master
            show beach bj
            "I oblige by cupping his balls in one hand and taking his shaft in the other, rubbing it up and down roughly."
            "Normally I'd be careful to build up to being this forceful with a guy's cock."
            "But I figure that he doesn't really deserve to be pampered, based on what he's paying for and his unpleasant pass-time here at the beach."
            "All the same, my harsh treatment of his cock seems to be having the desired effect."
            "He's as big as he's going to get without surgery, and the head is already throbbing and red."
            "I try not to look up at his face, which is mostly obscured by his beard anyway, instead listening to him gasp for breath."
            "My hand starts to move up and down his shaft faster still now, and I begin to squeeze at his balls too."
            "I don't know if it's because I'm simply that good at this kind of thing or the fact that he's so old."
            "But he's already starting to twitch and twinge, gasping as I push him ever closer to cumming with each second that passes."
            "I make the mistake of thinking that I still have enough time to get out of the way before I bring him off."
            show beach bj cum
            "And I'm proven spectacularly wrong a couple of seconds later when he shoots his load straight into my unsuspecting face."
            "I have to give it to him, it splatters all over my face like I'd have expected of a man half his age."
            "As I wipe the cum out of my eyes, squinting the whole time, he offers me a helpless grin and hands over a surprisingly pristine handkerchief to speed up the process."
            "He offers to let me keep the handkerchief, and I smile condescendingly, tossing it aside as soon as I'm all cleaned up and a safe distance away."
            "I'm much more satisfied with being able to keep the wad of money he hands over at the same time anyway."
            $ hero.money += 50
            if game.get_flag_value("morality") > -50:
                $ game.set_flag("morality",1,mod="-")
        "Offer a blowjob" if game.get_flag_value("morality") <= -50:
            $ game.set_flag("MasterBreeStory",1)
            hero.say "Well, I dunno - just how much are we talking about here?"
            "Sensing that I might not be opposed to what he's suggesting, the old codger suddenly perks up."
            "He reaches into the pocket of his shorts and pulls out a wad of notes, nodding and grinning as he does so."
            "I try to guess how much is wrapped up in there, thinking the whole time that I could really use the money."
            hero.say "Tell you what, I'm feeling particularly generous today."
            hero.say "Hand over the whole wad, and I'll let you blow yours in my mouth."
            hero.say "How does that sound, hmm?"
            "His eyes light up at this, or at least from what his bushy eyebrows are doing above his sunglasses, I assume they do."
            "Without as much as a single word, he shoves the entire wad of notes into my hand, nodding vigorously the entire time."
            "Don't judge me, okay?"
            "He might be an old perv, but he looks like he keeps himself clean and he's not even tried to put a hand on me before this."
            "And who knows - if he got more attention of this kind, then maybe he'd be less inclined to hang about the beach, letching on sunbathing girls?"
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            "I tell myself that this isn't so bad - I only have to touch one part of him, and he doesn't get to touch me at all."
            "The old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            "But it does reveal that his body is in pretty good shape for an old-timer."
            "Maybe he wasn't so full of shit as I thought when he claimed he was some kind of martial artist?"
            "Plus, his cock is quite a relief when I finally see it - not a monster, but pretty decent for the junk of an old man."
            "There's a story worth telling - the one about the time I blew a martial arts master off on the beach!"
            "Of course when I do tell it, he'll look more like Bruce Lee, and maybe the money will be his winnings from a lethal tournament of death..."
            hide master
            show beach bj blowjob
            "Starting to feel more at ease with the whole idea, I kneel down in front of him and give his already twitching cock a few playful strokes."
            "I lick my lips at the same time, letting him get the impression that I'm looking forward to getting my lips around it."
            "Call it insincere if you like, but I just want him to feel like he's getting value for his money."
            "I tickle his balls with one hand while guiding the tip of his cock into my mouth with the other."
            "Not taking it straight in, I kiss and lick at the head for a short while, building his anticipation for what's to come next."
            "And then, when he's already panting and biting his lip, I take him in further and begin to suck away with some gusto."
            "I don't intend to make this either particularly long or complicated, just give him a thrill and make him cum in short order."
            "After all, he's paying for a blow-job, not a six-year relationship."
            "And I don't know if his old man's body could take much more without him having a stroke or something similar."
            "I'm going at him pretty hard now, taking him almost as far in as I can manage and giving his balls a good, hard squeezing."
            "He's gasping with what I assume to be orgasmic pleasure, and not the first flushes of a heart attack, and so I redouble my efforts."
            "Jerking and staying up only because he has the wall for support, he loses himself a couple of seconds later."
            show beach bj blowjob cum
            "True to my word, I keep him in my mouth the whole time, not letting one drop of cum leak out of my mouth."
            "I'm swallowing even as his cock slithers out of my mouth and he slowly slides down the wall to end up sitting in an exhausted heap before me."
            "As he looks to be in no condition to say a word, and as I already have his money, I get to my feet and give him a little wave goodbye."
            "Walking back to my towel and the bottle of water I brought with me, I really don't spare a thought for his fate should anyone discover him in such a state."
            "I took care of my part of the bargain, and now all I have to worry about is soaking up the sun for what's left of the day."
            $ hero.money += 100
            if game.get_flag_value("morality") > -75:
                $ game.set_flag("morality",1,mod="-")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
