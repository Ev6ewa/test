init python:

    Event(**{
        "name":"shiori_init",
        "label": ["shiori_init"],
        "priority": 1000,
        "girls_conditions": {"shiori":{"flag_story":False}},
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "shiori_start",
        "label": ["shiori_start"],
        "priority": 500,
        "duration": 0,
        "game_conditions":{"done":"shiori_teaser", "flag_female":0},
        "do_once":True,
        })

    Event(**{
        "name": "shiori_pregnant_flag",
        "label": ["shiori_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"shiori":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "shiori_give_christmas",
        "label": ["shiori_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"shiori":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "shiori_give_birthday",
        "label": ["shiori_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"shiori":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "shiori_give_valentine",
        "label": ["shiori_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"shiori":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name":"shiori_scold_1",
        "label": ["shiori_scold_1"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":20}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "do_once":True,
        "once_day": True
        })


    Event(**{
        "name":"shiori_coffee_1",
        "label": ["shiori_coffee_1"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":30}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "do_once":True,
        "once_day": True
        })

    Event(**{
        "name":"shiori_scold_2",
        "label": ["shiori_scold_2"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":80}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "done":"shiori_scold_1", "flag_female":0},
        "do_once":True,
        "once_day": True
        })

    Event(**{
        "name":"shiori_scold_3",
        "label": ["shiori_scold_3"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":60}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "done":"shiori_scold_2", "flag_female":0},
        "do_once":True,
        "once_day": True
        })

    Event(**{
        "name":"shiori_scold_4",
        "label": ["shiori_scold_4"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":80}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "done":"shiori_scold_3", "flag_female":0},
        "do_once":True,
        "once_day": True
        })

    Event(**{
        "name":"shiori_scold_5",
        "label": ["shiori_scold_5"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":100}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "done":"shiori_scold_4", "flag_female":0},
        "do_once":True,
        "once_day": True
        })

    Event(**{
        "name":"shiori_coffee_2",
        "label": ["shiori_coffee_2"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":110, "flag_coffee":1}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0, "done": "shiori_coffee_1"},
        "do_once":True,
        "once_day": True
        })


    Event(**{
        "name":"shiori_office_bj",
        "label": ["shiori_office_bj"],
        "duration": 0,
        "priority":100,
        "girls_conditions": {"shiori":{"valid":True,"room":["personal","office","breakroom"],"min_love":120}},
        "game_conditions": {"activity":["work","workhard","work_personal","workhard_personal"], "done":"shiori_scold_5", "flag_female":0},
        "do_once":True,
        "once_day": True
        })

    Event(**{
        "name": "shiori_kiss_me",
        "label": ["shiori_kiss_me"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"shiori":{"min_love":150,"present":True, "valid":True}},
        "game_conditions":{"flag_female":0, "chances":20},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "shiori_preg_talk",
        "label": ["shiori_preg_talk"],
        "duration": 0,
        "girls_conditions": {"shiori":{"flagmin_pregnant":6, "flag_toldpreg":False, "present":True}},
        "game_conditions":{"flag_dateinprogress":False, "flag_female":0},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "shiori_investigation_callback",
        "label": ["shiori_investigation_callback"],
        "game_conditions": {"hours":(9,22)},
        "girls_conditions": {"shiori":{"countermin_investigationcallback":2, "present": False}},
        "do_once": True
        })

label shiori_preg_talk:
    show shiori
    hero.say "Hey, Shiori - what's up?"
    "I can tell the very moment that I look into her eyes this close up that I've badly misjudged the situation."
    "Shiori's own eyes are almost as wide as saucers, glazed over as if seeing only wondrous things."
    "All tell-tale signs that, whatever the matter is, it's taking over every thought that's passing through her head."
    "At the sight of me, Shiori practically throws herself in my direction, almost collapsing into my unsuspecting arms."
    "It's all that I can do to keep from either dropping her or being knocked over myself."
    shiori.say "Oh, [hero.name], I'm so happy to see you!"
    shiori.say "I have the most wonderful news!"
    "Wonderful news?"
    "Now that's not something I expected to hear from her today."
    hero.say "Erm...okay, Shiori."
    hero.say "I guess you should probably tell me just what it is..."
    "Her own enthusiasm means that she totally misses my own confusion and sudden anxiety as to just where all of this will ultimately lead."
    "Shiori simply smiles so broadly that her eyes are almost forced closed by the degree to which her cheeks rise in sympathy."
    "She pulls back from my embrace just enough to grab one of my hands and hold it over her belly."
    "Her grip is far stronger than anything I ever imagined her being capable of, and it even scares me a little."
    shiori.say "Can you feel it?"
    "She's looking at me with such intensity that I can hardly tear my eyes away from her gaze to look down at her stomach."
    shiori.say "Can you feel the first stirrings of the miracle that we created?"
    shiori.say "The new life that you planted inside of me?"
    "Suddenly, realisation dawns on me."
    hero.say "Oh god, you don't mean..."
    "Shiori nods furiously, her smile becoming almost manic as she does so."
    shiori.say "Yes, [hero.name], I do - I'm pregnant!"
    shiori.say "Isn't it wonderful news?!?"
    menu:
        "You should abort":
            "I feel like a gaping black hole just opened up under my feet and is trying to pull me down into oblivion."
            "It's not that I hate the idea of either having a kid or being with Shiori for a long while to come."
            "But having both dropped on me from a great height is simply a terrifying prospect."
            hero.say "But...Shiori...we can't..."
            "Even someone as oblivious and innocent as Shiori can't fail to pick up on the fact I'm not exactly elated with her news."
            "Her eyes become wide and her smile shrinks away to almost nothing."
            show shiori sad
            shiori.say "[hero.name]...what's the matter?"
            shiori.say "Aren't you happy that you're going to be a father?"
            "Something about her expression makes the floodgates finally open for my emotions."
            hero.say "I can't have a kid, Shiori...we can't..."
            "Shiori suddenly cries out in horror."
            shiori.say "Oh, [hero.name]...you don't mean..."
            hero.say "It's okay, Shiori - I'll pay for the operation."
            hero.say "You won't have to worry about a thing, I promise!"
            "Shiori backs away from me slowly, shaking her head as if she no longer knowns who she's looking at."
            shiori.say "No...I won't...I won't let you kill our baby!"
            "She turns her back on me with more drama than I thought she was capable of."
            "And then she runs away from me, her sobs carrying backwards on the air."
            $ shiori_love_max = 0
            $ shiori_love = 0
            $ HIDDEN.append("shiori")
        "That's wonderful":
            "It takes a good few moments of staring into space and not saying a word."
            "But I soon realise that most, if not all, of my negative emotions are just the shock of being told that I'm going to be a father."
            "When I actually look down and see Shiori looking back up at me, hanging on my response to her news, I feel positively elated."
            show shiori happy
            $ shiori.love += 10
            hero.say "Shiori...that's amazing news!"
            hero.say "I'm going to be a dad!"
            "I don't think I've ever seen a smile like the one on Shiori's face right now."
            "Her eyes almost seem to glaze over with happiness."
            hero.say "Wait...you do want me to be involved, to raise the kid - don't you?"
            "Shiori doesn't seem to be able to believe the words that keep coming out of my mouth."
            shiori.say "YES...I mean, yes...of course I do, [hero.name]!"
            shiori.say "Actually, I was worried that you...might not want to be..."
            "I shake my head in disbelief at the very idea that she might think I would reject her and the baby."
            hero.say "Shiori, I never really thought about it much before."
            hero.say "But the way I see it, this is the perfect chance for us to build a life together."
            hero.say "I mean, this pretty much makes us a family, doesn't it?"
            "Suddenly I feel my middle being squeezed tightly enough to make me gasp for breath."
            "I look down in surprise to see Shiori wrapped around me like a constricting snake."
            shiori.say "Oh, [hero.name], you've made me so happy!"
            $ shiori.set_flag("toldpreg",True)
    "Once Shiori pulls herself together enough to be on her way, I'm left alone to contemplate all that she's told me."
    "I'm still feeling more than a little disoriented myself, and it still hasn't really sunk in."
    "All that has is the overwhelming news that I'm going to be a father!"
    return

label shiori_pregnant_flag:
    $ shiori.set_flag("pregnant",1,mod="+")
    return

label shiori_coffee_2:
    show shiori
    "When you're messing around with someone in the workplace, things can often get a little complicated."
    "For example, you tend to start speaking in code for the sake of keeping what you get up to from being overheard."
    "The problem comes when you realise that almost every term and phrase that you could use in the course of the working day now also means something else entirely."
    "So when your secret paramour comes into your office and asks you to help them find a lost file in the basement archives."
    "How are you supposed to know if you're being invited for a quick fuck out of the sight of your colleagues."
    "Or if you actually are being drafted in to dig out a particularly elusive client file?"
    "Trust me, if you're not careful, that kind of confusion can lead to serious trouble!"
    "I get reminded of this conundrum when I hear the sound of someone bustling into my office without bothering to knock."
    "Not that the person in question failing to knock bothers me at all, it just means I can narrow down who it might be without needing to look up."
    if not "lavish" in HIDDEN:
        "It can't be Lavish, as she's young and paranoid about making a bad impression, so she always knocks."
    if not "aletta" in HIDDEN:
        "It can't be Aletta, because in the very few seconds after the person came in, they didn't start making demands of me."
    if not "audrey" in HIDDEN:
        "And it can't be Audrey, as they're not leaning over my desk or making a show of themselves in any way."
    "Which means it can only really be one other person."
    show shiori
    hero.say "Good morning, Shiori."
    "I don't bother to look up as I greet her, enjoying the little squeak of surprise she lets out."
    shiori.say "Good...good morning, Mr [hero.family_name]!"
    "I make a point of never explaining how I can work out that it's her, no matter how many times I'm able to do so."
    "It keeps Shiori just that little bit in awe of me and off her guard."
    hero.say "Was there something I can do for you, Shiori?"
    hero.say "Or is this just a social visit?"
    "When there's no answer save for some nervous muttering, I finally decide to look up from my work."
    "I see Shiori, looking as embarrassed and awkward as usual, a tray of hot drinks clutched in her hands."
    "I raise my eyebrows, giving her a clear signal that I want her to explain herself."
    "Even though it's already pretty obvious what she's here for."
    shiori.say "Erm...I...I wondered if you'd like your coffee, Mr [hero.family_name]?"
    "I raise one eyebrow now, making my expression quizzical."
    hero.say "Of course I would, Shiori."
    hero.say "You know that I like a coffee around this time in the morning and you also know just how I take it."
    hero.say "So would you mind explaining to me why today you feel the need to come in here and ask?"
    "Shiori gives me what I think is supposed to be a nonchalant shrug and a smile, which ends up looking more than a little panicked and paranoid."
    shiori.say "Well...I was thinking...I know that you have milk in your coffee."
    "I nod as she gingerly puts the tray down on the desk in front of me."
    shiori.say "But I wondered if...for a change...you might want to choose the kind of milk I put into it today?"
    "Now I see that there are two small jugs on the tray, as well as the cups of steaming, black coffee."
    hero.say "I am going to want milk, Shiori - so what have you got there?"
    "Shiori's mood recovers a little at my interest, and she smiles as she points to each jug in turn."
    shiori.say "Ah...okay...you normally have fat-free, but I also have half-fat, and..."
    "I can hear her pause and take in a deep breath before she continues."
    shiori.say "You could have...full-fat...if that's what you'd like?"
    "Her hands rise up and out of view, and my eyes instinctively follow them."
    "Shiori clasps one hand on either side of her breasts and slowly pushes them together so that they bulge outwards, almost popping out of her blouse."
    "Wait a minute - does she actually mean..."
    "Shiori keeps on leaning further forwards until her heaving chest is almost hanging over the coffee cups on the tray."
    "She looks at me, clearly waiting for an answer, her breasts in increasing danger of falling out of her top."
    menu:
        "No":
            $ shiori.love -= 5
            "I can feel my stomach begin to churn at the very thought of what Shiori's suggesting."
            "An unconscious urge makes me cough, and I can taste the hint of bile at the back of my throat."
            show shiori sad
            hero.say "You know what, Shiori - I think I'll stick with the good, old fat-free, okay?"
            "Shiori's eyes widen and her cheeks colour as my answer sinks in and she realises that she's still pushing her breasts together almost in my face."
            "Her arms shoot to her sides and she stands bolt upright, making her chest bounce in sympathy."
            shiori.say "Oh...okay...that's...that's great, Mr [hero.family_name]..."
            "She pours the milk into one of the cups of black coffee as an awkward silence fills the space between us."
            "Once she's stirred the coffee and placed it on the desk, she gives me a fragile smile and hurries out of my office."
            "I blow out my cheeks and shake my head, still not quite able to get my head around what Shiori actually just did."
        "Yes":
            $ shiori.love += 5
            $ shiori.sub += 10
            "I look Shiori in the eye and then glance down at her breasts, licking my lips as I try to make a decision."
            "The look in her eyes tells me that she's totally serious, and I can't deny that I'm instantly curious too."
            "I don't know whether it's a kink in me, or just a natural instinct given the size of her breasts."
            "But can anyone honestly say that they haven't at least wondered what breast milk tastes like?"
            show shiori happy
            hero.say "Erm...okay, Shiori...that sounds...nice."
            "Her face instantly lights up at my accepting her offer."
            shiori.say "Sure thing, Mr [hero.family_name]!"
            shiori.say "I'm so happy to serve you - to let you use every single part of me."
            shiori.say "It makes me feel so happy...so useful!"
            "I loosen my collar with a finger as Shiori describes how she wants to be used by me."
            "But then I find myself tugging in my tie as though it's a garrotte as soon as she begins to unbutton her blouse."
            "Shiori bears her left breast, pulling down her bra so that it falls, full and heavy to sway over my desk."
            "She's actually going to do it!"
            hide shiori
            show shiori milk
            "Cupping the breast with her right hand and placing her left hand atop it, she dangles the breast over one of the cups of black coffee."
            "Shiori then begins to push her left hand down the breast, pressing and massaging as she goes."
            "No milk flows to begin with, but I can see from her expression that she's becoming somewhat aroused already."
            "As Shiori sighs and moans from the sensations of trying to milk herself, eyes closed and biting her lip, I can feel my cock stiffening in sympathy."
            "Soon the first of the milk begins to dribble from her large, swollen nipples and into the steaming coffee below."
            "And then it starts to come in more regular squirts, most hitting the cup, but some spilling onto the desk around it."
            "The milk is thick and it must be full of fat, as I can see it covering the surface of the coffee with an oily sheen."
            "Thick bubbles of fat are also coagulating and floating as more breast milk is pumped into the cup."
            "By now, the contents are starting to spill over the lip of the cup, and Shiori's eyes are beginning to glaze over."
            "My erection is becoming painful for the want of being stuck into her, and I can only guess that her pussy must be in a similar state."
            hide shiori milk
            show shiori
            hero.say "SHIORI!"
            "She snaps out of it suddenly at the sound of my raised voice."
            hero.say "Shiori...that's enough - the cup's full, see?"
            "She looks at me with a distant expression, and then down at the cup."
            shiori.say "Oh, I see...silly me!"
            "She grins whilst still looking more than a little spaced out, and turns to leave."
            hero.say "Ahem...Shiori - your collar's a little twisted..."
            "Shiori glances down and takes a full five seconds to realise that her left breast is still hanging out."
            "She giggles in embarrassment, makes herself decent and then slips out of my office."
    "Left alone, I pick up my coffee and blow the steam off of the top before taking a long and much-needed mouthful."
    "I don't get back to work immediately, as Shiori and her strange habits are still uppermost in my mind."
    "All of this over my choice of milk!."
    "I'm not sure if I should feel flattered or terrified!"
    return

label shiori_coffee_1:
    show shiori
    "I watch Shiori absently as she scurries here and there, nodding and shaking her head at the answers that she gets from each successive colleague."
    "Strictly speaking, the company's quite progressive on things like making drinks and fetching stuff for superiors."
    "There's no specific requirement for someone of her grade to actually do things like that."
    "And even if Aletta or I asked her to, Shiori could still say no and be well within her rights to do so."
    "But she seems eager to take on any and all roles that she can of that nature, as though she wants to mother the entire office and make herself indispensible."
    "I keep on trying to tear my attention away from Shiori and get back to work, as she's only taking down orders for drinks after all."
    "And yet I find that, for some reason, I can't take my eyes off of her for more than a couple of seconds before I feel compelled to look her way again."
    "Full disclosure up front, if you'll pardon the pun - I know that she has unfeasibly large breasts."
    "They're distracting enough, even when she's trying to hide them under her otherwise demure and sensible work-clothes."
    "But it's not just that, you have to believe me!"
    "There's just something about how deferent and eager to please Shiori seems to be."
    "Something I can't quite put my finger on, and yet it makes me wonder what lies behind her being so damn needy and quick to seek praise like that..."
    shiori.say "Good morning, Mr [hero.family_name]!"
    "I jerk to attention at my desk, as Shiori bustles in on me and bursts the bubble of my thoughts with her cheery presence."
    hero.say "Erm...hi, Shiori - what can I do for you this morning?"
    "She smiles at this, almost blushing at the same time, clasping her hands together and cocking her head on the side as she looks at me."
    shiori.say "Don't be silly, Mr [hero.family_name] - I'm the one that's supposed to do things for you!"
    shiori.say "You can ask me to do anything you want, any time you feel the need..."
    "Is it me, or did it just get hotter in here?"
    "I fiddle with my collar nervously, while I momentarily lose the power of speech."
    hero.say "COFFEE!"
    "Shiori jumps slightly at the volume with which the word comes out of me."
    "I can't help but notice the impressive way that her breasts jump in sympathy too."
    hero.say "Coffee, Shiori - I guessed that you were going round asking people how they took theirs just now!"
    shiori.say "Oh, yes, of course...that's what I came in here to ask."
    shiori.say "I'm such a scatter-brain, Mr [hero.family_name] - whatever are you going to do with me?"
    "There's a suggestive weight to that last question that I try to ignore as best I can."
    hero.say "Well, Shiori - getting back to the subject of the coffee..."
    menu:
        "Black":
            hero.say "I like my coffee the same way I like my women."
            hero.say "Sweet, black and hot as hell!"
            show shiori sad
            "I laugh the instant after I say this, trying to show Shiori that I'm joking."
            "But she looks more shocked and embarrassed than anything else."
            "Also a little hurt too, as though I've said something to deliberately hurt her alone."
            hero.say "Ah look, I'm sorry, Shiori...that was just a poor attempt at a joke."
            hero.say "For the record - I take my coffee black with one sugar."
            hero.say "And I'd be very grateful if you could make me one."
            "Shiori smiles weakly at this, nodding before she turns to go."
            "She leaves me hoping that I've not just landed myself an appointment with human resources."
            "I really hope not, as I can't take the prospect of sitting through the orientation video on sexual harassment again!"
        "Milky":
            $ shiori.set_flag("coffee",1)
            hero.say "I always take mine white - I can't stand the taste of the stuff without milk, you know?"
            show shiori happy
            "For some reason, Shiori seems to be oddly pleased with this statement, almost like I gave her the exact answer she was looking for."
            shiori.say "Great, Mr [hero.family_name] - I'll be sure to make it nice and milky for you!"
            "I try not to be too weirded out by her enthusiasm at discovering I like my coffee with plenty of milk."
            hero.say "Erm...okay, Shiori...was there anything else that you wanted to ask me right now?"
            shiori.say "No, I don't think so..."
            shiori.say "But, of course, that's not to say that there isn't!"
            shiori.say "I'm such a scatter-brain, after all!"
            "And with that, she turns around and bustles out of my office."
            "If it had been anyone else, then I'd have fully expected to be looking up to find a white coffee on my desk sometime in the next ten minutes."
            "But as it's Shiori I'm dealing with, it could well be tomorrow before one appears."
    "So there I am - left feeling odd and edgy by the supposedly simple act of having Shiori come in and ask me how I take my coffee."
    "I shake my head, and then try to get my mind back on my work once more."
    "But I still can't keep myself from taking the occasional glance out into the office and shaking my head at Shiori's quirkiness."
    return

label shiori_kiss_me:
    call shiori_greet from _call_shiori_greet_5
    show shiori
    "I don't think that in all the time she's been working under me, I've once seen Shiori do something that could honestly be described as assertive in any way."
    "And that's exactly what makes me stop and watch, almost in fascination, as she seems to be trying to summon the will to do just that."
    "At first I just assume that she's pissed about something and is trying to summon up the courage to mention it to me."
    "But no matter how long of a pregnant pause I allow to build up between us, she still doesn't as much as open her mouth to let out a squeak."
    "I really don't want to be an ass-hole to Shiori, as she's genuinely as shy and bumbling as she's being right now."
    "And yet I also don't want to have to sit around all day, just for the sake of hearing her meekly explaining some minor grievance that I don't even care about."
    "Let let out an exasperated breath, meaning to utter a couple of words with the intention of prodding Shiori into action."
    "But the moment that I have my mouth open, she seems to come instantly to life."
    "Before I have time to guess what she's doing, I feel her mouth clamping over mine like a leech!"
    show expression "shiori kiss "+shiori.get_clothes()
    "Shit, what's going on?"
    "Is Shiori actually planting a kiss on me?!?"
    "I haven't fully managed to answer that question before I find myself leaning into the unexpected kiss without any conscious choice on my part."
    "Her lips are so full and soft, and the sounds that she's making are such a turn-on that I can't help but go along with it too."
    hide expression "shiori kiss "+shiori.get_clothes()
    return

label shiori_office_bj:
    scene bg office
    show shiori
    hero.say "Shiori, I have an idea, if you’re interested."
    "Shiori looks up from her desk, eyes wide. "
    shiori.say "Did I do something wrong, Mr [hero.family_name]?"
    "I shake my head. "
    hero.say "No, nothing like that, but I was thinking maybe you deserve yourself a little reward. Of course... it’d be pretty dangerous if we get caught."
    hide shiori
    scene bg personal
    "I walk past her, letting her wonder what it is we were doing."
    "Sitting at my desk, I resolve to get some work done before she comes in. "
    show shiori
    "Soon, however, there’s a knock on my door. Shiori stands there, looking shy as she meekly speaks up. "
    shiori.say "W... what did you want from me, Boss...?"
    "I scoot back from my desk, my legs spread a bit as I motion down underneath. "
    hero.say "Come on over here..."
    "She gasps, but does as she’s told. "
    hide shiori
    "Soon, she’s sitting in the little area under my desk, peering up at me with big, excited eyes. "
    shiori.say "Oh, boss... if I’m in here, no one’s going to be out there to greet people. What if someone comes in?"
    show shiori bj office outfit hand smile
    "I unzip my pants, letting my dick spill out "
    hero.say "That’s where the fun comes in."
    shiori.say "O... oh my!"
    "She stares at my length. "
    shiori.say "Boss, I don’t think... is this even... ethical?"
    hero.say "Since when were you about following the rules?"
    shiori.say "H... hey. I don’t break them... on purpose"
    hero.say "Well, then, go ahead."
    show shiori bj office outfit hand smile
    "She wraps her fingers around the base as she scoots herself in, closing one eye as she licks up from base to the tip. "
    show shiori bj office outfit suck
    "She sighs, her body shuddering as she holds onto my thigh with one hand and lowers her lips around my cock, holding me still with the other."
    "She slips up and down along the pole, the quiet office filled with the slurping slick sounds of her mouth and tongue over my length. I groan as I pet her hair, and she glances up at me, sucking upon my length with a happy squeak."
    "The door opens up, and I scoot in, reflexively pushing her head closer to my thighs, and holding her in place. "
    hide shiori
    show aletta
    "After a quick muffled grunt, she is trapped in between my thighs as I sit there, hands folded as Aletta enters the room."
    aletta.say "Ah, there you are [hero.name]. I’ve been looking for you."
    hero.say "Ah, yeah? You have?"
    aletta.say "Yes, I wanted to discus some of the reports here. It seems your office has missed a few things."
    hero.say "Ah, that must be my Shiori. She’s a nice girl, but lacks proper discipline."
    aletta.say "This company can’t permit slackers, Mr. [hero.family_name]."
    hero.say "Oh, don’t you worry about that. I’ll be sure to whip her into shape."
    hide aletta
    show shiori bj office outfit suck
    "As I speak, Shiori’s mouth around my cock only sucks harder. "
    "I wince slightly, but keep my cool."
    "In... in fact, I think I’ll personally see to her training, if you don’t mind. I have a... a good feeling about this one, as long as she’s... whipped into shape."
    hide shiori
    show aletta
    "Aletta nods. "
    aletta.say "Well, as long as you have things handled, I guess I’ll just head on out."
    aletta.say "I want a report on her workmanship in the morning."
    "Aletta leaves, slamming the door behind her. "
    hide aletta
    "A moment later, I fall forward on the desk and shove my hips forward, practically forcing my cock down Shiori’s throat."
    show shiori bj office outfit suck cumshot
    "Under the desk, Shiori gulps and gasps as cum shoots down her. "
    "Soon, she backs out, with only a small trail of pearly whiteness left dribbling down her chin. "
    hide shiori
    show shiori blush
    "I scoot back, smiling down at her as she whipes her chin off, panting heavily."
    hero.say "Well, I’m sure you heard all of that, but you know what...?"
    hero.say "Looking at you, I think you have a stellar performance review."
    "She smiles up at me, sighing with dreamy happiness. "
    shiori.say "Pleasure as always, Mr. [hero.family_name]."
    hero.say "Glad your morale is up."
    "I zip up my pants and stand up."
    hero.say "Because you’re going to have to stay late tonight to organize that mess."
    "Shiori whimpers slightly, though her smile never leaves her face. "
    shiori.say "I’ll... I’ll do my best, sir."
    hero.say "That’s the morale we need at this company. Good job!"
    hide shiori
    return

label shiori_scold_1:
    "Getting chewed up by my superior for missing the call of an important client is not exactly the way I thought my day was going to go."
    "I’m not supposed to take calls, anymore. That’s my secretary’s job. I guess it’s time to go find out what’s up."
    show shiori
    "I find Shiori at her desk, talking on the phone and filing her nails."
    hero.say "Shiori, do you have a minute?"
    shiori.say "Hold on, Mr. [hero.family_name]. Yes... uh-huh? I’ll let him know right away."
    "She hangs up the phone, looking up to me with a smile on her face. "
    shiori.say "That was the order you called in for yesterday."
    shiori.say "They’ll be making their way in by tomorrow..."
    shiori.say "And..."
    "She gasps, covering her mouth."
    shiori.say "Oh my gosh! Mr. [hero.family_name]! "
    shiori.say "The Parkerson appointment! I totally forgot."
    shiori.say "I’m so sorry!"
    "I shake my head. "
    hero.say "Sorry isn’t going to cut it. You’re in deep trouble, do you understand?"
    hero.say "Now, I’m going to have to stay overtime just to find a replacement! I have plans. I can’t just go around fixing your messes."
    shiori.say "I... I guess you’re going to write me up, aren’t you...?"
    "She lowers her head a bit, slumphing her shoulders forward as she sighs, defeated."
    hero.say "You need to shape up, or there’s going to be some serious consequences, that’s for sure."
    shiori.say "Serious, huh...?"
    "From under her breath, she mutters something."
    hero.say "What’s that?"
    "She gasps again. "
    shiori.say "Oh, I’m sorry boss, did you hear that?"
    hero.say "What did you say to me just now?"
    "There’s a silence as she glances back and forth. Everyone else is out to lunch, leaving her and myself alone for the time being. "
    show shiori blush
    shiori.say "Oh, nothing. I just said ‘what are you going to do, spank me?"
    hero.say "I... what?"
    "She shrugs. "
    shiori.say "Well, you aren’t going to write me up, right?"
    shiori.say "Guess you could punish me some other way."
    shiori.say "I mean that WOULD get the message across not to mess with you anymore."
    "The smile on her face, the redness on her cheeks..."
    hero.say "Wait a minute... are you...?"
    shiori.say "Hm...?"
    "I shake my head. "
    hero.say "No, nevermind. Just see if you can’t get them to reschedule, or else you really are going to get it."
    shiori.say "Oooh, yes, Sir!"
    "she says, saluting me and th en grabbing the phone. "
    "As I walk away from her, I give her one last parting look, curious at what her game is. But as I see her, her eye catches mine, and a slight smirk spread across her face."
    hero.say "Just make sure if you make another mistake..."
    "I begin to speak to her, taking the time to steel myself for what I was about to imply. "
    hero.say "...you’d better make sure its not something so important. I don’t want to get REALLY angry with you and make a..."
    "I cough and straighten my tie."
    hero.say "I don’t want to make a DRASTIC decision."
    "She bites her lip and leans over her computer, typing away furiously as I finally turn and head back to my desk. "
    "Let’s see how morale goes after THAT."
    hide shiori
    $ shiori.love += 5
    return

label shiori_scold_2:
    "I decide to return to my office to get some work done."
    hero.say "Dammit! What the hell is this!"
    "I stomp out of my office and scan over the room. "
    hero.say "Shiori!"
    show shiori
    "Shiori comes running in, panting and bending over, her hands on her knees. "
    shiori.say "I’m sorry... M... Mister [hero.family_name]. What’s the matter?"
    "I hold up the package of pens, 20 count, all of them black."
    shiori.say "I... I don’t understand. I told inventory about your pen shortage?"
    shiori.say "Is something the matter?"
    "I take a deep breath, trying to calm down. "
    hero.say "Alright, first of all, the contracts we deal with have to be done in blue ink, Shiori."
    "I shove the package to her."
    "She fumbles a moment and holds it between her hands, pressing the packet up against her breasts. "
    shiori.say "Oh, but, Mister [hero.name], that’s okay. Because the memo I sent you said we were allowing black pens now, and..."
    "She trails off as I stare death threats into her eyes. I didn’t need to say it. "
    "I really didn’t WANT to say it, but here I am, anyway. "
    hero.say "Shiori... what memo...?"
    "She buries her face in the pens, trembling at the thought. "
    shiori.say "O... oh, did I... did I forget to send it to you."
    hero.say "Yes, yes you did."
    "She sighs, lowering the pens. For a split second, I can see a little grin on her face. "
    "Oh, no, is this what she was planning? I sigh and I take the pens from her."
    hero.say "And another thing... I said I needed 10 pens, not 10 CRATES of pens! Just look at this. It’s covering my desk!"
    shiori.say "Oh, my, sir, that’s a lot... a lot of pens! I guess I don’t listen very well, do I?"
    "I lean in, narrowing my gaze at her. "
    "She stares up at me with a dumb little smile as she leans back, stumbling a moment until she hits a desk behind her with a squeak."
    hero.say "No, apparently you don’t listen very well."
    show shiori blush
    shiori.say "Are you going to spank me now, sir?"
    "I slowly move my hand up towards her, hovering by her thigh a moment. "
    hero.say "Hm... well, you do deserve a punishment."
    "She squeaks, shaking as I lean in closer to her, a smile spreading upon my lips."
    shiori.say "I’ve... I’ve been such a bad girl, boss..."
    hero.say "Yes, yes you have..."
    "I say, chuckling softly to her."
    shiori.say "I really should be punished... and there’s no one here to stop you."
    hero.say "No, there isn’t..."
    "I agree."
    shiori.say "S... so, how are you going to do it?"
    "she asks, her eyes watering, getting wide. "
    "She bites her lip as she looks to me with expectant glee."
    "I grab the pens and yank them from her. "
    hero.say "First of all, I'm going to have to put these back in their box. Then, I’m going to have to ask you to take these to the post office."
    shiori.say "W... what?"
    hero.say "And then after that... you can get me a coffee. You’re really pushing your luck."
    hero.say "Next time, your punishment WILL be severe"
    "She grumbles, but I catch a quick flick of her tongue as she licks her lips. "
    hide shiori
    "Oh yes, this could be quite fun to keep up."
    $ shiori.love += 5
    return

label shiori_scold_3:
    "As I arrive at my office, there sits a large coffee cup from an expensive store with my name spelled wrong upon it. "
    "I give it a quick sip, only to spit it back out immediately."
    hero.say "What the hell? Shiori!?"
    show shiori
    "Shiori peeks into my office, hiding her face behind the door. "
    shiori.say "Y... yes, Mr. [hero.family_name]?"
    "I clap my hands together and breathe deeply through my nose. "
    "Closing my eyes, I refocus myself a moment before I push my hands downward. "
    "Once I open my eyes again, I see her, and I just ask her a simple question."
    hero.say "Why... does my coffee... have salt?"
    shiori.say "Oh, that?"
    "Shiori taps her cheek, looking up and away, putting on an almost ditzy face. "
    shiori.say "I have no idea how that could have happened."
    shiori.say "I mean, I forgot to get you sugar at the store, and I know you asked for sugar last night, so... I just went to the break room and poured some in and-"
    "She gaps, slapping her cheeks. "
    shiori.say "Oh no, Mr. [hero.family_name], you dont’ suppose I put salt in there by mistake?"
    shiori.say "Oh, I’m so terribly sorry! I can’t believe I did that. Please, oh please, oh please don’t reprimand me!"
    "I take the coffee cup and slam it on a cabinet, leaving my desk clear. I then point to it, and nod."
    "She gasps, but frowns, shaking her head. "
    shiori.say "Oh, no, sir! Please, don’t do this! I’ll do better, I promise!"
    "I just point."
    show shiori spanking
    "She gulps, trembling as she bends herself over the desk, pressing her ample breasts up against the desktop. "
    shiori.say "Oh, this is so embarrassing. I can’t believe I’m being so degraded!"
    hero.say "You should have known that sugar and salt are in two different containers in the break room."
    shiori.say "I know, I know! I was just so worried!"
    hero.say "Well, now, you have to pay the price."
    show shiori spanking hand
    "I lift my hand upwards."
    "She closes her eyes, burrowing her head down against the desk."
    "I wiggle my fingers a moment, holding my arm in the air."
    "She whimpers in preparation."
    show shiori spanking blur
    "I then throw my arm down, smacking her right on her skirt-covered rump."
    show shiori spanking done
    "She gasps, tilting her head back."
    shiori.say "Oooh, I’m sorry, sir! Please, don’t do it again!"
    hide shiori
    show shiori blush
    "I grab my coffee and then I walk out towards the hallway. "
    hero.say "No, I think you’ve learned your lesson. I need to get myself a coffee."
    hero.say "You go and keep up your work, and don’t fail me again."
    hide shiori
    $ shiori.love += 5
    "I toss the cup in the trash and continue on my way out, leaving her to grumble as I leave her wanting for more."
    "This game we’re playing... it’s actually getting to be kinda fun. "
    "Except... maybe for the salty drinks. Gah!"
    return

label shiori_scold_4:
    "I grumble at my desk and turn off my computer. "
    "Tapping one of my bulk-ordered black pens on my desk, I can’t help but feel a bit anxious. "
    "I haven’t gotten a call I wanted in a few hours, and they said they’d call today. "
    "I can’t get anything done without them, and there’s nothing else to do around here until they do."
    "I scoot out of my desk and peer out towards Shiori’s desk. "
    "She’s on her phone... it seems like a pretty slow day, too. "
    "Sighing, I lean up against the door and I call out to her. "
    hero.say "Shiori, get in my office."
    show shiori
    "Surprised, she immediately hops up, following me inside."
    shiori.say "W... what did I do this time, Mr. [hero.family_name]."
    hero.say "It’s more like what you didn’t do... Shiori, did you remember to call Miss Jefferson back this morning?"
    "She blinks a moment, and she tilts her head. "
    shiori.say "Miss... Miss Jefferson...?"
    hero.say "Oh, come on, Shiori! You’re usually so good, but when you screw up, you really screw up. How could you forget Miss Jefferson!"
    shiori.say "I honestly have no idea who you’re talking about!"
    "She whines."
    "I snicker at that. "
    hero.say "Well, if you’re so forgetful, I think I’ll have to give you something that’ll be hard to forget. Bend over."
    "She stares at me amoment, only to then shake her head as she walks on over to the desk. "
    show shiori spanking
    shiori.say "Oh, Mr. [hero.family_name], you’re so mean! I can’t believe I take this abuse from you."
    hero.say "Yeah, well, if you don’t learn, you’re going to have to keep taking it... and I’m going to have to make it more memorable this time."
    show shiori spanking botup
    "I flip up her skirt and she grips my desk, gasping at the rush of air."
    "I lean in, giving the cheek a bit of a squeeze. "
    hero.say "Right. Now, that this is out of the way, I can actually get to that skin underneath."
    "Maybe I should..."
    "I tease at the hem of her panties, and she groans, but I pull away."
    show shiori spanking botup hand
    hero.say "Hey, who said you could enjoy your punihsment, hm? You want to like this shit?"
    show shiori spanking botup blur
    "I smack her on one cheek, leaving a red mark on her rump. "
    show shiori spanking botup done pain
    "She gasps, shaking underneath. She holds her mouths hut so she doesn’t scream too loud that others could hear."
    show shiori spanking botup hand normal
    hero.say "Good girl, you’re learning not to be too loud."
    show shiori spanking botup blur
    hero.say "You’ll need it."
    show shiori spanking botup done pain
    "Without warning, I smack her other cheek, and she screams louder into her hands, huffing after I’m done. "
    "I stand up and I grab my coat. "
    hero.say "I’m going to go out for a walk a bit. Hold my calls until I get back, and try to remember Miss Jackson."
    "As I step out of the room, she gasps and says. "
    shiori.say "Hey wait, you said it was ‘Jefferson’ earlier. Boss, are you... did you... YOU HAD ME WORRIED!"
    "I snicker as I walk out the door. "
    "Two can play at her game, indeed."
    $ shiori.love += 5
    return

label shiori_scold_5:
    $ shiori_love_max = 120
    show shiori angry
    "Shiori barges into my office, the smuggest of smug looks upon her face as she stands there, hands folded over her chest."
    "I stare up at her, confused as to what she’s doing. "
    hero.say "Can I... help you, Shiori...?"
    shiori.say "I’m onto you, you know,"
    "she says, sass starting to drip from every syllable."
    hero.say "Oh, really...? And just what am I up to?"
    show shiori normal
    shiori.say "I remember when you made up Miss Jackson and Miss Jefferson, trying to make me think I was forgetting someone important."
    shiori.say "Well, guess what? I figured out you actually hired some girl to pretend to be one of them and call with an ‘urgent request."
    "I lower my coffee cup. "
    hero.say "W... what?"
    shiori.say "Oh yeah, she said she needed to speak with her right away."
    shiori.say "Well, you know what I did? I told her she could talk to Miss Lincoln if she wanted to make a complaint."
    "Rubbing my eyes, I put my coffee aside and ask. "
    hero.say "Shiori... was that... Jenna Jefferson...?"
    "She nods. "
    shiori.say "Yup! That’s the one. That’s the plant you put in there to punk me."
    shiori.say "Well, you know what? No more teasing from you, Mr. [hero.family_name]. I got you this time, hehe!"
    "I push up from the desk and point to it. "
    hero.say "No, you just hung up on an actual client. It’s come to my attention that you’re just wanting to be spanked."
    "Maybe now, I can cure you of that disease byt giving it to you, very, very hard."
    "She gulps, shudering. "
    shiori.say "Oh, I... is that... so? Look, I’m really sorry and..."
    hide shiori
    show shiori spanking
    "I point to my desk, and she sighs, sliding over it. "
    show shiori spanking botpantiesdown
    "I grab her skirt, hiking it up and showing off her panties. "
    "I then trace my fingers down along the white fabric before I gripped at them and tugged them down, exposing her before me. "
    show shiori spanking botpantiesdown hand
    hero.say "A bare butt... that’s the only way to cure you."
    show shiori spanking botpantiesdown done mark pain foot
    "I slap her square in the center, lower than normal, getting close to her exposed pussy."
    hide shiori
    show shiori spanking botpantiesdown hand normal
    "She yelps, her tongue rolling out from that hit."
    show shiori spanking botpantiesdown done mark pain
    shiori.say "Aaaagh! Boss, I’ll do better, I promise!"
    hide shiori
    show shiori spanking botpantiesdown hand normal
    hero.say "No more games from now on!"
    show shiori spanking botpantiesdown blur
    "I said, slapping her on one cheek, and then the other."
    show shiori spanking botpantiesdown done mark pain
    "She grips the desk, shuddering violently as she groans out from my slaps. "
    hide shiori
    show shiori spanking botpantiesdown hand normal
    shiori.say "B... Boooosss!"
    show shiori spanking botpantiesdown blur
    hero.say "From now on, if you want to be punished, you do a GOOD job. That’s because you want this so much."
    show shiori spanking botpantiesdown done mark pain foot
    shiori.say "Aaah, r-right boss!"
    hide shiori
    show shiori spanking botpantiesdown hand normal
    hero.say "Screw up in your job for real again, and I’ll really get you upset, and that’s a promise."
    show shiori spanking botpantiesdown blur
    "I give her a triple slap."
    show shiori spanking botpantiesdown done mark pain foot
    "One cheek, the other, and then in between."
    hide shiori
    show shiori spanking botpantiesdown e pain
    "She pants, leaning over the desk, groaning as her butt shines red with my handprints."
    show shiori spanking botpantiesdown e normal
    hero.say "Now, then... I need to call Miss Jerfferson back and apologize for the incompetence of my staff. We’ll talk about this later. Got it?"
    shiori.say "Uh... huh..."
    "She sighs, closing her eyes and smiling."
    hero.say "Dang, it’s a message."
    hero.say "Shiori, you can take care of this, but... leave your panties here when you go back to your desk."
    hide shiori
    show shiori blush
    "She squeaks and pushes herself up, pulling down her skirt and running off towards the room."
    hide shiori
    "Yes, I believe its game over... now the real fun begins."
    $ shiori.love += 5
    return

label shiori_give:
    $ gift = Consumable("Shiori's milk", money_cost = 250, effects = [("energy",1),("hunger",1)], limit = "day")
    "She hands me a bottle of milk."
    hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label shiori_give_valentine:
    show shiori
    "Shiori walks hesitantly towards me."
    call shiori_greet from _call_shiori_greet_7
    show shiori blush
    shiori.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Shiori's milk", money_cost = 250, effects = [("energy",1),("hunger",1)], limit = "day")
    "She hands me a bottle of milk."
    hero.say "Thank you, Shiori."
    $ hero.gain_item(gift)
    hide shiori
    return

label shiori_give_birthday:
    show shiori
    "Shiori walks towards me."
    call shiori_greet from _call_shiori_greet_8
    show shiori happy
    shiori.say "Happy birthday [hero.name]!"
    call shiori_give from _call_shiori_give
    return

label shiori_give_christmas:
    show shiori
    "Shiori walks towards me."
    call shiori_greet from _call_shiori_greet_9
    show shiori happy
    shiori.say "Merry christmas [hero.name]."
    call shiori_give from _call_shiori_give_1
    return

label shiori_start:
    $ shiori_love_max = 120
    $ shiori.set_flag("story",1)
    $ if "shiori" in HIDDEN: HIDDEN.remove("shiori")
    return

label shiori_init:
    python:
        if "shiori" not in HIDDEN and not shiori.get_flag_value("story"):
            HIDDEN.append("shiori")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
