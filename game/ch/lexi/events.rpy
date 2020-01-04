init python:
    Event(**{
        "name": "lexi_event_02",
        "label": ["lexi_event_02"],
        "priority": 500,
        "duration": 0,
        "girls_conditions": {"lexi":{"flag_story":1}},
        "max_girls":0,
        "game_conditions":{"room":["livingroom"],"hours":(20,25), "flag_female":0},
        "do_once":True,
        })

    Event(**{
        "name": "lexi_pregnant_flag",
        "label": ["lexi_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"lexi":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "lexi_start",
        "label": ["lexi_start"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"flagmin_lexistart":1, "room":["nightclub"], "flag_female":0},
        "do_once":True,
        "quit": False,
        })

    Event(**{
        "name":"lexi_init",
        "label": ["lexi_init"],
        "girls_conditions": {"lexi":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "lexi_give_christmas",
        "label": ["lexi_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"lexi":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "lexi_give_birthday",
        "label": ["lexi_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"lexi":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "lexi_give_valentine",
        "label": ["lexi_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"lexi":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "date_lexi_meet_jack",
        "label": ["date_lexi_meet_jack"],
        "duration": 0,
        "game_conditions": {
            "room":["date_mall"],
            "chances": 5,
            "flag_female":0
            },
        "girls_conditions": {"lexi":{"present":True,'valid':True, "min_love":150}},
        "do_once": True,
        })

    Event(**{
        "name": "date_lexi_meet_jack_3",
        "label": ["date_lexi_meet_jack_3"],
        "duration": 0,
        "game_conditions": {
            "activity":["talk"],
            "done":"date_lexi_meet_jack_2",
            "flag_jackandlexi":2,
            },
        "girls_conditions": {"lexi":{"present":True,'valid':True,"active":True}},
        "do_once": True,
        })

    Event(**{
        "name": "date_lexi_meet_jack_4",
        "label": ["date_lexi_meet_jack_4"],
        "duration": 0,
        "game_conditions": {
            "room":["map"],
            "done":"date_lexi_meet_jack_3",
            "hours":(15,17)
            },
        "girls_conditions": {"lexi":{'valid':True}},
        "do_once": True,
        })

    Event(**{
        "name": "date_lexi_meet_jack_2",
        "label": ["date_lexi_meet_jack_2"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"hours":(16,17),"chances":5,"flag_dateinprogress":0,"flag_jackandlexi":1, "flag_female":0, "done":"date_lexi_meet_jack"},
        "do_once":True,
        })

    Event(**{
        "name": "lexi_sell_drugs",
        "label": ["lexi_sell_drugs"],
        "duration": 0,
        "game_conditions": {
            "room":["park"],
            "hours":(0,5),
            "flag_female":0
            },
        "girls_conditions": {"lexi":{'valid':True, "min_love":150}},
        "do_once": True,
        })

    Event(**{
        "name":"lexi_preg_talk",
        "max_girls": 1,
        "label": ["lexi_preg_talk"],
        "duration": 0,
        "do_once": False,
        "girls_conditions": {"lexi":{"flagmin_pregnant":6,"flag_pregtalk":0, "active":True}},
        "game_conditions": {"activity":"interact"}
        })

    Event(**{
        "name": "lexi_sasha_1",
        "label": ["lexi_sasha_1"],
        "duration": 1,
        "game_conditions": {
            "room":["date_mall"],
            "flag_female":0
            },
        "girls_conditions": {"lexi":{"present":True,'valid':True, "min_love":150},"sasha":{"room":["clothesshop"],'valid':True, "min_love":150}},
        "do_once": True,
        })

    Event(**{
        "name": "lexi_slave_request",
        "label": ["lexi_slave_request"],
        "duration": 1,
        "game_conditions": {
            "activity":["talk"],
            "flag_female":0
            },
        "girls_conditions": {"lexi":{"present":True,'valid':True, "min_sub":75, "active":True, "flag_slave":1}},
        "do_once": True,
        })

label lexi_slave_request:
    show lexi blush
    hero.say "Lexi, what's wrong?"
    hero.say "You're really starting to freak me out right about now!"
    "Lexi chuckles and cocks her head on one side, a quizzical look on her face."
    lexi.say "Huh?"
    lexi.say "What're you talking about, [hero.name]?"
    hero.say "Lexi, first you drop off the radar for days on end, no calls, no texts, no nothing."
    hero.say "Then you call me up, out of the blue and ask me to come over her, and you're being super sweet and nice."
    hero.say "That's not the normal you, and I know the normal you...hell, I kinda adore the normal you!"
    "Lexi actually blushes a little, looking away as though she can't meet my eye."
    "That's scary too, as I've never seen this girl blush before, no matter what was going on at the time."
    lexi.say "Ah...it's not easy for me to say..."
    hero.say "Try, Lexi...I'm listening."
    lexi.say "Well, you know how we saw that Sasha chick when we were out shopping the other day?"
    "The first time my girlfriend on the side met my slave - how could I forget?"
    hero.say "Yeah...I do."
    lexi.say "And do you remember what we talked about after?"
    "Ah, of course...now it starts to make some kind of sense!"
    hero.say "Yeah, Lexi...I remember that as well."
    lexi.say "I've been thinking a lot about it...about what you said I could be..."
    hero.say "You've been thinking about whether or not you want to be my slave too...just like Sasha already is?"
    "Lexi nods, still unable to meet my eye."
    lexi.say "Yup, just that."
    lexi.say "And I think...that is to say that...I want to."
    "She still can't quite bring herself to say the actual word out loud."
    hero.say "You want to be what, Lexi?"
    hero.say "Come on, out with it - you can't truly become it, not if you can't say it to my face."
    "Slowly, Lexi looks up and manages to meet my eye."
    "It's hard to believe that she's this shy and maybe even scared of something after all."
    lexi.say "[hero.name], I want...I want to be your...slave."
    lexi.say " I want to be your slave."
    "I get the feeling that Lexi repeats herself as much for her own benefit as mine."
    menu:
        "No":
            hero.say "I have to be honest, Lexi - I don't think that'd be a good idea."
            "Lexi keeps up the theme of unfamiliar facial expressions, now showing crestfallen disappointment."
            lexi.say "But...but why not?"
            lexi.say "We've done all kinds of crazy shit since we hooked up!"
            lexi.say "And I'm well used to doing as I'm told...it comes with being pimped out for so long!"
            "I sigh at her words, not liking being forced to make the admission that's coming next."
            hero.say "That's part of the problem, Lexi...this is different to what you've known before."
            lexi.say "How?"
            hero.say "Back then you were obeying Danny because he controlled you, beat you, even threatened to kill you."
            hero.say "You were afraid of him, Lexi."
            hero.say "This kind of master and slave relationship isn't like that - it's based on trust."
            hero.say "I don't want to become like Danny, and I really don't want to see you go back to being afraid of someone who should love you."
            hero.say "Lexi, I've fallen for who you've grown into since we got rid of that sack of snake faeces."
            hero.say "I won't stifle that person for the sake of getting freaky or having you give me an ego rub."
            "Lexi looks even more disappointed now, but as the meaning of my words sinks in, she begins to smile weakly."
            lexi.say "You...you really mean that...that you like me just the way I am?"
            hero.say "Yeah, Lexi - you're honest, uninhibited and I have more fun than I could imagine with you already."
            hero.say "I don't want to change you, or for you to change for me."
        "Yes":
            $ lexi.set_flag("slave",2)
            hero.say "I don't know, Lexi - are you ready to devote yourself to me, mind and body?"
            "Lexi nods eagerly at the question."
            hero.say "Are you able to obey me, without question, no matter what I ask of you?"
            "She nods again."
            hero.say "Will you submit yourself willingly to any punishment that I decide you deserve?"
            "I see Lexi almost shiver at the mention of punishments, but she nods all the same."
            hero.say "Lexi, can you accept me as your one and ONLY master?"
            "Lexi's cheeks are almost burning now, but I can't tell if from embarrassment or arousal."
            hero.say "Alright then...if you can promise me all of that, then I can accept you as my slave."
            "Lexi sits with her hands in her lap, looking up at me eagerly, waiting to be given her first command as a slave."






            lexi.say "Th...Thank you...M...M...Master..."
            "There's a sense of anticipation in her words, and one of release as well."
            "Maybe Lexi's been longing for something like this to happen to her for a very long time and just didn't know it."
    return

label lexi_sasha_1:
    scene bg mall
    show lexi
    lexi.say "Hey, I wanna look in here!"
    hero.say "Erm...I didn't think that whole goth thing was your bag."
    lexi.say "Maybe I want to try something new...they got straps, spikes and stuff like that too."
    lexi.say "Don't tell me you wouldn't like to tie me up and spank me?!?"
    scene bg clothesshop
    "Before I can come up with another lame excuse, Lexi's already dragging me towards the store entrance."
    "I can't protest any louder for fear of making a scene or letting Lexi know what's real source of my reluctance."
    "At the same time, I don't want Sasha to hear my voice either."
    "I try to hang back a little, as Lexi busies herself digging through items of clothing in black and conspicuously made of rubber."
    hide lexi
    show sasha
    "Just as I'm beginning to think that Sasha might be on a break or tied up in the back of the store, I hear the inevitable sound of her voice behind me."
    sasha.say "Oh, hey [hero.name], haven't seen you in here before."
    sasha.say "What's up?"
    hero.say "Hey, Sasha - I was just in the mall, and I guess I thought I'd say hello."
    "Sasha suddenly notices Lexi, and I can see her eyes sweeping over the other girl in harsh judgement."
    sasha.say "Urrgh...we get one of these every so often."
    sasha.say "Refugees from the discount stores or Goodwill by the pound!"
    "I grin nervously, thinking that if Lexi stays put, maybe I can wrap up talking to Sasha before either sees the other or knows I know them too."
    hide sasha
    show lexi at left
    show sasha at right
    lexi.say "Hey, [hero.name] - this one's got a hole in the crotch!"
    lexi.say "That's gotta be for fucking, right?"
    show sasha
    "Sasha fixes me with an almost horrified stare as Lexi bounds over, clutching something shiny and unbelievably small in her hands."
    "Suddenly, both of them are looking at each other, and then back at me."
    "Feminine instinct means that they both know something's up."
    "And they're evidently waiting for me to attempt an explanation to clear everything up neatly in a package."
    "Probably with a bow on top too."
    if not "sasha_sub_event_1" in DONE or sasha.sub < 75:
        show sasha angry
        hero.say "Ah, Lexi...meet Sasha!"
        hero.say "She's...my housemate."
        "While Lexi doesn't seem to initially pick up on the awkward tone of my voice, Sasha's eyebrows raise significantly at being described as nothing more than my housemate."
        lexi.say "Oh, hey there, Sasha!"
        show sasha normal
        sasha.say "Hello...Lexi...how do you know [hero.name] here?"
        lexi.say "Well, it's kind of romantic, you know?"
        sasha.say "Really?"
        lexi.say "Oh yeah - we met in a club one night, and he saw off my old boyfriend, who was also kinda my pimp at the time."
        sasha.say "You don't say?"
        lexi.say "I do...and now we're fuck buddies!"
        show sasha wtf
        sasha.say "Wow - it's like some kind of fairy tale come true."
        "Lexi nods, apparently unaware of the sarcasm dripping from Sasha's words."
        "She returns to browsing the racks, blissfully unaware of what's happening just out of earshot."
        hero.say "Sasha...I can explain..."
        show sasha angry
        sasha.say "Really, [hero.name]?"
        sasha.say "Because if you can, I want to hear it."
        sasha.say "It must be some really crazy explanation."
        "I begin to open my mouth, but then my shoulders sag as I realise the game is up."
        sasha.say "Oh, [hero.name] - I'm not mad...just disappointed, I guess."
        sasha.say "I thought what we had was good, that it was enough."
        $ sasha.love -= 25
        sasha.say "Looks like it was only good enough for me."
        hide sasha
        "We linger around for a few more minutes, until Lexi's done browsing."
        "Back out in the mall, she seems to sense that there's something wrong."
        lexi.say "Blow-job for your thoughts?"
        hero.say "What...oh, yeah - I think I just went and ruined my relationship with Sasha back there."
        lexi.say "How come?"
        hero.say "Well...I guess I wasn't being strictly honest when I said that she was just my housemate, if you get what I mean!"
        lexi.say "Yeah, I kinda got that vibe off of her...I just didn't want to rub your nose in it."
        hero.say "You're not mad at me?"
        "Lexi laughs in a snorting, unselfconscious manner that speaks of her easy sexuality and basically honest nature beyond her initial appearance."
        lexi.say "[hero.name], you think that Danny didn't screw around with whatever took his fancy?"
        lexi.say "He couldn't have given a shit, and he was beating the hell out of me at the same time, too!"
        lexi.say "So you fucked this Sasha bitch, so what?"
        lexi.say "You can keep on doing it, if she'll let you, for all it bothers me."
        lexi.say "Gimmie the choice between a good guy that fucks another woman on the side and a bastard that does the same and hits me, and I'll take you every time."
        lexi.say "And if the raging bitch can't learn to share, then fuck her."
        lexi.say "Because you can always fuck me instead!"
    else:
        $ lexi.set_flag("slave",1)
        sasha.say "Who is this, Master?"
        "I don't immediately answer, instead watching Lexi's response to the other girl's submissive posture and term of address."
        "She looks at Sasha's downcast gaze, then at me with a puzzled expression on her face."
        hero.say "This is Lexi, Sasha - another girl that I've been fucking at the same time as you."
        sasha.say "Oh, I see."
        sasha.say "Does she please you, Master?"
        hero.say "She satisfies me, yes...but she's not as obedient as you."
        "Lexi notes the instant and sincere smile this last comment elicits from Sasha, her mouth hanging open in genuine surprise."
        hero.say "Are you jealous of Lexi, Sasha?"
        "Sasha looks down at the floor for a moment, obviously thinking hard about her answer."
        sasha.say "Yes, master."
        "She looks up and catches my questioning look."
        sasha.say "But only because she occupies time when I might be pleasuring you myself."
        sasha.say "Maybe...maybe we could both pleasure you at once, Master?"
        sasha.say "Then we could try to outdo each other in gratifying you, Master!"
        hero.say "Maybe, Sasha, maybe."
        hero.say "Well, I don't need to talk to you any longer, so you can go."
        hero.say "I may fuck Lexi here before I come home."
        hero.say "But I promise that I'll still have enough energy to do you as well, even if it's just letting you give me a blow-job."
        "Sasha nods happily at the last part, turning away and getting back to her work on the shop floor."
        hide sasha
        "I can see Lexi looking at me in what might actually be fascinated awe as we leave."
        "Based on her past with that scumbag Danny, it must be odd to see a woman so obedient and submissive without a hint of violence in the offing."
        lexi.say "[hero.name]...what was that back there?"
        lexi.say "Why was that Sasha girl talking to you like that...calling you 'Master' all the time?"
        hero.say "Ah, I don't exactly advertise it, Lexi...but I've kinda been getting really into BDSM recently...bondage and all that stuff."
        "Lexi nods slowly, clearly turning this revelation over in her mind and getting to grips with how it changes her image of me."
        hero.say "There's really no other way to say it - Sasha's my slave and I'm her master."
        lexi.say "It looks kinda...kinda kinky."
        hero.say "You have no idea, Lexi!"
        "I can see that this whole thing is putting Lexi on the wrong foot."
        "She's clearly so used to being able to shock me with her own outrageous past, that it's made her unsure and more than a little confused."
        lexi.say "Would you...well...would you like me to be like that too?"
        hero.say "You don't have to do it in order to keep me, Lexi."
        hero.say "I won't stop wanting to fuck you just because you're not my slave too."
        hero.say "But if you're interested, then yes...I'd let you be my slave as well."
        hero.say "If I'm honest, your past kept me from bringing it up."
        hero.say "I don't want to turn into Danny 2.0...you know?"
        "Lexi thinks for a couple of minutes, a long time for her to keep from talking, and then slowly shakes her head."
        lexi.say "I don't think it's the same...I don't think you're the same as him, not at all."
        hero.say "Okay, if that's how you feel, we'll give it a shot."
        "Lexi smiles in an oddly satisfied manner, and I can't tell if she's genuinely happy or just wanting to outdo Sasha."
        lexi.say "Maybe we can try that thing that Sasha talked about too?"
        lexi.say "You know, trying to see who can be the best slave and please the master the most?"
    "I begin to wonder about the relative merits of Sasha and Lexi."
    "As well as any possible ways they could be convinced to tolerate the presence of the other, now that they know I've been seeing them behind each other's backs."
    return

label lexi_preg_talk:
    show lexi
    "I can sense that there's something up with Lexi almost the moment that I see her."
    "She might be a professional when it comes to using her natural charms to get her way."
    "But she's actually pretty bad at lying when she can't use her hips, ass or chest to her advantage."
    "She's visibly edgy, glancing over her shoulder as she walks up the driveway to the house."
    "When I open the door, she almost darts inside, as if she's afraid of being seen."
    "My mind leaps to the most obvious conclusion imaginable."
    hero.say "What's up, Lexi?"
    hero.say "Has that ape Danny been beating you again?"
    lexi.say "What?"
    "Lexi looks startled, but I don't know if it's at the mention of violence or just of a thug like Danny."
    lexi.say "No, no...well, no more than usual."
    "If it were anyone else saying that, I'd have been horrified and telling her to call the police."
    "But then, if it were anyone else, I wouldn't be asking them that question in the first place."
    "It strikes me as odd how quickly I've come to accept the strangeness of Lexi's life as almost normal for her."
    hero.say "Okay...you want to sit down and have a drink?"
    "Normally Lexi wouldn't hesitate to accept any kind of alcohol at almost any hour of the day."
    "But now she pauses for a full five seconds before nodding, as though she has to think about it first."
    "I pour her a glass of the red wine that she seems to have been getting a taste for on her recent visits to my home."
    "I carry it over to the sofa, where Lexi's already draped herself in a habitually showy manner."
    "Though her face still looks preoccupied, her body gives out the same vibes as always."
    "I find it hard to make myself look serious and keep from staring at the way her skimpy clothes do nothing to hide her astonishing body."
    hero.say "So, lexi...what's up, for the second time of asking?"
    lexi.say "Erm...well...this is kinda hard to say..."
    "It must be bad, as Lexi's never been short of words or afraid of saying whatever comes into her head before now."
    hero.say "Don't worry, you can tell me anything, Lexi."
    "She smiles weakly at this, showing that rare honest vulnerability that makes her so much more than the cheap little harlot she seems to be in the outside."
    lexi.say "Well...with what we've been doing...I thought I ought to tell you..."
    "My smile gets ever more pained as I'm convinced that she's about to tell me she's had bad news from the VD clinic."
    lexi.say "I'm pregnant - or I think I am!"
    "My mouth moves, but no words seem to come out."
    lexi.say "Well, say something, for fuck's sake - even if it's something mean about me and the way I live my life, just say something already!"
    "Of all the things I could have imagined her saying, I was not prepared for that."
    hero.say "Wow, Lexi - that's caught me off guard!"
    lexi.say "Well, I thought I'd tell you, 'cos you're the smartest person I know - the least crooked as well."
    hero.say "I guess I should be flattered...wait a minute, Lexi - the kid is mine, isn't it?!?"
    "Any other woman, I'd have expected to confirm the fact within a second."
    "But Lexi instead pauses for a moment, as if totting up the chances in her head."
    lexi.say "Oh, I'm almost totally certain it's probably your's."
    hero.say "You don't say?"
    lexi.say "Danny always uses a rubber, and he already beat up anyone else it could have been so badly that it can't be them - you follow?"
    "I nod, my head swimming at the hurricane of bad news Lexi most often represents."
    "Lexi doesn't say anything more, just looks at me with eyes that have never looked so large and pleading."
    "She looks so much like a vulnerable little girl in that moment."
    "I can't help but pick up on the fact that she wants me to tell her what to do, to make it all better for her."
    menu:
        "Tell her to abort":
            hero.say "You can't look after a baby, Lexi - Christ knows you're struggling to look after yourself."
            hero.say "I don't like it, but the best thing would probably for you to abort it now, before it's too late."
            "Lexi's expression becomes visibly more hopeful, but I can see she wants me to add something more to my advice."
            if hero.money >= 200:
                menu:
                    "Tell her you'll pay for it":
                        $ hero.money -= 200
                        $ lexi.love += 5
                        $ lexi.sub -= 5
                        show lexi happy
                        hero.say "Don't worry about the money, either - it's probably mine, and anyway, it's time someone was nice to you for a change."
                        "Lexi looks at me in a different way to normal, without a hint of calculation or cynicism."
                        "I wonder how often someone in her life as acted in her best interests out of pure affection for her alone."
                    "Don't":
                        $ lexi.love -= 10
                        $ lexi.sub += 5
                        show lexi sad
                        hero.say "The money shouldn't be a problem, not with how good you are at picking pockets and screwing gullible marks over."
                        "Lexi says nothing, just nods meekly, clearly having been expecting more from me."
            else:
                $ lexi.love -= 10
                $ lexi.sub += 5
                hero.say "The money shouldn't be a problem, not with how good you are at picking pockets and screwing gullible marks over."
                "Lexi says nothing, just nods meekly, clearly having been expecting more from me."
            $ lexi.set_flag("pregnant", 0)
        "Tell her to keep the baby and that you will support her":
            $ lexi.love += 10
            $ lexi.sub += 10
            hero.say "You can look after a baby, Lexi - so long as you have someone to look after you too."
            "Lexi's eyes are suddenly full of what looks like surprise, confusion and not a little fear as well."
            hero.say "Wait a minute, Lexi - before you say no, just hear me out."
            hero.say "You once told me that you live the life you live because you don't have a choice."
            hero.say "Well now I'm giving you that choice, because I think you're worth a hell of a lot more and you're being wasted in the life you're living."
            hero.say "Have the baby, and I'll be right by your side from now on."
            hero.say "Fuck Danny and fuck the past - it'll be just us, and whatver we want to make of it."
            "Lexi looks literally stunned, nodding with a blank expresion on her face."
            $ lexi.set_flag("pregtalk", 1)
    "The apprehension from when she came in gone, Lexi drains her glass as the weight of what we just agreed finally starts to sink in."
    "I can feel the same weight too, and I'm already trying to work it all out inside of my head."
    return

label lexi_sell_drugs:
    scene bg alley
    show lexi casual
    "I corner Lexi at the alleyway, keeping her from leaving as I confront her."
    hero.say "I thought you said you wouldn’t be dealing drugs anymore now that we’re together."
    "Flustered, she snaps back."
    lexi.say "Look, until you whisk me off my feet and get me out of the trailer park for good, I gotta keep myself supported somehow."
    hero.say "Supported? I do so much for you already. It’ll be a little longer, I promise Just... come on!"
    "She frowns, but then she nods at me. "
    lexi.say "Alright, alright, but a gal like me can’t just go unpunished for not listenin’ to ya."
    "Catching onto her quickly, I chuckle and place my hand upon her cheek, tapping her gently."
    "I then run my fingers through her hair and shove her down onto her knees."
    hide lexi
    show lexi bj casual nobg casual nodick
    hero.say "You’ve really been a bad girl. Show me how sorry you are!"
    hide lexi
    show lexi bj casual nobg
    "She wastes no time in undoing my pants and tugging them apart, letting my cock spring open."
    show lexi bj suck
    "Staring up at me with eyes that were definitely not sorry, she sucks my cock with the hungry skill that she can muster. "
    show lexi bj deepthroat open
    "Her eyes roll back as she tastes me, her tongue lapping up under the head as she gets into the rythmn. "
    "There’s not much I can do in this situation. "
    "Having the power over her is just too much, and the threat of being found only makes things worse."
    show lexi bj suck left right
    "I groan, gripping her hair, and pulling her back."
    show lexi bj normal cum
    "She stares in shock at my swollen pole, only to squeal when warm streams of cum shoot off and cling to her face, rolling slowly down along her. "
    show lexi bj facial
    lexi.say "O... oh fuck..."
    hero.say "That’s right. You are mine to do as I want!"
    show lexi stand2 alley casual manoutfit cum
    "I pull her up and slam her against the wall, my hands moving down along her body and lifting her legs. "
    "I hold her up against the wall by her waist and she instinctually takes me by the shoulders. "
    if persistent.xray:
        show lexi stand2 vaginal
    "With no more pomp, I thrust my still hard cock deep into her. "
    "Grunting, I whisper into her ear. "
    hero.say "Take it, and take it raw."
    hero.say "I’m gonna knock you up, and then you won’t be able to sell drugs, you’ll be so busy."
    lexi.say "Oh... oh fuck! Aaah, I’m a useless whore..."
    "I nip her on the ear as I continue to thrust away at her. "
    hero.say "Oh no, you don’t... you aren’t useless."
    hero.say "You’re mine, and that makes you the most important thing right here and now."
    lexi.say "Oooh... oh, you’re... you’re so sweet!"
    show lexi stand2 alley casual manoutfit cum ahegao
    "I hilt into her, tilting my own head back as I shoot off deep into her. "
    "She rolls her tongue out, going into full ahegao as I splurt up into her, filling her up, and leaving her swelling with my jizz."
    hide lexi
    show lexi casual
    "I step back and she slides down along the wall, huffing in a dazed mess. "
    lexi.say "Aa... aaah.... N... no more... selling... b... boss..."
    return

label date_lexi_meet_jack_2:
    play sound "sd/cell_vibrate.mp3"
    hero.say "Hey Jack."
    jack_say "Hi bro."
    jack_say "I wanted to ask..."
    hero.say "What?"
    jack_say "Are you serious about that girl you were with at the mall?"
    hero.say "Lexi?"
    menu:
        "Yes":
            hero.say "Yeah, totally."
            jack_say "Ok then, have fun I guess..."
        "Not really":
            hero.say "She's just a sweet piece of ass."
            jack_say "Do you think I could get a slice?"
            hero.say "What do you mean?"
            jack_say "Well I would pay good money to fuck that ass..."
            jack_say "And with that look of her I am pretty sure she would be willing."
            menu:
                "No way!":
                    hero.say "Nope, I am not a pimp..."
                    jack_say "Fuck man, you suck..."
                "Ok":
                    hero.say "500$"
                    jack_say "Sold!"
                    hero.say "I'll see what I can do."
                    jack_say "Thx man, you're a real friend."
                    $ game.set_flag("jackandlexi",2)
    return

label date_lexi_meet_jack_3:
    show lexi
    hero.say "Hey Lexi do you remember my friend Jack ?"
    lexi.say "The weird guy we met at the mall?"
    hero.say "He asked me if you would be willing to fuck him..."
    lexi.say "Why would I do that?"
    hero.say "He is willing to pay."
    lexi.say "..."
    $ lexi.love -= 10
    lexi.say "Ok."
    lexi.say "You get half of it, but not a cent more."
    hero.say "... ok."
    hide lexi
    return

label date_lexi_meet_jack_4:
    show bg trailer
    "So I find myself standing rather awkwardly outside of Lexi's trailer, looking at my watch."
    "It's getting close to the time that I agreed with Jack for him to show up for his 'appointment' with Lexi."
    show lexi casual annoyed
    lexi.say "Jeez, what are you even doing out here?"
    hero.say "Erm...I dunno - I was just waiting for Jack to show up."
    lexi.say "That's sweet of you, but maybe I should be the one showing the nerves?"
    hero.say "Give me a break, Lexi - I've never pimped anyone before now!"
    lexi.say "Urgh...just leave it to me, I've been pimped enough times for us both!"
    lexi.say "Look, just take his money and send him in to me."
    lexi.say "Think you can handle that?"
    "I nod, trying to look confident."
    lexi.say "Okay...God help me...just back me up if you hear any serious shit going down, yeah?"
    hero.say "Should we agree on a safe word?"
    lexi.say "Yeah, I was thinking of something like 'GET THIS FUCKING ASSHOLE OFF OF ME!!!'...what do you think?"
    "I sigh and nod to acknowledge her sarcastic point."
    "Lexi walks back into the trailer and I return to watching for Jack's arrival."
    hide lexi
    "He pulls up a few minutes later, his new and shiny compact car looking distinctly out of place in the trailer park."
    show jack normal
    "Jack almost jumps out of the car, apparently already anticipating what Lexi has in store for him."
    show jack happy
    jack_say "Hey, man - where's Lexi?"
    jack_say "She's in the trailer, right?"
    "He goes to enter the trailer, and looks surprised when I bar his path."
    show jack normal
    jack_say "What's up?"
    hero.say "Cash up front."
    jack_say "Oh, oh right...okay."
    "He hurriedly ferrets out his wallet and presses $500 in bills into my hand."
    show jack happy
    jack_say "Sorry, man - I guess I'm not as clued up on this kind of thing as you are!"
    hide jack
    "I furtively shove the notes into my pocket without counting them and close the trailer door."
    "As soon as I feel enough time has passed to make it look a little less obvious, I dart around the back of the trailer."
    "Luckily for me, Lexi's trailer has only a rickety fence behind it, so no one can see me as I scramble atop an old patio table dumped there."
    show lexi pimping
    "I already chose the window to let me look into Lexi's bedroom and watch the action about to take place."
    show lexi pimping laying
    "I can see Jack standing by the door and Lexi laid on the bed in a typically slothenly manner."
    "Their lips are moving, but I'm not really interested in what either of them is saying."
    "For all of his eagerness in front of me, Jack looks pretty nervous now he's alone with Lexi."
    "Lexi, by way of contrast, is acting all nonchalant and relaxed."
    "She stays reclined on the bed, not bothering to get up as she reaches for Jacks flies without asking permission first."
    "Where he was almost quaking before, Jack now freezes in place as Lexi's hand creeps into his pants."
    show lexi pimping handjob
    "She keeps talking to him as she massages his dick until I can clearly see it standing to attention through his shorts."
    "Lexi almost carelessly yanks Jacks now painfully erect dick out of his flies in one move."
    "He gasps in pain, and she giggles at the sound, still stroking his shaft all the while."
    show lexi pimping blowjob casual
    "Holding his eye, she leans forwards and begins to lick the tip and kiss it, wrapping her lips softly around it."
    "Then she closes her eyes and takes him slowly into her mouth, making small sounds of pleasure as she does so."
    "I find that I'm not so much watching them both as just focussing on Lexi and putting myself in Jack's place."
    "Memories of the last blow-job Lexi gave me come flooding back, and I can feel my own dick rapidly stiffening."
    "Lexi brings Jack almost to the point of blowing his load in her mouth."
    hide lexi
    "But then she pulls away with an almost audible sound and leaves him gasping."
    "Taken by surprise, Jack gapes as she casually tosses him a condom."
    "She unbuttons and yanks down her tiny denim shorts, tossing them into the corner of the untidy room."
    "Then Lexi climbs onto the bed with her back to him and pulls off her T-shirt."
    "Unhooking her bra, it's impossible not to see her large, heavy breasts fall free, even from behind."
    "She puts her hands on the headboard and bends forwards, proffering her ass to him."
    "During all this, Jack has been struggling to pull his pants off and put on the condom at same time."
    "He almost loses his balance and falls flat on his face as he finally manages one and then the other."
    show lexi pimping fuck
    "Luckily for him, he falls onto the bed and desperately clambers onto Lexi for all he's worth."
    "Lexi makes no attempt to build this up into something more than it is."
    "She's been sold to Jack as a piece of ass that he can fuck without consequences, and that's what she's giving him."
    "As he thrusts away desperately, she writhes and moans like he's showing her something entirely new."
    "But I've heard Lexi do the same with me, and I can see right through her performance."
    "Unsurprisingly, Jack can't hold on for very long, and he soon groans massively as he cums."
    hide lexi
    "Lexi coos and giggles, rubbing her hands over her belly and breasts to show off the fact that they're suitably slick with sweat."
    "They exchange a few awkward words as he wipes his dick on a grubby T-shirt she offers him."
    "And I choose this as the perfect moment to climb down and sneak back around to the front of the trailer."
    show jack perv
    "When he emerges from the door, Jack has assumed an air of confidence that doesn't hold true with his performance inside."
    hero.say "Well - do we have a satisfied customer, or what?"
    jack_say "Best five hundred dollars I ever spent, man!"
    hero.say "Yeah, she sure is something, isn't she?"
    jack_say "You know it - and I think she enjoyed herself too...if you know what I mean?"
    "Jack winks at me in a suggestive manner."
    hero.say "Really - you don't say?"
    jack_say "I DO say!"
    hero.say "Well, thanks for the cash - I think Lexi'll be putting hers towards finishing up her acting classes at night school."
    show jack normal
    jack_say "Acting classes?"
    hero.say "Oh yeah - you really should see her when she wants to put it on, utterly convincing."
    "Jack seems to deflate a little and I grin wickedly inside at the sight."
    hide jack
    "With that he climbs back into his car, making aimless small talk and obviously wanting to get away as quickly as possible."
    show lexi casual
    "I wave him off as I count his money and then divide it up between Lexi and myself."
    "Pimping might not be easy, but that doesn't mean it can't be fun."
    $ hero.money += 250
    hide lexi
    return

label date_lexi_meet_jack:
    $ game.set_flag("jackandlexi",1)
    show lexi
    "As we walk around the mall I hear a voice."
    jack_say "Hey, [hero.name]!"
    hide lexi
    show jack happy
    "I turn around and see Jack walking toward us."
    hero.say "Hey, Jack."
    show jack perv
    jack_say "Woah man, who's the cutie?"
    hero.say "Jack this is Lexi, Lexi meet Jack."
    jack_say "Hi hot stuff!"
    hide jack
    show lexi
    lexi.say "..."
    hide lexi
    show jack perv
    jack_say "You should swing by, I got weed."
    hero.say "Sorry man, we are in the middle of a date."
    hero.say "See you around."
    hide jack
    return

label lexi_give:
    if not hero.has_condom():
        $ gift = Item("condom",money_cost=10)
        "She hands me a box of condoms."
        hero.say "Thanks..."
        $ nbr = 10
        while nbr:
            $ hero.gain_item(gift)
            $ nbr -= 1
    elif lexi.love() >= 50:
        $ gift = Consumable("lexi's panties", money_cost = 100, effects = [("fun",5)], limit = "day")
        "She hands me a pair of panties."
        lexi.say "I just took them off."
        hero.say "..."
        lexi.say "Your welcome [hero.name]."
        $ hero.gain_item(gift)
    return

label lexi_give_valentine:
    show lexi
    "Lexi walks hesitantly towards me."
    call lexi_greet from _call_lexi_greet_7
    show lexi blush
    lexi.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Lexi throws a box of chocolates towards me."
    hero.say "Thank you, Lexi."
    $ hero.gain_item(gift)
    hide lexi
    return

label lexi_give_birthday:
    show lexi
    "Lexi walks towards me."
    call lexi_greet from _call_lexi_greet_8
    show lexi happy
    lexi.say "Happy birthday [hero.name]!"
    call lexi_give from _call_lexi_give
    return

label lexi_give_christmas:
    show lexi
    "Lexi walks towards me."
    call lexi_greet from _call_lexi_greet_9
    show lexi happy
    lexi.say "Merry christmas [hero.name]."
    call lexi_give from _call_lexi_give_1
    return

label lexi_init:
    if "lexi" not in HIDDEN:
        $ HIDDEN.append("lexi")
    $ lexi.set_flag("nodate")
    $ lexi.set_flag("nokiss")
    return

label lexi_start:
    $ lexi_love_max = 20
    $ lexi.set_flag("story",1)
    "Nightclubs are always so so."
    "Sometimes they’re lavish and worth the effort to enter. You might even end up brushing shoulders with some high profile people."
    "Other times they’re as tacky as they get. And they usually smell like puke."
    "Luckily this one is actually pretty damn good. Not the first time I’ve come here either."
    "I decided to come here on my own this time, since my friends are busy."
    "Usually they’d be happy to tag along, but I guess we all have our commitments to get to."
    "For now...my only commitment is trying to have a good time, and forget about nearly getting assaulted a while back."
    "Well, I actually was. Talk about danger..."
    "Leaning against the bar edge, I order a drink for myself casually, and scan the room."
    "Sipping my drink while dressed rather suavely, I figure I look inviting enough."
    "Naturally I’m looking to see if there are any lovely looking ladies around who might happen to be here alone too."
    "Who I don’t expect to see is a familiar face."
    hero.say "No...fucking...way..."
    show lexi date
    "It was only one time we met, but the event is so burned into my memory at this point that I recognize her instantly."
    "Blonde hair. Big boobs. Hell, she’s wearing a crop top with the word ‘SLUT’ printed on it."
    "Yes, it could only be her. Though I know I shouldn’t, I find myself walking towards that shady part at the back."
    "As I come closer, paying all my attention to her, I can see some slights of hand beneath the booth table she’s sitting at."
    "So...she not only plays accomplice in muggings, but she likes to dabble in drugs too?"
    "I’m not exactly a priest myself, but I don’t take kindly to seeing it either."
    "The idea of her making any sort of money off this makes me angry."
    "She doesn’t deserve it! She doesn’t deserve anything..."
    lexi.say "See you around."
    "I can just pick up on her farewell to the guy sitting there with her. He gets up carefully, and casually struts away with the good stuff in his pocket."
    "The seat opposite her seems free now, and I assume it’s for any potential buyer to take."
    "Well, I can be quite a good actor when I want to be. Maybe I ought to adopt that role."
    "Alternatively...I suppose I could just report her to one of the bouncers like a tattletale. Would be kind of lame, but at least it would mean she couldn’t rope me into anything."
    menu:
        "Approach her directly.":
            "I can’t be bothered with wasting time. I’d rather deal with this, right here and now."
            "I’m not the kind of guy who likes to wait around and hope. It’s better to face things head on, in my own opinion."
            "So I approach her table just like that, and sit down in the chair opposite her side."
            "For a moment she doesn’t seem to notice me, too busy fiddling around on her phone. I suppose I don’t stand out much, but still..."
            "I can’t wait to see how she reacts when she notices that it’s me..."
            "After a few more minutes, Lexi finally rolls her eyes, clicks her tongue and puts her phone down."
            "Only then does she look up, and her eyes quickly widen like saucers."
            hero.say "Hello again."
            "Oh, it feels good. Just seeing that flash of alarm on her face, however brief it might be, is immensely satisfying."
            show lexi date annoyed
            lexi.say "...Aw shit..."
            hero.say "You’re damn right ‘aw shit’. Don’t think I forgot what happened back there."
            if not game.get_flag_value("dannyvictory"):
                lexi.say "Calm down, it wasn’t nothin’ personal."
                hero.say "Oh? Nothing personal? Well sure, maybe it wasn’t. That would actually make sense."
                hero.say "What doesn’t make sense to me though, is how you can possibly justify telling me to calm down."
                hero.say "Bear in mind that you left me beaten and without any money. It wasn’t a good time having to cancel all my cards."
            else:
                if not game.get_flag_value("dannyvictory") > 1:
                    hero.say "Luckily I managed to stop things from going any further, but it was hardly a lot of fun."
                "Lexi leans back a bit and sighs."
                lexi.say "Yeah well...Danny knew to back off then."
                hero.say "I’m sure he did, wise choice."
                "It’s nice to actually feel like an alpha here."
                if not game.get_flag_value("dannyvictory") > 1:
                    hero.say "What’s really funny is that you still tried to call to me after doing that."
                    hero.say "Did you think I was going to forgive you?"
            show lexi date
            lexi.say "Look, I know you must be pissed off about what happened, but we all gotta make a living don’t we?"
            hero.say "Or you could, you know, get a job."
            lexi.say "I have a job."
            hero.say "And what’s that, dealing drugs?"
            "She quickly huddles over the table and glares at me, hissing through her teeth. I can see her tongue piercing glinting between them."
            show lexi date annoyed
            lexi.say "Are you insane!? What the hell are you tryin’ to do here!?"
            hero.say "Rat you out, maybe? I think it would be well deserved, considering the hell you’ve already put me through."
            lexi.say "Okay okay, look!"
            show lexi date
            "She leans closer, seemingly not caring that her boobs are practically popping out of that crop top."
            lexi.say "It’s either this, or the mugging. I don’t have a lot of options here, and less people will get hurt this way right?"
            hero.say "In the short term maybe..."
            lexi.say "Exactly. So cut me some slack."
            "I take my time, rapping my fingers against the table-top and observing her anxious face."
            "It feels nice to be holding all the cards here. She may have had the upper hand back in the alleyway, but right now I’m the one with the advantage."
            lexi.say "Will you? Will you please let me off just this once?"
            hero.say "...Why should I? What’s in it for me?"
            "She hesitates, and the corners of my lips curl upwards smugly."
            hero.say "Well? Please, I’m dying to know what my prize will be for all the effort."
            lexi.say "That’s...alright fine, I’ll blow you."
            "Now it’s my turn to be startled. I just about fall out of my seat when she so casually suggests it."
            hero.say "...I’m sorry...what?"
            lexi.say "You heard me. Let’s go to the bathroom and I’ll suck you off, no problem."
            hero.say "Um..."
            "I’m left speechless. I don’t quite know what to say to that."
            "I could accept it but...what if she tries to take advantage of me again?"
            "I’d rather that she didn’t steal anything from me, for example."
            "But I guess, if I keep my wits around me I might be fine."
            "All I really want is to get something back for what happened to me before."
            "Honestly...I feel like I definitely deserve it..."
            lexi.say "Well? You up for it?"
            menu:
                "Yes":
                    hero.say "...Fine. Fine, let’s go."
                    "I stand up along with her. She takes my hand firmly, and just like that I’m being tugged along with her."
                "No":
                    hero.say "Fuck off"
                    "Disgusted I leave her here..."
                    $ lexi.set_flag("story",100)
                    return
        "Tell someone else.":
            "Actually, approaching her straight up seems like a completely dumb idea."
            "I don’t know what Lexi herself is capable of, and if Danny comes out of the woodwork again, I’m totally screwed."
            "It’s far better for me to play it safe and let one of the staff members know."
            "Yes, it’s the lamer of the two options, but I’d rather do this than end up getting attacked again."
            "I scan the entrance to the nightclub for someone who seems good to notify."
            "There’s a pretty big looking bouncer there. I don’t think that even someone like big boy Danny would mess with him."
            "So, I walk over with a confident stride, fully committed then. If I end up having to pay some sort of consequence then so be it."
            "All I want to ensure is that Lexi doesn’t get to fuck me up and then walk away without any kind of punishment."
            hero.say "Excuse me sir-"
            unknown_girl_say "Oh! Sorry, sorry!"
            "I’m about to talk to the bouncer, he’s already half-turned to hear what I have to say, but I suddenly hear a girl calling out."
            unknown_girl_say "Don’t mind him, haha!"
            bouncer_say "Uh...can I help either of you?"
            show lexi date happy
            "An arm links around my own, and I look down to see none other than Lexi, clinging to me like some sort of drugged up koala."
            "She smiles up at me in a sickly sweet manner, and for once I’m more focused on her face than her chest."
            "So...this is a part of her plan then?"
            "I figure it out in my head, what seems probably at least. She must have seen me from the back and come rushing over to stop me from saying anything."
            "Guess she was a step ahead of me after all."
            hero.say "Hello...Lexi..."
            lexi.say "Hello babe, I’m so glad you could come!"
            "She grins at me, and I let out a heavy sigh. I don’t know what’s more insulting. The fact that she’s pretending to be my girlfriend?"
            "Or the fact that I’m just letting this happen..."
            bouncer_say "Look, I got work to do, so can you say what you were gonna say or leave?"
            "I pause, feeling her squeezing my arm all the more."
            "I guess that’s my warning."
            hero.say "Um...no it’s...it’s nothing. Sorry, sorry to bother you."
            bouncer_say "Whatever."
            "I back up along with Lexi, and we keep walking away until we’re in a quiet corner of the nightclub where nobody can really see us."
            "Only then does she let go of me and plant her hands firmly on her hips instead. The look in her eyes is deadly..."
            show lexi date angry
            lexi.say "What the HELL?"
            hero.say "I guess you figured me out. Just like I figured you out."
            lexi.say "Oh fuck off...you got no business bothering me!"
            hero.say "Kind of like how you had no business bothering me the other night?"
            "It feels good to actually say it to her. Call her out on it."
            if not game.get_flag_value("dannyvictory"):
                hero.say "Remember how I got beaten up by your boyfriend and left there without any money?"
                hero.say "Bet you would have stolen my clothes too if they were worth anything."
                "She sighs and looks down, tapping her foot."
                show lexi date annoyed
                lexi.say "Don’t be so annoyed. We all do things our own way, and that’s my way of doing things."
                hero.say "Right."
                "Well she sure goes about things in a bad sort of way then."
                lexi.say "Besides, you tried to kick him in the dick. Do you really think he was gonna let it slide?"
                hero.say "Screw me for using self defense right?"
                show lexi date
                lexi.say "...You should’ve just let us take your money, and you wouldn’t have ended up getting hurt."
                "Right. That’s a fair argument."
                hero.say "But then I would have never caught you dealing drugs, would I, Lexi?"
            else:
                hero.say "It’s a miracle I actually managed to get out of that mess."
                lexi.say "Oh yeah. Gotta thank you for kicking my boyfriend’s butt."
                "She scowls bitterly. I only tut."
                hero.say "I had good reason for doing it. He was threatening to kill me!"
                lexi.say "Yeah but he wouldn’t have! Hell, who do you think we are?"
                "I stare at her blankly."
                hero.say "Scum."
                "Never mind Danny, she looks fit to murder me for saying that."
                lexi.say "You better stop running your mouth!"
                hero.say "And you’d better stop selling drugs to people."
                lexi.say "-!"
            show lexi date annoyed
            "She shuts her mouth. Whatever she was planning on saying next, she seems to have abandoned the idea."
            "It’s nice to see her being quiet like this."
            "These are certainly interesting circumstances. I can see quite clearly, she’s very uneasy."
            "The other night, I was the one who was at a horrible disadvantage. Yet now, things have completely switched around, and I couldn’t be happier about it."
            hero.say "That’s right. Think carefully about your next move, because I’m not afraid to tell someone about this."
            show lexi date
            lexi.say "Alright! Alright alright, let’s just...let’s just take this slow..."
            hero.say "Take it slow? Why bother?"
            hero.say "I can just finish exactly what I already started before and tell that bouncer what I intended."
            "I can see hints of anger flickering in her eyes, but she seems to be urging herself internally to stay calm too."
            "I guess it’s only in her own better interest if she keeps her cool."
            lexi.say "...You’ll ruin me. I don’t have a lot of choices, come on!"
            hero.say "What do you mean by that?"
            show lexi date sad
            lexi.say "I mean...well...I mean look at me..."
            "Eyeing me, she runs her hands from her chest to her incredibly short skirt, showing off and amplifying her body all the more."
            lexi.say "In a meeting they’d take one look at me and kick me out on my ass."
            lexi.say "Even if I wanted to apply for a job there’s no way I would ever get it."
            "Admittedly, I can sort of see her point there. Though I suppose it would depend."
            show lexi date
            lexi.say "But when it comes to my body, it’s something I can use to lure in suckers like you and make a quick buck with Danny’s help."
            hero.say "Right. Yeah, I’m well aware of that now."
            "Even if I was partially drunk back then, I still feel like I was such an idiot for falling for it."
            lexi.say "Besides that...if I don’t want to trick other people, I have to do something like this. Stay under the radar."
            hero.say "If you’re trying to make me feel bad for you..."
            lexi.say "I’m not! But don’t you get it? It’s just how I gotta do things."
            "How she has to do things?"
            "If she didn’t dress up like a slut, literally, she might be able to land herself a decent job."
            "I know what a girl wears shouldn’t matter but...I don’t know if I can imagine seeing Lexi in an office cubicle."
            "I feel like she’d go insane in a place like that anyway."
            hero.say "Are you really that desperate to keep this hidden?"
            lexi.say "Of course I am! If I don’t, I’ll end up in jail."
            "Now there’s a place that I could see her fitting in."
            lexi.say "Please...please, I’ll give you something in return if you can keep this private."
            "I perk up a little bit when she suggests that."
            hero.say "And when you say ‘something’...you mean...what exactly?"
            "A sultry look immediately bleeds into her gaze."
            lexi.say "How about I blow you in the toilets here? You’ll love it, trust me. I am that good."
            "Hearing her say ‘trust me’ is ridiculous, but I find myself drawn in by the proposal anyway..."
            menu:
                "Yes":
                    "Just like that, I’m nodding my head. Agreeing."
                    "Maybe I actually do want this."
                "No":
                    hero.say "Fuck off"
                    "Disgusted I leave her here..."
                    $ lexi.set_flag("story",100)
                    return
    scene bg publicbathroom with fade
    "We sneak off toward one of the bathrooms, and she immediately pulls me into the cubicle at the far end of the room."
    "It’s not very classy, but at least it’s pretty clean. Small mercy, I guess."
    show lexi date
    lexi.say "Ok, now promise me before we start anything. I need you to make a deal with me."
    "Hesitating, I watch her uneasily until she speaks again."
    lexi.say "You won’t tell anyone, alright? Not a single person, or I swear I’ll be pissed!"
    "I blink a few times, before simply nodding to her."
    hero.say "Okay, fine, no problem."
    "It kind of is a lot to ask but...well I suppose I am getting something in return for my silence."
    lexi.say "Shake on it then."
    "She holds out her hand, and so I take it. It’s the first time we’ve touched each other properly."
    "Admittedly, it’s pretty nice. But we’re not here for this kind of thing."
    show lexi bj date
    "As soon as I finish shaking and pull my hand back, she gets down on her knees and reaches up for my belt."
    "Her fingers deftly work my belt loose, and soon she has my dick out of my boxers."
    "I lean back against the cubicle wall and hitch my breath, as if I’m bracing myself."
    "I’m looking forward to it but I’m also a little scared."
    "Maybe just because this is a first...and she did pretty much screw me over before..."
    show lexi bj suck
    "Yet the very moment her lips slip around the tip of my dick, I start to feel a twinge of pleasure."
    "It’s very pleasurable. Already I can feel myself starting to get into it, and things have only just kicked off."
    lexi.say "Mm..."
    "She lets out a moan, and I groan too, craning my head back and closing my eyes."
    show lexi bj deepthroat open
    "Her mouth slips further up towards the base of my dick, and I’m honestly quite surprised by how far she’s able to take it in."
    "I’m glad for it though."
    hero.say "Fuck..."
    show lexi bj suck closed
    "I can’t help saying it. She sucks me harder still."
    "It feels crazy good. My legs quiver and I bite my lip as she starts to quicken her pace."
    "Lexi blows me faster and faster, until finally she parts from my dick just in time for me to cum."
    menu:
        "Mess her face up":
            show lexi bj normal cum left
            "On a whim I grab her hair and prevent her from catching my jeez with her mouth, covering her face with it."
            lexi.say "Hey !!!!"
            hide lexi
            show lexi bj date facial left
            lexi.say "Fuck you messed up my make up moron!"
            hero.say "Serves you right."
            hide lexi
            show lexi bj date facial
            "For a moment we both stare at each other, but since I’m so weary it doesn’t feel awkward."
            "Lexi stands up then and wipes her face with the back of her hand."
            hide lexi
        "Let her do her thing":
            show lexi bj open cum
            "Deftly, she catches it all on her tongue..."
            hide lexi
            show lexi bj normal showcum
            "Then as if bragging she shows me her mouth full of my jizz..."
            show lexi bj swallow
            "...and swallows the lot..."
            show lexi bj smile
            hero.say "Fuck it's the most slutty thing a girl has ever done to me."
            lexi.say "Thanks."
            "For a moment we both stare at each other, but since I’m so weary it doesn’t feel awkward."
            "Lexi stands up then and wipes her mouth with the back of her hand."
        "Pull her deeper":
            show lexi bj left right
            "I decide to go all the way and grab her hair."
            show lexi bj deepthroat closed
            "I pull her face down on a forced deepthroat..."
            show lexi bj cum
            "And blow my load deep in her mouth."
            show lexi bj open
            "She looks up at me with teary eyes."
            hide lexi
            show lexi bj normal
            "For a moment we both stare at each other, but since I’m so weary it doesn’t feel awkward."
            "Lexi stands up then and wipes her mouth with the back of her hand."
    show lexi date cum
    lexi.say "So, we done?"
    "I take a moment to dab my own brow with my shirt sleeve, before nodding and pulling up my pants again."
    hero.say "Seems like it."
    lexi.say "Great! Well then, glad that’s sorted."
    "Admittedly, I feel a series of emotions, all mixed together."
    "On the one hand, it felt damn good, and I can’t deny that. She clearly knows exactly what she’s doing."
    "On the other...it almost feels like I’m still letting her off the hook too easily."
    "But after we shook on it, I’d feel like a douche to go back on that promise."
    hero.say "Yeah, fine."
    lexi.say "Hey now, cheer up honey. I gave you what you wanted."
    hero.say "Yeah, true."
    "She grins at me, seemingly unfazed. It was definitely too easy for her."
    lexi.say "Yep. There’s your night to remember."
    hide lexi
    if hero.money > 500:
        $ hero.money -= 500
    else:
        $ hero.money = 0
    "She leaves me there, and I let out a sigh."
    "Like instinct, my hand goes for my pocket. And as I suspect...she took it."
    "My wallet."
    hero.say "...Dammit."
    return

label lexi_event_02:
    if "lexi" in HIDDEN:
        $ HIDDEN.remove("lexi")
    $ lexi.set_flag("nodate",False)
    $ lexi.set_flag("nokiss", False)
    $ lexi_love_max = 200
    $ lexi.set_flag("story",2)
    $ lexi.set_flag("sex",1,"permanent","+")
    play sound "sd/cell_vibrate.mp3"
    $ hero.smartphone_contacts.append("lexi")
    pause 1.0
    "Somehow, when I see the ‘Unknown’ number flashing up as my phone buzzes, I already know who it’s going to be."
    "Lexi. Without a doubt."
    "Turns out, I’m right."
    hero.say "You’ve got some nerve calling me after stealing my shit."
    lexi.say "Oh boohoo, at least I bothered, right?"
    hero.say "Yeah, and right now I’m bothering to cancel my credit cards-"
    "I glance back at the laptop screen, tapping away on the keyboard with one hand."
    "The only other light besides the blue is my desk lamp."
    hero.say "-So have fun with that."
    lexi.say "Look, whether you cancel them or not doesn’t matter. I never used ‘em."
    hero.say "..."
    "I’m prompted to pause when she says that. It doesn’t make sense, why bother stealing my wallet if she isn’t going to try and run my bank balance dry?"
    hero.say "...What’s the matter, too scared of getting caught?"
    lexi.say "I’m not scared of anything! I just...I decided against it."
    hero.say "Oh how noble. A sudden change of heart."
    lexi.say "I ain’t a bad person."
    hero.say "Uh huh. Yeah, just a slutty drug deale-"
    lexi.say "HEY."
    "I can tell by her tone that she’s suddenly dead serious. It actually makes me flinch a bit."
    hero.say "...What??"
    lexi.say "Don’t. Call. Me. A. Slut."
    hero.say "Fine, fine."
    lexi.say "And we put the drug business behind us when I sucked you off too."
    hero.say "Well, that was before you stole my wallet."
    lexi.say "So what, you holdin’ a grudge now?"
    "I roll my eyes and sigh down the phone from my end."
    hero.say "Yeah, and rightfully so, wouldn’t you say?"
    lexi.say "..."
    "There’s a long pause from her side."
    "I guess I stumped her with that one."
    lexi.say "...Can you at least...let me come over?"
    hero.say "Excuse me?"
    lexi.say "I mean I know where your address is now. It’s written in your wallet."
    "Fuck!"
    "I guess she knows too much about me now. Dammit..."
    hero.say "Why would I...let you come to my house?"
    lexi.say "Well...so I can give your wallet back."
    hero.say "The hell? Are you serious?"
    "She can’t be..."
    lexi.say "I am. And you can’t say no to me."
    hero.say "...And why is that?"
    lexi.say "Hah! Cuz I’m already there!"
    "At first I don’t understand. Then I put two and two together."
    hero.say "...You’re joking, right?"
    lexi.say "Cul de sac for rich people...stupid comedy doormat that says ‘LEAVE’? Ring a bell, asshole?"
    "It does."
    lexi.say "Look out your damn window."
    hero.say "Charming. Alright-"
    "I go to do just that, and as I pull my blinds open, I look down to see her on the street below."
    "A top that might as well be a bra, ridiculously short shorts, and a thong poking out on either hip."
    "Yeah. It’s definitely Lexi."
    "She seems to notice me, and waves using the phone, giving me a shit-eating grin."
    "Well. Great."
    hero.say "...I’ll be right here."
    "Bitterly, I go to the front door and let her in."
    show bg kitchen
    show lexi casual
    with fade
    "Once she does, I lead her inside to my kitchen area, scowling all the way."
    "After we reach my kitchen I lean against the island and mentally prepare myself."
    "Just in case she starts arguing with me again..."
    lexi.say "Ooh, so you’re rich enough to afford a house? Maybe I should have taken your cards after all..."
    hero.say "Ahem."
    "I catch her attention with a cough and hold my hand out expectantly."
    hero.say "Hand it over."
    lexi.say "Hah. Fine, relax-"
    "She actually does it, and I take my wallet back with some relief."
    "Good. At least that’s a weight off my shoulders. Big time."
    "I check inside to make sure, and then look back at her."
    hero.say "Looks like everything’s there."
    lexi.say "Would I lie to you?"
    hero.say "Yes. 100%%, yes."
    lexi.say "Well, you got it back anyway. And...that should mean there are no hard feelings between us now?"
    "I let out a heavy sigh, tempted to yell at her."
    "Is she just delusional? Why does she assume that everything is suddenly going to be alright?"
    hero.say "...Do you have some other reason for coming here?"
    "I’m just about ready to smack my forehead off the edge of the counter, but her honest look catches me off guard."
    "She actually looks kind of...sad? Just for a moment, but I notice it."
    show lexi casual sad
    lexi.say "Well I...wanted to explain a few things. Y’know, like I don’t really mean to do that kind of shit, I just have to."
    hero.say "And by ‘shit’ I’m guessing you mean the whole robbing people thing?"
    lexi.say "And the drugs too..."
    hero.say "I thought we weren’t going to talk about those."
    lexi.say "And we ain’t! But..."
    "Her momentary defensiveness fades away again, and she seems to shrink even further."
    hero.say "...Just sit down. Want something to drink?"
    lexi.say "Yeah, got anything strong?"
    "As soon as I suggest it she immediately sits down like she owns the place, and I wonder if I’ve made some sort of grave mistake."
    "Well...no turning back now, I guess."
    hero.say "Let me check."
    "Soon enough I pour us both some wine, and she laughs, picking up her glass and examining it."
    show lexi casual happy
    lexi.say "Wow. You really are a posh boy."
    hero.say "Why? Because I have a nice house I worked for, and I drink wine?"
    "Screw me for trying to be a good host."
    lexi.say "Ugh, it’s whatever."
    lexi.say "Anyway...how’d you afford a life like this?"
    hero.say "I mean...I worked for it, just like anyone else."
    hero.say "Except you, I guess. You love your shortcuts, right?"
    show lexi casual sad
    "She grimaces."
    lexi.say "Told ya, I got no choice in it. So..."
    "Again, she goes quiet and just focuses on drinking for a moment."
    "I figure I’m as well doing the same, and the atmosphere becomes pretty awkward between the two of us."
    lexi.say "...It’s...just that I have no choice."
    hero.say "Humans have free will, don’t we? So how can you not decide for yourself?"
    show lexi casual angry
    lexi.say "Because!"
    "She suddenly snaps her head towards me."
    lexi.say "I owe somebody a debt, so it isn’t that simple!"
    hero.say "Who?"
    lexi.say "...Remember that big guy who nearly killed you in the alley? Danny? My boyfriend?"
    "‘Nearly killed’ me, eh? Well...at least she’s acknowledging it now."
    hero.say "Yeah, kinda hard to forget someone like him."
    show lexi casual sad
    lexi.say "Well, he’s a gangsta. I owe him a debt too, his whole gang really, so I gotta...obey him otherwise..."
    "Judging by the way she trails off then, I decide not to press for details. But I do need to know a bit more about this."
    hero.say "Right...and that’s why you’re doing all of this?"
    lexi.say "...Basically. I mean, I’m just fucking tired of it."
    "She downs the rest of her wine in one go and slams the glass down. I wince."
    hero.say "It’s not a shot Lexi. Anyway, I’m sorry you’re in that position but..."
    hero.say "...It doesn’t change what you’ve already done."
    lexi.say "Yeah, I get it, I suck. Relax."
    "I mean if she’s referring to what happened in the bathroom..."
    lexi.say "At least now you know why I’m doing these things."
    hero.say "..."
    "Taking a moment to pause and think it all over, I can’t bring myself to actually get mad at her."
    "I guess...maybe I feel kind of bad for her? It’s easy to just blame her for all of this but...she had her reasons I guess."
    hero.say "Okay...fine."
    "She looks up at me hopefully, and I give in entirely."
    hero.say "We can let bygones be bygones and...move on from this."
    show lexi casual happy
    lexi.say "Really!?"
    "Lexi perks up in an instant."
    hero.say "Yeah really. Just...don’t pull anything like that again, please."
    lexi.say "Deal. Thanks for listening to me."
    "I’m surprised by just how nice and open she’s being."
    "Of course, it could turn out to all be deception but...I can’t help but trust her."
    "Plus when she’s not being so bitchy she actually looks really quite attractive."
    show lexi casual blush
    lexi.say "Hmm...hey, woah-!"
    "Something suddenly catches her eye as she turns to look out of the sliding glass doors."
    "I’m guessing she spotted the pool. The lights just turned on a few minutes ago."
    lexi.say "You have a swimming pool!?"
    hero.say "Yeah uh...it came with the house. Might need to be cleaned, I haven’t used it in a while."
    scene bg pool
    show lexi underwear
    with fade
    "That lie doesn’t seem to phase her, she just rushes to the doors anyway and slides them open."
    "They bang and I cringe again. Doesn’t she know how to treat other people’s property?"
    hero.say "Lexi, hold up!"
    "I hurry after her, and rush through the open door."
    "She’s already standing at the edge of the pool, looking down into it eagerly."
    "That and...she’s pulling off some of her clothes."
    show lexi naked blush
    "She’s not wearing many, so it won’t take long before I have a naked chick hanging around in my garden."
    hero.say "Lexi could you just wait a minute!?"
    "Not listening to me, even still, she pulls off her bra and panties and dives into the water with only a little grace."
    "I end up getting splashed a bit considering I bothered to run over and try to stop her."
    hero.say "..."
    "Lexi turns in the water partially after surfacing again, and grins at me devilishly."
    "Before I can use my arms as a shield (or get a proper look at her body), she splashes some water right into my face."
    "I end up with a soaked shirt too, and I groan after wiping the droplets out of my eyes."
    hero.say "...Really?"
    lexi.say "Lighten up and join me! All the heavy shit is out of the way now, right?"
    "I guess so..."
    "And now that I can actually see her properly, it’s hard not to notice."
    "The water distorts her figure a little bit below the torso, but I can still see her pretty clearly thanks to how still it is now."
    "Her body is...gorgeous. I can’t deny it."
    "Her chest is ample, and it tapers nicely into a full set of hips as well. She’s slender and curvy in all the right places."
    "I guess I could have anticipated this, considering the kind of clothes she wears don’t typically hide anything. But..."
    "Seeing it in full...is really something."
    lexi.say "Hey, stick your tongue back in your mouth, perv."
    hero.say "Excuse me?"
    "She chuckles and swims to the edge of the pool, folding her arms and resting her chest against the edge."
    "I can see her breasts pressing up together, dripping with chlorinated water."
    "It’s...inviting, frankly."
    lexi.say "Interested? Why don’t you join me?"
    lexi.say "I mean, it’s not like you have anything to worry about this time. You can’t take your wallet in the pool."
    "True."
    "Well...maybe I should."
    "Or...should I?"
    menu:
        "Join her":
            "Going for an early night swim with a hot girl?"
            "I guess any sane person would say ‘yes’."
            "So without really giving myself any more room for hesitation, I take off my clothes and slip into the water with her."
            "Yes...I’m completely nude."
            "And she just stares at me."
            "Stares and stares..."
            lexi.say "Wow...you actually did it."
            hero.say "Well...I figured it was better than just standing around awkwardly until you get out."
            hero.say "And dressed."
            lexi.say "Well I’m impressed. So..."
        "Go back inside":
            "...I’m not an idiot."
            "Lexi may have had the courtesy to bring my wallet back, but what she’s doing right now just makes it seem like she’s playing some kind of game with me."
            "So I’m not going to bite the bait."
            lexi.say "Hey, aren’t you gonna come in?"
            hero.say "Yeah, no thanks-"
            "I walk past the edge of the pool, aiming to head back inside and just drink the rest of that bottle."
            "I guess I don’t account for just how close to her I am."
            "Her wet hand snakes out of the water and suddenly grasps my ankle, tugging it sharply and yanking me right over."
            hero.say "GAH!"
            "She’s lucky that I end up landing in the water."
            "Not smacking my head off the concrete."
            hero.say "Fuck! What the hell!?"
            "I snap at her as soon as I’m above water again, and she looks over at me with a smug grin."
            lexi.say "Trust me, you’re gonna wanna say yes to me tonight."
            "Before I can say a word in response, she comes closer."
    "Lexi doesn’t waste time. I feel like I’m in the nightclub toilets again as she presses up against my front."
    "Those same tits are right up upon me now. Yes...they’re great."
    "I’d be one stubborn idiot if I didn’t admit that."
    "My hands drift down to her sides and grip them gently."
    "Under the water, her skin feels even warmer."
    "I guess it is pretty fancy...having a heated pool."
    lexi.say "Heh..."
    "Her own hands start to feel my body, tracing down what seems like every single inch of my skin."
    "Soon enough, they seal around several other inches too, and start to rub away even in the water."
    "I lean back and close my eyes, resting both elbows against the side of the pool."
    "I figure she’s not going to suck me off underwater, so this is definitely going to be different from before."
    "But...am I really ready for things to go further?"
    "Well...I guess...there’s no turning back now."
    lexi.say "Look at you...you’re already getting hard."
    "She grins up at me, before I can feel her hand slip away."
    "Lexi rests against the other side just by me, and shows off her figure for me."
    "I can see her standing with her legs spread a little, like she’s just waiting for me to lift them and pull her close."
    "Yep...definitely no turning back now."
    hero.say "..."
    "I wade the few steps it takes to reach her, and reach under the water’s surface again, my hands slipping to her ass cheeks and giving both of them a firm squeeze."
    "Using my reasonable strength, I hoist her up and spread her legs a little more."
    hide lexi
    $ CONDOM = False
    if hero.has_condom():
        menu:
            "Use a condom":
                $ c = " vag-condom"
                $ hero.use_condom()
                $ CONDOM = True
            "Do it raw":
                $ c = " vag"
    else:
        $ c = " vag"
    if not persistent.xray:
        $ c = ""
    show lexi stand pool
    "Partially submerged along with her, I push my dick up inside of her waiting pussy."
    lexi.say "Haa-!"
    "Immediately she yelps. I’m already rigid."
    "That only serves as a cue to make me shove in further and firmer."
    "I can tell by her reaction that she loves it."
    "I push in even more, and start to slip in and out of her steadily."
    "Just like that, we’re gyrating and moving in tandem with one another, the warm water splashing and shifting around our naked bodies."
    "It’s times like this that I’m grateful for having such a private garden."
    lexi.say "Ha...harder!"
    hero.say "Nn-"
    "I grunt and obey, picking up the pace, not holding back."
    "Her body starts to become more and more heated, her walls closing in around my length."
    "I close my eyes just like I did when she jacked me off earlier."
    "Things grow more and more intense."
    hide lexi
    show expression "lexi stand pool ahegao"+c
    "Eventually, it seems that both of us hit our respective peaks, and with one final shudder, I orgasm inside of her."
    "It seems like my hot load triggers a burst of pleasure for her too, and she gasps sharply."
    lexi.say "Ahh~!"
    "That’s the ticket. I can feel her cum mingling in the water with my own, as I pull out and calm down."
    lexi.say "Y...you pulled out too quick-"
    hero.say "My bad."
    hide expression "lexi stand pool ahegao"+c
    "Honestly, I don’t think I’ve ever been with a woman like this."
    "It’s like it was too much. I hit my peak so quickly, and I’ve never been like that before."
    "Maybe it’s just that...this was so unexpected."
    "Actually fucking a girl like Lexi, in this setting too."
    "...How could I have anticipated this?"
    "Actually...how could I have anticipated any of this?"
    "Even after she leaves, looking smugly proud of myself, I get this strange feeling."
    "Like I don’t want her to go."
    if not lexi.get_flag_value("pill") and not lexi.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills):
        $ lexi.set_flag("pregnant",1)
    return

label lexi_pregnant_flag:
    $ lexi.set_flag("pregnant",1,mod="+")
    return

label lexi_fuck_date:
    scene bg bedroom1
    $ lexi.set_flag("sex",1,"permanent","+")
    "Lexi glances around my room. I can’t tell if she’s looking for something to pawn off, or judging me by my tastes."
    hero.say "So, what do you think?"
    lexi.say "Shucks, [hero.name]!"
    lexi.say "I’m just ready for a wild time, and you got a nice bed."
    $ drugs = False
    $ preg = False
    if lexi.get_flag_value("pregnant") >= 9:
        "She rubs her hand underneath her pregnant belly, sticking out of her short top."
        "Even after I knocked her up earlier, she didn’t want to change her wardrobe."
        "That’s fine."
        "It really shows how trailer trash she is, and that’s why I like her."
        "Immediately, she turns to me, grabbing my crotch and pressing her chest up against mine."
        "Her swollen breasts poke at my body, and I feel a tiny squirt of moisture on my shirt."
        lexi.say "So, why don’t you and I get more comfortable?"
        $ preg = True
    elif "drugs" in hero.inventory:
        menu:
            "Offer drugs":
                $ drugs = True
                $ lexi.love += 5
                $ hero.lose_item("drugs")
                "I chuckle as she gropes me, but I pat her on the cheek, looking over towards my bedside table."
                hero.say "Now, hold on there, Lexi. There’s something you’re probably going to want to see in that drawer first."
                "Lexi quirks an eyebrow and pulls herself away from me a moment."
                "She sways off and bends down, her short shorts unable to hide her booty as she bends over to look in the drawer."
                lexi.say "Oh fuck, [hero.name]!"
                "She gasps, pulling out the bag I had in my drawer."
                lexi.say "When the hell did you get this!?"
                "Thought a girl like you would like a little extra excitement."
                "Shucks, you’re a big time party animal now, [hero.name]. Quick, get me a credit card or something, fast!"
                "I hand her the card and she sits on the bed, quickly lining up the powder just right."
                lexi.say "It’s been too fuckin’ long since my last hit!"
                lexi.say "Danny never let me try the product, not without fuckin’ someone first."
                hero.say "Well..."
                hero.say "You are going to be fucking me, so..."
                lexi.say "Oh, shut up, you!"
                "She rolls up a dollar bill to the perfect consistency."
                "She takes in a nice, big snort, and immediately her eyes roll back."
                lexi.say "Oh, fuck me that’s good shit!"
                lexi.say "It’s gonna get really fuckin’ hot in here in a hot minute, [hero.name] You want a hit?"
                menu:
                    "Accept":
                        $ lexi.love += 1
                    "Reject":
                        hero.say "Nah..."
                        hero.say "I want remember how fucked up you are without fucking myself up."
                        "I say as I sit there, waiting for her to continue."
            "Don't":
                pass
    "She leads me over towards the bed and immediately lifts her top up off of her."
    if preg:
        "Who would have ever thought that the drug dealing con artist would ever have the curves of motherhood—the full breast, the baby bump."
        "It suits her well, though I’ll no doubt end up being the responsible parent."
        "Wasting no time, she undoes her shorts and shimmies out of them and her thong, leaving herself naked."
        "It takes her a little longer than she normally does, but that comes with the territory of the added baby weight."
    lexi.say "Well, come on."
    lexi.say "Don’t waste my time now."
    if preg:
        lexi.say "Let me see that dick that done knocked me up."
        lexi.say "Just cause I got a baby on board don’t mean I don’t crave a taste!"
    if drugs:
        lexi.say "Haha, okay! Well, I’m gonna devour that dick!"
        "Her eyes are wide and filled with lustful hunger."
    "I get out of my own clothing really quickly and lay naked on my bed."
    "She smirks as she climbs down onto her knees in front of me."
    show lexi bj naked bedroom nodick
    "She sighs as she lowers herself, nodding once she’s all settled into position."
    if preg:
        lexi.say "Whoo... not as easy as before, [hero.name] and that’s all yer fault, daddy."
    "All I can see of her between my legs is her smiling face."
    if preg:
        lexi.say "Alright, [hero.name], They say there’s strange cravings when a gal is bred, and I’m hankerin’ for some of this dick of yers!"
    hide lexi
    show lexi bj bedroom naked
    "She snickers and then leans in, rolling her tongue out and licking up along my shaft."
    show lexi bj suck
    if drugs:
        "It’s incredible how fast she can lick me, going over my shaft over and over again, as if I was a popcicle in danger of melting."
        "She growls and gasps with each lick, acting like a wild animal, hungry for more!"
    "I groan, letting her have her fun for now."
    "She keeps her hands away from my cock, instead holding onto my thighs and just wrapping her lips around my flesh."
    show lexi suck closed
    "The feeling is wonderful as she bobs her head up and down, sucking gently upon my skin as she slides her lips and tongue along my body."
    if not drugs:
        "Damn, she’s not doing anything crazy, but just with her technique she has and the look she gives me, it’s enough to make me explode."
        "But I can’t let it end without me doing anything, can I?"
    else:
        show lexi deepthroat closed
        "Damn, the way she’s going at me like a jackhammer is bound to make me explode sooner than later."
        "There’s no way I’m letting this coked up slut make me finish now, is there?"
    $ cum = ""
    menu:
        "let her finish":
            "She’s already doing a great job."
            "I should just let her keep going."
            if not drugs:
                "She hums as she pulls her mouth free from my cock, just at the perfect moment."
            else:
                "She growls as she pulls free from my cock just at the perfect moment, her crazed expression staring up at mine, revealing a slight sadistic glee as she stares back up at me."
            "I gasp, unable to hold back."
            show lexi bj normal open
            "She knows exactly when to finish a guy off, and I lift my hips just slightly, unable to control myself as I explode all over her face!"
            hide lexi
            show lexi bj bedroom naked facial
            if not drugs:
                "She squeals as my hot cum coats her, dribbling down along her cheeks and chin."
                "She snickers and then leans in, placing another kiss on my cock."
                lexi.say "Oh, yeah, you’re a real stud—a real animal [hero.name]."
                if preg:
                    "But just because you shot true with me before, daddy, don’t mean I don’t want it, so you’d better be ready for the next round!"
            else:
                "She squeals as my hot cum coats her, and then laughs, giggling like an idiot as she rubs her fingers over her cum-soaked face."
                "Her eyes roll back, her face plastered with a maniac smile as she revels in her cum-drenched face."
                lexi.say "Oh, fuck yes!"
                lexi.say "I’ve never felt more alive! Come on, stud. Finish me off!"
            $ cum = "cum"
        "take control":
            if not preg:
                "Oh, she think she can be the only one who can steer this relationship?"
                "She has another thing coming!"
            else:
                "Sorry, Lexi, but you lost control when I knocked you up."
            show lexi bj left right
            "I grab her by the hair and she gasps, closing one eye and looking up to me with a surprised gurble."
            "I’m close—I can tell she has been planning to finish me off, but she’s not going to finish without giving me a real gift!"
            menu:
                "Time to let her have it!":
                    show lexi bj deepthroat open
                    "I pull her in, and she squeals around my cock as I bring her up to my crotch."
                    "Her cheeks puff out and her throat bulges as my dick slams deep into her throat."
                    if drugs:
                        "Her eyes roll back, and in her drug-crazed stupor, she seems to be delivered to another world of pleasure as I release, shooting globs down deep into her."
                    show lexi bj cum
                    "Once I finish, we hold on there together for a bit, and I let go of her."
                    if drugs:
                        "She pushes herself free, gasping, coughing, spitting up some of my jizz as her whole body trembles from the excitement and energy from the stimulant coursing through her."
                    hide lexi
                    show lexi bj bedroom naked
                    lexi.say "D... damn!"
                    if not drugs:
                        "she gasps, rubbing her neck."
                        lexi.say "You sure are rough...!"
                    else:
                        lexi.say "I really am trash to you? I love it!"
                    $ cum = "cum"
                "Maybe I should pace myself?":
                    if not drugs:
                        "She looks up to me with pleading eyes, wondering what I’m going to do with this newfound control."
                    else:
                        "She looks up to me with hyperfocused and shaking eyes, wondering what I’m going to do with this newfound control."
                    show lexi bj normal
                    "I show her, pulling her head free from my grasp."
                    "She gasps once she has the air and pants, her chest rising and falling as she scans my eyes for an answer."
                    "She grits her teeth when I can’t give it to her right away, her whole body a jittery mess in my grasp."
                    "She’s eager for more before her crash, but we’re not playing on her time."
                    "I smirk at her."
                    hero.say "We’re not done yet, miss."
                    hero.say "No way I’m wasting myself on your throat today."
                    if preg:
                        hero.say "You know damn well where I like to cum, ‘mommy’."
    scene bg bedroom1
    show expression "lexi naked "+cum
    if cum and not hero.fitness >= 50:
        "My eyes get heavy, and a sudden rush of weariness takes me."
        "Falling back on the bed, I sigh out with a satisfied, yet tired breath."
        if not drugs:
            lexi.say "H-Hey, [hero.name]. You aren’t tuckered out are ya!?"
            lexi.say "Shucks that’s all you can handle?"
            lexi.say "Damn, and here I thought you could take me all the way."
            lexi.say "Guess I’ll see myself out, then!"
        else:
            lexi.say "H-Hey, [hero.name]!"
            lexi.say "No, don’t fall aslseep on me already!"
            "she groans, wrapping her arms around herself."
            lexi.say "Fuck, man, I’m still riding high."
            lexi.say "You can’t leave me hanging like this."
            "She collapses on the bed as I drift off."
            "I can hear her touching herself, groaning in frustration as I drift off into the land of dreams."
            $ lexi.love -= 5
        $ lexi.love -= 5
        return
    $ CONDOM = False
    if hero.has_condom():
        menu:
            "Use a condom":
                $ c = " vag-condom"
                $ CONDOM = True
                $ hero.use_condom()
            "Do it raw":
                $ c = " vag"
    else:
        $ c = " vag"
    if not persistent.xray:
        $ c = ""
    "I snicker."
    hero.say "Oh, no, we’re definitely not done yet."
    hero.say "You’re my whore all night long tonight!"
    "She giggles at that , slapping me on the thigh."
    if preg:
        lexi.say "Great! Now, how you gonna treat me, the momma of yer child?"
    if drugs:
        lexi.say "I’m yer crack whore!"
        lexi.say "Now, let me pay you off!"
    "I stand up , grabbing her by the arm, yanking her up so she stands with me."
    "I then spin her around, placing my hands upon her hips and whispering to her."
    hero.say "I’m going to use you however I want, for as long as I can handle."
    if not drugs and not preg:
        lexi.say "Oh, [hero.name], come on and show me how a real man fucks a woman!"
    elif drugs:
        lexi.say "Ah, come on! Stop teasing me! I’m so fucking hot, I can’t stand it!"
    elif preg:
        "She winces a moment, but smirks."
        lexi.say "Ah, not even gentle to yer kid?"
        lexi.say "Love that reckless shit. Come on and play with your favorite baby oven!"
    show expression "lexi naked "+cum
    show expression "lexi stand grope "+cum
    "Her thighs take my dick like they were hungry for it."
    "She shudders as my cock kisses her sex."
    if preg:
        lexi.say "Not worried about getting the baby all messy?"
        hero.say "Oh, don’t you worry about that."
        "I Pull back just a bit to get the right angle."
        hero.say "It’s perfectly safe for me to fuck you up until your water breaks, and I intend to take advantage of that the whole nine months!"
    elif drugs:
        lexi.say "Yeah, yeah! Come on, fucker! Fuck me right now!"
    else:
        lexi.say "Oooh, You’re... you’re gonna put it in now?"
    hero.say "I thrust inside, letting her dripping wet pussy suck me in."
    "She moans, squirming as I spread her and pump into her."
    if preg:
        lexi.say "[hero.name], yer so rough! Fuck me harder til my water bursts all over yer dick!"
    elif drugs:
        lexi.say "Ah, fuck, [hero.name], what is this weak shit!"
        lexi.say "I need a better high than this! Harder, harder!"
    "I do it, but only because I want it."
    "Soon, she’s bouncing on my cock, her breasts jiggling in large, sloshy movements, her messy face contorted into a mask of delight."
    "Her body is quite warm already, sweat glistening her body in such a wonderful sheen."









    menu:
        "Choke her":
            "She may be in my bedroom now, but Lexi’s a bitch, through and through."
            "I think about all the shit she put me through, and decide now that we’re together, I can get a little payback."
            if not drugs:
                lexi.say "Well, [hero.name]"
                lexi.say "what are you going to gaah!?"
            else:
                lexi.say "Dammit [hero.name]!"
                lexi.say "Are you just gonna’ sit there are are ya gonna do some-acck!"
            show expression "lexi stand choke "+cum
            "My hands move up along her body, fingers wrapping around her throat."
            if not drugs:
                "She shudders, quick breaths passing through her windpipe as I hold her down tight."
            else:
                "She croaks and squirms, her eyes rolling back as she grips onto me, digging into my flesh."
                "What rush must she be feeling now, knowing that I give her the thrill of air loss."
            if preg:
                "Even as I get the sick joy of this dangerous thrill, I can’t think about all the things she’s done to me."
                "Instead, I see her rounded belly and all I can think of is the life inside her, the one that hasn’t made her mistakes and doesn’t deserve to be hurt."
            elif drugs:
                "She struggles underneath my grasp, but with little laughs escaping the gasps and gurgles that she has."
                "At first, I wonder if I'm just imagining it, but when she grabs my cock and furuiously jerks it, I know I have to keep going, but is this all I had left in me?"
            else:
                "She squirms underneath my touch, her thighs rubbing along my cock, giving me a nice jerking off, even though she can’t bend down to stroke it."
                "The little gasps and gargles from her fill me with so much more desire."
            "I let go and give her a quick kiss on the cheek."
            hero.say "That’s enough of that for now,"
            "She gasps, falling forward a bit, but I catch her."
            if preg:
                "She sighs and nods."
                lexi.say "Shame... though after I pop this bundle out of me, you’d better choke me good, won’t you?"
            elif drugs:
                lexi.say "Either my heart’s gonna explode or you’re gonna choke me out!"
            else:
                "She coughs, sputtering up some drool before she wipes it off, wheezing."
                lexi.say "D... damn, [hero.name] what more can you do to me!?"
            hero.say "Is it too much?"
            lexi.say "Fuck that."
            lexi.say "what more are you gonna do to me!? Live fast, die young! What’s next!?"
            "Looks like you’ll find out..."
        "pull her hair":
            show expression "lexi stand pull "+cum
            "I move my hands up along her body and get good handfulls of those golden locks."
            "She tilts back as I yank on her, her chest poking out."
            "I know she likes to be handled roughly."
            if drugs:
                "Pain is just another form of pleasure just like drugs, isn’t it?"
            "She moves her hands back down to my waist, holding onto me as I yank at her, and I say."
            hero.say "You’re mine, got that?"
            "She nods, wincing when her hair tugs at her scalp."
            if not drugs:
                lexi.say "Do whatever you want to me... I’m your plaything!"
            else:
                "Her mouth opens as if she wants to say something, but she can only make her excited screams of pure hyped up delight!"
    menu:
        "Cum inside":
            show expression "lexi stand grope ahegao "+cum+" "+c
            "Both of us groan as we feel the pleasure welling up within us."
            "Soon, I release, sending my seed deep inside of her body."
            if drugs:
                "Lexi’s eyes roll back and she collapses her whole weight upon me, groaning as she crashes from the end of her high and the climax I gave her."
            elif not preg:
                "Lexi coos as she falls back on me, content that I have bred her."
            else:
                "Lexi coos as she falls back on me."
            hide expression "lexi stand grope ahegao "+cum+" "+c
            if not lexi.get_flag_value("pill") and not lexi.get_flag_value("pregnant") and not CONDOM and (randint(1,3) == 1 or "hung" in hero.skills):
                $ lexi.set_flag("pregnant",1)
        "cum outside":
            show expression "lexi stand grope ahegao "+cum
            "With one final groan, I shoot my load, unable to hold back any longer."
            "Lexi lays back against me, spreading her thighs and admiring the cumstains that soak her."
            hide expression "lexi stand grope ahegao "+cum
            scene bg bedroom1
            show lexi naked
            if not drugs:
                lexi.say "D... damn, [hero.name]."
                lexi.say "You lasted for awhile."
                lexi.say "I’m impressed!"
            else:
                lexi.say "Haa... imagine if ya took some yerself. Fuck, you’d be spurtin’ even farther, I’d bet. Whooo!"







    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
