init python:

    Event(**{
        "name":"alexis_init",
        "label": ["alexis_init"],
        "girls_conditions": {"alexis":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name":"alexis_start",
        "label": ["alexis_start"],
        "girls_conditions": {"alexis":{"flag_story":False}},
        "game_conditions": {"done":["alexis_event_01","alexis_init"]},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "alexis_give_christmas",
        "label": ["alexis_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas"},
        "girls_conditions": {"alexis":{"min_love":50,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "alexis_give_birthday",
        "label": ["alexis_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday"},
        "girls_conditions": {"alexis":{"min_love":40,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "alexis_give_valentine",
        "label": ["alexis_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine"},
        "girls_conditions": {"alexis":{"min_love":100,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "alexis_kiss_me",
        "label": ["alexis_kiss_me"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"alexis":{"min_love":150,"present":True, "valid":True, "flagmin_kiss":1}},
        "game_conditions":{"flag_female":0, "chances":20},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "alexis_pregnant_flag",
        "label": ["alexis_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"alexis":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name":"alexis_preg_talk",
        "label": ["alexis_preg_talk"],
        "duration": 0,
        "do_once": False,
        "girls_conditions": {"alexis":{"flagmin_pregnant":6,"flag_pregstory":0, "present":True}}
        })

    Event(**{
        "name": "alexis_event_02",
        "label": ["alexis_event_02"],
        "duration": 0,
        "girls_conditions": {"alexis":{"valid":True}},
        "game_conditions":{"flag_female":0, "days":"56", "hours":(14,15),"flag_dateinprogress":0, "min_money":1000},
        "do_once":True,
        })

    Activity(**{
        "name": "alexis_conv_1",
        "display_name": "About last time",
        "label": ["alexis_conv_1"],
        "duration": 0,
        "icon": "alexis",
        "game_conditions": {"activity":"interact", "flag_female":0},
        "girls_conditions": {
            "alexis":{
                "active":True,
                "flageq_story":2
                }
            },
        "do_once": True
        })

    Event(**{
        "name": "alexis_conv_2",
        "label": ["alexis_conv_2"],
        "duration": 0,
        "priority": 500,
        "game_conditions":{"hours":(9,22),"flag_dateinprogress":0,"flag_female":0},
        "girls_conditions": {
            "alexis":{
                "flageq_story":3
                }
            },
        "do_once":True,
        })


    Activity(**{
        "name": "alexis_conv_3",
        "display_name": "About last time",
        "label": ["alexis_conv_3"],
        "duration": 0,
        "icon": "alexis",
        "game_conditions": {"activity":"interact", "flag_female":0},
        "girls_conditions": {
            "alexis":{
                "active":True,
                "flageq_story":4
                }
            },
        "do_once": True
        })

label alexis_event_02:
    $ alexis_love_max = 200
    "I'm pretty much on autopilot when my phone rings, trying to manage two different tasks while remembering a couple of others that I have to take care of as soon as I've got these ones done."
    "So when I pull out my phone and see that the call is from an unknown number, I instantly make to reject it and get back to what I'm already struggling to get done."
    "But then, for some reason, I pause and decide to accept the call anyway."
    "I really can't explain what makes me do it, just one of those quirky feelings you get every so often to do something you'd normally pass over."
    hero.say "Hello?"
    "There's silence for a couple of seconds, and all that keeps me from hanging up is the sound of someone breathing on the other end."
    alexis.say "Hey, [hero.name], it's me - Alexis!"
    hero.say "Alexis...wow...erm, I was not expecting to get a call from you today!"
    "I can hear her make a little sound that could be laughter, or equally be a sly note of satisfaction."
    alexis.say "Well, surprise!"
    alexis.say "And I hope it was a good one?"
    "I'm genuinely too wrong-footed to be able to come up with anything clever to say."
    alexis.say "So, are you ready for our night out?"
    "I see my last chance to say no and get as far away as possible fading into the distance."
    hero.say "Okay, Alexis - I guess that'd be...nice."
    alexis.say "Let's meet tonight, at the restaurant."
    alexis.say "Okay - that's a date!"
    alexis.say "I'll text you the address and see you there, [hero.name]!"
    "And just like that she's back in my life and back taking control of it!"
    "And yes, I know that I just agreed to meet up with her for dinner, like a complete pussy!"
    "But it's not a date, I keep telling myself."
    "It's just two former aquaintances meeting up to compare notes and talk about old times."
    "And maybe if I keep on telling myself that for long enough, I might actually believe it too!"
    scene bg black with fade
    $ game.pass_time(6)
    scene bg highclassrestaurant
    "If I was nervous to be walking into the restaurant expecting to see Alexis waiting for me, then imagine how much it made me panic to find that she was nowhere to be seen."
    "I check my watch and glance around in the hope of spotting her, but it's no good, she's not hiding behind any of the potted plants or pillars dotted around the place."
    "At a loss what else to do, I wander over to where the maitre d' is standing, trying not to look too awkward and out of my element."
    "I mean, shit - this place is serious enough to have a damn maitre d' for god's sake!"
    "After exchanging a few clipped words with the maitre d' and being made to feel suitably moronic thanks to his superior attitude, things begin to make more sense."
    "Apparently the young lady in who's name the table has been booked called ahead to let them know that she was running late."
    "She left instructions that the gentleman she's dining with should be shown to the table to await her arrival."
    "It occurs to me, as I'm ushered into my seat, that it would have been pretty easy for Alexis to let me know she was going to be late too."
    "Already she's managed to wrong-foot me, even before I've laid eyes on her."
    "I want to believe that it's just an honest mistake, really I do."
    "But this smacks so much of the Alexis that I used to know..."
    "First the phone-call out of the blue, and now this!"
    "I resolve that when she finally does grace me with her presence, I should say something to get back on level ground with her."
    "I'm not talking about starting a blazing row or anything quite so dramatic."
    "Just being firm and laying down some basic rules, as I don't want this reunion to go the same way as our former relationship."
    show alexis date
    "But the moment that I look up and see her breezing casually into the restaurant, looking around for me, everything else seems to disappear from my mind."
    "I might have mentioned, in passing, the fact that Alexis was pretty cute back in the day."
    "Well, it looks like I remembered that wrongly."
    "Alexis was stunning...and she still is."
    "If she was a hot teenager when we were together, she's grown into an even hotter woman."
    "I can remember the tawny blonde hair, the huge eyes and the full lips."
    "But where she used to have the body of a girl yet to bloom, the black dress she's wearing now hugs the curves of an amazing feminine figure."
    "For a moment, she clutches her expensive-looking black purse to her chest as she glances around the room."
    show alexis date happy
    "Then she spots me, and waves."
    "Before I can stop myself, I'm standing up and waving back, smiling like a fool."
    "She walks over to the table, and I can hear the clacking of her high heels on the tiled floor."
    "I try to keep a sensible head on my shoulders, but she looks like something out of a damn movie right now."
    alexis.say "Hello, [hero.name], so good to see you again."
    hero.say "Y-yeah...great to see you too, Alexis."
    "I go to sit down, but Alexis gives a slight cough and nods towards her chair."
    "For a moment I'm puzzled by the gesture, until I realise that she's expecting me to pull her chair out for her."
    menu:
        "Pull out Alexis's chair":
            "I know it's a bit old-fashioned, but we are in a pretty up-market kind of place."
            "Nodding that I understand her, I hurry round to pull out Alexis's chair and make sure she's seated comfortably."
            "She smiles in approval, clearly gratified to have me treat her in such a gentlemanly manner."
            $ alexis.sub -= 5
            $ alexis.love += 1
        "Don't":
            "Jesus wept - I'm meeting an old girlfriend for a meal in the twenty-first century."
            "Not courting a prospective bride on the maiden voyage of the Titanic!"
            "I pretend not to have understood what Alexis was expecting of me and just sit straight back down."
            "I can tell from the expression on her face that she's momentarily put out."
            "But she'd have to call me out on it and look like a bit of a bitch in doing so, and instead she chooses to ignore the whole matter and just sit down herself."
    "As the menus arrive and I realise that this place is so much style over substance that I haven't been able to even guess what the cuisine they're serving is, we try to make small-talk."
    hero.say "I'm guessing there was a bit of a mix-up with the times tonight?"
    "Alexis smiles at me over the top of her menu and lightly waves the comment away."
    hide alexis
    show alexis date
    alexis.say "Oh, [hero.name], that's fine - there's no need to apologise!"
    "What - did she actually just let me off the hook for something that she did?!?"
    "I open my mouth to object, but find myself interrupted by the arrival of the waiter to take our orders."
    "Unable to give Alexis a piece of my mind in front of someone else, I simply have to simmer down and pretend not to be annoyed at what she just did."
    "I'm feeling pretty wound up and distracted by now, and I just pick something almost at random from the menu before handing it back to the hovering waiter."
    alexis.say "It's so nice of you to agree to this, [hero.name]."
    alexis.say "I know we didn't part on the best of terms..."
    "Now there's quite the understatement."
    alexis.say "There were things we both did wrong..."
    "Both of us - really?"
    "I'd like to see the list of grievances against my name from back then!"
    alexis.say "But that was so long ago now."
    "I can feel teeth almost grinding together as I grit them and reply in a diplomatic manner."
    hero.say "That's all in the past now, Alexis."
    hero.say "I'd like to think that we've grown into different people since then."
    "That answer seems to be the one that Alexis was looking for, and the mood begins to lighten from that point on."
    "We eat a couple of courses of way too expensive food and drink a bottle of wine that I suppose must be a decent one (it's expensive enough!)."
    "The talk turns to memories of being at school, with both of us being careful to avoid any sensitive topics."
    "I've almost forgotten all of the things that Alexis has done to irritate me tonight."
    "That is until I hear a deep, impossibly masculine voice intruding on the moment."
    man_say "Damn, girl - you're something else!"
    "I look up to see a guy towering over me that instantly makes me almost jump in my seat."
    "He's well over six feet tall, built like a professional athlete and shows off rugged good looks as he smiles down at Alexis."
    "She's already returning his smile, soaking up the adoration of this ebony demi-god that's decided to crash our private dinner."
    show alexis date flirt blush
    alexis.say "Aww...that's so kind of you to say!"
    alexis.say "Tell me, do you work out?"
    alexis.say "I mean, you look like you must play ball or something, right?"
    "I can't believe that she's actually flirting with this guy, right in front of me!"
    "I know we kind of, sort of said this wasn't really a date."
    "But we both know that it kind of, sort of actually is!"
    menu:
        "Say something" if hero.fitness >= 25 and hero.charm >= 25:
            hero.say "Hey, do you two mind doing your flirting on your own damn time!"
            "My angry words shatter the convivial mood that was fast building between Alexis and the other guy."
            show alexis date angry
            "She looks at me with barely concealed annoyance in her eyes."
            "But to give him his credit, the guy seems to notice me for the first time."
            man_say "Hey, chill, bro - it's cool."
            man_say "I didn't know I was cramping your style...no need to get mad."
            "He holds up a hand to acknowledge that he's backing off and that, as far as he's concerned, the matter's over and done with."
            "Alexis keeps her mouth shut as the guy walks away, but the rest of the night is irrevocably tainted by the incident."
            "We eat the rest of our meal in a cold near silence and then go our separate ways."
            $ alexis.set_flag("story",2)
            $ game.pass_time(2)
            return
        "Say nothing":
            "I could speak up, but then this is supposed to be something that's not quite a date."
            "I don't really have any right to stop Alexis from talking to whoever she chooses."
            man_say "That's right, I play quarterback - you're a very perceptive young lady, you know that?"
            alexis.say "Let's just say that I have a lot of experience when it comes to spotting a pedigree athlete!"
            "The stranger beams at the compliment, but then seems to notice me for the first time."
            man_say "Oh, my apologies - I didn't see your man there."
            alexis.say "Who, [hero.name]?"
            alexis.say "Oh, he's okay - we're old friends catching up on old times."
            man_say "That's cool...but don't forget to keep some space aside for NEW friends?"
            man_say "You know what I'm saying?"
            "With that he walks off and leaves us alone again."
    hide alexis
    show alexis date
    "We continue eating, but the tone of conversation is more muted now."
    "I could make an effort to inject new life into it, but the sight of Alexis flirting so openly in front of me makes me wonder what the point would be."
    "She's practically made it clear to me with that one act that this isn't some desperate attempt on her part to make things right between us."
    "Maybe the best I can hope for is to come out of this in one piece and with her as a kind of platonic friend, one that I can easily make excuses not to see ever again?"
    hide alexis
    "Just before we order dessert, Alexis excuses herself to go to the bathroom."
    "I don't notice how long she's been gone until the waiter comes back a second time to ask if we're ready to order yet."
    "Telling him to come back in five minutes, I begin to wonder what's keeping Alexis."
    menu:
        "Go check on her":
            "I get up as discreetly as I can and hurry over to the toilets."
            "It's only then that I realise I have absolutely no idea of how to check on Alexis in the women's bathroom."
            "I can't start hammering on the door or shouting her name, and walking straight in just isn't an option either."
            "In the end I settle for going into the men's bathroom instead, hoping that the wall between the two will be thin enough for me to hear what's happening on the other side."
            "But as soon as I walk in through the door, I disturb one of the waiters, who jumps at the sight of me and quickly scuttles out."
            "For a moment I can't make sense of it, thinking that restaurants usually have toilets in the back for staff."
            "It's only when I hear the sounds coming from the last cubicle that I begin to understand what he was actually doing in here."
            "The groans and moans emanating from behind the locked door can mean only one thing."
            "And I think that I'd honestly made up my mind what I was going to see, even before I walked into the second-to-last cubicle and stood on the toilet seat to peer over."
            show alexis reverse toilets dickin
            "There's the stranger that stopped at our table not twenty minutes ago."
            "And there's Alexis, riding him like her life depended on it."
            menu:
                "Leave":
                    "I could have lived with her chatting another guy up, even in my company."
                    "But shit like this is just too much for me to put up with."
                    "It's proof positive that Alexis hasn't changed one bit since we were together all those years ago."
                    "I jump down from the toilet seat and storm out of the men's bathroom, not caring if either of them hears me as I go."
                    hide alexis
                    "The waiter sees me grabbing my coat, and hurries over to make sure someone pays the bill."
                    "I sneer at his fake courtesy and tell him rather bluntly that the lady will be settling the cheque for tonight's meal."
                    "Alexis, I think, has already made me pay in more ways than one."
                    $ alexis.set_flag("story",3)
                    return
                "Watch":
                    "I should walk away from this, or at least have the balls to interrupt them."
                    "But instead I find myself compelled to remain silent and watch as they fuck in the next stall."
                    "I don't get to see everything, as I've evidently walked in on them while they're in the middle of it all."
                    "Both of them are stripped naked, the stranger sitting astride the toilet and Alexis straddling his considerable lap."
                    "Neither of them speaks, and they're trying to keep as quiet as possible, though not really succeeding."
                    "I suppose it won't surprise you to learn that the guy's cock is simply massive."
                    "It stands erect and proud, perhaps an inch below Alexis's pussy as he literally holds her above it."
                    "Though I can see her naked body without any kind of impediment, I keep finding myself drawn back to the expression on Alexis's face as she's lowered slowly onto the waiting cock."
                    "It's not one that I can ever recall seeing her show before, desperate, needy and almost, well...almost shameful."
                    "I watch as she bites her lip, almost expecting to see blood flow, in an effort to keep quiet as she slides down onto the huge cock beneath her."
                    "This isn't a long, drawn out instance of making love."
                    "It's just two strangers fucking for the thrill of it in a toilet."
                    "The stranger holds the underside of Alexis's thighs so that he can more easily lift her up and down on his manhood."
                    "And with every thrust, she gasps more loudly, while her face becomes ever more flushed, her eyes more distant and cold."
                    show alexis reverse toilets dickin pussy
                    "It's not long before the guy cums inside of her, filling Alexis to the point where it begins to leak out even before he pulls out of her stretched pussy."


                    show alexis reverse toilets dickout creampie ahegao
                    "Her head lolls like that of a puppet with severed strings, and her tongue lolls out of her open mouth."
                    hide alexis
                    "Sensing that the end is fast approaching, I hop down from my perch as quietly as I can manage and hurry back to our table."
                    "When Alexis returns a few minutes later, I try not to notice the signs of dishevelment that she's not been able to hide."
                    "The conversation is muted from then on, but I decide to play along with her excuse of being tired."
                    "We see out the end of the meal with this pretence of ignorance still going on."
                    "But all the time, my mind is racing thanks to what I've seen and the things that it could imply."
                    $ alexis.set_flag("story",4)
                    $ hero.money -= 1000
                    return
        "Wait":
            "It seems to take forever for Alexis to wrap things up in the bathroom and make it back to the table."
            "She looks a little worse for wear when she sits down, but assures me that she's just feeling a little tired and that there's nothing more to worry about."
            "I try to forget about it and focus on ordering dessert, but a knowing grin on the waiter's face still bugs me all the same."
    "The rest of the meal passes fairly pleasantly and without incident."
    "Only when the bill arrives and Alexis smiles at the waiter do I feel like the old annoyances are creeping back in once more."
    alexis.say "My date will be handling the cheque."
    "My eyes almost pop out of my head, as I've been keeping a rough estimate of the evening's cost in the back of my mind."
    "Luckily Alexis is still looking at the waiter when this happens, and I manage to pull my face back into something resembling a blithe grin when she does turn back to me."
    alexis.say "It's so kind of you to agree to treat me like this!"
    "She flutters her eyelids as I allow the waiter to rob me blind."
    "I just hope this is a simple case of miscommunication, and that Alexis isn't a gold-digger that's eyeing me up as her latest claim."
    $ hero.money -= 1000
    $ alexis.set_flag("story",1)
    $ game.pass_time(2)
    return

label alexis_conv_1:
    show alexis
    hero.say "Look, I just wanted to have it out about what happened at the restaurant the other night."
    "Alexis pause, the silence becoming almost instantly pregnant."
    alexis.say "Okay...I'm listening."
    menu:
        "Apologize":
            hero.say "I just wanted to say sorry for getting upset when you were talking to that guy."
            hero.say "It was way out of order - I have no right to tell you who you can and can't talk to."
            alexis.say "It's okay, really...don't worry about it."
            hero.say "No, it's not - I got too possessive and jealous, even when we weren't supposed to be officially on a date."
            show alexis happy
            "Alexis chuckles to herself, and she shakes her head at me."
            alexis.say "Like I already said, it's no big deal, [hero.name]."
            alexis.say "In fact, it was kind of flattering, the way you wanted me all to yourself!"
            hero.say "Well...I guess I'd just forgotten how much I liked spending time in your company, that's all."
            alexis.say "What do you say we just put it behind us and move on?"
            alexis.say "I think I'd like to hear more about just how much time you want to spend on me..."
            $ alexis.set_flag("story",1)
        "Tell her off":
            hero.say "I won't agree to see you again if you keep on behaving like that in front of me, Alexis."
            hero.say "I'm sorry if that makes me sound like a jealous prick of a throwback to a less enlightened time."
            hero.say "But we're not in High School anymore, and I won't put up with someone flirting in front of me like that."
            "Alexis is silent for a while, probably taken aback by the strength of my ultimatum."
            show alexis confused
            alexis.say "Okay, [hero.name]...I...I guess I didn't realise how strongly you felt about that kind of thing..."
            "I let out a frustrated sigh, afraid of sounding like a jealous ogre over what she probably regards as something completely harmless."
            hero.say "Look, I think we made a mistake by going into this whole idea of us getting to know each other again a bit naively."
            hero.say "We can't hide the fact that we both have a lot of emotional baggage that we're still carrying from the past."
            alexis.say "I guess so..."
            hero.say "What I'm saying is that I think we need to establish a few small ground-rules - and that no flirting while we're together is one of them."
            hero.say "By that I mean no flirting with other people...not each other."
            hero.say "Not that I'm saying you HAVE to flirt with me - unless you want to, that is!"
            "Alexis laughs, genuinely for the first time during our conversation."
            alexis.say "Don't worry, I think I get what you mean!"
    "Hopefully I haven't killed this thing before it got started over something that was nothing to worry about in the first place."
    return

label alexis_conv_2:
    play sound "sd/cell_vibrate.mp3"
    pause 1.0
    "I'm still feeling humiliated and more than a little stupid for thinking that she might have turned over a new leaf when my phone suddenly rings."
    "Seeing Alexis's name on the call ID almost makes me ignore the thing altogether."
    "But then I wonder if I shouldn't hear what she has to say."
    "Who knows, maybe she's spent all night stewing in it too."
    "Maybe she's actually come to the conclusion that screwing one guy in the bathroom while on a date with another is just a little bit rude."
    "I accept the call and steel myself for what's awaiting me on the other end."
    hero.say "Good morning, Alexis."
    "My tone is as flat and emotionless as I can make it, under the circumstances."
    alexis.say "YOU FUCKING PRICK!"
    "Well, I guess that answers the question about whether or not she's calling to apologise."
    alexis.say "Where in the HELL do you think you can get away with skipping out on me like that?!?"
    alexis.say "I come back from the bathroom, and you've walked out..."
    alexis.say "Worse than that, you left me to pick up the bill!"
    "I keep quiet, letting her rant away and list her perceived grievances, hoping that she'll eventually run out of steam."
    alexis.say "I have NEVER been so humiliated..."
    "But at the use of that word, I just can't keep from jumping in."
    hero.say "Oh, for the love of god, Alexis - shut up for a second and actually listen to yourself."
    hero.say "Sure, I walked out on you last night, I admit it."
    hero.say "But it was only after I walked in on you while you were in the men's bathroom."
    "There's a silence on the other end of the line at that."
    "The kind that usually signifies that the goalposts in the argument are in the process of moving."
    hero.say "Are you still there, Alexis?"
    alexis.say "Yes...I can...listen, I can explain..."
    "This should be good."
    alexis.say "You...you weren't supposed to see that, [hero.name]..."
    hero.say "Yeah, Alexis - I kinda figured that one out for myself!"
    alexis.say "No...that's not what I meant...it's more complicated than I can say over the phone..."
    "Complicated, really?"
    "It looks like I'm going to have to lay down the law on this one."
    menu:
        "Tell her that you don't want to see her again":
            hero.say "Look, Alexis - I thought that it'd be great to see you again, that we'd likely both changed."
            hero.say "But I guess what I saw last night proved that I was only half right."
            hero.say "I might have changed, but you're still up to the same old shit you were back in the day."
            alexis.say "[hero.name], please..."
            hero.say "What are you going to tell me, Alexis?"
            hero.say "How can you spin the fact that I caught you fucking another guy into a positive thing?"
            "There's no immediate response to that."
            "But then I was hardly expecting one."
            hero.say "Alexis, I think I'd prefer it if we didn't see each other again...period."
            "It hurts to end the call like that, but I can't honestly see that I have another choice."
            $ alexis_love_max = 0
            $ alexis_love = 0
            $ HIDDEN.append("alexis")
        "Demand that she never do it again":
            hero.say "Last night was a serious screw-up on your part, Alexis."
            hero.say "But...I guess that as we weren't officially on an actual date, we can chalk it up to a mistake and try again."
            alexis.say "You'd be okay with that?"
            "Alexis sounds as though she was expecting me to go off the deep end and dump her or something."
            "Which would have been hard, as we're not actually dating yet!"
            hero.say "I just think that we need to establish some ground rules, Alexis, that's all."
            hero.say "Maybe the first of which would be that we lay off excusing ourselves to fuck other people while we're together?"
            "She had to laugh at the frank nature of my last statement."
            alexis.say "But what if they're like REALLY hot?"
            "The sarcasm and amusement in her voice suddenly reminds me of the Alexis that I always wanted to reconnect with."
            hero.say "I think we need to tackle that on a hottie by hottie basis, Alexis!"
    "I end the call still feeling somewhat emotionally hungover from the night before and its fallout."
    "But there's a kernel of hope that I can sense, deep down in my gut."
    "I think that I might have just made the right decision for the both of us."
    return

label alexis_conv_3:
    show alexis
    "I don't think that I let on what I saw Alexis and the stranger doing in the men's bathroom the other night, or gave her a clue I suspected something was up."
    "But that means that I'm now left trying to bury that mental image, while all the time pretending that everything's okay and I'm convinced that Alexis is a changed woman."
    "I'm supposed to just get up and go about my day as though nothing untoward happened and nothing's bugging me."
    "In the end, I decide that it's better to talk to her and have it out than to just sit here stewing."
    hero.say "Well, Alexis - I had a pretty great time last night."
    hero.say "But..."
    menu:
        "Confront Alexis about her cheating on you":
            hero.say "...I got worried when you were taking so long in the bathroom last night."
            hero.say "So I went to check on you...and I saw you with that other guy."
            "There's a long, drawn-out silence on the other end of the line as the significance of my words sinks in for Alexis."
            show alexis confused
            alexis.say "[hero.name]...that wasn't what it looked like...I..."
            "Seriously, that's the best excuse she can come up with?"
            hero.say "What was it supposed to look like, Alexis?"
            hero.say "Because to me, it looked like you'd snuck off to fuck another guy in the middle of our date."
            hero.say "Or was it the angle that I was watching you from?"
            hero.say "Should I have been looking under the door rather than over the top of the stalls?"
            show alexis sad
            alexis.say "[hero.name], you're not letting me explain..."
            hero.say "What's there to explain, Alexis?"
            hero.say "Apart from that I thought you might have changed and you proved me wrong?"
            show alexis cry
            alexis.say "If you'd just..."
            hero.say "No, Alexis - no more excuses and lies."
            hero.say "We're done!"
            "And with that, I cut her off before she can say another word."
            $ alexis_love_max = 0
            $ alexis_love = 0
            $ HIDDEN.append("alexis")
            return
        "Ignore the cheating":
            hero.say "...I guess I can't wait to know when I'm gonna get to see you again!"
            show alexis blush
            "Alexis chuckles sweetly at this, clearly flattered by my neediness."
            alexis.say "You need to be just a little more patient, [hero.name]!"
            alexis.say "But I promise that you can see more of me real soon..."
            "From there the conversation turns to the subject of when and where we're going to see each other next."
            "All the time I feel kind of bad for not confronting Alexis about the fact I caught her cheating on me."
            "But the more I think about it, the more I realise just how much I got off on watching her being fucked by another guy."
            "I don't know if it was just the voyeurism involved, or that I actually got to watch what she tried to hide from me when we were an item in the past."
            "Either way, it made me feel as though I was a part of what she was doing somehow."
            "The fact that I was a secretive watcher turned the act from one of simple cheating into something I could enjoy in a twisted manner."
            "Unlike when she went behind my back in the past, this time I was already aware of her predilection to cheat."
            "That put the suspicion in my mind and made me go looking when she lingered in the bathroom."
            "Perhaps that's the crux of it all - now that I'm aware of what she's doing, I feel more like I have a share of the power?"
            "I could confront Alexis at any time and place, but that's all in my hands."
            "Or I can choose to keep her in the dark and continue to watch as she fucks whoever she pleases, thinking that she's doing so without the slightest suspicion on my part."
    "At the end of the call I feel a little light-headed on account of the serious stuff that just got decided."
    "But the way in which the incident in the men's bathroom last night had been dominating my thoughts seems to have passed."
    "There might be other potential fallout from the way I left things with Alexis."
    "But I think that, in the short term at least, I've dealt with one nagging problem for sure."
    return

label alexis_preg_talk:
    "It'd be fair to say that I walk into what I thought was supposed to be nothing more than a chance to meet Alexis with my guard well and truly down."
    show alexis
    "But almost the same moment that I see her face for the first time, I can tell that I'm actually walking into something pretty damn heavy."
    "She greets me with an expression that's equal parts pained and a visible effort to put on a brave face."
    hero.say "Hey, Alexis...what's up?"
    hero.say "You look like you've got the weight of the world on your shoulders."
    "She gives me another pained look, and takes a deep breath, as if steeling herself for what she's about to say."
    alexis.say "You could say that, [hero.name]..."
    alexis.say "I don't know how best to get this out, so I'm just going to say it."
    "Oh shit - here we go!"
    alexis.say "You know how we've been getting on so well these past few weeks?"
    "I nod quickly"
    alexis.say "How we've been having a lot of fun - like multiple amounts of fun, sometimes on the same occasion?"
    "My nodding is getting more frantic now, as I begin to get the gist of what she's trying to tell me."
    alexis.say "Well, let's just say that a little something I picked up at the chemist's told me that we might have had too much fun!"
    alexis.say "Specifically, unprotected fun..."
    "Ah, I see what she means now."
    hero.say "You mean you're..."
    alexis.say "Yes, [hero.name] - I'm pregnant."
    "The weight of what she's just told me begins to sink in, almost making me want to sit down in sympathy."
    hero.say "And, well...what do you want to do about it?"
    "Alexis shakes her head, partly from genuine confusion and, I sense, at least a little from frustration at my passive response to such momentous news."
    alexis.say "I don't really know, [hero.name]."
    alexis.say "But I thought that I should tell you the truth, and maybe we could work that out together."
    "It occurs to me that Alexis must have known about this for at least a little amount of time before she told me."
    "And I wonder if she's really wanting to ask me for my input, or she's actually made her mind up already."
    hero.say "Wow...this has kind of dropped on me, Alexis."
    hero.say "Maybe if you tell me what you think, just off the cuff, I could use that to get my own thoughts straight too?"
    if alexis.love >= 150:
        "Alexis sighs and takes a hold of my hand, squeezing it tightly as she looks me straight in the eyes."
        alexis.say "I love you, [hero.name], and that's the truth."
        alexis.say "What I want is to have the baby and for us to raise it together, as a family."
        alexis.say "Look, I know we had issues in the past...that I did things that hurt you deeply."
        alexis.say "But we've looked the past in the face now and moved on together, haven't we?"
        show alexis flirt
        "She pauses for a moment, the emotion of what she's telling me clearly playing on her face as she does so."
        alexis.say "I don't think those hurtful things make us weak, I think that overcoming them made us stronger than before."
        alexis.say "In fact, I think that'd make a pretty sound base on which we could even build a marriage..."
    else:
        "Alexis smiles at me in an oddly amorous way, given the subject that we've just been discussing."
        "She leans in closer, placing her hand atop mine and beginning to stroke it with her fingers."
        show alexis happy
        alexis.say "Well, as you were man enough to get me in the family way, how about you go all the way with it?"
        alexis.say "I'm tired of being on my own and having no one to devote myself to in life."
        alexis.say "What I really want is the chance to settle down and become a happy little wife for you."
        show alexis blush
        "Her smile becomes wider still, and she now has a wicked glint in her eyes."
        alexis.say "And let's just say that I don't want to be one of these 'modern wives' either."
        alexis.say "When I promise to love, honour and obey you, then I really mean it."
        alexis.say "No matter what you might want - I'll always obey..."
    "And I thought just being hit with the news of the pregnancy was enough to make me confused and conflicted!"
    "What Alexis just added to that is equal parts dream come true and terrifying nightmare, depending simply on whether I choose to trust her or not."
    "I mull over what she's said for a moment, wondering if I should ask her for more time to consider my answer."
    "But one look into her eyes tells me that she's expecting one here and now."
    menu:
        "You should have a termination":
            "I puff my cheeks out in preparation for saying something that I know isn't going to go down well."
            "But I feel that I wouldn't be playing it fair if I chose to say something else for the sake of being liked."
            hero.say "Alexis, I hate to say this, but I think you should seriously think about having a termination."
            hide alexis
            show alexis angry
            "She stares at me for a moment, dumbfounded."
            "And then her face becomes angry, almost outraged."
            alexis.say "[hero.name]...how in the hell can you even think of such a thing?"
            alexis.say "This is a human being we're talking about - your own kid!"
            "I prepare myself again, as here comes the low blow that I'm not proud of, but I think needs to be delivered all the same."
            hero.say "You say it's mine, Alexis - but we both know that's not a certain thing."
            show alexis sad
            "Her anger abates for a moment, replaced with shock and genuine pain."
            "I know instantly that what I just said has hurt Alexis deeply, and I wish I could take it back."
            "But I won't."
            hero.say "You were a cheater back then, Alexis, and you're still a cheater now."
            hero.say "I don't want to turn down raising a family with you because of that, though."
            hero.say "I just won't raise kids with someone that I can't trust, as it wouldn't be fair on them."
            show alexis cry
            "Alexis has no answer to that."
            "Instead she just shakes her head as she backs away, then turns and runs from me."
            "The worst part is that I can tell she's trying to keep me from seeing the tears running down her face as she does so."
            $ alexis.set_flag("nodate")
            $ alexis.set_flag("nokiss")
            $ alexis.love -= 50
            $ alexis.set_flag("pregstory",2)
        "I want to raise the child with you":
            "I take a deep breath in preparation for what I'm going to say next, knowing that it will change my life forever."
            hero.say "You know what, Alexis - I think you're one hundred percent right."
            "Alexis looks at me with a hopeful expression, almost unable to believe what I just told her."
            alexis.say "You mean..."
            hero.say "I mean that we should totally make a go of raising the kid together."
            "Before I can say another word, Alexis wraps her arms around me and pulls me into a ferocious hug."
            "My face us buried in her hair, and all I can feel is the pleasant sensation of her body pressing itself against mine."
            "It takes me a while to realise that I can hear something, a sound that Alexis is making, even as she's still hugging me."
            "I pull back a little, and notice that she's crying in my arms."
            hero.say "Alexis, what's the matter...why are you crying?"
            "She sobs and sniffles a little as she tries to explain herself."
            alexis.say "I'm happy, really I am..."
            alexis.say "It's just that...you showed me that you really do forgive me for what I did to you before..."
            hero.say "Alexis, of course I do...we were kids, and you're a different person now!"
            alexis.say "I know, I know...but I never really believed it myself before now."
            alexis.say "I always thought I'd be tainted by it somehow..."
            alexis.say "But I can put it behind me now, start over again."
            alexis.say "Oh, [hero.name]...I promise I'll make you so happy!"
            hero.say "You already did, Alexis."
            $ alexis.love += 10
            $ alexis.set_flag("pregstory",1)
    "Two lives changed forever thanks to just one little conversation."
    "But a conversation with consequences that were far from little in their implications."
    return

label alexis_pregnant_flag:
    $ alexis.set_flag("pregnant",1,mod="+")
    return

label alexis_kiss_me:
    hide alexis
    show expression "alexis kiss "+alexis.get_clothes()
    "I don't know what I've said or done to make Alexis feel the way that she must be feeling right now."
    "All I know is that the moment I turn my head towards her, I'm met by the sensation of her lips pressing against mine."
    "They're softer than I remember them ever being in the past."
    "And they move gently against my own in a way that tells me she wants this kiss badly."
    "I go slowly at first, letting her show me what she desires and not even trying to assert myself."
    "Looking at the way her eyes are so delicately closed suddenly makes me aware that I've kept mine open just to look at her."
    "I close them and try to focus only on the experience of Alexis feeling me out in such an enjoyable manner."
    "Alexis doesn't rush to slip her tongue between my lips, and instead I feel it tentatively reaching out, a little more each time."
    "Soon she musters the courage to explore further, and I hear her breathing become that much more intense as she does so."
    "All this time, neither of us touches the other with any other part of our bodies."
    "More than once I feel my hands begin to reach out for Alexis, but somehow the tenderness and intensity of the kiss always defeats me in this."
    "It's almost as if I fear that touching her will somehow break the spell, and that no subsequent kiss will be as special as this one is right now."
    hide expression "alexis kiss "+alexis.get_clothes()
    $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != alexis and renpy.has_label(g.id+"_cheated")]
    if cheated_girls:
        call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_127
    return

label alexis_start:
    $ alexis_love_max = 40
    if "alexis" in HIDDEN:
        $ HIDDEN.remove("alexis")
    return

label alexis_give:
    alexis.say "What do you think about your present?"
    hero.say "What present?"
    alexis.say "The necklace I am wearing, silly."
    hero.say "!?"
    alexis.say "I bought it just so that you could see me wearing it..."
    return

label alexis_give_valentine:
    show alexis
    "Alexis walks hesitantly towards me."
    call alexis_greet from _call_alexis_greet_7
    show alexis blush
    alexis.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Alexis hands me a box of chocolates."
    hero.say "Thank you, Alexis."
    $ hero.gain_item(gift)
    hide alexis
    return

label alexis_give_birthday:
    show alexis
    "Alexis walks towards me."
    call alexis_greet from _call_alexis_greet_8
    show alexis happy
    alexis.say "Happy birthday [hero.name]!"
    call alexis_give from _call_alexis_give
    return

label alexis_give_christmas:
    show alexis
    "Alexis walks towards me."
    call alexis_greet from _call_alexis_greet_9
    show alexis happy
    alexis.say "Merry christmas [hero.name]."
    call alexis_give from _call_alexis_give_1
    return

label alexis_init:
    if "alexis" not in HIDDEN:
        $ HIDDEN.append("alexis")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
