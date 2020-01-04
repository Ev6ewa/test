layeredimage bg date_park:
    if game.hour >= 20 or game.hour <= 5 and game.season == 0:
        "park_0_night"
    elif game.season == 0:
        "park_0_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 1:
        "park_1_night"
    elif game.season == 1:
        "park_1_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 2:
        "park_2_night"
    elif game.season == 2:
        "park_2_day"
    elif game.hour >= 20 or game.hour <= 5 and game.season == 3:
        "park_3_night"
    elif game.season == 3:
        "park_3_day"

init -2 python:
    Room(**{
        "name":"date_park",
        "exits": ["map"],
        "alternate_exits": ["map"],
        "display_name": "park",
        "hours": (14,18),
        "music": "music/TRG_Banks/the_night_bus.mp3",
        "outfit":"casual"
        })

    Date(
        "park",
        display_name="park",
        clothes = "casual",
        game_conditions={"valid_room":"date_park"},
        love_gain = 2,
        )

    Activity(**{
        "name": "date_go_for_a_run",
        "duration": 1,
        "fun":1,
        "icon":"jog",
        "display_name": "Run together",
        "game_conditions": {"min_fitness":10,"room":["date_park"]},
        "label": ["date_go_for_a_run"],
        "once_day": True
        })

    Activity(**{
        "name": "date_read_poetry",
        "duration": 1,
        "fun":1,
        "icon": "sing",
        "display_name": "Read poetry",
        "label": ["date_read_poetry"],
        "game_conditions": {"min_knowledge":10,"room":["date_park"]},
        "once_day": True
        })

    Activity(**{
        "name": "date_picnic",
        "duration": 1,
        "fun":1,
        "icon": "picnic",
        "display_name": "Have a picnic",
        "label": ["date_picnic"],
        "game_conditions": {"room":["date_park"], "seasons":"012"},
        "once_day": True
        })

    Activity(**{
        "name": "date_cloud_gaze",
        "duration": 1,
        "fun":1,
        "icon": "clouds",
        "display_name": "Watch the clouds",
        "game_conditions": {"min_charm":10,"room":["date_park"]},
        "label": ["date_cloud_gaze"],
        "once_day": True
        })

    Activity(**{
        "name": "date_snow_ball_fight",
        "duration": 1,
        "fun":1,
        "icon": "snowball",
        "display_name": "Have a snowball fight",
        "game_conditions": {"min_fitness":10, "seasons":"3","room":["date_park"]},
        "label": ["date_snow_ball_fight"],
        "once_day": True
        })

    Activity(**{
        "name": "date_make_snowman",
        "duration": 1,
        "fun":1,
        "icon": "snowman",
        "display_name": "Make a snowman",
        "game_conditions": {"min_charm":10, "seasons":"3","room":["date_park"]},
        "label": ["date_make_snowman"],
        "once_day": True
        })

    Event(**{
        "name":"date_park_random_events",
        "label": ["date_park_random_events"],
        "duration": 0,
        "priority": 0,
        "game_conditions": {
            "room":["date_park"],
            "chances":20,
            },
        "do_once": False,
        "once_day": True,
        "quit": True
        })












