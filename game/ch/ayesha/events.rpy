init python:
    Activity(**{
        "name": "ayesha_teaser_2",
        "display_name":"Go to Ayesha's show",
        "label": ["ayesha_teaser_2"],
        "duration": 0,
        "game_conditions":{"hours":(14,18), "flag_female":0, "days":"7", "done":"ayesha_teaser"},
        "girls_conditions": {"Bree":{"valid":True}},
        "icon":"ayesha",
        "do_once":True
        })        

label ayesha_teaser_2:
    scene bg gym
    "I was nervous about the tickets that Ayesha gave to me to her wrestling show, and torn as to whether I should go along or not."
    "The plus side was, of course, that the tickets were free and the show was happening at the same gym that I work out at."
    "On the other hand, while I watched it as a kid, pro-wrestling's never really been my thing since I grew up and sort of became a responsible adult."
    "And I'm still pretty intimidated by Ayesha in her own right."
    "Add to that the theatrics and over-the-top trappings of wrestling, and it might just be too much for me to handle."
    "But then I remembered that I had two tickets, and thus the ability to bring along a companion to make the whole thing that much easier to bear."
    "My thoughts went immediately to Jack, not least because I knew that he was pretty into wrestling and fit the image I had in my head of a typical grapple fan too."
    "The only problem was that didn't want to look like one by default too."
    "Plus there was the fact I would have to listen to his encyclopedic and exhaustive knowledge of wrestling as well."
    "Those two counts against him were enough to score a pin-fall against him and set me to looking for another potential companion instead."
    "I was afraid that Sasha would just laugh in my face, so that left Bree as the next name on my list."
    "Selling it to her as a kind of performance art and theatre with added acrobatics and simulated combat seemed to do the trick."
    "It's only when we arrive at the gym and find out seats in the front row that Bree finally realises that I've not been strictly honest with her."
    show bree casual
    bree.say "Hey, that looks just like a wrestling ring right there!"
    bree.say "And there's a hell of a lot of fat, sweaty neck-beards in wrestling t-shirts here too!"
    bree.say "[hero.name], be honest - is this really a piece of experimental theatre?"
    "I shrug and try to look like the whole thing is an amusing misunderstanding."
    "But the look on Bree's face tells me I'm having little success."
    hero.say "Okay, okay...it IS a wrestling show."
    hero.say "So technically I did sort of tell you a lie."
    "Bree gives me the stare of death, easily wiping the already weak smile right off of my face."
    hero.say "Sorry, okay - I just needed someone kind of normal to come with me to this thing."
    bree.say "I guess I should be flattered to know that I qualify as at least 'kind of normal'!"
    "I have to rescue this situation, and quickly - I can't let Bree walk out and leave on my own after we've gotten this far."
    hero.say "Look, Bree - cards on the table, okay?"
    "I hold up my hands up in a gesture of surrender."
    "And I'm relieved to see her shake her head at first, but then nod in grudging agreement."
    bree.say "You better make this good, [hero.name]!"
    hero.say "Honestly, Bree - there's this girl at the gym who's wrestling on the show tonight."
    "Bree looks instantly more interested at the mere mention of a woman being involved in tonight's proceedings."
    bree.say "Oh, you mean like on that GLOW show?"
    "Fate seems to have dropped a golden opportunity into my unsuspecting lap."
    "And I don't hesitate to grab it with both hands, then hang on for dear life."
    hero.say "Yes, exactly like that!"
    "Bree smiles and even claps her hands together a little in a show of delight."
    bree.say "I LOVED that show - why didn't you say it was going to be like that from the start?"
    "The truth is that I have literally no idea if there's going to be anything like the damn show happening here tonight."
    "I don't follow wrestling and I didn't see GLOW either."
    "But I'm not going to stop that from giving me an in with Bree to get her interested keeping her buttocks on her folding seat for the duration."
    bree.say "So, you wee telling me about this girl from the gym?"
    "Shit, I'd all but forgotten about explaining Ayesha to Bree, thinking that the connection with her wrestling TV show would be enough to seal it."
    hero.say "Yeah...well, she kind of gave me the tickets to the show."
    hero.say "And I was a bit scared to come along on my own..."
    "I watch as Bree's eyes glaze over at my words, and she clasps her hands together with a sickly grin on her face."
    bree.say "Aww, [hero.name] - that's so sweet!"
    "I look at her with a look of almost sheer disbelief on my face."
    hero.say "What...you really mean that?!?"
    bree.say "Of course I do - she's desperate to have you come along and support her while she performs."
    bree.say "And you're so embarrassed about seeing her again that you needed a friend to come along for moral support!"
    bree.say "Seriously, it's like a plot from a romantic movie or something!"
    "Oops, she thinks that this is some kind of fairytale, with Ayesha as the shy little princess."
    "What's she going to think when she sees her for the first time and realises that she's more likely to grind my bones to make her bread?!?"
    "But I can hopefully deal with that problem when it arises, so there's no point bringing it up here and now."
    "The show starts a couple of moments later, mercifully cutting off the chance for Bree to ask any more questions."
    hide bree
    "What follows is pretty much the kind of thing that I'd been expecting to see."
    "Rock music blares from the PA system, and one after another, a steady stream of gaudily-dressed wrestlers parade to the ring and ply their trade."
    "I soon find myself forgetting any misgivings I had as the over-the-top feel of it all actually starts to hook me and draw me in."
    "Bree and I are soon laughing at the comedy spots, clapping at the aerial feats and even booing and hurling abuse at the villains who taunt the crowd."
    "The only fly in the ointment is that whenever a female wrestler appears, Bree instantly coos over her and demands to know if the newcomer is the mysterious Ayesha."
    "So when the last match of the show is announced, and a brooding thrash-metal track begins to play, I can see a look of confusion on Bree's face."
    "This only becomes more pronounced as Ayesha's name is called over the PA and she strides out onto the stage like a conquering amazon."
    show ayesha teaser work mask
    "She's wearing yellow spandex with black stripes, a tiger's head on her belt and mask on her face completing the outfit."
    "Ayesha plays the part to the full, raising her arms and slashing with her hands to imitate a big cat as she growls at the audience."
    show bree
    "Bree finally manages to tear her eyes away from Ayesha long enough to give me a shocked glance that speaks volumes."
    bree.say "THAT'S HER?!?"
    "The volume of the music saves Bree's shout from being audible to anyone other than me, and I nod in way of answer."
    "I raise my eyebrows and shrug in a manner that I hope lets her know this is the reason that I'm intimidated by Ayesha, and not the cutesy reason she had concocted beforehand."
    "Ayesha's opponent is a far smaller blonde oriental girl, dressed in grungy clothes and strutting around the ring with a cocky arrogance."
    bree.say "It can't be her against that other girl - she'll use the poor thing as a tooth-pick!"
    "I nod, unable to do anything but agree with Bree's assessment of the odds in the match that's about to begin."
    show ayesha fight
    "But as soon as the bell rings, I remember the fact that we've both been conned into forgetting about pro-wrestling."
    "This isn't a straight-up athletic competition, rather it's a choreographed performance that's supposed to pull at the audience's emotions."
    "I'm proven right as Ayesha initially overwhelms her smaller foe and the audience instantly shows its disapproval."
    "But then the smaller girl uses her quickness and smarts to duck and dodge, and the crowd's right there behind her."
    "As I watch Ayesha in the ring, I begin to appreciate the subtlety with which she's delivering her performance."
    "Far from being the monstrous villain that she's playing, I can start to see that she's taking great pains to keep the other girl safe while still making it look convincing."
    "I even feel myself becoming concerned for Ayesha when it's her turn to be the one taking the beating."
    "I never said she wasn't a striking woman to look at, but seeing her show vulnerability really brings home the fact that she's actually quite beautiful too."
    "But a moment later, I'm snapped out of my contemplation by the action spilling out of the wrestling ring and onto the floor."
    "Ayesha charges towards her opponent, only to have her pull down the top rope at the very last minute."
    "She keeps on going, pitching out of the ring and tumbling into the front row."
    "And, as fate would have it, she's falling straight towards me!"
    menu:
        "Protect yourself":
            $ protect = False
            hide ayesha
            "I might be able to pull off being a gentleman and act all chivalrous in better circumstances than this."
            "But the mere sight of Ayesha's substantial frame plummeting towards me means that I'm reacting on instinct alone."
            "All that I can do is grab for Bree in the seat next to me and do my best to drag her into Ayesha's path to save myself."
            "Everything happens so fast that I'm sure she doesn't have the time to figure out what I just did."
            "People are scattering and folding chairs are skittering across the floor, making everything a mass of confusion."
            show ayesha teaser work mask
            "I look up in time to see Ayesha laid almost face-down on the ground perhaps a few feet from where I ended up being thrown."
            "For a moment, I can't see any trace of Bree whatsoever."
            "But then Ayesha pulls herself up onto her elbows, and I can see that the smaller girl is trapped beneath the amazon."
            "Bree looks petrified at first, but then a strange look seems to pass between them, one that I really can't make sense of at all."
            "I watch as Ayesha gets up slowly, pulling Bree to her feet with a gentleness that belies her hulking frame."
            "Bree allows herself to be drawn up, staring wide-eyed at the other woman the whole time."
            "Neither of them speak, but I see Ayesha cup Bree's chin in her hand for a moment before turning and walking away."
            "Bree's cheeks instantly flush a bright red at this, even more so when she sees me watching the silent exchange."
            "What was all of that?"
            "Did they just flirt with each other or something?!?"
        "Protect Bree" if hero.fitness >= 50:
            $ protect = True
            hide ayesha
            "There's no time to even think about moving out of the way, yet everything seems to happen in slow motion."
            "I look up and see Ayesha, silhouetted against the lights above the ring and baring down on me."
            "She reminds me of an angel - not the flouncy pleasant kind, but the pissed-off avenging, wrath of God kind."
            "As she comes closer, I wonder if this is really such a bad way to go."
            "I mean, it has to beat being squashed by a truck or smeared across the tracks by an express train, right?"
            "And then she actually hits me, at which point everything becomes a scrabbling mess of flying people and folding chairs."
            "When the world finally begins to make some kind of sense again, the first thing I realise is that I have something big and heavy atop me."
            "And of course, that would be Ayesha herself, laid with her back to my belly as she struggles to regain her own senses too."
            "She seems to have no idea that she's atop me, and so when she begins to writhe and wriggle, I feel every single movement of her body against mine."
            "Ayesha tries to turn onto her belly a couple of times before she finally succeeds."
            "Her powerful limbs and firm muscles feel like they're giving me in impromptu and undisciplined massage the whole time."
            "And when at last she's on her belly, she's also still on top of me, easily covering and pinning me to the ground."
            "Before she hauls herself back to her feet, she looks down at me with eyes that are only now coming back to full awareness."
            "I can't manage anything but a nervous grin, which makes her face melt into an amused and almost predatory smile."
            "I've never been this close to Ayesha before, and I can't help noticing that her eyes are a deep, enchanting shade of brown."
            "Her smile is all the more intriguing thanks to her exceptional stature and the strength she exudes."
            "Trust me - this close up, it's almost like a pheromone that she exudes from her very pores!"
            show ayesha work confused
            ayesha_say "Aww, don't be scared, man - I'm a real safe worker."
            "I feel her hand on my groin as she starts to get to her feet, squeezing me so that I feel an exquisite pain."
            show ayesha work happy
            ayesha_say "I won't hurt you - unless you really want me to..."
            "And with that, she's up and climbing back into the ring to finish her match."
    hide ayesha
    "Bree and I almost stagger out of the gym once the wrestling show is finally over."
    "Both of us have gotten far more involved in the evening's proceedings than we ever intended to."
    "Which means we're a little bruised and emotionally drained as we stagger home together."
    "Neither of us says anything, but it's safe to assume Ayesha's as much on Bree's mind as she is mine."
    if protect:
        $ game.set_flag("ayeshasnumber")
        "It's then that I reach into my pocket and feel something that I don't recall putting in there myself."
        "I discover a crumpled note, with a hastily-written name and a mobile number on it."
        "Of course, the name is 'Ayesha', and I can guess that the number is hers as well."
        "She must have shoved it into my pocket during the confusion when she feel out of the ring."
        "I stare at the note for a moment, and then cram it back into my pocket before Bree can see it too."
    "I don't know if tonight has made me more or less afraid of Ayesha, and I don't know which would be the better of the two options either."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
