init python:

    Event(**{
        "name":"aletta_init",
        "label": ["aletta_init"],
        "girls_conditions": {"aletta":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "aletta_event_01",
        "label": ["aletta_event_01"],
        "game_conditions": {"min_charm":30,"activity":"coffee_break", "flag_female":0},
        "girls_conditions": {"aletta":{"room":["office","alettaoffice"]}},
        "priority": 500,
        "clothes": "work",
        "do_once": True
        })

    Event(**{
        "name": "aletta_event_02",
        "label": ["aletta_event_02"],
        "game_conditions": {"min_charm":40,"activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "girls_conditions": {"aletta":{"min_love":20, "flageq_story":1,"room":["office","alettaoffice"]}},
        "priority": 500,
        "clothes": "work",
        "do_once": True
        })

    Event(**{
        "name": "aletta_event_03",
        "label": ["aletta_event_03"],
        "game_conditions": {"min_charm":50,"activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "girls_conditions": {"aletta":{"min_love":40, "flageq_story":2,"room":["office","alettaoffice"]}},
        "priority": 500,
        "clothes": "work",
        "do_once": True
        })

    Event(**{
        "name": "aletta_event_03b",
        "label": ["aletta_event_03b"],
        "game_conditions": {"min_charm":55,"room":["map"], "flag_female":0, "days": "67", "hours":(12,18)},
        "girls_conditions": {"aletta":{"min_love":50}},
        "priority": 500,
        "clothes": "suit",
        "do_once": True
        })

    Event(**{
        "name": "aletta_event_04",
        "label": ["aletta_event_04"],
        "game_conditions": {"min_charm":60,"activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "girls_conditions": {"aletta":{"min_love":60, "flageq_story":3,"room":["office","alettaoffice"]}},
        "priority": 500,
        "clothes": "work",
        "do_once": True
        })

    Event(**{
        "name": "aletta_event_04b",
        "label": ["aletta_event_04b"],
        "game_conditions": {"min_charm":70, "flag_female":0, "days": "6", "hours":(9,11), "done":"aletta_event_03b"},
        "girls_conditions": {"aletta":{"min_love":70, "flageq_sidestory":1}},
        "priority": 500,
        "clothes": "suit",
        "do_once": True
        })

    Event(**{
        "name": "aletta_event_05",
        "label": ["aletta_event_05"],
        "game_conditions": {"min_charm":80,"activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "girls_conditions": {"aletta":{"min_love":80, "flageq_story":4,"room":["office","alettaoffice"]}},
        "priority": 500,
        "clothes": "work",
        "do_once": True
        })

    Event(**{
        "name": "aletta_event_05b",
        "label": ["aletta_event_05b"],
        "game_conditions": {"min_charm":90,"room":["livingroom"], "flag_female":0, "days": "6", "hours":(9,12), "done":"aletta_event_04b"},
        "girls_conditions": {"aletta":{"min_love":100, "flageq_sidestory":2}},
        "priority": 500,
        "clothes": "suit",
        "do_once": True
        })

    Event(**{
        "name": "aletta_investigation_callback",
        "label": ["aletta_investigation_callback"],
        "game_conditions": {"hours":(9,14)},
        "girls_conditions": {"aletta":{"countermin_investigationcallback":2, "present": False}},
        "do_once": True
        })

    Event(**{
        "name": "aletta_give_christmas",
        "label": ["aletta_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"aletta":{"min_love":50, "present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "aletta_give_birthday",
        "label": ["aletta_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"aletta":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "aletta_give_valentine",
        "label": ["aletta_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"aletta":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "aletta_kiss_me",
        "label": ["aletta_kiss_me"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"aletta":{"min_love":150,"present":True, "valid":True}},
        "game_conditions":{"flag_female":0, "chances":20},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name":"aletta_preg_talk",
        "label": ["aletta_preg_talk"],
        "duration": 0,
        "do_once": False,
        "girls_conditions": {"aletta":{"flagmin_pregnant":6,"flag_pregtalk":0, "active":True}},
        "game_conditions": {"activity":"interact"}
        })

    Event(**{
        "name": "aletta_pregnant_flag",
        "label": ["aletta_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"aletta":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

label aletta_pregnant_flag:
    $ aletta.set_flag("pregnant",1,mod="+")
    return

label aletta_preg_talk:
    $ aletta.set_flag("pregtalk",1)
    show aletta
    aletta.say "[hero.name], are you okay?"
    aletta.say "Seriously, you look terrible!"
    "Great start - aren't I supposed to be the solid rock of a guy, supporting Aletta through whatever's troubling her?"
    "I need to snap out of it and stop being such a pathetic mess!"
    hero.say "It's okay, Aletta...I'm...I'm just worried about you, that's all."
    hero.say "Worried about why you wanted to meet me at such short notice, you know?"
    "Aletta looks at me sideways, as though she's not quite convinced by my explanation."
    "But she nods nevertheless, hinting that what she wants to discuss is more important than her doubts about my sincerity."
    aletta.say "Well, yes...what I have to tell you is quite important - and it does have to do with you specifically."
    "She pauses, and I nod emphatically, not even able to allow her a momentary pause in her delivery."
    hero.say "And that would be...what, exactly?"
    aletta.say "I'm pregnant, [hero.name]."
    "There it is, a bald and frank statement of the basic facts."
    "Trust Aletta not to beat around the bush or waste time gilding the lily."
    hero.say "You're...pregnant?"
    "Aletta raises her eyebrows at the question and my incredulous tone."
    aletta.say "Yes, is that not what I just said?"
    hero.say "Yeah...yeah, I heard you, Aletta."
    hero.say "It's just a bit of a shock, you know...a lot to take in all at once?"
    "Aletta shrugs dismissively at my confusion."
    aletta.say "I really don't see how it's that much of a surprise."
    aletta.say "We did it without protection more than once, and the chances are we were going to get caught out eventually."
    aletta.say "The question you should be asking yourself isn't if you can get your head around it, as you really don't have a choice in the matter."
    aletta.say "I'm pregnant, and that's all there is to it."
    aletta.say "What we need to be thinking about is what we're going to do about it."
    "Typical Aletta, straight to the point and with no time for sentimentality."
    if aletta.get_status() == "fiance":
        aletta.say "In any other circumstances, I would have been one hundred percent in favour of having a termination."
        aletta.say "But you've already asked me to marry you, [hero.name] - and that changes everything."
        aletta.say "It means that we have a real chance to start a family together, build something meaningful - something bigger than the pair of us."
        "I've never heard Aletta talk like this before, as though all of her blunt force was being transformed into a genuine passion for making a future together."
        "I have to admit, it's more than a little scary!"
        menu:
            "Agree":
                "But when I actually start to think about the implications of what Aletta's suggesting, I find a lot of that fear oddly begins to fall away."
                "What am I really afraid of, commitment and spending my life with her and our child?"
                "I've been spending most of my time with her as things are, and I rushed here for fear of something being wrong."
                hero.say "You're right, Aletta - we should grab hold of this and make all that we can out of it."
                hero.say "Plus, I think we'd make pretty great parents, don't you?"
                show aletta happy
                "Aletta raises a quizzical eyebrow at this last statement, but she's already wearing a genuine smile that she just cant suppress."
                aletta.say "Well, that has yet to be seen..."
                aletta.say "But I have to admit, it'll be fun to find out!"
            "Disagree":
                $ aletta.love -= 20
                hero.say "Wow, that's one hell of a big step, Aletta..."
                hero.say "In fact, it's more of a leap than a step, one that you don't know where you're going to land!"
                "I let out a breath of frustration as I try to find the words to express myself without coming across as an irresponsible jerk."
                "And from the look growing on Aletta's face, I can tell that I'm not succeeding."
                show aletta angry
                aletta.say "Hmm...I'm beginning to think that I've misjudged you, [hero.name]."
                aletta.say "I thought that you were growing into a more mature and responsible character."
                aletta.say "One upon which I could firmly rely to provide the stability I would need to begin a new chapter in my life."
                aletta.say "I can see now that I was wrong!"
                aletta.say "In fact, I need to think again about our entire relationship."
    else:
        aletta.say "I'll be honest with you, [hero.name] - my preferred solution is to have a termination before that's not an option."
        "I feel as though I've been hit with a right hand blow and then caught with the left on the way back."
        "Just when I thought that I was getting used to Aletta's forthright way of dealing with matters too."
        "Somehow it's so much harder to deal with when she's talking about a thing that's so personal to me."
        "Do I want to keep the baby or not?"
        "I suppose that I honestly don't know..."
        menu:
            "Tell her not to do it":
                hero.say "But I'm the father, so I get a say in this, right?"
                "Aletta nods, but not with the kind of expression on her face that says she's looking forward to hearing my input."
                aletta.say "Yes, [hero.name], of course you do."
                aletta.say "Why else would I have told you all this, and not just had the termination if you didn't?"
                hero.say "Well...maybe I think that the best thing would be for us to keep the baby."
                hero.say "What do you say to that?"
                "Aletta looks at me sideways, as if weighing up the whole situation."
                aletta.say "Hmm...I'm not totally convinced that you're up to the task, [hero.name]."
                hero.say "I know, I know - but don't worry, I'm one hundred percent committed to proving it to you!"
                aletta.say "Well, let's not be hasty - we have a small window of opportunity before a decision has to be made."
                aletta.say "But I have to say that you're going to have to do a lot to convince me!"
            "Agree":
                hero.say "I think you're probably right, Aletta."
                hero.say "I'm not ready to be a parent, and it doesn't sound like you are either."
                "I can't say that Aletta looks happy at this statement, or even relieved to have me agree with her."
                "At the best I can only say that she seems oddly sad and yet resigned to they way things have turned out."
                aletta.say "Well, if that's all that you've got to say..."
                aletta.say "I'll call the clinic in the next day or so and make the arrangements."
                hero.say "Aletta...I'll stump up for my share of the bill."
                show aletta sad
                "Aletta smiles a little sadly at that, nodding so slightly that it's almost impossible to notice."
                aletta.say "Okay...that's decided then..."
                $ aletta.set_flag("pregnant", 0)
                $ aletta.set_flag("pregtalk",0)
    "With that, we both go our separate ways, and I'm sure Aletta's thoughts are racing as much as mine."
    "But I think that, under the circumstances, we've made the best decision for everyone involved."
    return

label aletta_event_05b:
    $ aletta_love_max = 200
    "I was a little curious when Aletta called me up, pretty much out of the blue and said she wanted to come over and see me."
    "But we'd had what I thought was a pretty successful date (if you could call it that) at the shooting range."
    "And after that, I was keen to see more of her as soon as the chance arose - so I instantly said yes."
    "It was only a few seconds before she hung up that she dropped into the conversation the fact that she also wanted to 'talk to me' about something."
    "Now to a girl, those are nothing more than words making up a casual statement."
    "But to a guy, they're almost always enough to send chills up your spine."
    "What in the hell could she possibly want to talk about?"
    "We're not at the stage in our relationship that we need to be talking about things yet, surely?"
    "We've only been out on sort-of dates a couple of times - so is it even properly a relationship yet?"
    "The only logical conclusion is that she's got cold feet and wants to call it all off."
    "And she's coming round to tell me how 'it's not you, it's me'!"
    "But then I actually manage to sit down and tell myself I'm being stupid, jumping to wild conclusions."
    "Best to just wait for her to turn up and hear what she has to say."
    "When the doorbell rings, I try not to leap up and run to answer it."
    "Instead I walk as calmly as I can manage into the hallway and open it with what I hope is a smile on my face."
    scene bg house
    show aletta suit hairdown
    aletta.say "Hello, [hero.name], I came over as soon as I could."
    hero.say "Hey, Aletta..."
    "No sign of anything on her face to say she's not telling the truth."
    aletta.say "Well..."
    hero.say "Well what?"
    aletta.say "I was presuming that you were actually going to invite me in?"
    hero.say "Oh, yeah...of course...come on in!"
    show bg livingroom
    "I step aside to let her into the hallway, only noticing at that moment that she's carrying what looks like an overnight bag in one hand."
    "What's that about - is she planning on asking to stay over?"
    "I close the door, but before I can ask about the bag, Aletta steps forward and wraps her arms around me tightly."
    "She kisses me without asking, passionately and quickly adding her tongue as soon as I return the gesture."
    "Well, that certainly took my mind off of the idea of her coming over just to dump me!"
    "When the kiss is over, she smiles slyly at me."
    aletta.say "You remember when we went to the shooting range?"
    "I nod slowly, wondering where this is going."
    if "shooting" in hero.skills:
        aletta.say "And how you kept it a secret that you're actually a pretty good shot?"
        "'Pretty good shot' - I seem to remember beating Aletta's score that day!"
    else:
        aletta.say "And maybe needing more practice."
    "I nod again."
    aletta.say "Well - I wondered if you fancied a rematch?"
    hero.say "You mean you want to go back to the shooting range again?"
    "Aletta shakes her head and holds up the bag she's brought with her."
    aletta.say "No, [hero.name] - I brought my gun with me."
    aletta.say "You have woods out back, right?"
    aletta.say "I thought we could go out there and maybe shoot some cans."
    aletta.say "Loser buys dinner - what do you think?"
    "It's not what I was expecting, but it's a far better prospect than what I'd imagined."
    hero.say "Sure - why not?"
    show bg pool
    "We walk out of the back door, past the pool (which I note Aletta seems surprised by), and out of the back gate."
    show bg black
    "The woods start a couple of feet from the property line."
    "And I figure that if we go far enough into them, the combination of distance and a major road on the other side should be enough to keep the sounds from alarming the neighbours."
    "We chat as we walk, not really talking about much that would interest anyone else."
    "The only stops we make are to collect maybe half-a-dozen empty cans along the way."
    "We stop when we come across a wall we can use, made out of brick and a little over waist height."
    "I have no idea what it once was or what it was supposed to mark out, but it's just about perfect."
    hero.say "Seeing as how this was your idea, how about you set up the cans how you'd like them?"
    "Aletta nods and smiles, accepting the cans."
    "She arranges them in two groups of three, each group three feet apart and each individual can maybe one foot from the next."
    "That done, she walks over to her bag and unzips it."
    "Aletta reaches inside and pulls out a handgun, matt black and impressive enough to appear in a slick action movie."
    "She smiles at the look on my face, clearly thinking that I'm impressed."
    "But right now, intimidated would probably be closer to the actual truth."
    "She proceeds to drop out and catch the ammo clip, slide the chamber back and basically do all that neat stuff people do in films to show they're a wizard with a gun."
    aletta.say "This is a Gnock 18 semi-automatic pistol and it fires a nine millimetre parabellum round."
    aletta.say "So I don't need to tell you to treat it with respect, right?"
    "Everything she just said basically boiled down to 'this is a big, scary gun that fires bullets that'll kill you, stone dead'."
    "But I nod all the same, still well aware of the dangers posed by a gun."
    aletta.say "You ready?"
    hero.say "As I'll ever be, I guess!"
    "Aletta turns the gun around in her hand so that she's holding it by the barrel and I'm taking it by the grip."
    "Shit, this girl really takes her firearms safety seriously!"
    hide aletta
    show aletta shooting mike forest
    "Once I have the gun in my hands, the weight of it somehow makes this whole thing seem suddenly real."
    "We're not joking around and talking about this any more - we're actually doing it!"
    "Was I right about the distance and the sound of the road covering the shots?"
    "What if someone comes walking through the woods and gets shot by a stray bullet?"
    "Fuck - what if I shoot myself in the goddamn foot?"
    "Breathe, just breathe and keep calm!"
    "I've shot a gun before, and this is no different to those times."
    aletta.say "You okay?"
    hero.say "Sure, sure...I'm fine."
    hero.say "It's just...new gun, you know?"
    aletta.say "Okay...but there was just one more thing."
    aletta.say "I'd thought of it as a forfeit, to make it a little harder for you to shoot straight."
    aletta.say "But if you're nervous, then maybe it'll actually help to calm you..."
    "With that enigmatic last line, she kneels down slowly in front of me."
    "And then she starts to unzip my pants, while she smiles up at me slyly."
    "Bloody hell - she's really going to give me a blow-job while I'm supposed to be shooting this thing!"
    if not "shooting" in hero.skills or not hero.fitness >= 50:
        "Aletta doesn't find me very aroused when she first pulls my dick out."
        "But under the circumstances, can you blame me?!?"
        "Not that it discourages her to any great degree though."
        show aletta shooting mike forest bj lick
        "I try to tear my eyes away as she begins to stroke the shaft of my dick with her fingers, occasionally bringing it to her lips and kissing the tip."
        "I look down the barrel of the gun, amazed to see just how much it's shaking."
        "The one thing that I know for sure is that I'm not exactly shrinking from the situation - if you understand what I mean?"
        "Maybe it's the danger of doing something this risque and dangerous out in the open like this."
        "Maybe I'm having a perverse burst of excitement from handling a powerful gun in such a reckless manner."
        "Or just maybe Aletta's that damn good with her fingers and lips that I can't help stirring at her attentions."
        "She certainly looks good as I risk a glance down at her."
        "I'm semi-erect by now, and well on my way to being fully standing to attention."
        show aletta shooting mike forest bj suck
        "Aletta looks up at me as she slips her lips around my cock."
        "Her big, blue eyes are full of mischief and her lipstick glistens in the afternoon sunlight."
        show aletta shooting mike forest bj suck fire
        "Without thinking, I squeeze the trigger, sending a shot flying crazily wide of the mark."
        "While I jerk at the deafening sound, somehow Aletta manages to remain still."
        hide aletta
        show aletta shooting mike forest bj suck
        "Even the exaggerated motion of my dick she takes completely in her stride, widening her eyes in mock surprise as I push deeper into her open mouth."
        "From there, it's almost impossible for me to pay more attention to shooting straight than to what Aletta's doing to me."
        "Call me a pussy for not being able to concentrate on the gun if you like."
        "But I'm not ashamed to say that I was far more interested in the sensational things that I discovered Aletta could pull off with her tongue that afternoon."
        "I can't recall just how many bullets there were in the magazine."
        show aletta shooting mike forest bj suck fire
        "Only that I most of them randomly into the woods, completely missing the targets."
        "I might have grazed one of Aletta's cans, and I know I fired at least one shot almost straight up into the air."
        "Part of me expected that one to hit a passing bird, just to add to the insanity of what was happening to me right there and then."
        hide aletta
        show aletta shooting mike forest bj suck mouth
        "About the only thing that I did manage to shoot on target, was when I finally came into Aletta's mouth."
        "She smiled as she released me and swallowed without pause of hesitation, knowing full well what she had managed to make me do."
    else:
        "It's weird, but there's just something empowering about the thought of Aletta giving me oral while I'm shooting a big, macho handgun."
        "Maybe it's tapping into the primitive parts of my brain, but I suddenly feel incredibly aroused by what's going on."
        "The biggest side effect of this is that, by the time Aletta gets my dick out of my pants, I'm already almost fully erect."
        "She smiles at the sight of it, chuckling to herself."
        show aletta shooting mike forest bj lick
        "It doesn't take long for Aletta to have me standing fully to attention, as she strokes and caresses the shaft."
        "I take aim for the first can almost the same moment that she begins to lick tentatively at the tip of my dick."
        show aletta shooting mike forest bj suck
        "Her lips close around the head as I squeeze the trigger."
        show aletta shooting mike forest bj suck fire
        "In the confusion of the resulting crack of gunfire, Aletta takes me deeper into her mouth."
        "Bullseye - the first can is nowhere to be seen, blown clean off of the wall."
        hide aletta
        show aletta shooting mike forest bj suck
        "Aletta's pace quickens now, and I can feel the sensation of her full lips travelling up and down, her tongue working away at me."
        show aletta shooting mike forest bj suck fire
        "The second shot comes as if carried on this feeling, as easy as me simply walking up and pushing it over with a finger."
        hide aletta
        show aletta shooting mike forest bj suck
        "Two cans down, one to go."
        "Aletta's working on me like a machine by now, her head bobbing back and forth."
        "I look down at her for a moment, and I almost forget about taking my last shot."
        "She has her eyes closed and an almost peaceful look in them."
        "The sunlight is coming down, dappled by the leaves and branches overhead."
        "She looks amazing, mottled in the shadows and shade."
        "I feel like I could lose myself, right here and now, just looking at her."
        "But I resolve to take a shot at my last can before she makes me cum."
        "I have the shot all lined up just as I realise how close she's actually brought me."
        "Trying to breathe evenly, I begin to squeeze the trigger for one last shot."
        hide aletta
        show aletta shooting mike forest bj lick fire
        "And almost at the same moment that the gun fires, Aletta sends me over the edge."
        show aletta shooting mike forest bj lick fire facial
        "As I cum, the gun is thrown around in my hand, and it's all I can do to keep from firing off the remaining bullets in the clip."
        "Aletta makes sure that she finishes the job neatly, licking me clean afterwards."
        "When she's done, I risk a glance at the wall."
        "Three shots and three hits."
        "I wonder if that's more to do with my skills or Aletta's."
    hide aletta
    show aletta suit
    "Aletta looks over my shoulder at the wall, smiling like a cat at the evidence of my performance."
    "She seems inordinately pleased with the effect her attentions seemed to have upon me."
    aletta.say "My turn!"
    "She takes the gun from me and replaces the clip, ensuring that she has a full load."
    show aletta shooting
    "And then she takes up a firing stance, looking at me with raised eyebrows."
    "It's then that I realise she's waiting for something."
    "Specifically, she's waiting to see if I'll reciprocate while she's shooting!"
    menu:
        "Don't":
            "What does she think this is, an exhibitionist's stroll in the woods?"
            "Sure, I'm bowled over that Aletta would give me a blow-job out here."
            "But it's not like I asked her to do it!"
            "Plus, it's not like she needs the help to clear her mind or anything."
            "Aletta's already a great shot!"
            hero.say "What are you waiting for?"
            hero.say "Fire away!"
            $ aletta.love -= 5
            "Aletta looks puzzled for a moment, and then she realises that I'm not about to give her oral any time soon."
            "Irritation and annoyance cross her face."
            "But then she buries those emotions under the veil of pretending not to give a shit."
            "A part of me thinks that it's high time I took some control back in this relationship."
            "What with guns, leathers and motorbikes, I sometimes feel like Aletta's the one constantly in the driving seat."
            show aletta shooting fire
            "With a cold efficiency that I suppose has to come mainly from my own actions, she reels off three shots in short order."
            "One after another, all three of her cans spin off into the trees as she hits them each in turn."
            hide aletta
            show aletta shooting
            "I clap and smile as she turns to regard he, more than a little haughtily."
            "While I might have refused to give her oral just now, my praise genuine."
            $ aletta.sub += 5
            "And I think Aletta can sense that, as she raises one eyebrow and returns a sliver of a smile."
            "If I'm right, and I sincerely hope that I am, I might actually have succeeded in making her respect me."
            "Maybe just a little."
        "Do it" if hero.fitness >= 50:
            "Well, fair's fair, I suppose!"
            "And really, is it that much of a chore to play with a girl the likes of Aletta?"
            "There are guys that'd kill for the chance to do just that!"
            "I nod eagerly, walking round behind her and open her flies."
            show aletta shooting finger open
            "In a moment, I have her suit open and pull them halfway down her thighs."


            "For all of her outward confidence, I can already feel her pussy almost quivering at my touch."
            show aletta shooting finger open fire
            "I probe the length of her pussy with one finger, and then hear the crack of the gun firing."
            hide aletta
            show aletta shooting finger open
            "A glance over her shoulder reveals that Aletta never even turned her head as she pulled the trigger, sending the shot way off target."
            "Realising what she's done, she shakes her head and tries to concentrate on the task at hand."
            "And now I see that I have a challenge too!"
            hide aletta
            show aletta shooting finger open juice
            "Using my fingers to stroke lower between Aletta's lips, I slip my free hand under her top and begin to massage her breasts."
            show aletta shooting finger open fire
            "She actually moans a little at that, but then steels herself and fires off a shot that I hear connect."
            hide aletta
            show aletta shooting finger open
            "My only answer is to take hold of one of her nipples and pinch it, beginning to push my fingers in deeper still into her pussy."
            show aletta shooting finger open juice fire
            "Aletta tries to get off another shot before the effects take hold."
            hide aletta
            show aletta shooting finger open juice cum
            "But all too soon she's almost crying at what I'm doing to her pussy and breasts."
            "The fingers playing with her breasts are slick from her sweat, and those in her clit are already wrinkling from how wet she's become."
            show aletta shooting finger open juice cum fire
            "I almost forget the sound of the shots that she's firing, not really caring any longer who wins the shooting contest."
            show aletta shooting finger open juice cum
            "In the end, I vaguely hear the sound of Aletta dropping the gun onto the ground, before clasping her hands around my neck."
            show aletta shooting finger open juice cumhard
            "I still have my fingers deep in her pussy when she finally cums, and I feel every twitch and flex of her muscles as she does so."
            "Afterwards, I see one can missing, one on its side and another completely untouched."
            "A result of which I feel I can be quite proud."
            $ aletta.love += 5
    hide aletta
    show aletta suit
    "Aletta packs the gun away in her bag, and links my arm as we walk back to the house together."
    "I'm not sure that I'll ever be fully comfortable combining guns and girls like this."
    "But for her, it was well worth the effort."
    return

label aletta_event_04b:
    "After a week full of work and household politics, my Saturdays are usually when I officially turn off my brain and try to recuperate."
    "If I'm lucky, I can sometimes even manage to get away with not setting foot out of bed until some time in the afternoon."
    "To this end, I always leave my phone set to vibrate and on top of something soft, just to make sure I'm not disturbed."
    "The only possibility is opening my eyes for a moment and actually seeing that there's someone calling I can't resist talking to."
    "Which is what's happening right now."
    "I glance blearily at the phone, trying to make out who's calling at this time on a Saturday morning."
    "'Aletta' - almost as soon as I read the name, I'm already scrambling for the phone."
    "I fall out of the bed grabbing for it, and accept the call whilst laid on the floor in a heap of bedclothes."
    "Call me desperate, if you like."
    "But I'm not swimming in offers to the point where I can ignore a call from a girl the likes of Aletta."
    hero.say "Hey there...Aletta - what's up?"
    aletta.say "Hey, [hero.name] - I thought you weren't going to pick up for a minute there!"
    hero.say "I was struggling to get to my phone."
    hero.say "You know how it is on a weekend, right?"
    aletta.say "Oh, tell me about it!"
    aletta.say "I've been up since before six so that I could get to the gym and then hit the classes that I take on a Saturday morning."
    aletta.say "The weekend is supposed to be time to relax, but I always seem to end up doing more than I would have at work!"
    "Oh great - the girl can even make me feel inadequate over the phone, and without try very hard too!"
    aletta.say "That's what I was calling about, actually."
    hero.say "What - you want me to work this weekend?"
    hero.say "It's kinda short notice..."
    aletta.say "No, no - nothing like that!"
    aletta.say "I meant that I managed to get some free time this afternoon."
    aletta.say "And I wondered if you wanted to come do something with me?"
    aletta.say "Something fun?"
    "Already my mind is conjuring all manner of 'fun' things that could be done with Aletta's help..."
    hero.say "What did you have in mind?"
    aletta.say "Well, I like to get some practice in down at the firing range every few weeks."
    aletta.say "I thought it'd be a laugh if we went along and squeezed off a few rounds together."
    aletta.say "What do you think?"
    menu:
        "Refuse":
            "The firing range?"
            "What does she think I am - some kind of gun-toting loon?"
            "Come to think of it, who invites someone on a date to go shoot off a shit-load of guns?"
            "Is she a gun-toting loon herself?"
            hero.say "Ahh...that sounds like a great idea, Aletta."
            hero.say "But I'm gonna have to take a rain-check...sorry."
            aletta.say "Oh...okay, I guess."
            aletta.say "Do you mind if I ask why?"
            "Here we go - better think up a good excuse, and fast."
            hero.say "Well...you know how we were talking about how much work we had on this week in the office?"
            aletta.say "Yeah...sort of..."
            hero.say "I brought a pile home with me to get through before Monday morning, and I just remembered about it."
            "There's a pause before she replies."
            aletta.say "You brought that much work home and still managed to forget about it all?"
            hero.say "Weird, I know!"
            hero.say "But I think it must have been the thought of getting to sack it all off and spend the rest of the day with you."
            hero.say "That probably would have been enough to make me forget about almost anything else!"
            "I wait for a moment, hoping that she buys it."
            "There's a muffled gasp and then a pretty genuine sounding giggle from the other end of the line."
            aletta.say "Well, if I have to be stood up, then at least it's nice to get a compliment like that at the same time."
            aletta.say "I'll call you some other time - don't work too hard now!"
            hero.say "Looking forward to it already!"
            "I think I might actually have pulled it off!"
            return
        "Accept":
            $ aletta.set_flag("sidestory",2)
            hero.say "The firing range...sure, why not."
            aletta.say "Great - I'll swing by on the bike and pick you up in about an hour, okay?"
            hero.say "I'll be ready."
            show bg black with fade
            $ game.pass_time(1)
            "I put down the phone and hurry to get showered and ready for Aletta's arrival."
            scene bg house
            show aletta suit helmet
            "By the time she roars to a halt outside the house, I'm already standing by the kerb, waiting for her."
            "No one could know that I was slobbing in bed until so recently."
            "Aletta flips up the visor of her helmet and tosses me the spare."
            aletta.say "Jump on - you know the drill, right?"
            "I nod and do as I'm told, trying not to make it so obvious that I'm eager as hell to press myself tightly against Aletta on the bike."
            hide aletta
            show aletta ride mike
            "The ride there is swift, thrilling and over way too soon."
            show bg black
            "We dismount and Aletta leads the way inside."
            "The staff on duty seem to be pretty familiar with her, offering greetings and even a few little jokes."
            "But I don't have even have time to get jealous, as she ushers me into the range and we prepare to shoot."
            "The place is pretty much like what you see on any cop show paper targets on the opposite wall in a long room, with booths for the shooters to stand in."
            "Ear and eye protectors are provided, and I hear Aletta say something about the handguns we're going to be shooting that gets lost in the constant din of the place."
            show aletta shooting
            "She goes first, and even before she's let off a single shot, I can tell from her stance that she's pretty damn serious about this thing."
            show aletta shooting fire
            "I watch as Aletta puts one bullet after another into her target."
            "Sure, not all of them are kill-shots, but she's accurate enough to make the prospect of her shooting at you a pretty scary one."
            "Still wearing the ear protectors, she waves for me to take my shots."
            show aletta shooting mike
            "First I take a deep breath, and then step up to shoot."
            if "shooting" in hero.skills:
                "I don't know if my stance is as good as Aletta's, but it's always served me well enough."
                show aletta shooting mike fire
                "I shoot until the magazine is empty."
                "Not a crazy flurry of shots or a torturous series of quivering ones."
                "All of them are, more or less, on target."
                "Looking at it again, I think I even did a little better than Aletta herself."
                $ aletta.love += 5
                $ aletta.sub += 5
                "She certainly looks impressed enough with my performance."
                "What can I say?"
                "Just because I don't own a mountain of guns or want to start a militia in the backyard, that doesn't mean I can't be a good shot."
                "Not all people who can shoot are fanatics or spend the whole time bragging about it either."
                scene bg street
                show aletta suit
                "Outside of the range, I try to look surprised at Aletta's evidently growing admiration for my marksmanship."
                aletta.say "Someone's certainly a dark horse!"
                hero.say "I'd prefer to call it not blowing my own trumpet."
                aletta.say "It's nice to know that you actually have a trumpet!"
                hero.say "Ah, well...what kind of a jerk would I have been if I bragged about it the moment you said you wanted to go shooting with me?"
                "Aletta goes quiet for a moment, just nodding in silence, as if she were lost in thought."
                "From the reaction my being humble stirred in her, I begin to wonder if she's mentally comparing me with Dwayne."
                "Now ther is a guy that never had a single problem shouting his talents from the rooftops."
                hero.say "Are you okay, Aletta?"
                aletta.say "Oh, yeah...I'm fine."
                aletta.say "I was just thinking that it might be fun to find out what else you've been hiding from me!"
                "I laugh at the comment, like I'm supposed to."
                "But I'm already thinking that it might be fun to let her."
            else:
                "It's all I can do to keep the pistol from visibly shaking in my hand as I try to aim it at the target."
                show aletta shooting mike fire
                "All of the advice Aletta tried to give me before we started went straight over my head."
                "Just like most of my shots do to the human shape described on the target I'm supposed to be aiming for."
                "I lose all track of the number of bullets that there should be left in the magazine as I reel of one lousy shot after another."
                "Soon the bullets run out, and I realise that I'm just pulling the trigger to no effect."
                hide aletta
                "Sheepishly, I put the gun down and turn to face Aletta."
                "No one else is shooting now, so it's safe for us both to remove our ear protectors."
                show aletta suit
                $ aletta.sub -= 20
                hero.say "Sorry...I guess...I guess I just embarrassed you pretty badly, huh?"
                aletta.say "Don't be silly - there's no shame in being a bad shot, just in not wanting to get better."
                aletta.say "[hero.name], why didn't you just say if you weren't into this kind of thing?"
                hero.say "It's that obvious?"
                aletta.say "Well, let's just say that if the aim were to keep from hitting the target at all - you'd be a natural."
                hero.say "Like I already said...I'm sorry."
                hero.say "I just thought that if I said I wasn't into guns, then you'd think less of me."
                hero.say "It was a chance to spend some more time with you, too..."
                "Aletta smiles at the admission, and I begin to see that I was wrong to imagine her looking down on me for those reasons."
                "I think she's genuinely touched at the idea of me wanting to see her that much."
                "And maybe also finding my honesty more than a little endearing too."
                aletta.say "I could always teach you...if you'd like?"
                "It doesn't take much for me to agree, and while she gives me some more verbal pointers, she can't talk me through the actual shooting."
                "Of course, this means that she has to get in real close to ensure the lessons sink in when I try to shoot again."
                "Some guys might feel a little emasculated to have a woman bracing them and showing them how to fire a gun like this."
                "But I'm very happy to feel Aletta pressed against me, arms almost wrapped around me and the warmth of her breath against my cheek."
                "It gets even better when I actually squeeze the trigger and the force of the shot travels through my body and into hers."
                "By the time we've polished off an entire clip, she's practically wrapped herself around me."
                "I choose to read a lot into the fact that Aletta is not quick to release that hold she has on me."
                "And the way she lingers close afterwards is very pleasant as well."
                "As we leave, I can't help thinking how weird it is that I seem to have made such an impression on Aletta by kind of being weak where she's strong."
    $ game.pass_time(6)
    return

label aletta_event_03b:
    scene bg street
    "There I am, just strolling along, maybe gazing into a couple of shop windows on the way."
    "When I suddenly hear the distinctive sound of a high-powered motorbike approaching at some speed."
    "I look up and around, not because I'm particularly impressed by that kind of thing, but more because it's the natural human reaction."
    "The bike is one of those Japanese types, the ones that look like they should be being ridden on some big racetrack in front of a load of cheering fans."
    "It's black and has streamlined bodywork that makes me wonder if even a radar could pick the thing up when it's speeding along."
    "But then I see the rider for the first time, and she looks like she could have been made to fit the bike, rather than the other way round."
    "Her black helmet and matching black leathers render her completely anonymous."
    "And yet the bodysuit is so fitted and tight that it leaves little to the imagination when it comes to her statuesque figure."
    "The female rider is tall, curvy and sits on the bike like some kind of warrior queen riding her steed into battle."
    "It's then that I realise I've been able to see so much only because she was in the act of slowing down and coming to a stop at the kerbside a couple of metres away."
    "I realise as well that I must have literally stopped in my tracks the very moment that I first laid eyes on her too."
    "As the rider uses her booted foot to put down the kickstand and turns the bike off, I try to look casual and turn away slowly, hoping that she hasn't seen me openly ogling her in the street."
    show aletta suit helmet
    aletta.say "Hey, [hero.name]...where are you going in such a hurry?"
    "I recognise Aletta's voice instantly and turn back around, assuming that she must have walked up behind me in the street."
    "This could be awkward."
    "I'm not about to openly blank Aletta, but I don't want the biking amazon to see me either."
    "Though when I do turn around, I'm amazed to see that they're actually one and the same person."
    "Oh yes, the leather goddess on the bike is none other than Aletta!"
    "The moment that I turn round to see this, the sun just so happens to be behind her."
    hide aletta
    show aletta suit hairdown
    "And she just so happens to be in the act of taking off her helmet and shaking out her thick, brown hair."
    "Framed by the light of the sun, I swear that I see the whole thing in slow motion..."
    "...maybe even with classical music playing in the background too."
    hero.say "I..."
    aletta.say "I said, where are you going, [hero.name]!"
    "I shake my head and try to pull myself back together."
    "It was bad enough just having to work with that body."
    "Now I have to deal with the memory of it in tight, form-fitting black leather too!"
    hero.say "Uh...sorry, Aletta - I guess I was just in a world of my own."
    "She smiles and shakes her head at my state of distraction."
    aletta.say "Well, work has been pretty crazy this last week or so."
    aletta.say "It's at times like this that I always feel the need to bust this baby out and go for a long ride."
    aletta.say "Really helps to clear the cobwebs, I can tell you."
    hero.say "Huh...I didn't recognise you until you took your helmet off just now."
    "She gives me an odd, sideways look."
    "As if she's almost disappointed that I didn't recognise her simply from the shape of her body."
    "But if that is the case, she soon hides it."
    hero.say "I had no idea you were into motorbikes."
    hero.say "At least I've never seen you on one before...and you never talked about them at work either."
    "Aletta smiles at me, clearly pleased to have been able to surprise me and maintain an air of mystery at the same time."
    aletta.say "Oh yeah, [hero.name], I love to ride."
    aletta.say "I just love the feeling of the bike, throbbing away beneath me..."
    aletta.say "Eating up the open road..."
    "Aletta grips the handlebars of the bike while she's telling me all of this, simulating the posture that she no doubt adopts when riding."
    "But all the time she does so, I'm wondering if she realises how she's straddling the bike in a REALLY suggestive manner."
    "She's almost throwing her head about as she acts out turning the thing, and I can't help thinking that she's actually imaging something else altogether being ridden rather passionately..."
    aletta.say "Anyway...I can't sit around here all day chatting."
    aletta.say "I need to get away before I get a ticket."
    "She pauses in a thoughtful manner, so well rehearsed that I suspect it was far from spontaneous."
    aletta.say "Say...would you like a ride home?"

    aletta.say "You'd be on your doorstep before you knew it."
    aletta.say "Especially with the way I ride!"
    "Right now, I can believe her!"
    menu:
        "No thanks":
            $ aletta.love -= 5
            hero.say "Ah...thanks for the offer, Aletta."
            hero.say "But I kinda walk home sometimes for the same reason you just said you ride that bike!"
            "I'm rubbing the back of my neck even as I say this, aware of just how lame it sounds."
            "Aletta looks genuinely surprised at my refusing her offer."
            "And with the way she looks on that bike and in those leathers - who can blame her?"
            "But then she nods and shrugs her shoulders, seeming to accept my explanation."
            aletta.say "Huh...I guess that makes sense, [hero.name]."
            aletta.say "We've all got our own ways of handling the daily grind."
            aletta.say "Far be it from me to screw up yours with mine!"
            "I smile weakly, relieved to have been let off the hook."
            "But I can see a look of disappointment in Aletta's eyes, no matter how hard she tries to hide it."
            "And now I feel guilty for turning her down when she was clearly looking forward to showing off her bike and giving me a ride."
            "We exchange a few more awkward pleasantries before she puts her helmet back on and gives me one final wave."
            "As she speeds off into the distance, I can't help wondering if I made the right decision."
        "Sure":
            $ aletta.set_flag("sidestory",1)
            hero.say "Sure, Aletta - I'd love to hitch a ride home with you!"
            "My almost too eager response elicits a sly, knowing smile from Aletta."
            "I'm sure she's fully aware of just how much she's managed to reel me in with all of this biker chick stuff."

            "There might be a very real sexual undertone to what's going on here."
            "But Aletta offered me the chance to ride her bike - not to ride her."
            aletta.say "Just keep your feet up and make sure you hold onto me...tight."
            hero.say "Okay, okay...please don't go so fast that I fall off!"
            aletta.say "No promises, [hero.name] - so like I said, hold onto me real tight!"
            hide aletta
            show aletta ride mike
            "Aletta says all of this even as she's revving the bike and pulling away from the kerb."
            "I'm sure she's doing this on purpose, filling my head with the need to cling onto her and then adding acceleration as a motivator."
            "I've seen people doubled up on bikes many times in the past, and I try to copy their example."
            "But I still have to deal with the fact that I'm basically clinging onto Aletta for what feels like dear life."
            "Don't get me wrong - it's not that I don't WANT to cling onto Aletta under the right circumstances."
            "Though I fear that I'm going to end up paralysed and hanging off of her back like a priapic Yoda, still stuck in place even after the ride is over and done with."
            "I have my hands somewhere at the top of Aletta's thighs, trying to hold on well enough not to fall into traffic and yet not tight enough to make her think I'm already taking liberties."
            "She begins to speed up as soon as the first opportunity presents itself, weaving in and out of traffic with, what seems to me at least, increasing abandon."

            "So I have no choice other than to accept that my life is literally in her hands."
            "I try to distract myself by focussing on the sensations of being this close to Aletta."
            "I know I was going on about keeping this platonic and not getting sexual before now."
            "But I really need the distraction, and so let myself off the hook on this occasion."
            "What can I say about it that you've not already imagined?"
            "Aletta's body is pretty damn impressive through the clothes she wears to work."
            "But through supple leather, it's simply divine."
            "Her back an buttocks are quite possibly the most comfortable thing I've ever felt against my chest."
            "Not to mention lower down..."
            show aletta ride mike lboob
            "Before I realise what I'm doing, my hands are no longer just holding onto Aletta's thighs for fear of falling off."
            "I can't help moving them up and down, almost massaging her through the leathers as I do so."
            "The need to keep up my grip means that I'm not being in the least bit gentle, but rather kneading handfuls of her beneath the leggings of her bodysuit."
            "Aletta must be well aware of what I'm doing, but she makes no attempt to slap away my hands or pull the bike over."
            "Instead, I swear she actually begins to rev the bike's engine almost in time to my squeezing of her thighs."
            "She also starts to go faster and ride with more abandon than before."
            "Though now, where before this would have intimidated me, I can't help finding that the arousing element of the ride turns the speed into something I actually enjoy."
            "The thought that Aletta is piling on the speed in direct response to my massaging her thighs is an incredible turn-on."
            "It feels almost as though she and the bike are linked, as though they're one entity."
            show aletta ride mike lboob pussy
            "The more I stir Aletta, the more the bike revs its engine and builds its speed."
            "My head is suddenly full of crazy thoughts, like making love to her while we're in motion, or mounting her as if she were a bike herself."
            "Suddenly I wonder if she can feel my dick through those leathers?"
            show aletta ride mike lboob pussy happy
            "I can't exactly help having a raging erection right now, can I?"
            "I'm genuinely worried about cuming in my pants if this keeps up as well!"
            "But then I can feel the speed of the bike lessening."
            "I shake off the almost trance-like state into which I'd fallen on the back of the bike and look around me."
            hide aletta
            show aletta suit happy
            "We're pulling up at the end of my street, just a couple of metres from my front door."
            "I step off of the bike, almost shaking from the adrenaline still coursing through my veins."
            "Aletta flips up the visor of her helmet as I hand mine back to her."
            hero.say "Th..Thanks...Thanks for the lift...Aletta."
            "She smiles, and it's then that I know she can't have been ignorant of what even such a short ride with her has done to me."
            aletta.say "No problem, [hero.name] - it was my pleasure."
            hero.say "Well, I guess I'll see you at work tomorrow, yeah?"
            "Aletta nods and gives me a little wave."
            aletta.say "This was fun...we'll have to do it again some time, maybe?"
            "I nod, trying not to look either nervous or too turned on at the prospect."
            aletta.say "Yeah, I'd really love to let you have ride with me sometime soon..."
            "It's only when she's driven away from the kerb and I actually think about what she actually said, that I realise she never as much as mentioned the bike in relation to the proposed 'ride'."
    return

label aletta_kiss_me:
    call aletta_greet from _call_aletta_greet_5
    show aletta
    "Being around Aletta for any significant amount of time, you tend to get used to her imperious, no-nonsense attitude to most situations and subjects."
    "I'm sorry, but maybe I worded that in a way that makes you think there's an element of choice involved for anyone interacting with her."
    "Just to clarify, there isn't - you either toughen up and deal with it, or else she grinds you mercilessly beneath her high, pointed heel."
    "This is the exact reason why it takes me completely by surprise when she begins to lean in towards me, closing her eyes and opening her mouth."
    "Is she going to shout in my face, even head-butt me out of some unsaid grudge?"
    hide aletta
    show expression "aletta kiss "+aletta.get_clothes()
    "And then she kisses me - out of nowhere."
    "And it's just impossible to describe...but I'll try all the same."
    "Aletta kisses like she handles most human social interactions, with force and passion."
    "All of that unyielding bossiness and dominating behaviour suddenly begins to make sense to me."
    "As I feel the emotion and almost desperate need for release in the way she pushes her tongue between my lips, I realise that what Aletta desires is perfection."
    "She strives to be the best in whatever she does, and she asks the same of those around her too."
    "Now that our hands are all over each other, I finally understand how much of a challenge it is to earn her trust and be worthy of her affection."
    hide expression "aletta kiss "+aletta.get_clothes()
    "Aletta isn't cold or distant, she just places a high price on her emotions."
    "If you can pay that price, the rewards are every bit its equal in value."
    hide aletta
    return

label aletta_give:
    "She hands me box, an envelope."
    hero.say "Thanks."
    "I open it and there is $50 inside it."
    $ hero.money += 50
    aletta.say "Go buy whatever you want with it."
    return

label aletta_give_valentine:
    show aletta
    "Aletta walks confidently towards me."
    call aletta_greet from _call_aletta_greet_7
    show aletta blush
    aletta.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Aletta hands me a box of chocolates."
    hero.say "Thank you, Aletta."
    $ hero.gain_item(gift)
    hide aletta
    return

label aletta_give_birthday:
    show aletta
    "Aletta walks towards me."
    call aletta_greet from _call_aletta_greet_8
    show aletta happy
    aletta.say "Happy birthday [hero.name]!"
    call aletta_give from _call_aletta_give
    return

label aletta_give_christmas:
    show aletta
    "Aletta walks towards me."
    call aletta_greet from _call_aletta_greet_9
    show aletta happy
    aletta.say "Merry christmas [hero.name]."
    call aletta_give from _call_aletta_give_1
    return

label aletta_init:
    python:
        if "aletta" not in HIDDEN:
            HIDDEN.append("aletta")
        aletta.set_flag("nodate")
        aletta.set_flag("nokiss")
    return

label aletta_event_01:
    scene bg office
    $ aletta_love_max = 20
    $ aletta.set_flag("story",1)
    $ if "aletta" in HIDDEN: HIDDEN.remove("aletta")
    $ if "alettaoffice" in HIDDEN: HIDDEN.remove("alettaoffice")
    "I am ready to bang my head against my desk staring at the code on my computer."
    "This morning has been rather stressful so far at work."
    "I need to tell Aletta she needs to take this assignment over if it is this impossible."
    "I let out a sigh of relief when I see it is finally time for my break."
    "Without a second thought I get up and go to the break room."
    "I keep my eyes straight ahead not wanting to deal with anyone just yet."
    scene bg breakroom
    "Pushing open the door to the break room I almost don’t notice the cool breeze or the faint hint of cigarette smoke."
    show aletta
    "Distracted from my bad mood I look around the room and to my surprise find Aletta at the corner window smoking."
    "She doesn’t seem to notice me."
    menu:
        "Tell her it’s Forbidden":
            "I walk over to her.."
            hero.say "Smoking is forbidden inside the building."
            "She turns and raises an eyebrow at me. Apparently, she did know I was in there."
            aletta.say "You think I don’t know that?"
            "She blows smoke out of the side of her mouth out the window and I notice how her lipstick hasn’t smudged a bit."
            "How does she do that?"
            aletta.say "I’ve been working here long enough that they won’t fire me for sneaking a cigarette."
            "She flips ashes out the window."
            aletta.say "I’ve also been here long enough to not give a damn about the rules or if they fire me."
            aletta.say "Besides, I got friends in cooperate. They’d help me get back on or a new job if I wanted."
            $ aletta.love -= 1
        "Tell her it’s unhealthy":
            "Feeling like I should say something, but not brave enough to mention the rules..."
            hero.say "Do you know how unhealthy smoking is for you?"
            "Aletta turns a tired look on me, like she had heard this line more than she likes."
            aletta.say "I don’t do it for my health, I do it to relax."
            "She takes a puff and then blows the smoke out the window."
            aletta.say "Stress can kill you just as fast as cigarettes. And working here?"
            aletta.say "Maybe faster."
            "She flips her ashes out the window."
            aletta.say "So don’t lecture me about what’s good for me. I’ll be the judge of that."
            "I did see a way to argue that so I just shrug."
            $ aletta.love += 1
        "Ask if she has an extra":
            "I felt like trying my luck. If the boss is smoking in the break room, how could she seriously tell me I couldn’t?"
            hero.say "Do you have an extra smoke?"
            "She looks at me first in surprise and then with a smirk."
            "Placing her cigarette in her mouth she shakes another loose for me and holds it out."
            aletta.say "Need a light?"
            "I nod and she hands me her lighter as well."
            "After taking a puff I hand it back and pull up a chair so I can sit by the window as well."
            "It seems odd to be smoking with my boss, but somehow calming as well."
            $ aletta.sub += 1
        "Say nothing":
            "I decide it is best to say nothing, but Aletta see’s me before I can make my way to the frig and leave."
            "Blowing out smoke in annoyance she turns toward me."
            aletta.say "I suppose this is awkward."
            "I shrug, still not believing I am seeing my tight knit boss breaking one of the company rules."
            aletta.say "Relax, rules get broken every day and the world still spins."
            "She did have a point."
    "I realize there’s really no reason to rush."
    "I mean after all I was in no hurry to go back to my desk and Aletta didn’t seem bothered by me being there."
    "Getting my lunch and an extra coke out of the fridge for Aletta I walk back over to her window."
    "Seeing me set the coke down in front of her she gives a small smile."
    aletta.say "Thanks [hero.name]."
    hero.say "No problem."
    "I watch her manicured nails open the tab as her red lips hold her cigarette all the while she looks out the window at nothing in particular."
    "She then takes the cigarette out of her mouth, and takes a sip of her coke."
    "The break room is quiet except for the faint sound of traffic."
    "It’s the first calm I have felt all morning since coming to work."
    "As I eat I look to Aletta and see how tired she looks with her guard down."
    "I don’t think I have ever seen her with her guard down."
    hero.say "Rough morning?"
    "She gives a laugh but it doesn’t sound like any humor is in it."
    aletta.say "You don’t know the half of it."
    aletta.say "Three people late, two sick, deadlines that are now impossible to make and corporate is riding my ass like it’s somehow my fault?"
    "She shakes her head after making another puff."
    "She blows the smoke out of her very feminine lips."
    aletta.say "Let me hire decent people and maybe it wouldn’t happen..."
    "Suddenly she flashes a look..."
    aletta.say "That wasn’t directed at you- you’re a good worker [hero.name]."
    hero.say "Don’t worry, no offence taken."
    "She seems to relax again, going back to her cigarette."
    "I think this is the most human I have seen Aletta in the enter time I have known her."
    "I feel bad as I realize I never once thought about how much stress she must be under being the boss."
    "And only minutes ago I was annoyed at my desk job when I was only responsible for my own work, and could ask for help whenever I got stuck."
    "Aletta was responsible for dozens of us, and had no help."
    hero.say "You know, maybe if a few people got fired for 'not calling in' you could get a few new employees in."
    "Aletta seems confused but then what I am saying seems to dawn on her."
    aletta.say "Very true, [hero.name] I’ll have to go check the call logs after my break. Thanks for the reminder."
    hero.say "Anytime Boss,"
    "Standing up I gather my things to go back to work."
    "I decide I can figure out the code on my own if I try a little harder."
    hide aletta
    return

label aletta_event_02:
    scene bg office
    $ aletta_love_max = 40
    $ aletta.set_flag("story",2)
    "I lean back in my desk chair and stretch my arms over my head as I smile having just wrapped up a difficult assignment."
    "I feel rather accomplished for the day and it is not even noon yet."
    "I don’t get to enjoy my moment of relaxation long when suddenly I hear a commission out in the hallway."
    "Curious, I get up to go see what is going on."
    show aletta angry
    "I come up to a scene of another worker screaming in Aletta’s face while she calmly stands there with her hands on her hips and everyone just watches."
    "I see how pissed off she is behind her composure."
    "I hear someone snicker before turning to see a female coworker whispering in another one’s ear, and I get the feeling they are not on Aletta’s side."
    "I remember the day Aletta was smoking in the break room and how stressed she was. This isn’t right."
    coworker_say "You ask too much from us!"
    coworker_say "You are just a lazy bitch who pushes all of your own work onto the rest of us and then complain when we can’t get it and our own work down on time!"
    coworker_say "I’m sick of being your lacky!"
    "Why wasn’t anyone saying anything?"
    "Whether they liked Aletta our not, this was wrong."
    menu:
        "Stand up for Aletta":
            hero.say "I think you need to back off buddy."
            "I take a step forward and become aware that all eyes are now on me."
            coworker_say "Who are you?"
            "The guy sneers at me."
            hero.say "I’m [hero.name], and that just so happens to be our boss that you are disrespecting."
            hero.say "Don’t you have any manners? You sound like a spoiled child."
            "Now there are snickers at the man who seems embarrassed."
            hero.say "If you knew half of the work Aletta does, you wouldn’t have a leg to stand on."
            "There are more murmurs around the workers as those who had just been siding with this guy were now unsure of themselves."
            coworker_say "Pff whatever. You’re just an ass kisser."
            "He turns and makes his exit as if he has won but I can tell he is eager to get out of here."
            "I just shake my head."
            "He didn’t even give me a change to respond."
            "Everyone starts to go back to work and I see Aletta looking at me with thankful eyes."
            show aletta happy
            aletta.say "That was nice of you to step in."
            "I shrug."
            hero.say "It was nothing. I was just trying to do the right thing."
            "She gives a bitter laugh."
            aletta.say "No one else was going to. You’d think as much as they all come to me with their problems they would be a little more grateful."
            $ aletta.sub += 1
            $ aletta.love += 1
        "Keep watching.":
            "The guy keeps yelling at Aletta. She can barely get a word in, and when she does she is almost drowned out by him."
            "But that is only because she is trying to stay professional."
            "Security finally comes."
            security_say "What’s going on here?"
            coworker_say "Nothing. We are just having a conversation."
            hero.say "You think screaming at your boss is a conversation?"
            "He sneers at me."
            coworker_say "Who are you?"
            hero.say "Doesn’t matter."
            security_say "Okay well if everyone can just go back to work there will be no need for further action."
            "The guy glares at Aletta, and then me, but finally agrees and goes back to work."
            "Security also leaves and with the show ever everyone goes back to their desks."
            "Except me."
            "Aletta looks tired and I find myself walking over to her."
            hero.say "Are you okay?"
            show aletta
            "She looks to me slightly surprised."
            aletta.say "All in a days work."
    aletta.say "I need a smoke now after all of that. Care to join me?"
    "I am surprised that my boss was inviting me on a smoke break, but I follow her to the break room anyway."
    "She offers me one but I’m not brave enough to push my luck today. It’s not even my break yet."
    scene bg breakroom
    "She lets out a sigh after lighting her cigarette."
    "She rubs her neck as if it hurts."
    menu:
        "Offer to give her a massage":
            hero.say "Does your neck hurt?"
            "Looking at me out of the corner of her eye she blows smoke out the window."
            aletta.say "When doesn’t it? It’s just tight like my shoulders."
            hero.say "Here let me help."
            "I stand behind her and start rubbing her shoulders and neck gently."
            "At first she stiffens and then easies into it."
            "I hear her let out a sigh of relief. And she leans her elbow on the window sill."
            show aletta happy
            aletta.say "You’re really good at that [hero.name]."
            hero.say "Thanks. Maybe I can do it more often if you would like?"
            aletta.say "Maybe I’ll let you. I’ll keep it in mind."
            "I keep massaging until she tells me it feels better than it has in a long time."
            $ aletta.love += 1
        "Tell her she should go get a massage":
            hero.say "Does your neck hurt?"
            "She glances at me as she takes a puff."
            aletta.say "Yeah, but when doesn’t it?"
            aletta.say "Part of the job description."
            hero.say "Maybe you should treat yourself to a massage at a spa?"
            "She looks to me and I think I catch a hint of disappointment in her eye before it is gone."
            aletta.say "Oh."
            "She drops her hand."
            aletta.say "Maybe. I’ll look into that."
            "She goes back to looking out the window and smoking her cigarette."
    show aletta
    "I don’t know what it is about Aletta that changed, but I feel myself getting closer to her when she is like this."
    "I feel the need to say something when suddenly the door to the break room opens and Aletta’s almost finished cigarette goes out the window."
    aletta.say "That’s correct [hero.name], so if you continue at the pace you are going you should have no trouble finishing your work by the deadlines this week."
    aletta.say "Good job on getting that assignment for yesterday finished, I understand it was a difficult one."
    "I am confused as to what she is talking about for a moment but then realize she is acting."
    hero.say "Um... thank you. I just wanted to make sure."
    "Make sure of what I didn’t know. I glance to the other worker that came in as they get a drink out of the frig and leave not having noticed Aletta was smoking."
    "After the door shuts Aletta smiles to me."
    aletta.say "Guess our break times over."
    aletta.say "Better get back to work before someone more observant comes in."
    "She shuts the window and I can’t help but watch a little disappointed as she leaves."
    hide aletta
    return

label aletta_event_03:
    scene bg alettaoffice
    $ aletta_love_max = 60
    $ aletta.set_flag("story",3)
    $ aletta.set_flag("nodate", False)
    $ aletta.set_flag("nokiss", False)
    "The deadlines at work this week are ridiculous."
    "So much so they are pretty much impossible to get done on time without working over. But did anyone volunteer?"
    "No, of course not."
    "So that is why Aletta came to me and 'suggested' I stay after when I first got to work this morning."
    "At first I was dreading it, but throughout the day as I imagined being alone with her I started to look forward to it until it was what was getting me through my regular shift."
    "Now that she is sitting next to me I felt like the temperature in the room has gone up ten degrees."
    "What am I thinking?"
    "She is my boss."
    "But I find myself sitting closer throughout the night and she doesn’t stop me."
    "Seeing her breasts peeking out of her shirt starts to make my heart beat a little bit faster."
    "Exactly what do I expect to happen tonight? That’s right. Nothing. Because she is my boss. I need to get a grip of myself."
    "A grip... hmm maybe that isn’t such a bad idea."
    "Maybe that’s just my problem, I need to get off."
    "I could go to the bathroom real quick and jerk off and she would never know-"
    show aletta
    aletta.say "[hero.name]..."
    aletta.say "[hero.name] are you listening to me?"
    "I shake myself out of my thoughts."
    hero.say "Uh, what? Sorry. I kind of zoned out."
    "I try to laugh it off but she doesn’t look happy with me."
    aletta.say "I’ll go over it again, but pay attention this time."
    "In no time I am zoned out again just watching her lips move and barely catching what she is saying."
    menu:
        "Brush against her arm":
            "I lean slightly closer as if to see the report she is showing me better and brush my arm against hers"
            "To my surprise she doesn’t flinch away."
            "So I decide to keep my arm there and she doesn’t move away."
            "Trying to hide my smirk I feel a surge of confidence."
            "But also blood rushing south."
            "Opps."
            $ aletta.love += 1
        "Keep some space between each other":
            "I lean on my right arm to keep from moving any closer to her."
            "At first she keeps talking but then glances my direction and there is a flicker of disappointment before she continues with what she is telling me."
            "Is it just my imagination?"
    aletta.say "So do you understand what I am saying?"
    hero.say "Uh, yeah. I-I mean, yes, Aletta. I should be able to get it done no problem."
    "She seems to relax into her chair for the first time, taking off her glasses and putting one ear piece to her lips."
    aletta.say "That’s a relief. I was really worried about how to get this assignment done. I really don’t need corporate on my ass again."
    "She sighs and reaches back to rub her tense shoulders."
    "I want so badly to rub them for her but don’t trust myself to be able to stop there."
    "The thought of having her bent over the desk out in the open with her skirt pushed up-"
    "Wait what? Since when am I someone who falls for their boss?"
    "Am I falling for her? Or am I just horny?"
    "It has to be just horny. And she is an attractive woman. It is understandable."
    "That’s it I need to go take care of this."
    hero.say "Don’t worry about it Aletta, I’ll have it done before I leave here. I’m just going to go to the bathroom real quick."
    aletta.say "No problem, [hero.name], it really is a great help."
    "She suddenly drops some of her papers as she turns in her chair to get up."
    aletta.say "Oh-."
    hero.say "Don’t worry I got them!"
    "I quickly drop to the floor before she can get out of her seat and gather them up. Some slide under the desk and I have to crawl under."
    "When I come back up I turn my head and my heart jumps when I realize I can see up her skirt and can’t tear my eyes away."
    "At first I think I am imagining that her legs are opening wider to show her panties and I can’t believe my luck until she talks."
    show aletta blush
    aletta.say "You know, that is quite rude to stare."
    "I look up so fast I bang my head on the bottom of the desk and swear."
    menu:
        "Apologize":
            "I’m so sorry Aletta. I... It just caught me off guard."
            $ aletta.sub -= 1
        "Play dumb":
            "I-I... don’t know what you mean."
    "Not being able to look her in the eyes I quickly hand the papers to her, which she takes with a smirk."
    aletta.say "Let me know if you need anything, [hero.name]."
    "Now I definitely need to go to the bathroom, I think as I watch her walk away."
    hide aletta
    "Once in the stall I don’t waste any time pulling my cock out of my pants."
    "I set a timer and tell myself I am going to make sure I cum in two minutes."
    "This has to be a quicky because I am not going to get caught with my pants down at work."
    "I wrap my hand around my cock and moan."
    "Jerking it to a steady tempo I can feel the pleasure flooding my senses and I am glad it is after hours or I know I would get caught."
    "I can’t think about anything else right now."
    menu:
        "Think about Aletta’s breasts":
            "I start to image her breasts free of her shirt and me cupping them in my hands before taking one of her nipples into my mouth."
            "I imagine the moans that would pour out of her and start jerking off faster."
            "If only I was actually holding them instead of my dick."
            "I keep thinking of Aletta’s breasts in the most lewd ways possible and in no time I am cumming all over my hand and panting heavily."
            "I wash my hands and go back to work thinking about how I couldn’t wait for a chance to spray her breasts with my cum."
        "Think about Aletta’s pussy":
            "I start to image spreading Aletta’s legs wide open and taking those lace panties off."
            "I think about plunging my fingers into her and making her scream."
            "I keep jerking off with my eyes closed pretending my hand is really Aletta’s pussy and cum hard all over my hand."
            "After I clean up I go back to work with a satisfied smile, hoping I can get a chance at the real thing soon."
        "Think about an office intern":
            "I find myself thinking about an intern in the office instead of Aletta and before I know it my hard on is gone and I’m left disappointed."
            "I sigh and go wash my hands before going back to work."
    "At least my problem was gone."
    return

label aletta_event_04:
    scene bg alettaoffice
    $ aletta_love_max = 80
    $ aletta.set_flag("story",4)
    show aletta
    "I hear Aletta huff in aggregation and reach down to take her heels off all of a sudden."
    "We were working over again and she had seemed in a cranky mood the whole time."
    aletta.say "I hate that I have to wear these stupid high heels everyday."
    hero.say "Why don’t you just wear flats then?"
    aletta.say "Can’t, part of the dress code for us bosses. Makes us look more professional or some bullshit like that. All it does is give me sore feet!"
    "She starts rubbing her foot with the cutest pout I have ever seen her have."
    "I give her a smirk."
    hero.say "Here, let me help you with that."
    "I reach down and lift her legs up and put her feet in my lap."
    "She raises her eyebrow at me and moves so I can’t see her underwear to my disappointment."
    aletta.say "What are you doing, [hero.name]?"
    hero.say "Helping."
    "With that I start massaging her right foot and she makes a sound of pleasure."
    aletta.say "I might have to make you do this more often."
    "She leans into the back of the couch and puts her other foot in my lap close to my crotch, teasingly close."
    "I start to notice that ever time I find a good spot while massaging her foot she gets a little bit closer to my crotch her other one."
    "When I switch to her other foot she presses the first one completely against my groin and I have to hold back a moan."
    "She keeps pressing harder and rubbing with her foot as I massage all the while making complete eye contact with me."
    "For some reason I find this so hot."
    menu:
        "Talk dirty to her":
            hero.say "Well, well, aren’t you a naughty girl?"
            show aletta blush
            "She gives me a smirk."
            aletta.say "Me? The naughty one? You are the one getting hard by your boss rubbing you off. Looks like you are the bad one."
            hero.say "Me? You started it."
            aletta.say "No, I believe you did when you tried to look up my skirt."
            "I can’t really deny this."
            "She gives me a wink."
        "Pretend not to notice what she is doing":
            "I try my hardest for as long as I can to pretend like I can’t feel what she is doing."
            "But it just feels so good, even if it is just through my pants."
            "Finally a moan escapes me despite myself."
    show aletta happy
    "Aletta laughs and get up off the couch."
    "She gives me a sexy look as she lifts up her skirt just enough to hook her thumbs into her panties and pull them down her legs while making eye contact."
    "I can feel my heart pounding and my cock throbbing as she does so."
    "I can’t take my eyes off of her."
    show aletta oral noman
    "With a laugh she tosses them onto the floor and then places her hands on the table next to the couch."
    "Her pussy is just barely covered by the bottom of her skirt and she looks back at me with a lustful look as if temping me."
    "She spreads her legs more as if in invitation."
    menu:
        "Push her skirt up gently":
            "Getting up slowly I rub her bottom before taking the hem of her skirt in my hands and pushing it above her ass."
            "I look at what was before me and it is such a beautiful sight."
            "Her lips are already wet for me."
        "Be rough with her":
            "I yank her skirt up over her ass and give the right side a hard slap making her gasp."
            "She looks back at me in shock but pushes back against me as if she wants more."
            "So I give her another real quick slap before moving on to more fun."
    show aletta oral manb
    "I take my fingers and run them along her lips slowly and teasingly until I suddenly thrust them into her center and she lets out a moan, pushing back to further fill herself with them."
    "Only a few minutes of this and her juices are already all over my fingers and threaten to run down her legs."
    "Needing more leverage, she drops down to her knees on the table."
    "It is the sexiest sight I have ever seen."
    "I follow suit, going down to my knees on the floor so my face is level with her pussy."
    "I love the smell of her and have a feeling I am going to enjoy the taste of her as well."
    show aletta oral mana tongue
    "I plunge my tongue inside and she lets out a startled but pleasured yell."
    aletta.say "Oh [hero.name]..."
    "Her moan is so sexy I decide to reward her by rubbing her clit in slow circles and continue to lick her out at the same time."
    "I hear her start to pant heavily."
    aletta.say "[hero.name]... [hero.name]... I’m... I’m going to..."
    hero.say "It’s okay Aletta, just let go and enjoy yourself."
    "I quickly replace my tongue with my fingers to help her along and she lets out a long drawn out moan as she squirts on my face."
    menu:
        "Try to catch it in your mouth":
            hide aletta
            show aletta oral mana cum
            "Knowing she was about to do so I had opened my mouth trying to catch as much as I could, licking my lips when she was done."
            hero.say "Mmm, Aletta you taste so good."
        "Quickly shut your mouth":
            hide aletta
            show aletta oral manb cum
            "Knowing she was about to do that, I quickly try to shut my mouth but didn’t turn my head quick enough."
            "I make a face but try not to let her see it."
    hide aletta
    show aletta oral mana arm
    "I start to suck on her clit while still thrusting my fingers back and forth in her and she moves to give me more access as more needed, breathy, moans come out of her mouth."
    show aletta oral mana arm tongue
    "I lick her from her clit to her taint and back again as she tries to push back on my face."
    "She squirts again and seems to be losing control of herself."
    "I massage the walls of her vagina and nurse her clit at the same time and don’t let up as I hear her beside herself in pleasure."
    "She tries to say my name but can hardly speak."
    show aletta oral mana arm tongue orgasm
    aletta.say "[hero.name]!"
    "I suddenly feel a shudder go through her and she lays her head down on her arms as she rides out the rest of her orgasm."
    "Standing up I use a tissue to wipe off my face before stealing her panties and pocketing them."
    "I didn’t think she was going to miss them."
    hide aletta
    return

label aletta_event_05:
    scene bg personal
    $ aletta_love_max = 100
    $ aletta.set_flag("story",5)
    "I’m halfway to falling asleep in the middle of my current project when there’s a knock at my office door."
    "I make sure I’m upright and look awake and focused before I call out."
    hero.say "Yeah? Come in."
    show aletta work at left
    "The door swings open and Aletta steps inside."
    "She doesn’t immediately say anything, like ‘hey, I was just looking for the stapler,’ so my first thought is that I’m in some kind of trouble."
    show dwayne teaser at right
    "But she steps aside, and another someone steps into the doorway after her."
    "He’s big and surprisingly burly in his office formal wear, his muscles visible beneath the fabric of his shirt."
    "What is this, Aletta’s newest hire?"
    "He looks like an ex-underwear-model thinly veiled as an employee."
    "I bet she’s gonna keep him under her desk."
    aletta.say "I wanted to introduce you, since I don’t think you’ve ever met."
    "Aletta holds a hand up to the guy, who seems to be waiting for something."
    "I realize immediately that he’s expecting me to get to my feet and shake his hand."
    menu:
        "Get up":
            $ game.set_flag("worksatisfaction",5,mod="+")
            if "work" in hero.skills:
                $ game.set_flag("worksatisfaction",5,mod="+")
            "I guess I’ll give the guy some dignity, even if he might be a nobody."
            "I’m not stupid enough to potentially piss off someone important, anyway."
            "I roll back my seat from my desk and get to my feet, turning to offer my hand to the dude."
            "His hand seems to be twice the size of mine when he reaches out and gives it a firm shake."
            aletta.say "This is Mr. --"
            dwayne_say "Please."
            "He interrupts her, giving me a formal but pleasant smile as he looks down at me with my hand still clasped in his."
            dwayne_say "Dwayne’s fine."
            "Ah. He’s the kind of ‘I’m a cool coworker’ guy."
            "I don’t mind."
            "They’re definitely better than the uptight stiffs who expect you to address them like royalty."
            hero.say "Nice to meet you."
            aletta.say "Dwayne, he’s been working with us for a while now. He’s…"
            "She stops to think for a second, staring at me, like she’s evaluating what she wants to say."
            if game.get_flag_value("worksatisfaction") > 50 or game.get_flag_value("promoted") >= 10:
                $ aletta.love += 10
                aletta.say "... efficient, and talented. I’m happy to have him as an employee."
                "Aw, Aletta, you shouldn’t have. I could almost blush."
                dwayne_say "A driving force in the company’s success, huh?"
                "Dwayne gives my hand one last firm shake before letting it go and stepping back."
                dwayne_say "Very nice to meet you."
                hero.say "Likewise."
            else:
                aletta.say "...he’s been getting the job done."
                "Dwayne chuckled, giving my hand one last small shake before letting it go and stepping back."
                dwayne_say "A workhorse, huh? Always good to have them on board."
                hero.say "Good to be here."
                "Having a job is kind of a necessity, anyway."
            "I get the feeling this isn’t her new hire."
            aletta.say "You might not recognize him by first name. Dwayne is the CEO of the company."
            "Recognition floods me all at once, and suddenly I’m looking at this mammoth of a man with new eyes."
            "That’s right, his name was Dwayne, wasn’t it?"
            "It’s hard to remember, since the guy’s never really around in the office."
            aletta.say "Well, we’ve got more stops to make, so."
            hero.say "Ah, yeah. I’ll get back to work."
            dwayne_say "Have a good one."
            hero.say "You, too."
            hide dwayne
            hide aletta
            "It’s a little jarring, still, after the two of them leave."
            "I wish she would have warned me he was coming around today, so I could have dressed a little nicer or something."
            "Oh well. I think I made a good enough impression."
        "stay seated":
            $ aletta.sub += 10
            "I lean myself back a little bit in my seat, making myself comfortable."
            "I was almost dozing off a second ago; I’m not gonna expend any precious energy standing up for formalities."
            "I’m sure he doesn’t actually care."
            "Aletta seems like she’s shooting me daggers from my peripheral, but I don’t bother to look over to catch them."
            "I keep my eyes on the new guy."
            "She seems a little flustered by my choice."
            "I never really thought of first impressions as being as important as people make them out to be."
            "I need time to grow on people. Formality is fake, anyway."
            aletta.say "Well…"
            "She gestures towards me, and the guy nods his head."
            aletta.say "He’s…"
            "She pauses, maybe trying to think of some way to talk me up, even if she thinks I’m being a bit rude."
            if game.get_flag_value("worksatisfaction") > 50 or game.get_flag_value("promoted") >= 10:
                $ aletta.love += 10
                aletta.say "...surprisingly competent,"
                "she continued though it seemed to pain her a little bit."
                aletta.say "Usually not like this."
                "Aw, Aletta, you shouldn’t have. I could almost blush."
                man_say "A driving force in the company’s success, huh?"
                "He seems less bothered by my snub than Aletta is."
            else:
                aletta.say "...he’s been getting the job done."
                "I guess that’s all she can manage, right now."
                man_say "A workhorse, huh? Always good to have them on board."
            "I’m starting to get the impression that this guy’s not just her new hire."
            "Aletta clears her throat and glances back to me."
            aletta.say "This is Mr.--"
            "She still sounds a bit strained while she addresses me."
            dwayne_say "Please."
            "He interrupts her, giving me a tight and formal smile as he looks down at me."
            dwayne_say "Dwayne’s fine."
            aletta.say "...He’s the CEO of our company."
            "Oh, shit."
            "Well, it’s too late to jump to my feet and try to grovel."
            "I hope that it exudes confidence and some kind of alpha-demeanor for me to remain seated, but at this point I don’t get the impression that Dwayne’s the kind of man to be impressed by feigned dominance."
            "He could ruin my life in a second. I gulp hard, but try to keep my appearance under control."
            dwayne_say "Well, it’s been nice to meet you."
            "Aletta shoots me a glance that says she doesn’t feel the same."
            hero.say "Uh, yeah. Likewise."
            hide dwayne
            hide aletta
            "I feel a little off even after they leave, internally cringing, just a little bit."
            "She could have at least warned me, or something."
            "You can’t just barge in with higher-ups and expect me and my office to be spotless and perfectly deferential behavior off the bat."
            "Oh well. Hopefully I gave a good enough impression to not lose my job."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