label date_park_random_events:
    scene bg park
    show expression date_girl.id
    $ r = randint(1,10)
    if r <= 1 and game.season == 3:
        "It's so bitingly cold today that I'm glad to have wrapped up with more warm layers than I would usually have bothered with."
        "But a casual glance at [date_girl.name] shows me that she's shivering and I can almost hear her teeth chattering"
        menu:
            "Offer her your coat":
                hero.say "I can't believe I've been so rude as not to notice that you were cold."
                hero.say "Here, let me lend you my coat."
                if date_girl.has_trait("princess"):
                    "[date_girl.name] accepts the offer without hesitation, happy to be on the receiving end of such kindness."
                    $ game.set_flag("datescore",10,"day","+")
                elif date_girl.has_trait("rebel"):
                    "[date_girl.name] shakes her head in disgust at the offer and walks on ahead, rubbing her arms for added warmth."
                    $ game.set_flag("datescore",10,"day","-")
                else:
                    "[date_girl.name] refuses for a short while, and then grudgingly accepts the offer."
                    $ game.set_flag("datescore",5,"day","+")
            "Do not offer her your coat":
                hero.say "That outfit looks real good on you, but it sure looks cold as well!"
                if date_girl.has_trait("princess"):
                    "[date_girl.name] makes a haughty noise and turns her nose up at me, clearly having been expecting more than a critical comment."
                    $ game.set_flag("datescore",10,"day","-")
                if date_girl.has_trait("rebel"):
                    "[date_girl.name] frowns as if she doesn't particularly care and just shakes her head, as if not in the least bit bothered about the discomfort."
                    $ game.set_flag("datescore",5,"day","+")
                else:
                    "[date_girl.name] looks a little hurt at the blunt nature of my comment, rubbing her arms in an attempt to generate more warmth."
                    $ game.set_flag("datescore",5,"day","-")
    elif r <= 2 and game.season == 1:
        "The grassy areas of the park are almost all covered with people playing casual games and sports."
        "Eventually the inevitable happens, and a football rolls to a stop, right by my feet."
        "As the people to whom it belongs begin to call for it back, [date_girl.name] looks at me to see what my reaction will be."
        menu:
            "Punt the ball back":
                "I take a couple of steps back and punt the ball as hard as I can in their direction."
                "It's nothing particularly impressive, but it gets the job done all the same."
                if date_girl.has_trait("sportsy"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] seems impressed with the way I stepped up to even such a minor challenge."
                elif date_girl.has_trait("geek"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] looks surprised that I'd even know what to do with a football without an explanation."
                else:
                    $ game.set_flag("datescore",5,"day","+")
                    "[date_girl.name] doesn't seem in the least bit perturbed or impressed by what just happened, and so we just walk on."
            "Ignore the ball and walk on":
                "Afraid that I'll just send the ball flying in the wrong direction, I ignore it and pretend not to have heard the cries of its owners behind me as I walk on."
                if date_girl.has_trait("sportsy"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] says nothing, but I can see her shaking her head in disbelief that I'd be so timid."
                elif date_girl.has_trait("geek"):
                    $ game.set_flag("datescore",5,"day","+")
                    "[date_girl.name] keeps quiet, but I can see a look of empathy in her eyes, as if she'd have done the same thing for simiar reasons."
                else:
                    $ game.set_flag("datescore",5,"day","-")
                    "[date_girl.name] doesn't seem in the least bit perturbed or impressed by what just happened, and so we just walk on."
    elif r <= 3:
        "I can vaguely hear the sound of someone calling out in vain for an errant dog to come to heel."
        "[date_girl.name] yelps in surprise and alarm, making me glance round to see a large and very slobbery dog bearing down on us."
        menu:
            "Recoil from the dog":
                "I've never been too keen on big dogs, and this one seems to have appeared out of nowhere."
                "I cry out too and back off from the dog, trying to keep it from getting any closer."
                if date_girl.has_trait("innocent"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] clings to me, looking relieved to see me have the same reaction as she did."
                elif date_girl.has_trait("playful"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] looks surprised at my reaction, and instantly goes to pet the approaching dog."
                else:
                    $ game.set_flag("datescore",5,"day","-")
                    "[date_girl.name] makes no move to approach the dog, but looks a little surprised at my dramatic reaction to it all the same."
            "Pet the dog":
                "I'm fond enough of dogs to know that this one just wants to play, so I hold out my hand and encourage him to come closer for a fuss."
                if date_girl.has_trait("innocent"):
                    "[date_girl.name] cries out again, not reassured by my example, and hides behind my back."
                    $ game.set_flag("datescore",10,"day","-")
                elif date_girl.has_trait("playful"):
                    "[date_girl.name] follows my lead, and soon we're showering the happy dog with praise and attention as his owner approaches."
                    $ game.set_flag("datescore",10,"day","+")
                else:
                    "[date_girl.name] smiles at my petting the eager dog, but doesn't seem inclined to join me in doing so any time soon."
                    $ game.set_flag("datescore",5,"day","+")
    elif r <= 4:
        "Walking through a secluded part of the park, it occurs to me that a spot amongst the trees is almost completely hidden from the view of the path we're on."
        "[date_girl.name] notices the attention that I'm giving the little nook and looks at me for an explanation."
        menu:
            "Admit it looks inviting for an amorous liaison":
                hero.say "I bet no one would be able to see us in there - no matter what we were getting up to..."
                if date_girl.has_trait("slutty"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] grins wickedly, instantly picking up on the possibilities of sex in a public place."
                elif date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] gives me a puzzled look, as if she thinks I mean to use the spot to piss in or something just as mundane."
                else:
                    $ game.set_flag("datescore",5,"day","-")
                    "[date_girl.name] smiles indulgently, but I get the impression she has a more pure and romantic image of the whole thing than I do."
            "Say it could be used for a prank":
                hero.say "I mean, you could jump out on someone walking past, really make them shit themselves!"
                if date_girl.has_trait("slutty"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] stares at me, amazed that I'd miss such a blatant opportunity to misbehave in public."
                elif date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] giggles and snorts at the thought of pulling off just such a prank."
                else:
                    $ game.set_flag("datescore",5,"day","+")
                    "[date_girl.name] shakes her head, not sure if she should find my childish suggestion pathetic or endearing."
    elif r <= 5:
        "I have to confess to being rather fond of admiring female joggers as they pass me in the park."
        "Unfortunately for me, it's become such a habit, that when a couple sprint past, I totally forget who's company I'm currently in."
        "[date_girl.name] notes my interest in their lycra-clad forms, making me stutter to explain myself."
        menu:
            "Admit that you were looking":
                hero.say "I'm sorry, I guess I just have a thing for tight clothing on a tight body!"
                if date_girl.has_trait("flirty"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] smiles and squeezes my hand, giving me the distinct impression that she's storing that little admission away for a later date."
                elif date_girl.has_trait("yandere"):
                    $ game.set_flag("datescore",10,"day","-")
                    $ date_girl.set_flag("yandere",1,mod="+")
                    "[date_girl.name] almost ignores what I say, as she shoots evil, almost threatening glances at the joggers as they disappear around a corner up ahead."
                else:
                    "[date_girl.name] shakes her head a little ruefully, but seems to appreciate my honesty all the same."
            "Make an insulting comment":
                hero.say "You need a really tight arse to pull that look off, not a bag of blamanche like that!"
                if date_girl.has_trait("bitchy"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] sneers a little and nods in agreement, clearly amused by my putting the other girls down in front of her."
                else:
                    $ game.set_flag("datescore",5,"day","-")
                    "[date_girl.name] gives me a scrutinising look, as if she's not sure she believes I was just looking to pass judgement on the joggers."
    elif r <= 6:
        "As we walk past a stand of trees, the sound of someone playing a guitar and singing can be heard."
        "When the musician comes into view, I see a long-haired, hippy kind of guy being adored by at least half-a-dozen girls."
        "[date_girl.name] smiles sideways at me, clearly looking to discover just what I think of the scene."
        menu:
            "Dismiss the guitarist as a jerk":
                hero.say "Urgh...what a creepy layabout!"
                if date_girl.has_trait("workaholic"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] raises her eyebrows in approval and snorts derisively at the fawning crowd around the bohemian guitarist."
                elif date_girl.has_trait("guitar"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] shakes her head and snorts at my dismissing the guitarist, clearly thinking that I'm just jealous of the attention that he's attracting."
                else:
                    "[date_girl.name] shrugs, as if she's not convinced that I'm being entirely unbiased in my assessment of the guitarist and might be just a little jealous."
            "Envy the guitarist his popularity":
                hero.say "I sometimes wish I could make a living doing something like that!"
                if date_girl.has_trait("workaholic"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] shakes her head in disapproval, clearly not impressed by the bohemian guitarist or my desire to emulate him."
                elif date_girl.has_trait("guitar"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] smiles in genuine approval, pressing herself a little closer to me now she knows I desire a bohemian lifestyle too."
                else:
                    "[date_girl.name] shrugs, as though she's not particularly interested in the idea of emulating what pretty much amounts to a busker."
    elif r <= 7:
        "The green spaces of the park are almost totally full of happy, laughing families, their picnics spread out on colourful blankets."
        "Parents sit on the ground, while kids toss frisbees and play with bouncy dogs."
        "I see that [date_girl.name] is staring intently at the scene, and she turns her head, catching me staring at her in turn."
        menu:
            "Gush over the happy families":
                hero.say "Wow...I really hope that I could be as happy as those guys look one day!"
                if date_girl.has_trait("family"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] squeezes my hand suddenly and smiles as widely as her mouth can manage."
                    "It seems like I've said something that she very much approves of..."
                elif date_girl.has_trait("not_family"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name]'s mouth hangs open as she almost literally shudders at the thought of being in the same position as the parents on their picnic blankets."
                else:
                    "[date_girl.name] gives me an enigmatic grin, but doesn't say as much as a word in way of response."
            "Shudder at the thought of being tied down with a family":
                hero.say "I could never be that guy, you know - so tied down that I couldn't just up and walk away if the mood took me."
                if date_girl.has_trait("family"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] looks at me with an expression of surprise and not a little saddness on her face."
                elif date_girl.has_trait("not_family"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] gives me a slow and very much approving smile, letting me know that she feels the exact same way too."
                else:
                    "[date_girl.name] gives me an enigmatic grin, but doesn't say as much as a word in way of response."
    elif r <= 8:
        "We had been planning on going for walk around the park, but the amazingly hot weather sees us finding a suitable spot and just laying down instead."
        "As I settle down to enjoy the sun, I notice that a couple of girls nearby have actually gone topless, right here in the park!"
        "[date_girl.name] follows my gaze and sees the same thing, and then looks at me as if challenging me to explain my interest in the sight."
        menu:
            "Disapprove of the topless sunbathing":
                hero.say "God, what are they even thinking doing that here!"
                hero.say "It's not like this is the beach."
                if date_girl.has_trait("trashy"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] shrugs and keeps on admiring the sight of the girls, as if she's impressed by their boldness."
                elif date_girl.has_trait("submissive") or date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] nods furiously, as if she's almost too eager to second my disapproval."
                else:
                    "[date_girl.name] shrugs, as if to say that she's not particularly interested in what other people are doing right now."
            "Applaud the daring of the topless sunbathers":
                hero.say "Wow...those are some seriously liberated young ladies over there!"
                if date_girl.has_trait("trashy"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] chuckles and shakes her head, as if taking my admiration for the topless sunbathers as a personal challenge."
                    "One that she will have to rise to at a later date..."
                elif date_girl.has_trait("submissive") or date_girl.has_trait("princess"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] looks at me as if she's been given an outright order, and begins to unbutton her top..."
                else:
                    "[date_girl.name] shrugs, as if to say that she's not particularly interested in what other people are doing right now."
    elif r <= 9:
        "I spot that a new cafe has opened up in the park, and then remember hearing pretty good things about it too."
        "It's getting close to lunchtime, and I wonder if we should call in and grab a bite to eat."
        "[date_girl.name] notices the cafe too, and then that I'm looking at it with interest."
        menu:
            "Suggest that you grab a bite to eat at the cafe":
                hero.say "You feeling hungry?"
                hero.say "What about grabbing a bite to eat here?"
                if date_girl.has_trait("poor"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] keeps on staring at the fancy decor of the place, and I begin to wonder if I've made a mistake."
                elif date_girl.has_trait("gourmand"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] nods with enthusiasm, practically pulling me towards the door."
                else:
                    "[date_girl.name] give me a 'what-the-hell' smile, and seems to want to leave the ultimate decision up to me."
            "Suggest that you just eat a hotdog":
                hero.say "You know, places like that are always over-priced."
                hero.say "How about we heat a hotdog?"
                if date_girl.has_trait("poor"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] nods and smiles, looking positively relieved at my suggestion."
                elif date_girl.has_trait("gourmand"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name]'s face falls at my suggestion, and she looks back over her shoulder longingly as we walk away."
                else:
                    "[date_girl.name] shrugs and shakes her head, as if to say that she's fine with whatever."
    elif r <= 10:
        "I hear voices from around the corner, and then see a large group of people come into view as we walk around it."
        "Craning my neck, I can just see that the crowd has gathered to watch what looks like a play being performed in the open air."
        "[date_girl.name] spots the same thing, standing up on her tip-toes to get a better look."
        menu:
            "Suggest that you stay and watch":
                hero.say "I've never seen a play performed in the open air before."
                hero.say "Maybe we should hang around and watch for a while?"
                if date_girl.has_trait("bookworm"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] nods with enthusiasm, already looking for a way into the crowd."
                elif date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] rolls her eyes and sighs dramatically, as though the idea is the most tedious thing ever."
                else:
                    "[date_girl.name] gives a nonchalant shrug, as if she's equally happy to indulge me or simply walk on by."
            "Sneer at the players":
                hero.say "What a set of geeks - imagine wasting a day like this performing a play, let alone watching one!"
                if date_girl.has_trait("bookworm"):
                    $ game.set_flag("datescore",10,"day","-")
                    "[date_girl.name] frowns at me and furrows her brows, as if resisting the temptation to call me an uncultured oaf."
                elif date_girl.has_trait("dumb"):
                    $ game.set_flag("datescore",10,"day","+")
                    "[date_girl.name] laughs and nods in agreement, shaking her head at the crowd as we walk away."
                else:
                    "[date_girl.name] shakes her head, as if she's not particularly interested in or offended by the presence of the play and its audience."
    hide expression date_girl.id
    return

