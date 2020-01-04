init python:
    Event(**{
        "name": "bree_about_kiss",
        "label": ["bree_about_kiss"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"room":["bathroom","bedroom2"], "flag_female":0, "valid":True},
        "girls_conditions": {"bree":{"max_love":80,"flagmin_kiss": 1,"present":True}},
        "do_once": True,
        "quit": False
        })

    Event(**{
        "name": "bree_talk_breakup",
        "label": ["bree_talk_breakup"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"bree":{"min_love":80, "present":True, "valid":True}},
        "game_conditions":{"flag_female":0},
        "do_once": True
        })

    Event(**{
        "name": "bree_get_out",
        "label": ["bree_get_out"],
        "duration": 0,
        "priority": 1000,
        "game_conditions":{"room":["bathroom","bedroom2"], "flag_female":0},
        "girls_conditions": {"bree":{"max_love":139,"clothes": "naked", "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": False,
        "once_hour": False,
        })

    Event(**{
        "name": "bree_get_out_2",
        "label": ["bree_get_out"],
        "duration": 0,
        "priority": 1000,
        "game_conditions":{"room":["bathroom","bedroom2"], "flag_female":0},
        "girls_conditions": {"bree":{"max_love":99,"clothes": ["underwear","towel"], "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": False,
        "once_hour": False,
        })

    Event(**{
        "name": "bree_not_get_out",
        "label": ["bree_not_get_out"],
        "duration": 0,
        "priority": 200,
        "game_conditions":{"room":["bathroom","bedroom2"], "flag_female":0},
        "girls_conditions": {"bree":{"min_love":140,"clothes": "naked", "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": True,
        })

    Event(**{
        "name": "bree_not_get_out_2",
        "label": ["bree_not_get_out_2"],
        "duration": 0,
        "priority": 200,
        "game_conditions":{"room":["bathroom","bedroom2"], "flag_female":0},
        "girls_conditions": {"bree":{"min_love":100,"clothes": ["underwear","towel"], "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": True,
        })

    Event(**{
        "name": "bree_give_birthday",
        "label": ["bree_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday", "flag_female":0},
        "girls_conditions": {"bree":{"min_love":40,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "bree_give_valentine",
        "label": ["bree_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine", "flag_female":0},
        "girls_conditions": {"bree":{"min_love":100,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "bree_kiss_me",
        "label": ["bree_kiss_me"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"bree":{"min_love":150,"present":True, "valid":True}},
        "game_conditions":{"flag_female":0, "chances":20},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "bree_give_christmas",
        "label": ["bree_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas", "flag_female":0},
        "girls_conditions": {"bree":{"min_love":50,"present":True, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "bree_event_01",
        "label": ["bree_event_01"],
        "duration": 1,
        "game_conditions":{"room":["livingroom"], "flag_female":0},
        "girls_conditions": {"bree":{"activity":"play", "min_love":20,"present":True}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "bree_event_02",
        "label": ["bree_event_02"],
        "duration": 1,
        "game_conditions":{"room":["arcade"], "flag_female":0},
        "girls_conditions": {"bree":{"min_love":40,"present":True, "flageq_story":1}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "bree_event_03",
        "label": ["bree_event_03"],
        "duration": 1,
        "game_conditions":{"room":["livingroom"], "hours":(10,19), "flag_female":0},
        "girls_conditions": {"bree":{"min_love":60,"present":True, "flageq_story":2}},
        "required_item": "zbox 360",
        "priority": 500,
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "bree_event_04",
        "label": ["bree_event_04"],
        "duration": 2,
        "game_conditions":{"hours":(12,18),"days":"12345", "chances":10,"flag_dateinprogress":0, "flag_female":0},
        "girls_conditions": {"bree":{"min_love":80, "flageq_story":3}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })          


    Event(**{
        "name": "bree_event_05",
        "label": ["bree_event_05"],
        "duration": 2,
        "game_conditions":{"hours":(18,20),"days":"123456", "activity":"interact","room":["livingroom"], "skill":"video_games", "flag_female":0},
        "girls_conditions": {"bree":{"min_love":100, "flageq_story":4}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })          

    Event(**{
        "name": "bree_event_05b",
        "label": ["bree_event_05b"],
        "duration": 2,
        "game_conditions":{"hours":(9,22),"room":["secondfloor","bedroom2"], "flag_female":0},
        "girls_conditions": {"bree":{"min_love":100, "room":"bedroom2", "flagmin_story":4}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })          

    Event(**{
        "name": "bree_event_06b",
        "label": ["bree_event_06b"],
        "duration": 2,
        "game_conditions":{"hours":(18,22),"room":["livingroom","kitchen"], "flag_female":0, "done":"bree_event_05b"},
        "girls_conditions": {"bree":{"min_love":120, "room":"bedroom2"}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })          

    Event(**{
        "name": "bree_event_07b",
        "label": ["bree_event_07b"],
        "duration": 2,
        "game_conditions":{"hours":(12,18),"days":"12345","room":["map"], "flag_female":0, "done":"bree_event_06b"},
        "girls_conditions": {"bree":{"min_love":130}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })          

    Event(**{
        "name": "bree_pool_throat",
        "label": ["bree_pool_throat"],
        "duration": 0,
        "game_conditions":{"activity":"swim_pool_home","hours":(9,19), "flag_female":0},
        "girls_conditions": {"bree":{"min_sub":50, "flagmin_sex":1}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })   

    Event(**{
        "name": "bree_event_bowsette",
        "label": ["bree_event_bowsette"],
        "duration": 1,
        "game_conditions":{"hours":(18,20),"days":"12345","room":["secondfloor","bedroom2"], "days_played":21, "flag_female":0},
        "girls_conditions": {"bree":{"min_love":100, "room":"bedroom2"}},
        "priority": 500,
        "do_once":True,
        "quit": True
        })       

    Event(**{
        "name":"bree_talk_preg",
        "max_girls": 1,
        "label": ["bree_preg_talk"],
        "duration": 0,
        "do_once": False,
        "girls_conditions": {"bree":{"flag_pregtest":1, "active":True}},
        "game_conditions": {"activity":"interact"}
        })

    Event(**{
        "name":"bree_preg_test",
        "max_girls": 0,
        "label": ["bree_preg_test"],
        "duration": 0,
        "do_once": False,
        "girls_conditions": {"bree":{"flagmin_pregnant":6,"flag_pregtest":0}},
        "game_conditions": {"hours":(6,11),"room":["bathroom"]}
        })

    Event(**{
        "name": "bree_pregnant_flag",
        "label": ["bree_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"bree":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })


    Event(**{
        "name": "bree_gone",
        "label": ["bree_gone"],
        "duration": 0,
        "girls_conditions": {"bree":{"flag_gone":True,"flag_goneDelay":False}},
        "do_once":False,
        "quit": False,
        })


    Event(**{
        "name": "bree_anal_confession",
        "priority": 500,
        "label": ["bree_anal_confession"],
        "duration": 0,
        "game_conditions":{"activity":["interact"], "flag_female":0},
        "girls_conditions": {"bree":{"present":True,'valid':True, "active":True, "flag_anal":1}},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "bree_ending",
        "priority": 500,
        "label": ["bree_ending"],
        "duration": 0,
        "game_conditions":{"days":"56", "flag_female":0},
        "girls_conditions": {"bree":{'valid':True, "flag_engagedmike":1}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name":"bree_shower_BJ",
        "label": ["bree_shower_BJ"],
        "duration": 1,
        "game_conditions": {
            "activity":["shower"],
            "flag_female":0,
            "hours":(20,25)
            },
        "girls_conditions": {"bree":{"min_love":150,"present":True, "valid":True, 'flagmin_sex':1, 'min_sub':50}},
        "once_week": True,
        "once_day": False,
        "do_once": False,
        "quit": True
        })

label bree_ending:
    $ game.hour = 16
    if sasha.get_flag_value("engagedmike") and game.get_flag_value("homeharem"):
        jump sasha_bree_ending
    show bg church
    "There was a time when I'd have thought that a church wedding with all of the gaudy trimmings and traditional trappings was something I would avoid at all costs."
    "But I guess that a lot's changed, in terms of both myself and my life in recent times, enough to make me rethink a lot of the assumptions I made in the past."
    "What am I even trying to say here?"
    "It's Bree that's changed me and my life, a great deal and all for the better!"
    "She's the reason that I'm standing at the altar in such a grand church, done up in a fancy suit and listening to the music playing that's supposed to accompany her down the aisle."
    "Everything about the wedding that we've planned is inspired by her, not that she'd be aware of that fact."
    "Me, well...I'm kind of a retiring type."
    "What's officially my side of the church is nowhere near filled by the few members of my family and close friends that I cared to invite."
    "By way of contrast, Bree's side is so full that guests are spilling over into the empty pews on the other."
    "Friends from as far back as her childhood and right up to the present day are crammed in next to a procession of relatives that never seems to end."
    "It honestly didn't look like this many people when we sat down to put the guest list together!"
    "But that's just my point - Bree takes me out of my rut, puts me somewhere that I can't predict, she makes my life vital and exciting."
    "I mean it when I say that I can genuinely feel my heart racing, as I look back over my shoulder for the first glimpse of her entering the church."
    show bree wedding blush
    "And there she is..."
    "Ah...I...wow!"
    "Sorry about that - it's just that, what with Bree being such a stickler for tradition, she kept me from seeing the dress she's chosen until this very moment."
    "And I'm glad that she did, because she looks simply stunning."
    "I honestly can't remember how the kids and young teenagers that make up her bridal party are related to her or what any of their names are."
    "They could not be there at all for the tiny amount of attention that I can spare for them."
    "Right now, Bree's the only person that I want to lay eyes on."
    if not bree.get_flag_value("pregnant") >= 9:
        "I'm surprised to see that, despite being fond of tradition, Bree's chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The expression on my face must be as easy to read as words on a page, making Bree blush a little as she reaches my side."
        "Though my hand was supposed to be in my pocket to keep hold of the ring, I find myself now using it to pinch myself on the thigh instead."
        "Part of me just can't believe this is actually happening!"
    else:
        "I'm surprised to see that, despite being fond of tradition, Bree's chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The dress has been tastefully cut to accommodate the curve of Bree's belly, and so this only adds to her radiance."
        "That's one thing that neither of us is old fashioned about."
        "We both take delight in being reminded of the fact that we're expecting our first child together."
    "I'm about to say something to her, compliment the dress or make a comment about how good she looks."
    "But then there's a discreet cough, and I glance around to see the priest smiling and glancing at his watch."
    "I look back to Bree, who has an amused grin on her face, clearly aware that I was taken completely out of the moment at the sight of her."
    "She shakes her head in a gesture of affection, and we both turn to face the priest, with me at least trying to look prepared for what lies ahead."
    "But I needn't have worried, as the whole thing comes off as smoothly as it did in the rehearsal."
    "In fact, once we've exchanged out vows and then the rings, it take me a few seconds to realise that it's for real this time."
    "Bree and I are actually now husband and wife!"
    show bree kiss wedding
    "When the time comes to kiss the bride, I don't do anything dramatic, like bending her over backwards."
    "Instead we kiss with a brief, understated brush of the lips."
    "But the electricity I feel as we do so is worth more than any amount of unrestrained Frenching."
    hide bree
    show bree wedding happy
    "All of the usual stuff follows the actual ceremony - throwing the bouquet over the shoulder, tossing confetti and the like."
    "For me, all of it's a blur, things that I'll need Bree to talk me through when we get hold of the wedding album."
    "It's all I can do to tear my eyes away from her for more than a couple of seconds at a time."
    "Maybe I'll soon get used to the fact that the girl who was once only my housemate, then my friend and lover is now my wife."
    "But I don't think I'll ever be able to take someone as amazing as Bree for granted, no matter how long she happens to be a part of my life."
    scene bg park
    show bree ending bree
    with fade
    bree.say "Bet you were thinking that this was the end of the story, and you were gonna hear from [hero.name] again to wrap it all up, huh?"
    bree.say "Well, surprise - you were wrong twice over!"
    bree.say "This is as much my story as it is [hero.name]'s, and I can assure you that it's far from over."
    bree.say "Sure, it took us a while to get here, and there were some bumps along the way."
    bree.say "But I don't think that I'd change anything, even if someone told me that I could."
    bree.say "Those bumps will become fond memories soon, and we'll laugh about them when we look back."
    bree.say "We have the rest of our lives to look forward to, and I'm going to make sure that we live every day to the full."
    bree.say "I'll admit, when I first moved into the house with him, that I maybe didn't appreciate [hero.name] as much as I should have."
    bree.say "He was sweet and looked pretty cute, but I guess I was in a fuss about living in a new place with new people."
    bree.say "So it kind of took me a while to notice him in that way, which meant that he grew on me a little at a time."
    bree.say "By the time I realised he was sneaking his way into my affections, it was too late!"
    bree.say "And now I can't imagine what life would be like without him."
    bree.say "Sure, he's a typical guy most of the time, forgetful, messy and with his mind always on the one thing a guy's mind is always on."
    bree.say "But he's also sensitive, caring and he makes me feel like I'm the thing that he wants most in the world."
    bree.say "So you don't need to remind me, as I know just how lucky I am to have found him."
    bree.say "After the wedding and the honeymoon, we came back to the house."
    bree.say "And for a little while at least, things felt like they were pretty much back to normal."
    bree.say "But somehow we all knew that the old times were gone, no matter how much we hated to admit it."
    bree.say "Somehow the place felt crowded now, even though there were still only three of us under the same roof."
    if not bree.get_flag_value("pregnant"):
        bree.say "Sasha never said as much out loud, but I think that we were cramping her style."
        bree.say "It's hard to be the spare wheel when the other people in the house do everything as a couple."
        bree.say "So she moved out a couple of months after the wedding and found a place of her own."
        bree.say "We still see her every now and again, though not as often as either of us would like."
        bree.say "But I can't hide the fact that part of me likes the fact we now have the house to ourselves."
        bree.say "It makes me feel like a wife from one of those silly, old-fashioned soap operas!"
    else:
        bree.say "Sasha never said as much out loud, but I think that we were cramping her style."
        bree.say "It's hard to be the spare wheel when the other people in the house do everything as a couple."
        bree.say "And when Poppy was born...well, that pretty much sealed the deal for her."
        bree.say "So she moved out a couple of months after the wedding and found a place of her own."
        bree.say "We still see her every now and again, though not as often as either of us would like."
        bree.say "But I can't hide the fact that part of me likes the fact we now have the house to ourselves."
        bree.say "I feel like we're a perfect little family unit!"
    bree.say "Is there much more to say than that?"
    bree.say "I mean, no one wants to be bored with details of what's happened to [hero.name] at work or me at uni, do they?"
    bree.say "It's like the way that you never see anyone use the toilet in a movie."
    bree.say "This is the part of the story where you want a montage of happy scenes, like snapshots of our lives, right?"
    bree.say "Well, how about a nice image of us, strolling through the park on a lovely summer day?"
    bree.say "That kind of sums it all up neatly, if you ask me."
    bree.say "We're smiling and laughing while the sun's beating down on us and times are good."
    bree.say "But if the sun goes behind the clouds or the rain starts to come down, then we can huddle together and smile at the memories we've made together."
    $ renpy.full_restart()

label sasha_bree_ending:
    show bg beach
    "While it's a pretty romantic choice of location, none of us would have settled on getting married on the beach had it not been for the rather unique nature of the wedding that we were planning."
    "For a start, there are three of us involved in this relation ship, which means three rings, three wedding outfits and three lots of guests to be accommodated on the big day."
    "Sure, we might have been able to find a church or a civil venue that could have handled all those people without looking too hard."
    "But when there's two brides and one groom, what side of the aisle are people even supposed to sit on?"
    "On top of all that, we also had the issue of being one of the first trios (well, we're not a couple now, are we?) to get married under the new polygamy laws."
    "The fuss hasn't died down over them yet, and the press have been hungry for weddings involving three individuals that they can turn into a sensational story."
    "None of us wanted that to happen either, and so a remote stretch of the beach that was well of the beaten track seemed to be a sensible choice."
    "We had to spend a lot of time figuring out just who would go where for the ceremony as well."
    "Should we all be at the front of the congregation to begin with?"
    "Should we all come down the aisle together?"
    "Or should we come down one at a time, and if so, in what specific order?"
    "In the end, for the sake of simplicity, that I would stand at the head of the congregation, like a traditional groom, while Bree and Sasha walked up the aisle together."
    "They justified this to me by saying that neither of them wanted to upstage the other on their big day."
    "But a large part of me thinks that it had more to do with them wanting to make a show of numbers and remind me that I'm the minority gender in this relationship!"
    "So here I am, standing with the eager crowd of guests behind me and nothing in front of me, save for the priest and the view out to sea."
    "Just as I think that I can feel the nerves starting to set in, the band starts to play."
    "Instantly I recognise the tune that Bree and Sasha settled on coming down the aisle to."
    "And I damn well should, as it took almost a month of arguing and negotiation to eventually come to a compromise!"
    "Turning to watch their approach, I see the crowd part roughly down the middle to allow my two brides to walk to where the priest and I are awaiting them."
    show bree wedding blush at left
    show sasha wedding blush at right
    if not bree.get_flag_value("pregnant") >= 9 and not sasha.get_flag_value("pregnant") >= 9:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, Bree's chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red above flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebon hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    elif bree.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("pregnant") >= 9:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, Bree's chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The dress has been tastefully cut to accommodate the curve of Bree's belly, and so this only adds to her radiance."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red, cut to be sympathetic to the curve of her swelling belly."
        "Below are flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebon hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    elif bree.get_flag_value("pregnant") >= 9 and not sasha.get_flag_value("pregnant") >= 9:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, Bree's chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The dress has been tastefully cut to accommodate the curve of Bree's belly, and so this only adds to her radiance."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red above flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebon hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    elif not bree.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("pregnant") >= 9:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, Bree's chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red, cut to be sympathetic to the curve of her swelling belly."
        "Below are flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebon hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    "Seeing them walking towards me, their arms intertwined, I'm reminded of the fact that Bree and Sasha are as much marrying each other as they are me."
    "So it's heart-warming to see how close they are and how natural they look together, a beautiful sight to see."
    "And I don't just mean that in carnal sense either - we've grown so close as a trio that we have a true bond now."
    "When I say that we love each other, I mean it in every possible sense of the word."
    "Of course, the ceremony takes a little longer than it would for a couple getting wed."
    "There's an extra set of vows and questions to be asked, but they're longer than they would otherwise be."
    "After all, we're making a declaration of faithfulness and commitment to two other people, rather than one."
    "I can almost hear the guests straining to listen for every unique word and phrase used in the ceremony and then whispering to each other with curiosity."
    "In truth, I can't blame any of them for being so intrigued."
    "I'm intrigued myself, only more as to what happens after the ceremony than during it!"
    "We exchange rings by each putting one onto the finger of one of the others and pushing them on at the same time."
    "I don't know if the guests pick up on the symbolism of this gesture."
    "But we wanted it to show us binding ourselves together, each binding themselves to the others."
    priest_say "I now declare you husband and wives - you may kiss...well...each other!"
    "Bree, Sasha and I wrap our arms tightly around each other, pulling our bodies close and placing our lips together in a three-way kiss."
    "As the girls...no, I mean my wives - wow, that's going to take some getting used to!"
    "As my wives toss their bouquets to the clapping and cheering guests, it strikes me how far we've come and how much has changed."
    "When we met, this wouldn't have been legal, let alone believable."
    "Bree, Sasha and I have gone from housemates, to friends and then to lovers, finally committing our lives to one another."
    "I honestly have no idea as to just what the future might hold for us."
    "But if it's even half as exciting as the journey that got us here, it'll be well worth looking forward to."
    scene bg park
    show bree ending bree sasha
    with fade
    bree.say "So, hey...yeah...it's me, [hero.name]."
    bree.say "You know, the hero of this whole story?"
    sasha.say "That's so funny, Bree - you sound just like him!"
    bree.say "Uh...yeah - I'm gonna wrap up this whole thing, and tell you how it is!"
    bree.say "And then, I'm gonna fart, and blame it on Sasha and Bree - like I always do!"
    sasha.say "Okay...okay...it's us - it's Sasha."
    bree.say "And Bree!"
    sasha.say "We thought that [hero.name] had been telling his side of the story for too long already."
    bree.say "Yeah, too right!"
    bree.say "And seeing how it's now our story too, we think that we at least deserve to have the last word on it."
    sasha.say "This is the point where, I guess, we're supposed to say something deep and philosophical about married life."
    bree.say "Or get all teary-eyed over the journey that we took to get where we are right now."
    sasha.say "But that sounds pretty boring to us, so we won't."
    bree.say "We think you're far more interested in hearing all about what it's like to live in a threesome."
    bree.say "Am I right?"
    sasha.say "Well, no one ever sat down and wrote a book about it."
    sasha.say "So after the wedding was over, we were pretty much left to figure it out for ourselves."
    bree.say "We kept doing most of the same fun stuff that we'd been doing before we were married."
    bree.say "But with the added bonus that we didn't have to hide it any more!"
    sasha.say "In a lot of ways, we're just like an ordinary married couple."
    sasha.say "We eat out and go to the movies, argue about who's turn it is to put out the rubbish."
    bree.say "And then we have make-up sex, which is almost worth starting an argument for in the first place!"
    bree.say "But it's different too..."
    bree.say "Like if two of us fall out over something, there's always another head to see both sides and mediate."
    sasha.say "And you're not often lonely either."
    sasha.say "Chances are that if one of us is working late or cramming into the night for an exam, the other two are curled up on the sofa together."
    bree.say "Hey, Sasha - I bet that last one had everyone imagining us two being the lonely ones, and [hero.name] tied up somewhere else!"
    sasha.say "You mean people are wondering if we have fun together while [hero.name]'s away?"
    bree.say "Uh-huh!"
    sasha.say "Well, there are some things that should remain a secret - part of the sanctity of marriage!"
    sasha.say "So they can just go on wondering!"
    if not bree.get_flag_value("pregnant") and not sasha.get_flag_value("pregnant"):
        bree.say "We still live in the same house together."
        sasha.say "But we have been talking about saving up to put a deposit down on something we can one day own."
    elif bree.get_flag_value("pregnant") and sasha.get_flag_value("pregnant"):
        bree.say "We still live in the same house together."
        sasha.say "But that's mainly because I was expecting Dahlia so soon after the wedding."
        bree.say "And don't forget I was almost as far on with Poppy at the same time too!"
        sasha.say "So with two baby girls on the way so close together, moving was out of the question!"
    elif bree.get_flag_value("pregnant") and not sasha.get_flag_value("pregnant"):
        bree.say "We still live in the same house together."
        sasha.say "Mainly because we thought you were going to pop any second after the wedding!"
        bree.say "With Poppy on the way, moving was out of the question!"
    elif not bree.get_flag_value("pregnant") and sasha.get_flag_value("pregnant"):
        sasha.say "We still live in the same house together."
        bree.say "Mainly because we thought you were going to pop any second after the wedding!"
        sasha.say "With Dahlia on the way, moving was out of the question!"
    bree.say "We all still talk about just how weird it is - that things turned out like this."
    bree.say "It was total chance that Sasha and I both moved into the same house that [hero.name] was already living in."
    sasha.say "More than that, what are the chances that two of us out of the three would have hit it off so well as to start a relationship - let alone all three of us becoming involved?"
    sasha.say "And even then, it working for anything more than a quick fling before blowing up in our faces!"
    bree.say "I guess that it was just written in the stars, that it was meant to be!"
    sasha.say "Urgh...let's just say that it was a freakily rare thing, and we're lucky to have something so special!"
    bree.say "If you say so, Miss Misery-Guts!"
    sasha.say "Right back at you, Sugar-Coated Snot!"
    bree.say "Love you!"
    sasha.say "Yeah, I love you too!"
    $ renpy.full_restart()

label bree_anal_confession:
    $ bree.set_flag("anal",2)
    show bree blush
    "I would have just written it off as nothing more than a typically casual conversation with Bree, save for the fact that she really wasn't saying anything at all."
    "Some people have a habit of babbling like that, but with her, there's usually some kind of point that she gets to in the end."
    "But not today, as she seems to be flitting from one subject to another with no actual interest in what she's actually saying."
    "In the end, I can't take it anymore and just want to hear what's really on her mind."
    hero.say "Bree, is there something that you wanted to say?"
    bree.say "Ah, well...yeah, there kinda was."
    bree.say "It was about the other night..."
    "This could be bad - but then what could be so bad that she have needed to wait all of this time to bring up?"
    hero.say "What about the other night?"
    "Bree's blushing now and faltering as she tries to get her words out."
    hero.say "Did I do something that upset you, Bree?"
    bree.say "No, no...I'm just...embarrassed to talk about it, that's all!"
    "Now I think I understand where she's wanting to go with this."
    hero.say "I'm sorry that we ended up doing it that way, Bree."
    hero.say "I wasn't lying when I said it was an accident...at least at first."
    "Bree shakes her head, finally seeming to find the courage to explain herself completely."
    bree.say "Oh no, I'm not angry about it!"
    bree.say "Just the opposite, really..."
    "She can hardly meet my eye as she admits this, her cheeks still burning with the shame it's making her feel."
    hero.say "You mean...you liked it when I took you up the ass?"
    "Bree bites her lip as she nods."
    bree.say "I...I liked it...a lot."
    "Wow - Bree just found out that she's a dirty little girl, and that she loves it!"
    "Is it just me, or did it suddenly get hotter in here?"
    hero.say "So did I, Bree - you were pretty amazing!"
    "She looks up at me, genuine surprise in her eyes at this unexpected praise."
    bree.say "I...I was?"
    "I'm not lying just for the sake of encouraging her, she really was!"
    hero.say "Bree, fucking your ass was incredible!"
    "She smiles at this, clearly loving the fact that I said so, but still feeling that she should be ashamed of herself for it."
    bree.say "Would...would you like to...fuck my ass again some time?"
    hero.say "Bree, it would be my pleasure!"
    "The look of satisfaction and excitement on Bree's face is enough to make me want to take a cold shower."
    "But the thought of what she just asked me to do is not something that's going to be washed away do easily."
    return

label bree_gone:
    if "bree" in HIDDEN:
        $ HIDDEN.remove("bree")
    $ bree.set_flag("gone",False)
    return

label bree_pregnant_flag:
    $ bree.set_flag("pregnant",1,mod="+")
    return

label bree_preg_test:
    scene bg bathroom
    "I walk into the bathroom groggily, my eyes still heavy from waking up only minutes ago."
    "Flicking the lightswitch, I squint at the bright light that reflects off of the ceramic tile."
    "I rub my face, trying to rid whatever tiredness I have left. I set some extra clothes I brought with me on the sink and turn on the shower."
    "It takes a minutes before it heats up, putting my hand under the water to check the temperature."
    "I step in, letting the heat run over my shoulders. Steam rises to the ceiling and fogs the mirror."
    "Once I manage to relax, the rest of the shower takes no time at all."
    "I don’t want to get out, but I step onto the fuzzy rug anyway, grabbing a towel and wrapping it around my waist."
    "I take another towel from the rack and dry my hair."
    "When I’m done and as dry as I’ll get myself I throw on my clothes for the day."
    "I go to brush my teeth, but find my toothbrush buried between hair products and other things I don’t really recognize."
    "Ever since Bree and Sasha moved in, I’ve been finding their stuff everywhere I look."
    "I don’t completely mind, but when I can barely find my own things underneath, it starts to get annoying."
    "Once I spot my toothbrush, I make a move to grab it along with the paste."
    "As I pull back, my wrist hits a small container filled with some sort of lotion. I try to grab it as it falls, but I miss and I wince as it hits the floor."
    "I set my brush down and crouch to see where it landed. I can’t find it."
    "Maybe it’s behind the trash can? I push it aside and don’t see it either. I’m about to stand back up, but see it inside the trash."
    hero.say "Shit."
    "I quickly take it out and set it back on the counter."
    "As I lift it, something catches my eye- a white stick poking out between a few tissues. Without thinking, I grab that too."
    "I inspect the stick closer. A pregnancy test? Who’s was this?"
    "My brain immediately goes back to when I had sex with Bree. This couldn’t be…?"
    "I can hear my heartbeat in my ears, my anxiety shooting up."
    "If it was, then I had no idea what I would do. I flip the thing over to see the results. Two stripes."
    "How long has this been going on?"
    "I jump when I hear a knock on the bathroom door."
    sasha.say "Hey! How long are you going to be in there for?"
    hero.say "Uh- sorry!"
    "I call back to her and open the door."
    scene bg secondfloor
    show sasha towel
    "The cold air from the hallway hits me and makes me shiver."
    "I shove the test into my back pocket before she can see."
    "Her arms are crossed, looking annoyed."
    sasha.say "Are you done?"
    hero.say "Yup. Go ahead."
    "She nods and pushes past me for her turn in the bathroom."
    hero.say "Wait!"
    "She stops before closing the door. Sasha raises an eyebrow."
    hero.say "You haven’t… taken a pregnancy test lately, have you?"
    "No other way to really say it, but I have to know. Sasha stares at me, eyes full of suspicion."
    sasha.say "No. Why?"
    hero.say "Just asking."
    $ bree.set_flag('pregtest',1)
    return

label bree_preg_talk:
    show bree sad
    hero.say "Bree?"
    "Her blonde hair whips around as she turns to look behind her."
    "Her eyes are rimmed red, her cheeks wet with tears."
    "She attempts to compose herself, but her smile falls as soon as she tries."
    "I take a seat next to her, not knowing what to say."
    hero.say "What’s wrong?"
    "I’m pretty sure I know what’s wrong."
    bree.say "..."
    hero.say "I just… wanted to talk to you."
    bree.say "I need to talk to you too."
    "I nod, and start taking the pregnancy test out of my pocket."
    bree.say "I- I… went to the pharmacy yesterday-"
    "Before she can finish, I hand her the white stick."
    "She stares at it for a moment then bursts into tears."
    bree.say "I’m so sorry."
    menu:
        "You have nothing to be sorry about.":
            hero.say "You don’t have anything to be sorry about."
            show bree normal
            "Bree slowly lifts her head."
            bree.say "You’re not mad?"
            hero.say "Why would I be mad?"
            bree.say "I don’t know! Because we never talked about having kids."
            bree.say "I can barely afford rent and you need roommates."
            bree.say "We’re not even married!"
            hero.say "..."
            "She has a point. We’re not exactly prepared for a baby."
            hero.say "That doesn’t mean we can’t try."
            bree.say "... For real?"
            hero.say "Yeah."
            show bree happy
            "Her eyes start to well up again. She lunges forward and pulls me into a hug and I hug her back, squeezing her tightly."
            "Going through with this would be a struggle, but it would be worth it if I could do it with her."
        "You should have told me.":
            $ bree.love -= 25
            hero.say "Why the hell wouldn’t you tell me right away?!"
            "Bree winces as I raise my voice, but I can’t help the irritation that rises in my chest."
            bree.say "I’m sorry."
            hero.say "This isn’t something you just keep to yourself!"
            bree.say "I wasn’t going to! I was going to tell you."
            hero.say "When?!"
            bree.say "I don’t know! When I was ready!"
            "Her face is turning red, the color crawling down her neck."
            bree.say "You can’t just like yell at me for this!"
            menu:
                "I’m sorry.":
                    "I purse my lips and force myself to calm down. She was right. I may be upset, but I can’t really imagine how she must be feeling."
                    hero.say "You’re right. I’m sorry, Bree."
                    "She takes a breath and her shoulders relax."
                    bree.say "It’s okay."
                    "Silence stretches between us for a long minute."
                    bree.say "Are we good?"
                    hero.say "Sure."
                "I’ll do what I want.":
                    "No. This is ridiculous. How could she just keep this to herself?"
                    hero.say "You have to tell me when these things happen!"
                    show bree angry
                    bree.say "I don’t have to tell you anything!"
                    "Her face gets red, but I can tell it’s from anger. She’s more upset than I’ve ever seen her."
                    hero.say "Bree-"
                    bree.say "Shut up!"
                    bree.say "I’m leaving."
                    hero.say "What?!"
                    bree.say "I said I’m going! Leave me alone!"
                    "With that she stomps off angrily."
                    $ bree.love -= 50
    $ bree.set_flag('pregtest',2)
    return

label bree_event_bowsette:
    scene bg secondfloor
    bree.say "Hey, [hero.name]..."
    "The voice comes from Bree's room, but sounds off somehow."
    hero.say "Bree?"
    bree.say "Um, can you come in please?"
    "It's definitely Bree, but it sounds as though she's trying to sound gruff for some reason."
    "Curious, I drop what I was doing and enter the room."
    scene bg bedroom2
    show bree bowsette joke
    bree.say "So, What do you think?"
    "She's dressed in cosplay consisting of horns, a cute little crown, cuffs and a long, green tail."
    "Are those... spiked false teeth as well?"
    "I recognise the character near instantly and can't help but grin at the sight."
    "Bree blushes, struggling to make eye contact, but when I don't say anything she takes a moment to resolve herself, and speaks."
    bree.say "You dare enter the realm of the king of the Koopas?"
    "The gruff voice is back, heavier now, and she strikes a pose, baring her 'claws'. Black fake nails in reality of course."
    hero.say "Bree, what are you doing?"
    "With a giggle, seemingly brought on by the drop in tension, Bree drops the pose and scratches the back of her head awkwardly."
    show bree bowsette happy
    bree.say "I heard you talking about Bowsette the other day, I thought you'd like it..."
    hero.say "You did this for me?"
    bree.say "Well, Yeah, I thought you might think it was cute,?"
    "She seems to be fishing for something, but I don't mind. After the effort that clearly went into the costume she deserves the praise."
    hero.say "Bree, it's adorable."
    if bree.get_flag_value("sex"):
        show bree bowsette blush
        bree.say "I'm so glad you think so!"
        "My approval seems to have raised her spirits, her smile covers most of her face by now."
        "I take a step closer and lean in, inspecting the costume closely."
        hero.say "This is really well made you know, you've got some real talent."
        "I can't see her face, but I'm positive how close my face is to her neck is embarrassing her as I look at the collar."
        bree.say "You really think so?"
        hero.say "Oh yeah, I'll try not to ruin it as I rip it off you."
        bree.say "Wa-"
        "Before she has a chance to object, or even question me, I push myself into her, latching my lips around her neck and littering it with kisses."
        "She stumbles backwards but I stay latched on, pressing her against the wall as she tries to catch her breath."
        "I wait for her to object, but instead I'm rewarded by a quiet little moan, as cute as it is arousing."
        "I pull my head back, but keep pressed against her, staring into her eyes as my hands travel further down her costume, fumbling with but eventually unhooking her skirt."
        "As it falls to the floor with a barely audible thump, she gives the slightest of nods, encouraging me to proceed, but I have something better in mind."
        hero.say "Aren't you going to stop me, oh big strong king?"
        bree.say "N-no fair!"
        "She whines, closing her eyes as my now free hands begin groping her through the skintight latex."
        "There's a moment of silence but it seems she got what I was hinting at as she forces herself to speak again in the cute, gruff voice she put on."
        bree.say "I-I'll have to endure it until I can return to normal!"
        hero.say "Well I hope that never happens, you're way hotter now, {i}Queen{/i} Koopa."
        "I hear another gasp as one of my hands begins rubbing her front through the suit, massaging her with just a single finger."
        hero.say "Come on Bowsette, let's draw you out of your shell."
        "The hand groping her ass began under her suit, making more direct contact now, and discovering an interesting secret about the outfit."
        hero.say "Oh, so you aren't wearing anything under here?"
        bree.say "O-of course not, It would have ruined the outfit,"
        hero.say "I'd have thought you'd at least have had a belt for the tail. I'm surprised they make butt plugs like this, more so that you own one."
        "I catch her eyes widen, then shut tight. I continue fondling her as I lean in closer, practically touching her ear."
        hero.say "So what do you say, does the queen want her knight to finish the job?"
        "I'm not even sure what Bowser's knight would be, those skeleton Koopa troopers? Bah, semantics."
        bree.say "Y-Yes. Your queen commands you,?"
        "She seems to be struggling to keep up the persona, she wasn't great at it to begin with to be honest, but that just made the whole thing cuter."
        "Her voice is shaky and she keeps gasping for air as I press down harder on her slit, doing it sporadically enough she can never quite prepare herself."
        "I grasp her waist, mostly to steady her as I fear without the wall or myself she'd simply topple over with how weak her knees seem, then toss her onto the bed."
        show bree miss bowsette breebedroom dressed
        "She lands softly enough, rolling over once, then looking up to me with a mixture of fear, anticipation, and arousal in her eyes."
        hero.say "Anything for my queen."
        "I step closer as she shuffles in place, preparing for my arrival, slowly spreading her legs wide."
        "I watch her and she watches me. I revel in her submission for a moment, before unzipping my pants, my cock springing out into the open air, already fully erect."
        "I spot her breath catch in her throat, and gaze drop to my member."
        bree.say "I didn't know you'd like it this much,"
        hero.say "Let me show you just how much I enjoy it."
        show bree miss bowsette breebedroom dickout dressed
        "I let her lie in anticipation as I remove the rest of my clothes, feeling her prying eyes the entire time."
        hero.say "Ready, my queen?"
        bree.say "C-Come, Sir knight, I'm tired of waiting..."
        hide bree
        show bree miss bowsette breebedroom fuck dressed
        "I clamber onto the bed, just as tired of the build up as her, almost ripping her costume as I grabbed the thin strip covering her pussy and tore it to the side."
        "Now, with nothing in my way, I eagerly plunge my rod into her waiting hole, it being already soaking wet."
        "I'm well acquainted with Bree's body by now, and the roleplay only makes things even more exciting, even if she's not the best at it."
        "The effort she's putting in despite how hard it is for her is why it's so special."
        show bree miss bowsette breebedroom fuck orgasm dressed
        bree.say "Ahh,! Ahh,! I-, Ahh!"
        "Her moans fill the room, that and the sound of my crotch slapping against hers."
        "One of her hands reaches up for her crown as a particularly rough thrust on my part almost knocks it off her head."
        "I build up my speed as a reward for her devotion to the outfit."
        hero.say "How are you enjoying my pipe, Bowsette?!"
        "I know the puns are awful but I get a weird sort of sick glee out of them nevertheless."
        bree.say "S-So good! Y-you're a l-loyal knight!"
        hero.say "You make a better slut than a queen!"
        bree.say "Ah! Y-Yes [hero.name]! I-I'm a slutty turtle!"
        hero.say "Cum for me, you slut!"
        hide bree
        show bree miss bowsette breebedroom cumshot arm ahegao dressed
        "I reach over and grasp her horns, not sure how they're attached still, but they give me the leverage to give her several last, powerful thrusts."
        "I feel her convulse, I watch her body shake and eyes roll backwards as her pussy clamps around my cock almost painfully tight."
        "The sight and sensation drives me over the edge in return, gleefully pumping my seed inside her as she makes her final attempts to milk me dry."
        hide bree
        show bree miss bowsette breebedroom dickout cuminside ahegao dressed
        "Ectasy overcomes us as our respective orgasms begin dying down,leaving me to collapse onto the bed besides her."
        hide bree
        show bree miss bowsette breebedroom base dressed
        "Exhausted, we each lay there for a few moments, panting and letting the sweat clinging to our bodies dissipate."
        "Eventually, I speak."
        hero.say "You need to dress up more often now, you know."
        "My eyes are closed, but I hear her laugh, then feel her lips delicately plant a kiss on my cheek."
        bree.say "I don't know, You really did a number on this suit, [hero.name]..."
        "I grin, but don't say more, and neither does she. We both just enjoy the moment, led besides each other, still bathing in the afterglow of sex."
        "I don't exactly know how much time passes, but inevitably I'm reminded that a world exists outside of the room, and I should get out of bed."
        "Bree seems almost disappointed when I look back over to her, but when she realises I'm staring she forces a grin."
        bree.say "I'll um, like, see if you actually ripped this and get to fixing it, I guess."
        hero.say "Heh, sounds like a plan. Can't wait to see what you dress up as next."
        "I lean over and place a kiss on her lips, which she reciprocates in kind."
        "Then, we each say our farewells and, after getting dressed of course, I'm on my way."
    else:
        show bree bowsette blush
        bree.say "I'm really glad you like it!"
        "Her spirits seem to have been raised, although embarrassed she can't help but grin at me in return."
        bree.say "I want to take some photos before I take it off though, it took like, an hour to put on, so shoo!"
        "I raise my hands in mock surrender as she hurries me out of the room, flashing me a quick, but awkward, thumbs up before closing the door behind me."
        if bree.love >= 50:
            "I pause outside the door for a brief moment, before shouting back to her."
            hero.say "Next time, I'll be taking it off you!"
            "I almost regret not seeing her reaction, but I don't push it, I don't want to embarrass her too much."

    hide bree
    return

label bree_event_01:
    $ bree_love_max = 40
    $ bree.set_flag("story",1)
    "I felt a small nagging sensation in the back of my mind telling me that something was wrong."
    "I quickly pat down my pockets."
    "As expected, most are filled to the brim with miscellaneous objects."
    "I heard the crinkle of old candy wrappers, and felt the familiar bulge of my wallet."
    "My keys poke through the fabric of my jeans and traced my palm and yet..."
    "No matter how long I spent searching my person, my phone was nowhere to be found."
    "These days, I did my best not to leave the house without it, even if only to pass the time browsing social media or whatever articles caugth my eye during a dull moment."
    "Besides, finding it shouldn’t be a monumental undertaking, I even had a vague recollection of leaving it on my nightstand."
    scene bg bedroom1 with fade
    "However, my memories quickly proved to be false."
    "My phone was absent from my nightstand, or my bedroom as a whole in fact."
    "I threw my sheets around, dug under my mattress, and evicted all of my various knick knacks from their rightful homes on display as I searched, but to no avail."
    "With my room a mess, and running considerably late already, I found myself frowning at the combination of stupidity on my part, and simple bad luck."
    "However, knowing that my phone must be in the house somewhere, I made my way back to the living room."
    scene bg livingroom with fade
    "The mess I created could be cleaned up another time, at the moment I had more pressing matters to deal with."
    "It was a problem for future [hero.name] to deal with."
    "Considering they were the two places in the house that I spent the most time, if my phone was nowhere to be found in the living room too, I’d have to ask someone to call me."
    "But, without a phone to do that, and with both Sasha and Bree out of the house, I’d have to go outside and track down someone I knew."
    "This was such a pain..."
    "However, as I stepped into the room to begin searching, a face I hadn’t expected greeted me from the couch."
    show bree phone 1
    "Or rather... Didn’t greet me."
    "Bree seems absorbed in some sort of handheld game, despite probably having only just sat down."
    "The two white earbuds in her ears were blasting the sounds of carnage loud enough for me to hear, and no doubt masking all sounds of my approach."
    "I must have been mistaken in assuming Bree had been out of the house."
    "Upon initial meeting, I’d gotten the impression that Bree would be the outgoing type, so when I heard no sounds coming from behind her door as I left, I’d assumed I’d been home alone."
    "Although, now that I thought about it, I don’t think I’ve seen Bree leave her room much since moving in."
    "It seemed like that cheerful and bubbly exterior hid quite the introvert."
    "Not that it mattered at the moment though, since my contemplation about the strange roommate I’d found myself with reminded me of the long and tiresome time I’d spent with her luggage."
    "As a result, Bree still owed me a favor, and considering I was currently in need of help, I could think of no better time to cash it in."
    "I walked to her side and paused, glancing over her shoulder, yet she seemed too distracted by the on screen brawl to notice."
    "It was only when I tapped her shoulder did I get a reaction, and a rather explosive one at that."
    show bree phone 2
    bree.say "AHHHHHHHHHH!"
    "Bree let out an ear piercingly loud yelp as she threw her hands into the air, almost sending her game flying across the room."
    "Fortunately for her, the vice like grip with which she held it kept the device firmly in place."
    "The sudden rather exaggerated reaction however, startled me in return, as I lept backwards on instinct."
    "It took a moment or two for us each to calm down, during which Bree slipped her headphones from their rightful place and scanned me."
    scene bg livingroom
    show bree
    bree.say "You scared me!"
    "I didn’t need to be told that, but at the very least she didn’t seem to be holding a grudge."
    bree.say "I thought you’d gone outside, I couldn’t see your jacket by the door."
    "With my assumption that the search would only take a minute or two, I hadn’t bothered shrugging off my jacket."
    hero.say "Yeah, I forgot my phone and couldn’t find it."
    menu:
        "Mind lending a hand?":
            $ bree.love += 5
            bree.say "Uhhhh..."
            "Bree seemed conflicted, her gaze slowly drifting back towards her game."
            "But, just before she said no, a flash of something I couldn’t quite place appeared in her eyes."
            "A smile grew on her face as she began eagerly nodding."
            bree.say "Sure! Where’d you last see it?"
        "Help me look.":
            $ bree.sub += 5
            bree.say "Wow, you could at least say please."
            hero.say "You owe me one after dragging your things inside."
            bree.say "I..."
            "Although she appeared visibly reluctant, a short pause followed before objecting, where their entire demeanor seemed to change."
            "A smile grew in place of her frown as she began eagerly nodding."
            bree.say "Alright! You got me there, where did you last see it?"
    hero.say "I thought it was in my room, but I can’t find it anywhere."
    bree.say "Hmm..."
    "Bree pauses for a moment as she thinks, adopting a rather cliche pose with her hand on her chin."
    "She holds it for long enough to make me doubt whether she’s actually going to be of any help before suddenly dropping it."
    "In one swift movement, her hand disappears into the couch cushions, and just as quickly it returns with my phone within her fingers."
    bree.say "Tada!"
    "She proudly shoved the phone in my direction, the grin on her face wide and sweet."
    hero.say "That was quick, thanks."
    "My fingers brush against hers as I take the phone, but she doesn’t seem to mind."
    "Her skin is surprisingly soft."
    bree.say "Yeah, couch cushions are like, magnets for things like that!"
    bree.say "I always lose my keys down the side of my bed these days."
    "Although I had been in somewhat of a rush earlier, by now I’ve resigned myself to being late."
    hero.say "I try not to leave my stuff in my pockets so they don’t get lost."
    "Despite now being roommates, I still know surprisingly little about Bree."
    "I’ve picked up one or two things, but since moving in I haven’t seen her much."
    hero.say "So, how’re you doing? Like the house?"
    bree.say "Oh yeah, it’s like, really great! Way better than my old place."
    hero.say "Where’d you live before here?"
    bree.say "Before here? Uh..."
    "She seemed reluctant to answer."
    "I didn’t want to make Bree uncomfortable, so I quickly changed the topic."
    hero.say "So uh, what’re you playing?"
    "Bree seemed almost instantaneously relieved as I yielded on my initial question."
    "There was even a small sparkle in her eyes that gave away the genuine joy she felt at my interest."
    bree.say "Oh! It’s Motor Racer 2!"
    hero.say "2? I thought there were five already."
    bree.say "Well yeah, but the second was like, way better than any of the new ones."
    hero.say "I don’t think I’ve ever played any of the originals."
    bree.say "You should! I think the arcade has got some original machines, I keep meaning to go visit."
    hero.say "So you play a lot of video games?"
    "Despite it being far from an unreasonable question to ask, it seemed to catch Bree off guard."
    "Her eyes shot wide open, almost as if in panic as she began to stumble over her words."
    bree.say "N-No! I mean... Yes? Uh..."
    bree.say "Maybe?"
    show bree blush
    "Although it can’t have helped, I found myself chuckling against my will, sending a light blush spreading across Bree’s cheeks."
    bree.say "H-Hey! Don’t laugh!"
    hero.say "Sorry! You just got all flustered really easily."
    hero.say "What’s the big deal?"
    bree.say "It’s embarrassing, you know?"
    bree.say "Liking video games is like, really nerdy and uncool!"
    show bree
    "Oh, thanks."
    hero.say "I play video games, you know?"
    bree.say "Oh! I-I didn’t mean you were nerdy and uncool! I-"
    bree.say "Ahh!"
    "I found myself laughing again at Bree’s plight, but I didn’t want to make her embarrassment worse, no matter how amusing that may have been."
    hero.say "It’s fine, I don’t mind."
    "Besides, nerdy and uncool isn’t really inaccurate."
    "Either way, once more I witnessed relief washing over Bree from my words, although she still seemed to feel somewhat awkward."
    "One thing I have noticed in my slim time with Bree is that the woman is exceptionally easy to read."
    "She seemed to wear every emotion and thought proudly on her face, even if she didn’t intend to."
    bree.say "Oh good! I was worried I’d offended you!"
    hero.say "Nah, I’m not that easy to hurt."
    hero.say "I don’t think just liking games makes you nerdy though."
    "It’s a rather childish way of viewing what should, and usually is, a harmless hobby."
    "Plus, she was acting like being nerdy was a bad thing."
    bree.say "Well, I guess not..."
    "I could tell she wasn’t convinced, even if she yielded the point."
    "She probably just doesn’t want to have an argument over something so petty, which is at least a sentiment I can agree with."
    hero.say "Anyway, I should get going."
    hero.say "I’m already late as it is, thanks for finding my phone though."
    bree.say "No problem! It was easy as pie!"
    hero.say "You should go down to that arcade, by the way."
    "I found myself speaking without really thinking about it."
    bree.say "Oh! Uh... Sure! I’ll go eventually, I’ve just been settling in."
    "Fortunately for me, Bree also happened to be a terrible liar."
    "Whatever the reason, I got the impression that something else had been holding Bree back."
    "Maybe it was her worrying about seeming ‘uncool’."
    "Maybe it was just laziness."
    "It didn’t really matter the reason, but lounging around the house all day couldn’t be good for her."
    hero.say "Maybe we could go together then?"
    hero.say "I mean, you peaked my interest about Motor Racer now."
    bree.say "Oh! Uh... Sure!"
    hero.say "Great, we can figure out a time later."
    bree.say "Yeah! That’ll be fun!"
    "I don’t think even she believed herself."
    "She seemed oddly apprehensive about the situation, and gave the impression that she was doubting everything she said even as she said it."
    "There was something about Bree as a whole that peaked my interest."
    "It wasn’t as though I didn’t trust her, but she didn’t seem to trust herself."
    "Something just seemed off about her..."
    "If nothing else, this trip would help me get a better read on the girl."
    hero.say "But yeah, I really should get going, later Bree."
    bree.say "Bye [hero.name]! See you later!"
    "I ended up spending a lot of time chatting with Bree, longer than intended, but at least it wasn’t time wasted."
    "I feel like we grew closer."
    "Not that that’s saying much."
    "Anyway, I need to hurry now before I miss it entirely."
    hide bree
    return

label bree_event_02:
    $ bree_love_max = 60
    $ bree.set_flag("story",2)
    show bree
    bree.say "Hey [hero.name]!"
    bree.say "What’s wrong? You look annoyed."
    "My discomfort must have been obvious, so I quickly feigned a smile."
    "It had been a shock when I’d stepped inside, but I was already starting to grow a little used to it."
    "Once I’ve started playing games and distracting myself, I should be fine."
    hero.say "Nothing, don’t worry about it."
    bree.say "Wanna play some games?"
    hero.say "Yeah sure."
    bree.say "Hehe, I was supposed to have class today."
    hero.say "Supposed to?"
    "I watched Bree’s eyes widen as I questioned her, it must have been a slip of the tongue because she quickly tries to cover up her own admission."
    bree.say "Oh! Uh, it got called off, the professor was really sick or something."
    "While Bree was easy to read emotionally, so easy I’m already confident in that statement, I found myself unable to tell whether or not she’s lying."
    "Not that it mattered of course, it’s really none of my business."
    hero.say "Huh, lucky you then."
    bree.say "Yeah! So I came here and played some games~!"
    "Uh oh, that means she’s practiced."
    hero.say "Should I be worried...?"
    bree.say "Nope! I know you haven’t played before, so I’ll go easy on you!"
    hero.say "Glad to hear it, don’t think I’ve been in an arcade since I was a kid."
    bree.say "Oh, I love these places!"
    bree.say "Everyone’s just having so much fun, and there are so many games to play!"
    hero.say "You seem pretty passionate."
    bree.say "Hehe, yep!"
    bree.say "Back home there was only one arcade, and it was really small."
    bree.say "It’s really cool to see one as big as this!"
    hero.say "Huh, don’t you think it’s a little mu-"
    bree.say "AH! Quick!"
    hero.say "Wait, wh-ah!"
    "I’m cut short from my surprise as Bree’s hand wraps around my arm unexpectedly and begins yanking me off in a seemingly random direction."
    "I let out a quiet yelp as my feet struggle to keep up, stumbling over each other as Bree sprinted full force towards a target I had yet to see myself."
    "I narrowly dodge one or two innocent bystanders before we finally come to a stop in front of an empty machine."
    bree.say "People have been on it since I got here! This is the first time I’ve seen it free!"
    "As she withdrew her hand from my sleeve, I take a moment to examine the cabinet before us."
    hero.say "Motor Racer ..."
    bree.say "Yeah! Just in time, huh?"
    bree.say "It seems really popular!"
    "Hopefully, that was just a sign of how good it was."
    bree.say "I was going to practice, but I ended up spending all my time on a bunch of light gun games waiting."
    hero.say "Hopefully you’ll still be a little rusty then."
    bree.say "Come on, I’m sure you’ll do great!"
    "Although skeptical, I simply nodded as she went to put a coin into the machine."
    "I took the opportunity to glance at the machine again, and get in position ready to play."
    show bree arcade 1
    if not hero.check_skill("video_games"):
        "I was anything but optimistic about my chances, and as the coin fell into the machine and Bree stood back up, I saw a focus and determination in her gaze that only worried me more."
        "I could tell instantly that I would get destroyed here, and began to dread the game ahead, but it was too late to back out now as the racing care select screen popped up."
        "Bree wasted no time in selecting a red sports car."
        "It took a moment or two, but I found a car I recognised from when I’d played the more recent games."
        "When the actual gameplay started though, I found myself at a loss."
        "As if the altered control scheme wasn’t bad enough, when I finally got used to it, I found out that all I remembered didn’t work in this version."
        "If nothing else, Bree did make an attempt to go easy on me, and I picked out one or two occasions where she deliberately slowed down."
        "But even as she restrained herself, I struggled to match her, and on the few occasions where I did win a lap or two, it was clearly mostly due to luck."
        "Despite all of this however, I actually found myself having a lot of fun."
        "Bree kept things light and I’ve never been too sore a loser, by the time we finally stopped so someone else could use the machine I’d definitely come a long way skillswise too."
        "I couldn’t tell if I was enjoying it because the game itself was good, or because I had good company."
        "Time flew either way, in fact we only stopped when we did because I noticed a few people lurking and watching over our shoulders."
        "Bree seemed too absorbed in what was happening on screen to notice, and acted incredibly apologetic and flustered when she realised we were hogging the game."
        "The sheer focus she showed when we were playing however was not only impressive, but almost uncharacteristic of the almost ditzy girl I thought I’d known."
        "It seemed like there were a few sides to Bree that I had yet to discover."
        "In any case, the two of us had probably played straight for an hour or so, so we decided to grab drinks before doing anything else."
        scene bg arcade
        show bree
        "We stood off to one side, sipping at cans of cola from a vending machine, watching the room as we engaged in idle chatter."
        hero.say "You were right, that game was good."
        bree.say "Hehe, did you doubt me?"
        hero.say "Not at all, you seem to know more about this stuff than me at least. Better at it too."
        bree.say "Are you sure you’ve never played that before? You were really good!"
        "I’m 90%% sure that she’s just saying that to make me feel better, but despite my doubt, it feels good to hear."
        hero.say "Heh, you still kicked my ass though."
        bree.say "Well I’ve got way more practice! You’ll be good enough to beat me soon enough!"
        hero.say "Don’t think I didn’t notice you going easy on me, Bree."
        bree.say "Well you’re new! It wouldn’t be fair not to!"
        hero.say "Yeah yeah, I know. Still, I’m curious what you’re like when you’re trying your best now."
        bree.say "Hehe, get better and one day I’ll show you~!"
        hero.say "As much as I’d like to spend all day everyday in here, I can’t afford it on my wage."
        "Once again, I find myself envying professional gamers."
        bree.say "If only we had a game system to play it back home!"
        bree.say "It would be so much fun!"
        hero.say "Huh, maybe when I have more cash then."
        show bree happy
        bree.say "Hehe, yay!"
        "Fun games with a cute girl? What isn’t to like."
        "Besides, it’d give me a chance to get to know Bree a little more, which is an intriguing opportunity if nothing else."
        $ bree.love += 5
    else:
        "I’d never played this game before, but as I rested my finger over the controls, I felt oddly confident."
        "Racing games weren’t my best genre, but I was still damn good at them."
        "I watched the screen as the coin slid into the slot, Bree quickly joining me at my side and mimicking my stance."
        "I glanced over at her as the race car select screen began booting, and saw a level of focus and determination in her gaze that almost worried me."
        "I knew she’d go easy as I got to grips with this specific games odd quirks, but after that?"
        "There was still so much to Bree that I considered a mystery that I wasn’t sure."
        "I thought I’d at least gotten used to her general demeanor, but looking at her now, she didn’t seem even remotely like the same person."
        "Just how many more sides to her would I discover?"
        "Before I had too much time to dwell however, the game started."
        "It quickly became clear to me that Bree had intended to give me a few moments to get around the controls before getting serious, but the moment the game loaded I crushed the pedal and rushed past her."
        "I was simply fortunate that it worked, although Bree was quite the opposite."
        "What followed was some of the most intense few games I’d ever played."
        "Although Bree had managed to quickly turn the tables, I managed to catch back up just as quickly, and it became clear that we were evenly matched in basically all areas."
        "Every race came close, and some even drew with both of us going out of the road, or hitting each other's car so perfectly in sync that both our car slowed."
        "We stayed mostly silent as we played, focusing with all our might, and it was only during a brief respite where we had to put in more coins that I noticed a few people watching our game from afar."
        "By the time we did finally stop, I could feel my heart racing from the session, having gotten quickly pumped up during the duel."
        "Glancing across to Bree, she seemed to feel the same, and wore a wide grin on her face as we made eye contact."
        scene bg arcade
        show bree
        "When she spotted the small group that had formed to watch however, she quickly became flustered and seemed eager to make her retreat, so we darted away to get drinks."
        bree.say "You told me you hadn’t played it before!"
        hero.say "I haven’t, it was just similar enough to the ones I have to pick up quickly."
        bree.say "You were so good!"
        hero.say "Hey, I’m pretty sure you won more than me."
        bree.say "No way! You did like, so good!"
        hero.say "I guess next time we’ll have to keep track."
        bree.say "Totally! We’ll definitely come back again soon!"
        hero.say "I’d love to, but this session’s already cost more than I expected."
        bree.say "If only we had a game system to play it back home!"
        bree.say "It would be so much fun!"
        hero.say "Huh, maybe when I have more cash then."
        scene bg arcade
        show bree happy
        bree.say "Yay!"
        "She seems almost relieved that I said maybe, was she nervous?"
        "If anything, I’m the one that should be nervous."
        "Still, this opportunity is too good to pass up. Fun games with a cute girl, plus it’ll give me a chance to learn more about Bree."
        $ bree.love += 5
    show bree
    bree.say "I was worried about making friends when I moved here, but I already have one!"
    hero.say "You were worried? Why?"
    "From the surprised expression on Bree’s face, I once more get the impression that my question caught her off guard."
    "It’s almost as if any time she tells me something about herself, she do so by accident."
    bree.say "Oh! Uh, it’s just weird, you know? Moving into a new place, it’s like, really nerve wracking."
    hero.say "Makes sense I guess."
    hero.say "No idea why you’d be nervous though, you’re one of the nicest people I’ve met in a while."
    show bree blush
    "Once more, I seem to have caught her off guard, as her eyes widen and a blush starts to form on her cheeks."
    bree.say "Oh! Um, thank you [hero.name]! I like, think you’re really nice too!"
    "Granted, with my luck with people that wasn’t much of a claim on my part, but I didn’t need to tell her that part."
    hero.say "Heh, thanks. So uh, day’s still young, wanna go play something else?"
    bree.say "Definitely! Anything catches your eye?"
    hero.say "Uh... You said you were playing those light gun games, right?"
    bree.say "Yeah! They’re so fun! Some of the guns even have inbuilt recoil so it simulates actually firing one!"
    bree.say "I mean, obviously it’s way weaker than an actual gun, but it’s still cool!"
    hero.say "Heh, sounds good to me."
    show bree happy
    bree.say "Yay~!"
    hide bree
    "With very little in terms of warning, Bree turned and begin darting off in a seemingly random direction, tossing her can over her shoulder on the way for it to land in one of many trash cans set up near where we stood."
    "Although I’m relieved that she didn’t grab me this time, I find myself stumbling over my own feet as I begin rushing to catch up with her, caught entirely off guard."
    "Fortunately for me, she didn’t go far, and before long we were using up the last of our change blasting away robots and aliens and all other manner of things on the screen in front of us."
    "Once again, Bree was entirely right, and the game is a lot of fun."
    if hero.check_skill("video_games"):
        "Neither of us is quite as good at it, but between us we actually manage to finish one or two."
        "We seem to make a pretty good team, and covered each other quite well."
    else:
        "The games are surprisingly difficult however, and although we end up putting up a good fight, we don’t get all that far in any of the games we try."
    show bree
    "But predictably, our pockets became lighter with every passing minute and before long we were heading for the door once again."
    hero.say "That was pretty fun."
    bree.say "I know, right? I love trips to the arcade!"
    hero.say "If only it didn’t cost so much."
    bree.say "Hehe, I know right?"
    bree.say "I need to, like, get a job or something."
    "Once again, the question of where their rent is coming from pops into my mind, but I don’t want to pry too much."
    hero.say "Would you even have time to work with school?"
    hero.say "And even if you do get a part time job, won’t be much time left for games then."
    bree.say "Ahh! Good point! Maybe I’ll just stay home then~!"
    hero.say "You should try to get out sometime, though."
    bree.say "Well, that’s what I have school for!"
    "That isn’t really what school is for at all."
    hero.say "I guess so."
    hero.say "So uh, which game was your favorite?"
    bree.say "Oh! I really liked..."
    "We continued to chat for a while as we walked, heading home together."
    "Time flew as we discussed a few unimportant things, and before long we were stepping back inside our house."
    "After a brief goodbye, Bree predictably ducked back into her room."
    "I’m glad she seemed to enjoy herself, especially considering her reluctance to come in the first place."
    "Now I just have to make time to play a few more rounds with her sometime."
    hide bree
    return

label bree_event_03:
    $ bree_love_max = 80
    $ bree.set_flag("story",3)
    "As expected, after visiting the arcade with Bree not much changed."
    show bree
    "I was loitering, lounging on our sofa idly checking my phone."
    "More than anything else, I was letting my mind wander, not taking in any of the seemingly endless information the screen presented to me."
    "My thumb flicked past a sea of articles and supposedly humorous images, before the sound of approaching footsteps knocked me out of my trance."
    "I glanced upwards to see Bree emerge from the hallway connecting to her room, checking her own phone, although she seemed much more engaged with whatever was happening on her screen than I was mine."
    "So much so in fact, that she didn’t notice me as I gave a short wave in her direction, leading me to open my mouth."
    hero.say "Hey Bree."
    "Somewhat predictably, the sudden sound startled Bree, much like it had the last time I interrupted her focus when I saw her playing Alley Brawler for the first time."
    "And, much like that time, her jumping metaphorically out of her skin caused her hand to slip and almost drop the device it was holding."
    bree.say "Oh! Hi [hero.name]! I didn’t like, see you there!"
    "I quickly covered up my smirk as she turned to me, hiding my amusement at her plight."
    hero.say "Yeah, you seemed pretty absorbed in your phone. What’re you reading?"
    bree.say "Oh yeah! Details on the next Motor Racer just got leaked!"
    hero.say "Woah, really? Anything interesting?"
    bree.say "A whole buncha cool new stuff! Here, take a look!"
    "Quickly rushing to my side, taking a seat next to me, Bree eagerly shoved her device in my face."
    "I take it with much less enthusiasm, although I am curious, it would just be impossible to match Bree’s seeming enthusiasm with every little thing she sees."
    "There’s a lot to take in, so I just briefly skim the list, and pick out a few of the more noteworthy parts."
    hero.say "New drift system...?"
    bree.say "Yeah! The leak was really vague so everyone online is theorising what it might mean!"
    hero.say "Sounds like it could end badly, the games feel pretty intuitive as is."
    bree.say "Maybe, but at least they’re trying something different!"
    hero.say "I guess so, just hope it doesn’t ruin the whole thing."
    bree.say "Oh come on, it’ll be like, really fun anyway!"
    hero.say "Hey, if you say so."
    "With a giggle, Bree takes her phone back off me, shoving it back into her pocket as she lept back off the couch and began towards the refrigerator."
    bree.say "I was just grabbing a drink, want one?"
    hero.say "Sure, grab me a cola?"
    "All the talk of Motor Racer has yet again reminded me of the deal I made with Bree."
    "Feeling an itch to play it once again, and seeing no reason not to hazard asking, once Bree returns with our drinks I bring it up."
    hero.say "You free for a while?"
    bree.say "Always! What’s up?"
    hero.say "Wanna play something?"
    show bree happy
    "I catch her usual wide grin spread just a little further on her cheeks."
    "I was satisfied as a result, that her answer would be a yes, even before she began eagerly nodding towards me."
    bree.say "Yeah! That’d be great! Come on! Let's get my copy of Motor Racer and we can play on your Z-Box!"
    hide bree
    "Once again, I find myself rushing after Bree to keep up, thankful that my can is still closed for the time being or I’d be spilling my drink everywhere."
    scene bg bedroom2
    "I make a note to keep it closed for a few moments after arriving in her room, out of fear of having the contents explode all over me."
    "It was when I reached her door and stepped inside that I realised just how little I’d gotten used to the idea of living with Bree and Sasha."
    "I was getting along with them well enough, sure, but the sight of Bree’s room instead of the gym me and Ryan set up?"
    "It not only gave me pause, but outright shocked me."
    "It was silly, I knew that, of course Bree wouldn’t just be sleeping on the floor amidst a few weights and a couple of exercise machines."
    "In a few ways, Bree and Samantha were quite similar I suppose, so maybe it wouldn’t have been as bad if I was used to it still being a bedroom."
    "And Samantha ended up abandoning her room for his not long after they started dating anyway..."
    "It was just odd is all. Having the change sprung on me so suddenly meant I hadn’t properly processed it, I suppose."
    "It was like being thrust into the reality of the situation in an instant."
    "I must have been wearing my shock visibly however, as Bree quickly caught it."
    show bree
    bree.say "What’s wrong, [hero.name]? I know it’s a little dirty, I’m sorry!"
    bree.say "I kept meaning to clean it but then I got distracted by the leak and-"
    hero.say "Don’t worry about it, Bree. Mine’s way worse."
    "I manage a chuckle, and pushed away the thoughts about my old crush as I took a couple of steps inside, swinging the door closed behind me."
    "Bree’s room itself isn’t all that surprising, if anything it was almost bland."
    "The walls were the same colors they’d always been of course, and what furniture she did have I’d already seen when I helped her bring in her things."
    "Well, aside from the larger items, which she had delivered soon after of course."
    "If Bree had tried to make me drag her entire bed to her room for her I don’t think I’d have given in as easily as I had."
    "I was reluctant enough with the boxes I did transport."
    "It gave me a chance to be a little nosey however, invasive perhaps."
    "The contents of each box were written on the outside in big black marker, so it wasn’t like I was taking a peek inside the boxes."
    "Besides, there wasn’t anything that juicy anyway, most of the boxes were just clothes or games."
    "While she had plenty for me to help with, that seemed to be all she had, everything she owned she’d brought then and there."
    "In a way, that could be seen as quite sad, at the same time it made me realise how much she needed this place."
    "I didn’t have answers yet, who knew if I’d ever get them?"
    "At the moment, the more pressing matter was preparing myself, as Bree had already found the box she was looking for and was rushing to get back down to the livingroom."
    scene bg livingroom
    show bree
    "She dropped the box near the Z-Box, took a Motor Racer 4 game out of it, and crammed it into the gaming system."
    "The graphics looked a little odd on such a large screen, but I didn’t let that distract me as I took the device I was handed, and chose the same car I’d played as last time."
    show bree console 3
    "A quick glance confirmed my suspicions, with Bree focusing intensely on the screen already like she tended to do when playing, it seemed."
    "I could sense she wasn’t going to make it easy, and already knew first hand how good she was at this game."
    "At least this time it was free."
    "..."
    "Around an hour or so passed of race after race of back and forth."
    "I find myself more at home using a controller, I was more used to it than the layout they had back at the arcade after all."
    "Unfortunately for me, the same seemed to go for Bree, who’d obviously been playing this way regularly, making what little boost in my own skill meaningless."
    "As predicted, time flies and we barely exchange glances or converse as we play, what few comments we exchange being exclamations about how well the other has performed."
    "I’m not entirely sure if I can blame my enjoyment on the game anymore, it isn’t exactly easy to grip me so hard so quickly."
    "In fact, I’was beginning to suspect that Bree’s participation alongside me is what made these sessions so engaging."
    "Whether or not she’s going easy on me is irrelevant anymore, there’s simply a constant back and forth between us that keeps it interesting."
    hide bree
    show bree happy
    bree.say "That one was close!"
    "She wasn’t wrong, I’d come out on top but only by a short length."
    "I’m not too proud to admit luck was a large factor in my victory."
    hero.say "Yeah, you almost had me."
    show bree console 2
    if hero.check_skill("video_games"):
        bree.say "I think you’re starting to really get the edge on me!"
        hero.say "Nah, we’re still pretty neck and neck."
        bree.say "No, really! You’re so good!"
    else:
        bree.say "You’re definitely getting better!"
        hero.say "Heh, maybe soon you won’t have to go so easy on me."
        bree.say "Definitely!"
    play sound "sd/cell_vibrate.mp3"
    "I see Bree open her mouth to say more, but before words come out she’s interrupted by a low buzzing."
    "It took a moment for me to identify the source as a phone vibrating, and a quick check told me it wasn’t mine."
    "I turned to mention it to Bree, but she’s way ahead of me, already checking her phone curiously."
    bree.say "Ah! Sorry [hero.name]! I have to take this!"
    hero.say "No problem, take your time."
    bree.say "Thanks! I won’t be long, promise!"
    "With a grin and a wave, Bree rushed for the exit."
    hide bree
    "I caught a brief glimpse of her holding the phone to her ear before her hand grasped the handle and my view was obstructed by the door."
    "The upbeat music of the game wafted through the room to save me from sitting in silence, although just doing nothing was still quickly growing incredibly awkward."
    "It didn’t take a genius to realise that, at the end of the day, there was only one real option in this situation."
    "I quickly skimmed through the content of the box, looking at the various games in it."
    "Next to a few fighting games there was a few country CDs."
    "Unlike everything else I’d found, this one surprised me."
    "I picked a CD at random and took it out of the box."
    "The cover depicted a man in one of the most stereotypical country outfits I’d ever seen, complete with big leather boots and cowboy hat."
    "In fact, cowboy was quite accurate to describe what he seemed to be going for."
    "The man was even sitting on a large bail of hay with an acoustic guitar on his lap, smiling at the camera with a farm in the background."
    "It was as if someone designed the cover for the sole purpose of screaming ‘Country’ as loud as possible."
    show bree
    "Unfortunately for me, however, it was at this exact moment that the door opposite me swung open and Bree reappeared in the room."
    bree.say "I’m really sorry that took so long, [hero.name]! I was just-"
    "She cuts herself short as she spots me staring at her, CD in hand."
    "I feel like a deer in the headlights, although it wasn’t like the item we paused over was hidden in anyway."
    "Before I could react however, Bree’s cheeks began to flush as she leapt at me, yanking the CD out of my hand."
    "For a moment, I thought she might be mad, but fortunately for me Bree quickly proved that that wasn’t the case."
    bree.say "Ah! Don’t look at that, I don’t like country music!"
    hero.say "Then uh, why do you have a bunch of country CDs?"
    "Another obvious question that seemed to catch Bree entirely off guard, as she quickly began tripping over her own words and the blush on her cheeks simply grew thicker."
    bree.say "Uh... OK, fine, I like country music..."
    menu:
        "Tease her":
            hero.say "Country music, really?"
            bree.say "Yeah..."
            "Bree’s cute normally, but when she’s embarrassed that’s doubly so."
            hero.say "Wow, and I thought you had good taste. Country music? That’s like, bottom of the barrel stuff."
            bree.say "H-hey! It’s not that bad..."
            hero.say "Whatever you say Now I know Motor Racer is a fluke though, I’ll just have to make sure to avoid anything you recommend in the future."
            "Although I’m clearly not serious, Bree seemed to be growing uncomfortable, so I quickly droped the act."
            hero.say "Hey, I’m kidding."
            "With a light flick of the wrist, I toss the CD towards Bree, who scrambles to catch it before it hits the floor."
            hero.say "I don’t care what you listen to."
            bree.say "Oh wow, you really had me going then!"
            "I may have pushed it a little far, but Bree simply goes back to grinning, she doesn’t seem to be all that bothered now."
            hero.say "Why do you care anyway? Who cares what your music tastes are?"
            bree.say "Well, it’s a little weird is all."
            hero.say "Weird, how so?"
            $ bree.sub += 5
        "Hey, I don’t care.":
            hero.say "Why should I? So we have different taste in music, doesn’t matter to me."
            "Everyone has different tastes, and although the temptation to tease Bree is there, only helped by how utterly adorable she looks when she’s blushing, I don’t want to really embarrass her."
            bree.say "Hehe, thanks [hero.name]! It’s just like, weird, you know?"
            hero.say "Liking country music isn’t weird."
            bree.say "No, I mean like... I don’t actually like the music itself."
            hero.say "Uh, what do you mean?"
            $ bree.love += 5
    bree.say "I only listen to it because it reminds me of home."
    bree.say "I came from like, a little town in the middle of nowhere, the exact sort of place these songs are about, you know?"
    bree.say "I dunno, guess it feels like, nostalgic?"
    hero.say "That makes sense I guess. You miss home?"
    "A short pause followed for Bree to think."
    "I don’t rush her, giving her the space she needed."
    "I do take the opportunity to take a seat back on the bed rather than have the conversation standing in the middle of the room however."
    "Fortunately for me, Bree followed, and she finally spoke as I leaned over to grab my now room temperature drink."
    bree.say "No."
    hero.say "Really?"
    bree.say "Yeah, I mean, I like, wouldn’t go back there, you know?"
    "It’s odd to see her, not exactly unenthused, just not quite as overly eager as she usually is."
    hero.say "Any reason why?"
    bree.say "Uh, it’s like, a really long story, and I don’t wanna bore you!"
    bree.say "I’m happy here with you and Sasha anyway!"
    "Well, that didn’t last long. Bree was already back to exclaiming everything she said needlessly enthusiastically, and the grin on her lips had already returned."
    "It didn’t take a genius to see that wasn’t the end of that story, but it didn’t take a detective to realise she just didn’t want to tell it."
    "Just having a bad childhood didn’t make sense, not if she willingly reminded herself of it with music."
    "I couldn’t deny being curious, but wasn’t going to push it any further, so I quickly gave her an out."
    hero.say "So you’ve been getting along with Sasha?"
    bree.say "Well enough! I mean, she’s a little mean and we like, argue sometimes I guess, but we at least aren’t enemies, and that’s good enough for me!"
    "That made enough sense to me, their personalities do clash somewhat but Bree seems like the type of person who wouldn’t have enemies of any kind."
    hero.say "Glad to hear you’re getting along, it’s one thing not to like someone, entirely another thing not to like your roommate."
    bree.say "Hehe, I can only imagine! You guys are my first roommates, so I guess I’m like, really lucky~!"
    bree.say "Oh right! You like, took two roommates at once, right? Did you have people staying here before?"
    hero.say "Yeah, remember how I mentioned my friend just graduated medical school? Him and his girlfriend."
    hero.say "Well, they weren’t together when we first moved in."
    bree.say "Wow! So they like, moved in as roommates then fell in love~?"
    bree.say "That’s really romantic!"
    hero.say "Yeah, sure it is."
    "The disdain in my voice must have been obvious."
    "I was still friends with Ryan, sure, but I also still harboured quite the crush on Samantha, and Bree gushing over their relationship didn’t help."
    bree.say "What’s wrong, [hero.name]?"
    hero.say "Nothing, it’s stupid."
    bree.say "Nuh uh! Listening to country music because it reminds you of home is stupid, and you were nice even then!"
    bree.say "I like, really don’t believe it’s that bad!"
    hero.say "And I really think it is."
    bree.say "Come on! Just tell me~! I promise I won’t laugh!"
    "I opened my mouth ready to say no once again, but there’s no point."
    "I already know that Bree is going to drag it out of me eventually, and I can’t be bothered with the back and forth anyway."
    hero.say "I used to have a crush on his girlfriend when she first moved in."
    "Bree’s eyes immediately widened with shock, her jaw practically dropping in surprise."
    bree.say "Ah! I’m like, really sorry!"
    bree.say "I probably just made you feel worse, I didn’t know, please forgive me!"
    hero.say "Relax, it’s fine."
    bree.say "Really? You mean it?"
    hero.say "Yeah, she made her choice, nothing I can do about it now."
    bree.say "Wow [hero.name], that’s like, a really mature way of looking at it!"
    hero.say "Really?"
    bree.say "Yeah, really! I’m impressed!"
    "Something about Bree’s warm expression and gleeful exclamation surprisingly makes me feel better."
    "It wasn’t as though she’d said anything monumental or particularly special, but she felt so genuine that I couldn’t help but smile along with her."
    hero.say "Thanks Bree, that makes me feel a lot better."
    bree.say "Hehe, anytime!"
    bree.say "I’m just like, really sorry for bringing it up!"
    hero.say "Hey, I already said it was fine."
    bree.say "I know but-"
    hero.say "Bree, it’s fine."
    bree.say "Hehe, alright~!"
    hero.say "So uh, wanna play a few more rounds?"
    bree.say "Always!"
    "Bree had made me feel better, sure, but I still wasn’t entirely over Samantha, and more than anything else right now I just wanted to take my mind off it."
    "Either Bree saw that, or she just wanted to play more, because before I had a chance to pick my controller back up she’d already selected her character and was waiting on me."
    "So, we played for another hour or so, the back and forth yet again keeping us engaged, and distracting each of us."
    "Me, from thinking about Ryan stealing Samantha, and for Bree, presumably memories of home."
    "Before long however, it was time to call an end to our game, the final score determining Bree the winner by a narrow margin, narrow enough that she insisted we call it a draw."
    "We grabbed another drink and chatted about the leak a little more before we each went our separate ways."
    hide bree
    return

label bree_event_04:
    $ bree_love_max = 100
    $ bree.set_flag("story",4)
    play sound "sd/cell_vibrate.mp3"
    pause 1.0
    hero.say "Hey Bree."
    bree.say "Hey, [hero.name]."
    bree.say "Could you meet me at the coffee shop in the mall?"
    hero.say "Why?"
    bree.say "Come on! I have something to discuss with you."
    menu:
        "Sure":
            pass
    bree.say "Great! I'll meet you there in an hour."
    scene bg mall
    $ game.pass_time()
    "So, I wasted time for an hour or so, before heading to the coffee place, setting off a little early to make sure I wasn’t late."
    scene bg coffeeshop
    "Predictably, as a result I got there early instead, it wasn’t particularly difficult to find so I wasn’t wandering for long and Bree’s directions got me to the general area."
    "Looking around, the place seems mostly empty, including free of any specific blonde roommate of mine."
    "A quick check of my phone tells me I am still early, so not a big deal."
    "Grabbing a quick drink I take a seat facing the door, and patiently wait for Bree to arrive."
    "Unfortunately for me, while I was early, Bree is definitely not."
    show bree casual
    "Around twenty minutes after she arranged to meet me, I see her burst through the door at mach 10 speed, quickly searching the room with wide, almost desperate eyes, before finding me."
    "As our eyes meet, she seems to relax somewhat, although still rushes over to my booth needlessly quickly."
    bree.say "I’m so sorry I’m late, [hero.name]!"
    menu:
        "Don’t worry about it.":
            bree.say "Really? I didn’t keep you waiting long, did I?"
            "By now I’d been here for half an hour at least, but it is clear Bree has gotten here as soon as she could."
            "While she is still... Presentable, I can make out a thin layer of sweat covering her face, and her hair's on the messy side."
            "It look like she’s been running for a while, if I listen carefully I can even tell she's breathing not only heavily, but slightly raspy too."
            hero.say "No, I just got here myself. It’s fine, really."
            bree.say "Oh, good! I was running late so got really worried!"
            "She seems to have bought it at least, either that or she knows I’m lying but is relieved I don’t care."
            "Either way, she seems to have calmed down a little."
            $ bree.love += 1
        "You kept me waiting.":
            bree.say "I know! I’m really sorry [hero.name]!"
            hero.say "I even came early so I wouldn’t keep you waiting."
            "I’ve been here long enough to start getting annoyed. It’s one thing for her to be late, but it’s been quite a while now, and she was the one who set the time to begin with."
            bree.say "I won’t be late next time, promise!"
            hero.say "Just make sure that you aren’t."
            $ bree.sub += 1
    hero.say "So, are you getting a drink?"
    "My own coffee hadn’t last me too long, and even if I’d saved it until now, it wouldn’t be hot anymore."
    "Besides, can you ever really have enough coffee?"
    bree.say "I like, wasn’t going to get one, but you can go get another before I tell you the thing!"
    hero.say "You sure? I’d feel bad getting myself one when you’ve not got anything."
    bree.say "Yep! Go ahead!"
    menu:
        "Get yourself a drink.":
            "If Bree isn’t going to pay for her own drink, I am not going to get one for her."
            "Fortunately for the both of us, there was no line at the moment, so grabbing another coffee only took a few moments."
            "I take a seat again opposite Bree, who seems to have relaxed a little more by now, and begin sipping at my drink."
            $ bree.sub += 1
            $ DRINK = False
        "Get yourself and Bree a drink.":
            hero.say "I’m not going to get anything if you aren’t. Come on, it’s on me."
            bree.say "Are you sure? I’ll pay you back, promise!"
            hero.say "Don’t worry about that. What do you want?"
            bree.say "Uh, just a latte please!"
            bree.say "Thanks [hero.name]!"
            hero.say "Don’t mention it."
            "Fortunately for the both of us, there is nobody else waiting for their drinks, so I head straight to the barista and before long I am returning to our booth."
            "Bree quickly thanks me again as I hand her her drink, which she quickly sips at, immediately pulling a face that suggests it's a little hotter than she expected."
            "After that, she's a little less eager to drink it."
            $ bree.love += 1
            $ DRINK = True
    hero.say "So, what did you want to talk about?"
    bree.say "Oh yeah! Right, so like, we’re friends now, right?"
    "My curiosity had already been peaked by what was supposedly an ‘important’ topic, but the question makes me lean forward in my seat, as if searching for more information."
    hero.say "Of course, why?"
    bree.say "Well, like, I think I’m not gonna make rent this week."
    bree.say "I’m almost there! Just a little short!"
    menu:
        "Don’t worry, I’ll cover the difference." if hero.money >= 50:
            $ bree.set_flag("debt",True)
            bree.say "Really?"
            "Bree seems shocked I’d even suggest such a thing, but it isn’t a big deal."
            hero.say "Yeah, of course. Like you said, we’re friends."
            "It's not like this is a regular thing after all, I’ve never had troubles with getting rent out of Bree before."
            bree.say "Wow, thanks [hero.name]! And to think I was nervous to tell you!"
            hero.say "Yeah well, everyone has off weeks."
            hero.say "You’ll have it next week though, right? I can’t cover for you forever."
            $ bree.love += 1
        "I’ll sort something out.":
            bree.say "Really?"
            hero.say "Sure. I’ll talk to the landlord and Sasha, one week a little short is no big deal."
            bree.say "Wow, thanks [hero.name]!"
            hero.say "Don’t mention it, it’s really not a big deal."
            bree.say "Hehe, now I feel silly for getting worried about it!"
            hero.say "You will have it next week though, right? I can’t cover for you forever."
            "Part of the reason it's no big deal is that Bree’s been reliable in paying her rent up until now, if that changed the landlord might not be too happy."
        "You better have it.":
            bree.say "I’ll do my best! Promise!"
            hero.say "Good, the landlord won’t be happy if we don’t give them the full amount."
            bree.say "It was only like, a warning just in case! I should have it!"
            hero.say "If you really can’t, you might get away with it once, but if you don’t have the full hundred by next week there’ll be trouble."
            hero.say "You will have it next week, right?"
            $ bree.sub += 1
    bree.say "Of course!"
    hero.say "That’s a relief."
    "There’s a short lull in conversation as I sip at my drink."
    if DRINK:
        "Bree sips at hers too, but seems to be still cautious not to let it burn her again."
    "Now seems like as good a time as any to pry for more information about Bree."
    "Call me nosey or invasive if you want, but I’m curious and she isn’t offering much information about herself without me asking."
    hero.say "You mind if I ask you something?"
    bree.say "Ask me anything!"
    bree.say "Hehe, as long as I can ask something in return~!"
    hero.say "It’s a deal."
    hero.say "I was just wondering, I know you’re a student, but do you have a job?"
    "For a split second, I worry if I’ve asked too much, the usual cheerful demeanor slipping for just a moment into something that doesn’t last long enough to place, before returning slightly weakened."
    "Bree’s already told me she was unemployed back at the arcade, but I’m digging for more information than that."
    "Besides I kinda forgot she said so when I asked the question, only realising so after the words had escaped my mouth."
    bree.say "Well, actually it’s like, a little embarrassing."
    bree.say "I used to work in one of those chain fast food places, but I quit when I started school again."
    bree.say "I’ve just been using my savings as rent!"
    bree.say "That’s actually why I wanted to meet here today! I was at a job interview nearby, there’s a cafe opening and they need more waitresses!"
    "So her savings have run out? Better hope she gets the job then, and that she can start soon."
    "By now, she’s returned to her full cheerful self once more, any signs of my question being awkward to ask vanished."
    hero.say "Did it go well?"
    bree.say "Well, I think so? I mean like, it was hard to tell."
    bree.say "They asked a lot of hard questions, but I did some research beforehand so I think I got them right!"
    bree.say "It was more like a quiz than an interview actually."
    bree.say "Oh! But the owner seemed happy when I gave him my measurements!"
    "Wait what?"
    hero.say "Wait what?"
    bree.say "Hehe, I mean like, he has a uniform that already fits me!"
    bree.say "It wasn’t like, a pervert thing!"
    hero.say "Good, you had me worried there for a minute."
    bree.say "Hehe, I could tell! You pulled a funny face~!"
    bree.say "Glad to know someone’s looking out for me though!"
    hero.say "It’s the least I can do."
    "I leave out the part where I’ve grown a little protective of Bree because her childish nature and seeming naivety of the world means she’s got a target painted on her back."
    "There are hundreds of creeps in this town who’d take advantage of someone like her."
    "I’m trying to be nice after all, I don’t want to insult her."
    hero.say "So, this fast food job, was that back home in the country?"
    bree.say "Nope! It was here in town, probably a ten minute walk from here!"
    "That’s odd. Bree had made it sound like she’d only just moved here when we visited the arcade together."
    "She talked as though she didn’t have any friends, but if she’d been here for a while that didn’t make sense to me, especially if she’d been going to both school and her job."
    "Surely one coworker or classmate would get along with them."
    "I’think I have been pushy for now though, and I don't want to come across as rude or as doubting her."
    bree.say "So! My turn to ask a question!"
    hero.say "Yeah, that was the deal, ask away."
    bree.say "Do you like your job?"
    "That wasn’t exactly what I was expecting."
    hero.say "Uh, not really. Actually, it kinda sucks."
    bree.say "Aww, that’s no good."
    bree.say "How do you get out of the bed in the morning?"
    bree.say "I mean like, if you hate it, it’s gotta suck getting up every day for it."
    hero.say "Well, yeah, but you gotta do it."
    hero.say "Part of being an adult, I guess."
    bree.say "Being an adult sucks."
    "I smirk. Not because what she said was wrong, or because I agree with her, but rather that it’s the exact sort of thing I’d expect coming from someone like Bree."
    if DRINK:
        hero.say "I could drink to that."
        bree.say "Then let’s!"
        "Bree gleefully extended her latte into the air, having drank most of it by now, but with enough left to toast."
        "Although I snicker at the thought of toasting with coffee, and snicker again at the irony of phrasing it like that in my mind, I hold mine up too."
        bree.say "To never growing up!"
        hero.say "To never growing up."
        "We clink our mugs together, and each take a sip of our drinks, neither disillusioning ourselves about quite how silly that was, but neither of us cared."
    else:
        hero.say "Agreed. Wish I coulda stayed a kid forever."
        bree.say "Hehe, me too! That would have been the best~!"
    "We each share a wide grin."
    "If nothing else, at this point I’m just glad that Bree seems to have relaxed properly again."
    "Nothing stays serious for long with her around after all."
    hero.say "So, if you’re getting a job I guess that means there’ll be less time for us to play together."
    bree.say "Yep, but it also means I’ll have money to go to the arcade again~!"
    hero.say "Heh, good point."
    hero.say "I don’t know though, I think I ended up enjoying playing at home a little more."
    bree.say "Really?"
    hero.say "Yeah, it’s the same game after all."
    hero.say "Something kind of nostalgic about going to the arcade, but sometimes it’s just nice to be home."
    hero.say "I think nostalgia is overrated."
    bree.say "Really? I like nostalgia, it’s like, bittersweet, you know?"
    hero.say "Yeah, it’s both the best and worst feeling in the world."
    bree.say "Yep! That’s exactly it."
    hero.say "Guess the worst part is a little higher for me."
    bree.say "Well, I’m OK with playing at home! I can save up my money and buy some new games too!"
    bree.say "Oh! And there’s this book that’s just come out that looks really good!"
    hero.say "Well, fingers crossed you get the job then."
    hero.say "You know if you’ve got a second one lined up yet?"
    bree.say "Actually, yep! They asked me to come back next week!"
    bree.say "I’m actually like, really nervous."
    hero.say "That’s normal. Anything I can do to help?"
    bree.say "Hmm... Oh, yeah! They like, said the waitresses would be doing both serving and cooking!"
    bree.say "Can you like, do some taste testing and stuff? I wanna practice before I go back, just to make sure I get it!"
    hero.say "Well, can’t say no to that."
    bree.say "Yay! Thanks [hero.name]! It’s nothing fancy, but I’ve never really cooked before, so I wanna make sure I get it right!"
    hero.say "If nothing else, I can give you a few pointers."
    hero.say "I’m not a master chef, but if it’s just simple stuff I should be able to manage."
    bree.say "That’d be great! Thank you so much!"
    hero.say "Don’t mention it. I’ll be expecting you to make me a few meals sometime in return."
    bree.say "Deal! If it’s alright, can you like, pretend to be a customer and stuff so I can practice serving too?"
    hero.say "Whatever makes you feel more confident."
    bree.say "Wow, thanks [hero.name], you’re the best!"
    hero.say "Whatever you say, Bree."
    "We shared another chuckle, before deciding to call it a day."
    "I brought the leftover mugs to the barista, thanking them for the drinks, before heading out of the door with Bree."
    "I had some plans for the evening already, so we agreed to practice as soon as possible."
    "Bree just seemed happy to take a break for the rest of the day, I couldn’t help but feel like she must have had a stressful time with the job interview and worrying about rent."
    "Besides, I needed to give her a chance to find some recipes at least."
    hide bree
    $ game.room = "map"
    return

label bree_event_05b:
    $ bree_love_max = 120
    scene bg secondfloor
    "It's been a few days since either me or Bree have mentioned her upcoming interview."
    "Despite how important it is that she gets the position so she can afford to live here, it's just never come to mind in the little time I've spent with her since then."
    "I'm not sure if that's by her design or simply because it's slipped the mind. Either way, I find myself curious how fat she's come since then."
    "Her cooking was bad, almost atrocious in fact, but if she's really applied herself I don't see any reason why she couldn't have improved in that time."
    "She should have definitely at least learnt to make something simple, like the soup she'd already attempted."
    "Glancing at the time, I find a long and monotonous day ahead of me, and if for no reason other than a distraction I decide to check up on her."
    "As I predicted, I find her quickly enough in her usual spot, her bedroom."
    "A swift knock on her door summons her."
    show bree
    bree.say "Yeah?"
    "The door is cracked open just enough for her head to poke out, greeting me with that signature grin."
    hero.say "Hey, I was just wondering if you could cook for me again."
    show bree annoyed
    bree.say "Cook for you again?"
    "She seems a little confused by the statement, as though she has no idea what I mean, but it clicks soon enough it seems."
    bree.say "Oh! Uh, sure? Why?"
    hero.say "Well I mean, thought I could taste test for you again. See how far you've come and all."
    "Bree seems conflicted for some reason, and although she eventually nods, shrugs and grins, I get the impression she doesn't really want to make anything."
    "Why is another question altogether, but I just chalk it up to laziness or her preferring the game she's playing."
    "This is important though, so I don't feel guilty for dragging her out of her hole."
    hero.say "So do you want to practice the maid persona again while I'm here?"
    "It's only half a joke. If she said yes my day would get better."
    bree.say "Nope! Thanks though, but I think I'm like, alright with that part."
    "Damn."
    scene bg kitchen
    show bree
    "I shrug and lead her to the kitchen, intending to overlook the process, but when we get there neither of us makes a move."
    hero.say "So?"
    bree.say "I'm just like, thinking where to start."
    bree.say "Should I try the soup again?"
    "It didn't matter much to me either way, I wasn't hungry, just trying to help. So, I shrugged."
    "It was probably better for her to just make whatever she felt most comfortable with, if she wanted to make soup, she could make soup."
    show bree normal
    bree.say "Alright! I'll give it uh- I'll give it a shot."
    "She hardly seems confident, in fact she seemed reluctant to come cook in the first place."
    "I begin wondering if something's wrong, but decide it best to just leave her to it. If they need help, I'm right here."
    hero.say "Sounds good to me. I'm right here if you need some help."
    bree.say "Thanks! But uh, would you not prefer like, going sitting down somewhere?"
    hero.say "Nah, it's alright. I can watch over you this way."
    bree.say "Well OK then! I'll just get started then!"
    "I smile and nod. It feels like she's maybe putting off actually cooking for as long as possible for some reason."
    "I consider asking why, but since Bree begins, reluctantly, collecting her ingredients anyway, I settle on just leaving her to it."
    "It does quickly become apparent however, that my suspicions were right, and something is wrong."
    "As I watch over her, Bree keeps hesitating, reaching for one ingredient and stopping and getting something else entirely, or starting to heat a pot of water before stopping inexplicably."
    "At one point, she even starts cutting up a leek before seemingly changing her mind and throwing the entire thing away."
    "More than once I think to intervene, she looks like she has no idea what she's doing, but I refrain out of a sort of morbid curiosity."
    "Besides, she isn't going to learn from her mistakes if I'm coddling her constantly."
    "Her attitude and innocence is very childlike, but it'd be condescending for me to look down on her as a result."
    "It does seem like Bree herself is starting to get frustrated though, she's making progress but it's slow and she's started to mutter the recipe aloud to herself."
    "I'm not sure how someone can be quite so bad at cooking, but I don't want to be insulting so I don't say anything."
    "I realise that was a mistake however, when as she's cutting carrots, Bree suddenly yelps and drops her knife."
































    hero.say "Are you alright?"
    "I'm worried about Bree, more than I usually am, and not just because of the cut."
    show bree sad
    bree.say "Uh, yeah! I'll be fine."
    bree.say "It hurts but it isn't that deep."
    hero.say "Oh good, that's a relief."
    "I flash her a half hearted smile, she gives me her usual grin in return, but it does little to put me at ease."
    hero.say "What happened?"
    bree.say "What do you mean? I just like, lost focus for a second and my hand slipped."
    "I was asking more about the cooking as a whole. I'd stayed out of it but it was a mess, and I don't believe her cutting herself was just because of a lack of focus."
    menu:
        "Be mean":
            $ bree.sub += 5
            $ bree.love -= 5
            hero.say "I mean your cooking was atrocious."
            "I'm well aware I'm being mean, but I'm also being honest and right now, with the threat of eviction on the horizon if she doesn't get a job, that's what Bree means."
            hero.say "Really bad. I thought you'd practiced."
            "I didn't need to wait for Bree's answer, the look on her face told me everything I needed to know."
            bree.say "Well I um Didn't practice"
            "She looks upset. In fact, very upset, almost on the brink of tears in fact. I've never seen Bree like this before, it's such a stark contrast to her usual cheerful self I feel my heart sink, even if I think I'm doing the right thing."
        "Be nice":
            $ bree.love += 5
            hero.say "You didn't really practice, did you?"
            "It didn't exactly take a genius to figure that out, if she'd even so much as tried to practice then she'd know the recipe at least."
            bree.say "...No"
            "She looks upset, very upset actually. Her eyes are almost watering, are and an uncomfortable shade of red."
            "I've never seen Bree like this before. Usually, she's so happy and upbeat, whenever I've seen her upset for whatever reason in the past she's bounced back in seconds but this is something else."




    bree.say "I should have practised and then I didn't and then I hurt myself and I embarrassed myself in front of you."
    hero.say "That's really why you're upset?"
    "It seems a little silly to me, to be so worried about what I think, but Bree nods in response and forces a smile."
    "At the very least it seems like she's calming down now."
    hero.say "You don't have to worry what I think of you, I guarantee anything you can do I've done stupider."
    hero.say "One time I was skimming stones and eating, and I took a bite out of a stone and threw my sandwich into a lake."
    "That wasn't true, I actually read that online a while back, but Bree doesn't need to know that."
    "I get the laugh I wanted, her face finally lighting up once more. "
    "That's the thing about people like Bree. They're always so happy that the second you see them upset it hits much harder."
    show bree happy
    bree.say "Thanks. You're pretty good at cheering me up!"
    hero.say "Guess so. At least I'm good at something."
    bree.say "You're great at lots of things! Like Alley Fighter!"
    "There's the Bree I know."
    hero.say "You're better and we both know it."
    bree.say "I've been playing longer than you though! Like, in time, you'll be better than me!"
    hero.say "Well, I will have a head-start practising as you work on cooking some more."
    "Bree's grin wavers for just a second, but any doubts I had are quickly put to rest as she gives me a determined nod and a thumbs up."
    bree.say "I'll be the best cook ever!"
    hero.say "Heh, glad to hear it. You should take a break for now though, and be more careful when you're cutting onions next time."
    bree.say "I will! I don't want you to worry!"
    hero.say "Heh, alright. You should also bandage that finger properly because I have no idea what I'm doing."
    bree.say "Got it! It should heal pretty quick, it wasn't as bad as it looked!"
    if "cooking" in hero.skills:
        hero.say "Sounds good. Let me know when you're practising next, I'll show you a few tricks to keep yourself safe."
        "Well, technically I already have, but I get the impression that Bree's forgotten them already."
        bree.say "Oh wow, thanks [hero.name]!"
    else:
        $ bree.love -= 5
        hero.say "That's a relief, I was worried I was going to have to rush you to the hospital."
        bree.say "Hehe, nothing that serious!"
    bree.say "So yeah! I'll definitely practice and I'm going to nail that interview!"
    bree.say "Then I'll impress you with a good meal and take you to the arcade to celebrate as thanks for your help!"
    hero.say "Sounds like a good time to me."
    "Also sounds like a date, but I'm positive that she didn't intend it like that."
    bree.say "Really though, you're being so nice to me! I do appreciate it."
    bree.say "Everyone in this town is nice!"
    hero.say "Good to see you back to normal, Bree."
    "I smile at her, and get a wink and another thumbs up in response."
    "We make some small talk while Bree finishes up with her finger, she eagerly tells me more details about a couple of upcoming games."
    "Then she makes her excuses and vanishes back into her room. Soon after I hear the telltale signs of video games again leaking into the hallway."
    "I sincerely hope that she does practice this time, she'll be in a tricky situation if she doesn't get the job after-all."
    "I also think it'd be good for her, not just getting out of the house more, but having something to do aside from play video games."
    "Well, I should go do things I guess, I'm sure Bree'll be fine."
    "As much as she reminds me of one sometimes, she isn't a child. It is condescending for me to treat her like one."
    "The best thing I can probably do for her now is remain optimistic."
    return

label bree_event_06b:
    $ bree_love_max = 130
    scene bg livingroom
    bree.say "Hey, roomie!"
    "I hear Bree calling me from the next room, summoning me, and seemingly not to just play video games for once."
    "I briefly consider that might have been her intention, a quick few rounds of alley fighter, but her voice came from the living room."
    "Also, it's a little early, in fact I've not long woken up myself and Bree seems the type to enjoy sleeping in as much as she can get away with."
    "Curious, I poke my head around the corner to see what she wanted."
    scene bg kitchen
    "I'm surprised to find her stood by the table, which has been set with a clean white tablecloth and fancy cutlery which I can't remember ever owning."
    "And of course, food. Quite a bit of it actually."
    "Closer inspection reveals it's all simple dishes, like the soup she'd been trying to make for the past week now, but they look actually edible if nothing else."
    "The most complicated dish there looked like some kind of home-made burger, and not coincidentally it looked like the least professional dish too."
    show bree happy
    bree.say "So I've been practising and I wanted some opinions before tomorrow!"
    bree.say "Because, like, I'm kinda nervous and stuff!"
    "She laughs, and I laugh, but I can tell she's serious, and she's right to be."
    hero.say "Yeah, of course. You didn't have to make so much though."
    bree.say "Well I didn't know like, what they were gonna be serving there?"
    bree.say "I wanted to have my bases covered! Plus it got boring making the same thing over and over and over and over"
    hero.say "Guess it is good to have a wider spread."
    hero.say "But where'd you find the time to learn so many in just a couple of days?"
    "Bree laughs again, but breaks eye contact and scratches at the back of her head."
    bree.say "Wellllll~."
    bree.say "I waited until like, you and Sasha had gone to bed then did it in the night!"
    bree.say "You know, if there was gonna be a big mess or something I didn't want to get in the way during the day."
    "Kind of weak reasoning in my eyes, but Bree's weird."
    "There is one larger problem with her story though, which makes me roll my eyes and groan."
    hero.say "Thanks I guess, but what about actually sleeping?"
    hero.say "That's important too."
    bree.say "Well duh! But like, I'm alright! See!"
    "She gives me a thumbs up and winks."
    bree.say "Not even tired!"
    "Every time I start to think that treating her, or even thinking of her, like she's a child is cruel or condescending she does something like this."
    hero.say "Well, as long as you sleep tonight."
    hero.say "This whole thing would have been a waste of time if you fall asleep while you're there."
    bree.say "Hehe! I'll stay awake, promise!"
    bree.say "Oh! But that does remind me. Would you mind coming with me?"
    bree.say "I mean like, you've been great help so far, and I totally get it if you're busy!"
    bree.say "But I'd appreciate the like, moral support?"
    hero.say "I get it. Of course I'll come."
    "I'm in too deep to say no now. Besides, it gives me an excuse not to go to my day job, and I'll take any of those."
    bree.say "Really?"
    bree.say "Yay! Thanks [hero.name]! You're the best!"
    "She practically flings herself at me, almost knocking me off my feet."
    "It takes a second for me to get my breath back and return her embrace, although her face in my chest is making it hard to breath."
    hero.say "Not sure about the best, but don't worry about it."
    "I enjoy the hug for a few moments, but then try to separate myself when it becomes abundantly clear that Bree isn't going to stop otherwise."
    hero.say "Food's getting cold."
    bree.say "Oh! Yeah! Quick, you should eat up!"
    "Fortunately that's enough for her to release her death grip, she even pulls out the chair for me."
    hero.say "What a gentleman."
    bree.say "Hehe! The like, whole thing at a maid cafe is service, right?"
    bree.say "I figured I'd try and get more used to that too!"
    hero.say "So you'll be putting on the persona? Calling me master and all that?"
    bree.say "Yep!"
    "Nice."
    hero.say "Well let's get started then."
    bree.say "Of course, Master!"
    "I watch her take a moment to straighten her back and clasp her hands behind her back, a posture which naturally juts her chest outwards."
    "Probably by design really, but I'm not going to complain."
    "In fact, the posture and the fact that she adds 'master' to the end of every sentence is pretty much the only change."
    "Bree curtsy's towards me, bowing her head as I grab the burger, eager to get it out of the way first."
    bree.say "I hope you enjoy, Master!"
    bree.say "That burger is my own special recipe~!"
    "That worries me more than it's appearance. The fact that she's tried creating something from scratch when just days ago she could barely make a sandwich."
    "But, I try not to let on to my worry, and take a bite."
    "The taste is overwhelming. It feels like a burger, it looks (barely) like a burger, but it tastes just like incredibly strong hot sauce."
    "The spice hits me instantly and it takes all of my willpower not to instantly spit everything out."
    "I barely manage to swallow, then have to practically down the nearby glass of water."
    "My exaggerated reaction clearly caught Bree's attention, the next time I look at her she's no longer curtsying and has a concerned expression."
    bree.say "Is something wrong, Master?"
    menu:
        "Was this a joke?":
            $ bree.sub += 2
            "I react without thinking, the burning sensation in my throat being my main focus and heightening my annoyance."
            "Convinced it's a practical joke, I glare at Bree for a moment, before realising it was, in fact, a genuine attempt."
            "Guilt twinges at me as I force myself to calm down, quickly trying to give an explanation."
            hero.say "I mean, it's really spicy!"
            hero.say "Did you make it out of crystallised hot sauce?"
        "That's really spicy!":
            hero.say "I mean, INCREDIBLY spicy, I couldn't taste anything aside from how hot it is."
    show bree sad
    bree.say "Oh! Um, I did put a bit of hot sauce in it, Master, I must have used too much."
    bree.say "Accept my deepest apologies for the mistake!"
    "She bows so quickly that for a second I'm scared she's going to slam her head straight through the table."
    "Fortunately, she manages to dodge the stationary object, but she doesn't seem like she's about to go back to normal until I say something."
    show bree normal
    hero.say "It's fine, it just caught me by surprise."
    hero.say "Maybe next time make it without the sauce. Get used to making a burger before you try to spruce it up."
    bree.say "Of course, Master! Once again, I'm truly sorry for serving you something subpar!"
    "Even if I was furious, the look that Bree gives me as she says that gives my stomach butterflies and causes me to choke on nothing at all."
    "She's really mastered the puppy dog eyes, I'm not sure if that came with practice or it's natural but it makes me feel guilty for her bad cooking."
    hero.say "It's fine, really. Let's just call that one a loss and try the others, alright?"
    bree.say "Of course! Thank you, Master! You're truly kind!"
    "I really hope she gets this job. Not just because we've worked towards it but because she'd make such a good maid."
    "Also I'd get to see her in the outfit."
    "It doesn't take long for me to try a few more things, there's no point in me finishing anything after all just make sure it's not offensively bad."
    "Luckily, Bree staying up all night seems to have paid off."
    "Everything aside from the burger is not only edible, but occasionally genuinely tasty. One or two things I'd actually pay for at a cafe."
    "She's still got a ways to go, but it's a significant improvement."
    "I let her know what I think of each meal after I try it, and if there was any leftover disappointment that her experiment had turned out poorly it quickly dissipated."
    "In fact, her spirits raise more and more after every bite, by the time I've finished she's practically shaking with joy."
    if "cooking" in hero.skills:
        "I make sure to give proper constructive feedback, letting her know what needs to be changed or congratulating her specifically on what she's done well."
    else:
        "I try to give constructive feedback but I've never had much of a pallet beyond food being good or bad, she seems to appreciate it nevertheless though."
    hero.say "So yeah, not a great start but you've really come a long way."
    hero.say "I'm genuinely impressed. Well done."
    "I'm thankful I'm sat down, because I can tell from the way Bree's practically jumping with glee by now that she'd tackle me again otherwise."
    bree.say "Yay~! I knew I could do it!"
    bree.say "Hehe! And it's all thanks to you!"
    hero.say "Nah, you're the one who practised. This is your win."
    bree.say "Hehe~! I'm feeling really good about my chances now, I think I might actually get the job!"
    bree.say "Like, I'm pretty sure I can act the part, right? You kept blushing when I called you master at least!"
    "Wait I did?"
    bree.say "And if I can like, cook, that's already half the job locked down!"
    hero.say "Glad to hear it, confidence is key. If you go in confident in your skills then you'll probably do better."
    bree.say "Hehe! I'm almost excited now!"
    hero.say "You need help clearing this all away?"
    bree.say "Nope! What kind of maid would let her master do all the work?"
    "God-damn it. Now that she's mentioned it I can feel my cheeks flush, I must have been doing it this whole time."
    "Now I'm the embarrassed one, which doesn't help the blush fade."
    hero.say "Alright, if you insist."
    "I get up, brushing myself down of any crumbs or the like that clung to my shirt, when I'm caught off guard."
    "Now that I was finally standing again, Bree had once again tackled me and once again knocked the wind out of me."
    "I should have known this'd happen."
    hero.say "Oof! You caught me off guard then."
    bree.say "Hehe! I know!"
    bree.say "Really though, thanks for all the help!"
    hero.say "It's nothing, I mean it."
    "I pat her back, and try to ignore the two orbs on her chest that are pressed against me."
    "Slowly, I manage to pry myself away again, much to Bree's dismay."
    hero.say "Ugh, I have to go to work."
    bree.say "Oops! Sorry for keeping you so long!"
    hero.say "It's fine, I just gotta dart."
    bree.say "Hehe, bye [hero.name]!"
    "I give her a quick wave, before slipping outside, muttering a few curses to myself for letting myself be so sidetracked."
    "It isn't Bree's fault, she asked for the help of course but I could have said no or just hurried up, instead I dragged it out and gave it my all."
    "She's good company, if a little weird and invasive at times."
    "It's like she radiates an aura of joy, just being near her sometimes can make a dull day brighter."
    "In fact, because of that, I'm almost excited to take her to the interview tomorrow."
    "I just hope she doesn't mess it up."
    return

label bree_event_07b:
    $ bree_love_max = 200
    scene bg street
    "The day has finally come, Bree's fated interview with the maid cafe."
    "A maid cafe being in my town is still a weird thought for sure, but I've long since stopped questioning it and started to appreciate my luck."
    "Maybe it's a super power or something, lately things have really been looking up for a few reasons."
    "Being around Bree regularly is a definite big one."
    "Even now, as we stroll through the streets towards the cafe, instead of seeming anxious and nervous, clamming up and avoiding eye contact."
    "Anything that I would do in her situation really."
    "Instead of all that, she's literally skipping along, eagerly chit-chatting with me about, what else, but video games."
    show bree casual
    "I feel like keeping her mind on the task at hand would be a better decision, but for all I know the task at hand is the reason she's talking so much about really anything else."
    "I don't want to start quizzing her or berating her for taking it too casually when it might just be her way of avoiding unnecessary stress. Besides, as I have to keep reminding myself."
    "She isn't a child."
    "I think that her outbursts when cooking or awkwardness when she first told me that she was going to struggle with rent were because of something other than weird circumstance."
    "She never really shows anything other than pure, unadulterated joy, so the instances where she's anything but are just that facade dropping for a moment."
    "After all, nobody can be that happy that often, she's just good at hiding when she isn't."
    "So if something makes her lose that mask it hurts to see that much more."
    "At least, that's my theory. I could be entirely wrong, I'm not a mind reader or anything, but that's all I can think of to explain her weird mood swings."
    "Well, that or she has some genuine mental illness, but for both of our sakes I hope that isn't true."
    bree.say "So anyway, the new is that the next one's gonna be great!"
    hero.say "Yeah, it sounds promising."
    "I base my response mostly off her tone of voice."
    "She isn't boring or anything like that, I just have this nasty habit of thinking too much sometimes."
    bree.say "Totally! Like, I wish I had an early copy or something!"
    bree.say "Oh! We're here!"
    "I look up from the floor where I was walking, but not quickly enough apparently, since before I know it Bree's hand has grasped my wrist and she's dragging me into a nearby building."
    scene bg coffeeshop
    show bree casual happy
    "I vocalise my objections but Bree ignores me, and I find myself stood inside what I can only assume must be the maid cafe."
    "It's closed today, so no cute women walking around calling me master. Yet."
    "I get enough of that at home these days though."
    hero.say "I have to admit, some part of me still doubted that this place was real."
    bree.say "Hehe! Of course it's real!"
    bree.say "You stay here, OK? I'm going to go talk to the owner!"
    "I give her a nod, then take a seat in a nearby empty chair."
    "The room is full of various sized tables, each covered in a silk white tablecloth and decorated with fresh flowers and a menu."
    "The walls look like something straight out of a Victorian mansion and the floor's so clean I can practically see the chandelier reflected in it."
    "Exceedingly extravagant would be the best way to describe the place."
    "In fact, despite it being just a cafe, me being sat here just makes me feel poor, embarrassingly enough, so to distract myself I decide to take a look at the menu."
    "The same kind of effort that was put into the rest of the room was clearly also applied to the menu, various frilly patterns line the page and each food item was delicately pictured."
    "The most surprising thing of all though was that each page seemed handwritten in a posh, almost cursive sort of style."
    "While the room is extravagant and posh, the menus are cute and colourful, I guess the two together do represent the whole maid thing quite well."
    "Overall I'm impressed with the whole thing, in fact I-"
    "Wait hold on a second."
    "HOW much for a coffee?"
    "In fact, looking closer, I see that pretty much everything on the menu is grossly overpriced, often going above double what I'd usually pay anywhere else."
    "I know the food at these places isn't exactly the main attraction but who in their right mind would pay this much?"
    "I'd assumed the place was closed thanks to the lack of people around, but now I'm not sure."
    "It could just be open and this is how busy it usually is thanks to this ridiculous pricing scheme."
    "Well, as long as they pay Bree properly it shouldn't be an issue, until they close down that is."
    "But still, there go my plans of being a regular here. I doubt any amount of hot women in maid outfits could convince me to fork over $10 for a coffee."
    "Actually they probably could, but that's why I need to stay far, far away."
    "Either way, the long, boring wait was luckily not used to anyone's advantage and I was not coerced out of a large amount of cash."
    "Instead I spent most of it on my phone, only really looking up when I heard two approaching pairs of footsteps from the area Bree had entered."
    "I stood up and listened to the conversation, eager to find out how the whole thing went."
    manager_say "I'm very impressed, really."
    bree.say "Thanks!"
    manager_say "So we open on Friday, which means I'll need you here Friday at eight."
    bree.say "Yeah! Totally! Thank you so much!"
    "This sounds promising."
    "The two round the corner and I see Bree, whose smile is pretty much her only facial feature."
    "Much like she had when I'd praised her cooking, she practically shakes with joy."
    "The man next to her who I assume is the owner seems amused by the childlike behaviour rather than annoyed, which is good, since she's always like this."
    manager_say "Oh, sorry, we haven't opened yet Sir."
    "He speaks to me, but I shake my head. Before I can explain though, Bree rushes over to me and performs what is quickly becoming her signature half-tackle-half-hug."
    "It catches me by surprise even though it's becoming routine."
    bree.say "This is [hero.name]! He's my friend, he came for moral support!"
    "As I wince from the impact, I give the man a short wave."
    hero.say "Hey."
    manager_say "A pleasure to meet you, Sir. You two are quite cute together you know."
    manager_say "Say, we are on the lookout for butlers if you're interested?"
    manager_say "The pay and hours are negotiable."
    "Bree gasps, breaking her hold on me prematurely."
    bree.say "Woah! We could work together!"
    hero.say "Uh, thanks but I've already got a job. I don't think I'd make a good butler either."
    "I'm not the type that thinks calling strangers all day 'master' or 'mistress' would be fun."
    "Well, maybe the latter, but in a different context."
    "Also I'm still not convinced this place will be here in a month, so quitting my job for a lower paid position here just feels like a terrible decision."
    manager_say "Well I'm sorry to hear that, Sir. If you have any friends as attractive as yourself, please, send them my way."
    manager_say "After all, the success of a business like mine depends on the quality of their staff."
    manager_say "That's why I'm so lucky that Bree here came through my door."
    "The man speaks in an old time-y British accent which, when mixed with the scenery, almost makes me feel like I was sent back in time."
    "Bree seems to love it though, I'm not sure if she finds it funny or what but her grin grows just a touch whenever he speaks."
    "Maybe the whole stereotype of women swooning over British people is true."
    bree.say "Hehe! Thanks manager! I'm glad like, all of my hard work paid off!"
    manager_say "That it did, Bree."
    "The man literally pets Bree like she's some kind of cat, which I find really weird but Bree doesn't question it. Then, he turns to me again."
    manager_say "As I was saying to your friend, we do most of our training in house, but their dedication is stunning."
    "I don't bring up the fact that she left all of her practice until the last minute, or that she stayed up all night to do so."
    bree.say "Hard work really does pay off!"
    hero.say "Uh, guess so."
    hero.say "So, should we get going, Bree?"
    "The two make a weird pair, but the man seems nice enough and although I'm getting some strange vibes coming from him, he doesn't seem malicious."
    "It doesn't make me overly eager to stick around though."
    bree.say "Yeah! Totally! Thanks again manager!"
    manager_say "Not a problem, Bree. Farewell to both of you."
    "The man bows as we leave, and I realise what he was doing."
    scene bg street
    show bree casual
    hero.say "So uh, did he do the entire interview in character.?"
    bree.say "Hmm? Oh, manager? Yep!"
    bree.say "He was like that when we talked on the phone too! Cool, isn't it?"
    hero.say "I'm not sure 'cool' is the right word for it, but sure."
    bree.say "He's like, really dedicated!"
    hero.say "Guess so. I can't imagine working with someone like that though, it'd get pretty tiring pretty quick."
    bree.say "Maybe! But at least I'll have the chance to find out~!"
    "She beams up at me, and raises a hand. It takes me a few moments to realise what she wants, and I give her a high five."
    bree.say "We did it, [hero.name]!"
    hero.say "No, you did it Bree."
    hero.say "This is your win."
    bree.say "Hehe! But I wouldn't have done it without your help!"
    bree.say "Come on, let's go celebrate!"
    "I feel her hand once again grasp my wrist as she begins dragging me down the street."
    hero.say "Woah! Where are we going?"
    bree.say "To celebrate!"
    bree.say "There's a really good pizza place down here and it's got some arcade machines!"
    "Sounds like Bree's kind of place. In fact, it sounds like mine too, so I'm in no place to judge her."
    hero.say "Fine, but why are you dragging me?"
    "Bree's surprisingly fast, and we're practically sprinting, it's a genuine effort to keep up with her pulling me isn't helping with my balance either."
    "It feels like I'm perpetually about to fall over."
    bree.say "Because I'm excited~!"
    "If anything, my complaints make her speed up much to my dismay. It's a miracle I'm not met with a face full of the floor before we arrive."
    bree.say "Tada~!"
    "Finally, she releases me, just to gesture up towards the building we're stood outside of."
    "It's a pizza place alright, it doesn't look that impressive either."
    "Maybe it's just because I'm fresh from the Victorian cafe, but it's definitely not something worth the fanfare that Bree's giving it."
    "I also might just be a little grumpy because I've been left winded by the run here, in fact I might have to start bringing an oxygen canister when I hang out with Bree."
    "It seems like I'm always out of breath for one reason or another when I'm with her."
    hero.say "Great, looks good?"
    "I can tell from the deep breaths Bree's taking that she's also out of breath, she's just hiding it well."
    bree.say "Come on! Let's go sit down!"
    scene bg highclassrestaurant
    show bree casual
    "That doesn't stop her from trying to grab me again, but this time I deftly avoid her grasp and head in on my own volition."
    "The two of us take a seat and order our food, plain cheese for me and one of everything for Bree."
    hero.say "So, the interview?"
    "I'm eager to find out whether anything we'd practised had actually come up, or if the entire charade had only served to boost her confidence."
    "Either way, it worked."
    bree.say "Yeah! So most of it was like, him asking me questions about like, maids!"
    bree.say "He seemed to really care about it being authentic or something?"
    bree.say "Either way he seemed really impressed by my act!"
    hero.say "Well yeah, it's great."
    hero.say "You really hit the nail on the head with it."
    bree.say "Hehe! Thanks!"
    bree.say "He even said that he already has a uniform in my size in storage!"
    bree.say "Something about it being custom made for someone else because of their bust then them quitting and it going unused."
    "That can't have hurt her chances, but I don't want to insinuate she got the job because of her looks, so I just nod along."
    bree.say "Oh! And he said most of what people order is just coffee, and I make plenty of that myself, so I'm like, all set!"
    hero.say "Sounds like a pretty easy job then if the whole maid thing comes naturally."
    bree.say "Hehe! I hope so!"
    bree.say "I mean I don't wanna complain or anything, but it doesn't pay enough to be like, really taxing and difficult."
    bree.say "Enough for rent though! He even like, gave me an advance so I'm all set!"
    if bree.get_flag_value("debt"):
        bree.say "Oh! Speaking of which!"
        "Bree pulls a bill out of her pocket and pushes it towards me."
        bree.say "Here's your money back!"
        hero.say "What money?"
        bree.say "You like, gave me rent money a while back, remember?"
        bree.say "I'm paying you back!"
        menu:
            "Take the money":
                $ hero.money += 50
                hero.say "Oh yeah, thanks."
                "I take the cash and pocket it, now just a little richer."
                bree.say "No problem! Thank YOU for letting me borrow it!"
            "Don't":
                $ bree.love += 2
                "I shake my head, and push the money away, much to Bree's confusion."
                hero.say "It was a gift, you don't need to give it me back."
                show bree casual happy
                bree.say "Really? Are you sure? I can afford it now!"
                hero.say "Yeah, I'm sure."
                bree.say "Alright! You're the best [hero.name]!"
    hero.say "I'm just glad you're financially stable now."
    "I'm cut off by the pizza arriving, and after quickly thanking the waiter, I realise that this is my chance."
    "I'd been curious about a few things, mostly about her education."
    "I remember her telling me that she quit her last job for school, but she seems entirely disinterested in studying."
    "I hadn't wanted to be nosy, but it was as good a topic as conversation in my eyes."
    hero.say "So, how's university going?"
    bree.say "Huh?"
    "The question seemed to take her off guard, and I have to repeat it once before I get an answer."
    bree.say "Oh! It's like, good! I told you I was like, gonna be a doctor, right?"
    hero.say "Yeah, I think so, but you never really talk about it."
    bree.say "Hehe! That's because it's boring~. At least it is compared to video games!"
    hero.say "Yeah, I never liked school either."
    hero.say "It's important though, you just have to power through."
    bree.say "Yep, I guess."
    "Oh boy, I think I said something wrong."
    "Bree's expression dropped for a moment as she stared down intensely, coincidentally at her pizza which made it seem a touch humorous but I try my best to take her seriously anyway."
    bree.say "I mean, yep! Totally!"
    "That was perhaps the least I'd ever believed anything Bree's ever said."
    hero.say "If you disagree you can just say so, you know?"
    bree.say "No! I mean, it's not that I disagree! You're right!"
    hero.say "Then.?"
    "Bree visibly hesitates, they seem torn for some reason. I do what I usually do, stay quiet, I don't push her and leave her to decide between whatever she's deciding between herself."
    bree.say "Alright. So like, I guess you've noticed I don't go to class a lot?"
    hero.say "Yeah?"
    "It was one of the first things I'd noticed that was off about her actually, but I don't tell her that."
    bree.say "Well like, I actually really, really don't want to be a doctor."
    bree.say "I think what they do is great and all, but I'm just really squeamish!"
    bree.say "I uh, only realised that too late though and I'd already like, paid my tuition."
    "That sounded quite short sighted, but not all that out of character for her."
    "I could believe she'd do something like that, but something about her explanation still sounded fishy, I just couldn't quite figure out what."
    "Maybe I should just drop it, Bree is my friend after all, it's weird for me to keep interrogating her like this. I just want to know more about her and she isn't offering much."
    "I'm tired of speculating and guessing, it still feels like we're strangers at times."
    hero.say "Well, you had good intentions at least. That's just a lot of money to waste."
    hero.say "Why don't you see if you can talk to the university? You might be able to sort something out, swap to a different course or just get at least some of your money back."
    bree.say "Well like, it isn't that simple? It's really hard to explain, but I would if I could!"
    hero.say "If you don't want to tell me, that's fine."
    hero.say "I can't make you and it'd be rude if I insisted anyway."
    bree.say "Really? Thanks [hero.name]!"
    bree.say "I really don't like, mean any ill will by it, it's just a complicated situation and like, I don't want to bring down the mood!"
    bree.say "We're like, celebrating! Shouldn't we keep things light?"
    hero.say "You're right, sorry for asking."
    bree.say "It's fine! So~."
    bree.say "What do you think of the manager?"
    "I'm convinced she only asked as a desperate way to change topic. Whatever it is keeping her from talking about university is something I'm not about to discover today."
    "At least I learnt a little about why she doesn't want to go to class, if she's avoiding it then getting a full time job isn't that unusual, and neither is spending all day in bed."
    "Well no, that last part is still weird, but understandable."
    hero.say "The manager? He seems alright. Does he have a name though?"
    bree.say "I don't know! He just introduced himself as manager!"
    hero.say "Weird."
    bree.say "Very! But like, what did you REALLY think of him?"
    hero.say "Really think of him?"
    bree.say "Yeah! He's handsome, right?"
    "I have no idea what Bree is talking about now, and I'm almost afraid to humour her."
    hero.say "I don't know, sure I guess? What about it?"
    bree.say "Hehe! He was totally hitting on you!"
    "What?"
    hero.say "What? Wait, really?"
    bree.say "Yeah! I wouldn't joke about something like that!"
    bree.say "Like, did you not notice?"
    hero.say "No I didn't notice! Is that why he offered me a job?"
    "That explains all the weird vibes I was getting from him, I just thought it was because of the persona he was putting on."
    bree.say "Duh! I was gonna give him your number!"
    hero.say "Woah woah woah, I don't see why you need to do that."
    bree.say "Hehe! Wow, you're pretty oblivious aren't you?"
    hero.say "Well I didn't THINK I was."
    bree.say "Obvious even to your own obliviousness!"
    hero.say "How was I supposed to know he was flirting? He's a guy."
    bree.say "Well yeah! Obviously! But like, I think that even if it was a girl you wouldn't have realised~!"
    hero.say "What's THAT supposed to mean?"
    "Was Bree flirting with me now? Or was she just messing with me?"
    "Her laughter was clearly at least somewhat at my expense, even if I laughed along."
    "She couldn't be flirting with me, she must just be trying to twist and confuse me now."
    hero.say "I'd definitely have picked up on it if it was a hot girl, trust me."
    bree.say "Are you sure~?"
    "Am I sure? Gah, she really is twisting me around her finger."
    hero.say "I'm sure."
    bree.say "Hehe! Then I'll take your word for it~!"
    hero.say "You should, I'm very trustworthy."
    bree.say "Of course! You've never lied to me at least!"
    bree.say "It's one of your best qualities!"
    hero.say "Not my natural charisma or athletic prowess? Or what about my amazing wit?"
    bree.say "Well duh! Of course all of those!"
    "I laugh again, and take a bite of my meal. I can't tell if she really thinks that highly of me or if she's just joking and being nice, but either way it's nice to hear."
    "Don't get me wrong, I don't swoon to just every girl who compliments me, honest."
    "But whenever Bree says something like that it make my heart leap in my chest, she's just so consistently adorable and genuine that it means more coming from her."
    hero.say "I'm glad you recognise how amazing I am then."
    bree.say "Of course! It's hard to miss~!"
    "Wait is Bree really flirting with me? I'm going to be hung up on this all day."
    "Do I flirt back or is she just being nice again? If I flirt back and she's just being nice she might get the wrong impression and get upset."
    "Or worse, she'll have endless ammunition to tease me. She wouldn't do that of course, but the option would always be there, looming over me."
    "But if I don't flirt I might just miss my chance."
    "Or am I imagining things entirely because she's convinced me that I missed it earlier?"
    "And how did she get into my head so easily to begin with anyway?"
    hero.say "I'm glad I make such a strong impression then."
    bree.say "Yep! You do that if nothing else!"
    bree.say "I'm all finished with my pizza, I wanna go try some of the games! They got in a couple new machines!"
    hero.say "You don't have to wait for me, go ahead. I'm taking my time."
    bree.say "Hehe, thanks [hero.name]! Come join me quick, alright?"
    "Before I can answer, she scrambles out of the booth and practically sprints over to the arcade cabinets sat over in the corner."
    "I'd practically left my pizza alone, to be entirely honest I wasn't all that hungry, it's why I chose something simple, but it still felt like a waste to just leave to get cold."
    "I watched Bree as I ate, as she very eagerly mashed buttons."
    "I once again got to see that way she got oddly focused when playing, even if she was taking it more lightly than usual."
    "Predictably, my mind began to wander once again, that overactive imagination of mine acting up."
    "What if Bree really had been flirting with me? She isn't the kind of person to do that casually. If she flirted with me, she probably genuinely likes me."
    "She does shower me with an awful lot of compliments, and she makes a lot of physical contact too, but as far as I know she's just like that."
    "I could ruin our friendship if I did something and was mistaken, so I can't make that risk."
    "That's assuming that I even wanted a relationship with her."
    "Am I ready for something as serious as being Bree's boyfriend would be? She's fun of course but it wouldn't be just a little fling."
    bree.say "Hey, [hero.name]! Come look at this!"
    bree.say "They've got this racing game where you can play as a bunch of Nimtembo characters!"
    "My train of thought is broken by me being summoned by Bree herself, but that's for the best."
    "Whatever comes, worrying about it isn't going to do any good. In fact, I should follow her lead."
    "Focus on video games and just take things in their stride."
    "More people could do to be a little like Bree in that way."
    hero.say "Sounds good, dibs on Muria!"
    "We spend a shameful amount of time playing video games until the restaurant closes and we're kicked out."
    "I walk Bree home, I tell her to get a few early nights so she's fresh for training day, she all but tells me she won't, then we part ways."
    "I'm left alone to wonder exactly what the future holds for the two of us."
    return

label bree_event_05:
    $ bree.set_flag("story",5)
    show bree
    "Bree’s holding a flyer in her hand, crinkled at the edges."
    bree.say "You won’t believe what I found!"
    "I raise an eyebrow."
    hero.say "A job?"
    bree.say "Wha- no! But... yes. Shut up!"
    "Bree plops down on the couch next to me. She hands the flyer over to me and I take it with a tired hand. I look down at it."
    "When my eyes focus, I’m drawn to the bright colours, explosive graphics, and the main header-"
    "Arcade Tournament! Join us at 7PM for a battle against gamers! Prize of $500! Sign up to compete today!"
    hero.say "A tournament?"
    bree.say "Yeah, a tournament!"
    hero.say "Are you saying you want to enter?"
    bree.say "Like, yeah! You see the prize money, right? I can totally pay for rent with that."
    hero.say "I mean, if you really want to, I don’t care. Do you really think you can win?"
    bree.say "I might as well try, ya know? It’ll be good money until I can find a job."
    hero.say "Alright, alright. You know it says there’s an entry fee?"
    show bree blush
    "Bree’s face falls for a millisecond, but in just as much time she’s batting her eyes at me."
    bree.say "Okay, I know I owe you for rent, but will you help me? Please? Please, please? I’ll totally make it up to you!"
    "I sigh. The fee isn’t too much- $15. If Bree can really win this, then it would be well worth it."
    menu:
        "Pay the Fee" if hero.money >= 15:
            bree.say "Thank you so much! You won’t regret it, I promise!"
            hero.say "Yeah, yeah. You better win!"
            $ bree.love += 1
            $ hero.money -= 15
        "Refuse":
            hero.say "Sorry, I can’t do that. I need to pay for my own things."
            show bree
            bree.say "Aww. Alright. I’ll have to figure something out then."
            bree.say "Maybe I can ask Sasha when she gets home."
            $ bree.love -= 1
    hero.say "Do you know what game the competition is for?"
    "Bree promptly takes the flyer out of my hands, flips it, and has me stare at the back. Oh. Alley Brawler."
    "I can vaguely remember a magazine guide and a cartridge of that game on Bree’s shelf in her room. Maybe she really did have a chance."
    bree.say "See! I can do it."
    hero.say "Yeah, okay. But this is coming up in a few days."
    bree.say "Don’t worry! We can go to the arcade to practice."
    hero.say "Um- we?"
    bree.say "Yes, we. I need someone to compete against! Let’s go! The arcade’s gonna close soon."
    menu:
        "No Way":
            $ bree.love -= 1
            hero.say "No- no way. I just got home from work."
            bree.say "Please! You gotta help me, [hero.name]."
            hero.say "Sorry. I need my sleep."
            show bree
            bree.say "...Alright."
            return
        "Fine, Let’s Go":
            $ bree.love += 1
    hero.say "What, now?"
    "Bree’s pulling me off the couch before I can blink."
    hero.say "Hey- woah! Can we at least pick up some coffee on the way?"
    scene bg black with fade
    $ renpy.pause(0.1)
    scene bg arcade
    "There’s not too many people in line at the arcade machine Bree wants to use."
    "In fact there’s only one person- a girl, sitting in a pulled up chair, with wrappers and and a paper cup set on top of it."
    "It didn’t look like she was moving."
    show bree
    bree.say "Hiya!"
    bree.say "How long do you think you’ll be using that?"
    unknown_girl_say "..."
    unknown_girl_say "Until I’m done."
    "Thank god we picked up coffee."
    "I can already tell where this is going."
    bree.say "What does that mean? Done with the round?"
    "The other girl doesn’t answer, instead tapping away on the bright arcade buttons."
    bree.say "Hey!"
    "Bree knocks on the top of the machine with her knuckles, grabbing the other girl’s attention."
    bree.say "You can’t, like, hog the game!"
    unknown_girl_say "Yeah. I can. I’m playing as long as I want. Now fuck off, blondey."
    "Bree seems to be shocked into silence- honestly, I kind of am too."
    "Bree looks over at me with pleading eyes. Did she want me to do something?"
    menu:
        "Intimidate":
            $ bree.love += 1
            if hero.fitness <= 50:
                "I puff out my chest and step forward."
                "I could ask nicely, but she didn’t seem like the kind of person to listen."
                hero.say "Let her have a turn."
                "She mockingly coos at me, puckering her lips."
                unknown_girl_say "Ooh~! Is the boyfriend coming to save the wench in distress?"
                hero.say "Don’t call her that."
                unknown_girl_say "Aw, what are you going to do? Stare at me to death?"
                hero.say "Wha-"
                unknown_girl_say "Either you and your blonde slut get out of my face or I scream ‘rape’. Your choice."
                "Before I can answer, Bree grabs onto my elbow. I look back at her in irritation, but her expression says to back down."
                show bree
                bree.say "C’mon, [hero.name]. We can come back tomorrow or something."
                hero.say "But-"
                bree.say "Let’s go."
                hero.say "..."
                hero.say "Okay."
                "Bree leads me out of the arcade until we come to the mall’s street."
                "I feel a little bad for not getting the game for her, but there was always tomorrow."
            else:
                hero.say "How old are you, seriously? Move."
                unknown_girl_say "Oh yeah? What are you going to do?"
                hero.say "You can get up yourself or I can move you and your little chair out to the street."
                bree.say "[hero.name]!"
                "I ignore Bree’s whisper of disapproval in favour of staring the girl down- which was quite easy, considering she was already sitting."
                "Her lips are pursed, as if considering if I’d really do it."
                unknown_girl_say "... Fine. I’m leaving. Geez, teach your boyfriend how to chill."
                "She promptly stands up and leaves, not sparing either of us another glance."
                "I move to wipe off the scraps she left behind and set the paper cup on the floor next to the machine."
                $ bree.love += 1
                bree.say "..."
                bree.say "... Thanks, [hero.name]."
                hero.say "No problem."
                hero.say "Something wrong?"
                "Bree looks pale, now that I’m looking at her."
                bree.say "No. I just... think you should be nice about it next time."
                hero.say "Uh, sure. Sorry."
                "Bree shakes her head lightly and throws me a small smile, before standing in front of the game."
                "She doesn’t look at me as the screen lights up her face in the darkness of the arcade."
                "She makes a few offhand quips as she starts a new game, but I could tell something was wrong."
        "Persuade":
            $ bree.love += 1
            if hero.knowledge >= 50:
                "The best way to ask was to ask nicely, right?"
                hero.say "Hey, can you let her have a chance?"
                "The girl tears her eyes away from the screen."
                hero.say "..."
                hero.say "Please?"
                "A few seconds pass with a silence that makes me think she didn’t hear me. Until she bursts out laughing."
                unknown_girl_say "You’re so cute! Honestly, you’re adorable. But, really, leave me alone or this will get ugly."
                hero.say "Really?"
                "She shoots both of us a bone chilling glare. In the side of my vision, I see Bree take a step back."
                bree.say "Let’s get out of here."
                hero.say "Fine. We can come back tomorrow."
                unknown_girl_say "I wouldn’t count on that!"
                show bree
                "Bree leads me out of the arcade until we come to the mall’s street."
                "I feel a little bad for not getting the game for her, but there was always tomorrow- whether that bitch likes it or not."
            else:
                hero.say "Hey- listen."
                "I step in front of Bree, facing the girl who was still halfheartedly paying attention to both of us."
                hero.say "This is a public place. You can’t exactly keep people from playing. So you either finish your game or we get the manager and see what he has to say? But we don’t want to get mixed up in that, do we?"
                "For the first time, the girl tears her eyes away from the screen. Her irises are piercing, giving me a glare that probably sends other people running."
                "A moment of silence passes of an intense staring contest, but it breaks once she forcefully grabs her paper cup and shoves the chair out from under her."
                unknown_girl_say "Fine. Whatever. I don’t want to be here anyway."
                "With that, she walks off. I almost think she’ll shoulder check me by the look on her face, but I’m surprised when I’m left alone."
                bree.say "..."
                $ bree.love += 2
                bree.say "Wow! Thanks, [hero.name]! That was, like, super cool."
                hero.say "Yeah, no problem. She was a bitch about it anyway."
                bree.say "Mega bitch."
                "I smile at her wording as she pushes the chair aside and chooses to stand instead."
                "The screen flashes with vibrant colours at the start of a new game."
                bree.say "Will you still coach me a little?"
                "Coaching was a strong word. In fact, she was probably better than me."
                hero.say "Yeah, of course."
        "Stay Out Of It":
            $ bree.love -= 1
            "Something tells me I should stay out of this. In fact, so should Bree. This girl didn’t exactly seem stable."
            bree.say "Hey! You can’t- This is- ..."
            unknown_girl_say "What’s wrong? Dick got your tongue?"
            "Bree turns bright red at this, stuttering at the other girl’s blatant phrasing."
            unknown_girl_say "Ha! I knew it. All you blondes are sluts. Is he your pimp? This is hilarious! Your own pimp can’t even stand up for you!"
            show bree angry
            bree.say "Shut up! Don’t talk about him like that!"
            "Wait, me?"
            hero.say "Bree, maybe we should-"
            unknown_girl_say "He speaks! Tell me, how much did you have to pay her to get with someone that looks like you?"
            "By the end of her sentence, there’s a sudden splash and a screech. I blink, until I realize Bree had turned the girl’s cup upside down on her head."
            "Brown, bubbly liquid, which I can only assume is soda, spills from her hair and down her shirt."
            unknown_girl_say "What the hell!"
            "She stands up, desperately trying to shake herself off. She gives out another shriek of frustration before rushing off in the direction of the bathrooms."
            unknown_girl_say "Bitch!"
            "..."
            "I look over at Bree, whose face is still red, but this time I recognize it at anger."
            hero.say "Um... maybe we should get out of here before she gets back."
            "She numbly nods, regret suddenly crashing over her with the fall of her expression."
            "I take her hand and lead her outside of the arcade. She immediately turns to face me."
            show bree
            bree.say "I’m not like that, [hero.name], I swear! I don’t know what I was thinking."
            hero.say "It’s fine. She had it coming anyway, so I wouldn’t feel too bad."
            "Bree doesn’t look convinced."
            hero.say "You can’t tell me she wasn’t a bitch."
            bree.say "..."
            bree.say "A total bitch."
            "I give her a smile."
            hero.say "How about we head home? We can come back tomorrow."
            bree.say "... Okay."
    hide bree
    return

label bree_pool_throat:
    "Nothing like a relaxing swim by the pool, I say."
    "The sun is shining, there’s no more work to do for awhile."
    "All is good."
    "While I’m getting in my few laps, the door opens up, and out steps Bree."
    show bree swimsuit
    "She’s dressed in a bikini that clings tightly to her body."
    bree.say "Heeey, [hero.name]! Enjoying the weather, too, huh?"
    hero.say "Hey, Bree. You getting in?"
    bree.say "Maybe! I just felt like I should step outside for once, you know, get some air."
    hero.say "Sounds good to me, it's as nice a day as any. Besides, I can't picture a better view."
    show bree swimsuit blush
    bree.say "Hehe, thanks [hero.name]~."
    bree.say "You're really nice sometimes, you know?"
    bree.say "I don't know though, like I've never liked being out in public dressed like this, you know?"
    hero.say "Well it isn't like anyone can see you except me, we're too high up."
    hero.say "Besides, I've already seen everything before."
    "I smirk as Bree gasps playfully, feigning outrage for a few seconds, before giggling with a few shades of rose on her cheeks."
    bree.say "See, this is what I mean, you're always so nice to me for some reason."
    bree.say "I'm not like, complaining or anything It's nice."
    "I smile at her, and she smiles back, then sets up her towel by the side of the pool and lies down."
    bree.say "I am pretty tired though."
    bree.say "Maybe I won't swim, just lie here for a while and do nothing."
    hero.say "Sounds productive."
    bree.say "Heh I'm uh, not very productive..."
    "I consider teasing her for a moment, but I detect a hint of sadness in her tone."
    "I'm not sure why, so I don't push it just in case."
    "Instead I swim over to her, resting by the side of the pool and examining her while she can't see me doing so."
    "Really, I haven't seen her in a swimsuit so close before."
    "I've seen her with plenty less, of course, but still."
    "There's just something about it that makes it titillating, even though it technically covers all the naughty bits."
    "I hope the water will hide my growing erection."
    show bree swimsuit
    bree.say "Hey, [hero.name]?"
    hero.say "Yeah?"
    bree.say "You went quiet, I was just making sure you were still there."
    hero.say "Heh, yeah I'm right here, I wouldn't just abandon you."
    bree.say "...Thank you."
    "She opens her eyes and cranes her head towards me, her grin not her usual but instead that cute little one she gave sometimes."
    "The smaller one, the one that's more genuine than cheerful. The one that makes my heart skip a beat."
    "I can't help but smile back. Leaning over, I plant a soft kiss on her forehead, before beginning to lightly stroke her hair."
    "We stay like that for a little while in silence, before I speak."
    hero.say "Hey, Bree?"
    bree.say "Hmm?"
    "She looks up to me, opening her eyes and raising an eyebrow, clearly wondering what I wanted."
    hero.say "I know I said it before, but seeing you in a swimsuit? Really something to behold."
    "She giggles and begins playing with a strand of her hair, back to her usual trademark grin."
    hero.say "No, I mean it. I know I've seen you with less, but there's really something special about you like this."
    "She doesn't giggle at this. Not because she doesn't like it, but because she's started to pick up on the underlining lust in my voice."
    show bree swimsuit blush
    bree.say "Really?"
    hero.say "Yeah, really."
    bree.say "Well You aren't that bad yourself."
    "There's something else in her gaze now, something I've felt since she walked out of the house."
    "Slowly, I lean over and meet her lips with my own, and what starts as an innocent peck quickly turns into a deep embrace."
    "I stand at my full height, practically looming over her and not only pulling her in closer, but shifting her around as well."
    "She lets me position her at my will, content to let me lead as per usual."
    "Soon, her head is just by the pool while her body stretches towards the house, and now that it's out of the water, she very quickly notices my bulge."
    "I feel like I've done a good job getting across my intentions, so I don't pause to ask for permission as I pull back, breaking the kiss, and shove my shorts down in one movement."
    "Her eyes widen as she sees my rod, but I don't give her much chance to prepare herself."
    "Before she can react, I grab her by the shoulders, pushing myself forwards into her throat."
    show bree pool oral
    "She squeals, her mouth now full of my chlorine cock."
    "Her heels dig into her towel as she rolls about, so I give her a brief respite, pulling back to give her a chance to breathe."
    "After a few seconds, I thrust again."
    "Her hair spreads out as it dips into the water, her face tilted all the way back with her forehead soaking in sweat and the liquid from the pool itself."
    show bree pool oral pain b
    "This gives my dick a straight shot down her mouth and into her throat."
    show bree pool oral a
    "I slowly build up speed, letting her get more used to the intrusion, but my lust begins to get the better of me, and soon enough I'm going as fast as my hips can manage."
    "Her squeals drive me forward as I push myself deeper into that uncharted territory, my hands gripping onto her shoulders and her neck as the bulge in her throat is evidence that I’m filling her up."
    show bree pool oral b throat pain
    "She grabs my sides, squeezing me tightly. Her body remains tense as I block her airway with my dick."
    show bree pool oral a
    hero.say "I'm close now!"
    "I tell her less as a warning, more as an assurance that she'll be back to breathing normally again soon."
    show bree pool oral b throat fx
    "She lets out an affirmative squeal, scratching along my sides."

    show bree pool oral a throat
    "Her suit stains with the wetness that I’m giving her."
    show bree pool oral b throat fx
    "Through the struggle I can see on her face she's getting some sort of enjoyment out of this, that it isn't entirely one sided."
    show bree pool oral a throat
    "Soon enough, I throw my head back, letting out a pleased groan as I shoot off into her."
    show bree pool oral b cum
    "Unfortunately, some of my sperm spits out of her mouth, trailing down towards her nose and her eyes and dripping into the pool."
    show bree swimsuit
    "When I pool back, she coughs, more of the jizz staining the pool."
    "She rubs her throat, groaning as she sits herself up, coughing and spluttering as she tries to get her voice back."
    "But I wrap my arms around her and she gasps, looking over her shoulder in surprise."
    bree.say "Aaah, [hero.name]!?"
    "Her voice is harsh and hoarse voice, but she’s interrupted before she can say anything else, falling into the water with me."
    "She eventually comes back up, looking down over herself, soaked, yet washed of my spunk."
    bree.say "...My throat hurts..."
    "I grin at her and we make eye contact, which is enough for her to giggle and smile in return."
    hero.say "Yeah, guess I could have been more gentle, but where's the fun in that?"
    "She blushes and giggles again, shrugging her shoulders in an exaggerated manner."
    show bree swimsuit blush
    bree.say "Well, I didn't like, hate it..."
    hero.say "I, for one, thoroughly enjoyed it."
    "She smiles, leans in, and pecks me on the cheek. Then splashes me."
    "I'm caught off guard and are left spluttering as Bree attempts to escape without recompense, but I quickly grab her leg and drag her back as she squeals."
    "We spend the next ten minutes playing in the pool, before Bree eventually says that she has to go clean up, and I decide to get out and clean up the mess we made in the pool too."
    return

    return

label bree_give:
    if not "zbox 360" in hero.inventory.keys():
        $ gift = Item("zbox 360",money_cost = 200)
        "She hands me a pretty large box."
        hero.say "Wow !\nIs that a Z-Box?"
        bree.say "It sure is..."
        hero.say "Thank you so much."
    elif bree.love() >= 25 and not "bree's sweater" in hero.inventory.keys():
        $ gift = Equip("bree's sweater", money_cost = 150, effects = {"bree":100,"charm":-5})
        "She hands me a hand knit sweater, a rather failed attempt at a hand knit sweater anymay."
        hero.say "It's beautiful..."
        bree.say "Thanks [hero.name]."
        hero.say "Thank you Bree."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label bree_give_valentine:
    show bree
    "Bree walks hesitantly towards me."
    call bree_greet from _call_bree_greet_7
    show bree blush
    bree.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Bree hands me a box of chocolates."
    hero.say "Thank you, Bree."
    $ hero.gain_item(gift)
    hide bree
    return

label bree_give_birthday:
    show bree
    "Bree walks towards me."
    call bree_greet from _call_bree_greet_8
    show bree happy
    bree.say "Happy birthday [hero.name]!"
    call bree_give from _call_bree_give
    return

label bree_give_christmas:
    show bree
    "Bree walks towards me."
    call bree_greet from _call_bree_greet_9
    show bree happy
    bree.say "Merry christmas [hero.name]."
    call bree_give from _call_bree_give_1
    return

label bree_about_kiss:
    show bree
    "Bree walks toward me."
    call bree_greet from _call_bree_greet_3
    show bree
    bree.say "About that kiss..."
    hero.say "Yes ?"
    bree.say "Could you forget about it ?"
    bree.say "I don't want it to be awkward between us..."
    $ result = renpy.display_menu([("Yes",1), ("No",2)])
    if result ==1:
        hero.say "Sure, It's already forgotten."
        bree.say "Thanks"
        $ bree.love += 1
    else:
        if hero.charm >= 20:
            hero.say "I don't want to, it's too sweet a memory..."
            bree.say "Well, try anyway... Please."
            $ bree.love += 2
        else:
            hero.say "No can do, I am still rock hard thinking about it !"
            bree.say "Jerk !"
            $ bree.love -= 3
    hide bree
    return

label bree_talk_breakup:
    call bree_greet from _call_bree_greet_4
    show bree
    bree.say "I heard you had a bad breakup ?"
    hero.say "Yeah, and then the girl I was in love with chose another man."
    bree.say "Tough luck..."
    hero.say "You don't say, I am afraid I'll never love again..."
    bree.say "You know what Yoda would say ?"
    hero.say "No ?"
    bree.say "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering."
    bree.say "So stop being afraid..."
    bree.say "Be a Jedi."
    hero.say "You do know that a Jedi is forbidden to love."
    bree.say "Yeah, maybe not my best metaphore."
    $ bree.love += 2
    hide bree
    return

label bree_kiss_me:
    call bree_greet from _call_bree_greet_5
    show bree
    if not bree.get_flag_value("kiss"):
        "Bree looks troubled while walking in my direction."
        "She seems to hesitate a little, then leans toward me, she obviously tries to kiss me."
        $ result = renpy.display_menu([("Kiss her",1),("Don't kiss her",2)])
        if result == 1:
            hide bree
            show expression "bree kiss "+bree.get_clothes()
            "Bree kisses me soflty but hungrily. The time stops for a few heartbeat."
            "After some time (I couldn't tell how long), we part."
            if bree.love() >= 60 - hero.charm()/2:
                hero.say "What's the occasion ?"
                bree.say "I felt like giving myself a treat."
                hero.say "Feel free to indulge yourself whenever you feel the need."
            else:
                bree.say "I shouldn't have done that..."
            $ bree.set_flag("kiss",1,"permanent","+")
            $ bree.love += 1
            hide expression "bree kiss "+bree.get_clothes()
        elif result == 2:
            "Bree looks hurt when I push her away."
            $ bree.love -= 1
    else:
        "Bree walks toward me..."
        show expression "bree kiss "+bree.get_clothes()
        "...and kisses me deeply."
        hide expression "bree kiss "+bree.get_clothes()
        show bree
        if bree.love() >= 60 - hero.charm()/2:
            hero.say "What's the occasion ?"
            bree.say "I felt like giving myself a treat."
            hero.say "Feel free to indulge yourself whenever you feel the need."
        else:
            bree.say "I shouldn't have done that..."
        $ bree.love += 1
    hide bree
    return

label bree_get_out:
    if game.from_room != "bathroom":
        show bree angry
        $ bree.set_flag("greeting",True,1)
        if bree.activity["clothes"] == "underwear":
            bree.say "Please can you step out ?"
        else:
            bree.say "I am naked. Please can you step out ?"
        $ bree.set_flag("peeping_tom",1, "day", mod ="+")
        $ peep = bree.get_flag_value("peeping_tom")
        $ bree.love -= peep
        hide bree
    else:
        "I hear a voice through the door."
        if game.room == "bathroom":
            if hero.check_skill("hung"):
                $ bree.love += 1
            bree.say "[hero.name] I need the bathroom, can you step out?"
        else:
            bree.say "[hero.name], can you step out?"
        hero.say "Sure."
    $ game.room = "secondfloor"
    return

label bree_not_get_out:
    $ bree.set_flag("greeting",True,1)
    show bree
    "Bree is naked..."
    hero.say "Sorry, Bree I didn't know you would be here."
    bree.say "You know..., I don't mind if you come in..."
    hide bree
    return

label bree_not_get_out_2:
    $ bree.set_flag("greeting",True,1)
    show bree
    if bree.get_clothes() == "underwear":
        "Bree is in her undies..."
    else:
        "Bree is only wearing a towel..."
    hero.say "Sorry, Bree I didn't know you would be here."
    bree.say "Stop it, we know each other well enough not to be bothered by that..."
    hide bree
    return

label bree_shower_BJ:
    "I usually take a shower in the morning so that I'm fresh for the day ahead, but tonight I was just so worn-out and tired that I felt I needed it."
    "So without any great fuss or ceremony, I just turn on the water, strip off and hop in on my way to crawling into bed at the end of the day."
    "The feeling of the water washing over me and the warmth seeping into my tired limbs is enough to tell me that I'd made the right decision."
    "Even after no more than a couple of minutes in there, I'm more than sure that I'll have no trouble falling into a deep and pleasant sleep as soon as my head hits the pillow."
    "In fact, I'm in so much of a state of relaxation that I hardly notice the sound of the bathroom door opening and someone slipping inside."
    "Normally I'd be pretty attentive to the fact that I've been joined in the middle of a shower like that."
    "But I feel so sleepy and relaxed by now that I just assume it's either Sasha or Bree nipping into the bathroom for some unknown reason and hoping not to be caught in the act."
    "Whoever it is and whatever they're after, I simply decide that, so long as they don't make the fatal error of flushing the toilet, they can do as they please."
    "This means that when I hear the sound of tapping at the glass of the door to the shower cubicle, I yelp and almost jump out of my skin."
    "That kind of a reaction would be embarrassing in of itself in any other circumstances."
    "But as I'm standing inside a shower that's raining water down on me, I instantly find myself slipping and sliding around on the floor, trying to brace myself against equally slippery walls."
    "I don't know if my unexpected visitor was always intent upon making their presence known to me and then letting themselves into the shower, or if apparent state of disorientation sees them coming it my aid."
    show bree naked
    "Either way, almost the same moment that I manage to stop myself slipping and suffering an unpleasant fall, Bree's head appears around the shower door."
    "At the sight of her, I begin to open my mouth, intending to say something that probably won't adequately explain why I just freaked out."
    "But Bree instantly puts a finger to her lips, telling me to keep quiet and waves me back with her other hand."
    "While our shower's not exactly huge, there's still enough room for me to flatten my back against the wall and allow her to step inside comfortably."
    "Only Bree pauses before she does this, letting me see her shoulder her way out of the robe she's wearing and let it fall to the floor."
    "Underneath she's completely naked, the crack of an opening in the shower door enough for me to know that my eyes aren't deceiving me."
    "The effect of sight is enough to ensure that my heart is racing even as she slides the door open just wide enough to step fully into the shower."
    "Even now that she's inside of the shower with me, still Bree doesn't as much as say a single word."
    "Instead she just stands there, letting the water run down her body and soak her hair so that it settles into heavy, honey-coloured locks."
    "I think that I'm beginning to understand a little of what this is all about, as I can't keep from staring at this stunning view of her naked body."
    "Bree's not saying a word because she wants to keep this little encounter between us based on nothing more than the sight of each other and the feelings this stirs inside of us."
    "And it's no great surprise that it's working - well, at least it is from where I'm standing."
    "Bree's doing nothing more suggestive than standing mere inches away from me whilst completely naked, and already I'm starting to stir."
    "As she watches my cock stiffen and begin to stand to attention with what looks like growing delight, I watch her expression just as closely."
    "This means that the more Bree looks at my cock with what can only be mounting anticipation, the more turned on I become in turn."
    "And in this way we seem to be feeding off of each other, becoming ever more aroused so long as neither of us breaks the cycle."
    "But all the same, when Bree finally does so, I can hardly say that it comes as any kind of disappointment."
    "Still keeping her silence, she bites her lip in anticipation and reaches out with one hand to take hold of my cock."
    "She holds it for a moment, and then begins to rub up and down the length of my shaft with a gentle, caressing touch."
    "The water that's constantly cascading over the both of us means that there's no need for any kind of lube."
    "And this also means that Bree can steadily increase the speed and the amount of pressure that she's applying too."
    show shower 2bj bree
    "Up until the very moment that she begins to sink down onto her knees, I had been thinking that I was getting a hand-job and would have been very glad of it."
    "But now I can see Bree's eyes focussing on the head of my cock, and the tip of her tongue sticking out from between her lips in anticipation."
    "And it seems as though I'm about to get far more than I could ever have expected."
    "Especially when all I wanted to begin with was a quick shower before bed!"
    show shower 2bj breemouth
    "I feel a shudder of pure pleasure pass through me as the sensation of Bree's lips and tongue fist caress the very tip of my cock."
    "She could spend as long as she wants doing just that, and I'd be perfectly satisfied."
    "But she apparently has other things in mind, as she takes a full third of my length into her mouth mere moments afterwards."
    "From there, she begins to bob her head back and forth, taking me by surprise with the vigour of her pace."
    "Her eyes are closed and her face shows nothing save for a devotion to the task at hand, cheeks puckering as she sucks as hard as she's able."
    "It's all that I can do to keep from closing my eyes too, from just letting the sensations that Bree's creating inside of me."
    "Instead I reach out and run my hands through her hair, gently holding the sides of her head as she moves."
    "I have no way of knowing if this tactile gesture has any effect whatsoever upon Bree."
    "But for me it's a means of grounding myself and adding another physical element to the experience."
    "All the same, she's taking me so deep now with every rhythmic motion of her head that it can't be long before I cum."
    "That I've lasted so long at all is baffling to me, as I was so weary to begin with that just standing up in the shower felt like a challenge."
    "Bree may have somehow managed to coax a hidden reserve of energy and stamina out of me with her attentions, but that can't last forever."
    hide shower 2bj
    show shower 2bj bree
    "She must feel the onset of my orgasm almost as clearly as I do myself, as she pulls back her head and frees my cock just in time."
    show shower 2bj bree shoot
    "Making no effort to get out of the way, she takes the entirety of my ejaculation full on and in the face."
    show shower 2bj bree facial
    "But all the same, there's only literal seconds to see the cum streaked across her face, as the water washes it away almost as quickly as it lands."
    "Bree remains kneeling in the shower, waiting patiently until the very last drop of evidence is carried down the drain as she's as clean as she was the moment she stepped into the shower to begin with."
    "And once she's spotless, she gets to her feet and lets herself out of the shower, still without uttering a single word."
    "Once Bree has left the bathroom, I can't help but think that it was probably for the best that she did remain silent throughout what she just did to me."
    "As it's a rare thing for a girl to leave a guy lost for words and not get mad when he actually is."
    return

label bree_sasha_threesome_2:
    scene bg bedroom1
    $ sasha.set_flag('sex', 1, 'permanent', '+')
    $ bree.set_flag('sex', 1, 'permanent', '+')
    show bree naked
    show sasha naked
    "As much as there's the excitement and thrill of living out a threesome, there's also always a faint feeling of unspoken tension hanging over it all too."
    "How could there not be, especially when the genders of the people involved means that you have two of one thing and one of the other to go around?"
    "No one ever talks about it beforehand, probably wouldn't even if they had the chance for fear of looking like they were trying to steal the lion's share for themselves."
    "But I can always feel the slight sense of competition between Bree and Sasha before we get up to something as a trio."
    "Neither of them would admit it, but they're both wondering just who's going to be the one to get to ride my dick."
    "For my part, I know that I should probably make sure that harmony is achieved and that nobody ends up feeling left out."
    "But I'm only human - how can I pretend that knowing two such hot girls are basically trying to outdo each other for that same reason?"
    "I feel like that right now, with the door to my room firmly closed behind us and the girls stripping off in front of me."
    "As I take off my own clothes, I can't help feeling like some kind of prize stallion that's having broody mares paraded in front of him."
    "Each one of them is enough to make me desperate on their own, but together it's going to be almost impossible to choose between them."
    "In the end, I'm, just going to have to come down and make a choice, for better or worse."
    "It's just then that I catch the twinkle in Sasha's eye."
    "Maybe it's nothing more than my imagination, desperately looking for an excuse to pick one over the other."
    "But there seems to be something darker and more sultry in Sasha's gaze - spice as opposed to Bree's own delightful sweetness."
    "Whether I'm right or wrong, I'll go with that."
    "If I wait and ponder it any longer, I'm afraid that the moment will pass and the mood die completely."
    if sasha.get_flag_value("pregnant") >= 9:
        "Sure, Sasha didn't have much trouble turning me on before she fell pregnant - after all, one kind of followed on from the other!"
        "But there's just something about the sight of her with that big, round belly that makes me want to do it all over again."
        "As I take her by the hand and make it plain that I want her in front of me, back to belly, she sways like a beautifully ripe fruit."
        "Once she's standing in front of me, I feel as though I'm about to have sex with a primeval fertility icon brought magically to life."
    elif sasha.get_flag_value("boobjob"):
        "Don't get me wrong, I love the natural size and shape of Bree's breasts."
        "But there's just something so wonderfully fake and dirty about the implants that pump Sasha's up to a comparable size."
        "As I take her by the hand and make it plain that I want her in front of me, back to belly, they bounce and sway like rubber balls."
        "Even when she's got her back to me, I can still see them sticking out in front of her!"
    elif sasha.get_flag_value("haircut"):
        "I reach out and take hold of Sasha's hand, leading her to stand before me and then turn her back."
        "Her ass is mere inches away from my already rising cock, and I can see the black roots of her blonde hair up close."
        "I don't know exactly why, but the sight of where the black meets the blonde always gets me worked up."
        "Maybe it's because it makes her look so delightfully trashy and cheap..."
    elif bree.get_flag_value("collared") and sasha.get_flag_value("collared"):
        "Bree and Sasha are obediently standing before me in their collars, a fact that should make the whole thing that much easier."
        "But still it feels a hard decision to make as I take hold of Sasha's lead and make it plain that she's the one I'm set on actually fucking tonight."
        "While she looks instantly delighted to have been chosen, I can see Bree trying to hide her disappointment so as not to be guilty of spoiling the moment."
        "Maybe that's what inspires me to be a little more forceful than I might otherwise have been as I tug Sasha's lead to have her trot around in front of me."
    "Eager to begin, Sasha clambers hastily onto the bed before me, looking back over her shoulder to be sure that I'm following."
    "She need not have worried in the slightest, as her thighs moving in this way means that I'm treated to an intimate view of what lies between them."
    "Even though we've hardly begun, I can see that her lips are becoming ever more slick in anticipation."
    "In fact, I swear that I can almost hear them make a liquid sound as she moves."
    "And right now, there's nowhere that I want to be more than right spot right there."
    "In all, Sasha can't be more than a couple of feet onto the bed before I'm up and after her."
    hide bree
    hide sasha
    show breeSasha threesome out
    "I catch her none to gently around the waist, taking her in a firm grip that makes it clear I don't intend for her to go any further."
    "She yelps in genuine surprise at the feel of me grasping her and taking full control of the proceedings."
    "But I also not with the faint beginnings of a smile that she offers no protests and makes no effort to break my hold upon her."
    "Keeping my hands in the same position as they were when I grabbed her a moment before, I now pull Sasha back towards me."
    "At the same time I thrust myself forwards to meet her, trusting to the design of nature to ensure that my aim is true."
    "For a second to two I think that my cock is going to go straight up her ass."
    show breeSasha threesome pussy
    "But then I feel the slick sensation of her pussy, and it spurs me to push on even more hastily than before."
    "I don't enter Sasha in the most gentle or smooth of motions, but this isn't an occasion for subtle entrances."
    "Even though she's already more than a little wet in anticipation, I still need to keep up the pressure and push hard to make it in one go."
    "As I show no signs of mercy to Sasha, I comfort myself with the clear evidence that she's liking this kind of treatment."
    "All the while she's gasping and moaning in what can only be a rough and breathtaking kind of pleasure."
    "And there's going to be plenty more of that kind of treatment to come, as the rough push to get inside of her has made me hungry for more of the same."
    "With every single thrust that I make into her, I feel like I'm trying to fill Sasha's pussy and get as deep in as possible."
    "Each movement of mine seems to shake her to the core, sending quivers and spasms through her muscles."
    "By now her moans have begun to turn into cries, and she's making them completely in time with my thrusts in and out of her."
    "I've been so distracted by Sasha, that when I feel someone leaning in close to, stroking my belly with their hands, I almost flinch in surprise."
    "Luckily for me, Bree sees the funny side of this, and begins to chuckle gently as she continues to caress me in the hope of getting some attention for herself."
    "I instantly feel bad for having almost forgotten that she was even in the room with us, let alone supposed to be a partner in our love-making."
    show breeSasha threesome bree
    "Unable and more than a little unwilling to be distracted from what I'm doing with Sasha, I let go of her waist with one hand and reach out towards Bree."
    "Guided more by instinct than anything else, I feel for the space between her thighs."
    "Luckily for me, I find my hand gripped firmly and pulled straight towards what had been my ultimate goal."
    "All I can say is that she must have been getting pretty excited from simply watching Sasha and I go at it."
    "Bree's crotch is wet and warm to the touch, and she wastes no time in pressing my fingers against her lips with almost desperate force."
    "Before it feels like any amount of time has passed, my fingers are finding their way ever deeper into her pussy."
    "Unable to fully divide my attention between the two tasks, I find myself pushing into Sasha and rubbing away at Bree with one single rhythm."
    "I can't honestly tell if Sasha senses a change in that same rhythm as I'm forced to accommodate Bree's needs, or else hears the other girls own sounds of pleasure."
    show breeSasha threesome out
    "Either way, she shifts beneath me and I can't keep my cock from slipping out of her pussy as she does so."
    "At first I can only think that she must be annoyed at losing the largest share of my attention."
    show breeSasha cumshot suck
    "But then she surprises me, and probably Bree too, by pushing her down onto the bed and leaning over her to snatch my cock into her own mouth."
    "The sudden change from being the one making the effort to please two other people to having one of them pleasuring me alone is sharp and sudden."
    "It's all that I can do to keep from losing it the moment that Sasha's lips close around the head of my dick."
    "She must sense that this means I'm about to cum, as she quickly releases me and waits poised for the climax."
    "But even so, there's no way to tell just what she intends to do when it finally arrives."
    if sasha.sub > bree.sub:
        "Much to my surprise, and again to Bree's too, Sasha backs off just enough to let me cum all over the other girl's chest."
        "Bree yelps and laughs in genuine surprise as the warm cum spurts and sprays onto her naked breasts."
        show breeSasha cumshot lick cum
        "But even before I've finished losing myself over the prostrate female form before me, Sasha leans back in again."
        "This time she has her tongue out and ready, wasting no time in licking away at the lines of sticky, white fluid running down Bree's breasts."
        "Each and every mouthful that she laps up is a sensual experience for the both of them, as Sasha is sure to pay close attention to not missing a single drop."
        "She chases the cum around Bree's nipples, between both breasts and finally down her stomach, swallowing each mouthful with relish."
    else:
        show breeSasha cumshot suck cum
        "Sasha surprises us both with her skill, if not as to her intentions, when she somehow manages to catch most of the cum in her mouth."
        "Only the smallest amount either misses her lips to spatter onto Bree's chest below, or else dribbles down Sasha's chin."
        "But then she looks down at the other girl with a mischievous smile on her face, lowering her head until they're mere inches apart."
        "Bree opens her mouth, meaning to ask what Sasha's up to, and that's all the opportunity that she needs for what comes next."
        show breeSasha cumshot spit cum
        "Quick as a flash, Sasha spits the mouthful of cum between Bree's open lips, making her eyes bulge wide with shock."
        "It's all that Bree can do to cough and splutter the second-hand cum down before it hits the back of her throat and chokes her."
    hide breeSasha
    "Though I'm exhausted and drenched in sweat by the time the whole thing is over, I still feel that I can't be nearly as spent as either Bree or Sasha."
    "Both are sprawled on the bed before me, bathed not only in their own perspiration, but a good amount of my own cum as well."
    "I don't bother to offer any invitations or suggest that they stay to sleep in my room if they like, as I'm frankly too tired to care."
    "All I want to do is find a portion of the bedclothes that we haven't completely soaked between the three of us and collapse."
    "Finding both or either of them by my side when I finally wake up would be a plus, but I'm not about to let the thought of it's likelihood keep me awake even a second longer."
    return

label bree_sasha_threesome:
    scene bg bedroom1
    $ sasha.set_flag('sex', 1, 'permanent', '+')
    $ bree.set_flag('sex', 1, 'permanent', '+')
    "It still feels bizarre to me to have come to the point where I'm living with two very different, but equally desirable women."
    "Even more so that my luck has turned around to the degree that not one, but both of them are also involved in a sexual relationship with me."
    show bree naked blush at left
    show sasha naked blush at right
    "A part of me can't keep from glancing from Bree to Sasha and back as they recline, naked on the bed waiting for me to join them."
    "Seeing me hesitate, they chuckle wickedly and shoot each other a conspiratorial look."
    bree.say "What are you waiting for?"
    sasha.say "Yeah - I promise we will bite!"
    "I climb onto the bed between them, still not sure where to look thanks to the appealing nature of each girl waiting for me."
    "Before I can decide where to start, Bree and Sasha rise to their knees."
    "Bree comes at me from the left and Sasha from the right, leaning in to kiss me at the corners of my mouth."
    "Neither of them kisses me full on the lips, but instead they tease me with their tongues and then begin to move downwards."
    "At the same time, I can feel their breasts brushing against my chest, and I reach out to take one from each girl in my hands."
    "Pinching and squeezing at their nipples, I enjoy the subtle differences in feel between the two breasts as I massage them."
    "Bree moans in appreciation as I twist her nipple between my fingers, and Sasha gives a delighted growl."
    "For a moment, the three of us are held there, just enjoying the sensations of each other."
    "But I can feel myself getting stiff and the heat from the girls is almost palpable in the air."
    "There's no way that this is going to be just a matter of kisses and the fondling of breasts, and everyone knows as much."









    "Suddenly there are hands, lips and bodies everywhere."
    "No one seems to be taking control, so I decide to push for what I want right there and then."
    menu:
        "Sasha eat Bree out":
            "As if Sasha and I are communicating on a psychic level, I press Bree's shoulders down while she does the same with her legs."
            "Bree doesn't resist, her eyes instead focused on my dick as it now hovers over her face."
            hide sasha
            show bree pool oral bedroom naked
            "I take hold of her head and gently guide her mouth as she takes the tip inside."
            show bree pool oral bedroom open sasha naked
            "Just as I start to feel the unbelievable sensation of her tongue snaking around the head, Sasha leans herself towards Bree's lower lips."
            "I watch as the other girl begins to tease and tickle Bree with her tongue, expertly probing and licking, more with each passing second."
            show bree pool oral bedroom open sasha squirt naked
            "Unable to see what is being done to her, I feel Bree's body shudder from the pleasure, making her attentions to me all the more intense and unpredictable."
            "I feel guilty to admit it, but part of me feels as though it's Sasha using her mouth on me, like we've turned Bree into nothing more than a human toy for our own pleasure."
            show bree pool oral bedroom open sasha cum naked
            "Shamefully turned on by the mere thought, I can't keep myself from cumming sooner than I wanted."
        "Sasha use a strap-on on Bree" if bree.sub >= 25:
            hide bree
            hide sasha
            show bree doggy
            "I guide Bree down onto all fours and she doesn't resist me, her eyes instead fixated on my cock as it hangs before her face."
            "Before she can reach out for it with either her hands or lips, Sasha comes up behind her, taking hold of her arms."
            "Bree's cheeks redden at the sudden realisation she's being forced into a submissive role, but we press on regardless of her reaction."
            show bree doggy suck
            "As Sasha forces her forwards and she accepts my dick into her open mouth, it's only then that I see the other girl has hastily strapped something around her own waist and groin."
            show bree doggy suck sasha scream
            "Sasha grins wickedly at me over Bree's back as she lowers the impressively-sized strap-on she's wearing and pushes from the opposite direction."
            "Bree's shocked whimperings of surprise translate into an unpredictable and yet exciting sensation for me, as she moans around my dick."
            "Sasha enthusiastically makes use of the strap-on, thrusting away inside of Bree until she's covered in a sheen of sweat from the effort."
            show bree doggy suck sasha ahegao
            "We lock eyes, both majorly aroused by the way in which we're using Bree as a vessel for our own pleasure."
            show bree doggy deep pull sasha ahegao
            "I use the last of my energy to thrust myself still further into Bree's throat, so that she had no choice but to accept it."
            show bree doggy deep pull cuminmouth sasha ahegao
            "Moments later, I feel myself losing it and releasing all that I have in one go."





















    hide bree
    "Nobody speaks as we lie in a slick pile of bodies and limbs, cooling rapidly but still feeling the aftershocks."
    "They say that people only complain if they're unhappy with the service."
    "So I'm happy to read the silence in the bedroom as quiet satisfaction on the part of Bree and Sasha."
    "I know for sure that I have no reason whatsoever to complain."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
