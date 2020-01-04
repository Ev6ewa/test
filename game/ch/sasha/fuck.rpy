init -15 python:
    Activity(**{
        "name": "fuck_sasha",
        "display_name": "fuck",
        "label":["ACTIVE_GIRL_fuck_ROOM"],
        "duration": 1,
        "game_conditions": {"hours":(20,25), "activity":"interact", "label":"ACTIVE_GIRL_fuck_ROOM", "flag_female":0},
        "girls_conditions": {
            "sasha":{
                "min_love":150,
                "not_activity":["sleep"],
                "flagmin_sex":2,
                "active":True,
                "flag_cheated":False
                }
            },
        "once_day": "ACTIVE_GIRL",
        "icon": "fuck",
        })

    Activity(**{
        "name": "fuck_sasha_female",
        "display_name": "fuck",
        "label":["ACTIVE_GIRL_fuck_ROOM_female"],
        "duration": 1,
        "game_conditions": {"hours":(20,25), "activity":"interact", "label":"ACTIVE_GIRL_fuck_ROOM_female", "flag_female":1},
        "girls_conditions": {
            "sasha":{
                "min_love":150,
                "not_activity":["sleep"],
                "flagmin_sex":2,
                "active":True,
                "flag_cheated":False
                }
            },
        "once_day": "ACTIVE_GIRL",
        "icon": "fuck",
        })

label sasha_fuck_bathroom_female:
    $ sasha.set_flag("sex",1,"permanent","+")
    if mike.room == game.room and not "mike" in HIDDEN and mike.get_flag_value("sex") >= 3:
        menu:
            "Should Mike join in ?"
            "Yes":
                call shower_ffm_female
                return
            "No":
                $ mike.love -= 2
                hide mike
    show sasha naked
    bree.say "Were you that dirty that you just couldn't wait your turn for the shower?"
    "I chuckle weakly at my lame attempt to relieve the tension between us with humour."
    "But Sasha almost totally ignores my words."
    "I can positively feel the progress of her eyes as they pass over my wet, naked body."
    sasha.say "Oh, I'm dirty alright...I'm feeling positively filthy right now, Bree.!"
    sasha.say "Only it's the kind of filthy that no shower's going to help me with..."
    "I can already feel my cheeks flushing, and not just from the awkwardness of my housemate joining me in the shower."
    "The look on Sasha's face tells me that she's not going to simply have a wash and then leave."
    "Oh no, she wants much more from me than that."
    "And it's this visible desire for me that's already making me feel hot in turn."
    "I'd be lying if I said that I didn't like to have people look at my body like this, guys and girls alike."
    "Having Sasha do the same is so flattering that I can't help but be turned on by her attention."
    "A part of me wants to rise to the challenge, to meet her on a level and show that I'm not afraid to embrace this element of my sexuality."
    "But another is enjoying the feeling of being eyed-up, quaking a little at the prospect of someone so hungry for me pressing their affections further."
    "What can I say - even a thoroughly modern, sexually-liberated woman likes to play the part of an innocent, blushing little maid once in a while..."
    show gog
    "And so I resolve to keep my back pressed against the wall, enjoying the sensation of having Sasha come to me."
    "And come on she does, perhaps sensing that I will do nothing to stop her advances, even being turned on by that realisation than ever."
    "As she closes the space between us, Sasha reaches out with one hand, caressing the inside of my thighs in the most suggestive manner possible."
    "Her other hand clasps the side of my neck, stroking my jaw with her thumb."
    "She holds my eye the entire time that her fingers a coming ever closer to the top of my thighs."
    "But even before I feel them brush the outermost folds of my pussy, I can sense it becoming hopelessly slick in anticipation and excitement."
    "It positively tingles with a static charge by the time the tips of Sasha's fingers finally slide along the length of its lips."
    "I meet this contact with a sharp intake of breath at how intense the feeling is, drawing a quizzical and amused look from Sasha in return."
    "She cocks her head to one side, as if to ask if I like what she's doing to me, and all I can do is close my eyes and nod frantically."
    "Encouraged by this, she goes further, stroking more deeply into my folds and pressing harder as she does so."
    "Now I can't help beginning to sigh and pant at the sensations spreading outwards from my groin and into every extremity of my body."
    "But as I do so, Sasha pulls my mouth towards her own and almost tries to swallow my gasps of pleasure whole."
    "At first she kisses me with a fiery aggression that forces me into utter submission, just as she's massaging me into a state of helpless arousal."
    "This changes though, as I feel the urge to push my tongue into Sasha's mouth, almost as a mirror of the way her fingers are now starting to slip inside of me."
    "We succeed in feeding the fire inside of each other now, her attentions making mine all the more intense and vice versa."
    "My hands wrap around the small of Sasha's back, pulling her so close to me that her hand is almost pressed as hard against her pussy as it is against my own."
    "I can feel out chests being forced together, my larger breasts slipping over her more petite pair."
    "Where our nipples brush past each other for the smallest of instances, I feel a new jolt of arousal that only adds to my pleasure."
    "But now that Sasha's hand is rubbing against her own pussy with almost as much effect as my own, I can feel her beginning to gasp as well."
    "Suddenly, she breaks the kiss and pulls away from me just enough to relieve herself before it's too late to keep from cumming."
    "I can't hide the surprise and disappointment on my face, but Sasha shakes her head and wags a playful finger in my face at this."



    "She's the one that needs to be in charge, and if anyone's going to cum, it has to be who she chooses and when."
    "Not that I mind that in the least, as I'm now resigned to being the passive partner in this encounter."
    "And damn, but she's good at this!"




    "Right now I know full well that Sasha's pleasing me the exact same way that she'd like to be pleasured herself."
    "And it's so good that it's simply exquisite."

    "Then I shudder, groan and feel the cascade of my orgasm coming over me with the inevitability of an incoming tide."
    "Still shaking, I slide down the last few feet of the wall until I end up curled in the bottom of the shower."
    "Sasha lies at my side, panting and exhausted from her own exertions at the same time."
    "Neither of us speaks as much as a word, because there doesn't seem to be any need for them."
    "We simply sit there in silence, while the water washes us clean once more and the evidence is carried away down the swirling drain."
    return

