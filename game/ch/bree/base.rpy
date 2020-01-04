init -1 python:
    Activity(**{
        "name": "have_a_meal_with_bree",
        "hunger": 10,
        "fun": 1,
        "game_conditions": {
            "max_hunger":9,
            "min_hunger":0,
            "min_grooming":0,
            "min_fun":0,
            "min_energy":0, 
            "room":["kitchen"], 
            "flag_female":0
            },
        "icon":"eat",
        "max_girls": 1,
        "girls_conditions": {
            "bree":{
                "present":True,
                "activity":"meal",
                "valid":True
                }
            },
        "display_name": "Eat with Bree",
        "label": ["bree_meal"]
        })

    Activity(**{
        "name": "watch_tv_with_bree",
        "duration": 2,
        "fun": 3,
        "icon":"tv",
        "display_name": "Watch TV with Bree",
        "girls_conditions": {
            "bree":{
                "present":True,
                "activity":["tv"],
                "valid":True
                },
            "sasha":{
                "not_activity":["tv"],
                "valid":True
                }
            },
        "game_conditions": {
            "room":["livingroom"],
            "min_fun":0, 
            "flag_female":0
            },
        "label": ["bree_tv"]
        })

    Activity(**{
        "name": "watch_tv_with_bree_b",
        "duration": 2,
        "fun": 3,
        "icon":"tv",
        "display_name": "Watch TV with Bree",
        "girls_conditions": {
            "bree":{
                "present":True,
                "activity":["tv"],
                "valid":True
                },
            "sasha":{
                "valid":False
                }
            },
        "game_conditions": {
            "room":["livingroom"],
            "min_fun":0, 
            "flag_female":0
            },
        "label": ["bree_tv"]
        })

    Activity(**{
        "name": "play_in_the_pool_with_bree",
        "duration": 1,
        "fun": 3,
        "icon":"playpool",
        "display_name": "Play with Bree",
        "girls_conditions": {
            "bree":{
                "present":True,
                "min_love": 10,
                "valid":True
                },
            "sasha":{
                "present":False
                },
            },
        "game_conditions": {
            "room":["pool"],
            "seasons":"01", 
            "flag_female":0
            },
        "once_day":True,
        "required_item": "swimsuit",
        "label": ["bree_play_pool"]
        })

    Event(**{
        "name":"bree_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "bree",
        "girls_conditions": {"bree":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"bree_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "bree",
        "girls_conditions": {"bree":{"contact":"bree","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(13,14),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"bree_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "bree",
        "priority":100,
        "girls_conditions": {"bree":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"bree_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "bree",
        "priority":100,
        "girls_conditions": {"bree":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"bree_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "bree",
        "priority":100,
        "girls_conditions": {"bree":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_bree_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"bree_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "bree",
        "priority":100,
        "girls_conditions": {"bree":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"bree_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "bree",
        "girls_conditions": {"bree":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name": "bree_masturbation",
        "priority": 500,
        "label": ["bree_masturbation"],
        "duration": 1,
        "game_conditions":{"hours":(20,3),"chances":25, "activity":"knock_bedroom2", "flag_female":0},
        "girls_conditions": {"bree":{"room": ["bedroom2"],'valid':True}},
        "do_once":False,
        "once_day":True,
        "quit": True
        })

label bree_masturbation:
    $ hero.activity.set_flag("canceled",True)
    "I'm only on my hands and knees because I dropped my phone, and I only dropped my phone because I tripped over my own feet."
    "And it's not my fault that I just happened to do all of this in the corridor outside of Bree's bedroom door either."
    "My honest intention is to do nothing more than scoop it up and get back to my feet."
    "But then I hear a sound coming from the other side of the door and realise how close I am to the keyhole."
    "I guess curiosity just gets the better of me, and before I know it, I'm kneeling in from of the door."
    "Putting my eye to the keyhole, I get a pretty good view of Bree's bedroom."
    "Although I quickly forget about everything else as soon as I see what's happening on the bed."
    "It's no great surprise to find out that the person laid upon the bed is Bree herself."
    "But the fact that she's currently naked and in the middle of doing something rather intimate is enough to instantly root me to the spot."
    "Bree's reclining on her side, her legs pulled up so as to better spread her thighs and expose what lies between them."
    "It would be pretty obvious what she's up to, even if I couldn't see what's going on between her legs right now."
    "The flushed colour of her face and the intense sounds she's making would be more than enough to give it away."
    "I'd guess that I've stumbled upon Bree just as she's building towards the climax of a pretty intense session of pleasing herself."
    if bree.sub <= 25:
        show bree mast finger
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        "I can't see any trace of toys or other means of getting herself off lying around within easy reach on the bed."
        "So it seems most likely that Bree's managed to get this far with only her own fingers and the power of her imagination."
        "I have to admit that, while I'm pretty into the idea of toys in the bedroom, it's quite a turn on to think she can get this worked up with no help whatsoever."
        "While one of her hand is playing with her pussy, the other busies itself by squeezing at the closest breast."
        "For a moment, I find my attention dragged away from the more obvious draw of the first hand, watching the movements of the second."
        "Bree massages her breast as if hoping to somehow release the tension evident in her quivering body."
        "But at the same time, Bree's fingertips twist and pinch at her nipple."
        "And this seems to have the opposite effect, only making her moan with ever more intensity than before."
    elif bree.sub <= 50:
        show bree mast finger
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        hide bree
        show bree mast small
        "A slippery, slithering sound alerts me to just what Bree's free hand is doing, as she produces a lubed-up dildo from somewhere amongst the sheets."
        "The folds of her pussy are already slick, and the dildo begins to sink between the lips almost the moment she begins to push it inside of her."
        "I'm almost as amazed at the sound that it makes as the sight of it, squeaking and squelching like rubber against rubber."
        "And accompanied by the moans that Bree starts to make as she works the dildo in and out of herself, it's something I can't help but watch in fascination."
        "I never thought that I'd envy a plastic cock so much, but the sight of what she's doing to that thing is making me pine for the same treatment."
        "All of the passion and pleasure that Bree's stirring inside of herself is being expressed by what she's doing with the dildo."
        "I wish so much that it was my own cock inside of her right now that it almost hurts to keep on watching."
        "But there's no way that I'm going to miss out on seeing more because I'm jealous of a sex-toy!"
    elif bree.get_flag_value("anal"):
        show bree mast finger
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        "A slippery, slithering sound alerts me to just what Bree's free hand is doing, as she produces a lubed-up dildo from somewhere amongst the sheets."
        "For a moment, I fully expect her to use the hand already working her pussy to part them, so that she can push the dildo inside."
        hide bree
        show bree mast ass small
        "But then she surprises me by reaching around and actually beginning to shove the entire thing between her buttocks."
        "Though the angle from which I'm watching means I can't see the dildo go on, I can certainly hear the sucking, squelching sound as it does so."
        "And every inch of its progress is written on Bree's face, as she grimaces and moans at the sensation of it parting the muscles of her backside."
        "The deeper the toy goes, the more intensely she grimaces in delightful pain and rubs yet harder at her already tingling pussy."
        "By the time Bree's managed to work it in so deep that her fingers are touching her buttocks, there are actual tears welling in the corner of her eyes."
        "I never thought that I'd envy a plastic cock so much, but the sight of what she's doing to that thing is making me pine for the same treatment."
        "All of the passion and pleasure that Bree's stirring inside of herself is being expressed by what she's doing with the dildo."
    else:
        show bree mast finger
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        hide bree
        show bree mast mouth small
        "With her free hand, Bree holds a sizable dildo up to her lips, licking and caressing the tip with her tongue."
        "Every twitch and twinge that her playing with herself creates, the further into her mouth she seems compelled to push the toy."
        "I never thought that I'd envy a plastic cock so much, but the sight of what she's doing to that thing is making me pine for the same treatment."
        "All of the passion and pleasure that Bree's stirring inside of herself is being expressed by what she's doing with the dildo."
        "By now she's taking more than half of it into her mouth with each thrust, moaning as she pushes her fingers into herself at the same time."
        "The fact that the sounds she's making are muffled by the dildo in her mouth only seems to make them that much more compelling too."
        "Still rubbing the lips of her pussy, her thumb almost grinding into her clit, Bree almost pushes the dildo so far in that she's deep-throating it."
        "Part of me's worried that she's going to choke, but another is willing her on to see just how much she can swallow."
    hide bree
    show bree mast finger
    "I watch as Bree bites her lip so hard that I expect to see her teeth draw blood."
    "And then she begins to roll her head, the locks of her long, blonde hair already becoming heavy ringlets thanks to the sweat upon her skin."
    "While I know that she's simply reacting to the pleasure overtaking her body, this motion of the head still makes Bree appear to be almost delirious."
    "Once her head has been cast back, she seems to recline yet further, giving me a better view of her below the neck."
    "Now that I have almost the whole length of Bree's form spread out before me, it's hard to stifle the urge begin panting in sympathy."
    "Thinking that she's alone and unseen, she holds nothing back and does whatever it takes to reach her climax."
    "A part of me has to fight the urge to slip a hand into my own pants and copy her example, the sight of her is getting me that hot."
    "But when she finally cums, I can only watch as Bree collapses onto her back."
    "She draws her legs up and curls into a foetal position on the bed, one hand still buried between her thighs."
    "As she falls silent, wrapped in her soaked sheets, I slowly become aware of my own heavy breathing as the only thing that I can still hear around me."
    "Even though she seems to be dead to the world, I'm nevertheless terrified of Bree's hearing me."
    "And so I hurry back to my room, still hunched over from the effects that my peeping on her has had on my body."
    return

label propose_bree_and_sasha:
    "I'm in pretty much uncharted territory here, considering how I've never proposed to one girl before, let alone two at once."
    "But what with the recent changes in the polygamy laws and the fact that I've been happily involved in a serious relationship with both Bree and Sasha, it seems like the way to go."
    "As I don't have any experience of this kind of thing, and there aren't exactly many books or movies in which a guy proposes to two girls at once, I decide to go with the old classic."
    "With just a few minor adjustments, that is..."
    "I pick my moment, and get down on one knee before them both, producing a ring in each hand."
    hero.say "Bree...Sasha...will you marry me?"
    hero.say "And, I guess, each other?"
    if bree.love < 100 and sasha.love < 100:
        "Bree and Sasha look at each other in genuine surprise for a moment."
        "And then Bree bursts into peals of laughter, followed by Sasha a few seconds later."
        bree.say "Oh, [hero.name] - that's so cute!"
        sasha.say "Honestly, is this a joke - did someone put you up to this?"
        hero.say "I...erm...I..."
        bree.say "I mean, this whole polygamy thing's just a fad, right?"
        sasha.say "Sure it is - mark my words, it'll be out of fashion by this time next year!"
        hero.say "Ah...yeah...of course - but I almost had you there for a minute, didn't I?"
        "I manage a nervous life as I die a little on the inside."
        $ bree.love -= 25
        $ sasha.love -= 25
        $ bree.sub -= 25
        $ sasha.sub -= 25
    elif sasha.love < 100:
        show bree happy
        bree.say "Yes, of course!"
        sasha.say "Oh, hell no!"
        "Before I can begin to make sense of their conflicting answers, Bree and Sasha turn to stare at each other."
        "Both their faces are an image of surprise and shock and hearing the other's honest answer."
        bree.say "What the hell, Sasha - are [hero.name] and I not good enough for you all of a sudden?"
        sasha.say "Huh...no, that's not it at all!"
        sasha.say "I just don't want to get tied down..."
        bree.say "Well, she might only be in it for the thrills - but I'm ready to make a commitment, [hero.name]!"
        "Well, I guess two out of three isn't bad."
        $ bree.set_flag("engagedmike")
        $ hero.lose_item("wedding ring")
        $ sasha.sub -= 25
        $ sasha.love -= 25
    elif bree.love < 100:
        show sasha happy
        bree.say "Oh...oh no!"
        sasha.say "Oh, hell yes!"
        "Before I can begin to make sense of their conflicting answers, Bree and Sasha turn to stare at each other."
        "Both their faces are an image of surprise and shock and hearing the other's honest answer."
        sasha.say "What the hell, Bree - are [hero.name] and I not good enough for you all of a sudden?"
        bree.say "No, no...I'm just not ready for that kind of commitment - not yet!"
        sasha.say "Forget her, [hero.name] - we're gonna make quite a pair, you and me!"
        "Well, I guess two out of three isn't bad."
        $ sasha.set_flag("engagedmike")
        $ hero.lose_item("wedding ring")
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        show bree happy
        show sasha happy
        bree.say "Yes!"
        sasha.say "Yes!"
        "Both of the girls stare at the expression of sheer amazement on my face."
        "And then they look at each other, seeing the exact same emotion there as well."
        hero.say "You really mean it - both of you?!?"
        bree.say "Sure - we started out as housemates, then became friends and eventually lovers."
        sasha.say "The only thing that could make what we have any better is it being made official."
        bree.say "We're all of us living proof that this kind of relationship can work, if you love each other enough."
        sasha.say "Yeah - I guess you could say we're kind of like pioneers, or something!"
        "I don't know much about being someone that drives social change."
        "But I do know that these two girls have just made me feel like the luckiest guy in the world."
        $ sasha.set_flag("engagedmike")
        $ hero.lose_item("wedding ring")
        $ bree.set_flag("engagedmike")
        $ hero.lose_item("wedding ring")
    return

label bree_propose:
    call bree_greet
    if game.get_flag_value("homeharem") and sasha.room == game.room and not "bree" in HIDDEN and hero.has_item("wedding ring") >= 2 and not sasha.get_flag_value("engagedmike"):
        call propose_bree_and_sasha
    else:
        show bree
        "When the time finally comes to pop the question to Bree, I find myself pretty conflicted as to how I should go about it."
        "I wanted to avoid all the cliches and yet somehow still manage to include all of the really romantic stuff."
        "But in the end, I was in such a state of indecision, that I just decided today was the day, and stuffed the ring into my pocket."
        "I get Bree's attention, but I can't think of anything clever or original to say."
        "So I simply take her hand and get down on one knee, right then and there."
        hero.say "Bree...will...will you marry me?"
        if bree.love < 100:
            show bree sad
            "Bree's eyes dart this way and that, noting that people are already starting to look in our direction."
            bree.say "What...are you actually serious?"
            hero.say "Erm...well...yeah, pretty much."
            hero.say "I mean...I have a ring and everything!"
            bree.say "Aw, that's so sweet, [hero.name]!"
            bree.say "But I can't marry YOU!"
            bree.say "Now get up - you're embarrassing me!"
            "Well, that could have gone better..."
            $ bree.love -= 25
            $ bree.sub -= 25
        else:
            show bree happy
            "Bree's face looks stunned at first, but soon breaks into a beaming expression of pure happiness."
            bree.say "Yes...yes, of course I will!"
            bree.say "Oh, [hero.name] - I thought you'd never ask!"
            "Well, that was easier than I expected it to be!"
            $ bree.set_flag("engagedmike")
            $ hero.lose_item("wedding ring")
    return

label bree_cheated:
    show bree
    if game.get_flag_value("homeharem") == 1 and game.active_girl.id in ["sasha"]:
        bree.say "Can I get one too?"
        show expression "bree kiss "+bree.get_clothes()
        "And without warning Bree kisses me."
        $ bree.love += 1
        hide expression "bree kiss "+bree.get_clothes()
    else:
        $ bree.set_flag("cheated", game.active_girl.name)
        show bree angry
        bree.say "..."
        $ bree.love -= 20
    hide bree
    return

label smartphone_bree_hint:
    $ story = bree.get_flag_value("story")
    if not bree_love == bree_love_max and not story > 3:
        "I should get to know her better."
    else:
        if not "bree_event_01" in DONE:
            "I think Bree is often in the living room in the morning."
            "I wonder what she is doing."
        elif not "bree_event_02" in DONE:
            "I should see Bree at the arcade, I think she is there mostly on saturdays."
        elif not "zbox 360" in hero.inventory.keys():
            "I need to buy a Z-box to play with Bree."
        elif not "bree_event_03" in DONE:
            "I should see Bree in the living room to play with her."
        elif not "bree_event_04" in DONE:
            "I wonder what Bree is doing, maybe she'll give me a call later on."
        elif not "bree_event_05" in DONE and not "bree_event_05b" in DONE:
            "I should see Bree in her bedroom during the day."
        elif not "bree_event_05b" in DONE:
            "I should see Bree in her bedroom in the evening."
        elif not "bree_event_06b" in DONE:
            "I should see Bree in the kitchen in the evening."
        elif not "bree_event_07b" in DONE:
            "Bree will come to me, eventually."
        else:
            "I reached the end of Bree's story for now."
    return

label bree_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = bree.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = bree.get_activity(bye_hour)
    if not activity == bree.activity:
        if day != game.week_day:
            $ bree.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ bree.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "bree "+bye_outfit
        if activity["activity"] == "sleep":
            bree.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            bree.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            bree.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            bree.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            bree.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            bree.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            bree.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            bree.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            bree.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            bree.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            bree.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            bree.say "I ll go get dressed."

        hide expression "bree "+bye_outfit
    return

label bree_play_pool:
    show bree
    "I recoil as a wave of water makes contact with my unsuspecting face."
    "Bree's laugh leaves no question as to what the cause was, so I return in kind, sending a large splash back to her."
    "The back and forth continues for a short while before we decide on a truce."
    "We spend the rest of our time in the pool peacefully."
    bree.say "Hehe, that was really fun!"
    bree.say "We should do it again sometime!"
    hero.say "Sure, no objections here."
    $ bree.love += 1
    $ bree.set_flag("greeted",True,1)
    return

label bree_tv:
    call bree_greet from _call_bree_greet
    show bree
    if hero.charm >= 40 - bree.love() or bree.get_activity()[1]["activity"] == "tv":
        $ bree.set_flag("daily_interact", 1, 1, "+")
        bree.say "Why not."
        $ choices = ["Action movie","Cartoon","SciFi movie","Fashion show", "Discovery channel", "Romantic comedy", "Porn", "Horror movie", "News", "Reality show", "Music channel"]
        python:
            for i in range(1,4):
                choices.remove(randchoice(choices))
            result = renpy.call_screen("select",choices)
        if game.hour > 20:
            show tv bree
        if result == "Action movie":
            "We watch an action movie."
            "Bree looks a little bored."
        elif result == "Cartoon":
            "We watch a funny cartoon."
            "Bree seems to enjoy herself."
            $ bree.love += 2
        elif result == "SciFi movie":
            "We watch a scifi movie."
            "Bree seems to enjoy herself a lot."
            $ bree.love += 3
        elif result == "Fashion show":
            "We watch a fashion show."
            "Bree looks completly bored."
            $ bree.love -= 1
        elif result == "News":
            "We watch the news."
        elif result == "Reality show":
            $ a = randchoice(["dead", "bimbo", "nazi","smart","real","fake","gay","stupid","angry","cute","white","black","racist","socialist","poor","rich","ugly","sexy","fat","mean","nice","old","young","virgin"])
            $ b = randchoice(["housewives","cops","millionaires","geeks","sluts","nuns","cats","dogs","grannys","middle aged men","asians","government officials","strippers","doctors","truck drivers"])
            $ c = randchoice(["the world","venezuela","paris","mars","the sewers","new-york","france","spain","seattle","los angeles","my basement","texas","mexico","brazil", "space"])
            $ d = randchoice(["of","against","meet","discover","lost in"])
            $ t = (a+" "+b+" "+d+" "+c).title()
            "We watch [t]."
            "Bree looks completly bored."
            $ bree.love -= 1
        elif result == "Music channel":
            "We watch concert."
            "Bree looks bored."
        elif result == "Discovery channel":
            "We watch discovery channel."
            "Bree seems to enjoy herself."
            $ bree.love += 1
        elif result == "Romantic comedy":
            "We watch a romantic comedy."
            "Bree seems to enjoy herself a little."
            $ bree.love += 1
        elif result == "Horror movie":
            "We watch a horror movie."
            "Bree seems to be more scared than enjoyed."
            $ bree.love -= 1
        elif result == "Porn":
            if hero.charm >= 100 - bree.love():
                "We watch some porn together."
                menu:
                    "SM porn":
                        $ bree.sub += 1
                        $ bree.set_flag("porn")
                    "Femdom porn":
                        $ bree.sub -= 1
                        $ bree.set_flag("porn")
                    "Gonzo porn":
                        $ bree.love += 1
                    "Lesbian porn":
                        $ bree.love += 1
                        $ NOTIFICATIONS.append(["Bree {image=ui/icon_les_vsmall.png}+5",2])
                        $ bree.set_flag("lesbian",1,mod="+")
                "Bree seems to be quite excited by the sight."
                if bree.love >150 and bree.get_flag_value("sex"):
                    show couch fun bree
                    "Bree wraps her fingers around my shaft and rolls her tongue out, licking up along my length."
                    hero.say "O... oh wow..."
                    hero.say "It feel so good."
                    bree.say "I kind of knew this would please you."
                    "Again, she licks up my shaft, up over the glans and over the tip."
                    "What did I do to deserve the greatest roomate in the world?"
                    "I wonder this as the excitement of her actions tingles up through my body."
                    show couch fun bree cumshot
                    "I can’t hold back and, with a groan, I release, shooting up onto her."
                    "Cum sprays up onto her face, getting her nice and covered by my jizz."
                    hide couch
                    show couch fun bree facial
                    "Bree smiles up at me, batting her half-lidded eyes up in my direction."
                    bree.say "Enjoy this view, [hero.name],"
                    "Bree takes a finger and slips a drop of my cum off of her face."
                    "She then wraps her lips around my cock, moaning in delight at the taste."
                    hide couch
                $ bree.love += 1
            else:
                bree.say "Sorry, I don't want to watch this sort of things."
                $ bree.love -= 1
                hide bree
                return
        $ hero.fun+= 1.5
        if game.hour > 20:
            hide bree
    else:
        bree.say "Sorry, I don't have time right now."
        $ hero.activity.set_flag("canceled",True)
        hide bree
    hide tv
    return

label bree_meal:
    call bree_greet from _call_bree_greet_1
    if hero.check_skill("cooking"):
        $ bree.love += 1
    if game.hour < 12:
        show bree breakfast
        bree.say "It's nice having breakfast together."
        $ bree.love += 1
    else:
        show bree diner
        call expression bree.get_chat() from _call_expression_23
    hide bree
    return

label bree_greet:
    if not bree.get_flag_value("greeted"):
        show bree
        $ bree.set_flag("greeted",True,1)
        $ result = randint(1,3)
        if result == 1:
            bree.say "Hello, [hero.name]."
        elif result ==2:
            bree.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                bree.say "Good morning [hero.name]."
            elif game.hour < 19:
                bree.say "Good afternoon [hero.name]."
            else:
                bree.say "Good evening [hero.name]."
        $ result = randint(1,3)
        if result == 1:
            hero.say "Hello, Bree."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                bree.say "Hello [hero.name]."
            elif game.hour < 12:
                hero.say "Good morning Bree."
            elif game.hour < 19:
                hero.say "Good afternoon Bree."
            else:
                hero.say "Good evening Bree."
        hide bree
    return

label bree_kiss:
    scene expression "bg "+game.room
    if bree.love() + hero.charm() < 80 and not bree.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show bree
        "Bree quickly takes a step back, and turns away."
        if bree.love < 40:
            bree.say "Sorry but... I don't really feel comfortable with that."
            $ bree.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                bree.say "Sorry, but let's just not."
                $ bree.love -= 1
            else:
                bree.say "I'm sorry, but I have to go..."
            "Before I can react, Bree turns and rushes away."
        hide bree
    elif bree.love() + hero.charm() < 60  or (game.get_flag_value("datescore") >= 75 and not bree.love() + hero.charm() < 60):
        hide bree
        show expression "bree kiss "+bree.get_clothes()
        if not bree.get_flag_value("kiss"):
            "I watch Bree's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "bree kiss "+bree.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != bree and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_46
            elif bree.love >= 60:
                show bree
                bree.say "Um, I think we should talk about this later, alright?"
            else:
                show bree
                bree.say "Oh uh... I've got to go..."
                "Before I can object, Bree begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ bree.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Bree, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "bree kiss "+bree.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != bree and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_47
        $ bree.love += 1
    else:
        hide bree
        show expression "bree kiss "+bree.get_clothes()
        if not bree.get_flag_value("kiss"):
            "I feel my lips passing over Bree's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Bree with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "bree kiss "+bree.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != bree and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_48
            elif bree.love() >= 60:
                show bree blush
                bree.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show bree blush
                bree.say "Um... I should go..."
                "Before I can object, Bree turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Bree's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Bree with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Bree, close enough that our bodies are very nearly touching."
                "I bring one hand to Bree's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Bree's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "bree kiss "+bree.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != bree and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_49
            if hero.charm() >= 160 - bree.love() and bree.love < 50:
                show bree blush
                bree.say "Stop doing that."
        hide bree
        $ bree.love += 2
    return

label bree_gift_signed_fantasy_book:
    call bree_greet from _call_bree_greet_2
    show bree
    bree.say "Is that what I think?"
    show bree happy
    bree.say "Wow, and it's signed!"
    bree.say "That's the best gift ever !!!"
    $ bree.love += 5
    "She jumps in my arms."
    bree.say "Thank you so much [hero.name]!"
    hide bree
    return

label bree_fuck_date:
    $ bree.set_flag("sex",1,"permanent","+")
    if not bree.get_flag_value("sex") > 1:
        scene bg street
        show bree
        "Holding hands for the first time, Bree and I decide to walk home."
        "The chat and laughter from the evening continues on the way back to the house."
        "Bree gets a little loud on occasion, but none of the stares that we get are enough to spoil our mood."
        scene bg livingroom
        show bree
        "Neither of us has a clue if Sasha's even in when we stagger through the front door."
        "But the thought that she might seems to have us both instantly in stitches for some reason."
        "I manage to mess up a knock knock joke as we stand in the hall, and I can't tell if Bree's genuinely amused or just laughing from sympathy."
        scene bg bedroom1
        show bree
        "Either way, it lasts until we're in my bedroom and the door closes behind us."
        "Bree almost collapses onto my bed, and I flop down beside her."
        if not bree.get_flag_value("collared"):
            bree.say "I...I had a really nice time tonight, [hero.name]."
        else:
            bree.say "I...I had a really nice time tonight, Master."
        hero.say "Me too, Bree..."
        bree.say "Why are you always so nice to me?"
        if not bree.get_flag_value("collared"):
            hero.say "Because you're my girlfriend...you are my girlfriend, aren't you?"
        else:
            hero.say "Because you're my slave...you are my slave, aren't you?"
        "Bree giggles, looking away for a moment."
        "I catch the barest hint of red on her cheeks as she takes a deep breath."
        "I sense that she's plucking up the courage for something."
        "Bree takes a deep breath, looking me in the eye as she takes my hand in her own."
        if not bree.get_flag_value("collared"):
            bree.say "Yeah, [hero.name]...I'm your girlfriend."
            bree.say "And I want to do the kind of things that a boyfriend and girlfriend to together..."
        else:
            bree.say "Yeah, Master...I'm your slave."
            bree.say "And I want to use me in everyway a Master can use his prized sex slave..."
        play music "music/Neighborhood_Toys/inside_deep_note.mp3" loop
        "I can feel my heart begin to pound in my chest in anticipation of just what Bree might have in mind."
        "And my body is already reacting without asking permission, as a bulge begins to show in the front of my pants."
        "Bree follows my eyes downward, seeing the same evidence of my arousal."
        "She giggles at the sight of it, her cheeks colouring in a way that somehow makes her look even cuter."
        "Bree slides off of the bed and kneels before me, encouraging me to strip off my shirt."
        "While it's only half over my head, I can already feel her hands unbuttoning my pants and then unzipping my flies."
        "Tossing away my shirt, I'm treated to the sight of Bree enthusiastically pulling down and then off both my pants and my underwear."
        show bree naked
        "I could return the favour and help Bree strip off her own clothes."
        "But I'm just too taken with the sight of her revealing herself a little at a time to be able to do anything but watch in silence."
        "I have no idea of what Bree intends to do next, and once she's totally naked, I can't think of anything else at all."
        "So I simply stare at her, waiting with baited breath to see what happens next."
    else:
        play music "music/Neighborhood_Toys/inside_deep_note.mp3" loop
        scene bg bedroom1
        show bree
        "It's not like this is the first time Bree's ever set foot inside of my bedroom."
        "But there's still an odd feeling in the air, as if neither of us really knows what to do next."
        "We glance at each other and then quickly away again."
        "And then Bree seems to find the courage from somewhere to break the awkward silence between us."
        bree.say "This is so stupid!"
        hero.say "Yeah, I know..."
        bree.say "We're sitting here, acting like a couple of strangers!"
        "I shrug at her comment."
        hero.say "Well, this is kind of a new situation for us to be in together..."
        hero.say "I guess I'm just afraid that I'm going to say something stupid or mess up!"
        "Bree's laughter at this makes me think I've done just that."
        bree.say "I was thinking the exact same thing!"
        bree.say "Is it the thought of us being in your room?"
        bree.say "We can go across the hallway to mine, it you'd like?"
        hero.say "I'm not sure it's the location that's the problem..."
        "It's about this time that both of us seem to stop talking at the exact same moment."
        "Words might have failed us, but I swear I can feel us begin to communicate on another level entirely."
        "Looking each other straight in the eye, I feel Bree's hand reach out for mine."
        "Our fingers twine together, and we finally close the distance between us."
        hide bree
        show expression "bree kiss "+bree.get_clothes()
        "She's as tentative as me when we begin to kiss, and so it's a slow, sensual process of almost feeling each other out."
        "But with each pass we make, I can feel her instinctively pulling closer to me, until we're pressed together, belly-to-belly."
        "Rather than making the whole thing chaste, I find that Bree's need to build her confidence with me means my own passion builds at the same time."
        "This means that by the time we're wrapped up in a close embrace, my anticipation is becoming almost unbearable."
        "I can her Bree making little sighing and almost mewing sounds between kisses, almost like a preamble for what's still to come."
        "Her hand begins to explore my body, travelling over my stomach and down, below my belt."
        "Here, Bree finds the unavoidable proof of just what kind of an effect she's having on me."
        "She breaks the kiss for a moment, stroking my cock through the fabric of my pants."
        "And then she shoulders off her jacket and begins to pull off her top."
        "As if suddenly brought back to life by Bree's example, I start to strip off my own clothes a second later."
        hide expression "bree kiss "+bree.get_clothes()
        show bree naked blush
        "Bree and I have seen each other every day for as long as we've been living under the same roof."
        "But this is the very first time that we've seen each other naked."
        "I couldn't have imagined anything that would come close to doing the sight of her unclothed body justice."
        "She's just perfect - smooth skin, flawless curves, pert breasts and blonde hair tumbling over her shoulders."
        "And then there's the bashful expression on her face and the blush spreading across her cheeks."
        "Is she blushing from embarrassment?"
        "No, I realise in that moment that I'm staring at her like a starving man seeing food."
        "I look away quickly."
        hero.say "I...I didn't think you could look any more beautiful, Bree..."
        hero.say "But I was wrong!"
        "There's a look in her eyes that takes a moment for me to understand."
        "It's like a glistening, almost as though she's going to shed a tear."
        "But then I finally understand that I've managed to say just the right thing at just the right moment."
    if "bree_event_07b" in DONE and bree.get_flag_value("sex") > 1 and not bree.get_flag_value("tittyfuck"):
        $ bree.set_flag("tittyfuck")
        show bree boobjob
        "Bree takes me by surprised when she leans forward and presses my cock between her breasts."
        "I would have been blown away (if you pardon the pun) by either a blow-job or just her hands."
        "They're soft and yet firm at the same time, and so warm I can't help biting my lip at the sensation."
        bree.say "H...How does it feel?"
        "Bree looks up at me as she whispers the question."
        "The faint blush across her cheeks has now become a flush that's turned both her cheeks red."
        hero.say "It feels...amazing!"
        "I try to say something romantic and manly, but the words just blurt out of me all the same."
        "She smiles, and I feel that my own nervousness has somehow helped to stamp down hers too."
        "Bree begins to move her breasts up and down, slowly and steadily."
        "Pinned between them, I feel my cock pulled and pressed in sympathy."
        "I've had this kind of treatment before, but not from a girl that I liked as much as Bree."
        "Which is already making the whole thing feel so much better than the last time I can recall."
        "By now, she's settled into a steady rhythm that it's hard to describe in as anything other than divine."
        "But I can feel her beginning to speed things up a little more as time passes."
        "All the while, she keeps catching my eye, seeking for my approval of what she's doing."
        show bree boobjob wink
        if not bree.get_flag_value("collared"):
            bree.say "Do...do my tits feel good around your c...cock?"
        else:
            bree.say "Do...do my tits feel good around your c...cock, Master?"
        "I've never heard this kind of talk coming from Bree's mouth before this moment."
        "She's trying her best to talk dirty, stumbling over the words in embarrassment."
        bree.say "Uh...oh, it looks so good to me..."
        "Somehow the fact that she's no good at this makes it all the more endearing to hear."
        bree.say "I...I can't wait for it to go pop in my face..."
        "I've started moving my cock up and down in the tight cleft of her breasts now."
        "Sweat from both our bodies making it move that much faster with little effort."
        hero.say "Fuck, Bree - you're so damn hot..."
        "I'm muttering the words, but I guess that she hears them, as I can feel her efforts redouble."
        "Bree's nipples are getting pressed into my stomach with the force that we're rubbing against each other now."
        bree.say "Do...do my tits feel good around your c...cock?"
        if not bree.get_flag_value("collared"):
            bree.say "[hero.name]...will you cum soon?"
        else:
            bree.say "Master...will you cum soon?"
        "Bree's voice is quiet and yet filled with intensity as she asks the question."
        hero.say "Yeah...I think I'm on the brink."
        bree.say "I want to make you...make you cum."
        if not bree.get_flag_value("collared"):
            bree.say "I want you to use me, [hero.name] - use me to get off."
        else:
            bree.say "I want you to use me, Master - use me to get off."
        bree.say "Come on me...cum for me..."
        bree.say "Please?!?"
        "The look on her face as she literally pleads for me to cum over her is all I need to lose it."
        show bree boobjob cumshot
        hero.say "Oh, god - Bree!"
        hide bree
        show bree boobjob facial body
        "Bree makes little strangled cries as she's spattered across the face with my cum."
        "It's hard to tell if they're from surprise, disgust or satisfaction."
        if bree.sub >= 75:
            show bree boobjob facial lick finger
            "Before she finally releases my cock from between her breasts, Bree licks the last droplets of cum from the tip of her fingers."
        "I can't keep from almost grabbing her in a bear-hug the moment that she relaxes."
        "I pull Bree under the covers with me, feeling a second burst of energy run through me."
        hide bree
        call sleep from _call_sleep_9
        return
    if bree.get_flag_value("tittyfuck") and bree.sub >= 50:
        bree.say "Um, well like, do you want me to do it again?."
        bree.say "Show my appreciation..."
        menu:
            "Yes":
                "Bree slides off of the bed and kneels before me."
                "I have no idea of what Bree intends to do next, and once she's totally naked, I can't think of anything else at all."
                "So I simply stare at her, waiting with baited breath to see what happens next."
                show bree boobjob
                "Bree takes me by surprised when she leans forward and presses my cock between her breasts."
                "I would have been blown away (if you pardon the pun) by either a blow-job or just her hands."
                "They're soft and yet firm at the same time, and so warm I can't help biting my lip at the sensation."
                bree.say "H...How does it feel?"
                "Bree looks up at me as she whispers the question."
                "The faint blush across her cheeks has now become a flush that's turned both her cheeks red."
                hero.say "It feels...amazing!"
                "I try to say something romantic and manly, but the words just blurt out of me all the same."
                "She smiles, and I feel that my own nervousness has somehow helped to stamp down her's too."
                "Bree begins to move her breasts up and down, slowly and steadily."
                "Pinned between them, I feel my cock pulled and pressed in sympathy."
                "I've had this kind of treatment before, but not from a girl that I liked as much as Bree."
                "Which is already making the whole thing feel so much better than the last time I can recall."
                "By now, she's settled into a steady rhythm that it's hard to describe in as anything other than divine."
                "But I can feel her beginning to speed things up a little more as time passes."
                "All the while, she keeps catching my eye, seeking for my approval of what she's doing."
                show bree boobjob wink
                bree.say "Do...do my tits feel good around your c...cock?"
                "I've never heard this kind of talk coming from Bree's mouth before this moment."
                "She's trying her best to talk dirty, stumbling over the words in embarrassment."
                bree.say "Uh...oh, it looks so good to me..."
                "Somehow the fact that she's no good at this makes it all the more endearing to hear."
                bree.say "I...I can't wait for it to go pop in my face..."
                "I've started moving my cock up and down in the tight cleft of her breasts now."
                "Sweat from both our bodies making it move that much faster with little effort."
                hero.say "Fuck, Bree - you're so damn hot..."
                "I'm muttering the words, but I guess that she hears them, as I can feel her efforts redouble."
                "Bree's nipples are getting pressed into my stomach with the force that we're rubbing against each other now."
                bree.say "[hero.name]...will you cum soon?"
                "Bree's voice is quiet and yet filled with intensity as she asks the question."
                menu:
                    "Keep going":
                        $ bree.sub += 1
                        hero.say "Yeah...I think I'm on the brink."
                        bree.say "I want to make you...make you cum."
                        if not bree.get_flag_value("collared"):
                            bree.say "I want you to use me, Master - use me to get off."
                        bree.say "Come on me...cum for me..."
                        bree.say "Please?!?"
                        "The look on her face as she literally pleads for me to cum over her is all I need to lose it."
                        show bree boobjob cumshot
                        hero.say "Oh, god - Bree!"
                        hide bree
                        show bree boobjob facial body
                        "Bree makes little strangled cries as she's spattered across the face with my cum."
                        "It's hard to tell if they're from surprise, disgust or satisfaction."
                        if not hero.energy >= 8 and hero.fitness >= 75:
                            if bree.sub >= 75:
                                show bree boobjob facial lick finger
                                "Before she finally releases my cock from between her breasts, Bree licks the last droplets of cum from the tip of her fingers."
                            "I can't keep from almost grabbing her in a bear-hug the moment that she relaxes."
                            "I pull Bree under the covers with me, feeling a second burst of energy run through me."
                            hide bree
                            call sleep from _call_sleep_3
                            return
                    "Stop her":
                        hero.say "No, Bree - I really want to fuck you right now..."
                        $ bree.love += 1
            "No":
                $ bree.love -= 1
    menu:
        "Anal" if bree.get_flag_value("anal") >= 2:
            "I can hear panting in my ears right now, but I can't be sure if it's coming from Bree, myself or the both of us."
            "Not that it matters, as I turn Bree around to face away from me and guide her down onto the bed, not giving her time to question or object."
            "As she clambers onto the mattress, she's forced to go down on all fours to avoid falling onto her face."
            show bree doggy anal
            "And before she can either sit back up or try to lie down on her belly, I take a firm hold of her around the waist."
            "Bree seems to understand the gesture, and remains obligingly down on all fours as I climb up behind her."
            "She can't know what I'm intending to do to her, and the fleeting glances that she gives me over her shoulder are testament to this."
            "But I'm enjoying her being in the dark, and so am in no mood to offer her any solid clues as to my intentions just yet."
            "Instead I make a point of seizing her buttocks, one in the palm of each hand, and massaging them as though I was kneading dough."
            "Bree moans at the sensation, the movement creating sympathetic twinges from between her thighs."
            "Slowly, I part her buttocks to reveal the crease that they serve to hide from me."
            "And there, glistening like a wondrous prize, is the sight of Bree's tight little pussy."
            "It's already so wet that I can smell it's scent, almost quivering with anticipation enough for the eye to perceive it."
            "But my goal is just a little way above it, a much more challenging and rare objective."
            "It'd be so easy to just slip inside of Bree's pussy right now..."
            "And so maybe that's why I choose the more demanding option."
            "And maybe that's why she's so surprised when I do so."
            "I rub my fingers along the sides of Bree's pussy, collecting a little of the juices flowing so freely there."
            "As she squeals in genuine surprise, I use this to lube up the head of my cock."
            show bree doggy anal speed
            "A moment later, I spread her buttocks wider still, and then begin to push my way into her ass."
            "Where she squealed before, Bree now lets out a long, low moan as she feels my cock forcing its way inside of her."
            "In contrast to the welcome that her pussy had laid out for me, her ass is as tight as can be."
            "It feels incredible as the muscles squeeze against me, trying in vain to keep my cock from penetrating further."
            "There's nothing but forward motion of short pauses to begin with, as I battle against Bree's body."
            "She's doing nothing to stop me on a conscious level, but the need to fight for every inch is making me all the more determined."
            show bree doggy anal speed ahegao
            "By the time I'm almost balls deep into her, Bree's clawing at the sheets and tossing her head around like an animal on heat."
            "And then, it's as if her body finally surrenders to the inevitable, and the walls come down all at once."
            "I feel the last shred of resistance drain away, and her muscles accept the inevitable."
            "Like a doe that needed to be conquered by a rutting stag, Bree's body melts beneath me."
            "And only then do I really start to fuck her ass."
            "Now the thrusts that I begin to push into her with are hitting on already spent, exhausted muscles."
            "This means that Bree feels the full force of my every movement with nothing at all held back."
            "Every second that I'm inside of her makes her legs, stomach and arms shudder with sensation."
            "I can see her breasts shaking in sympathy, her head hanging down in sheer submission."
            "It's as though, by bending her ass to my will, I've unlocked the key to conquering every part of her body afterwards."
            "Right now I can't imagine this hole being meant for anything but taking my cock."
            "And the resigned nodding that Bree's head has settled into seems to confirm me as being the one in charge."
            show bree doggy -noone anal cuminass
            "By the time that I make one final push into her, spending myself in the effort, I doubt Bree could have objected if she'd tried."
            $ bree.sub += 1
        "Doggy" if bree.sub >= 25:
            if hero.has_condom():
                menu:
                    "Use a condom":
                        $ CONDOM = True
                        $ hero.use_condom()
                    "Do it raw":
                        $ CONDOM = False
            else:
                $ CONDOM = False
            "Bree offers no resistance whatsoever as I turn her around and push her gently onto the bed before me."
            "For a moment she goes to lay flat upon her stomach, but I put a hand at the top of each of her thighs and pull her upright once more."
            "She seems to get the message, and raises herself up on her elbows and knees, shuffling the last bit of the way onto the bed."
            "I climb up behind her, noting the look of anticipation on her face as she glances back, over her shoulder."
            "I can see Bree's breasts, still swaying slightly from the momentum of her movements."
            "I can see her buttocks, standing still and unprotected before me."
            "As I part them to reveal her already glistening pussy, I hear a faint moan of anticipation from her other lips."
            "And that makes me want her all the more."
            if not bree.get_flag_value("anal") and randint(1,4) ==1:
                show bree doggy anal
                "Bree moans more audibly as she feels my cock begin to push its way into her."
                "It's a sensation that I can certainly appreciate, as she's much tighter than I'd anticipated."
                "I try not to be dissuaded by this unexpected discovery, instead redoubling my efforts."
                "Bree actually cries out in response to this, yelping and sighing more with every inch that I make it into her."
                "It's baffling me how I could have just seen her so wet and ready for this, yet find so much resistance."
                "Glancing down to see if I was mistaken, I soon discover the actual source of the problem."
                "I'm not in Bree's pussy after all, but by now, balls deep in her ass!"
                hero.say "Whoops!"
                "Bree looks back at me over her shoulder, her expression not outraged or angry in any way."
                "In fact, she looks pretty accepting of what I've been doing to her..."
                menu:
                    "Pull out, Pull out!":
                        show bree doggy fuck dickout
                        "I pull out of Bree's ass as quickly as I can manage, still trying to be as gentle as I can with her."
                        "But the sigh of (what I assume is) relief that she lets out while I withdraw makes me wonder if I've misjudged the situation entirely."
                        hero.say "Erm...Bree...I'm sorry."
                        hero.say "That was kind of an accident..."
                        if not bree.get_flag_value("collared"):
                            bree.say "Ah...It's okay, [hero.name]...really it is."
                            bree.say "Just warn me the next time you want to go there, okay?"
                        else:
                            bree.say "Ah...It's okay, Master...really it is."
                        "I nod quickly."
                        hero.say "Do you still want to..."
                        bree.say "If you do too..."
                        "With that, she looks away a little, as if inviting me to try again."
                    "Keep going":
                        show bree doggy anal speed
                        "I choose to take the fact that Bree's not telling me to stop as tacit approval for what I'm doing."
                        "Rather than stopping, I begin to thrust into her that much harder and with more force than before."
                        "As she's still looking back at me over her shoulder, I can see the instant effect this has upon Bree's expression."
                        "Her eyes seem to lose their focus and her features almost slacken a little in response to the way she's being used."
                        "A part of me feels as though, in her acceptance, she's become almost like a passive receptacle for my desires."
                        "This impression is only helped by the fact that she makes no sounds that could be taken as words from this point on."
                        "Instead, Bree begining to gasp and almost yelp like a dog."
                        "I feel as though with every push into her from my cock, she becomes ever more like a beast that's being mounted."
                        show bree doggy anal speed ahegao
                        "Any issues that I might have had from there being no natural lubrication from Bree's ass is no longer a problem."
                        "Thanks to the sheer amount that we're sweating, she's as wet and slippery down there as her pussy could ever be."
                        "I can see her hands grabbing at the bedclothes, gripping onto them as if for dear life."
                        "The only sounds that she's making now are coming in the form of low groans, almost turning into growls."
                        "I've never seen Bree like this before, as though being fucked up the ass is turning her into a primitive, yowling animal."
                        "Part of me is worried that I've gone too far, but the larger part of me is simply too aroused to even think of stopping."
                        "And now it's my turn to let out an animalistic cry, as I feel myself cuming."
                        if not CONDOM:
                            menu:
                                "Pull out":
                                    "I managed to pull my cock out of Bree's ass the second before I cum."
                                    "Suddenly left a gaping void, I see her shudder as her backside finally relaxes."
                                    show bree doggy fuck dickout cumshot
                                    "Her buttocks quiver as I splatter them with a shower of white."
                                    hide bree
                                    show bree doggy fuck dickout cumonass
                                    "Bree seems to shiver bodily more with each drop that lands upon her naked, exposed skin."
                                "Cum inside":
                                    "I didn't think that I could possibly push any further inside of Bree than I already had."
                                    "But as I cum, I thrust with such determination that she almost screams from the sensation."
                                    "A moment later, her arms and legs collapse beneath her, and Bree's head slumps onto the pillows."
                                    show bree doggy anal cuminass
                                    "Even once it's over, Bree doesn't snap out of her stupor."
                                    "Instead, she only manages to turn her head a little, so that she can stare at me out of the corner of her eye."
                                    "Her expression is still that of a stunned animal, not fully conscious of what just happened or why."
                        else:
                            "I can't stop now, and I'm pretty sure that Bree wouldn't want me to either."
                            "I push further into her than I ever thought possible, making her squeal like an animal caught in a trap."
                            "Bree's limbs begin to shake, and then they go limp as she collapses onto the bed."
                            show bree doggy -noone anal cuminass
                            "Even after I've climaxed whilst do deep inside of her ass, Bree doesn't stir from where she fell."
                            "All I can do is pull myself gingerly out of her and take care of the condom still clinging to my cock."
                        hide bree
                        "To me, it feels like what we just did was amazing, and I fall back onto the bed in a state of satisfied triumph."
                        show bree naked blush
                        "But the moment that Bree regains her senses, she darts off of the bed."
                        "She hurriedly gathers up her clothes, not even bothering to dress, her face bright red as she does so."
                        "Then she almost runs out of the room, and I hear her cross the hallway, slamming her own bedroom door behind her."
                        "I begin to wonder if I really messed up back there."
                        "Or maybe Bree's just embarrassed at being taken up the ass without warning?"
                        "Either way, it's not how I'd have wanted things to work out."
                        $ bree.set_flag("anal",1)
                        return
            show bree doggy fuck pussy
            "I don't make straight for Bree's pussy with my cock, instead allowing it to rub against the folds and lips for a little while."
            "My reward is to feel her shudder in anticipation and let out a series of little moans as she's teased with the promise of what's still to come."
            "By this time, Bree is literally wet and almost leaking onto me."
            "And so when I finally adjust my hips just so, I slide into her as smoothly as if she was greased slick."
            "I go slowly, knowing just how much she's wanting this, and hoping to make her savour the feeling as much as possible."
            "Bree tosses her head more with every inch that I push into her, almost reacting to my movements before I can make them."
            "Indeed, she begins to try to push herself backwards, wanting to have more than I'll allow her."
            "But I take a firm hold of her buttocks, using my arms to arrest her progress."
            "Bree struggles and whines at this, like a dog denied a treat by its master."
            "And so I'm forced to reward her by pushing the last few inches into her, until I can go no deeper."
            "She writhes as I do this, lowering herself to the mattress so that my angle of entry is as acute as possible."
            "At the same time, Bree grabs handfuls of the bedclothes, almost tearing at them in her passion."
            "I'm going as fast as I can by this point, the sound of my thighs slapping against her buttocks a sharp crack."
            "Bree buries her face in the pillows, but I can still hear her moans and cries, muffled as they are."
            "I can't keep this up much longer - something's got to give!"
            if not CONDOM:
                menu:
                    "It's not worth the risk" if hero.fitness >= 25:
                        show bree doggy fuck dickout
                        "I manage to keep my head and pull out just before it's too late."
                        "I hear Bree sigh in unconscious disappointment, but I know she'd have been rather more irate to feel me cuming inside of her."
                        "The consequence of my conscientiousness is that she almost instantly gets showered with all that I have to give."
                        "It spatters down on the small of her back, running down her spine and between her buttocks."
                        "She looks at me with an embarassed expression on her face."
                        show bree naked blush
                        bree.say "Wow...that was crazy!"
                        bree.say "I honestly thought you were going to cum in me for a moment back there!"
                        "I shake my head, still breathing a little heavily from my exertions."
                        hero.say "I know...it was touch and go for a while!"
                        hero.say "You get me so worked up with passion, Bree - I think we need to use a condom in future!"
                        "My compliment does nothing to keep her from blushing all the more."
                        "Bree doesn't say anything more, but she wraps her arms around me in an embrace that's worth a thousand words."
                    "Cum inside" if bree.get_flag_value("cum-in"):
                        if (randint(1,3) == 1 or "hung" in hero.skills) and not bree.get_flag_value("pregnant") and not bree.get_flag_value("pill"):
                            $ bree.set_flag("pregnant",1)
                        $ bree.sub += 1
                        "I'm too far gone to even think about pulling out of Bree by now, and so I press on regardless."
                        "She must realise what's going on, as I feel her begin to wriggle almost desperately."
                        "But she's given up too much of her leverage in lowering herself down to allow me further in, and she can't hope to free herself in time."
                        "As I cum into her, I press down with all of my weight, making sure that she stays put until I'm utterly spent."
                        show bree doggy fuck pussy cuminpussy
                        "I can hear Bree whimpering and moaning at the feelings of ecstasy she's experiencing and the knowledge of what I've done to her."
                        "But I'm too exhausted to either feel triumphant or else let the implications of it all sink in."
                        "So I lie down on the bed and leave Bree to deal with it on her own for a while."
                        show bree naked blush
                        if bree.love >= 150 or bree.get_flag_value("pill"):
                            $ bree.love += 1
                            "Bree looks around at me eagerly, even as my cum is starting to drip out and run down the inside of her thighs."
                            if not bree.get_flag_value("collared"):
                                bree.say "Mmm...I feel so good when you fill me up to the brim Master!"
                            else:
                                bree.say "Mmm...I feel so good when you fill me up to the brim!"
                            bree.say "All warm and melty inside, like you've turned my pussy into a jar of warm honey..."
                            "I can't help laying myself atop her as she says this, covering her body with mine."
                            hero.say "I promise that next time, I'll lick that pot clean!"
                            "Bree laughs as we collapse onto the bed together in a tangle of sweaty limbs."
                        else:
                            bree.say "[hero.name]...you're gonna..."
                            "But it's way too late for that now, and I feel myself letting go inside of her."
                            "I expected Bree to freak out and instantly try to clamber out from under me, at least chew me out verbally."
                            "So when she stays perfectly still and allows me to thrust my last into her, I'm more than a little puzzled."
                            "Afterwards, she gasps as I pull out, a strange look of fear and...what looks like excitement, in her eyes."
                            hero.say "Bree, I'm sorry - I..."
                            "She holds a hand up and shakes her head, silencing me."
                            bree.say "Don't say it..."
                            bree.say "Just please, use a condom next time...okay?"
                            "I nod hastily, already seizing upon the mention of the next time as a possible sign."
                            "Hopefully I've not marked my card with her permanently here."
                            $ bree.love -= 20
            else:
                "This is it, I let go of myself and cum without restraint."
                show bree doggy -noone fuck pussy condom
                "Bree bucks beneath me, my own orgasm seeming to push her over the brink herself."
                "Even though I'm absolutely spent, I use the last of my energy to make sure she feels all of it that I can manage."
                "In the end, I don't so much pull out of Bree as slide out as I collapse onto the bed."
                show bree naked blush
                "A moment later, I feel her snuggling against me, pushing her way into my arms."
                if not bree.get_flag_value("collared"):
                    bree.say "Oh, thank you, [hero.name] - that was perfect!"
                else:
                    bree.say "Oh, thank you, Master - that was perfect!"
                "I don't think she's ever looked as beautiful to me as she does right now."
                "She fits into the crook of my body so well that I don't even need to move an inch."
        "Missionary":
            if hero.has_condom():
                menu:
                    "Use a condom":
                        $ CONDOM = True
                        $ hero.use_condom()
                    "Do it raw":
                        $ CONDOM = False
            else:
                $ CONDOM = False
            "I take Bree firmly by the hand and lead her over to the side of the bed."
            "She still seems nervous, stealing glances at me as we go and smiling weakly."
            hero.say "You don't have to be afraid, Bree."
            if not bree.get_flag_value("collared"):
                hero.say "I want you so badly right now - but whatever happens, you can always say no."
                "Bree gulps audibly, but nods all the same."
                bree.say "O...okay, [hero.name]...I trust you."
                "I can see that she's aware of just how hungrily I'm looking at her right now."
                bree.say "You can...you can do whatever...whatever you want to do to me..."
            else:
                "Bree gulps audibly, but nods all the same."
                bree.say "O...okay, Master...I trust you."
                "I can see that she's aware of just how hungrily I'm looking at her right now."
                bree.say "You can...you can do whatever...whatever you want to do to me Master..."
            "I can see that she's aware of just how hungrily I'm looking at her right now."
            bree.say "You can...you can do whatever...whatever you want to do to me..."
            "I don't offer an answer to this, and simply begin to strip off her clothes."
            "Bree shudders a little, but makes no objection as I remove one item at a time."
            "Soon she's standing before me, totally naked."
            "I take far less time to strip off my own clothes, and then guide her down onto the bed."
            "Slowly, I climb atop her, making sure that my weight is lowered onto her gently and a little at a time."
            "Bree remains still and compliant, the only sound she makes being the sound of her quickening breath."
            "I part her thighs and begin to rub my now stiff cock against the folds of her perfect pink pussy."
            if bree.get_flag_value("collared"):
                bree.say "Master..."
            "She's already slick and warm, so soft and inviting that I have to struggle to keep from taking her right there and then."
            "But instead, I continue to tease her with the promise of my cock."
            show bree miss dickout arm
            "All the while that I'm tormenting Bree's pussy, I make sure to rub my chest against her stiffening nipples."
            "At the same time, I keep on nuzzling and nipping at her neck, my hands entwined in her hair."
            "She tries to writhe and move beneath me, lowering herself in the hope of capturing my cock."
            "But I can feel her every effort coming and move just enough to keep her constantly frustrated."
            if not bree.get_flag_value("collared"):
                bree.say "Please...[hero.name]...I want..."
            else:
                bree.say "Please...Master...I want..."
            "I lean in close, my lips next to her ear as she pushes her head back into the pillows, looking for release."
            hero.say "What do you want, Bree?"
            hero.say "Tell me, and you can have it...right now."
            "Bree let's out a strangled cry of frustration before she's able to reply."
            bree.say "Uhhh...your cock..."
            bree.say "I want your cock inside of me..."
            if not bree.get_flag_value("collared"):
                bree.say "[hero.name], please...let me have your cock!"
            else:
                bree.say "Master, please...let me have your cock!"
            hide bree
            show bree miss fuck arm orgasm
            "Not wanting to disappoint her, I instantly oblige."
            "By now, I'm laid completely atop Bree, my arms pinning her shoulders and legs upon her thighs."
            "All it takes is a subtle movement and I'm inside of her in less than a second."
            "I don't go slowly, either - using my superior weight and angle to push as far into Bree as I can physically manage."
            "Not stopping until I feel my balls against her ass, I use my entire body to push her further downwards."
            "If she was struggling to get her words out before now, Bree loses the power of speech entirely at this point."
            "As I begin to thrust up and down, always careful never to fully pull out of her, she's reduced to mere cries and moans."
            "I'm being as relentless as I can be on Bree's pussy, actively trying to push her as far as I can."
            "She must be getting sore from the friction, as wet as she was when I began."
            "But still she shows no signs of begging me to stop, and so I press on with yet more gusto."
            "In the end, Bree's clinging to me, almost as though the only torture worse than going on would be to suddenly stop dead."
            "The latter of which might soon be the only option though, as I can already feel myself cumming."
            if not CONDOM:
                menu:
                    "cum inside":
                        if (randint(1,3) == 1 or "hung" in hero.skills) and not bree.get_flag_value("pregnant") and not bree.get_flag_value("pill"):
                            $ bree.set_flag("pregnant",1)
                        $ bree.sub += 1
                        show bree miss fuck arm orgasm
                        "There's nothing I can do to stop myself from cuming, long and hard."
                        show bree miss fuck arm ahegao cuminside
                        bree.say "Ah...ah...[hero.name]!"
                        "Bree begins to quiver and shake, her own orgasm taking hold of her."
                        "I feel the muscles inside of her pussy clamp down on me, holding me inside of her."
                        "It's hard to reconcile what she's doing with the look on her face right now."
                        "Which is showing the strangest combination of ecstasy and concern."
                        hide bree
                        show bree miss
                        "Once she finally releases me, Bree pulls herself up on her elbows and a little away from where I'm lying."
                        "The look on her face reminds me of one of those classical oil paintings, in which someone's been mortally wounded and lies dying."
                        "It's only when I follow her gaze down and see the sheer amount of glistening cum that's oozing out of her that I finally understand."
                        bree.say "That quite something..."
                        if not bree.get_flag_value("pill"):
                            bree.say "But did you have to...cum inside?"
                            menu:
                                "Not sorry!":
                                    hero.say "The way I felt, I was never going to pull out of you!"
                                    "I shake my head at her."
                                    hero.say "Do you have a problem with that?"
                                    "I know I sound like an asshole here - but she did tell me that she'd do whatever I wanted."
                                    if bree.love >= 75:
                                        if not bree.get_flag_value("collared"):
                                            bree.say "Oh...okay, [hero.name]...so long as you're happy, so am I..."
                                        else:
                                            bree.say "Oh...okay, Master...so long as you're happy, so am I..."
                                        "I can tell that she's not, but as long as she's trying to hide it, I win."
                                        $ bree.set_flag("cum-in", 1)
                                        $ bree.love += 1
                                    else:
                                        show bree naked angry
                                        bree.say "I...I have to...I have to go - now!"
                                        $ bree.love -= 25
                                        "Bree's on her feet and out of the room before I can say a word."
                                        "Was it something I said?"
                                "Sorry...":
                                    hero.say "God, I'm so sorry, Bree."
                                    hero.say "I guess I just got so caught up in the moment I was swept away..."
                                    "Bree's clearly unhappy with the way things turned out here."
                                    "But there's something else on her mind, something I can't quite put my finger on."
                                    bree.say "Ah, I suppose it can't be helped now."
                                    bree.say "But you have to promise me that you'll use a condom next time, okay?"
                                    bree.say "We can't take that risk every time."
                                    "I'm a little hesitant to snuggle closer to her after that, for fear of her still being mad."
                                    "But Bree soon puts my fears to rest by pulling my arm around her and placing herself firmly in my embrace."
                    "Cum outside":
                        hide bree
                        show bree miss dickout arm
                        "I pull out just the moment before I cum."
                        "Beneath me, Bree moans in unconscious disappointment at her now empty pussy."
                        show bree miss dickout arm cumshot
                        "I hardly notice her reaction, as I release a stream of warm cum onto her slick breasts, which runs around her nipples and onto her sweat-covered belly below."
                        hide bree
                        show bree miss dickout arm bellycum
                        "Bree looks seriously fucked, in every sense of the word."
                        "But I'm guessing a degree of the delight that I can see in her eyes is on account of me not cuming inside her unprotected."
                        "Still slippery and wet from everything that's been showered over her, she snakes into my arms and nestles there happily."
            else:
                show bree miss fuck arm orgasm
                "I keep myself firmly inside of Bree as I cum, feeling oddly thankful for the condom that lets me do so without fear of the consequences."
                if not bree.get_flag_value("collared"):
                    bree.say "Oh god...[hero.name]...I'm going to cum!"
                else:
                    bree.say "Oh god...Master...I'm going to cum!"
                "And then she does, her pussy clamping down on me like a man-trap as she shakes and quivers helplessly."
                "I push into her as best I can, even with my cock already losing its stiffness, trying to give her all that I can."
                if bree.sub >= 75:
                    "I carefully strip the condom off of my dick, taking care to catch as much of the cum as I can in the top as I do so."
                    "Holding it in one hand, I beckon Bree to come closer from where she's lying in a sweaty mess upon the bed."

                    "I gently open her mouth, and then tip up the condom so that the contents drizzle onto her tongue."
                    "Bree swallows the dregs of my cum without complaint, even taking the time to lick her lips to ensure she's captured every last drop."
                "And in so short of a time after that crazy exertion and tumult, Bree's wrapped in my arms as still as if she were sleeping."
    hide bree
    call bree_sleep_date_fuck from _call_bree_sleep_date_fuck
    return

label bree_sleep_date_fuck:
    scene bg bedroom1
    show bree naked
    if not bree.get_flag_value("collared"):
        bree.say "[hero.name], can I... Can I please spend the night?"
    else:
        bree.say "Master, can I... Can I please spend the night?"
    menu:
        "No":
            hero.say "No, you shouldn't; I have to get up early tomorrow,"
            "The sex was beyond incredible."
            "Frowning a little, Bree straightens and collects her clothes in silence."
            bree.say "That's OK, sleep well!"
            "She then grins at me, before leaving."
            $ bree.love -= 3
        "Yes":
            hero.say "Of course you can."
            "I catch a brief moment of joy flash across her face, before she pulls me into a hug, nuzzling into me once again."
            bree.say "Thank you..."
            "I'm not sure why she seems so happy about this, but it looks like I picked the right answer."
            if not bree.get_flag_value("collared"):
                bree.say "Sleep well, [hero.name]."
                hero.say "You too."
            else:
                bree.say "Sleep well, Master."
                hero.say "You too my cute little slave."
            "We both cuddle in silence, drifting off to sleep in each others arms."
            $ bree.love += 3
    $ renpy.call_in_new_context("sleep")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
