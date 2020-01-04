init python:

    Event(**{
        "name":"audrey_help_at_work",
        "girls_conditions": {"audrey":{"room":"office"}},
        "label": ["audrey_help_at_work"],
        "duration": 0,
        "game_conditions": {"room":["office","personal"], "chances":10, "activity":["work","workhard","work_personal","workhard_personal"]},
        "do_once": False,
        "once_week": True
        })

    Event(**{
        "name":"audrey_talk_breakup",
        "max_girls": 1,
        "label": ["audrey_talk_breakup"],
        "duration": 0,
        "do_once": True,
        "girls_conditions": {"audrey":{"min_love":20, "active":True,}},
        "game_conditions": {"chances":"love_audrey_5", "activity":"interact", "flag_female":0}
        })

    Event(**{
        "name": "audrey_gay_mistake",
        "label": ["audrey_gay_mistake"],
        "girls_conditions": {"audrey":{"max_love":30,"room":"office"}},
        "game_conditions": {"min_charm":20,"room":["office","personal"], "chances":10, "activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "do_once": True
        })

    Event(**{
        "name": "audrey_event_01",
        "label": ["audrey_event_01"],
        "game_conditions": {"min_charm":20,"min_fitness":20,"room":["pub"], "flag_female":0},
        "girls_conditions": {"audrey":{"present":True}},
        "priority": 500,
        "do_once": True
        })

    Event(**{
        "name": "audrey_event_02",
        "label": ["audrey_event_02"],
        "duration": 1,
        "game_conditions":{"room":["office"], "flag_female":0},
        "girls_conditions": {"audrey":{"min_love":40,"present":True, "flageq_story":1}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "audrey_event_03",
        "label": ["audrey_event_03"],
        "duration": 1,
        "game_conditions":{"room":["gym"], "flag_female":0},
        "girls_conditions": {"audrey":{"min_love":60,"present":True, "flageq_story":2}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "audrey_event_04",
        "label": ["audrey_event_04"],
        "duration": 1,
        "game_conditions":{"days":"6","hours":(12,16),"flag_dateinprogress":0, "seasons":"01", "flag_female":0},
        "girls_conditions": {"audrey":{"min_love":80, "flageq_story":3}},
        "priority": 500,
        "clothes":"swimsuit",
        "do_once":True,
        "quit": True,
        
        })

    Event(**{
        "name": "audrey_event_05",
        "label": ["audrey_event_05"],
        "duration": 0,
        "game_conditions":{"days":"5","hours":(19,19),"flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"audrey":{"min_love":100, "flageq_story":4}},
        "priority": 500,
        "clothes":"date",
        "do_once":False,
        "quit": True,
        
        })

    Event(**{
        "name": "audrey_event_06",
        "label": ["audrey_event_06"],
        "girls_conditions": {"audrey":{"min_love":100,"room":"office", "flageq_story":5}},
        "game_conditions": {"min_charm":50,"room":["office","personal"], "activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "do_once": True
        })

    Event(**{
        "name": "audrey_event_07",
        "label": ["audrey_event_07"],
        "girls_conditions": {"audrey":{"min_love":120,"room":"office", "flageq_story":6}},
        "game_conditions": {"min_charm":60,"room":["office","personal"], "activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0},
        "do_once": True
        })

    Event(**{
        "name": "audrey_spanking_start",
        "label": ["audrey_spanking_start"],
        "girls_conditions": {"audrey":{"min_love":90,"min_sub":25, "room":"office"}},
        "game_conditions": {"room":["office","personal"], "activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0, "done":"shiori_scold_3"},
        "do_once": True
        })

    Event(**{
        "name": "audrey_spanking_1",
        "label": ["audrey_spanking_1"],
        "girls_conditions": {"audrey":{"min_love":110, "min_sub":50 ,"room":"office", 'flag_spankingdelay:':0}},
        "game_conditions": {"room":["office","personal"], "activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0, "done":"audrey_spanking_start"},
        "do_once": True
        })

    Event(**{
        "name": "audrey_spanking_2",
        "label": ["audrey_spanking_2"],
        "girls_conditions": {"audrey":{"min_love":130, "min_sub":75 ,"room":"office", 'flag_spankingdelay:':0}},
        "game_conditions": {"room":["office","personal"], "activity":["work","workhard","work_personal","workhard_personal"], "flag_female":0, "done":"audrey_spanking_1"},
        "do_once": True
        })

    Event(**{
        "name":"audrey_init",
        "label": ["audrey_init"],
        "girls_conditions": {"audrey":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "audrey_give_christmas",
        "label": ["audrey_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas"},
        "girls_conditions": {"audrey":{"min_love":50,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "audrey_give_birthday",
        "label": ["audrey_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday"},
        "girls_conditions": {"audrey":{"min_love":40,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "audrey_give_valentine",
        "label": ["audrey_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine"},
        "girls_conditions": {"audrey":{"min_love":100,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "audrey_kiss_me",
        "label": ["audrey_kiss_me"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"audrey":{"min_love":150,"present":True, "valid":True}},
        "game_conditions":{"flag_female":0, "chances":20},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "audrey_investigation_callback",
        "label": ["audrey_investigation_callback"],
        "game_conditions": {"hours":(12,18)},
        "girls_conditions": {"audrey":{"countermin_investigationcallback":2, "present": False}},
        "do_once": True
        })

    Event(**{
        "name": "audrey_pregnant_flag",
        "label": ["audrey_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"audrey":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

label audrey_pregnant_flag:
    $ audrey.set_flag("pregnant",1,mod="+")
    return

label audrey_spanking_2:
    $ audrey.set_flag("spankingdelay",True,3)
    "I don't really have a dedicated secretary working under me at my current pay grade, and I'm in the habit of writing letters, emails and memos myself whenever I need them."
    "But I do on occasion find myself inaudundated to the point where I have to ask one of the people that I'm responsible for in the office to take dictation and write up my words for me."
    "Normally I'd ask Shiori to handle it, as she's insanely eager to please and terrified of screwing up even the smallest, most insignificant of tasks."
    "But on one particular occasion she was nowhere to be seen and I was forced to resort to the desperate measure of having Audrey do it instead."
    "Everything seemed to go off without a hitch, until I look back over the file the next day and just so happen to glance at the copy of the letter inside of it."
    hero.say "AUDREY - get in my office...NOW!"
    show audrey
    "Despite the fact that I'm yelling at the top of my voice and visibly annoyed, Audrey takes her own sweet time sauntering into my office."
    "She has a look of sublime innocence on her face that only serves to make me become instantly more irate with her."
    "There's no way that she can pretend to be ignorant of what's making me angry, or of what she's gone and done."
    audrey.say "Yes, Mr [hero.family_name] - what can I do for you?"
    "I hold up the copy of the offending letter, doing so with a finger and thumb, as though it were smeared in something unmentionable."
    hero.say "Audrey, please tell me that you didn't let this go out."
    "She cocks her head on one side and leans in a little closer to see just what I'm referring to, still playing the innocent party."
    audrey.say "Isn't that the letter you had me type up yesterday?"
    audrey.say "I was sure to see that it went out in last night's mail, just like you asked me to."
    "Seeing that she intends to keep on playing this game until someone blinks, I shake my head in frustration."
    hero.say "You do understand, don't you, Audrey, how dictating a letter works?"
    hero.say "You're not a court reporter, taking it all down word for word!"
    hero.say "For example, I don't think the client will be too impressed with this part here."
    "I point to a particularly offensive passage somewhere in the middle of the letter."
    hero.say "Specifically this one where you chose to quote me as saying - 'whatever, give the sleazy old creep some bullshit excuse'!"
    "Audrey cocks her head, doing her best approximation of a puzzled expression."
    audrey.say "Oops...I guess I must have been daydreaming when they went through that one back in clerical slave school!"
    "At that, I have to bite my tongue to keep from saying something that I might later regret."
    "Not only has she deliberately put me in a compromising position, she's now throwing it in my face for asking her to take down the letter in the first place!"
    "I find that all I can do is close my eyes and force myself to count slowly to ten."
    "But when I open my eyes, Audrey is still standing there, that same look of mock-innocence barely concealing the smugness."
    "So I bite my lip and close my eyes again, counting to twenty this time."
    "When I open my eyes for the second time, my efforts to control myself have clearly done nothing but amuse Audrey."
    "She's smiling openly now, even beginning to get the giggles at how mad she's managed to make me in so short a space of time."
    "I should be able to rise above all of this petty shit, just give her a bollocking and then report the matter to HR."
    "The worst part of it is that I know why she's doing this to me, what she wants to happen next."
    "And I also know that I'm getting ever closer to giving in and letting her have it too."
    "Audrey, of course, knows all about the dilemma that I'm currently wrestling with, can read it in my expression."
    "She keeps the smile on her face as she walks slowly around the side of my desk, holding my eye the whole time."
    "As she gets closer, I instinctively push my chair back in order to keep some distance between us."
    "But that only means that I collide with the back wall of my office as she keeps coming on."
    "Seeing that I'm out from under the desk, Audrey leans in closer and actually lowers herself until she's over my lap."
    hide audrey
    show spank audrey
    "And then she lays herself across my thighs, looking back over her shoulder with that same feigned innocence as she does so."
    audrey.say "Well, it sounds like I've been a very bad girl."
    audrey.say "So you're going to have to punish me...aren't you?"
    "I take a deep breath, already unable to concentrate on anything other than the weight of her across my lap."
    "If I'd been able to, then I should have told her to stay on her own side of the desk or else get he hell of my lap well before now."
    "Resigned to the fact that there's no way out of this, I begin to raise my hand to strike the first blow..."
    "But then I pause, considering the fact that I've already spanked Audrey in the past."
    "Surely if I'm going to mete out the same punishment again, I need to step things up a notch?"
    show spank audrey worktop
    "Lifting Audrey's skirt to reveal her buttocks, I quickly follow this action by grabbing the waistband of her panties and yanking them down as well."
    "For the first time since she stepped into my office, I hear a squeal that tells me events have taken a turn which Audrey had not anticipated."
    "This only serves to make me all the more intent on following through with the notion, and I give her bare ass a swift slap for the sake of getting things started."
    "The first couple of slaps are relatively gentle, just a taster of what's to come."
    show spank audrey worktop marks
    "But all the same, the cheeks on Audrey's face are soon as red as those of her backside."
    "As I step up the intensity of the blows, I hear her begin to yelp over the sound of my hand making contact with her buttocks."
    "Audrey wriggles and squirms relentlessly as I continue to spank her, pushing herself against my groin."
    "The effect is enough to make me hope that I don't have to get up and leave the office in a hurry any time soon."
    "Because if that were the case, I'd be walking out bent double right now."
    "Soon we seem to be lost in a world of our own, each getting off on what we're doing or having done to us."
    "So much so that neither of us hears the door to my office being opened..."
    hide spank
    show shiori work
    shiori.say "Good morning Mr [hero.family_name]!"
    shiori.say "I wondered if you wanted some...BUTTOCKS!"
    "I look up in horror to see Shiori standing in the doorway, face aghast at what she's just walked in on."
    hero.say "Shiori...it's...it's not what it looks like!"
    show shiori work blush
    "Who in the hell am I trying to kid?"
    "What else could this be, other than exactly what it looks like?"
    "Shiori stands rooted to the spot for what feels like forever, and then backs out of my office without saying another word."
    hide shiori
    "Both Audrey and I are perfectly still now that we've been left alone once more."
    "I begin to wonder if Shiori's barging in on us like that has ruined the moment, and whether I should just stop."
    "But my hand, which had come to rest on Audrey's backside, slightly between her buttocks, suddenly makes an intriguing discovery."
    show spank audrey worktop marks wet
    "Rather than being put off by what just happened, my fingertips can now feel just how slick and wet she's become as a result."
    "The dirty little bitch actually got turned on by us being caught in the act!"
    menu:
        "Finger Audrey's pussy" if False == True:
            "Up until this moment, I've been totally focussed on spanking Audrey's ass, to the point of ignoring everything else."
            "But now I find my finger unconsciously circling the edges of her pussy, feeling just how invitingly wet it's become."
            "Without saying a word or giving any other kind of warning, I begin to gently stroke the inner folds."
            "Audrey responds to this unexpected turn of events by gasping and then proceeding to twitch and wriggle."
            "Having her doing so in my lap is quite something, and so I just can't help but push my finger slowly inside."
            "Audrey's moaning by now, a sound that's somewhere between arousal and humiliation."
            "As if the combination of being seen with her panties down and now being fingered roughly is just too much, she begins to buck in my lap."
            "When her climax finally comes over her, Audrey pants and cries with the spasms of her pussy, exposed and with nowhere to hide for the sake of her dignity."
        "Fingers Audrey's ass":
            "My guess is that Audrey's expecting me to either keep on spanking her buttocks or else take advantage of her exposed pussy."
            "But this is supposed to be a punishment, and so what would be the point in giving her what she wants?"
            show spank audrey worktop marks wet ass
            "Instead I part her buttocks and push a finger firmly into her anus, enjoying the way in which it twitches and tries to resist me."
            "Mirroring the reaction of her sphincter muscles, Audrey lets out a cry of alarm and struggles to see what I'm doing to her."
            "But she's in no position to put up any kind of resistance, and I easily hold her down while pushing the finger in still further."
            "Slowly, Audrey's yelps of pain turn into subdued moans of acceptance and submission, as she feels me press in as deep as I can go."
            "Intrigued to see how pliable her ass is, I push in another finger and then a third, each with the reception of a rise in her moans."
            "Soon I feel like I'm engaged in the act of slowly turning Audrey into some kind of perverted glove-puppet."
            "Then, before I can even think of putting another finger inside of her, she begins to twitch and jerk."
            "I don't know exactly what brings her off this time, but she cums with most of my fingers buried deep inside of her ass."
        "Continues spanking Audrey":
            "Perhaps she thinks that I've stopped because the feel of her wet pussy is enough to distract me from the task that I've already started."
            "But one massive crack on her already red and ruddy buttocks from the flat of my hand is enough to dispel any such illusions."
            "If anything, Audrey resumes squealing and yelping even more loudly than before now that the spanking has begun anew."
            "In fact, she's becoming so loud by now that I'm starting to get seriously worried about someone hearing her and coming to investigate."
            "The only choice that I seem to have is between stopping entirely or pressing on with even more gusto."
            "And so I choose the latter option, now whaling on Audrey's ass for all that I'm worth."
            "I swear that I can almost see the ripples that spread out from each impact of my palm in slow-motion."
            "The sight reminds me of those films run at ultra-slow speeds to capture the sight of droplets hitting water."
            "But it's the desperate gasping that Audrey's beginning to make that eventually pulls me back into the moment."
            "Red-faced and panting almost desperately, I'm not sure that she can take much more of this."
            "I give her one final slap of epic proportions, and then leave her, gasping and sweating across my lap."
    $ audrey.sub += 5
    hide spank
    return

label audrey_spanking_1:
    $ audrey.set_flag("spankingdelay",True,3)
    "My job's never been the easiest part of my daily life to manage, or the one that's given me the least amount of stress on a regular basis."
    "But at least it has the redeeming quality of paying me enough to put a roof over my head and fill the refrigerator."
    "It's just that recently things seem to have gotten a lot harder to handle in the office."
    "Almost as if something was actively working against me, making my daily grind that much harder to handle."
    show aletta
    "That's why I almost bite the head off of Aletta when she appears at my door."
    aletta.say "Oh, [hero.name] - do you have a moment?"
    hero.say "Aletta...what in the hell do you want?"
    "Aletta raises an eyebrow at the tone of my voice, luckily for me more in intrigue than offence."
    aletta.say "Well, it looks like someone hasn't had their required dosage of caffeine this morning!"
    hero.say "Sorry...sorry, Aletta."
    hero.say "I guess I'm just pretty strung out this morning, that's all."
    "Aletta gives me a cryptic smile and crosses her arms over her considerable chest."
    aletta.say "Well, what if I were to say that I could help make things that little bit easier for you?"
    hero.say "I'd say please do!"
    "Aletta nods before continuing, clearly pleased to have me indulge her."
    aletta.say "You recall how you have that file where all of the mail keeps disappearing?"
    "I nod eagerly at the mention of the troublesome case she mentions, my interest piqued."
    hero.say "Of course I do - every letter the client claimed to have sent seemed to vanish into a black hole!"
    aletta.say "Oh, it wasn't anything so dramatic as that."
    aletta.say "More like disappearing into the shredder down in the mailroom!"
    hero.say "WHAT?!?"
    "I stand up and slam my hands down on the desk, more for the sake of making a noise than anything else."
    "Aletta's grinning like a Cheshire Cat by now, simply loving the reaction that she's managed to get out of me."
    "If she could, I really think she'd be making a satisfied purring sound too."
    aletta.say "Let's just say that I happened to walk in on Audrey this morning."
    aletta.say "And that I caught her red-handed - shoving all of the correspondence for that file into the shredder."
    "Trying to control my temper, I pick up the receiver of the phone on my desk and dial the number for Audrey's extension."
    audrey.say "Hello?"
    hero.say "Audrey, would you mind stepping in here for a moment?"
    audrey.say "Okay...sure, I'll be right there."
    hero.say "Thank you so much..."
    "It only takes one glance from my quietly seething expression to Aletta's gloating smile for Audrey to realise she's in some rather deep shit."
    show aletta at left
    show audrey at right
    "Credit where it's due though, she still makes a valiant effort to appear none the wiser as to what's going on."
    audrey.say "Erm...you said that you wanted to see me?"
    show aletta happy
    "Aletta simply can't keep herself from letting out a sudden laugh at the other girl's feigned innocence."
    aletta.say "He know all about it - I told him what I saw you doing in the mailroom, you stupid little bitch!"
    "I cast a quick glance at Aletta, catching her eye."
    menu:
        "Let Aletta stay" if aletta.love >= 150 and aletta.get_flag_value("sex") >= 1 and aletta.sub >= 25:
            $ aletta_stay = True
            "I really should tell Aletta to get the hell out of here while I deal with Audrey in the only way that seems to work."
            "But there's just something about the gloating look that she has on her face right now that turns me on as much as the thought of spanking Audrey."
            hero.say "Audrey, get your ass here, right now and bend over the edge of my desk."
            hero.say "You deserve to be punished for what you've done."
            hero.say "And Aletta here deserves a reward, so she can watch me discipline you."
            "While Audrey slinks over to the indicated spot, Aletta looks shocked."
            "But I can't tell if she's more taken aback by the revelation that I'm about to spank Audrey or that I've invited her to watch."
            "Whatever the case, while she remains silent, I see that she also makes no effort to leave."
            "I nod at this, and she quietly closes the door as I push back my chair and go to stand behind Audrey."
        "Tell Aletta to leave":
            $ aletta_stay = False
            "I can see from the look on Aletta's face that she almost desperately wants to stay and see me chew Audrey out."
            "But the problem with that is the punishment I had in mind is a bit more extreme and definitely more corporal in nature."
            "I can't honestly go ahead with it if I'm going to have Aletta looking over my shoulder, so she's got to go."
            hero.say "Aletta, would you excuse us for a moment?"
            hero.say "Audrey and I have to straighten a few things out in our working relationship."
            hero.say "And as I'm sure you know, disciplinary matters are strictly confidential."
            "I can tell from the irritation on Aletta's face that she's loathe to give in, but I've got her on a technicality."
            "She gives me a terse nod and strides out, leaving me alone with Audrey."
            hide aletta
            hero.say "Audrey, get your ass here, right now and bend over the edge of my desk."
            hero.say "You deserve to be punished for what you've done."
    "As much as I know that this is pretty much what Audrey's been trying to push me into doing for some time now, I'm simply too hot to back down."
    "Before she was just playing stupid pranks on me around the office, but this has been a cause of stress for me in the past few weeks."
    "If she thought that getting me mad was going to be some kind of game, then I'm determined to prove her wrong."
    hide aletta
    hide audrey
    show spank audrey
    "Without a word of warning, I clap a hand on Audrey's thigh."
    "The blow is hard enough to make a slapping sound, and I hear her gasp in surprise - maybe even arousal."

    "With my other hand on the back of her neck, I squeeze one of her buttocks as hard as I dare, making her gasp again."
    hero.say "I used to think that you were just being playful, Audrey."
    hero.say "I used to think that you were kind of the office clown around here."
    "I give her ass another hard squeeze, just to keep her attention focussed on what I'm saying."
    hero.say "But now I see that I was wrong, and Aletta's right."
    hero.say "Only you're not a stupid little bitch - you're a spiteful little bitch!"
    "This time I practically crush her buttock in my hand, sure that I must have left bruises on her behind."
    "Audrey squeals at the sensation, trying to keep from making enough noise to have someone look in on us to see what's the cause of it all."
    hero.say "What you did caused me a lot of hassle."
    hero.say "It was a real pain in the ass."
    hero.say "So now I'm going to give you a pain in the ass in return..."
    "I deliver the first slap with the palm of my hand almost before the words are out of my mouth, giving Audrey no time in which to prepare."

    "Even though I start out slowly, actually trying to make a true punishment out of this, I can't help quickening my pace."
    "For all of her yelps and cries of pain, I can tell just how much Audrey must be enjoying what I'm doing to her right now."
    "Soon all thought of actually inflicting pain on her for the sake of teaching her a much needed lesson falls by the wayside."
    "All I can think about is the sight of her curvaceous body bent and prone over my desk."
    "The sound of her panting breath is making me breathe heavily almost in sympathy."
    "And every time my hand makes contact with her ass, I can't help but marvel at just how good it feels."
    "By now my cock is so hard that I can feel it pressing against the waistband of my shorts."
    "The only thing covering Audrey's reddening buttocks and what lies between them is a flimsy pair of panties."
    "It would be so easy to pull them down and discipline her in another way entirely."
    "My hand hovers over my flies for a moment..."
    "But then I seem to snap back to reality, as the weight of what I was thinking of doing hits home."

    hide spank
    if aletta_stay:
        $ audrey.sub += 10
        $ aletta.sub += 5
        show audrey at right
        show aletta at left
        "Before I can do anything to dismiss Audrey from my presence, Aletta gives her a vicious shove in the small of the back."
        aletta.say "Now run along, bitch - unless you want to be punished some more?"
        "Audrey looks back over her shoulder, as if contemplating whether or not to stand up to Aletta."
        "But then she turns and makes hastily for the door, and I think that I can see the beginning of tears in her eyes as she does so."
        "I slump down in my chair, wondering if I made the right choice in being so hard on Audrey."
        "But there seems to be no doubt in Aletta's mind, as she regards me with an admiration that almost seems to verge on actual physical hunger."
        hide aletta
    else:
        $ audrey.sub += 5
        show audrey
        "I give her a rough shove in the small of the back, pushing her towards the door in order to let her know that I'm done with her."
        "She staggers a little as she tries in vain to regain a little of the defiance and dignity that the spanking has cost her."
        "Stopping at the door to my office, Audrey looks back for a moment, as if expecting me to say something."
        "But I just sit back down behind my desk and make a dismissive gesture with my hand, unwilling to lose the upper hand I hope that this has gained me in our relationship."
        "Somehow, I doubt that this will be the last time that I find myself having to get hands on when it comes to dealing with Audrey in the workplace."
    hide audrey
    return

label audrey_spanking_start:
    $ audrey.set_flag("spankingdelay",True,3)
    "I'm so engrossed in the file open on my desk before me that I fail to even look up at the sound of the door to my office opening."
    "The fact that the person that's just walked in makes no attempt to identify themselves or say what they want isn't enough to make me do so either."
    "Past experience tells me that if they stay silent, then it's likely to be Aletta, waiting huffily for me to pay her attention."
    "Or if the person begins to make apologetic sounds in the next couple of seconds, then it's Shiori, demurely waiting for me to deign to notice her existence as usual."
    show audrey
    audrey.say "Hey, wake up - I haven't got all day!"
    "Now I have to admit, that was not what I was expecting to hear."
    "I look up to see Audrey standing in front of my desk, no sign of anything whatsoever in her hands that would make her visit work-related."
    "Taking a deep breath, I put down my pen and try to manage at least a ghost of a smile at her unasked for presence before me."
    hero.say "Audrey, to what do I owe the pleasure of this unexpected visit?"
    "She has a sardonic, superior smile on her face as she regards me."
    "But seeing as how that's more often than not her default expression, it doesn't help me guess at her purpose."
    "Audrey walks forwards so that she can sit on the edge of my desk."
    "She's sure to see that her skirt rides up as she crosses her legs, affording me a fine view of her hemline riding up to reveal her thighs."
    "Leaning forwards, she reclines on one elbow, as though she were posing for a revealing photoshoot."
    audrey.say "I just thought that I should drop by and let you know that I'm onto you..."
    "As distracting as it is to have her draped over my desk right now, I still manage to get my words out in an honest response."
    hero.say "Audrey, I have absolutely no idea what you're talking about."
    hero.say "Would you either start making sense or get the hell out of my office, please?"
    "Audrey raises her eyebrows at my statement of denial."
    audrey.say "Oh, but I think you do know what I mean."
    audrey.say "I've been having a little chat with Shiori on her breaks."
    audrey.say "And she's been very eager to tell me all about the private meetings you've been having."
    audrey.say "The private spanking meetings!"
    "Oh shit - now she's got my attention!"
    hero.say "Audrey, whatever happens between myself and other co-workers is none of your business!"
    "Audrey immediately jumps on what I just said, like a cat pouncing on its prey."
    audrey.say "Aha - I knew it, you have been spanking Shiori's pasty little behind!"
    audrey.say "And I'll bet it was right here in your office too!"
    "I try to keep from reacting to the accusation, but I can already feel my cheeks turning red."
    hero.say "Now you're just putting words in my mouth, Audrey."
    hero.say "I admitted to no such thing!"
    audrey.say "Ah, but you didn't deny it, did you?"
    audrey.say "Anyone can tell you that's as good as admitting that you're guilty!"
    hero.say "Who can tell you that - what are you even talking about?"
    "I lean back in my chair, trying as best I can to come across as calm and pragmatic."
    "But inside I'm already dreading the next question I have to ask and just where it might lead."
    hero.say "Okay, Audrey - what do you want?"
    "At this, she pulls back a little, putting a hand on her chest as if shocked by my line of questioning."
    audrey.say "What on earth can you be implying?"
    "I give her what I hope looks like a begrudging grin."
    hero.say "Come on - we both know you're not the Mother Theresa type, Audrey!"
    hero.say "There's no way that you'd come to me just for the sake of Shiori and some misplaced sense of sisterhood."
    hero.say "So I'll ask you again, Audrey...what do you want from me?"
    "She shrugs and makes a sound that's intended to be taken as nonchalant."
    audrey.say "Well, you see I'm a pretty modern kind of girl, Mr [hero.family_name]."
    audrey.say "And one of the things that I'm passionate about in the workplace is equality, regardless of sex, gender or race."
    audrey.say "So when I hear that Shiori has been getting a bonus that I haven't..."
    "Audrey sighs dramatically."
    audrey.say "Well, it makes me feel slighted, to say the very least."
    "Now I'm the one that's sighing."
    "Or maybe groaning at the inevitable conclusion I see fast approaching."
    hero.say "And do tell me, Audrey - how do you see there being a resolution to this most vexatious of issues in our department?"
    "Audrey's smile only becomes wider now, as she's clearly delighted to have reeled me in so far."
    "She uncrosses her legs and lowers them to the floor so that her backside is facing me across the desk."
    "Then she hitches up her skirt (which thanks to how short it is, doesn't take too much effort), so that her ass is revealed beneath her pantyhose and knickers."
    audrey.say "I would like to propose fair and equal treatment for my ass."
    "I have to admit that the fact she says this with a straight face does add to the moment somewhat."
    audrey.say "I feel it would only be right that my posterior receive regular spankings from yourself at regular intervals of my choosing."
    hero.say "Or in layman's terms..."
    audrey.say "Yeah...I want you to spank my ass."
    audrey.say "Good and hard, as and when I want it."
    hero.say "And if I don't?"
    audrey.say "Then I go running to HR and squeal on you for being a massive perv."
    "She gives me a sickly smile to underline her sincerity on the last point."
    "I take a deep breath, blow out my cheeks and shake my head."
    hero.say "Hell, Audrey, I don't see how you leave me any other choice..."
    menu:
        "Refuse":
            $ audrey.sub -= 5
            $ audrey.love -= 5
            hero.say "I'm going to have to ask you to leave, and take your filthy little collection of lies with you."
            show audrey angry
            "There's a genuine look of shock and surprise on Audrey's face as she shakes her head at me."
            "I'm damn sure that she's already steaming mad and plotting her next step to get her revenge."
            "But there's a part of me that's sure she's never been rebuffed like this when she's played these games in the past."
            audrey.say "Okay, if that's the way you want it."
            audrey.say "I'll be going to HR, you can be sure of that."
            audrey.say "But it won't be right now."
            audrey.say "Might be tomorrow, might be next week, or even next month."
            audrey.say "So enjoy thinking about it while that's hanging over you!"
            "She storms out in an appropriately dramatic fashion."
            "But I can't help thinking that by calling her bluff like that, I might just have begun to earn her begrudging respect."
        "Accept":
            $ audrey.set_flag("spanking",1)
            $ audrey.sub += 5
            $ audrey.love += 5
            hero.say "But to give you exactly what you want."
            show audrey blush
            "I try to keep from smiling, and I think that I manage to keep the effort from Audrey's notice."
            hero.say "So long as I have your word that you won't go to HR, I will agree to spank you, as and when you desire."
            "Audrey regards me with a triumphant look, almost as though she can't believe that I gave in to her demands so easily."
            "She nods her appropval and turns to leave."
            audrey.say "I'll hold you to that promise, but leave the exact time and place open-ended!"
            "I just nod and let her go, trying not to crack a smile as she walks out."
            "I'm quite happy to let Audrey think that she's got one over on me, whether she really has or not."
            "Especailly when the upshot of that is her coming to my office at semi-regular intervals to spank her brains out."
            "It's almost like I've been able to get my hands on that impressive ass of her's without even trying!"
    "Once she's gone and I'm alone in my office once again, I shake my head and go back to my work on the file in front of me."
    "I have a vague memory of someone telling me that I shouldn't try to get a job in an office, as it was all borning, monontous routine."
    "I think that if I met that person again, I might just be tempted to slap them across the face."
    return

label audrey_event_07:
    $ audrey_love_max = 140
    $ audrey.set_flag("story",7)
    "I didn't really notice the photocopy at first, as it was just sitting there atop my already teetering 'in pile' when I walked into the office and sat down at my desk."
    "In fact, I'd switched on my desktop, checked my voice messages and opened most of the mail that looked in any way interesting before my eyes drifted in its direction."
    "The first thing that catches my attention was the fact that I'm looking at an A3 sheet of paper that had the unmistakable sheen of having come out of the photocopier."
    "Most of the time, things get scanned these days, so there's not much need to use the copier, and sheets of that size are even rarer."
    "But when I actually look down and took note of just what the image is on the glossy paper, I immediately snatch it up for fear of someone walking in and seeing it."
    "There, on the paper, was the unmistakable, life-sized image of a backside, pressed up against the glass of the copier."
    "It's full and feminine in shape, wearing slight red knickers beneath black pantyhose."
    "There's the print of a kiss in red lipstick on one of the buttocks."
    "Written in marker on the other is 'Guess Who?', the writing exaggerated so as to hide it's owner's usual hand."
    "It's not either Valentine's day or April Fool's Day, so this has more of the air of a generally smutty prank about it."
    if not "lavish_start" in DONE:
        "I risk a glance up from the image of the backside, looking through the glass of my office door and into the space beyond."
        "Who could have done this and left it here for me to find?"
        "Even worse, what if someone else had walked in here and found it lying on my desk?!?"
    else:
        show lavish blush
        "I risk a glance up from the image of the backside, and find myself staring right into the wide, confused eyes of Lavish."
        "She has a pad and pencil in her hand, and I recall now that I asked her to be available to take the dictation of a letter before I left the office last night."
        "The shocked expression on her face makes it clear that she's already seen just what the photocopied image is."
        "Lavish continues to stare at me, like a proverbial deer in the headlights, clearly waiting for some kind of explanation."
        hero.say "Now, Lavish - let's not overreact, shall we?"
        "She glances over her shoulder at the photocopier in the corner of the outer office and then back at the image."
        "Unconsciously, her hand strays to her own ass."
        lavish.say "But...Mr [hero.family_name]...someone must have..."
        hero.say "Yes, Lavish - someone obviously thought it'd be funny to sit on the photocopier and...well, copy their backside..."
        "She looks at me now, clearly beginning to wonder how such a thing came to be on my desk, let alone dedicated to me with a signature in lipstick."
        lavish.say "Mr [hero.family_name]...did you..."
        menu:
            "Deny responsibility":
                $ lavish.love += 1
                hero.say "No...no, Lavish...I did not ask anyone to do this for my own gratification!"
                hero.say "There are strict rules and guidelines in the HR handbook that forbid anything of the kind..."
                "I try to calm myself down a little."
                hero.say "...as I'm sure you're aware."
                "Lavish just continues to stare at me with those huge, innocent eyes of her's."
                "She's not challenging me on my explanation, but she's not exactly jumping to agree with me either."
                hero.say "No, this is clearly someone's idea of a a joke...and a sick one at that!"
                hero.say "Maybe you could help me to identify the culprit?"
                "Lavish looks at me sideways."
                lavish.say "Let me get this straight, Mr [hero.family_name]."
                lavish.say "What you're saying is that you want me to try and identify one of my colleagues from a copy of their buttocks?"
                hero.say "Erm...maybe not in so many words, Lavish."
                hero.say "How about we limit your role to simply letting me know if you see anything suspicious?"
                lavish.say "Well, I'll be sure to sound the alarm if I see anyone else photocopying their backsides, Mr [hero.family_name]."
                "And with that, she mercifully turns and walks out of my office before I can dig an even deeper hole for myself to fall into."
            "Lead her on":
                $ lavish.love -= 10
                $ lavish.sub += 10
                "Well, I may not have, but what if I let poor, innocent little Lavish think that I did?"
                hero.say "Well, Lavish...I know that you're young, and probably very idealistic."
                hero.say "And believe me, all that woke stuff is great - in the world of social media and your college friends."
                hero.say "But this is the world of work, the REAL world."
                hero.say "And sooner or later, you have to learn that there are certain...favours, if you like."
                hero.say "These favours are the grease that keeps the wheels of commerce turning."
                hero.say "Do you know what I mean?"
                "Lavish swallows nervously, but she nods all the same."
                lavish.say "I...I think so, Mr [hero.family_name]."
                lavish.say "I think that you're saying you want me to do that for you."
                "She points a shaking finger at the photocopy on the desk."
                "I shake my head quickly."
                hero.say "No, Lavish - I'm not ASKING you to do anything."
                hero.say "I'm telling you that, if you chose, of your own volition and wholly without my coercion, to do certain things for my benefit."
                "At this, I glance briefly down at the image of the compressed buttocks for a moment."
                hero.say "Then I would, in turn, be inclined to bear them in mind, when it came time to make any decisions as to your future in this department."
                hero.say "Do you follow, Lavish?"
                "She nods hastily, smiling without it touching any other part of her face as she leaves my office."
                "And with that seed planted, all that I have to do now is find the culprit lurking out there to whom these buttocks belong."
    hide lavish
    "Unless someone from another department is behind this, then there are only really three viable candidates to hand."
    "I see Aletta stride by, her face already looking like thunder, probably on her way to chew someone out."
    "Shiori is desperately piling up files on her own desk, as though she's trying to look busy."
    "And Audrey is just sitting at her desk, openly checking her phone during office hours, seemingly without a care in the world."
    "I can only guess that whoever left this here for me to find is still wearing what can be seen in the image."
    "And that part of the thrill they're getting out of this is making me sweat over just who is behind it."
    "So, find the pantyhose, find the culprit."
    "It should be that simple, right?"
    "Wrong - of course not!"
    "It only takes a cursory glance around to confirm that, on this of all days, the three of them have chosen to wear almost identical black pantyhose to work!"
    "I can see that I'm not going to be able to solve this little mystery by just sitting here and scrutinising the image of the backside."
    "The fact that it's pressed up against the glass of the copier means that it really could belong to any of the three potential suspects."
    "And just in case you were wondering, it's a very nice ass indeed!"
    "I don't want you to hear all of this half-assed detective bullshit from me and think that I was doing it because the sight of the backside had upset me in any way."
    "I fully confess to taking some time out to appreciate it."
    "My concern was more for the sake of being drawn into someone's kinky games in the workplace and the possible repercussions for me in the future should this kind of thing become a habit."
    "And so, I was going to have to do some amateur sleuthing."
    $ photo_leave = False
    $ accuse_aletta = False
    $ accuse_shiori = False
    while not photo_leave:
        menu:
            "Accuse Aletta" if aletta.love >= 50 and not accuse_aletta:
                $ accuse_aletta = True
                "I fire off a short email to Aletta, asking if she had a moment to discuss something in my office, keeping things suitably vague."
                "Maybe choosing to confront her is a bit rash, but Aletta's always been forceful and upfront about things."
                "So if it is her, chances are she'll just up and admit it."
                "But then again, if not..."
                "A few minutes later, Aletta comes striding into my office, an expectant look on her face."
                show aletta angry
                aletta.say "Couldn't you have just explained whatever it is you want to discuss in your email?"
                aletta.say "You might not be particularly busy this morning, but I can assure that I am!"
                hero.say "Well, Aletta...thing is, this isn't really the kind of thing I can discuss in an email."
                "She raises one eyebrow, showing that if she's not impressed, at least she's a little intrigued."
                hero.say "You see, I found this on my desk this morning."
                "I hold up the image for Aletta to see, and at first she squints at it, as though she's not sure exactly what she's looking at."
                aletta.say "Is that what I think it is?"
                hero.say "It's an ass, Aletta - the question is, just who's ass is it?"
                aletta.say "Well, I can't say that I recognise it myself..."
                "Aletta trails off as she suddenly realises the inference that I'm making."
                aletta.say "[hero.name]...you're not seriously suggesting that I..."
                hero.say "I'm not suggesting it was you, Aletta."
                hero.say "Just giving you a chance to admit it...if it is you, that's all."
                "Aletta's expression darkens instantly and she crosses her arms over her chest."
                aletta.say "How dare you!"
                hero.say "What did I do, Aletta?"
                hero.say "I didn't accuse you of anything - but you have black tights on and a shapely butt!"
                hero.say "What was I meant to think?"
                aletta.say "This conversation is over!"
                aletta.say "And if you have any further complaints of this nature, then I suggest that you go through the correct channels and contact HR!"
                $ audrey.love -= 5
                $ aletta.love -= 5
                "With that, Aletta turns on her heel and storms out of my office."
                hide aletta
            "Accuse Shiori" if "shiori" not in HIDDEN and shiori.love >= 50 and not accuse_shiori:
                $ accuse_shiori = True
                "I put a call through to Shiori's desk phone, just asking her to come into my office, nothing more."
                "Sure enough, less than a minute later, Shiori comes hurrying in to see what it is that I want."
                show shiori
                shiori.say "Hello Mr [hero.family_name], good morning - what was it that you wanted?"
                "In a way, this should be far easier than confronting either Aletta or Audrey."
                "But I still need to remember that, under her innocent exterior, Shiori still likes to be manipulative in her own unique ways."
                "I hold up the image, waiting for its significance to register on her face."
                show shiori blush
                shiori.say "Oh...oh dear...Mr [hero.family_name]!"
                "I nod in agreement, thinking that Shiori has easily grasped what the issue is here."
                hero.say "I think you can see my problem, Shiori, can't you?"
                "Shiori nods slowly, glancing back over her shoulder in the general direction of the photocopier."
                "So, it was her after all!"
                hero.say "I think you already know what we have to do in order to remedy this situation, don't you, Shiori?"
                "She gulps and nods, clearly a little scared of what lies ahead."
                shiori.say "I...think so..."
                hero.say "Well, what are you waiting for?"
                hero.say "No time like the present!"
                shiori.say "Really, Mr [hero.family_name]...right here and now?"
                hero.say "Erm...why not?"
                shiori.say "Because people will see me!"
                shiori.say "Can't I put my bottom on the photocopier when everyone else has gone home for the night?"
                "She can clearly read from my expression that there's been a misunderstanding."
                shiori.say "Oh...I thought you wanted me to..."
                hero.say "No, Shiori...I thought that you already..."
                "Shiori puts her hand in front of her mouth and giggles, I suspect both at the miscommunication and my evident resulting embarrassment."
                shiori.say "Oh no, this can't be my bottom - I don't own any panties as wild as those!"
                shiori.say "All of mine are soft, and white and..."
                hero.say "Alright, alright, Shirori...I get the picture!"
                $ audrey.love -= 5
                $ shiori.love += 5
                "Still giggling to herself, Shirori leaves me alone with the image of the mystery backside once more."
                hide shiori
            "Accuse Audrey":
                $ photo_leave = True
                "It's with a growing sense of dread that I call up Audrey's desk phone and ask her to step into my office."
                "I see her give her habitual shrug and grunt of annoyance at being interrupted at work by work."
                "But she gets up and comes over all the same."
                "I should have guessed right from the start that this kind of trick has Audrey's name written all over it."
                "What's not so clear to me is just why it bothers me so much and I'm almost afraid of confronting her."
                "Is it about the power dynamic, or am I just scared of admitting that there's something maddeningly sexy about the whole thing?"
                show audrey
                "Where Aletta would have strode in and Shiori scuttled as meekly as a mouse, Audrey saunters as though we're casual acquaintances, rather than superior and subordinate."
                audrey.say "What's up, boss man!"
                hero.say "Audrey, would it kill you to show me even the smallest degree of respect?"
                hero.say "Maybe call me 'Boss' or even 'Mr [hero.family_name]' every once in a while?"
                audrey.say "I don't know...it might...so I think, why take the risk?"
                "I shake my head, hating that she makes me sound more like a bitter old man every time we have this little talk."
                hero.say "Anyway...that's not what I called you in here to discuss."
                hero.say "This is..."
                "I slide the image across the top of my desk towards Audrey."
                "It's turned so that she can read the words written upon it with ease."
                "At the sight of it, she smiles wickedly, giving me all of the proof that I need to know that she really is the culprit."
                "Without saying another word, Audrey turns and proceeds to sit down on the image, lining her ass up with the one on the paper."
                show audrey blush
                audrey.say "If the shoe fits - or maybe in this case, the butt-plug!"
                hero.say "So it was you - you admit it!"
                audrey.say "Phfft...of course it was me!"
                audrey.say "Shiori's too much of a little mouse and Aletta couldn't have gotten her massive horse's ass on there for the pole she's got stuck up it!"
                "I really should reprimand her for speaking about her colleagues in such a derogatory manner."
                "But right now, I'm more interested in the matter at hand."
                hero.say "Would you mind telling me why you felt the need to do it?"
                "Audrey's got her hands on the desktop now, leaning backwards as she looks at me over her shoulder."
                audrey.say "Oh, I just thought it might keep you from getting chewed out by HR, that's all!"
                hero.say "What...what do you mean by that?!?"
                audrey.say "Oh, don't play the innocent with me - I've seen how you look at me!"
                show audrey happy
                audrey.say "I figured that if you had this to keep you occupied, it might stop everyone else from noticing how much time you devote to staring at the real thing!"
                $ audrey.love += 5
                "With that, she kicks her legs and stands up from the desk, making sure to bend over a little as she does so."
                "As she straightens up, Audrey runs her hands up her body and sighs in a suggestive manner."
                "A second later and she's gone, leaving me speechless, confused and more than a little aroused."
                hide audrey
            "Investigate" if not accuse_shiori and not accuse_aletta:
                $ photo_leave = True
                "I decide that it'd be a bad idea to call any of the three girls into my office and present them with my accusations."
                "If they turn out to have a valid alibi, then not only would I end up with proverbial egg on my face, the whole thing would be out in the open too."
                "I slide out of my office door, trying as best I can to appear casual."
                show shiori
                "The first of the three that I come across is Shiori, ploughing through the files on her desk in the usual determined and yet incompetent manner she possesses."
                hero.say "Erm...Shiori?"
                "Her head bobs up with a suitably cute and eager smile plastered across it."
                shiori.say "Yes, Mr [hero.family_name] - what can I do for you?"
                hero.say "I need the...Zimmerman file...that's it - can you look the Zimmerman file out for me?"
                "Shiori nods and is instantly on her feet and heading for the last and lowest drawer of the filing cabinets."
                "I follow discretely as she begins to bend down, then gets on her knees in order to reach to the very back of the drawer."
                "Her skirt isn't exactly long, but it's still not riding up nearly enough to let me see her panties yet."
                hero.say "That's great, Shiori - keep on digging in the back until you find it!"
                "Finally she leans that little bit further and I can see..."
                "...the very edge of her neat, pristine, white panties."
                shiori.say "Here you go, Mr [hero.family_name]!"
                hero.say "What...oh, right...just put it on my desk, Shiori."
                $ shiori.sub += 5
                hide shiori
                "I hurry off, leaving Shirori looking a little puzzled and rather deflated."
                show aletta
                "I catch up with Aletta in the lift lobby, and before I can even speak to her, I notice that she's looking agitated."
                hero.say "Hey, Aletta - what's up?"
                aletta.say "What...oh, hello [hero.name]."
                aletta.say "Ah, it's nothing really - I just lost an earring on my way into the office this morning."
                aletta.say "The pair had some sentimental value."
                hero.say "Sentimental...really?"
                "Aletta frowns at my comment."
                aletta.say "Yes, sentimental - I might be professional when it's appropriate, but I'm not made of ice!"
                "At times, she could have fooled me."
                "Thinking as quickly as I can, I point to the far corner of the room."
                hero.say "What's that over there, something catching the light?"
                "Aletta rolls her eyes at me, but as she's already stated the sentimental value of the missing earring, she can hardly refuse to investigate."
                "Which means in order to do so, she has to bend down as far as possible."
                "I follow her into the corner, straining to see the first sign of her underwear as her skirt begins to ride up."
                "At first I don't think that I can see anything, but then I realise she has on a pair of panties in a matching shade of black to her tights."
                aletta.say "No, that's not it!"
                $ aletta.sub += 5
                "I manage to stand up a mere second before Aletta does, and she eyes me suspiciously, but then shakes her head and walks back to call a lift."
                hide aletta
                "Two down and one to go - so it must be Audrey!"
                "Asking around the office lets me know that she was last seen making for the stationary cupboard."
                "When I arrive, I find the door ajar."
                "Checking that no one else is around, I sneak inside."
                show audrey
                "Almost instantly, I see Audrey crouched in the far corner, struggling to reach something buried on a low shelf."
                "She still hasn't shown any sign of noticing me, so I creep closer and hide behind a shelf to watch."
                "Audrey leans further and further forwards, paying no attention to the fact that her barely acceptable skirt is already almost at the top of her thighs."
                "I lean forward myself, watching as it begins to creep up and over her buttocks."
                "Soon I can see the entire curve of Audrey's ass, and my dick starts to get stiff at the sight."
                "Her legs are so shapely and perfect beneath those black pantyhose that I almost forget why I'm actually doing this."
                "Finally I can see the red fabric of her panties that proves she's the culprit."
                "I could sneak out now and confront her with the evidence later."
                "But instead I remain rooted to the spot, watching as her skirt rises even higher."
                "By now, Audrey's skirt is fully hiked up around her waist, leaving her ass exposed to view."
                "She must be close to reaching what she's after, as she begins to drag herself forwards and then fall back again repeatedly."
                "All the time she's making these small, intense sighing and gasping noises, as if the effort is taxing her physically."
                "At my best guess, it takes me perhaps five minutes of watching this, sweating, fearing discovery and feeling my cock stiffen still further, before I realise that she's not looking for anything at all."
                show audrey happy
                hero.say "Very clever, Audrey...you can come out now."
                "I watch as Audrey eases herself backwards and out of the hole she had cleared for herself amongst the boxes of stationary."
                "She's smiling, clearly pleased with herself, and none too quick to pull her skirt back down either."
                audrey.say "Why boss, whatever do you mean?"
                hero.say "You know full well what I mean - I have something in my office that belongs to you!"
                show audrey blush
                $ audrey.sub += 5
                audrey.say "Oh, you feel free to hang on to it - maybe it'll help you keep the image fresh in your mind!"
                hide audrey
    "And with that, I'm alone again."
    "The worst thing is that I now have to get through the rest of the day with all of this still fresh in my mind."
    return

label audrey_event_06:
    $ audrey_love_max = 120
    $ audrey.set_flag("story",6)
    $ audrey.set_flag("nodate",False)
    $ if "audrey" in HIDDEN: HIDDEN.remove("audrey")
    "I haven't honestly calmed down or stopped ruminating over it since the incident happened the other night."
    "How I actually managed to get home from a restaurant where Audrey had walked out on me with cum-stained pants..."
    "Well, that's another story and doesn't bear repeating here."
    "What really matters is that this is the first chance I've had to confront her about it and demand an explanation."
    "Was planning on sending her a firm email or leaving a message on her phone telling her that I wanted her in my office first thing."
    "But she almost leaps out from behind her desk as soon as she sees me walk in and close my office door behind me."
    "I can here her knocking even before I've managed to sit down."
    "And so I don't, instead choosing to lean against my desk, arms crossed."
    hero.say "Come in!"
    show audrey
    "The door opens a second later, as Audrey slips in and then closes it behind her."
    audrey.say "Before you say anything - no, I don't know what gets cum stains out of a pair of cheap pants!"
    "She sniggers almost as she says this, not letting me get a single word in before the insults start to fly from her lips."
    hero.say "Audrey, I really don't..."
    audrey.say "Oh, I'm sorry - were they your favourite pair?"
    audrey.say "The one's that were so shiny you could see your face in them?"
    audrey.say "Don't worry, I'm sure the thrift store will have another pair in some day!"
    "I never really understood the way people described a red mist descending over them."
    "But meeting Audrey really cleared that one up for me rather neatly."
    "It's almost like I suddenly can't actually hear what she's saying any more."
    "I can see her mouth moving, and from way she's standing, I know she's still insulting me."
    "There's just nothing else apart from the unshakable feeling that I want her to stop."
    "I just know that want her to shut up - and I don't care how it happens."
    "I just want the words to stop coming out of her filthy, disgusting mouth..."
    menu:
        "Keep calm":
            $ audrey.love -= 20
            $ audrey.sub -= 20
            "In that moment, I could as easily have seen myself doing something to harm Audrey as I could doing nothing at all."
            "It honestly felt like a simple choice between two alternatives, with no care for the consequences of either."
            "A cold sweat breaks out on the back of my neck as I realise just how close I came to lashing out at her."
            hero.say "I...I don't care, Audrey."
            audrey.say "What?"
            "She cocks her head on one side, genuinely surprised at being stopped in her tracks."
            hero.say "I said I don't care, Audrey - about what happened the other night, about what you're saying to me now, none of it."
            hero.say "What I'd like you to do is get out of my office."
            hero.say "RIGHT NOW!"
            "Audrey looks at me with a mixture of amazement and contempt on her face."
            "But, to my great relief, she finally does as she's told."
            "She might have said something on the way out, but I ignore it and deliberately look at the wall until she's gone."
        "Lash out":
            "My hand moves before I realise what I'm doing, and far faster than I thought I was capable of moving."
            "Audrey's words are choked off raggedly and her eyes bulge with shock and what looks like genuine fear."
            "Simply relieved to have her stop speaking, I feel a similar sense of shock as I it dawns on me just why she shut the up."
            "As reality comes back to the fore, I see my own hand clamped firmly around Audrey's throat, squeezing hard."
            "For a moment, I genuinely can't make sense of what I'm doing, and so I keep on doing it."
            "In the end, it's Audrey's expression that makes me snap out of it."
            "I can see that beneath the real fear, there's a glimmer in her eyes that belies a deeper emotion."
            "This only starts to make sense when I notice that she's not struggling against me in any real sense."
            "In fact, my grip doesn't feel strong enough to choke the life out of her now that I can feel my limbs once more."
            "So the reddening of her cheeks and the sweat starting to bead at her temples must be on account of something else entirely."
            "I let go of her with some considerable effort, and she staggers to my desk."
            "Once there, Audrey takes a series of deep, rasping breaths as she eyes me in a disturbing manner."
            "Shouldn't she be mad, screaming for help or threatening me with, well...anything right about now?"
            "Instead, she almost looks like her eyes are eating me up."
            hero.say "Audrey...I'm sorry...I don't know what came over me..."
            $ audrey.sub += 2
            $ audrey.love += 2
            "In response, her smile is, if anything, a bit unnerving."
            show audrey happy
            audrey.say "Heh...heh...I do, [hero.name]..."
            audrey.say "You just accidentally behaved like a real man for a change..."
            audrey.say "But don't worry...you're already turning back into a little pussy..."
            "She let's out a cough before she can go on."
            audrey.say "I can practically hear your cock withering up back inside of you right now."
            audrey.say "You should see if one of the guys in the office wants to fuck the puckered little hole it leaves behind and call you his bitch!"
            menu:
                "Restrain myself":
                    $ audrey.love -= 10
                    $ audrey.sub -= 10
                    "I shake my head, not knowing if I should be more ashamed at myself for what I just did."
                    "Or else more sorry for Audrey that she wants to provoke more of it."
                    hero.say "I'm sorry, Audrey - but I'm not going to rise to your barbs again."
                    hero.say "I understand if you want to take this up with human resources."
                    hero.say "But I do feel that there are more than a few instances of your own behaviour that would interest them too, were I to bring them up."
                    "Audrey looks for a moment as if she's about to begin another tirade."
                    "But then something just seems to go out of her all of a sudden, and she shakes her head as she makes to leave."
                    "She says more before she's out of the door, but I tune her out and then collapse into my chair."
                    "I still can't believe she made me mad enough to lash out like that."
                    "Or that she really seemed to want to provoke me further!"
                "Give her what she deserve":
                    $ audrey.love += 3
                    $ audrey.sub += 3
                    $ audrey.set_flag("sex",1,"permanent","+")
                    "My free hand flashes out, catching Audrey a vicious slap with the palm of my hand."
                    "A seconds later she feels the other side as it deals her a backhander on the return."
                    "Before she can as much as cry out, I force her head down onto the desk and hold it there, hand in her hair."
                    "I spread her legs by kicking at her heels until she does as I desire, and then I press my weight onto her as she's leant over the desk."
                    "The hand not pinning her down yanks her skirt up to her waist and then roughly tugs down her pantyhose and knickers almost to her knees."
                    "I seem to have lost the power of speech this entire time, as though no words will explain what I'm doing or why."
                    "The first sound that I hear Audrey make is a strained moan as I rub my fingers harshly against her pussy."
                    "For some reason, the fact that it's already moist, the scent of it detectable on the air, makes me even more incensed."
                    "I push first two, then three and finally four fingers into Audrey's slippery lips."
                    "This isn't some attempt to coax her gently towards being ready for it."
                    "More like it's a way of mocking and humiliating while she's helpless."
                    "Even as she makes more incoherent sounds, I feel my desire to degrade her growing alongside my cock."
                    "I drag my fingers out of her and almost tear open my flies."
                    hide audrey
                    show audrey desk
                    "Leaning in close, I make sure Audrey can feel the head of my cock against her burning pussy."
                    hero.say "You remember this guy, Audrey?"
                    "She moans again, making no sense whatsoever."
                    hero.say "Sure you do - you were all over him the other night."
                    hero.say "Until you ran off and left him in the lurch..."
                    "I push myself just far enough inside of her to get the reaction I'm looking for."
                    hero.say "He wants to show you what you missed out on by cutting and running..."
                    hero.say "And this time, he's not taking no for an answer!"
                    "I don't want to make this some kind of kinky tease for her, so I shove myself inside as roughly as I can."
                    "She makes a sound that's more like an animal that's been kicked in the gut than a human being."
                    "If I'm honest, I get more gratification from that sound than I do the sensation of being inside of her."
                    "My incandescent rage means that I barely perceive what my cock is feeling."
                    hero.say "You had me open and exposed back then, Audrey..."
                    hero.say "What do you say about returning the favour, eh?"
                    show audrey desk up
                    "I pull her up by her hair just so that I can reach around and grasp the front of her blouse."
                    "The fabric rips almost without effort, and I begin to tear it apart."
                    "From there it's all too easy to spill Audrey's large breasts out and onto the desk."
                    "That done, I push her head back down, pressing the exposed orbs against the wood."
                    "I can't see it happening, but I get a perverse thrill at the thought of Audrey's nipples being rubbed abrasively across the desktop."
                    "Audrey's hands are groping amongst the papers and paraphernalia on my desk now."
                    "Her fingers clasp around and crease up handfuls of paper as I keep on pounding into her the whole time."
                    "Suddenly I have a moment of clarity, realising that there are several heavy objects well within her reach."
                    "She could snatch one up and swing it at me with ease, should the idea form in her mind."
                    show audrey desk up drool
                    "But then I catch a glimpse of Audrey's face in the reflective surface of the window."
                    "And I instantly know that there's no way she could manage such a thing."
                    "Audrey's cheeks and forehead are a vivid shade of red, her eyes crossed and almost rolling back into her head."
                    "Her tongue is lolling out of her mouth as she pants like an exhausted dog."
                    "I've never seen anything like it before...and it's strangeness snaps me back to reality."
                    "What freaks me out isn't the extreme nature of her expression, but the fact that it seems to suggest she's in a state of sheer ecstasy."
                    "Already I can feel my heart rate slowing and my cock beginning to shrink."
                    "I know that I should take more care, but I just can't help pulling out and stepping quickly away from Audrey."
                    "Without me to support her, she crumples to the floor and lays there in an untidy heap."
                    "Her body is still quivering even then, and I can hear her moaning as she rides out the last of what must be an orgasm."
                    "All I can do is stare at her, wondering just what the hell motivates this baffling woman."
                    "Did she actually..."
                    "Is there a chance that she..."
                    "Fuck - am I really thinking that she might have goaded me into doing this because she wanted it?!?"
    hide audrey
    return

label audrey_event_05:
    play sound "sd/cell_vibrate.mp3"
    "My mobile vibrate and I look down to see that the call is from Audrey, which means I really have to try to finish groaning before I answer it."
    hero.say "Hey, Audrey - what do you want now?"
    audrey.say "My, my - who's a sourpuss today?"
    audrey.say "Keep that up and I won't tell you about the nice surprise I have planned for tonight, [hero.name]!"
    "I sigh in resentment and shake my head."
    hero.say "Okay, Audrey - what have you got planned?"
    audrey.say "You are inviting me to that new restaurant that just opened up in the city."
    menu:
        "No":
            hero.say "Nah, Audrey - thanks for the offer, but I think I'll take a rain-check on this one."
            $ audrey.love -= 5
            audrey.say "Huh...whatever, [hero.name] - your loss!"
            "And with that, she cuts me off dead."
            return
        "Yes":
            "I know I shouldn't, but I really do like the look of that place..."
            hero.say "Okay, Audrey, I'll come along."
            audrey.say "Great, so it's a date then!"
    "As I put my phone down again, I'm already wondering if I've made the right decision."
    "Or just another terrible mistake that happens to involve Audrey."
    $ audrey.set_flag("story",5)
    $ game.pass_time(1)
    scene bg highclassrestaurant with fade
    show audrey eat
    "Even though I am dressed in a fancy suit that I would normally be uncomfortable in, I don’t even notice it as I look toward Audrey."
    "With it being a friday evening, the lighting lowered, and it nice and warm in the restaurant, this date is much more cozy than I expected it to be."
    "I expected it to be stuffy and boring since she insisted on a classy restaurant."
    "I can’t help but smile as I watch her reading the dessert menu in her stunning black dress that fits her so well."
    "I’m imagining her stripped out of it though, laid out on my couch in front of a fireplace as we make love when she glances up and catches me looking."
    audrey.say "What are you thinking?"
    menu:
        "Tell her":
            hero.say "I’m imagining what I want to do to you later."
            $ audrey.love += 1
        "Tease her":
            hero.say "Wouldn’t you like to know."
            $ audrey.sub += 1
    show audrey eat handjob
    "She gives me a mischievous look and scoots her chair closer to mine."
    "At first she lays her head on my shoulder and raises her hand on my leg."
    "I don’t even care or think about her getting makeup on my shirt."
    "I just enjoy her being closer to me and lean my head on top of hers closing my eyes when I suddenly feel her hand sliding up my leg under the table."
    show audrey eat handjob transparent awkward dick
    "My eyes fly open and I straighten back up in surprise as her hand wraps around my dick and pull it out of my pants my pants."
    hero.say "Audrey, what are you doing?"
    audrey.say "What do you think I am doing?"
    hero.say "This is supposed to be a special night."
    audrey.say "Oh don’t worry, it will be."
    "She starts to rub me off and I fight with myself about whether I should let her do it or not."













    "I can’t find a reason to make her stop as it starts feeling good, better than good, so I don’t say anything and causally move to give her more access to my crotch."
    "I try to not let it show on my face what she is doing, and have to act like I am clearing my throat to hide a moan."
    "Luckily everyone else is so into their partner no one notices us and our activities."
    hero.say "Ohhh… Audrey… Mmm. You’re… you’re so… gooood to me."
    "It is a struggle to form words as she picks up the place and I have to grip onto my knee with one hand and the table cloth with the other."
    "It gets increasingly hard to keep my breathing in control and I want so badly for her hand to be rubbing off my bare cock but we can’t do that here."
    "It will have to wait for later."
    show audrey eat kiss solid
    "She leans forward and kisses my lips slowly, then gives it a little bite and I start to lose focus."
    "She starts to pay special attention to the tip the best she can through my pants and a small moan escapes my lips."
    "I don’t care at this point if anyone hears but I hear her laugh."
    audrey.say "Does that feel good, [hero.name]?"
    "I give her a look because I don’t trust myself to form words right at that moment."
    show audrey eat handjob transparent dick
    "Just then the waiter comes with our food and I panic a little and expect her to let go, but she doesn’t stop."
    "She keeps rubbing me off while talking casually to the waiter and I start to sweat."
    "It is all I can do to not give it away, and Audrey is expertly managing to make it look like we are just holding hands under the table."
    man_say "And there you go. If you need anything else just let me know."
    audrey.say "Of course, thank you."
    "Audrey talks so causal if I were the waiter I never would have guessed what was going on."
    "It turns me on and makes me lust for her even more."
    "Audrey starts eating with one hand while she continues to stroke me and all I can do is keep watching her mouth work."
    audrey.say "You better start eating or that waiter is going to come over here wondering what is wrong with your food, and you are already looking a little red."
    "I realize she is right and look for the waiter, realizing he keeps glancing this way."
    "I quickly pick up my fork but only manage to take a couple bites."
    "This is impossible!"
    "I am hungry for something but it isn’t food."
    "This woman is driving me mad."
    "I finally just leaned into her neck like I am whispering sweet things into her ear, but really I am whimpering and begging her to stop."
    hero.say "Audrey, enough… I can’t take much more."
    "That just makes her take a stronger grip and start stroking harder."
    "I grunt and grab hold of her arm."
    show audrey eat handjob transparent orgasm
    hero.say "Audrey-I’m going to-."
    "Before I can say anything I cum as a tremor goes through my body."
    show audrey eat handjob transparent orgasm cumshot
    "I close my eyes tight and have to lean onto her shoulder to not fall out of my chair, still holding onto her wrist maybe a little to tight as I hear her laugh at me."
    hide audrey
    show audrey eat transparent pants dick
    "When I finally manage to calm back down and catch my breath Audrey is licking her fingers clean before she pushes her chair out and stands up."
    hero.say "Where are you going?"
    audrey.say "Home. I’m a bit tired."
    "With a smirk she walks away just as the check comes."
    "I look at the bill and then down at my pants and see the large stain on the front of them."
    "There is no way I am walking out of here without someone noticing."
    "And Audrey is already far gone so I don’t even have her to walk in front of me to hide it."
    "She wasn’t going to get away with this one once we got back to the apartment."
    $ audrey.set_flag("nodate",True)
    $ HIDDEN.append("audrey")
    $ game.pass_time(4)
    $ hero.fun -= 5
    $ hero.energy -= 2
    return

label audrey_kiss_me:
    call audrey_greet from _call_audrey_greet_5
    show audrey








    "When Audrey begins her usual routine of teasing and invading my personal space, I let her."
    hide audrey
    show expression "audrey kiss "+audrey.get_clothes()
    "And it's only when she's leaned in and tried to kiss me for perhaps the hundredth time, that she suddenly realises she's succeeded."
    "Before she can react, I increase her surprise tenfold my returning the kiss."
    "Gently and falteringly, we start to feel each other out from this strange and chance meeting."
    "Audrey seems to become almost timid now, as if she's been exposed and unnerved by getting the very thing that she's always claimed to want from me."
    "But she soon recovers sufficiently for the kiss to go from being awkward and unsure to easier and ever more enjoyable."
    hide expression "audrey kiss "+audrey.get_clothes()
    return

label audrey_give:
    audrey.say "What do you think about your present?"
    hero.say "What present?"
    audrey.say "The necklace I am wearing, silly."
    hero.say "!?"
    audrey.say "I bought it just so that you could see me wearing it..."
    return

label audrey_give_valentine:
    show audrey
    "Audrey walks hesitantly towards me."
    call audrey_greet from _call_audrey_greet_7
    show audrey blush
    audrey.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Audrey hands me a box of chocolates."
    hero.say "Thank you, Audrey."
    $ hero.gain_item(gift)
    hide audrey
    return

label audrey_give_birthday:
    show audrey
    "Audrey walks towards me."
    call audrey_greet from _call_audrey_greet_8
    show audrey happy
    audrey.say "Happy birthday [hero.name]!"
    call audrey_give from _call_audrey_give
    return

label audrey_give_christmas:
    show audrey
    "Audrey walks towards me."
    call audrey_greet from _call_audrey_greet_9
    show audrey happy
    audrey.say "Merry christmas [hero.name]."
    call audrey_give from _call_audrey_give_1
    return

label audrey_init:
    if "audrey" not in HIDDEN:
        $ HIDDEN.append("audrey")
    return

label audrey_event_01:
    show audrey danny
    if "audrey" in HIDDEN:
        "I see Audrey, My colleague from work, she seems a little scared."
    else:
        "I see Audrey, she seems a little scared."
    "A suspicious man is talking to her."
    thug_say "Do you live on a chicken farm?"
    thug_say "'Cause you sure know how to raise a cock."
    audrey.say "Please go away."
    thug_say "You are so selfish!"
    thug_say "You're going to have that body the rest of your life and I just want it for one night."
    "Audrey looks at me with expectation in her eyes."
    menu:
        "Help her":
            $ audrey_love_max = 40
            $ audrey.set_flag("story",1)
            $ if "audrey" in HIDDEN: HIDDEN.remove("audrey")
            $ fight = False
            $ audrey.set_flag("greeting",True,1)
            hide audrey
            hide audrey danny
            show danny
            hero.say "Hey man, she said to let her be and go on your way."
            thug_say "Fuck off, don't mess with my squeeze."
            hero.say "I said to leave her alone."
            menu:
                "Pretend she's yours":
                    hero.say "That's my pussy your messing with, and I don't like when others play with my toys."
                    thug_say "Didn't know that fine piece of ass was taken."
                    thug_say "I'll get another slut to take care of my pole."
                    hide danny
                    show audrey
                    audrey.say "Thanks for the help."
                    hero.say "It was nothing."
                    audrey.say "Arent you a little cocky ?"
                    show audrey blush
                    audrey.say "So, I am your 'pussy' and you don't like when people 'mess' with me ?"
                    hero.say "Ahem..."
                    audrey.say "Oh, and your 'toy' too..."
                    hero.say "It was to make him go away..."
                    audrey.say "Well, I do hope that's true."
                    audrey.say "Thanks for the help."
                    hero.say "It was nothing."
                    $ audrey.set_flag("toy",1)
                    $ audrey.sub += 5
                "Attack him":
                    hero.say "I'll have to kick your ass then."
                    $ fight = True
                "Intimidate him":
                    hero.say "If you don't go I'll crush your balls like wallnuts and make you eat what's inside."
                    if hero.fitness >= 25  or hero.charm >= 25:
                        thug_say "Ok, ok, don't be so work up about some pussy."
                        hide danny
                        show audrey
                        audrey.say "Thanks for the help."
                        hero.say "It was nothing."
                        $ audrey.love += 2
                    else:
                        "He doesn't seem impressed"
                        $ fight = True
            if fight:
                python:
                    d = 50
                    if not "martial_arts" in hero.skills:
                        d += 25
                if not hero.fitness >= d:
                    show danny fight lose
                    "I punch the jerk in the guts and kick him in the nuts."
                    "After that I throw him out of the pub."
                    hide danny
                    hero.say "Are you okay Audrey ?"
                    show audrey
                    audrey.say "I am fine [hero.name], thanks for the help."
                    $ audrey.love += 5
                    $ game.set_flag("thugfight",1)
                else:
                    show danny fight win
                    "I try to punch the jerk, but he is faster than me."
                    "I get punched instead."
                    $ hero.grooming -= 5
                    $ hero.energy -= 5
                    $ hero.fun -= 5
                    thug_say "You're not worth the trouble bitch."
                    "He then spit on me and leaves."
                    hide danny
                    show audrey
                    audrey.say "Are you okay [hero.name] ?"
                    hero.say "I am fine, at least he left."
                    audrey.say "Thanks for the help."
                    hero.say "It was nothing."
            hide audrey
        "Don't get involved":
            hide audrey danny
            "I leave her to fend for herself"
    return

label audrey_event_02:
    show audrey
    $ audrey_love_max = 60
    $ audrey.set_flag("story",2)
    "About an hour before my shift was over I see Audrey."
    "I walk over to talk about what happened the other night."
    "Maybe invite her on a date."
    hero.say "Hey Audrey, what’s up?"
    "She turns to me looking less than amused."
    audrey.say "Hello [hero.name], shouldn’t you be working?"
    "She turns back to the coffee pot in the break room. Her shift hadn’t started yet."
    "Her ass looks so good in those jeans."
    "What am I doing? This is Audrey... and we are at work!"
    hero.say "Um yeah... I just wanted to ask you-."
    "She turns back to be, looking annoyed."
    audrey.say "Ask me what?"
    hero.say "Err... I just wanted to see what happened the other night?"
    audrey.say "What do you mean? I went home."
    audrey.say "Thanks for your help with that guy, I have to work now."
    "She brushes past me coldly and I’m so confused."
    "Is this the same Audrey that had been flirting with me everyday at work?"
    hero.say "Are- are you mad?"
    "She stopped in her tracks."
    audrey.say "Why would I be mad? I said thank you for helping."
    hero.say "No I mean about-."
    audrey.say "I don’t know what you are talking about."
    "She turns and walks away then, but there is still a sexy sway to her hips."
    hide audrey
    "What is going on here?"
    scene bg black
    with dissolve
    pause 1.0
    scene bg office
    with dissolve
    "I volunteer for overtime just to see what would happen with Audrey."
    "She wasn’t flirting with me like usually."
    "I wonder if I did something wrong."
    "Maybe I should bring her flowers?"
    "Then again she wasn’t flirting with any of the guys tonight."
    "I sigh and turn off my computer."
    show audrey
    "As I am walking out I see Audrey again and smile."
    hero.say "Hey-."
    "She promptly ran into me as if she hadn’t seen me, spilling her cold coffee down the front of me."
    hero.say "Hey!"
    audrey.say "Oh, sorry about that. Guess I didn’t see you there."
    hero.say "You really should be more-."
    "I notice that she leans toward me more, and I can see that she's not wearing a bra."
    hero.say "...careful."
    "I finish my sentence."
    audrey.say "I should be. I’m so clumsy. I guess I could take lessons from you."
    "She gives me a wink and my mind is spinning as she walks away."
    hide audrey
    "... Totally confused."
    return

label audrey_event_03:
    $ audrey_love_max = 80
    $ audrey.set_flag("story",3)
    $ audrey.set_flag("nokiss",False)
    "Damn I must have it bad."
    show audrey
    "That girl across the room looks like Audrey."
    "Wait."
    "It is Audrey!"
    "I think about jumping off to go say hello, but decide to watch for a moment instead."
    "She has tight short shorts on and a t-shirt that form fits to her breasts."
    "She gets on one of the bikes across from me, seeming to have not noticed I’m there yet."
    "She starts to peddle and my eyes fall down to her ass."
    "I like the way it moves and want to hold it in my hands."
    "I don’t know how long I have been staring when I suddenly realize there is a mirror in front of her."
    "And she is looking into it back at me with a smirk on her face."
    "I feel my face heat up along with my pulse picking up with embarrassment."
    "How long as she known I was staring?"
    "She gets off then and stretches her arms high over her head."
    "I see part of her stomach as her shirt goes up."
    "Then she bends over all the way to touch her toes with her feet shoulder width apart."
    "She has a thong on!"
    "Blue. She’s wearing blue tonight."
    menu:
        "Go over to Audrey":
            "I shut the treadmill off and hop off quickly."
            "I am standing just behind Audrey before I know it."
            hero.say "Hey."
            "She stands up suddenly as if she wasn’t expecting me to be there"
            "Maybe she didn’t see me?"
            show audrey blush
            audrey.say "Oh hey,"
            "She smirks."
            audrey.say "What are the odds of running into each other here?"
            "I find myself not knowing what to say and scanning her over."
            "I hear her laugh."
            audrey.say "Did you like the show?"
            "Okay so she did know I was watching her."
            hero.say "Yeah.. When do I get to see more?"
            "She is smirking again and reaches into her shirt."
            "My eyes go wide but then I see her pull out a piece of paper."
            "I take it thinking I have gotten her number and she walks away."
            hide audrey
            "I open it up."
        "Don’t go over to Audrey":
            "I decide not to go over to Audrey, wanting to see what more I can see."
            "But I am sadly disappointed when she stands up looking pissed."
            "She turns around and starts walking towards me."
            "I swallow hard because I don’t know what to expect."
            "When she stops right in front of me, and reaches down the front of her shirt I quickly shut off the machine."
            "Handing me a piece of paper."
            hide audrey
    show audrey note
    $ renpy.pause()
    hide audrey note
    "I look back up to see Audrey is already half away across the gym and try to wait until she is out of sight."
    "I try not to look like I am in a hurry to go find her."
    "I wave to one of by buddies and keep going, glad that I’m not finding anyone I have to stop to talk to."
    "I round the corner to the lock rooms and I try to look casual."
    "Before I know what is happening, I feel something hit the side of my face and my whole head turns to the side."
    show audrey
    "Holding the side of my face I look around furious and see Audrey in the shadows."
    "Audrey just slapped me!"
    "What the hell!"
    menu:
        "Show her who's the boss.":
            "I reach forward and grab a fistful of her hair on top."
            "Pushing her against the wall where no one can see us I growl"
            hero.say "What do you think you are doing, slapping me?"
            "With a smirk she says, "
            $ audrey.sub += 2
        "Be gentle":
            "I rub the side of my face, less angry that I know it is Audrey."
            "I calmly ask,"
            hero.say "Why did you slap me?"
            "Some of her cockiness slips but she says,"
            $ audrey.love += 2
    audrey.say "I was getting your attention. And that was for watching me for so long and not coming to say Hi."
    audrey.say "Come on, I wanta show you something."
    "She motions for me to follow her down a short hallway I hadn’t paid much attention to."
    "Even in the dark I can still see her hips sway."
    audrey.say "I found this a while ago. But haven’t had a chance to use it."
    "I get nervous wondering what she is talking about."
    "We come up to a green door and she opens it before flipping on the light."
    "It’s an old smaller version of one of the locker rooms."
    "As soon as I’m in she shuts the door and I hear her lock it behind us."
    "I feel my heart start to race as I start to wonder what she is hoping to get out of this."
    "I know what I want, but I doubt she has protection and I know I don’t."
    "I turn to her and she has taken her t-shirt of."
    audrey.say "Sorry, that old thing was all sweaty..."
    "Her voice was sexy and I was losing control of my thoughts."
    audrey.say "I hope you don’t mind."
    "She flutters her eyelashes at me."
    "I quickly shake my head."
    hero.say "Not at all."
    "Again with the no bra..."
    "She walks seductively over to me and wraps her arms around my neck."
    menu:
        "Take charge":
            "I instantly take charge."
            "I pick her up and she wraps her legs around my waist."
            "I back up until I feel the bench that is against the wall at the back of my knees and sit down with her in my lap as we make out."
            "I run my fingers through her hair roughly and hear her moun right before I slip my tongue into her mouth for the first time."
            "This was too good to be true."
            $ audrey.sub += 2
        "Be passive":
            "I decide to let her take charge."
            "She pushes me until I’m backed up against a bench on the wall and then she pushes me down to sit on it."
            "I watch eagerly as she climbs on top of me with one leg on either side of my lap."
            "She takes my face in both her hands and kisses me slowly at first."
            "Then it gets rougher."
            "She slides her tongue into my mouth and I get embarrassed at how fast I am getting hard."
            "Suddenly she lets go looking bored."
            $ audrey.sub -= 2
    "I hear her sigh as she pushes back."
    audrey.say "Wanta know what’s wet?"
    "I can’t believe she just asked me that."
    "I can’t help but smirk."
    hero.say "Sure."
    audrey.say "Waterparks."
    hero.say "What?"
    audrey.say "Waterparks. There’s one downtown."
    audrey.say "They’re one of my favorite things to do during the summer."
    audrey.say "Take me there and you might get lucky."
    audrey.say "Meet me there next saturday afternoon at 2pm."
    "She gets off of me then to go collect her shirt and slips it on over her head before leaving me there to wonder what the hell just happened, and how we got so close with nothing happening again!"
    hide audrey
    return

label audrey_event_04:
    $ audrey_love_max = 100
    $ audrey.set_flag("story",4)
    $ audrey.set_flag("nodate",False)
    play sound "sd/cell_vibrate.mp3"
    pause 1.0
    "It's a text from Audrey."
    audrey.say "Meet me at the waterpark, now."
    scene bg black
    with dissolve
    pause 1.0
    scene bg waterpark
    with dissolve
    "I stand next to the yellow fountain in the shade feeling unsure and stupid."
    "What if this was just a trick and she wasn’t really coming?"
    "Audrey had slipped me a note the other day finally to let me know when to meet her at the water park."
    "I check the time again, she still has a few minutes."
    show audrey blush
    "I look up and realize she is walking my way."
    "She has a red and black checkered bikini swimsuit top on, with what looks like black bikini bottoms."
    "My eyes are glued to her."
    audrey.say "Hey, nice to see you made it. I wanta go on that."
    "She points to one of the tallest roller coasters."
    "I am not exactly fond of rides that high but...."
    "I didn’t want her to think I was a wimp if I didn’t go."
    hero.say "Uh, sure. Let’s go see how long the line is."
    "I wasn’t sure at all what I was getting myself into, but she squeals."
    show audrey happy
    audrey.say "Come on!"
    "Grabbing my hand she pulls me along with her to go check out the ride."
    "Unfortunately, the line is short because it is still early."
    "Of course, part of the deal was that I pay for everything, so when we got up front I gave the man the tickets."
    "It is still too early to buy wristbands."
    "In no time we are being strapped in."
    audrey.say "This is going to be fun."
    "Without warning I feel her grab my crotch and I tense."
    "She gives it a squeeze but then quickly lets go when then worker walks by."
    "I was confused as to which part she thought was fun."
    "Is she wanting me to touch her?"
    "I look around but I don’t have the nerve she does. So I wait until the ride starts moving."
    "Once we are in a dark tunnel, I take one hand off the bar and place it on her leg, sliding my hand up to tight."
    menu:
        "Slide hand up":
            "Slowly, as the ride pick up speed I slip my hand up toward her bikini bottom."
            "She doesn’t stop me so I keep going."
            "When I reach as high as I can I start to rub my thumb against the top of her leg and she presses her leg up against mine to encourage me."
            "I move to do more, but suddenly the tunnel ends and I am forced to grab onto the bar tight with both hands as we plunge several hundred feet downward."
            $ audrey.sub += 1
        "Don’t slide hand up":
            "I chicken out and decide not to feel her up."
            "I glance at her and she seems to be waiting for something."
            "I don’t know what to do and she seems to be getting impatient."
            "Just when I decide to do something the tunnel ends and I am forced to grab onto the bar tight with both hands as we plunge several hundred feet downward."
    "I hear a her let out a scream and I think about how I wish I was what was making her scream."
    audrey.say "[hero.name], this is aaaaaaaamazzzzzzing!"
    "Before I could answer we slashed down into the first pool of water. Now that I have to admit is cool."
    "Plus it gave me an idea."
    "I wonder if since she likes waterparks, if I could get her to do it in a pool?"
    "Just as quickly as we hit the water we were going back up and sideways several hundred feet."
    "By the time the ride was over we were both soaked and our limbs felt weak."
    "She hop out of the ride and giving me no time at all tells me,"
    audrey.say "I wanta go again! But on that one over there!"
    "This girl was going to wear me out. At least this one doesn’t seem as high."
    scene bg black
    with dissolve
    pause 1.0
    scene bg waterpark
    with dissolve
    "By the end of the day I think we have hit every roller coaster there is."
    "We step away from the one we just got of and Audrey grabs my hand for the first time since we first got there."
    audrey.say "Come here."
    "I don’t have a choice but to follow, and she leads me to a quiet area behind one of the rides where no one can see us."
    "I see a bench and walk over to it to sit down with her."
    "She leans in so I do the same."
    "Again, just like when we were in the gym locker room we are a tangle of hair and limbs."
    menu:
        "Feel her up":
            "I start to slide my hand up her leg but she slaps it away."
            audrey.say "Not in public."
            $ audrey.sub += 1
            menu:
                "Keep going":
                    hero.say "I'll do whatever I want."
                    "She seems to decide that I can and let me."
                    $ audrey.sub += 1
                "Stop":
                    "I’m disappointed but I decide to enjoy the kiss at least."
        "Don’t feel her up":
            "I decide it’s too dangerous to try and feel her up right now, someone might see us and call security."
            "Kissing is good enough."
    "Just when I think I can’t breath she pulls back."
    "I hear her sigh."
    audrey.say "Well, that was not a half bad date."
    audrey.say "You can try and invite me on more of those."
    "I have a board smile on my face until I hear her say."
    audrey.say "But don't bring me on lame ones."
    "My smile fell and I watch as she goes."
    "Somehow I feel like an idiot again."
    hide audrey
    $ game.room = "map"
    return

label audrey_gay_mistake:
    show audrey
    audrey.say "Hey gorgeous, how's it going?"
    hero.say "Mindlessly typing on a keyboard under fluorescent lights..."
    hero.say "does it get better than this?"
    audrey.say "Question. You're not dating anybody, are you, because I met somebody who would be perfect for you."
    hero.say "Ah, y'see, perfect might be a problem. Had you said 'co-dependent', or 'self-destructive'..."
    audrey.say "Do you want a date Saturday?"
    hero.say "Yes please."
    audrey.say "Okay. He's cute, he's funny, he's-"
    hero.say "He's a he?"
    audrey.say "Well yeah!"
    audrey.say "...Oh God. I- just- I thought- Good, Audrey."
    audrey.say "I'm just gonna go flush myself down the toilet now..."
    audrey.say "Okay, goodbye..."
    $ audrey.love += 1
    $ game.set_flag("gaymistake",1)

    return

label audrey_talk_breakup:
    show audrey
    audrey.say "I heard that you had a bad break up in high school?"
    hero.say "Yeah, but you know what the scariest part is?"
    hero.say "What if there's only one woman for everybody, y'know?"
    hero.say "I mean what if you get one woman- and that's it?"
    audrey.say "What are you talking about?"
    audrey.say "'One woman'?"
    audrey.say "That's like saying there's only one flavor of ice cream for you."
    audrey.say "Lemme tell you something, [hero.name]."
    audrey.say "There's lots of flavors out there."
    audrey.say "There's Rocky Road, and Cookie Dough, and Bing! Cherry Vanilla."
    audrey.say "You could get 'em with Jimmies, or nuts, or whipped cream!"
    audrey.say "This is the best thing that ever happened to you!"
    audrey.say "Welcome back to the world!"
    audrey.say "Grab a spoon!"
    hero.say "I honestly don't know if I'm hungry or horny."
    $ audrey.love += 1
    hide audrey
    return

label audrey_help_at_work:
    show audrey
    audrey.say "[hero.name], could you help me with something ?"
    $ result = renpy.display_menu([("Sure",1),("No, I don't have time",2)])
    if result == 1:
        show audrey work happy
        audrey.say "Thank you. I am cleaning up the archive room."
        "Fuck, that will take a while..."
        "We clean the archive room together."
        $ game.pass_time(needs = True)
        $ audrey.love += 1
        audrey.say "Thank you [hero.name].."
    else:
        show audrey work angry
        audrey.say "Thanks for nothing then."
        $ audrey.love -= 1
    hide audrey
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