label date_picnic:
    show expression game.active_girl.id
    hero.say "Let's have a picnic."
    if game.active_girl.has_trait("gourmand"):
        active_girl.say "Great idea!"
        $ game.set_flag("datescore",10,1,"+")
    else:
        active_girl.say "I'd love to."
        $ game.set_flag("datescore",5,"day","+")
    $ renpy.hide((game.active_girl.id))
    return

label date_make_snowman:
    show expression game.active_girl.id
    hero.say "Let's make a snowman."
    if not game.active_girl.has_trait("artsy") and not game.active_girl.has_trait("playful"):
        active_girl.say "I don't feel like it."
        $ game.set_flag("datescore",10,1,"-")
        $ hero.activity.set_flag("canceled",True)
    else:
        active_girl.say "I'd love to."
        "We make a snowman together."
        $ game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    return

label date_snow_ball_fight:
    show expression game.active_girl.id
    "I throw a snowball at [game.active_girl.name]"
    if not game.active_girl.has_trait("playful"):
        active_girl.say "Stop it, that's not funny."
        $ game.set_flag("datescore",10,1,"-")
        $ hero.activity.set_flag("canceled",True)
    else:
        active_girl.say "Hey, You'll pay for that !."
        "We have fun having a snowball fight."
        $ game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    return

