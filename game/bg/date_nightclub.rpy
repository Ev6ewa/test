layeredimage bg date_nightclub:
    always:
        "nightclub"

init -2 python:
    Date(
        "nightclub",
        display_name="Nightclub",
        money_cost=30,
        conditions = ['(game.get_flag_value("female") and "fancy dress" in hero.inventory.keys()) or (not game.get_flag_value("female") and "fancy clothes" in hero.inventory.keys())'],
        game_conditions={"valid_room":"date_nightclub"},
        clothes = "date",
        love_gain = 2,
        )

    Room(**{
        "name":"date_nightclub",
        "hours": (22,5),
        "display_name": "Nightclub",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "music": "music/Nihilore/Apricity.mp3",
        "outfit":"date"
        })

    Event(**{
        "name":"date_nightclub_random_events",
        "label": ["date_nightclub_random_events"],
        "duration": 0,
        "priority": 0,
        "game_conditions": {
            "room":["date_nightclub"],
            "chances":20,
            },
        "do_once": False,
        "once_day": True,
        "quit": True
        })

label date_nightclub:
    show expression game.active_girl.id
    "We go to the nightclub."
    $ renpy.hide((game.active_girl.id))
    return

label date_nightclub_random_events:
    scene bg park
    show expression date_girl.id
    $ r = randint(1,10)
    if r <= 1:
        "We've been on the dancefloor for a little while when I notice a guy showing marked interest in [date_girl.name]."
        "He keeps on dancing ever closer to her, not seeming in the least bit concerned about my presence."
        "[date_girl.name] seems to have noticed his interest in her too."
        menu:
            "Leave it to the girl to see him off":
                "I glare at the guy and then at [date_girl.name], hoping that she'll take the hint and tell the creep to get lost."
                if date_girl.has_trait("flirty"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl] either doesn't get the point, or else just chooses to completely ignore me."
                    "In fact, she actively encourages the guy more the closer that he gets!"
                elif date_girl.has_trait("submissive"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl] seems to get my point, but then just meekly quivers as the guy dances ever closer to her."
                else:
                    "[date_girl] shakes her head at the guy's obvious attempt to cut in and then turns her back on him."
            "Tell the guy where to get off":
                hero.say "Hey, man - I'm standing right here in front of you."
                hero.say "Stop trying to dance with my date and get lost!"
                if date_girl.has_trait("flirty"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl] smiles broadly at my asserting my manhood, and disdainfully shoos the other guy away."
                elif date_girl.has_trait("submissive"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl] almost clings to me in desperation as I stake my claim for her and push the other guy away."
                elif date_girl.has_trait("dominant"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl] look at me with disdain."
                else:
                    "[date_girl] gives the other guy a brief smile, but seems to be happy that I stood up to him."
                    $ game.set_flag("datescore",10,"day","+")
    elif r <= 2:
        "We're sitting at a table away from the dancefloor, waiting for the music to get better when one of the bar-staff comes over with a tray of drinks."
        "She puts one down in front of me and turns to go without as much as a word of explanation, and so I stop her before she can leave."
        hero.say "Hey, I didn't order this!"
        "She shrugs and points to a table of girls nearby, indicating that they sent the drink over for me."
        "[date_girl.name] looks in the direction that the barmaid is pointing and sees the girls laughing and waving at me."
        menu:
            "Refuse the drink":
                hero.say "I'm sorry, but I can't accept this - please take it away and don't bring anything else form them over here."
                if date_girl.has_trait("yandere"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl]'s eyes almost flash with delight at this gesture, delighting in my show of loyalty to her."
                elif date_girl.has_trait("slutty"):
                    $ game.set_flag("datescore",5,"day","-")
                    "[date_girl] looks confused, as if she's not sure why anyone would turn down a free drink."
                else:
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl] smiles and shakes her head, annoyed at the other girls flirting, but also pleased at my ignoring their efforts in favour of her."
            "Accept the drink":
                hero.say "Wow, that's really flattering!"
                hero.say "And it'd be plain rude to turn it down, right?"
                if date_girl.has_trait("yandere"):
                    $ game.set_flag("datescore",10,"day","-")
                    $ date_girl.set_flag("yandere",1,mod="+")
                    "[date_girl]'s eyes go cold and hard, making me wonder if she's madder at me or the girls that sent over the drink."
                elif date_girl.has_trait("slutty"):
                    "[date_girl] shrugs and nods, as if she'd have done the same thing and not thought twice about it either."
                else:
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl] frowns as I take a sip of the drink, not very pleased at my encouraging the girls on the other table."
























    elif r <= 3:
        "The club is very busy tonight, and I can see that [date_girl.name] looks pretty tired of being jostled and elbowed by the other clubbers."
        "I take a glance over at the VIP section and see that, in stark contrast to the rest of the place, it's virtually empty."
        "I take[date_girl.name] by the hand and shove my way through to where a bouncer is manning the entrance."
        menu:
            "Bribe the bouncer to get into the VIP section":
                hero.say "Hey - you want to see my VIP membership?"
                "As the bouncer leans over, I shove as much money as I can spare into his hand."
                "In response, he nods briefly and lifts the rope to allow us entry."
                if date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] swans straight into the deserted VIP section, a huge and rather smug smile plastered across her face."
                elif date_girl.has_trait("poor"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] shakes her head as she reluctantly follows me into the VIP section, seeming to think what I just did was pretty vulgar."
                else:
                    "[date_girl.name] laughs at my audacity to offer the bouncer a bribe, but follows close on my heels all the same."
            "Make fun of the fact the VIP section is so empty":
                hero.say "Look at all that wasted space, with no wastes of space to fill it up!"
                if date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] pouts and makes a huffing sound, clearly thinking that I was going to get us in there somehow."
                elif date_girl.has_trait("poor"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] grins and laughs at my joke, clearly relieved that I didn't try to get us into the VIP section somehow."
                else:
                    "[date_girl.name] chuckles at my joke, but still can't help eyeing up the free space in the VIP section as we keep on being squashed by the bodies around us."
    elif r <= 4:
        "I really can't recall just how long we've been on the dancefloor, but [date_girl.name] just seems to love every song the DJ plays."
        "My limbs are starting to feel like they're made of lead, and collapsing into bed to sleep is the most enjoyable thing I can imagine right now."
        "But all it takes is one glance at [date_girl.name] to see that she's still full of energy and wanting to keep on going."
        menu:
            "Say that you want to call it a night":
                hero.say "Hey - I'm dead on my feet out here and I have work tomorrow!"
                hero.say "You mind if we call it a night?"
                if date_girl.has_trait("workaholic"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] looks disappointed, but nods as if she understands the need to be fresh for the office in the morning."
                elif date_girl.has_trait("lazy"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] shakes her head in relief."
                elif date_girl.has_trait("sporty"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] shakes her head in disbelief, looking at me like I'm an old man."
                else:
                    "[date_girl.name] shrugs and then nods, clearly wanting to stay and yet indulging me all the same."
            "Ignore your tiredness and keep on going":
                "I know that I'll regret it in the morning, but I just can't let [date_girl.name] down."
                if date_girl.has_trait("sporty"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] keeps right on going, not seeming to note the ever-decreasing speed with which I manage to keep up."
                elif date_girl.has_trait("lazy"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] shakes her head in disbelief, looking at me like I'm torturing her."
                else:
                    "[date_girl.name] soon notices the terrible state I'm in, and motions for a time-out away from the dancefloor so that I can recover."
    elif r <= 5:
        "I've been in this club before, but I never noticed that they actually have a dancing pole in one of the corners for the use of club-goers."
        "I must have been staring at it for quite a while, as I look round to see [date_girl.name] regarding me with curiosity in her eyes."
        "Clearly she's interested in hearing what I have to say about the pole..."
        menu:
            "Suggest that she try it out":
                hero.say "That looks like it could be fun..."
                if date_girl.has_trait("trashy"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] seems to catch my drift almost instantly, smiling and walking over to the pole in a provocative manner."
                elif date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] gives me scowl of offence, and walks away from the pole."
                elif date_girl.has_trait("playful"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] shakes her head and points at me, suggesting that she wants me to go first."
                else:
                    "[date_girl.name] gives me a mock scowl of offence, but doesn't seem like she's going to take the hint and actually use the pole."
            "Dismiss the pole as sexist":
                hero.say "Urgh, how typically sexist!"
                if date_girl.has_trait("trashy"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] frowns at me, as if I'm speaking a foreign language that she doesn't understand."
                elif date_girl.has_trait("bookworm"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] nods in apparent agreement as she pulls me out of sight of the pole."
                else:
                    "[date_girl.name] shrugs, as if she's not particularly interested in or offended by the presence of the pole."
    elif r <= 6:
        "We're in the middle of the dancefloor when something that's currently doing the rounds in the download charts gets played."
        "It's one of those stupid, manufactured and yet incredibly catchy tracks that's the very definition of an earworm."
        "[date_girl.name] looks at me to see what my reaction will be..."
        menu:
            "Dance to the song":
                "Unable to keep from being swept up in the moment, I start to dance like I just can't help myself and there's no one watching me."
                if date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] bursts into laughter and immediately rushes to join in."
                elif date_girl.has_trait("guitar"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] looks mortified with embarrassment, clearly shocked that I'd be into something so shallow and trashy."
                else:
                    "[date_girl.name] looks surprised, like she's not sure what to make of my actions."
            "Walk off the dancefloor":
                hero.say "Oh no - I can't dance to this kind of shite!"
                if date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] follows in my wake, looking puzzled as to what's gone wrong with the music all of a sudden."
                elif date_girl.has_trait("guitar"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] smiles as she allows me to usher her off of the dancefloor, obviously sharing the same sentiment about the music."
                else:
                    "[date_girl.name] doesn't seem as concerned as me, but follows me off of the dancefloor all the same."
    elif r <= 7:
        "Before I've even raised the drink I just bought halfway to my mouth, a guy bumps into me and sends it spilling to the floor."
        hero.say "Hey, watch it!"
        "The culprit stops in his tracks and then turns to regard me."
        "[date_girl.name] looks on with interest to see what my next move will be."
        menu:
            "Tell the guy off":
                hero.say "That was a full glass, you clumsy wanker!"
                hero.say "You'd better cough up for another - and quick!"
                "Much to my relief, the guy apologises and hands over the money to replace my drink."
                if date_girl.has_trait("submissive"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] almost trembles as she watches me chew the poor sap out."
                elif date_girl.has_trait("dominant"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] seems oddly cold at the sight of me asserting myself in front of her."
                else:
                    "[date_girl.name] looks relieved that the confrontation is over, but doesn't object to me standing my ground all the same."
            "Let it go":
                hero.say "Erm...never mind - I shouldn't have been in your way, I guess..."
                if date_girl.has_trait("submissive"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] looks puzzled, as though she's disappointed in my lack of spine."
                elif date_girl.has_trait("dominant"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] smiles at the sight of me shying away from the confrontation, as though it confirms her opinion of me."
                else:
                    "[date_girl.name] gives me a weak smile, clearly glad to avoid a scene and yet not be seen to be judging me at the same time."
    elif r <= 8:
        "[date_girl.name]'s eyes follow a couple of girls dressed in almost impossible amounts of bling tottering past."
        "They breeze through into the VIP section almost without pausing to take a breath, as if they were simply meant to be there by reason of their haughtiness."
        "I'm not sure whether [date_girl.name] is jealous or disdainful of them, but I get the impression I should say something either way..."
        menu:
            "Compliment the girls":
                hero.say "Wow, no wonder they got let straight into the VIP section."
                hero.say "They really look like they belong in there!"
                if date_girl.has_trait("bitchy"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] snorts and looks at me as though my spine just dropped out of my arsehole."
                else:
                    $ game.set_flag("datescore",5,"day","-")
                    "[date_girl.name] sighs and nods, clearly not happy with the situation, but powerless to do anything about it either."
            "Insult the girls":
                hero.say "I never knew that VIP could stand for 'very insecure prostitutes'..."
                if date_girl.has_trait("bitchy"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] laughs out loud at my taking such a shot at the tarted-up girls, grinning wickedly the whole time."
                else:
                    "[date_girl.name] slaps me on the arm in disapproval, but can't help laughing all the same."
    elif r <= 9:
        "I don't have a chance to see how it gets started, but all of a sudden [date_girl.name] is exchanging angry words with a girl I've never seen before."
        "Soon they're pushing and shoving at each other, with attempts being made on both sides to grab handfuls of hair."
        "I only have a couple of seconds in which to decide what I should do..."
        menu:
            "Wade in and pull the other girl off":
                hero.say "Get your hands off of her, you crazy bitch!"
                "I wade straight into the middle of them, stepping in front of [date_girl.name] and shoving the other girl firmly away."
                "The stranger shouts something at [date_girl.name] while I block her way, and then pushes her way through the crowd and disappears."
                if date_girl.has_trait("rebel"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] crosses her arms over her chest and shakes her head, clearly unhappy that I didn't let her handle matters herself."
                elif date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] clings to me with all her might, grateful for being saved from any harm befalling her."
                else:
                    "[date_girl.name] looks shaken and angry, but a whole lot more relieved that it's over."
            "Let them settle it themselves":
                "It's the twenty-first century, and I figure that a woman should be able to stand up for herself."
                "What follows is a brief and inconclusive scuffle, where it's hard to tell who comes off the worst."
                if date_girl.has_trait("rebel"):
                    $ game.set_flag("datescore",10,"day","+")
                    "Nevertheless, [date_girl.name] smiles triumphantly as she wipes the blood off of her lip and shows me the handful of hair she tore from the other girl's scalp."
                elif date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] sniffles and wipes a tear from her eye as she nurses the bruises and scrapes she earned in the fight, still unable to believe that I didn't come to her aid."
                else:
                    $ game.set_flag("datescore",5,"day","-")
                    "[date_girl.name] looks pretty shaken up as she walks away from the fight, but I console myself with the thought that the other girl looked just as beaten up too."
    hide expression date_girl.id
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
