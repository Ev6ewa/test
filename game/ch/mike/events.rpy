init python:

    Event(**{
        "name": "mike_give_christmas",
        "label": ["mike_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":1},
        "girls_conditions": {"mike":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "mike_give_birthday",
        "label": ["mike_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":1},
        "girls_conditions": {"mike":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "mike_give_valentine",
        "label": ["mike_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":1},
        "girls_conditions": {"mike":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name":"bree_mike_shower_bj",
        "label": ["bree_mike_shower_bj"],
        "duration": 1,
        "game_conditions": {
            "activity":["shower"],
            "flag_female":1,
            },
        "girls_conditions": {"mike":{"min_love":100,"present":True, "valid":True}},
        "once_week": True,
        "once_day": False,
        "do_once": False,
        "quit": True
        })

label bree_mike_shower_bj:
    "It's been a long day, and all that I can think about doing right now is stepping into a steaming hot shower to wash the worst of it away and then collapse into bed."
    "I start the water running and leave it to get to that elusive point where it's just right before I get inside, brushing my teeth and taking care of other small tasks while I wait."
    "As soon as I'm done, I shove a hand inside and find that the temperature's not quite perfect, but good enough for me to jump in regardless."
    "It only takes a couple of minutes standing under the cascade of water for me to begin feeling the effects in the best way possible."
    "Muscles that have been tense all day are now loosening and knots in my body that I had no idea were even there fall away as the warmth seeps into my limbs."
    "I take my time over actually getting cleaned up, doing all that I can to make it an extension of relaxing."
    "And yet I'm still done well before I'm ready to get out of here."
    "Guilt tells me that I'm just wasting water staying in here any longer, not to mention hogging the bathroom."
    "Worse still, my brains just too tired to come up with a good enough excuse to ignore all of that as well!"
    "But then, as if in answer to my prayers, I hear the sound of the bathroom door opening."
    mike.say "Erm...hello?"
    mike.say "Sasha...Bree?"
    mike.say "Who's in here?"
    "I open the shower door just enough to stick my head out."
    "And I can see Mike doing pretty much the same thing on the other side of the bathroom."
    hero.say "It's me, Mike - just in the shower."
    "He looks more than a little embarrassed at having disturbed me, immediately beginning to apologise."
    mike.say "Oops, sorry!"
    mike.say "I just needed to use the facilities - but I'll go downstairs instead."
    menu:
        "Bree lets Mike go downstairs":
            hero.say "Don't let me keep you from answering the call of nature!"
            "Mike nods a little awkwardly and ducks back out of the bathroom, leaving me to wrap up my shower in peace."
            "A few minutes later, I hop out and wrap myself in a towel before heading to my own room and bed."
        "Bree tells Mike to go ahead and use the toilet in the bathroom" if game.get_flag_value("morality") < 25:
            $ mike.love += 1
            hero.say "It's okay, you can just go ahead and use the one in here - so long as it's not a sit-down affair."
            mike.say "Are...are you sure?"
            hero.say "Don't be a prude, Mike!"
            hero.say "Besides, the glass is all steamed-up anyway."
            hero.say "And the sound of the water means I won't hear a thing."
            mike.say "Umm...okay - if you say so!"
            "Mike hurries into the bathroom as I close the shower door."
            "He doesn't need to know that I can see him perfectly well, as it'd only make him feel self-conscious."
            "Truth be told, I like playing the part of the laid-back female housemate."
            "The one that's almost like another guy, but still gets him hot under the collar."
            "I know it's a cheap thrill, watching him as he has his cock in his hand."
            "But what Mike doesn't know won't hurt him."
            "Once he's done, Mike nods a little awkwardly and ducks back out of the bathroom, leaving me to wrap up my shower in peace."
            "A few minutes later, I hop out and wrap myself in a towel before heading to my own room and bed."
            "I fall asleep with the mental image of his dick still on my mind."
        "Bree invites Mike into the shower for a blow-job" if game.get_flag_value("morality") < -25 or (mike.get_flag_value("sex") and game.get_flag_value("morality") < 50):
            hero.say "Why would you want to do that?"
            hero.say "Go up here and then hang around afterwards."
            hero.say "If you do, I promise that I'll do something for you with it that's much more fun!"
            $ mike.love += 1
            "I really don't know where the urge to suddenly get so flirty and frisky with Mike comes from."
            "Just a couple of minutes before I was ready to get out of the shower and jump straight into bed."
            "Maybe it's the relief of being loosened up by the shower, or the fact that he's coming in here with his dick on his mind."
            "I know this makes me sound like some kind of cock-crazed hussy - but all I have on my mind right now is the exact same thing!"
            "I guess that with the stress of the day finally washed away, I've got the head-space to start thinking about more enjoyable stuff."
            mike.say "Do...do you mean what I think you mean?"
            hero.say "Tell you what - you take care of business and then join me in here."
            hero.say "Then we can see if I am or not!"
            "I can't suppress the laughter that slips out as I close the door on Mike, seeing how he hurries to attend to the call of nature."
            "The sound of him hastily stripping his clothes off follows soon afterwards."
            "And it can't be more than a few seconds later that he opens the shower door and steps nervously inside."
            "It's sweet that he's so eager and yet still showing trepidation, so I start out being gentle with him."
            "At first all he gets is a chaste kiss on the lips, followed by another on the side of his jaw."
            "Next come his neck, and then his chest, as I make my way downwards."
            "By the time I'm crossing his stomach and going below his waist, I'm also sinking down onto my knees."
            "My hands follow, tracing parallel lines down the side of his body until they come to rest on his thighs."
            "Needless to say, Mike's already perked up a great deal since he joined me in the shower."
            "This means that he needs only a little bit more encouragement from me to get him standing to attention."
            "I give this to him by wrapping my lips around the very tip of his cock, just enough to be able to lick at it with my tongue."
            "Keeping my head still, I coax him fully erect and at the same time manage to make the rising of his cock push the head further into my mouth."
            "This means that by the time he's as big as he's going to get, he's already in there and feeling the sensation of my tongue around him."
            "Only now that he's inside of my mouth do I actually touch his cock with my hands, encircling it with a finger and thumb and then rubbing gently up and down."
            "Mike's leaning back against the tiled wall by now, his head leant back so that the water from the shower is streaming down over his face."
            "I can hear him moaning at the feeling of what I'm doing to him, overcome by the moment."
            "And he's not the only one enjoying himself either."
            "The feeling of his cock in my mouth is better than I could have imagined it to be."
            "Warm and slippery, washed totally clean by the water of the shower."
            "It's so good to caress that I just don't want to let it go."
            "But I'm going to have to soon, as I can tell from Mike's suddenly changing his posture that he's on the brink of cuming."
            menu:
                "Aim it at the floor" if game.get_flag_value("morality") >= 0:
                    if game.get_flag_value("morality") >= 25:
                        $ game.set_flag("morality",1,mod="-")
                    "This may be all fun and games for Mike, but there's a limit to what I'm going to let him do to me."
                    "The thought of letting him shoot his entire load into my mouth is just too disgusting to think about."
                    "And so as he finally cums, I make sure his cock is nowhere near my mouth and pointed safely down at the floor of the shower cubicle."
                    "All the same, I keep on smiling up at him in a demure and pleasant manner."
                    "After all, I don't want him to know how much I loathe the idea of swallowing his cum, now do I?"
                "Spit it out" if game.get_flag_value("morality") >= -25 and  game.get_flag_value("morality") <= 25:
                    if game.get_flag_value("morality") >= 0:
                        $ game.set_flag("morality",1,mod="-")
                    "Opening my mouth as wide as I can manage, I let Mike release himself straight onto my tongue without even flinching."
                    "I manage to catch almost all of it and then close my mouth again, smiling up at him to make it plain I enjoyed the experience."
                    "The cum washes around in my mouth for a few moments, and then I choose a convenient opportunity to discreetly spit it out again."
                    "Mike doesn't see me doing this, and even if he did, he can't begrudge me anything after what I just let him use my mouth for!"
                "Swallow" if game.get_flag_value("morality") >= -50 and  game.get_flag_value("morality") <= 0:
                    if game.get_flag_value("morality") >= -25:
                        $ game.set_flag("morality",1,mod="-")
                    "I kneel before Mike, my mouth wide open and my tongue sticking out, hoping that I don't look too much like an eager dog as I do so."
                    "The moment that he cums, I can't help rising up on my haunches, just a little, in order to make sure that I catch the whole thing."
                    "The white streamers land mostly on my tongue, some dripping onto my chin before I can curl it and save them from being lost."
                    "Soon I have a veritable mouthful of cum, all pooled in the middle of my tongue."
                    "I swallow it down slowly and with a look of infinite satisfaction on my face, savouring like it was a rare delicacy or a fine wine."
                    "Finally, I lick my lips for the last few droplets, relishing every single speck that I can find."
                "Finsh with a bang" if game.get_flag_value("morality") <= -25:
                    if game.get_flag_value("morality") >= -50:
                        $ game.set_flag("morality",1,mod="-")
                    "Slowly I draw him out of my mouth, teasing him with tongue, teeth and lips one final time."
                    "He loses it just as I pull the head of his cock between my lips in a last kiss."
                    "This means that a little of his cum clings to my lips, but the rest is able to erupt in the open."
                    "It does so less than an inch from my face, meaning that I get showered in tight, looping whorls even as the actual shower washes them away again."
                    "I make no effort to speed the water's efforts to cleanse me of Mike's cum, instead smiling up at him in amusement."
            "Neither of us speaks as we let the shower clean us up one final time."
            "But I note that Mike silently takes hold of my hand as we walk out of the bathroom, not letting go until we reach my bedroom door and I slip inside."
            "Sleep comes easily after that, and the last thing on my mind before I drift off is the feeling of his cock between my lips."
    return


label mike_give:
    if not "Guitar book" in hero.inventory.keys():
        $ gift = Consumable("Guitar practice book", money_cost = 100, label = ["guitar_practice_book"], uses = 10)
        "She hands me a pretty large book."
        hero.say "Wow !\nIs that a book with guitar tricks?"
        mike.say "It sure is..."
        hero.say "Thank you so much."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "He hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label mike_give_valentine:
    show mike
    "Mike walks hesitantly towards me."
    call mike_greet from _call_mike_greet_7
    show mike blush
    mike.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Mike hands me a box of chocolates."
    hero.say "Thank you, Mike."
    $ hero.gain_item(gift)
    hide mike
    return

label mike_give_birthday:
    show mike
    "Mike walks towards me."
    call mike_greet from _call_mike_greet_8
    show mike happy
    mike.say "Happy birthday [hero.name]!"
    call mike_give from _call_mike_give
    return

label mike_give_christmas:
    show mike
    "Mike walks towards me."
    call mike_greet from _call_mike_greet_9
    show mike happy
    mike.say "Merry christmas [hero.name]."
    call mike_give from _call_mike_give_1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