label date_cloud_gaze:
    show expression game.active_girl.id
    hero.say "Let's watch the clouds."
    if not game.active_girl.has_trait("dreamer"):
        active_girl.say "No, thank you."
        $ game.set_flag("datescore",10,1,"-")
        $ hero.activity.set_flag("canceled",True)
    else:
        active_girl.say "Yes, sure."
        "We sit on a bench and watch at funny clouds."
        $ game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    return

label date_read_poetry:
    show expression game.active_girl.id
    hero.say "Would you like me to read you some poetry ?"
    if not game.active_girl.has_trait("bookworm") and not game.active_girl.has_trait("artsy") and not game.active_girl.has_trait("dreamer"):
        active_girl.say "No, thank you."
        $ game.set_flag("datescore",10,1,"-")
        $ hero.activity.set_flag("canceled",True)
    else:
        active_girl.say "Yes, sure."
        "We sit under a tree and I start reading her some poetry."
        $ game.set_flag("datescore",5,1,"+")
    $ renpy.hide((game.active_girl.id))
    return

label date_go_for_a_run:
    show expression game.active_girl.id
    hero.say "Let's go for a run."
    if not game.active_girl.has_trait("sportsy"):
        active_girl.say "No, thank you."
        $ game.set_flag("datescore",10,1,"-")
        $ hero.activity.set_flag("canceled",True)
    else:
        "[game.active_girl.name] quickly change into her sports clothes."
        show expression game.active_girl.id+" sport"
        active_girl.say "Ready whenever you are."
        "We have a good race."
        $ game.set_flag("datescore",5,1,"+")
        show expression game.active_girl.id+" casual"
    $ renpy.hide((game.active_girl.id))
    return

label date_park:
    show expression game.active_girl.id
    "We go to the park."
    $ renpy.hide((game.active_girl.id))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
