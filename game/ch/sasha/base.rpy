init -1 python:
    Activity(**{
        "name": "have_a_meal_with_sasha",
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
        "max_girls": 1,
        "icon":"eat",
        "girls_conditions": {
            "sasha":{
                "present":True,
                "activity":"meal",
                "valid":True,
                "flag_cheated":False
                }
            },
        "display_name": "Eat with Sasha",
        "label": ["sasha_meal"]
        })

    Activity(**{
        "name": "watch_tv_with_sasha",
        "duration": 2,
        "fun": 3,
        "icon":"tv",
        "display_name": "Watch TV with Sasha",
        "girls_conditions": {
            "sasha":{
                "present":True,
                "activity":["tv"],
                "valid":True,
                "flag_cheated":False
                },
            "bree":{
                "not_activity":["tv"],
                "valid":True
                }
            },
        "game_conditions": {
            "room":["livingroom"],
            "min_fun":0, 
            },
        "label": ["sasha_tv"]
        })

    Activity(**{
        "name": "watch_tv_with_sasha_b",
        "duration": 2,
        "fun": 3,
        "icon":"tv",
        "display_name": "Watch TV with Sasha",
        "girls_conditions": {
            "sasha":{
                "present":True,
                "activity":["tv"],
                "valid":True,
                "flag_cheated":False
                },
            "bree":{
                "valid":False
                }
            },
        "game_conditions": {
            "room":["livingroom"],
            "min_fun":0, 
            },
        "label": ["sasha_tv"]
        })

    Activity(**{
        "name": "play_in_the_pool_with_sasha",
        "duration": 1,
        "fun": 3,
        "icon":"playpool",
        "display_name": "Play with Sasha",
        "girls_conditions": {
            "sasha":{
                "present":True,
                "min_love": 10,
                "valid":True,
                "flag_cheated":False
                },
            "bree":{
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
        "label": ["sasha_play_pool"]
        })

    Event(**{
        "name":"sasha_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "sasha",
        "girls_conditions": {"sasha":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True,"flag_cheated":False}},
        "game_conditions":{"chances":5},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"sasha_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "sasha",
        "girls_conditions": {"sasha":{"contact":"sasha","valid":True,"present":False,"not_activity":"sleep","min_love":50,"flag_cheated":False}},
        "game_conditions": {"hours":(18,19),"flag_dateinprogress":0,"chances":10},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"sasha_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "priority":100,
        "girl": "sasha",
        "girls_conditions": {"sasha":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50,"flag_cheated":False}},
        "game_conditions": {"chances":50},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"sasha_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "priority":100,
        "girl": "sasha",
        "girls_conditions": {"sasha":{"valid":True,"present":True,"not_activity":"sleep","min_love":50,"flag_cheated":False}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"sasha_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "priority":100,
        "girl": "sasha",
        "girls_conditions": {"sasha":{"valid":True,"present":True,"flag_cheated":False}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_sasha_2"},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"sasha_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "priority":100,
        "girl": "sasha",
        "girls_conditions": {"sasha":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False,"flag_cheated":False}},
        "game_conditions": {"chances":5},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"sasha_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "sasha",
        "girls_conditions": {"sasha":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50,"flag_cheated":False},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name": "sasha_masturbation",
        "priority": 500,
        "label": ["sasha_masturbation"],
        "duration": 1,
        "game_conditions":{"hours":(20,3),"chances":25, "activity":"knock_bedroom3", "flag_female":0},
        "girls_conditions": {"sasha":{"room": ["bedroom3"],'valid':True}},
        "do_once":False,
        "once_day":True,
        "quit": True
        })


    Event(**{
        "name": "sasha_masturbation_bree",
        "priority": 500,
        "label": ["sasha_masturbation_bree"],
        "duration": 1,
        "game_conditions":{"hours":(20,3),"chances":25, "activity":"knock_bedroom3", "flag_female":1},
        "girls_conditions": {"sasha":{"room": ["bedroom3"],'valid':True}},
        "do_once":False,
        "once_day":True,
        "quit": True
        })

label sasha_masturbation_bree:
    $ hero.activity.set_flag("canceled",True)
    "Everyone walks around with their unconscious ear for interesting sounds turned on, don't they?"
    "I mean, I'm no different from the next girl when it comes to that kind of thing, not at all."
    "It's not like I snoop around the house the whole time, trying to find stuff to eavesdrop on - honestly, it's not!"
    "But I'm only human, and so when I hear something that intrigues me, how can I help turning an ear towards?"
    "That's natural curiosity, not any kind of perviness on my part...right?"
    "Anyway, that's how I end up looking in through the keyhole of Sasha's bedroom door."
    "I just happen to be wandering past, and I hear the most worrying sounds coming from inside of there."
    "Unable to guess just what's going on, and worried that poor Sasha might be in some kind of terrible pain, I rush over and put my eye to the keyhole."
    "Obviously I can't just knock on the door, as she might be perfectly fine in there, which would be embarrassing for the both of us."
    "No - much better to take a quick peak through the keyhole and make sure that she's actually in need of my help first."
    show sasha mast
    "At first, all I can see is Sasha herself, spread out on the bed, naked as the day she was born."
    "And bless her, the poor thing does seem to be in the throes of agony, casting her head about and moaning terribly."
    "But then I see the various phallic-shaped objects that are scattered on the bed around her."
    "And I begin to think that I might have made slight error in my guess at just what Sasha's been up to!"
    menu:
        "Stop watching":
            "Oh...my...god!"
            "She's masturbating, right there in front of me!"
            "Well...I suppose she's actually doing it in the privacy of her own room and behind a closed door..."
            "But still - she's masturbating!"
            "I feel instantly dirty and wretched as I tear my eye away from the keyhole, wishing that I'd never taken a peak to begin with."
            "Urgh...that image is going to be seared into my memory forever!"
            "I retreat to the safety and sanctuary of my own room, terrified that I might get the urge to copy what I've seen."
            "Or worse - that I might do it while still thinking about Sasha!"
            "Eww...why do I have to have such a dirty little bitch for a housemate?"
            hide sasha
            return
        "Keep watching" if game.get_flag_value("morality") >= 0:
            "Oh...I see - she's not in THAT kind of pain!"
            "I guess that I should have noticed sooner just where Sasha's hands were."
            "And the fact that the toys on the bed are all visibly slick with a fresh application of lube."
            "Look, I know that this is the point where I should get all embarrassed and maybe even puritanically squeamish."
            "But there's always been that little bit of curiosity in the back of my mind when it comes to this kind of thing."
            "I might not be ready to give up on guys altogether, but the thought of watching another girl is kind of intriguing."
            "And it's not like I'm sneaking into some stranger's home to do it, right?"
            "Sasha and I have been living under the same roof for long enough by now."
            "Both of us have seen the other in our bikinis and running here and there in nothing but underwear."
            "So that unspoken barrier has already been broken..."
            "Anyway, it's not like I'm planning to make a habit of this!"
            "I'll watch this one time...just to see what happens."
        "Keep watching" if game.get_flag_value("morality") < 0:
            "Oh wow - this is the chance of a lifetime!"
            "Sasha's actually pleasuring herself in there, right now."
            "And it looks like I might just have stumbled upon her as she's getting to the best part!"
            "I press my eye closer to the keyhole, straining to get the best view as possible."
            "As I do so, I can't help wondering if Sasha knows that someone could be watching her right now."
            "Perhaps she does, and that's all part of the thrill for her?"
            "I mean, if she wants to do something like that in privacy, why wouldn't she have kept the noise down?"
            "The walls around here aren't paper thin, but all the same, noise still carries."
            "Come to think of it, Sasha might have done everything in her power to tip off Mike and me to the fact that she's doing this."
            "So it'd be pretty rude to ignore the show she's putting on for our benefit."
            "Not to mention prudish to be offended or outraged too!"
    if game.get_flag_value("morality") >= -25:
        $ game.set_flag("morality",1,mod="-")
        $ NOTIFICATIONS.append(["{image=ui/icon_bad.png}+1",2])
    "I don't think I've ever seen Sasha looking more worked up than she does right now."
    "Her normally pale, milky skin is suffused with a rosy, pink flush that's most intense in her cheeks."
    "And she's almost glistening with perspiration, as she pants with her tongue almost hanging out of her mouth the whole time."
    "By now she's laid on her belly, with her head against the pillows and her backside hoisted in the air."
    "I can see her little round breasts hanging down beneath her, swaying in time with the way she's moving."
    "Sasha has her left hand reaching around to part her buttocks and encourage the lips of her pussy to spread in sympathy."
    "The right hand is doing a pretty good job of parting them the rest of the way."
    "As well as rubbing frantically at the sensitive, exposed flesh within."
    "I can't honestly tell if the glistening slickness of Sasha's pussy is from the lube on the toys or a natural consequence of what she's doing to herself."
    "But either way, the intensity of the act is causing it to slide down the inside of her legs in rivulets."
    "It's a tough decision whether to watch Sasha's face as she pants and moans, or her hands as they make her do the same."
    "As my eyes dart between the two, I can feel myself getting hotter and more excited in sympathy."
    "I can already feel that tell-tale tingling between my own legs that's telling me I'm being turned on, whether I like it or not."
    "Unconsciously, my hand drifts towards the exact same spot, pushing under the waistband of my panties before I truly know what it's doing down there."
    "It's then that Sasha either saves me from myself or ruins my fun, based on your point of view."
    "She beigns to literally push two of her fingers inside of herself, at the same time stroking at her clit with her thumb."
    "This is enough to start her on the inevitable path towards her climax, as her panting and moaning increase noticeably as she does so."
    "In sympathy, Sasha's body twitches and jerks like never before."
    "She arches her back, pushing her head into the pillows at the top of the bed."
    "Whether she does this for relief or in the hope of stifling her cries of pleasure, it seems to achieve neither."
    "Sasha cums then, collapsing into a sweaty heap of limbs as her muscles finally betray her and turn to water."
    "I watch as she writhes helplessly on the bed, wrapping herself in the bedclothes before finally curling up into a foetal position."
    "After that, Sasha doesn't move for the whole while that I stay there, still peeping through the keyhole."
    "She could be awake, sleeping or unconscious for all I can tell."
    "Soon enough I'm skulking off back to my own room, already wondering what I'm going to do about the head-full of images I now possess."
    "I might sleep in tomorrow morning, or at least wait until Sasha goes out for the day before showing my face."
    "I'm just not sure that I can stomach looking at her over the breakfast table for a while."
    hide sasha
    return

label sasha_masturbation:
    $ hero.activity.set_flag("canceled",True)
    "I'm not normally the kind of guy to be caught sneaking around for the sake of looking through a keyhole in the hope of being able to see something that's supposed to be strictly private."
    "But I'm also only human, and living with a couple of female housemates as cute as Bree and Sasha means that there are times when I just can't help myself and the normal rules go straight out the window."
    "I don't wander around the house, waiting for such an opportunity to arise like a raving pervert."
    "They just seem to happen when you least expect it, and before I can reign myself in, I'm utterly, helplessly hooked."
    "This is a good example of what I mean - all I intended to do was walk back downstairs from the bathroom to my own room."
    "There was the addition of a stop in the kitchen to make a snack, but that was it."
    "It's just that halfway across the upstairs corridor; I hear a sound coming from behind the door to Sasha's bedroom."
    "So what, you might say - surely there are sounds coming from both of the girls' bedrooms most of the time they're in there?"
    "But you see, the thing is that these are the kind of intriguing sounds capable of stopping most people in their tracks."
    "I can hear deep, breathy series of sighs and moans that just keeps on getting louder and louder by the second."
    "Thinking that I'll just listen for a moment or two, long enough to confirm my suspicions as to what's going on in there, I walk as quietly as I can over to Sasha's door."
    "Before I can put my ear to the door, I see a chink of light emerging from the keyhole."
    "Again, I swear that I don't make a conscious decision to crouch down and squint through the hole - I just kind of find myself doing it."
    "But almost as soon as my eye adjusts to the light coming from the keyhole, any thought of the morality of what I'm doing is utterly forgotten."
    "Instead I find myself rooted to the spot, straining to get a better view of what I can see inside."
    show sasha mast
    "Upon the bed, laid on her stomach and with her backside up in the air is Sasha."
    "Utterly naked, her normally pale skin is flushed with a rosy shade of pink and positively glistening with perspiration."
    "Her head is turned so that I can make out the almost dazed expression she wears upon her face, and her mouth hangs open as she pants and moans."
    "As if I needed any further explanation of just what she's in the middle of doing to herself, I see sex-toys and lubed-up dildos strewn on the bed around her."
    "Sasha's left arm is stretched behind her, spreading her buttocks as wide as she can manage."
    "At the same time, the right is reaching under her belly and between her thighs, stroking fervently at her exposed pussy."
    "Even if I could get my head straight and think about how much of an intimate moment I'm peeping in on here, I don't think that I could tear myself away from the keyhole."
    "A part of me is disappointed to have missed the sight of Sasha getting those sex-toys into such a wonderfully filthy state."
    "But what could be better than actually getting to see the moment where she's stroking herself towards cuming with such obvious and audible passion?"
    "I watch with rapt attention as Sasha's fingers perform a dextrous dance over the lips and folds of her pussy."
    "Each touch seems to send shivers of pleasure shooting through her already aroused body, as if she were electrifying every inch of her skin."
    "Her task is made that much easier by the combination of lube and natural juices that I can see making her pussy as slick as can be."
    "Even the insides of her thighs seem to be as well-oiled, as rivulets of the same viscous fluid run down towards the bedclothes below."
    "Part of me is watching simply for the voyeuristic pleasure of seeing Sasha pleasure herself without fear of being disturbed."
    "But another is trying to make mental note of where she touches her pussy and how."
    "I'm not clueless when it comes to the ways in which most women like to be touched down there."
    "But tell me how often a guy gets a chance to see for himself just what turns a particular girl on?"
    "And think of the kudos that kind of knowledge could earn when put to good use with the girl herself..."
    "I watch as Sasha sinks two of her fingers slowly into her pussy, working them in and out, the speed increasing as she goes."
    "At the same time her thumb begins to press down on her clit, massaging the sensitive spot without mercy."
    "Just when I think that I can see what's finally going to bring her off, the fingers of the hand spreading her buttocks begin to move as well."
    show sasha mast ass
    "Reaching down, Sasha feels for her anus and then pushes a finger in so deep that it almost disappears from view up to the knuckle."
    "Working herself up with both holes at once, her cries seem to reach a peak in very short order."
    "My own cock has been hard almost since the moment that I started watching through the keyhole."
    "But now I can't keep from rubbing at it through my pants as I watch Sasha begin to cum at her own hand."
    "While the sight of what she's doing to herself is unbelievable, it's the expression on her face in that moment that really turns me on."
    "I guess I'm used to seeing her with a knowing grin or rolling her eyes at something dumb that came tumbling out of my mouth."
    "To see her features almost rendered insensible by the pleasure that she's experiencing is something I don't think I'll ever forget."
    "It's all that I can do to keep my hand from creeping into my own pants and following her example."
    "And that's something which almost becomes a battle as Sasha tosses her head back and starts to yelp at the arrival of her climax."
    "Laid there, with her ass in the air and her pussy exposed, she cums more like an animal on heat than a girl bringing herself off."
    "Sasha's eyes glaze over and her tongue begins to lol out of her mouth, the first hints of drool escaping from the corner of her mouth as it does so."
    "Finally, her legs begin to wobble from exhaustion, and she literally collapses onto the bedclothes, adding to the dark patches that she's already dropped beforehand."
    "Though her eyes are closed, I have no way of knowing if Sasha's asleep or just momentarily unable to summon the strength to open her eyes."
    "Not wanting to be caught out either way, I clamber to my feet and continue on my way back to my room, trying to hide my painful erection as I go."
    "All thought of visiting the kitchen for a snack is forgotten as I struggle to keep the images of what I've just witnessed fresh in my mind."
    "I wouldn't tell her as much, but Sasha's not going to be the only person that she managed to make cum in this house tonight."
    hide sasha
    return

label sasha_propose:
    call sasha_greet
    if game.get_flag_value("homeharem") and bree.room == game.room and not "bree" in HIDDEN and hero.has_item("wedding ring") >= 2 and not bree.get_flag_value("engagedmike"):
        call propose_bree_and_sasha
    else:
        show sasha
        "I really want to keep as far away from the traditional trappings of a proposal as I can for this, as I'm not exactly asking a traditional girl to marry me."
        "But despite the effort that I've gone to in order to avoid all of the cliches, it's more than worth it for the sake of making the proposal unique."
        "And that's because Sasha's pretty damn unique herself - and it's one of the things that makes me love her the way that I do..."
        "This means that I don't plan a huge gesture or go down on one knee in public with all eyes upon me."
        "Instead, I pick a quiet, intimate moment and pull out the ring without a great deal of ceremony."
        hero.say "Sasha, I have something I've been meaning to ask you..."
        if sasha.love < 100:
            show sasha sad
            "Much to my distress, the look of surprise in Sasha's eyes soon turns to agonised discomfort."
            sasha.say "Oh, [hero.name] - why'd you have to go and do a silly thing like that?"
            sasha.say "I was happy with things just the way they were."
            sasha.say "But this pretty much tells me you're not..."
            "I honestly don't know what to say."
            "How could I have misjudged the situation so badly?"
            $ sasha.love -= 25
            $ sasha.sub -= 25
        else:
            show sasha happy
            "At the sight of the ring, Sasha's eyes light up with what looks like genuine happiness."
            sasha.say "Oh, [hero.name] - are you asking me to marry you?!?"
            hero.say "Y...yes...yes I am, Sasha."
            hero.say "And...is that a yes?"
            sasha.say "Yes, of course it is!"
            sasha.say "I always dreamed of marrying my best friend - and now that dream's coming true!"
            $ sasha.set_flag("engagedmike")
            $ hero.lose_item("wedding ring")
    return

label sasha_cheated:
    show sasha
    if (game.get_flag_value("homeharem") == 1 and game.active_girl.id in ["bree"]) or (game.get_flag_value("bandharem") == 2 and game.active_girl.id in ["kleio", "anna"]):
        sasha.say "Give me back my toy!"
        show expression "sasha kiss "+sasha.get_clothes()
        "And without warning Sasha kisses me."
        $ sasha.love += 1
        hide expression "sasha kiss "+sasha.get_clothes()
    else:
        $ sasha.set_flag("cheated", game.active_girl.name)
        sasha.say "What the fuck do you think you are doing you moronic ape?"
        $ sasha.love -= 20
    hide sasha
    return

label smartphone_sasha_hint:
    $ story = sasha.get_flag_value("story")
    if story == 0:
        "I should never say this."
    elif story == 1:
        "Maybe I could help Sasha unpack in her room."
    elif story == 2:
        "I wonder if Sasha goes to the pub sometimes?"
    elif story == 3:
        if sasha.love < 30:
            "I should ge to know Sasha better."
        else:
            "I think I heard noises coming from Sasha's bedroom at night."
    else:
        "I reached the end of Sasha's story for now."
    return

label sasha_play_pool:
    show sasha
    "I splash some water towards Sasha."
    sasha.say "Dimwit ! You'll regret that!"
    "After that she retaliates and we play in the water for a while..."
    sasha.say "That was fun!"
    hero.say "It sure was."
    $ sasha.love += 1
    $ sasha.set_flag("greeted",True,1)
    return

label sasha_tv:
    call sasha_greet from _call_sasha_greet
    show sasha
    if hero.charm >= 40 - sasha.love() or sasha.get_activity()[1]["activity"] == "tv":
        $ sasha.set_flag("daily_interact",1, 1, "+")
        sasha.say "Ok."
        python:
            choices = ["Action movie","Cartoon","SciFi movie","Fashion show", "Discovery channel", "Romantic comedy", "Porn", "Horror movie", "News", "Reality show", "Music channel"]
            for i in range(6):
                choices.remove(randchoice(choices))
            result = renpy.call_screen("select",choices)
        if game.hour > 20 and not game.get_flag_value("female"):
            show tv sasha
        if result == "Action movie":
            $ renpy.say("", randchoice(["We watch an action movie.","We watch a movie with "+randchoice(["Schwarzenegger","Stallone","Statham"])+".","We watch a "+randchoice(["Die Hard","Rambo","Dirty Harry","James Bond"])+" sequel."]))
            "Sasha looks a completly bored."
            $ sasha.love -= 1
        elif result == "Cartoon":
            "We watch a funny cartoon."
            "Sasha looks a completly bored."
            $ sasha.love -= 1
        elif result == "News":
            "We watch the news."
            "Sasha looks a completly bored."
        elif result == "Reality show":
            $ a = randchoice(["dead", "bimbo", "nazi","smart","real","fake","gay","stupid","angry","cute","white","black","racist","socialist","poor","rich","ugly","sexy","fat","mean","nice","old","young","virgin"])
            $ b = randchoice(["housewives","cops","millionaires","geeks","sluts","nuns","cats","dogs","grannys","middle aged men","asians","government officials","strippers","doctors","truck drivers"])
            $ c = randchoice(["the world","venezuela","paris","mars","the sewers","new-york","france","spain","seattle","los angeles","my basement","texas","mexico","brazil", "space"])
            $ d = randchoice(["of","against","meet","discover","lost in"])
            $ t = (a+" "+b+" "+d+" "+c).title()
            "We watch [t]."
            "Sasha looks a completly bored."
        elif result == "Music channel":
            "We watch a concert."
            "Sasha enjoys herself very much."
            $ sasha.love += 3
        elif result == "SciFi movie":
            "We watch a scifi movie."
            "Sasha seems to enjoy herself."
            $ sasha.love += 1
        elif result == "Fashion show":
            "We watch a fashion show."
            "Sasha seems to enjoy herself."
            $ sasha.love += 1
        elif result == "Discovery channel":
            "We watch a discovery channel."
            $ sasha.love += 1
        elif result == "Romantic comedy":
            "We watch a romantic comedy."
            "Sasha seems bored."
        elif result == "Porn":
            "We watch some porn together."
            if hero.charm >= 80 - sasha.love():
                menu:
                    "SM porn":
                        $ sasha.sub += 1
                    "Femdom porn":
                        $ sasha.sub -= 1
                    "Gonzo porn":
                        $ sasha.love += 1
                    "Lesbian porn":
                        $ sasha.love += 1
                        $ NOTIFICATIONS.append(["Sasha {image=ui/icon_les_vsmall.png}+5",2])
                        $ sasha.set_flag("lesbian",1,mod="+")
                "Sasha seems to be quite excited by the sight."
                if sasha.love >150 and sasha.get_flag_value("sex") and not game.get_flag_value("female"):
                    show couch fun sasha
                    "Sasha wraps her fingers around my shaft and rolls her tongue out, licking up along my length."
                    hero.say "O... oh wow..."
                    hero.say "It feel so good."
                    sasha.say "I kind of knew this would please you..."
                    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                        sasha.say "...master."
                    "Again, she licks up my shaft, up over the glans and over the tip."
                    "What did I do to deserve the greatest roomate in the world?"
                    "I wonder this as the excitement of her actions tingles up through my body."
                    show couch fun sasha cumshot
                    "I can’t hold back and, with a groan, I release, shooting up onto her."
                    "Cum sprays up onto her face, getting her nice and covered by my jizz."
                    hide couch
                    show couch fun sasha facial
                    "Sasha smiles up at me, batting her half-lidded eyes up in my direction."
                    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                        sasha.say "Enjoy this view, master."
                    else:
                        sasha.say "Enjoy this view, [hero.name],"
                    "Sasha takes a finger and slips a drop of my cum off of her face."
                    "She then wraps her lips around my cock, moaning in delight at the taste."
                    hide couch
                $ sasha.love += 1
            else:
                "Sasha seems to enjoy herself a little."
                $ sasha.love += 1
        elif result == "Horror movie":
            "We watch a horror movie."
            if not sasha.get_flag_value("zombietalk"):
                hero.say "Okay, in no way is this movie based on a true story."
                sasha.say "It's a future true story."
                sasha.say "A zombie apocalypse is going to happen."
                sasha.say "l mean, studies show only one of us would survive."
                sasha.say "The question is, which one? Depends on survival strategy, you know?"
                sasha.say "Are we talking strength to fight them or ability to blend in and live amongst them ?"
                sasha.say "All right, if we're gonna do ability to blend in, l say you."
                sasha.say "You are basically a zombie."
                sasha.say "Wake up at 7:00, shower, eat."
                sasha.say "Eh And, like a zombie, you don't really have any hopes or dreams."
                hero.say "l have dreams."
                sasha.say "Really?"
                $ result = renpy.display_menu([("Finding love",1),("Becoming rich",2),("Banging a lot of women",3)])
                if result == 1:
                    hero.say "Look, l'm looking for the love of my life."
                    $ sasha.love -= 1
                elif result ==2:
                    hero.say "Look, l'm going to be filthy rich."
                    $ sasha.love += 1
                else:
                    hero.say "Look, l'll fuck every women I can."
                sasha.say "Oh, yeah, you seem to be doing just fine."
                hero.say "l can tell you who would die first in a zombie attack."
                hero.say "l mean, it's obviously you."
                hero.say "You are out of shape, have no marketable talents, and no survival skills."
                sasha.say "There are things in this world that you love."
                sasha.say "That's slows people down."
                sasha.say "My cold, black heart and living without attachments to anyone or anything, that's my greatest asset right there."
                $ sasha.set_flag("zombietalk")
            else:
                "Sasha seems to enjoy herself very much."
            $ sasha.love += 2
        if sasha.sub <= -50 and sasha.love >= 100 and hero.check_skill("massage") and game.week_day in [1,2,3,4,5] and sasha.get_flag_value("footrub") == 4 and game.hour > 20:
            "To a casual observer, it might appear that there's absolutely nothing going on in the living room apart from what can be seen with the naked eye."
            "There's just Sasha and myself, sitting on either ends of the sofa with the TV blaring out the standard fare that we like to unwind to when we have the time."
            "But we both know full well that there's an unspoken agenda here."
            "One that she's just keeping me in a state of suspense over, and enjoying every minute of it too."
            "Neither of us says a word, only casting the occasional furtive glance in the direction of the other."
            "Whenever my own eye catches Sasha's, I can't help but look away quickly as she smiles in plain amusement at my discomfort."
            "Eventually, just when I think that I'm about to snap from the tension, I feel the sensation of something landing upon my lap."
            "Even though it's exactly what I've been expecting to happen sooner or later, I still can't help jumping a little in surprise."
            "This earns me a laugh from Sasha, and it's all the sound that she needs to make, as I know exactly what's expected of me in this situation."
            hide sasha
            show sasha foot massage
            "Without a moment of pause or hesitation, I take Sasha's bare foot in both hands and begin to work away at the sole with my thumbs."
            "This isn't the first time that she's demanded such treatment from me, and I know the drill pretty well by now."
            "Hell, I've even been watching videos online to pick up some hints and tips on how to make my foot rubs something special, for her sake alone."
            "I can soon hear the evidence of this paying off too, as Sasha begins to make appreciative noises and recline on the sofa."
            "A chance moment of glancing upwards from my task shows me that she's closed her eyes in order to better savour the effects of the massage as well."
            "This means that I can watch freely as she succumbs to the pressure that I'm applying in all of the right amounts and in all of the right places."
            "Sure, it might look like Sasha's the boss in our relationship and that I'm afraid to step a foot (if you'll pardon the pun) out of line with her."
            "But the truth is that I actually enjoy being able to please her like this, and it makes me know that she needs me too."
            "I know that she's not just walking all over me (again with the puns, sorry) right now."
            "What I'm doing shows her just how much I care."
            "It shows that she can ask anything of me and I'll always rise to the challenge."
            "As far as she's concerned, nothing's too much trouble - and I mean that."
            sasha.say "Mmm...[hero.name]...that feels SO good!"
            sasha.say "But you know what - I think it'd feel much better if you used your tongue instead..."
            menu:
                "Don't do it":
                    $ sasha.set_flag("footrub",0)
                    $ sasha.sub += 1
                    $ sasha.love -= 1
                    "Feel better for who, exactly?!?"
                    "I mean, as much as I like giving Sasha a massage like this, that's asking too much!"
                    hero.say "I hear what you're saying, Sasha."
                    hero.say "But I don't think I'm up for doing that right now."
                    hero.say "Have you even washed your feet today?"
                    "Sasha, of course, looks instantly annoyed."
                    "But I can't tell if it's more on account of my refusal to do what she wants or my suggesting that her feet might be less than squeaky clean."
                    "Either way, she doesn't say a single word in response, only yanks her foot out of my grasp and then turns her back on me in a huff."
                "Do it":
                    $ sasha.set_flag("footrub",1,mod="+")
                    $ sasha.sub -= 5
                    $ sasha.love += 5
                    "What the hell?"
                    "It's not like I haven't licked other parts of Sasha's body in the past, now is it?"
                    "And the look on her face is telling me that she's already pretty into the idea of me doing it to her."
                    "So what have I got to lose?"
                    "I shrug and give Sasha a smile as I nod to show my assent."
                    hero.say "Sure, why not?"
                    hero.say "If I have to kiss someone's feet, why not yours?!?"
                    "Sasha returns my smile, looking all the while like the cat that got the cream."
                    "Who would have thought all you needed to do to keep such an amazing girl happy was keep on giving her whatever she wants?"
                    "It's just so simple - why did I never hit upon the idea before now!"
                    hide sasha
                    show sasha foot lick
                    "I lift Sasha's foot up a little, just enough so that I can lean forward and reach it with my lips."
                    "The truth is that, up this close, it doesn't really smell all that bad."
                    "There's just the lingering scent of her socks and shoes, but nothing that could put me off."
                    "I'm not sure of just where to begin, so I fall back on the basics, kissing the sole at first."
                    "The skin is softer than I expected it to be, and I'm thankful for the fact that Sasha has such healthy and pristine feet like never before!"
                    "She giggles and flinches a little in response, betraying just how ticklish she actually is."
                    "Of course the laughter only serves to begin to turn me on, and I respond by taking my first actual lick at her foot."
                    "Sure, it tastes a little bitter against my tongue - but what's that compared to how weird an actual pussy tastes?"
                    "And anyway, I soon forget about all of that when I hear the reaction that it gets out of Sasha."
                    "After that there's no stopping me, and I find myself licking the entire length of the sole, over and again."
                    "I try to trace the lines and curves of her muscles, just like I would with my fingers."
                    "But my tongue doesn't seem to have the same amount of stamina, and I soon have to limit myself to gentle, sensual passes instead."
                    "I work my way vaguely upwards, starting each new lick from a higher point, until I finally reach Sasha's toes."
                    "Then I work inwards from the smallest, liking around the bottom of them and then sucking them into my mouth one by one."
                    "While I might not hear any evidence of Sasha being on the brink of cuming from what I'm doing to her, she keeps up the moans and sighs the whole time I'm at it."
                    "And when I'm finally finished, she looks almost as relaxed and satisfied as I do exhausted and tongue-tied."
        elif sasha.sub <= -25 and sasha.love >= 100 and hero.check_skill("massage") and game.week_day in [1,2,3,4,5] and sasha.get_flag_value("footrub") >= 5 and game.hour > 20:
            $ sasha.set_flag("footrub",3,mod="-")
            $ sasha.sub -= 5
            $ sasha.love += 5




            "I can't quite put my finger on it, but there's an odd cast in Sasha's eyes whenever she looks over in my direction."
            "It's not hostile in any way, just enough to make me feel a little nervous."
            "I feel as if she's watching me, waiting for the right moment to spring an unexpected surprise."
            "My legs are stretched out in front of me as I recline on the sofa, but Sasha's are laid across the length of it."
            "She has her head propped up on cushions at the other end and her bare feet resting idly in my lap."
            "They've been still and unmoving for a while now, but then I feel movement and look down at them."
            "Sasha's begun the rotate her feet, stretching them as she clenches and unclenches her toes."
            hide sasha
            show sasha foot massage
            "Almost absent-mindedly, I take hold of her left foot and begin to massage the sole with my thumbs."
            "I should say that I'm not any kind of serous foot fetishist, but also that I'm not phobic of them either."
            "And Sasha does have one of the nicer pairs of feet that I've ever had the privilege of handling in this manner."
            "I'm also not a professional masseur, but it's almost impossible not to get a positive reaction from giving a foot-rub unless you're absolutely clueless."
            "Sasha begins to make appreciative sounds almost immediately, though she doesn't take her attention off of the TV show she's assiduously not watching."
            "That's fine by me, as it's enough to know that she appreciates my efforts, no matter how small."
            "I move on from the left foot to the right, repeating the same process and taking an equal amount of time and care."
            "It's only when I finish my massage on the second foot that I actually look up and realise that Sasha's no longer pretending to watch the TV."
            "Instead she's watching me, her face reminding me of a satisfied cat."
            "Or maybe one that's just woken from its nap and finds itself feeling a little frisky."
            sasha.say "You know, [hero.name], you're pretty good with your hands."
            hero.say "Th...thanks, Sasha!"
            "I hope that my eager grin at her praise doesn't make me look too goofy."
            sasha.say "But I tell you what...I bet I'm better."
            sasha.say "In fact, I bet you that I'm even better with my feet!"
            "What does she mean by that?"
            "Is she about to walk all over me, like they do in those oriental massage parlours?"
            "While I kind of enjoy her doing it in a metaphorical sense, I don't know if I'm up for Sasha doing it in a literal one too!"
            sasha.say "Open your flies, [hero.name]."
            "It's not a request, nor even really a command."
            "More of a statement of what's going to happen without the thought of it being objected to."
            "Even so, I find myself hurrying to do as I'm told, already intrigued to see exactly what Sasha has in mind."
            sasha.say "Good...now get your dick out."
            "Again I follow her instructions, pulling my cock out of my pants and allowing it to flop into my lap and onto Sasha's naked feet."
            show sasha foot footjob blush
            "Sasha smiles indulgently at me as she begins to move her toes, causing my cock to bounce up and down as they do so."
            "She tries to catch it between her feet, clumsily at first, but then slowly getting the hang of it a little at a time."
            "I can already feel my cock beginning to get hard, which serves to make her job that much easier as it rises of its own accord."
            "Though I can't be sure if the erection's more on account of what she's doing with her feet now or the thought of what might come next."
            "I've heard of foot-jobs, but I've never actually had one before now."
            "They're not on my regular list of preferences for porn viewing either, so this could be a true voyage of discovery for me."
            "Once my cock is as stiff as it's going to get, Sasha starts to rub the soles of her feet up and down its length."
            "All the time she does her best to keep it held between them, so that I feel the touch of her soles as they work my shaft."
            "The clumsiness of her feet means that she has to go slowly and carefully, making the whole experience that much more sensual and involved for me."
            "While I might miss the delicate touch of more dextrous fingers or a tongue, the fact that Sasha's feet are larger means that I can feel more of my cock being caressed."
            "She varies her technique then, using the sole of one foot to press my dick against the other."
            "Her left foot is above and the right below, so that I'm pressed into the former by the latter."
            "Soon Sasha seems to have become comfortable enough to settle into a routine of switching between these two positions."
            "One moment she uses both feet on me, and the next she changes so that one holds me while the other rubs against it."
            "Again the care required of her and the size of her soles ensure that I find the whole experience exquisite in the extreme."
            "I honestly think that Sasha could have brought me off doing just that if she had been of a mind to."
            "But I can see, from the amused look on her face as she watches me gasp from her efforts, that she already has something else in mind."
            "It's then that Sasha begins to use her toes to grip and squeeze the sensitive skin of my cock."
            "If I thought that the soles of her feet were good to feel against my dick, then I was in no way prepared for the sensation of the muscular balls of her feet."
            "I feel as though I'm being seized and massaged by miniature and yet strong hands."
            "Sasha uses both feet to clutch me close to the head of my cock, and then starts to work the shaft almost as if giving me a hand-job."
            "Only now does she start to go faster, perhaps sensing that this is a more familiar technique and feeling more comfortable as a result."
            show sasha foot footjob orgasm
            "The effect on me is pretty much the same - I quickly go from feeling relaxed and like I'm being eased towards an orgasm to the urgency of the thing taking over completely."
            "Her toes are digging into me now, the motion of her feet needing the entirety of her legs to move in order to keep up the pace."
            "I hadn't noticed before, but my own hands are clutching handfuls of the sofa cushions and my toes are gripping the pile of the carpet as if they fear to let go."
            "Sasha shifts her feet slightly, so that they're clasping my cock between them now."
            "She continues to massage with her toes, but now most of the motion is coming from her legs and she reminds me of a cricket using it's limbs like a fiddle."
            show sasha foot footjob cum
            "Faced with all of this sensation and the strength of Sasha's entire lower half, I can already feel myself cuming."
            "Moments later, I see the evidence of this as it's forced from between her clenching toes and begins to run down the tops of her feet."
            "As I pant from my exertions and my cock starts to go flaccid again, Sasha makes no effort to remove her feet."
            "Instead she keeps them right where they are, still enjoying the feeling of massaging the softening length of my cock now that she has my cum between her toes and on the soles of her feet."
            "I should try to get up and clean myself off, definitely change my pants."
            "But for the moment, all I can do is lie slumped upon the sofa, staring at the satisfied and triumphant look on Sasha's face."
            hide sasha foot
        elif sasha.sub <= 0 and sasha.love >= 50 and hero.check_skill("massage") and game.week_day in [1,2,3,4,5] and game.hour > 20:
            "I'm trying to finally turn my brain off after a particularly stressful day at work by bombarding it into submission with mindless TV shows, when Sasha walks into the room."
            "She makes a show of flopping down on the opposite end of the sofa from where I'm sitting, pulling her legs up onto the cushions as she does so."
            "When she doesn't as much as say a word, I feel like I'm being baited into breaking the silence, but do so just to stop it from getting too weird."
            hero.say "Hey, Sasha - how was your day?"
            "She sighs with a little too much of a practised sound to it for me to believe that she's being totally genuine, before she answers me."
            sasha.say "Ah, pretty tough, you know - really tiring too!"
            "I nod in genuine sympathy."
            hero.say "Me too - had to deal with this really awkward case where..."
            sasha.say "You know what, [hero.name] - I'm just too frazzled to be a good listener tonight, yeah?"
            "I shrug off the way that Sasha just shut me down, willing to accept that she's not in the mood to exchange stories about our mutually shitty day."
            hero.say "Okay...you just want to lounge around here with me tonight, watch some garbage TV?"
            "At this, Sasha makes an odd sort of non-committal sound, as though she wants something more, but won't straight out ask for it."
            "I notice that she's stretching her legs out now, frowning a little as she does so, as if to suggest there's pain involved in the movements."
            "As is her habit when she's lounging around the house with nothing better to do, Sasha's wearing shorts right now."
            "And this means that I'm getting a rather spectacular view of her long, shapely legs as she inches her feet ever closer to me."
            sasha.say "Well, [hero.name], I've been on my feet all day at work."
            sasha.say "And I was going to ask if..."
            "Sasha pushes her bare feet the last couple of inches needed to close the distance between us, and plants them in my lap."
            sasha.say "If you'd be a babe and give me a little bit of a foot rub?"
            "I look down at her pale, delicate feet as they're resting on my lap."
            "And then up at Sasha's endearing smile - a smile that seems to say what she's asking for is as innocent as passing her the remote or telling her the time of day."
            "I can't help gulping as I ponder my options."
            menu:
                "Do it":
                    $ sasha.sub -= 1
                    $ sasha.love += 1
                    "It's a simple choice, really - sit here and watch TV that's slowly melting my brain, or do the same whilst getting my hands on Sasha's feet."
                    "Come to think of it, is there really any choice at all?"
                    hero.say "I'm no professional masseur, Sasha - but I'll gladly give it my best shot."
                    "Sasha smiles at this and sinks down lower on the sofa, only stopping when she's practically horizontal and I can easily get at the soles of her feet."
                    sasha.say "Oh, [hero.name] - you're a godsend!"
                    sasha.say "I don't need my Chakras rearranged, just some life rubbing back into them!"
                    show sasha foot massage
                    "I nod as I make sure my palms aren't sweaty, and then gently take hold of her right foot."
                    "When I told Sasha that I wasn't a masseur, it was the honest truth."
                    "And so the best that I can do is go on feeling and instinct, then keep an eye on how she reacts to what I'm doing."
                    "I begin by using my thumbs to rub around the heel of her foot, working my way slowly upwards as I go."
                    "Sasha's feet are as tight and tense as she claimed, but they soon start to loosen up under the firm but gentle pressure I'm applying."
                    "As my thumbs move further up the sole of her foot, I start to apply the balls of my thumbs to the parts that I've already been over."
                    "And soon I'm massaging as much of her foot as possible all at once."
                    "I'm hardly looking down at my efforts as I switch to Sasha's left foot and repeat the process."
                    "The sight of her sighing and beginning to breathe more deeply in response to the massage is far more compelling of a thing to watch."
                    "Getting the same treatment as the right foot, her left is soon as relaxed and supple too."
                    "From there, I switch to rubbing her toes, taking each one individually and never hurrying to move on to the next."
                    "Soon, Sasha's eyes are closed and she's paying no attention whatsoever to the TV."
                    "The expression on her face is almost enough to make me get hard myself, and I think I'm beginning to gain a certain sympathy for foot fetishists too!"
                    "When she finally opens her eyes once more and nods in satisfaction, I feel lost at the massage coming to an end."
                    sasha.say "Aww...thanks, [hero.name], that really did the trick!"
                    sasha.say "Hopefully I can sleep now."
                    "I shrug off her thanks and smile sheepishly, not knowing if I'll be able to do the same myself."
                    $ sasha.set_flag("footrub",1,mod="+")
                    hide sasha foot
                "Don't do it":
                    $ sasha.sub += 1
                    $ sasha.love -= 1
                    hero.say "Normally I would, Sasha, honestly."
                    hero.say "But I've got just the same problem with my hands."
                    "Sasha raises an eyebrow as she looks at me with visible disbelief."
                    hero.say "No, seriously - I spend all day typing away at a computer."
                    hero.say "So by the time evening comes around, my fingers are just as screwed-up as your feet must me right now!"
                    "Sasha rolls her eyes and shakes her head at this."
                    hero.say "It's the truth, Sasha - I'd be afraid of doing more harm than good..."
                    "She snorts in derision and drags her legs back over to her own side of the sofa."
                    "After that, we continue to watch TV while an awkward silence prevails."
        $ hero.fun+= 1.5
        if game.hour > 20:
            hide sasha tv
    else:
        sasha.say "Sorry, I don't have time right now."
        $ hero.activity.set_flag("canceled",True)
        hide sasha
    hide tv
    return

label sasha_meal:
    call sasha_greet from _call_sasha_greet_1
    if hero.check_skill("cooking") or hero.charm() >= 20:
        if game.hour < 12:
            show sasha breakfast
            sasha.say "It's nice having breakfast together."
        elif randint(1,2) == 2:
            show sasha diner
            call expression sasha.get_chat() from _call_expression_30
        else:
            show sasha diner
            $ say_meal = [
                "You are a not a bad cook...",
                "You'll make a fine bride some day.",
                "I can't eat one more bit.",
                "That soup was pretty good.",
                "Are you trying to make me fat?."
                ]
            $ sasha.say(randchoice(say_meal))
            $ sasha.love += randint(1,3)
        hide sasha
    else:
        if game.hour < 12:
            show sasha breakfast
        else:
            show sasha diner
        $ say_meal = [
            "I don't know what's worst, the company or the food...",
            "you don't get points for trying.",
            "Are you sure it's safe to eat?",
            "You should stop cooking... definitively...",
            "Are you trying to poison me?"
            ]
        $ say_meal = randchoice(say_meal)
        sasha.say "[say_meal]"
        $ sasha.love += 1
        hide sasha
    return

label sasha_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = sasha.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = sasha.get_activity(bye_hour)
    if not activity == sasha.activity:
        if day != game.week_day:
            $ sasha.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ sasha.set_flag("activity-"+str(day)+"-"+h,activity, "day")
        show expression "sasha "+bye_outfit
        if activity["activity"] == "sleep":
            sasha.say "I am smashed, I should go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            sasha.say "I'll go clean myself up now, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            sasha.say "I've got to run or I'll be late for work, bye."
        elif activity["activity"] in ["meal"]:
            sasha.say "I am starving, I'll go grab a bite!"
        elif activity["activity"] in ["tv"]:
            sasha.say "I am bored, I'll watch some tv I think."
        elif activity["activity"] in ["drink"]:
            sasha.say "I'll go to the pub and have a drink, see you around."
        elif activity["activity"] in ["sunbath"]:
            sasha.say "It's sunny today, I think I'll go laze around near the pool."
        elif activity["activity"] in ["shop"]:
            sasha.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            sasha.say "I'll go read a book now, that's how bored I am."
        elif activity["activity"] in ["dance"]:
            sasha.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            sasha.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            sasha.say "I ll go get dressed up."
        hide expression "sasha "+bye_outfit
    return

label sasha_greet:
    if not sasha.get_flag_value("greeted"):
        show sasha
        $ sasha.set_flag("greeted",True,1)
        $ result = randint(1,3)
        if not "sasha_sub_event_1" in DONE or sasha.sub < 75:
            if result == 1:
                sasha.say "Hello."
            elif result ==2:
                sasha.say "Hi, [hero.name]."
            else:
                if game.hour < 6:
                    sasha.say "Hello [hero.name]."
                elif game.hour < 12:
                    sasha.say "Good morning [hero.name]."
                elif game.hour < 19:
                    sasha.say "Good afternoon [hero.name]."
                else:
                    sasha.say "Good evening [hero.name]."
            $ result = randint(1,3)
            if result == 1:
                hero.say "Hello, Sasha"
            elif result == 2:
                hero.say "Hi."
            else:
                if game.hour < 6:
                    hero.say "Hello."
                elif game.hour < 12:
                    hero.say "Good morning Sasha."
                elif game.hour < 19:
                    hero.say "Good afternoon Sasha."
                else:
                    hero.say "Good evening Sasha."
        else:
            if game.hour < 6:
                sasha.say "Hello Master."
            elif game.hour < 12:
                sasha.say "Good morning Master."
            elif game.hour < 19:
                sasha.say "Good afternoon Master."
            else:
                sasha.say "Good evening Master."
            if game.hour < 6:
                hero.say "Hello my slave."
            elif game.hour < 12:
                hero.say "Good morning my slave."
            elif game.hour < 19:
                hero.say "Good afternoon my slave."
            else:
                hero.say "Good evening my slave."
        hide sasha
    return

label sasha_kiss:
    if not sasha.love() >= 70 and not sasha.get_status() in ["girlfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show sasha wtf
        "Sasha slaps me."
        if game.get_flag_value("female"):
            sasha.say "Try that again and I'll cut your tits off."
        else:
            sasha.say "Try that again and I'll cut your balls off."
        $ sasha.love -= 2
        hide sasha
    elif not sasha.love() >= 120  or (game.get_flag_value("datescore") >= 75 and not sasha.love() >= 70):
        $ sasha.set_flag("kiss",1,"permanent","+")
        hide sasha
        if not game.get_flag_value("female"):
            show expression "sasha kiss "+sasha.get_clothes()
        if randint(1,2) == 1:
            "Sasha looks surprised but doesn't resist..."
            "When we part she look me in the eyes."
        else:
            "Sasha kisses me softly."
        if not game.get_flag_value("female"):
            hide expression "sasha kiss "+sasha.get_clothes()
        $ sasha.love += 1
        $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != sasha and renpy.has_label(g.id+"_cheated")]
        if cheated_girls:
            call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_50
        elif not sasha.get_flag_value("kiss"):
            show sasha blush
            sasha.say "If you wish to give me another one of those, don't hesitate."
            "After that line she turns around and leave."
    else:
        $ sasha.set_flag("kiss",1,"permanent","+")
        hide sasha
        if not game.get_flag_value("female"):
            show expression "sasha kiss "+sasha.get_clothes()
        if randint(1,2) == 1:
            "Sasha grip my neck and stick her wet tongue in my mouth. I can feel that she is waiting for more."
            "After what feel like an eternity, we part, breathless..."
            $ sasha.love += 1
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != sasha and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                if not game.get_flag_value("female"):
                    hide expression "sasha kiss "+sasha.get_clothes()
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_51
            elif not sasha.get_flag_value("kiss"):
                if not game.get_flag_value("female"):
                    hide expression "sasha kiss "+sasha.get_clothes()
                show sasha blush
                sasha.say "I was getting tired of waiting"
                "After that line she turns around and leave."
        else:
            "Sasha kisses me passionately."
            if not game.get_flag_value("female"):
                hide expression "sasha kiss "+sasha.get_clothes()
        $ sasha.love += 2
        hide sasha
    return

label sasha_fuck_date_female:
    $ sasha.set_flag("sex",1,"permanent","+")
    scene bg bedroom2
    show sasha
    "If I was nervous about going out on a date with Sasha, I'm even more so about taking it to the next level."
    "I know that I shouldn't be - this is the twenty-first century, for god's sake!"
    "And I'm not some religious nut or moral conservative either...but the alcohol certainly helps to ease my nerves as I let Sasha lead me into her bedroom."
    "Sasha's bedroom is a perfect reflection of her persoanlity, mostly black, covered in heavy metal posters and with the occasional splash of colour."
    "She begins to strip off her clothes, starting from the top and working her way down."
    "But she stops when she's down to her bra and panties, noting my own hesitation."
    sasha.say "What's up - you feeling like you're about to be eaten up by the Big Bad Wolf-Bitch?"
    hero.say "I'm sorry...I guess I'm just a little scared, that's all."
    sasha.say "Hey, there's no need to be."
    sasha.say "It's just like sex with a guy, only there's no dicks involved!"
    "I chuckle at the implied joke, beginning to feel more relaxed as Sasha's humour defuses the awkward moment."
    sasha.say "Would it help if I took the lead here?"
    "I nod silently, suddenly aware of how close she's standing to me and the fact that she's almost naked."
    sasha.say "Okay, just relax and trust me - you're going to love this."
    "With that, Sasha reaches out and begins to undress me."
    "I'm only wearing a pair of shorts and a sweater, but somehow she makes peeling them off of me feel like an intense and prolonged ritual of seduction."
    "Stepping out of my shorts as she pulls them down, Sasha wastes no time in unhooking my bra and then tugging at my own panties."
    "Completely naked now, I realise that she's enjoying being in a position of power over me."
    "The notion causes my cheeks to flush with colour, something that only serves to make Sasha's grin become wicked with intent."
    sasha.say "Up on the bed with you, come on."
    "Still blushing, I obey without saying a word."
    sasha.say "I want you on all fours...that's right, good girl!"
    hide sasha
    show bree doggy noone
    "I keep looking forwards, unable to see what Sasha is doing."
    "I think that I can hear her taking off the last of her clothes."
    "But there's also the sound of something else, almost like she's pulling on a belt or harness of some kind."
    sasha.say "Like I already said - one of the best things about doing it with another girl is that you get to decide whether or not there's a dick involved."
    sasha.say "But you can also choose who gets to use it as well!"
    "I can feel something brushing the cheeks of my ass, threatening to nudge itself between them."
    show bree doggy sasha
    "A glance over my shoulder makes me gasp in surprise at what I see there."
    "Kneeling on the bed behind me, Sasha is wearing one of the most impressive dildos that I've ever seen."
    "It glistens with lube in the subdued lighting of her bedroom, swaying slightly as she leans forwards to put it to use."
    "To put it to use on me!"
    "I can feel a strange mixture of arousal and fear making my pussy almost quiver in anticipation."
    "Half of me wants to cower away from the approaching dildo and the other half perversely can't wait to discover what it'll feel like."
    "But Sasha's not going to let the former happen, I know that much."
    "I feel her hands take a gentle but firm hold of my ass, pulling me towards her even as she thrusts forwards."
    "My pussy is a little tight at first, reflecting my trepidation."
    "But Sasha presses on regardless, using the dildo with the skill of a pro to stroke and tease my lips until I can't help sighing in genuine pleasure."
    "Now all I can feel is my resistance melting away, more with each second that passes and each new stroke at my pussy."
    "Instinctively I lower myself just a little, spreading my legs at the same time."
    "Now the tip of the dildo is literally pressing against the lips of my pussy, threatening to push in at any moment."
    "Sasha took the liberty of lubing it up beforehand, and now with my own body responding and things down there stretched apart, it's not a challenge to go further."
    "I'm no stranger to a man's dick inside of me, or using a dildo for my own pleasure."
    "But this somehow like both and yet neither."
    "Sasha is obviously getting a kick out of this, but she's not obsessed with getting herself off like a guy would be right now."
    "Likewise it's a totally different feeling to have someone else use a dildo on me rather than doing it myself."
    "As the head goes as far in as possible and the shaft rubs back and forth inside of me, I can't help but gasp in amazement at the sensations it creates."
    "But a large part of my pleasure is coming from the fact that I'm being brought off by Sasha's efforts alone."
    "My cheeks begin to burn anew as I realise how much I'm getting off on being treated like some glorified toy for her gratification."
    "All too soon I can feel the sensations becoming too much for me, and I begin to spill over into an orgasm."
    show bree doggy sasha ahegao
    "Cumming whilst on the end of Sasha's strap-on makes me redden all the more, but it also makes the whole experience that much more exciting too."
    $ game.room = "bedroom4"
    call sleep from _call_sleep
    return

label sasha_fuck_date:
    $ sasha.set_flag("sex",1,"permanent","+")
    scene bg bedroom1
    show sasha underwear
    play music "music/the_money_shot.mp3" loop
    "My door opens and I watch a little gape-jawed as Sasha comes down the stairs."
    "She's wearing a little black lace lingerie set, probably just for me."
    "That thought had me even more aroused than the sight of the beautiful woman in such an erotic outfit had gotten me; my boxers stands out a little as my cock starts getting hard."
    sasha.say "Happy to see me?"
    "Sasha's voice sounds like a pleased purr with a glint of humor in her eyes."
    menu:
        "Admit it":
            "A little surprised and embarrassed that she'd so easily turn me on, I look down and blush a little."
            hero.say "Why wouldn't I be?"
            "I ask, as if I don't know she's caught sight of the erection straining against my boxers."
            sasha.say "Aw.. no need to be shy..."
            "she murmurs, swaying her way up to me."
            "I can see the pink tint of her nipples through the black lingerie that cling to her small breasts."
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "I like it when you're 'happy' Master."
            else:
                sasha.say "I like it when you're 'happy'."
            $ sasha.love += 1
            $ sasha.sub -= 1
        "Taunt her" if hero.charm >= 25:
            hero.say "Want to come find out just how happy I am?"
            "I flash her a grin and she grins right back at me, looking me over with desire in her eyes."
            "I love the way her gaze pauses when it gets to my crotch; she's got a fine view of how aroused her appearance has made me."
            "She sways her way up to me, the shifting of her nightie teasing me with glimpses of skin beneath."
            "Looking her over, I'm fairly sure she's not wearing anything underneath that scrap of lace, and that makes my cock get even harder for her."
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "Let's see how much happier I can make you, Master."
            else:
                sasha.say "Let's see how much happier I can make you."
            $ sasha.love += 1
            $ sasha.sub += 1
    $ STRAP = False
    if sasha.sub <= -25:
        if not game.get_flag_value("sashastrapon"):
            sasha.say "You wanna try something new?"
            menu:
                "No":
                    hero.say "Not tonight..."
                    sasha.say "Too bad, you don't know what you are missing."
                "Yes":
                    $ STRAP = True
                    hero.say "What did you have in mind?"
                    sasha.say "I was thinking of having you take it in the ass for once"
                    hero.say "Say what now?"
                    "I know I've heard her correctly, but still!"
                    "That was direct."
                    "Yet... there's a bit of temptation."
                    "I wonder what it would feel like..."
                    sasha.say "I use a strap-on on you."
                    "She slinks over, running a hand down my chest and stomach."
                    sasha.say "Come on... it won't hurt. You might even like it..."
                    "Then she sticks out her lower lip and pouts at me in that adorably sexy way she's got, and I'm hooked."
                    hero.say "Alright."
        else:
            $ game.set_flag("sashastrapon")
            sasha.say "Wan't me to use the strap-on on you and make you my little bitch."
            "She slinks over, running a hand down my chest and stomach."
            sasha.say "Come on... You know you like it..."
            "Then she sticks out her lower lip and pouts at me in that adorably sexy way she's got, and I'm hooked."
            menu:
                "No":
                    hero.say "Not tonight..."
                    sasha.say "Too bad, but you do know what you are missing."
                "Yes":
                    hero.say "Alright."
                    $ STRAP = True
    if not STRAP:
        menu:
            "Use the anal beads" if "anal beads" in hero.inventory.keys():
                call sasha_beads_play from _call_sasha_beads_play
            "Use the rope" if "bondage ropes" in hero.inventory.keys():
                call sasha_bondage_sex
            "Just fuck her":
                call sasha_normal_fuck from _call_sasha_normal_fuck
    else:
        call sasha_strap_fuck from _call_sasha_strap_fuck
    hide sasha
    return

label sasha_strap_fuck:
    "I'm nervous as I lay down on the bed. Nervous, but excited; my cock is already standing tall and hard for Sasha, who smirks down at me."
    sasha.say "Come on.. you know the position, [hero.name]."
    "I do. "
    "I draw my knees up to my chest and spread my thighs."
    "It's the most vulnerable I've ever felt with a woman and for a moment I nearly change my mind..."
    show sasha strapon blush
    "She stands at the edge of the bed, stark naked and looking so hot."
    "She's strapped her toy on, black vinyl bands making stripes along her pale skin."
    "From the pelvis protrudes a pink cylinder with a rounded top; I know that it's got some give to it, and that it vibrates. "
    "I can't imagine how that's going to feel."
    "Sasha pours some lube into one hand and starts stroking that pink toy as she climbs onto the bed with me. "
    hide sasha
    show sasha strap
    "Once she's settled between my spread legs, she reaches out with her other hand to grab my cock and start stroking me with the same rhythm."
    "I was already hard, but this just turns me on more. "
    "Shivering, I grasp the backs of my thighs with each hand to keep my legs apart for her, knees drawn up so she has easy access to my backdoor."
    "Her hand drops from that toy --which is looking larger by the moment as anticipation and nervousness grows-- and I feel lube-slicked fingers circling around my anus, spreading that slippery fluid and teasing at sensitive skin."
    "To my surprise, it sends a little shiver up my spine; it feels good, especially with the slow and steady way she's stroking my cock."
    "Sasha takes her time lubricating my asshole before slipping a finger slowly in. "
    "It makes me tense at first, but she strokes my dick harder and I relax with a sigh."
    "She slowly pushes that finger in, then pulls it back out, rubbing the heated walls of flesh."
    "I slowly get used to the sensation, even squirming a little when she slows down for a moment."
    "Moving her hand briefly from my cock makes me grunt in protest. "
    "She dips her hand in the front of the strap-on rig and suddenly there's a buzzing sound and Sasha gasps, then laughs in a sensual manner. "
    "She must be getting that vibration too..."
    "That makes it hotter, knowing that she'll be feeling that hum constantly, having it press harder as she uses that toy on me."
    "Which starts surprisingly fast; she rests it atop my balls and I nearly jump out of my skin at the sensation!"
    "I've never played with vibrators on myself before, and the sensation is incredible! "
    "I can feel it tingling all the way through me, and a drop of pre builds up quickly, then drips down the underside of my dick."
    "Before it can hit my balls, Sasha's hand is wrapped around my cock again, slowly stroking. "
    sasha.say "Ready?"
    "With the way my cock is twitching, I'm beyond ready. As long as I don't think too hard about it. "
    "Not trusting my voice, I just nod."
    show sasha strap
    "It hurts just a little at first, I think mostly because I was expecting it to. "
    "Sasha slides the rounded tip in, guiding her toy carefully with one hand while the other continues stroking my rod and the ache gives way to pleasure."
    "She starts to rock her hips back and forth, leaning back and propping herself up on one hand so she can balance with her body on sexy display just for me."
    "I love the way her small, firm tits sway as she moves, pushing the toy just an inch or so in, then back out, giving my body time to get used to this. "
    "Soon enough, I'm groaning and more pre is dribbling down my dick, getting her hand sticky."
    "Good thing she likes her sex messy."
    "Bit by bit, she inches closer to me, which ever-so-slowly pushes this humming toy deeper into my ass. "
    "The vibrations are just incredible, almost too much for me to take, but by the way she's moaning, she'll wind up getting off on it."
    "Finally, my spread ass is between her thighs and only an inch or two of her fake phallus is sticking out of me. "
    "She flashes me that wicked grin even as her cheeks turn pink from pleasure and starts to fuck me."
    "I choke back a cry as she starts moving faster, getting rough with me now that I've adjusted. The quicker, harder motions make her breasts bounce and the black vinyl straps slap against her thighs."
    "She's moaning like she's the one being fucked, loving the bump and vibration of the toy's base tucked into the harness, rubbing up against her pelvis low enough that her clit catches some of the humming sensation."
    "I'm growing short of breath, panting heavily in time with her movements, feeling my cock throb within her grip. "
    "I groan loudly and she gives me that wicked grin again, starting to jerk me off urgently. "
    sasha.say "Cum for me!"
    show sasha strap precum
    "Insistent, she sinks her hips a little lower and aims a thrust upward to judge against the swollen gland that people call the male G-spot and I'm thrown over the edge."
    "I've never felt anything like that before; combined with her thrusts and the quick and messy way she's jerking me off is enough to make me do exactly what she told me to do."
    show sasha strap precum cum
    "Hot spurts of sticky cum fly up to splash down on my chest and stomach, making a flush of heat come to my cheeks just like Sasha's when I get her sloppy."
    "She moans loudly, grinding against me like she's using me to get herself off --which she is, as it turns out."
    show sasha strap precum orgasm
    "Sasha throws her head back with a delighted cry, tremors visibly rushing through her body."
    "I know I've cum a little more than usual, probably thanks to that nudge against my prostate gland, and I slowly lift up to look down at myself."
    "What a mess! "
    show sasha strap
    hero.say "Gonna help me clean up, Sasha?"
    "She smirks at me and pulls back, tugging the toy free of my ass, then gets on her hands and knees over me."
    sasha.say "What do you think?"
    "She asks as she dips her head, licking up a line of sticky jizz."
    hide sasha
    call sasha_sleep_date_fuck from _call_sasha_sleep_date_fuck_2
    return

label sasha_beads_play:
    $ SEXATTRIBUTES = []
    hero.say "Let's try something new tonight, Sasha."
    "I grin a little as she looks up at me with a mixture of suspicion and anticipation."
    "I walk over to the dresser and open the top drawer."
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        sasha.say "Anything you like Master..."
    else:
        sasha.say "Watcha lookin' for?"
    "Sasha comes over to stand beside me, dressed in her black underwear. She peers into the drawer, wondering if anything has caught my eye."
    "Spotting a blue orb-shape, I reach in and pull out my set of anal beads."
    hero.say "Perfect."
    if sasha.sub < 50:
        show sasha underwear angry
        sasha.say "Absolutely not!"
        "Sasha rushes out of the door."
        $ sasha.love -= 5
        $ sasha.sub -= 5
        return
    $ sasha.set_flag("anal", True)
    sasha.say "Um.. I guess we can... I take it those are for me?"
    "Sasha tilted her head in that cute curious way she has."
    hero.say "Good guess,"
    hero.say "Also, you're wearing way too many clothes."
    "Sasha chuckles and steps back, making a small show of peeling that snug bra off and tossing it aside, displaying her lovely little breasts for me, then bending down to tug the panties down to her ankles and stepping out of them."
    show sasha naked
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        "Is this better Master?"
    else:
        sasha.say "Better?"
    hero.say "Much."
    "She really is a hottie. I can't wait to make her moan."
    if not "sasha_sub_event_1" in DONE:
        sasha.say "Then you better get out of your clothes too. I'm not going to be the only naked one around here."
    "I smirk at her and start disrobing, not bothering with a little show like the one she put on."
    "I love the way she looks me over, a touch of desire gleaming in her eyes."
    "I'm already half-hard thinking of what I'll do to her... or have her do to me."
    "Grabbing one last thing out of the drawer -- a bottle of lube -- I turn toward the bed and motion Sasha to come with me."
    hero.say "Time to bend over."
    show sasha doggy waiting
    "Sasha bites her lower lip, looking with something like trepidation at the big beads I'm holding, then reluctantly bends over with her hands on the bed."
    if sasha.get_flag_value('collared') and sasha.sub > 50:
        hero.say "First, let's remind both of us who's in charge."
        show sasha doggy leashing
        "I attach the lead of the leash to her collar. For her part, Sasha closes her eyes and lets me."
        $ if not 'leash' in SEXATTRIBUTES: SEXATTRIBUTES.append('leash')
        show sasha doggy -leashing leash
        hero.say "That's a very good girl, Sasha."
        sasha.say "Thank you, Master."
    "But first, though..."
    show sasha doggy cockedback waiting
    "I can't resist giving her ass a slap that makes her gasp."
    show sasha doggy impact hurt
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        menu:
            "Keep spanking":
                "I can't help it. When I hear her gasp, I know there has to be more."
                show sasha doggy cockedback waiting
                hero.say "Who do you belong to?"
                sasha.say "Oh, God!"
                show sasha doggy blur waiting
                hero.say "Wrong answer!"
                show sasha doggy impact hurt
                "My hand impacts her ass with another loud slap, and this time she shrieks."
                show sasha doggy cockedback entered
                hero.say "Who do you belong to?"
                sasha.say "You!"
                show sasha doggy blur waiting
                hero.say "Call me Master, slave!"
                show sasha doggy impact scream
                "My hand impacts her ass with another loud slap, and this time she shrieks, but this time it's more like delight than pain."
                show sasha doggy cockedback entered
                hero.say "Last try, who do you belong to?"
                sasha.say "You, my Master! I belong to you!"
                show sasha doggy blur waiting
                hero.say "Yes, my slave! You're all mine!"
                show sasha doggy impact ahegao
                "She got it right, but I let my hand fly anyway. This one is the gentlest impact of them all, though, and her moan is pure pleasure."
                $ if not 'spanked' in SEXATTRIBUTES: SEXATTRIBUTES.append('spanked')
            "Get on with the beads":
                pass

    show sasha doggy waiting nohand
    "After opening the little bottle of lube, I start rubbing it over her tight asshole with two fingers, dipping them briefly inside now and then."
    "It gets Sasha to start breathing a little quicker, and I hear a small moan."
    "Then I put some lube on the end bead and press it to her tight pucker."
    hero.say "Ready?"
    sasha.say "Mm.. mhm.."
    "She doesn't sound entirely certain, but I know she's just a little nervous about having one of the toys she usually use on submissive men turned on her."
    show sasha doggy beads5 scream
    "Slowly I start to push, watching her dark pink asshole widen to take the girth of the bead."
    show sasha doggy beads4 entered
    "It then closes tight around the flexible bar between beads and Sasha whimpers."
    show sasha doggy beads3 entered
    "I love that sound."
    "I repeat this with all but the last bead, fascinated and aroused by her reactions and the way her asshole widens to take each bead."
    show sasha doggy beads2 entered
    "I wonder if it will stay stretched wide after I pull them out."
    show sasha doggy beads hurt
    "Once they're all in except a bit to use to pull them back out after, I guide her to stand and turn around."
    hero.say "Feels good to be stuffed full, doesn't it?"
    "Her cheeks redden and she looks down, nodding hesitantly."
    hero.say "Good. Now I want you on your hands and knees."
    "Again, she makes that whimpering sound, but complies, getting onto her hands and knees on the bed, licking her lips."
    show sasha bj beads mike nodick
    "She knows what's next, and despite her blush and embarrassment, there's a touch of eagerness in the way she looks at me."
    "Or rather, looks at my cock."
    "By now it's rock hard and I drop one hand to give it a few slow strokes purely to tease Sasha."
    show sasha bj beads mike dickout
    "I step closer and let the wide head brush against her parted lips, shuddering when her tongue darts out to flick against sensitive skin."
    "She's so good at sucking me off."
    show sasha bj mike dickin
    "Soon her mouth is stuffed with my dick; I'm thrusting my hips and pushing to the back of her throat, listening to her whimper and whine around my cock."
    "Her ass is in the air and I can get a glimpse of the bead that still sticks out, which probably explains that deep blush to her cheeks."
    "Her mouth feels so good and I know I'm close to cumming."
    "I'm panting, muscles shaky as I keep fucking her mouth, feeling her tongue caressing the sensitive underside of my cock."
    "Finally, I can't take it anymore."
    menu:
        "Cum on her face":
            "I pull back with a groan, grab my dick, and start jerking myself off hard and fast."
            show sasha bj beads mike dickout cum
            "The first spurt of cum splashes her cheeks, making her gasp, and the second rope of thick cum lands in her hair, making her blush even harder."
            "I close my eyes to savor the pleasure as I keep stroking myself to milk every last bit of jizz out to paint her pretty face with."
            "She moans and gasps through it like an eager little cum-slut."
            show sasha bj beads mike dickout cumafter
            "I slowly stop stroking myself and open my eyes to look down at Sasha's face, half-painted with my sticky seed."
            "The redness to her cheeks shows she's still feeling embarrassed, maybe even humiliated."
            if 'cumface' not in SEXATTRIBUTES:
                $ SEXATTRIBUTES.append('cumface')
        "Cum in her mouth" if hero.fitness > 25:
            "A wave of pure pleasure rolls over me, and then I explode into her mouth."
            show sasha bj beads mike dickin cum closed
            "Sasha closes her eyes and drinks it all in. First the opening spurt, and then the much bigger, second spurt that erupts, causing me to moan loudly."
            show sasha bj beads mike dickin cumafter open
            "When I pull out, she proudly displays the my cum on her tongue, before swallowing."
            pass
    if hero.fitness < 25:
        "Go clean up. I'm too tired for more; I'm going to bed."
        $ sasha.love -= 2
        $ sasha.sub -= 2
        return
    hero.say "I'm not done with you yet."
    hero.say "Turn around."
    $ sasha.sub += 2
    show sasha doggy beads2 -cumafter -cum nodick
    "She does as she's told, clearly hoping to be on the receiving end of pleasure now, since she's taken the beads and the blowjob so well."
    "But I'm not sure what I want."
    "First there's that pretty pussy, hairless and glistening with arousal."
    "But there's also that perky ass stuffed with beads, that could easily be stuffed with cock instead."
    "It's a difficult choice."
    menu:
        "Fuck her pussy with a condom" if hero.has_condom():
            $ hero.use_condom()
            call sasha_beads_fuck_pussy (condom=True)
        "Fuck her pussy raw":
            call sasha_beads_fuck_pussy (condom=False)
        "Fuck her ass":
            "She may be eager for pleasure, but I think I want to leave her squirming for the night, her tight pussy unfucked."
            show sasha doggy beads3 entered
            "I give her ass a slap, then grasp the protruding bead and slowly start to pull the toy out of that little hole, watching as her asshole expanded and contracted to allow the beads to be removed."
            show sasha doggy beads5 scream
            "It's a pretty arousing sight, but I certainly didn't need the extra arousal. Even after that heavenly blowjob, I want more."
            show sasha doggy waiting anusopen -mike
            "I consider just tossing the beads aside, but then I get a better idea."
            show sasha doggy mouthbeads nobeads waiting anusopen
            "I lean forward over her form and stuff the bottom two beads into her surprised mouth, making her give a muffled sound of protest."
            hero.say "You keep those right there until I'm done fucking you."
            hero.say "You'll need something to bite down on."
            "It's likely those words that bring realization to her eyes, realization that she's not going to get her pussy pounded like she wants."
            show sasha doggy mouthbeads waiting mike anal
            "Before realization can turn to resentment, I lean back and grind my hips to hers, caressing her nicely-rounded butt just before I guide my dick to her hole and start pushing in."
            "It's easier like this, after she had her ass stuffed with a toy."
            "Instead of a mild ache at the tightness, I get a flush of pleasure and room enough to start fucking her hard."
            "That's exactly what I start doing."
            "Gripping her hips, I begin thrusting quick and hard, making Sasha give a muffled scream of surprise around the beads that stuff her mouth."
            "It feels incredible, and looking down at Sasha's wincing, cum-stained face makes it even hotter for me."
            "I love the way she quivers, the way she blushes, and especially the way she starts to grind back against me."
            "After such a fantastic blowjob, it's not going to take long to get off again, and I want that burst of bliss."
            "Panting, I tighten my grip on her hips and start pounding her tight little ass faster, driving myself as deep as I can into that greedily clutching hole."
            "Finally, that squeeze of her asshole around my thick rod is enough to push me over the edge."
            menu:
                "Cum inside":
                    show sasha doggy mouthbeads waiting mike anal cum
                    "I slam my hips forward, making Sasha cry out again, and hold her body still with my grip on her hips."
                    "My body jerks as muscles twitch from the exciting pleasure of climax, my hot and sticky cum filling up her snug tunnel."
                    "It's longer than with the blowjob; with this load I probably could have covered her whole face."
                    show sasha doggy mouthbeads entered mike anal anusopen cumafter
                    "When the shuddering bliss subsides, I slowly pull out and watch as my cum drools from her stretched asshole."
                "Pull out":
                    show sasha doggy mouthbeads waiting mike dickout cum
                    "I take my cock out of her tight asshole, pointing it toward her lovely back."
                    "My body jerks as muscles twitch from the exciting pleasure of climax, my hot and sticky cum splattering on her skin."
                    "It's longer than with the blowjob; with this load I probably could have covered her whole face, and I cover a lot of her back."
                    show sasha doggy mouthbeads waiting dickout cumafter
                    "When the shuddering bliss subsides, I take a step back and watch the lovely mess I made of her."
            "Sasha's breathing hard too, cheeks still red, beads still held in her mouth."
            "I lean forward and gently pull them out, tossing the anal beads aside, then pull back a little to pat her on the ass."
            hero.say "That was fantastic."
            "Sasha gives me a sullen look that makes me chuckle."
            hero.say "Oh, don't pout at me, Sasha. You'll get yours in the morning. I'm sure you'll still be horny."
            "That makes her blush even deeper and I back away from the bed to tug my pants on."
            "I take her into my arms, getting ready to sleep."
            $ sasha.sub += 5
    call sasha_sleep_date_fuck from _call_sasha_sleep_date_fuck
    return

label sasha_beads_fuck_pussy(condom=False):
    if condom and not 'condom' in SEXATTRIBUTES:
        $ SEXATTRIBUTES.append('condom')
    "My cock is still a little slippery with cum, but it doesn't look like she'll need the extra lube."
    show sasha doggy beads2 entered mike pussy
    "I press the broad head to her little hole and push forward, groaning as her pussy clings so tight to my still-sensitive dick."
    "It makes my muscles quiver even more; I know it won't take too long to cum."
    "Looking down at her, seeing her jizz-splashed face, arouses me further."
    "I give her ass a slap, then grab her hips with a tight grip that makes her whimper with anticipation."
    "I don't leave her anticipating long."
    "Almost immediately, I push her hips forward, then pull them back forcefully, using her body like a sex toy for a moment."
    "I stand still, pushing and pulling at her hips, making her ride my cock."
    "The blush on her face beneath the white lines of cum makes the experience so much hotter; I'll have to do that to her more often."
    "The slap of our bodies meeting gets louder as I begin to thrust my hips forward when pulling her back toward me."
    "Her moans get louder and shudders ripple down her spine; she might be close too."
    "Much as I don't want to, I hold back, intending to let her climax first."
    "She deserves it; she did such a good job sucking me off."
    "She tosses her head back and cries out when orgasm hits, her body trembling, her hips bucking back against mine as she grinds hard, trying to get my cock as deep as she can."
    "As she climaxes, I grab the bead that juts out of her ass and start pulling, dragging the beads out slowly through her orgasm."
    show sasha doggy beads2 ahegao mike pussy
    "It makes her cry out more, feeling such intense sensation in both holes."
    "Now it's more than I can take."
    menu:
        "Pull out":
            "At the very last minute, I pull my dick out."
            show sasha doggy mike cum dickout
            "I groan again as the cum explodes from my cock, letting Sasha know how thoroughly I enjoyed her beautiful pussy."
            if condom:
                "The condom is almost a disappointment, catching all of the cum, but it doesn't matter. The orgasm itself, not my first of the night, is absolutely incredible."
            else:
                show sasha doggy mike cumafter dickout waiting
                "My load explodes out of my cock, covering her back and ass with globs of the sticky liquid."
            "I just stand there for a moment, admiring my handiwork."
        "Cum inside":
            "I thrust forward, holding her hard against me as my cock twitches deep inside her."
            show sasha doggy mike pussy cum scream
            if condom:
                $ sasha.impregnate(counter=False)
                "I groan loudly with every spurt of hot sticky cum that I fill her pussy with, panting, until my climax finally ends."
                show sasha doggy mike pussy cumafter waiting
                "I pull out, looking down to see some of my cum dribble out of her pussy and down the inside of one thigh."
            else:
                "I groan loadly and fill the condom with spurt after spurt of hot sticky cum. I stand there, panting and squeezing cum out of my cock until my climax finally ends."
                show sasha doggy mike dickout cum entered
                "When I pull out, I can see just how much of the condom I have filled."

    "Arousal slowly fading, I pull her down on the bed with me to spoon together, trying to catch my breath."
    hide sasha
    show sasha naked
    sasha.say "Wow..."
    hero.say "Glad you liked it,"
    "I toss the beads aside and cuddle close, deciding we'll sleep together tonight."
    $ sasha.love += 1
    $ sasha.sub += 1
    return

label sasha_normal_fuck:
    $ SEXATTRIBUTES = []
    show sasha foreplay underwear boxer
    "She reaches out and caresses my cock through the thin fabric of my boxers, nudging at the parting of the fly so the head of my cock slips free."
    sasha.say "Very happy."
    "She strokes her palm over the rounded tip of my dick, encouraging a little drop of pre to appear at the slit."
    hero.say "Are you happy too?"
    "I smirk at her and arch a brow, reaching out to slip one hand between her thighs."
    "Her grin widens, so sensual, and she steps forward a little to encourage the touch."
    "I'm delighted to find out I was right; no underwear bars the way between my hand and her flesh."
    "The folds of her pussy are so soft and smooth, no hair in the way either, and I dip one fingertip into her slit to find her already a little wet."
    hero.say "Seems like it."
    sasha.say "Mm. I've been thinking about this all day."
    "she steps in so our bodies just barely touch."
    "She lifts up onto her toes and presses her lips to mine, parting them with the tip of her tongue for a slow and erotic kiss that promises so much more."
    "My arousal sky-rockets; between her kiss and the stroke of her hand as her fingers curl around my shaft, I'm so hard I ache."
    "I'm ready to fuck her right now, but the anticipation will make the pleasure even better."
    "Besides, I suspect she's the type to enjoy some thorough foreplay."
    "I put one hand on the curve of her hip to keep her close while the other stays between her thighs."
    "One fingertip finds the swollen nub of her clit and I start stroking the sensitive flesh in slow circles, drawing a soft moan from her against my lips."
    "I let my tongue seek out hers to deepen the kiss while teasing her with light flicks of my fingertip."
    "I can tell by the way she shivers how much she likes it."
    "She's eager; Sasha stops toying with my half-exposed cock, instead using her hands to carefully push my boxers down, letting them fall to the floor."
    hide sasha foreplay
    show sasha foreplay underwear
    "I step out of them and kick them absently off to the side, too distracted by what she's doing to give the clothing much thought."
    "Now that I'm naked, she gets busier with her hands. One dips down to cup my balls, kneading them so gently within her palm; the sensation sends tingles through the flesh she's touching and makes me sigh between our kisses."
    "Her other hand wraps around the base of my cock and gives the hard flesh a squeeze firm enough to be just shy of uncomfortable."
    "It makes me grown against her lips, and she responds with a sensual chuckle in her throat, clearly enjoying teasing me."
    "Standing against one another, we both take our time in teasing each other."
    "The anticipation is building almost too high to keep ignoring, but what she's doing feels so good."
    "Sasha grips my cock and starts stroking slowly, twisting her hand from one side to the other for added friction, caressing the pad of her thumb over the tip of my cock each time her stroking leads up to the plump head."
    show sasha foreplay underwear up
    "I'm starting to breathe harder and so is she, too fast to keep up the kissing."
    "I rest my forehead against hers, looking intently into dark eyes that are filled with lust, watching the pink flush of arousal stain her cheeks."
    "My hand pushes further between her thighs and I let two fingertips rub against her opening."
    "It's already very slick, making it easy to slip the tips of the digits inside her, making her tilt her head back with a moan."
    "I start to slowly finger-fuck her, wanting her as lusty as I am, imagining how incredible it will feel when I replace my thrusting fingers with my cock."
    "I want her naked."
    "With my free hand, I push the robe off her shoulders and let it fall to the floor, then tug the nightie off over her head and toss it aside."
    show sasha foreplay naked
    "She's so gorgeous, with those small perky breasts, that trim figure, and long, perfectly shaped legs."
    "Each steady movement of my hand makes her whimper and her lovely eyes flutter shut as her breath quickens."
    "She starts stroking my dick a little faster, squeezing at the head, gliding her hand up and down my shaft."
    if sasha.sub >=25:
        "Then she leans down, putting her hands on my knees."
        "She pushes them apart and then kneels between my legs; now I know what's coming."
        "I can feel my cock swell almost to full size in anticipation."
        if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
            sasha.say "Can I suck your cock Master?"
            sasha.say "Please..."
            hero.say "You can little slave."
        else:
            sasha.say "You're going to like the next part..."
        show sasha bj mike
        "Sasha takes a hair tie off her wrist and uses it to bind back that pretty black hair, then ducks her head to flick her tongue over the slit at the tip of my dick."
        "I'm helpless to stop a little groan, and my fingers curl into my bedspread."
        if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
            hero.say "Not bad."
            sasha.say "Thank you Master."
        else:
            hero.say "Nn.. good present."
            sasha.say "Thought you'd like it."
        "She whispers back, letting her warm breath caress over the head of my cock."
        "It makes me shiver and shift my hips, eager for more."
        "Apparently, Sasha is just eager to draw this out and torment me."
        "She curls a finger beneath my cock and lifts it upward, then tucks her head in further to start lapping lightly at my balls."
        "That's not an experience I get very often, and I lean back, parting my thighs further to give her all the room she could want."
        "She chuckles softly and keeps licking."
        "I'm trembling by the time she's done sucking and licking at my balls, which I can feel throbbing."
        "I'm marveling over how much she's managed to work me up while barely touching my dick at all."
        "Breathing hard, I squirm as she lifts her head and pulls her hand away, letting my stiff rod drop a little until the head is pointed at her face."
        "Part of me wishes I was ready to cum right now; it would be incredibly hot to paint her cheeks and lips with my jizz, but she doesn't have me worked up quite enough for that."
        show sasha bj mike
        "Just as well, because a moment later, she's leaned in and taken the head of my cock into her mouth."
        "It's so warm and wet, and I can feel her tongue rubbing lightly at the lines and ridges just beneath the head along the underside; those spots are so sensitive!"
        "If she keeps that up, she might wind up with a mouthful of spunk before she's ready for it, and it seems she knows that too, for she stops and simply presses the flat of her tongue up against the underside."
        show sasha bj mike dickin
        "Instead of further teasing, she starts sucking, and she sucks hard!"
        "I hadn't thought my dick could get any harder, but Sasha proves me wrong."
        "I ache, wanting more, wanting her to bob her head on my dick, but for now I hold still and let her go at her own pace."
        "It's clear she wants to torment me anyway."
        "And she's very good at tormenting me."
        "Her fingertips drift up and down in a feathery caress along the underside of my shaft, sending tingles through my body and making me squirm."
        "It's almost embarrassing how much reaction she's getting out of me already. I want more."
        if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
            sasha.say "Please fuck me Master."
        else:
            sasha.say "Nn.. bed,"
        "Sasha steps back and releases her grip on me so suddenly I let out a protesting sigh."
        "But when she walks over to the bed, I follow, stiff rod swaying with my steps. She gives me a heated stare."
    if hero.has_condom():
        menu:
            "Use a condom":
                $ CONDOM = True
                $ hero.use_condom()
                if not 'condom' in SEXATTRIBUTES:
                    $ SEXATTRIBUTES.append('condom')
            "Do it raw":
                $ CONDOM = False
    else:
        $ CONDOM = False
    sasha.say "How do you want me?"
    menu:
        "Missionary":
            $ p = "missionary"
            hero.say "On your back,"
            "I want to be able to see the desire and pleasure in her eyes while I'm fucking her."
            show sasha missionary noman
            "Sasha gets onto the bed, leaning back and spreading her legs, knees bent."
            "She smiles seductively and lets one hand drift between her thighs, idly rubbing her clit while waiting for me."
            "The view is incredible."
            show sasha missionary man nodick
            "I crawl up from the foot of the bed until my knees are between her parted thighs."
            "Grinning wickedly at her, I reach back and take her ankles, lifting them to my shoulders; Sasha's flexible enough to enjoy this."
            "I lean forward, pushing her legs back and elevating her hips in the process, letting my cock rub against her pussy while I steady my hands on the bed to either side of her shoulders."
            show sasha missionary man out
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "Please, fuck me hard Master."
            else:
                sasha.say "Fuck me hard."
            "Her words ignites higher passions and makes me groan. I certainly intend to."
            show sasha missionary man fuck
            "This position makes her so tight as I push in, and the angle forces the head of my cock to rub firmly at the front of her walls, right along her G-spot."
            show sasha missionary man fuck
            "At the first brush to that tender patch of flesh, she arches with a moan, then flops back to lay flat, her hands moving to grip my wrists as though she's bracing herself."
            "Once I'm buried deep in her clingy cunt, I hold still for a minute so she has time to adjust to her walls being stretched for me."
            "It feels incredible, how tight her pussy grips my shaft, and I savor it during those slow-passing moments."
            "Lust darkens her eyes as she stares hotly up at me, clearly growing impatient."
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "I beg you Master..."
            else:
                sasha.say "Fuck me..."
        "Standing" if hero.fitness >= 50:
            $ p = "stand"
            hero.say "Come here,"
            "I lead Sasha over to the dresser."
            hero.say "Bend over."
            "She blinks, then grins when she realizes why I've chosen this spot."
            "We can watch each other in the mirror while I fuck her; it will be incredibly hot."
            "Sasha bends forward and braces her hands on the edge of the dresser, looking at me expectantly in the reflection."
            "Tense with anticipation, I put my hands on my hips and rub my cock against her slick pussy until the head nudges at her entrance."
            "With a low groan that Sasha echoes, I slowly push in until my rod is buried to the hilt."
            show sasha stand dickin open
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "Do whatever you want Master."
            else:
                sasha.say "Nn.. fuck me hard, [hero.name]."
            "Lust is glowing in her eyes. She looks so incredibly sexy in the mirror."
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                hero.say "That's what I intend to so little slave."
            else:
                hero.say "As hard as you want."
            "Putting action to words, I pull halfway out of the heated grip of her cunt, then plunge back in hard enough to make those pretty little tits sway."
            "Being able to watch her reaction, watch her body in the mirror is so much hotter than I thought it would be."
            "She moans for me as I start thrusting, pulling only partly out before driving hard back inside, not wanting to be free of the snug cling of her pussy for long."
            "It feels so good, hot and wet walls squeezing my shaft."
            "Her expression is one of total desire, full lips parted, dark eyes half-closed and gleaming with lust, a pink flush spreading over her cheeks."
            "Each thrust makes higher pitched moans come from her throat, getting louder and louder every time."
            "A few groans of my own join her sounds, along with the slap of flesh on flesh each time I shove deep."
            "I can feel wetness on my balls when they smack against her pussy and I can't help imagining how the insides of her thighs must glisten with how soaked she is."
            "I lose myself in the hard and fast rhythm; we watch each other in the mirror, getting more turned on by being able to see how turned on the other is."
            "Using the mirror was a perfect idea."
            show sasha stand dickin closed blush
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "Can I cum?"
                sasha.say "Please Master, I am so close..."
                hero.say "You have been a good little slave, you may enjoy yourself now."
                sasha.say "Thank you master."
            else:
                sasha.say "Harder!"
                sasha.say "I'm so close..."
                "I'm happy to oblige, right on the edge myself."
            "Her head lowers and I frown; I want to see that pretty face painted with bliss."
            "One hand leaves the curve of her hip, moving to grip her hair initially, but my fingers find her neck first."
            "Grinning wickedly, I grip it instead."
            "She cries out, partly in surprise and partly in pleasure, the sound cutting off as my fingers squeezes at her throat."
            "Sasha lifts her head, bowing her back and raising her shoulders, pushing at the edge of the dresser."
            "Shock widens her eyes, but they glitter with intense desire; it seems she likes being choked a little."
            "That combined with the harder thrusts proves enough to send her over the edge."
            show sasha stand open dickin cum blush
            "I gasp as I feel the hot wash of nectar splash against my balls and I shove deep, wanting to feel every quiver and clutch of her orgasm."
        "Doggy" if sasha.sub >= 25:
            $ p = "doggy"
            "Much as I might enjoy drawing it out longer, at this moment there's nothing I want more than to pound her little pussy until she screams."
            "So I give her a shove between the shoulder-blades, sending her to her hands and knees."
            show sasha doggy waiting
            "I kneel upright, smack her ass with both hands, then grab her hips."
            "She yelps, the sound turning to a low moan, and she grinds back against me, getting my pubic hair moist with her arousal."
            "After all this anticipation, it feels beyond amazing to slowly sink my dick into her clingy cunt."
            show sasha doggy mike pussy entered
            "Feeling her walls close tight around her shaft draws a groan from me and I push until I'm buried completely inside my new pet."
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                hero.say "Mm... Such a tight little slave."
            else:
                hero.say "Mm... my good girl is so tight."
            "Her striped ass jiggles with each impact as I shove in as deep as I can, the impact of flesh on flesh making a slapping sound in the small room."
            "She's my pet now."
            "I can do what I want with her, and by the way she's crying out, it won't be long before she cums."
            if sasha.get_flag_value("anal"):
                "Shuddering, I pull out of her abruptly enough to make her whine in protest, but I'm ready to push back in."
                "Just not into her pussy."
                "I lift up a little, letting the soaked and slippery head of my cock glide up until it's pressed against the tight ring of her asshole."
                show sasha doggy mike anal hurt
                "Without giving her time to prepare, I start pushing in."
                "It's so tight it begins to ache, the way that tunnel grips my cock."
                "She cries out in pain but apparently she likes it despite her sounds, for she pushes back against me cautiously, taking my thick rod deeper into her ass."
                "When my cock is as deep in as it can go, I hold still for several moments, letting my little fuck-doll adjust."
                "She's panting for breath, each exhale a whimper, shivers dancing down her spine."
                "She's been so good, I know I should make her cum too, considering how close to the edge I am."
                "I slide one hand around between her thighs, pinching her throbbing clit between two fingers and wiggling those digits from side to side."
                show sasha doggy mike anal entered
                "It's apparently a way she really loves to be touched, for Sasha cries out and grinds down hard against me before doing as ordered."
                "I keep rubbing her clit to make her cum for a moment, then slide my hand further between her thighs and start fingering that slippery little cunt."
                "She shudders hard and I cup one bouncing tit with my other hand, giving the nipple a cruel pinch."
                hero.say "I know you're close, pet."
                hero.say "Cum for me."
                hero.say "Soak my hand, show me how much you love it,"
                show sasha doggy mike anal scream
                "Sasha probably didn't really need the encouragement; it's only a few more bounces before she throws her head back and lets out a yell of bliss."
                "As ordered, she really does soak my hand, hot nectar squirting against my palm."
                "I had no idea she could cum so hard and it almost sends me over the edge."
                "Quickly, I pull my hands back from her body and my dick out of her ass, groaning."
                show sasha doggy mike pussy entered
                "I don't even give her the time to catch her breath before plunging back into her pussy."
    menu:
        "Keep fucking her":
            if p == "missionary":
                show sasha missionary man fuck speed
            "I can't hold back any longer anyway; it feels too good."
            "I start rocking my hips at a quick pace, keeping the angle of her lower body tilted so that each thrust teases over her G-spot."
            "With that kind of attention, she's gasping for breath and squirming soon, her lips parted and a flush across her cheeks."
            "I love the lusty look in her eyes."
            "I don't bother to vary my pace or position."
            "It's clear by her whimpers and gasps that I'm doing just what she wants, and it feels wonderful to me too."
            "Her cunt is so tight and I can feel it getting more and more slippery the longer I fuck her."
            "The smell of sex rises in the air, arousing both of us even further."
            "I can tell by the way she trembles and how tight she holds onto my wrists that she's close."
            "Groaning, right on the edge myself, I shorten my thrusts and fuck her harder, entranced by the way her small breasts jiggle and bounce with each impact."
            "Finally, I can't hold it off any more."
            "Just as I shove deep, my cock starting to throb, she cries out and arches to grind against me."
            $ choking = False
            if p == "missionary" and hero.fitness >= 25:
                menu:
                    "Choke her":
                        "On an instinctive whim, I move one hand to grasp her neck, strangling her throat."
                        "Her eyes get huge and she bucks hard against me while she struggles for breath, lost in sudden euphoria that draws her climax out longer."
                        "She gets my pubic hair soaked and I can feel her hot nectar dripping down my balls."
                        if not CONDOM:
                            show sasha missionary man fuck cumshot
                            "Thrilled to have found something she likes so much, I grind deep into her as I cum, spurting jets of hot sticky seed deep into her squeezing tunnel."
                        else:
                            "Thrilled to have found something she likes so much, I grind deep into her as I cum."
                        $ sasha.sub += 1
                        $ choking = True
                    "Keep going":
                        pass
            if p == "missionary":
                show sasha missionary man sashacum fuck cumshot
                if CONDOM:
                    "It's a much harder orgasm than I expected; soon the condom is completely full of my jizz."
                else:
                    "It's a much harder orgasm than I expected; soon my jizz is dripping from her filled pussy."
                "It's all I can do not to collapse on top of her."
                if choking:
                    "I let go of her neck and she gasps for breath and lets out a low whimper of intense pleasure."
                if not CONDOM:
                    $ sasha.impregnate(counter=False)
            else:
                menu:
                    "Cum inside":
                        if CONDOM:
                            "It's a much harder orgasm than I expected; soon the condom is completely full of my jizz."
                        else:
                            "It's a much harder orgasm than I expected; soon my jizz is dripping from her filled pussy."
                            $ sasha.impregnate(counter=False)
                        if p == 'doggy':
                            show sasha doggy mike pussy cum
                        else:
                            show sasha stand dickin cum
                    "Pull out":
                        "At the very last minute I pull my throbbing cock out of her pussy. I barely have time to clear her vulva before I explode."
                        if p == 'doggy':
                            show sasha doggy mike dickout cum
                        else:
                            show sasha stand dickout cum
                        if CONDOM:
                            "The condom fills with my sticky fluid."
                        else:
                            "My jizz spurts several times, covering her beautiful ass with hot, sticky semen."
                            if p == 'doggy':
                                show sasha doggy cumafter dickout
                            else:
                                show sasha stand cumafter dickout

            "As my climax ends and hers dies down to shudders, I roll off of her onto my back."
            "Several moments of silence stretch as we both struggle to catch our breath."
            hide expression "sasha "+p
        "Make her suck you off" if sasha.sub >= 25:
            show sasha bj -mike
            hero.say "On your knees."
            "I need more. I want to feel her bobbing on my dick."
            "Groaning, I lean back a little more and brace on one hand."
            "The other hand moves to grip her hair so I can hold her head still."
            show sasha bj mike dickin
            "I don't want to force too much, so I start by just giving little bucks between her lips, pushing my cock in until her mouth is full."
            "By the gleam in her eyes, Sasha looks like she really enjoys having a mouth full of dick!"
            "Sensing that the teasing portion of the evening is done, she settles back to sit on her heels, one hand lifting to cup my balls."
            "After how she'd sucked and licked those full, rounded orbs, having her knead at them and roll them across her palm is nearly bliss."
            "Her other hand comes up and wraps around the base of my cock."
            "For long moments as I give those small, careful thrusts, she grips and squeezes in time with my movements."
            "Then she starts stroking my shaft so her index and thumb meet her lips when I push into her mouth."
            "The tandem sensations are incredible! This girl really knows how to give head."
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                hero.say "Take me deep slave!"
                "I command her, knowing she will obey."
            else:
                hero.say "Hnn... I wanna put my cock in your throat."
                "I murmur without thinking; when her gaze lifts to meet my eyes, I flush a little, and I'm not sure if it's shyness regarding what I blurted out, or the rapidly building pleasure."
            "She gives my balls a little squeeze, then lifts her head, letting my cock slide out of her mouth for a moment, though the tip rubs against her lower lip still."
            show sasha bj mike
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "Yes Master."
            else:
                sasha.say "Don't worry, we're getting there."
                "She smirks and tosses me a wink."
                sasha.say "Don't push it; this is my present to give."
                "Reluctantly, I take my hand away from her hair and place it on the bed again, leaning back a little and looking down my body at her."
            "She grins that wicked grin of hers and slowly takes the head of my cock into her mouth without breaking eye contact."
            "There's just something so sexy about that!"
            show sasha bj mike dickin
            "She continues to meet my gaze as she starts to bob on my dick, and Sasha looks incredibly hot doing so."
            "It turns me on so much, watching her watching me as she's got a mouthful of my cock."
            "I want to thrust, but I hold back, letting her go at her own pace."
            "After a moment, she starts bobbing a little further down, until I can feel the tip of my rod brushing the back of her throat."
            "Her eyes squeeze shut for a second as she holds herself there, then pulls back and resumes sucking, working her way up to more."
            "Meanwhile, her hands stay busy."
            "The way she fondles my balls feels great, but it's her other hand that has me a little distracted."
            "She's still stroking me firmly, and she's pressing her thumb hard against the underside of my cock, knowing that's the most sensitive zone she could be touching aside from the head."
            "It's bringing me closer and closer to climax."
            hero.say "Don't s-stop..."
            "I groan down to her, and her eyes light up with something like joy; she really wants me ready to cum!"
            "I wonder if she'll let me cum on her face; I really want to see those pretty cheeks and lips coated with my seed, but I'm torn, since cumming down her throat would be just as incredible."
            "It seems like she's going for that second option, too."
            "She pushes her head down lower, and after a brief moment of struggle, she takes the head of my cock into the incredibly tight grip of her throat."
            hero.say "Fuck! Gonna make me cum!"
            "I start panting, right on the edge, and she knows it."
            "Sasha takes her hand away from my shaft, disappointing me only briefly, since it seems she just wanted it out of her way."
            "Now she starts bobbing on my dick, taking my rod into her throat for about half the length."
            "She pauses each time she's at the lowest point and stares up at me while she swallows, making her throat grip my cock even tighter than her hand had, and squeezing downward from shaft to head."
            "It's beyond amazing."
            hero.say "Almost there."
            "I warn her, not wanting Sasha to be surprised."
            "She doesn't slow down, doesn't even hesitate!"
            "Still staring up at me, she keeps bobbing quickly on my dick, making wet and sloppy sounds as she moves faster, clearly eager for my cum."
            "I can't help myself."
            menu:
                "Cum in her mouth":
                    "I grip the back of her head with one hand as tremors start to rock through me, and I push deeper; she makes no protest though her eyes tear up a bit."
                    show sasha bj cum mike dickin
                    "Groaning, I gasp for breath as my cock twitches and throbs, forcing her to swallow quickly as pleasure sends spurts of hot cum straight down her throat."
                    show sasha bj mike dickin cumafter open
                    "It takes several moments for my climax to pass, and when it does, I drop back to the bed, panting, trying to catch my breath."
                    "Dimly, I feel Sasha licking at my cock lightly before she pulls away and stands."
                "Cum on her face" if sasha.sub >= 50:
                    "My breath stays quick and shallow; I can feel the heat and tension low on my stomach that lets me know climax is close."
                    "I love the way she's sucking my cock, but I want something more than just cumming in her mouth, no matter how eager she seems."
                    show sasha bj mike dickout cum
                    "Grabbing her hair, I pull her off my dick and start jerking off with my free hand; it doesn't take long for the first ropes of cum to splash on her pretty face, one spurt landing in her jet black hair."
                    "I shudder, back arching as the climax rolls through me, making sure to cover my little lover's face with the seed she wants so badly, then drop back onto the bed, panting."
                    show sasha bj mike dickout cumafter
                    "She stands, a little shaky, and looks down at me while wiping some of the jizz off her face, then licking it from her fingers, knowing how much of a turn-on that view will be to me."
                    $ sasha.sub += 2
            if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
                sasha.say "Thank you Master."
            "I let out a pleasure-filled sigh and look up at her with half-lidded eyes."
    hide sasha
    call sasha_sleep_date_fuck from _call_sasha_sleep_date_fuck_1
    return

label sasha_sleep_date_fuck:
    scene bg bedroom1
    show sasha naked
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        sasha.say "Can I sleep here Master?"
    else:
        sasha.say "Mm.. want me to spend the night?"
    menu:
        "No":
            hero.say "No, you shouldn't; I have to get up early tomorrow,"
            "I say as I pull out of her slippery pussy with a soft groan."
            "The sex was beyond incredible."
            "Frowning a little, Sasha straightens and shrugs, then goes to collect her robe from where she'd let it fall earlier."
            sasha.say "Alright. Sleep well."
            "She then heads up the stairs."
            $ sasha.love -= 3
        "Yes":
            hero.say "Absolutely."
            "I say, my voice a little shaky."
            "I pull out with a reluctant sigh, then turn toward the bed."
            "We curl up spooning together in bed, drifting toward sleep."
            sasha.say "Sweet dreams."
            hero.say "You too."
            $ sasha.love += 3
    call sleep from _call_sleep_7
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
