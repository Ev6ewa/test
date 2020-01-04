init python:

    Event(**{
        "name":"hanna_init",
        "label": ["hanna_init"],
        "girls_conditions": {"hanna":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "hanna_masturbate",
        "label": ["hanna_masturbate"],
        "duration": 1,
        "priority": 500,
        "game_conditions":{"room":["gym"],"hours":(10,17), "min_fitness":30, "activity":["train_hard", "train"],"flageq_hannastart":1, "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "hanna_event_02",
        "label": ["hanna_event_02"],
        "duration": 1,
        "priority": 500,
        "girls_conditions": {"hanna":{"flageq_story":1}},
        "game_conditions":{"room":["gym"], "min_fitness":40, "activity":["buymembership"], "flag_female":0},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "hanna_event_03",
        "label": ["hanna_event_03"],
        "duration": 1,
        "priority": 500,
        "girls_conditions": {"hanna":{"flageq_story":2, "min_love":40}},
        "game_conditions":{"room":["gym"], "min_fitness":50, "activity":["train_hard", "train"], "flag_female":0},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "hanna_event_temp",
        "label": ["hanna_event_temp"],
        "priority": 500,
        "game_conditions":{"done":"hanna_event_03"},
        "do_once":True,
        })

    Event(**{
        "name": "hanna_give_christmas",
        "label": ["hanna_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"hanna":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "hanna_give_birthday",
        "label": ["hanna_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"hanna":{"min_love":80,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "hanna_give_valentine",
        "label": ["hanna_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"hanna":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name":"hanna_preg_talk",
        "label": ["hanna_preg_talk"],
        "duration": 0,
        "do_once": False,
        "girls_conditions": {"hanna":{"flagmin_pregnant":6,"flag_pregtalk":0, "active":True}},
        "game_conditions": {"activity":"interact"}
        })

    Event(**{
        "name": "hanna_pregnant_flag",
        "label": ["hanna_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"hanna":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

label hanna_pregnant_flag:
    $ hanna.set_flag("pregnant",1,mod="+")
    return

label hanna_preg_talk:
    show hanna blush
    hanna.say "Hey...hey, [hero.name]...hey there!"
    "My head snaps around in time to see Hanna, obviously out jogging and coming straight towards me."
    "I was never a fan of Baywatch back in the day, but she seems to run slow-motion as she approaches all the same."
    "Her shorts show off her shapely legs, her chest sways with the motion of her body, and her hair bounces around her face like a blonde halo."
    "Do I sound like I'm reeling off the virtues of a goddess at all?"
    "If so, then what do I care?"
    "She looks stunning, full stop."
    hero.say "Oh, hi, Hanna."
    "She stops just before me, bending over to rest her hands on her thighs and catch her breath for a moment."
    "Having to watch her spandex shorts stretch as she does so is such a chore to endure!"
    "She stands up and stretches a little more, so close that I can feel the heat smell the perspiration coming off of her body."
    "It's weird how normally another person's sweat normally freaks me out."
    "But with her, it's somehow sexy - like she's giving off a pheromone, or something."
    hanna.say "I must have jogged past here every day for months now."
    hanna.say "How come I've never seen you before?"
    hanna.say "You work around here, right?"
    hanna.say "I remember you saying so."
    hero.say "Yeah, in that building, right there."
    hero.say "Normally I've got so much on that I eat lunch at my desk."
    "Hanna shakes her head in disbelief, the idea that no sane person would allow themselves to be chained to a desk all day implicit in her eyes."
    hanna.say "But today, you managed to escape?"
    hero.say "Yeah, I guess you could say that."
    hero.say "And ran into you - so I guess you could call it fate!"
    "I can see from the way her expression changes that the joke fell far short of the mark."
    "But I can't tell for the life of me why."
    hanna.say "Well...maybe you might want to think about whether or not you believe that later."
    hero.say "What...why, Hanna?"
    hanna.say "There's something that I've been meaning to tell you for a while now."
    "Oh shit, here we go."
    hanna.say "I'd been trying to think of the right moment and spot, but nothing came to mind."
    hanna.say "So I guess, as fate made us meet at random, here and now is as good of a place and time as any."
    hero.say "Hanna, you're scaring me a little - are you trying to tell me that you want to break up or something?"
    hanna.say "[hero.name], no...god no...not that!"
    hanna.say "But it's almost as serious, I guess."
    hero.say "Aww, hell...just tell me, please?"
    "Hanna pauses to look around for a moment, as if steeling her nerves before she speaks again."
    hanna.say "Well, [hero.name]...her goes - I'm pregnant."
    "I feel like someone just snuck up and hit me in the gut with a sledgehammer."
    hero.say "You...you're sure?"
    hanna.say "As I can be - I took the test a couple of days ago, and it was positive."
    hanna.say "That's why I've been off the radar recently."
    hanna.say "I had to get my head round it before I told you."
    hanna.say "So - what are we going to do?"
    "Part of me feels mad that Hanna took so long to get her own head straight, but then dumped this on me in the street with no prior warning."
    "But then this is as serious as she says it is, and getting petulant and mad isn't going to make it any easier in the long run."
    menu:
        "You should have a termination":
            $ hanna.love -= 10
            hero.say "Jesus, Hanna - I'm not ready for this!"
            hanna.say "Look, I know I kinda just dropped this whole thing on you, and it's big."
            hanna.say "If you want time to think, maybe we could meet up tonight?"
            hero.say "No, Hanna, you don't understand."
            hero.say "What I mean to say, is that I'm not ready to be a parent - not at all!"
            hanna.say "But..."
            hero.say "And I don't think you are, either."
            show hanna sad
            "Hanna looks instantly devastated, as though she's desperately trying to think up a counter to my argument."
            hero.say "I don't just mean emotionally either."
            hero.say "My job has me wound up so tight that I might snap, and I still live in a house that I have to rent rooms in to make ends meet."
            hero.say "Your dad might own the gym, but neither of us wants to sponge off of him, do we?"
            hanna.say "So you think that we...that we should..."
            "She can't even bring herself to say the word, so I have to do it for her."
            hero.say "A termination, Hanna - yes, I think we have to get a termination."
            "Hanna's huge blue eyes begin to shed genuine, heartfelt tears."
            "I embrace her, right there in the street."
            "Having to say that out loud was tough, but I genuinely think, under the circumstances, it was the best thing for the both of us."
            $ hanna.set_flag("pregnant",0)
        "We should keep it":
            $ hanna.love += 10
            hero.say "Hanna, you should have told me the moment that you knew!"
            hanna.say "Oh geez, [hero.name] - you're not mad at me, are you?"
            hero.say "What?"
            hero.say "No, Hanna...I'm...I'm...the other thing...you know?"
            hanna.say "Happy?"
            hero.say "Yes, Hanna - I'm really, really happy!"
            show hanna happy
            "Hanna looks more startled than happy herself."
            hanna.say "Oh god, I really thought you were going to get mad...or tell me to get rid of it!"
            hero.say "No...why would I do that?"
            hanna.say "Well, that's why I took so long to tell you."
            hanna.say "First I was worried you wouldn't want it, or that you wouldn't want me anymore."
            hanna.say "Then I thought about how stressed you always are with your job, and how mine's no better..."
            hero.say "Fuck the jobs, Hanna - I don't mind scrubbing toilets if it means I can be with you...and our baby!"
            hero.say "All that's just minor details, and we'll work something out, just like people have been doing since the dawn of fucking time!"
            "Hanna throws her arms around me, almost crushing the air out of my lungs."
            "She's crying, but I'm sure that they're tears of relief and, I hope, happiness."
            $ hanna.set_flag("pregtalk",1)
    "Eventually, I have to call time on our embrace and get back to the office."
    "Hanna looks a bit of a mess, with tears still staining her cheeks."
    "But she assures me that she's fine, and we agree to meet up later that evening to discuss things further."
    "As hard as work was to deal with this morning, I think it's going to be that much worse this afternoon, with those revelations kicking around inside of my head."
    return

label hanna_masturbate:
    $ hanna.set_flag("story",1)
    scene bg black
    "There’s nothing like a nice shower after a good, sweaty workout."
    "The whole body gets reinvigorated, and I come out stepping clean and ready to tackle the rest of the day."
    "I let the water run for an extra long shower, enjoying not having to pay the water bill to feel the hot spray over my body."
    "Luckily, the gym is pretty dead this time of day, so I get the whole locker room all to myself with no one questioning me."
    "As I continue to appreciate my ‘me’ time, something makes me listen."
    "There’s a locker slam, and a shuffling of clothes. Heh, no problem."
    "Just a couple dudes in a locker room after exercising."
    "Nothing wrong with that."
    unknown_girl_say "A... ahh..."
    "W... what!?"
    "That sound—that’s no dude!"
    "There’s... a woman in here?"
    "I wrap the towel around my waist and poke my head out past the curtain."
    show hanna mast
    "I almost gasp when I see her—the woman from the treadmill!"
    "I’d recognize that tanned body and golden hair anywhere!"
    "But... she’s not wearing her gym outfit."
    "Is she... naked?"
    "Does she not know this is the men’s lockerroom?"
    "Shit... does she see me?"
    "What’s she doing?"
    unknown_girl_say "Aah... [hero.name],"
    "She lift up a piece of fabric, taking in a deep whiff and then shudders, letting out a long, sighing moan."
    "Oh fuck... that’s... that’s my underwear!"
    "She’s sniffing my boxers and... and that’s not all."
    "She lowers her one hand down along her body."
    "It still glistens with the sweat of her intense workout."
    "I can see everything, from her amazing abs and her well-toned arms, down to her legs, spread apart, her sex quivering in desire."
    "She pinches at her erect nipple, letting out a little gasp."
    "She holds my trousers in her other hand, and shuffles the fabric around until she gets right where my dick would be."
    show hanna mast b
    unknown_girl_say "Mmm fuck, that... that’s some good smell,"
    "She whispers to herself, but the echo-filled room allows me to hear all. "
    unknown_girl_say "But it doesn’t cover up your musk, [hero.name],"
    "A dreamy face fills her as she rolls her eyes back. "
    unknown_girl_say "Oh... yes..."
    "I take a few tentative steps out of the shower, tiptoeing my way to the bench, but hiding behind a series of lockers."
    "She lays on her belly, draping the underwear over her face as a blush passes over her flushed face."
    "It’s a whole pallete of intersting colors on those cheeks of hers, but she’s not done yet."
    "Her finger trails down lower on her body when she keeps talking. "
    unknown_girl_say "Y... yeah... I didn’t know how to tell you..."
    "Her fingers start rubbing over her lips. "
    unknown_girl_say "I’m a real fitness freak. I love everything.. Everything about it!"
    "She gasps as two fingers dip inside. "
    show hanna mast b wet
    unknown_girl_say "Ah, you like... you like that?"
    "She gives me no chance to answer. "
    "Does she even know I noticed her?"
    "No, obviously, she still thinks I’m in the shower. "
    "Is she... is she waiting for me to get out?"
    unknown_girl_say "Oooh... fuck me, [hero.name],"
    "Her fingers pushes deep inside of her. "
    "She rubs her clit with her palm and takes another long hit of my smell."
    unknown_girl_say "Th... that’s right! I love it. Your smell, your taste, aaanh!"
    "She lifts her ass upward, lifting up onto her toes as she cries out. "
    unknown_girl_say "Yeah, come on..., let’s do it! It’s the best exercise. Rougher, rougher!"
    unknown_girl_say "Burn those calories, build that muscle so you can pound me longer next time!"
    "She squirms, biting her lip. I can’t help myself but to keep watching."
    "Obviously, she thinks I’m some kind of fitness god."
    "With the rate she fingers herself, I start to get a little jealous with myself."
    "She throws my trousers to the side and gropes around the ground blindly as she handfucks herself."
    "I kneels down and grab my sweaty boxer shorts and toss them back closer to her."
    "Her groping fingers grip at the fabric and she brings it up to her face."
    unknown_girl_say "Oh, fuck yes..."
    "She hisses, and then just shoves the crotch right into her face. "
    unknown_girl_say "Ooooh, fuck! That musk!"
    "She laughs a little."
    unknown_girl_say "It’s the greatest smell. Come on, [hero.name], fuck me like the animals we are."
    unknown_girl_say "This... this is what our bodies are for!"
    show hanna mast wet squirt
    "She rocks her hips wildly in a rhythm with those fingers, her gasps getting louder and louder."
    hide hanna
    "I tiptoe my way back, keeping her thrusting movements in my eyesight, and soon, I get back to the shower stall."
    "With a loud slam, I turn off the water, leaving a few dripping droplets of water to fill the now quiet room."
    "From her location, she bites her finger, stifling back a few small whimpers. "
    "She then sits up quickly, shuffling into her clothes, wait... was she not wearing underwear before!?"
    "Before I could register that idea, she already closed the door, leaving me alone with the slam."
    "When I return to my bench, I whistle—the whole area doesn’t look like anyone had been there. "
    "All my clothes were back in my locker where I left them. "
    "The only thing different is the stain at the bench."
    "Here I thought this girl was out of my league. "
    "Now, it seems like I’m the one SHE looks up to."
    "..."
    "..."
    "But what the hell is her name? And how the hell do I introduce myself NOW!?"
    return

label hanna_give:
    if not "Protein powder" in hero.inventory.keys():
        $ gift = Consumable("Protein powder", money_cost = 100, effects = [("fitness",5),("hunger",1)])
        "She hands me a bottle of protein powder."
        hero.say "Wow !\nThanks!"
        hanna.say "It's nothing..."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label hanna_give_valentine:
    show hanna
    "Hanna walks hesitantly towards me."
    call hanna_greet from _call_hanna_greet_7
    show hanna blush
    hanna.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Hanna hands me a box of chocolates."
    hero.say "Thank you, Hanna."
    $ hero.gain_item(gift)
    hide hanna
    return

label hanna_give_birthday:
    show hanna
    "Hanna walks towards me."
    call hanna_greet from _call_hanna_greet_8
    show hanna happy
    hanna.say "Happy birthday [hero.name]!"
    call hanna_give from _call_hanna_give
    return

label hanna_give_christmas:
    show hanna
    "Hanna walks towards me."
    call hanna_greet from _call_hanna_greet_9
    show hanna happy
    hanna.say "Merry christmas [hero.name]."
    call hanna_give from _call_hanna_give_1
    return

label hanna_init:
    python:
        if "hanna" not in HIDDEN and not hanna.get_flag_value("story"):
            HIDDEN.append("hanna")
    return

label hanna_event_02:
    $ hanna.set_flag("story",2)
    $ hanna_love_max = 40
    if "hanna" in HIDDEN:
        $ HIDDEN.remove("hanna")
    "Well, here I am. Better get that membership renewed."
    "Can’t let my gains go to waste..."
    show hanna normal
    hero.say "No way."
    "Sitting at the desk is the girl from the locker room, the one who flicked her bean while I was taking a shower."
    "What the hell would she be doing here?"
    "She looks up a moment, her eyes widening when she sees me."
    "Oh, great, now we’re both caught in the headlights."
    hero.say "Uh... H-hi!"
    "I blurt out, pulling out my card."
    hero.say "I, uh, need to renew!"
    "She sighs and runs a hand through her blond hair, ushering me forward."
    unknown_girl_say "Ah, a-alright. Welcome to The Gym. I’m Hanna. So, let’s see, [hero.name], right?"
    "She talks while clacking away at the keyboard."
    menu:
        "Yes":
            hero.say "That’s right."
            "I slide the membership card over towards her, real professional-like."
            "She doesn’t even look at it as she puts in information into the system."
            "Trying to figure her out is going to be difficult."
            "It’s not everyone who tries to pleasure themselves to you and you don’t even know their name."
            hero.say "So, not often I see one of the members working at the desk. What’s up with that?"
        "No":
            hero.say "Actually, no, that’s not my name."
            hanna.say "W... what?"
            "She turns bright red, glancing over towards my card, and then shooting me a glare."
            hanna.say "He-hey, what are you trying to do here? Are you messing with me?"
            "I chuckle..."
            hero.say "Just seeing if you were paying attention."
            "She rolls her eyes, and then types in the system."
            hero.say "I’m not the only one being deceptive, you know. Here, I thought you were a member, not a worker."
            $ hanna.love += 5
        "How do you know?":
            hero.say "How do you know my name? I don't’ remember giving it to you."
            show hanna blush
            "She blushes at that, but types furiously into the system."
            "Obviously, I struck some kind of nerve. What is her game?."
            $ hanna.sub += 5
    show hanna normal
    hanna.say "Ah, well, that. That’s easy."
    hanna.say "My dad owns the gym."
    hanna.say "I work here from time to time, you know, when I’m not working out."
    hero.say "Ah, that makes sense."
    "Her tanktop is loose and I can nearly see all the way down to her nipples."
    hanna.say "The payment method the same?"
    hero.say "Uh, yeah!"
    hero.say "Everything the same."
    hero.say "Nothing I’d want to change around here, payment, machines, and staff."
    "She smiles at that and nods."
    hanna.say "You’re all updated. The card should still work! Hope you have a great day!"
    menu:
        "See ya":
            hero.say "Alright, cool."
            hero.say "Gonna go to the locker room now."
            hero.say "Gotta get my workout on."
            hero.say "Is there anyone in there right now?"
            "She pauses a moment, her face a blank mask a moment before she smirks."
            hanna.say "No. You’d be all alone in there."
            "And with that, I give her a nod and walk away."
            "Even if I wanted to pursue something with her, perhaps while she’s working and has my access to the gym in her hands isn’t the best time?"
            "I may be pressing it by teasing that I know her secret."
        "About treadmill":
            hero.say "You know..."
            hero.say "I couldn’t help but notice that you were checking me out the other day..."
            "Her eyes get really shifty at that."
            hanna.say "Aah, what? What are you talking about?"
            hero.say "Oh, you know... when you were on the treadmill."
            "Hanna’s fingers curl and she blows out a huge breath."
            hanna.say "I... did what?"
            hero.say "Yeah, you were stealing some glances, weren’t you?"
            "She looks off to the side a moment, scratching her cheek."
            hanna.say "I’m... not supposed to oogle the customers."
            "But you did... and I liked it."
            "For a moment, she says nothing, but she takes her hands off of the computer and places them upon her knees."
            $ hanna.love += 5
            hanna.say "I... I really need to get some work done."
        "About locker room":
            "Perhaps now that we’re finally confronting each other for the first time, I can actually get some answers out of her."
            hero.say "You know..."
            hero.say "I have been meaning to talk to you for a little while now."
            hanna.say "O... oh, why is that?"
            "She asks, though the way she bites her lip lets me know she is anticipating the exact question I am about to give her."
            hero.say "Well, I wasn’t sure what you were doing at first. I thought maybe you were lost and went to the wrong locker room."
            "She squirms in her chair, her hands moving to her knees, gripping them tightly."
            hero.say "But then, I heard you calling out my name... that was pretty weird, too."
            hero.say "But now that I know that you actually WORK here, things are starting to come together."
            "Her face turns beet red as she stares up at me, though her lips part."
            hanna.say "aah.... Ha...."
            hero.say "But there you were, lying on a bench, sniffing my stuff, and fingering yourself."
            "I lean closer into the table."
            hero.say "I just couldn’t help myself but watch you,"
            "I continue, chuckling when she pushes herself back a bit."
            hanna.say "I... I’m sorry."
            hero.say "Don’t be."
            hero.say "I’m going to exercise now. Enjoy your work. I’ll see you later."
            "I turn to leave."
            hanna.say "Wait!"
            "I stop and turn around. She has clasped her hands together, surprised at how loud she actually was."
            hanna.say "Let’s..."
            hanna.say "Let’s talk about this, when I’m off work. Here..."
            "She scribbles something down and hands me the sticky note."
            hanna.say "My number."
            hanna.say "Call me when you want us to talk."
            "I smile and give her a wave. Perhaps I’ll let my exercise wait for the day?"
            $ hanna.sub += 5
            $ hero.smartphone_contacts.append("hanna")
    return

label hanna_event_temp:
    $ hanna.set_flag("story",3)
    $ hanna_love_max = 200
    return

label hanna_event_03:
    $ hanna.set_flag("story",3)
    $ hanna_love_max = 60
    show hanna
    "After a long work out, I can’t help but notice just how much Hanna looks at me as I wipe my brow."
    hanna.say "[hero.name]. There’s no one else around. We got the whole gym by ourselves. Do you want to get cleaned off?"
    hero.say "Heh, and here I thought you liked being dirty."
    "She smirks at that and turns around heading towards the women’s lockerroom."
    hanna.say "Alright, then, see you next time!"
    hide hanna
    "I shrug and make my way back to the locker room."
    "There, I undress and get into the shower."
    "Nothing quite like washing off after a great workout, that’s for sure!"
    "As the water washes over me, the curtain opens quickly, and standing there just on the other side is Hanna, biting her lip and dressed in her white gym gear still."
    show hanna
    hanna.say "Hey there, [hero.name], mind if I join?"
    menu:
        "I mind":
            hero.say "H... Hanna!? I’m just taking a shower! What are you doing?"
            hanna.say "W... what? Oh, I’m sorry, shit! Fuck!"
            "She throws the shower closed and runs out of the room, her face beet red."
            "I think I might have fucked up."
            hide hanna
            $ hanna.love -= 5
        "I don’t mind":
            "I step back and usher Hanna inside."
            "She slowly steps on in, pressing her body up against mine, water puddling up on her chest as she sighs out."
            hanna.say "I’ve been wanting to do this since our first rep."
            hide hanna
            show hanna bj outfit
            "Soon, she slides down along my body, painting my chest with her tanktop."
            "The water spills out between and over her breasts, the white outfit getting heavy and transparent as it sticks to her body."
            "Its almost as if she is wasn’t wearing anything, but much, much hotter!"
            "Her breasts run down over my cock."
            "It springs free from between her breasts, quite ready for the attention now."
            "As the water rolls down her face, she looks up to me with half-lidded, lustful eyes."
            "She leans in, breathing with heated breaths over my skin."
            show hanna bj outfit suck
            "The hunger in her eyes is real as she takes in my member."
            "She hums, groaning louder than the spray of water as she puts her hands off of my thighs and over her tits."
            "Her lips wraps around the head of my cock as she starts to bob up and down along my length, always looking up at me as she does it, seeking my approval, craving my satisfaction."
            "The wet fabric wraps around my flesh. Honestly, I can’t say I’ve ever felt something quite like it before."
            show hanna bj outfit
            "The softness of her breasts mix with the rough stickyness of her top."
            "I wince as it catches my skin a moment, but she laughs, pulling away from my length. "
            hanna.say "Haha... yeah, a stupid idea."
            show hanna bj
            "Blushing, she peels her shirt upward and above her head."
            "As any red-blooded man would do, I take the oppurtunity and slide my dick on in between her tits until it pops out from her cleavage."
            show hanna bj suck closed
            "Now basically wearing my cock, she wraps her lips around it again, never breaking her eye contact through that entire exchange."
            "How long she goes without blinking, even in the shower, is crazy."
            "Now that her nice big tits wrap around my dick, with no sticky shirt to mess with me, I get more bold, and thrust forward."
            "She groans at the sudden increase in force, but takes it like a champ, bobbing her head over and over in the repetitive motions that only a fitness nut could truly appreciate."
            "Like I’m some kind of weights, she keeps up her tit reps."
            "She does give her body quite the workout as her tongue lashes under the head and up along the sides."
            "But even if a great athelete paces, it becomes impossible to hold out forever, and just like the runner who used too much of his speed at the beginning of the race, I can’t keep it up myself."
            show hanna bj cumshot
            "Instead, I yank her back, shooting my load all over her face."
            show hanna bj cum
            "Hanna groans in a loud and lewd cry as my cum mixes with the water already raining down on her face."
            show hanna bj
            "Soon enough, it will all wash away, but not before she runs her hands up over her cheeks and shudders."
            hanna.say "Aaah, nothing like the signs of a good workout."
            hanna.say "The body perspires... the muscles ache, the eyes grow heavy, and the cock shoots its load."
            hanna.say "It’s wonderful, isn’t it? What the body can do?"
            "I chuckle at that and sigh, leaning back against the shower."
            hero.say "Yeah, it is. But come here. Looks like you need a shower now, yourself."
            "Hanna hops up, wrapping her arms around me and pressing her chest against my body."
            "She nuzzles against me a bit, letting the water hit over our flesh for a bit longer before finally pulling away."
            hanna.say "Alright, well, could you get my back, [hero.name]?"
            "I grab the soap, delighted to do so."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