label sasha_fuck_bathroom:
    scene bg bathroom
    show sasha naked blush
    "She's already standing under the cascading water by the time I'm finally naked, and I watch it run in rivulets over her body."
    "Sasha's hair quickly becomes a mane of soaked tendrils that surround her pale features."
    "The water trickles over her milk-white skin, making her breasts and slender legs all the more alluring to the eye."
    "I take a deep breath and step into the shower, feeling the water begin to rain down on me too."
    if game.get_flag_value("homeharem") and bree.room == game.room and not "bree" in HIDDEN:
        show sasha at left
        show bree at right
        bree.say "Can I join in?"
        menu:
            "Yes":
                hero.say "That would be great."
                call shower_ffm
                $ bree.love += 2
                $ sasha.love += 2
                $ sasha.set_flag("lesbian",1,mod="+")
                $ bree.set_flag("lesbian",1,mod="+")
                return
            "No":
                $ bree.love -= 2
                hero.say "Sorry, I wanna be alone with Sasha a little."
                hide bree


    if sasha.get_flag_value("collared") and sasha.sub >= 75:
        "Sasha waits patiently for my instruction, hands clasped behind her back."
        "I take hold of her leash and give it a gentle but firm tug, pulling her downwards."
        "In response, she nods eagerly, and begins to lower herself onto the floor of the shower."
        "My cock instantly begins to stiffen at the sight of Sasha's unquestioning obedience."
        "That means it stands proud and ready to greet her almost as soon as she's in position."
        "And once she is, Sasha doesn't need to be told what's expected of her."
        "Without a moment's pause, she takes my cock into her mouth and begins to lick and suck with unrestrained enthusiasm."
        "Sasha's hands are still clasped behind her back and her eyes are closed as she works on me, as if to close out the rest of the world from her senses."
        "I watch the water soaking her and running over her features, wondering that it does nothing at all to distract her from the task she has been set."
        "Were I just to leave her to it, I have no doubt Sasha would bring me off sooner, rather than later."
        "But a firm tug on her leash lets her know that I have other things in mind."
    elif sasha.sub <= -50:
        "Sasha has a lascivious smile on her face as she catches my eye and points downwards, drawing my attention to the point between her legs."
        "There's no question as to just what she wants, and I hurry to get down on my knees and position myself just so."
        "Placing a hand on each of Sasha's thighs, I begin to lick gently at the outer edges of her pussy."
        "I can feel the familiar folds of her outer lips and the prickle of where she's shaved."
        "But the constant flow of water means that it's hard to smell her scent or taste the unique flavour of her like I'm used to."
        "Only when I begin to venture further in, exploring the inside of her lips, that I begin to feel the comforting tingle of Sasha on my tongue."
        "A moment later, the water dilutes the taste and then washes it away almost completely."
        "Not to be deterred, I respond by pushing my tongue yet deeper into Sasha's pussy, perhaps reaching an inch or two inside."
        "Though almost all of my attention is focussed on what my mouth is doing, I can still hear her moaning in approval at my efforts."
        "A moment later, I feel Sasha lean against the wall of the shower, holding herself up and pushing her groin further towards me."
        "This exposes her clit to me, and I waste no time in making it the centre of my attention."
        "Sasha's legs start to tremble, and I hear her gasping now."
        sasha.say "Yes...yes, [hero.name]..."
        sasha.say "That's it...that's right..."
        sasha.say "Make me...cum!"
        "Perhaps a second or two later, Sasha casts her head back and makes a sound that tell me I've done just that."
    else:
        "Sasha treats me to a mischievous grin as she lowers herself down onto her knees before me."
        "She places a hand on each of my thighs, and begins to use only her lips and tongue to tease me fully erect."
        "Soon enough my cock is standing to attention, having done so whilst in Sasha's mouth."
        "This means that we ease from foreplay and into the actual blow-job almost seamlessly, my pleasure increasing accordingly at the same time."
        "The combination of the warm water washing over me and Sasha's attentions is quite a combination."
        "The former feels like it's bringing my body to life from the outside."
        "While the latter is touching me on the inside in much the same manner."
        "It's then that I realise I don't want to cum just yet, I want to be inside of Sasha before I do!"
        "Gently and with care not to startle her for the safety of my own private part, I pull my cock out of Sasha's willing mouth."
    "Soon enough, we're both back on our feet and panting a little from the combination of the heat and the things that we were doing to each other a moment before."
    "But I can feel that I'm not done yet, and from the look in her eyes, neither is Sasha!"
    show sasha showersex
    if sasha.get_flag_value("collared") and sasha.sub >= 75:
        "Taking Sasha's leash in one hand and roughly grabbing one of her buttocks in the other, I pull her towards me without warning."
        "She doesn't resist for a moment, instead letting herself be dragged forwards without much effort."
        hero.say "Sasha, get on my cock - NOW!"
        sasha.say "Yes, Master, right away."
        "Sasha takes my erect dick in both hands, guiding it into herself with a great deal of care and attention."
        "I hardly have to move a muscle as she inched herself forwards, doing almost all of the work."
        "But the feeling is sensational all the same, and I'm happy to sit back and let Sasha earn her keep."
        "She moans and sighs in a way that makes the whole thing that much more enjoyable, as she rides my cock."
        "All the time Sasha uses her one free hand to massage her breasts and squeeze her own nipples."
        "I can see them bouncing up and down as her breasts move in time with the rest of her body."
        "Water from the shower runs over them and they send droplets splashing away as they go up and down."
        "I could reach out and touch her right now, but I'm enjoying having her service me too much."
        "My ultimate desire is to remain as still and impassive as I can possibly manage, letting Sasha do all of the work."
        "The effort that's taking and the demands it's making on her are clear to see in her flushed cheeks and how she's panting for breath."
        "But she doesn't complain or as much as pause for a single moment."
        "I can't tell whether it's the sensation of Sasha wearing herself out on my cock, or the degree to which I seem to have her trained."
        "But either way I can feel that she's on the brink of bringing me off any moment."
        "Only now do I take a firm hold of Sasha, keeping myself inside of her as I begin to cum."
        "I have no idea if she's cuming herself, even when her sighs and moans fill my ears."
    elif sasha.sub <= -50:
        "Sasha grabs my dick and squeezes it without a seconds pause to think how much it hurts me."
        "Still gripping it tight, she pulls me closer to her."
        sasha.say "My pussy's still hungry, [hero.name]."
        sasha.say "Feed your cock to it - right now!"
        "I rush to obey her, fumbling for her lips even before she's managed to spread her legs wide enough."
        "I don't know if she's amused more by my eagerness or how inept it makes me."
        "But I can hear Sasha laughing even as I finally find my way and thrust myself into her."
        "I know that there's nothing to be gained from objecting to her laughter which comes at my expense."
        "And so the only option open to me is to make her stop by other means."
        "Now that I'm as deep into her as I can go, I begin to pound away on Sasha as hard as I'm able."
        "The tone in which she demanded that I fuck her was strident and firm."
        "So I'm determined to give her what she's asked for in a similar manner."
        "I can tell that she's not prepared for me to be so forceful, as she almost immediately begins to yelp and cry."
        "But she can't object to what I'm doing, as it'd be tantamount to admitting that it's too much for her to bear."
        sasha.say "Ah, [hero.name]...pull out...before you cum inside of me!"
        "Damn it - a direct order!"
        "I do as I've been told, pulling out and letting Sasha go."
        "To my surprise, she immediately grabs my dick a second time and begins to rub it mercilessly."
        sasha.say "Rub my clit...get me off..."
        "I swear that she almost says 'please'."
        "But I would have obliged her willingly, whether she said the word or not."
        "So stroking each other into a state of ecstasy, we keep on until the end finally comes."
        "Sasha almost screams as she leans against me for support, and my cum spatters onto her belly before being washed down the inside of her legs."
    else:
        "Sasha leans her back against the tiled wall of the shower cubicle, at the same time pushing her groin out towards me."
        "I don't need a written invitation to know what she wants of me, and I close the space between us as quickly as I can."
        "With my hand holding onto the underside of Sasha's thighs, I pull her the last few inches towards me."
        "She reaches down to direct traffic, taking my cock in both hands and steering it home."
        "Wet and more than willing for what we both have in mind, the feeling as I slide into Sasha's pussy is as smooth as silk."
        "But that same wetness makes it that much harder to keep a firm grip on her."
        "And I feel my hands clutching handfuls of her firm thighs in an effort not to lose my hold on her."
        "Sasha seems to sense this danger too, wrapping her hands hastily around my waist and pressing herself against me."
        "This adds a terrible sense of desperation to what we're doing, as if we're afraid of slipping and being separated at any moment."
        "I feel as though each and every thrust that we manage to pull off is as much thanks to us clinging to each other as it is to us staying on our feet."
        "This intensity only serves to make the experience all the more powerful for me, and I can already feel my peak approaching."
        hero.say "Sasha...I'm gonna cum!"
        sasha.say "Okay, okay...let me down as slow as you can."
        sasha.say "Just don't drop me!"
        "I do my best to help Sasha's descent, so that she slithers off of my cock and onto her knees in the bottom of the shower."
        "A moment later, I lose it and shoot all that I have straight into Sasha's face."
        "I watch as the cum spatters across her features, and is quickly washed away by the falling water."
    if (randint(1,3) == 1 or "hung" in hero.skills) and not sasha.get_flag_value("pregnant") and not sasha.get_flag_value("pill"):
        $ sasha.set_flag("pregnant",1)
    "It's only thanks to the water from the showerhead that Sasha and I manage to make it out of the bathroom less filthy than when we first came in."
    "All of the sweat and other bodily fluids have been washed down the drain, but the evidence of it all is clear as we walk out exhausted and still short of breath."
    $ sasha.love += 1
    return

label sasha_fuck_livingroom:
label sasha_fuck_kitchen:
label sasha_fuck_pool:
label sasha_fuck_bedroom1:
label sasha_fuck_bedroom2:
label sasha_fuck_bedroom3:
label sasha_fuck_secondfloor:
label sasha_fuck_home:
    show sasha
    hero.say "Hey, wanna come and have fun in my bedroom ?"
    sasha.say "Sure."
    if game.get_flag_value("homeharem") and bree.room == game.room and not "bree" in HIDDEN:
        show sasha at left
        show bree at right
        bree.say "Can I join in?"
        menu:
            "Yes":
                hero.say "That would be great."
                call bree_sasha_threesome_2 from _call_bree_sasha_threesome_1
            "No":
                $ bree.love -= 2
                hero.say "Sorry, I wanna be alone with Sasha a little."
                hide bree
                call sasha_fuck_date from _call_sasha_fuck_date
    else:
        call sasha_fuck_date from _call_sasha_fuck_date_1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
