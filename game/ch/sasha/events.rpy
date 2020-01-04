init python:
    Event(**{
        "name": "sasha_get_out",
        "label": ["sasha_get_out"],
        "duration": 0,
        "priority": 1000,
        "game_conditions":{"room":["bathroom","bedroom3"], "flag_female":0},
        "girls_conditions": {"sasha":{"max_love":139,"clothes": "naked", "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": False,
        "once_hour": False,
        })

    Event(**{
        "name": "sasha_get_out_2",
        "label": ["sasha_get_out"],
        "duration": 0,
        "priority": 1000,
        "game_conditions":{"room":["bathroom","bedroom3"], "flag_female":0},
        "girls_conditions": {"sasha":{"max_love":100,"clothes": ["underwear","towel"], "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": False,
        "once_hour": False,
        })

    Event(**{
        "name": "sasha_not_get_out",
        "label": ["sasha_not_get_out"],
        "duration": 0,
        "priority": 200,
        "game_conditions":{"room":["bathroom","bedroom3"], "flag_female":0},
        "girls_conditions": {"sasha":{"min_love":140,"clothes": "naked", "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": True,
        })

    Event(**{
        "name": "sasha_not_get_out_2",
        "label": ["sasha_not_get_out_2"],
        "duration": 0,
        "priority": 200,
        "game_conditions":{"room":["bathroom","bedroom3"], "flag_female":0},
        "girls_conditions": {"sasha":{"min_love":100,"clothes": ["underwear","towel"], "present":True, "not_activity":"sleep", "valid":True}},
        "do_once": True,
        })

    Event(**{
        "name": "sasha_b_event_01",
        "label": ["sasha_b_event_01"],
        "priority": 500,
        "conditions":['game.room == "livingroom"', "game.hour >= 9 and game.hour <= 19", "game.get_flag_value('female')==0"],
        "duration": 1,
        "do_once": True,
        })

    Event(**{
        "name": "sasha_event_coffee",
        "label": ["sasha_event_coffee"],
        "priority": 500,
        "game_conditions":{"activity":["date_coffee"], "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True, 'present':True, "not_activity":"sleep", "min_love":50, "flag_cheated": False}},
        "do_once": True,
        })

    Event(**{
        "name": "sasha_sub_event_1",
        "label": ["sasha_sub_event_1"],
        "priority": 500,
        "game_conditions":{"room":["kitchen"], "activity":"interact", "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True,"active": True, "not_activity":"sleep", "min_love":125, "min_sub":75, "flag_cheated": False}},
        
        "do_once": True,
        })

    Event(**{
        "name": "sasha_event_04",
        "label": ["sasha_event_04"],
        "priority": 500,
        "game_conditions":{"room":["livingroom"], "activity":"interact", "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True,"active": True, "not_activity":"sleep", "min_love":25, "flag_cheated": False}},
        
        "do_once": True,
        })

    Event(**{
        "name": "sasha_event_05",
        "label": ["sasha_event_05"],
        "priority": 500,
        "game_conditions":{"room":["livingroom"], "activity":"interact", "done":"sasha_event_05", "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True,"active": True, "not_activity":"sleep", "min_love":50, "flag_cheated": False}},
        
        "do_once": True,
        })

    Event(**{
        "name": "sasha_event_01",
        "label": ["sasha_event_01"],
        "priority": 500,
        "game_conditions":{"room":["bedroom1"], "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True,"room":"pool", "not_activity":"sleep", "activity":"sunbath", "min_love":50, "flag_cheated": False}},
        
        "do_once": True,
        })

    Event(**{
        "name": "sasha_b_event_02",
        "label": ["sasha_b_event_02"],
        "duration": 1,
        "priority": 500,
        "do_once": True,
        "conditions":['9 <= game.hour <= 24', "game.room in ['secondfloor','bedroom3']"],
        "girls_conditions": {"sasha":{"valid":True,"room":"bedroom3", "not_activity":"sleep", "flageq_story":1, "flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_b_event_03",
        "label": ["sasha_b_event_03"],
        "duration": 1,
        "priority": 500,
        "do_once": True,
        "game_conditions": {"room":["pub"]},
        "girls_conditions": {"sasha":{"valid":True, "present":True, "flageq_story":2, "flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_b_event_04",
        "label": ["sasha_b_event_04"],
        "duration": 1,
        "do_once": True,
        "priority": 500,
        "game_conditions": {"hours":(18,24),"room":["secondfloor","bedroom3"], "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True,"room":"bedroom3", "not_activity":"sleep", "flageq_story":3, "min_love":60, "flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_band_event_01",
        "label": ["sasha_band_event_01"],
        "duration": 4,
        "priority": 500,
        "do_once": True,
        "game_conditions": {"hours":(20,21),"room":["map"],"days":"5", "flagmin_band":1, "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True, "flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_band_event_02",
        "label": ["sasha_band_event_02"],
        "duration": 4,
        "priority": 500,
        "do_once": True,
        "game_conditions": {"hours":(20,23),"room":["pub"],"days":"5", "flagmin_performance":1, "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True, "flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_give_birthday",
        "label": ["sasha_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday"},
        "girls_conditions": {"sasha":{"min_love":50, "flag_cheated": False}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "sasha_give_valentine",
        "label": ["sasha_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine"},
        "girls_conditions": {"sasha":{"min_love":100, "flag_cheated": False}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "sasha_give_christmas",
        "label": ["sasha_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas"},
        "girls_conditions": {"sasha":{"min_love":50, "present":True, "valid":True, "flag_cheated": False}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "sasha_practice_01",
        "priority": 500,
        "label": ["sasha_practice_01"],
        "duration": 0,
        "game_conditions":{"activity":["practice"],"flagmin_bandpractice":25,"flag_dateinprogress":False, "flag_female":0},
        "girls_conditions": {"sasha":{"min_love":50,"present":True,'valid':True, "flag_cheated": False}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "scottie_appears",
        "priority": 500,
        "label": ["scottie_appears"],
        "duration": 1,
        "game_conditions":{"room":["livingroom"], "days_played":7, "flag_female":0},
        "girls_conditions": {"sasha":{"present":True,'valid':True, "flag_cheated": False}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "sasha_scottie_talk",
        "priority": 500,
        "label": ["sasha_scottie_talk"],
        "duration": 1,
        "game_conditions":{"flag_female":0, "done":"scottie_appears"},
        "girls_conditions": {"sasha":{"present":True,'valid':True, "max_love": 99, "flag_scottieDelay":0, "flag_cheated": False}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "sasha_threesome_request",
        "priority": 500,
        "label": ["sasha_threesome_request"],
        "duration": 0,
        "game_conditions":{"room":["livingroom"], "days_played":14, "flag_female":0, "done":"scottie_appears"},
        "girls_conditions": {"sasha":{"present":True,'valid':True, "max_sub":24, "min_sub":-25, "flagmin_sex":1, "min_love":150, "flag_cheated": False}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "sasha_threesome_confrontation",
        "priority": 500,
        "label": ["sasha_threesome_confrontation"],
        "duration": 0,
        "game_conditions":{"activity":["interact"],"flag_sashathreesomedelay":False,"flag_dateinprogress":False, "flag_female":0, "done":"kleio_and_anna"},
        "girls_conditions": {"sasha":{"present":True,'valid':True, "flag_cheated": False}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "kleioannafoursome",
        "priority": 500,
        "label": ["kleioannafoursome"],
        "duration": 1,
        "game_conditions":{"flag_dateinprogress":False, "flag_female":0, "hours":(20,22), "room":["livingroom"]},
        "girls_conditions": {"sasha":{'valid':True,"flag_kleioannafoursome":True, "flag_cheated": False}},
        "do_once":True,
        "quit": True
        })


    Event(**{
        "name": "kleioannafoursome2",
        "priority": 500,
        "label": ["kleioannafoursome2"],
        "duration": 1,
        "game_conditions":{"flag_dateinprogress":False, "flag_female":0, "hours":(22,24), "room":["studio"], "done":"kleioannafoursome"},
        "girls_conditions": {"sasha":{'valid':True, "present":True, "flag_cheated": False},"anna":{'valid':True, "present":True},"kleio":{'valid':True, "present":True}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name":"sasha_init",
        "label": ["sasha_init"],
        "game_conditions":{"flag_female":1},
        "girls_conditions": {"sasha":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "sasha_likes_blondes_1",
        "label": ["sasha_likes_blondes_1"],
        "duration": 1,
        "do_once": True,
        "quit": True,
        "priority": 500,
        "game_conditions": {"hours":(20,24),"room":["livingroom"], "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True, "present":True, "min_love":125, "flag_cheated": False},"bree":{"valid":True, "present":True}}
        })

    Event(**{
        "name": "sasha_likes_blondes_2",
        "label": ["sasha_likes_blondes_2"],
        "duration": 2,
        "do_once": True,
        "quit": True,
        "priority": 500,
        "game_conditions": {"hours":(20,24),"room":["livingroom"], "flag_female":0, "flag_LikesBlondes":True},
        "girls_conditions": {"sasha":{"valid":True, "present":True, "min_love":130, "flag_cheated": False}}
        })


    Event(**{
        "name": "sasha_likes_blondes_3",
        "label": ["sasha_likes_blondes_3"],
        "duration": 0,
        "do_once": True,
        "priority": 500,
        "game_conditions": {"flag_female":0, "done":"sasha_likes_blondes_2", "flag_LikesBlondesDelay":False, "flag_LikesBlondes":False},
        "girls_conditions": {"sasha":{"valid":True, "flag_cheated": False}}
        })


    Event(**{
        "name": "sasha_breast_complex_1",
        "label": ["sasha_breast_complex_1"],
        "duration": 1,
        "do_once": True,
        "priority": 500,
        "game_conditions": {"hours":(20,24),"room":["livingroom"], "flag_female":0},
        "girls_conditions": {"sasha":{"valid":True, "min_love":50,"flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_breast_complex_2",
        "label": ["sasha_breast_complex_2"],
        "duration": 1,
        "do_once": True,
        "priority": 500,
        "game_conditions": {"seasons":"01","room":["pool"], "flag_female":0, "done":"sasha_breast_complex_1"},
        "girls_conditions": {"sasha":{"valid":True, "min_sub":75, "min_love":100,"flag_cheated": False},"bree":{"valid":True, "present":True, "clothes":"swimsuit"}}
        })

    Event(**{
        "name": "sasha_breast_complex_3",
        "label": ["sasha_breast_complex_3"],
        "duration": 1,
        "do_once": True,
        "priority": 500,
        "game_conditions": {"room":["bathroom"], "flag_female":0, "done":"sasha_breast_complex_2"},
        "girls_conditions": {"sasha":{"valid":True, "min_love":150, "flagmin_sex":1, "present":True,"flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_breast_complex_4",
        "label": ["sasha_breast_complex_4"],
        "duration": 1,
        "do_once": True,
        "priority": 500,
        "game_conditions": {"flag_BreastComplexDelay":False, "done":"sasha_breast_complex_3"},
        "girls_conditions": {"sasha":{"valid":True, "present":True, "flag_BreastComplex":1,"flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_breast_complex_5",
        "label": ["sasha_breast_complex_5"],
        "duration": 1,
        "do_once": True,
        "priority": 500,
        "game_conditions": {"room":["livingroom"], "hours":(10,18), "flag_BreastComplexDelay":False, "done":"sasha_breast_complex_4"},
        "girls_conditions": {"sasha":{"flag_BreastComplex":1,"flag_cheated": False}}
        })

    Event(**{
        "name": "sasha_kiss_me",
        "label": ["sasha_kiss_me"],
        "duration": 0,
        "max_girls": 1,
        "girls_conditions": {"sasha":{"min_love":150,"present":True, "valid":True,"flag_cheated": False}},
        "game_conditions":{"flag_female":0, "chances":20},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "sasha_pregnant_flag",
        "label": ["sasha_pregnant_flag"],
        "duration": 0,
        "girls_conditions": {"sasha":{"flagmin_pregnant":1}},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "sasha_preg_talk",
        "label": ["sasha_preg_talk"],
        "duration": 0,
        "girls_conditions": {"sasha":{"flagmin_pregnant":6, "flag_toldpreg":False,"flag_cheated": False}},
        "game_conditions":{"flag_dateinprogress":False, "flag_female":0},
        "once_day":True,
        "do_once":False,
        "quit": False,
        })

    Event(**{
        "name": "bree_sasha_bitches_1",
        "label": ["bree_sasha_bitches_1"],
        "duration": 0,
        "girls_conditions": {"sasha":{"flag_collared":1, "min_sub":90,"flag_cheated": False},"bree":{"flag_collared":1, "min_sub":90}},
        "game_conditions":{"flagmin_homeharem":1, "flag_female":0, "activity":"watch_tv_with_everyone"},
        "do_once":True,
        "quit": True,
        })

    Event(**{
        "name": "bree_sasha_bitches_2",
        "label": ["bree_sasha_bitches_2"],
        "duration": 0,
        "girls_conditions": {"sasha":{"flag_collared":1, "min_sub":100,"flag_cheated": False},"bree":{"flag_collared":1, "min_sub":100}},
        "game_conditions":{"flagmin_homeharem":1, "flag_female":0, "activity":"watch_tv_with_everyone", "done":"bree_sasha_bitches_1"},
        "do_once":True,
        "quit": True,
        })

    Event(**{
        "name": "sasha_event_bree_shower",
        "label": ["sasha_event_bree_shower"],
        "duration": 1,
        "game_conditions": {"flag_dateinprogress": False, "flag_female": 0, "hours": (20, 22), "room": ["bedroom1"]},
        "girls_conditions": {"sasha": {"flagmin_lesbian": 10}, "bree": {'flagmin_lesbian': 10, 'valid': True}},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "sasha_ending",
        "priority": 500,
        "label": ["sasha_ending"],
        "duration": 0,
        "game_conditions":{"days":"56", "flag_female":0},
        "girls_conditions": {"sasha":{'valid':True, "flag_engagedmike":1, "flag_cheated": False}},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "sasha_nightclub_showdown",
        "label": ["sasha_nightclub_showdown"],
        "duration": 1,
        "game_conditions": {"flag_female": 0, "hours": (20, 25), "room": ["date_nightclub"]},
        "girls_conditions": {"sasha": {"flagmin_sex": 1, "present":True, "max_sub":75}, "audrey": {'flagmin_sex': 1, 'valid': True, "room":"nightclub"}},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "sasha_piss_off",
        "label": ["sasha_piss_off"],
        "duration": 0,
        "game_conditions": {"activity": "interact"},
        "girls_conditions": {"sasha": {"flag_cheated": True}},
        "do_once": False,
        "once_hour": False,
        "quit": True
    })

    Event(**{
        "name":"sasha_shower_BJ",
        "label": ["sasha_shower_BJ"],
        "duration": 1,
        "game_conditions": {
            "activity":["shower"],
            "flag_female":0,
            "hours":(20,25)
            },
        "girls_conditions": {"sasha":{"min_love":150,"present":True, "valid":True, 'flagmin_sex':1, 'min_sub':50}},
        "once_week": True,
        "once_day": False,
        "do_once": False,
        "quit": True
        })

label sasha_bondage_sex:
    scene bg bedroom1






    show sasha foreplay rope
    "I tie Sasha up, using a length of rope to create a series of intricate knots across her body."
    "It snakes around her neck, chest and hips, encircling her breasts and even the space between her legs."
    "We're both already naked at this point, with her standing in front of a full-length mirror."
    sasha.say "That's it, pull it up and then tie it off, right...there!"
    "She's supposedly using the mirror to guide my efforts, but it's obvious that she's getting off on the sight of herself being trussed up."
    "I can feel the heat emanating from her body and see the way her cheeks are flushing a deep red."
    "It seems oddly contradictory to see such an outwardly strong and feisty woman being turned on by being in a compromising, even belittling situation."
    "But I can't say that it's not working for me as well, and Sasha's eyes keep stealing towards my dick as it responds in kind."
    "Sasha clambers onto the bed, looking at me the whole time with wide, expectant eyes."
    "She kneels down facing me, then moves onto all fours."
    "Sasha's eyes are huge and her expression seems to be urging me to make a move."
    "For a moment I'm lost, used to being wowed by her looks and astonishing body."
    "But then I remember, this is about something else entirely, and I swallow hard before jumping into, what I hope she's expecting."
    hero.say "What are you waiting for, instructions with a slideshow?!?"
    "Sasha's eyes widen at the brusqueness of my tone, but she eagerly shuffles forwards on her hands and knees."
    hero.say "Lips and tongue!"
    show sasha bj rope mike dickout
    "I feel bad for speaking to Sasha like this, but I try to tell myself that the rules are different here."
    "Not needing to be told twice, she begins to kiss and lick eagerly at the tip of my dick."
    show sasha bj rope mike dickin
    "Soon she's swallowing the shaft as much as she's able to manage, the indignity of her situation making her work all the harder."
    hero.say "Keep it up, that's right...this'll teach you what your mouth's really good for."
    "I worry about going too far, but every word seems to make Sasha even more dogged in her attentions."
    "Soon I can feel myself starting to lose control, beginning to cum."
    menu:
        "Cum in her mouth":
            $ sasha.sub += 1
            "The feeling of her tongue around my dick and her bound breasts against my thighs is just too much."
            show sasha bj rope mike dickin cum
            "Without a single thought for the consequences, I let myself go inside of Sasha's mouth."
            "She coughs and begins to gag, but I take hold of her head, figuring this is all part of the bondage experience."
            hide sasha
            show sasha rope
            if hero.fitness < 75:
                $ sasha.sub -= 3
                sasha.say "I think that's enough for one night, [hero.name]!"
                "I look disappointed at that, but Sasha shakes her head and smiles."
                sasha.say "Don't look so downhearted, man - it was your first time, you're allowed to be a bit overwhelmed!"
                return
            else:
                hero.say "Don't just lie there panting like a bitch on heat!"
                hero.say "We're not done until I tell you we're done!"
                "Sasha keeps on playing the part of the submissive, but I can see the spark in her eye at the thought of there being more ahead."
        "Cum on her face":
            $ sasha.sub += 2
            show sasha bj rope mike dickout
            "Not wanting to cum in her mouth, I pull my dick hastily out from between Sasha's lips."
            "Surprised by the move, she nips at the tip with her teeth."
            show sasha bj rope mike dickout cum
            "The unexpected gesture is all that's needed to tip me over the edge, and I loose myself instantly over her shocked face."
            show sasha bj rope mike dickout cumafter
            "Both of us are panting now, red-faced and overcome by the excitement of what we've just done."
            hide sasha
            show sasha rope
            if hero.fitness < 75:
                $ sasha.sub -= 3
                sasha.say "I think that's enough for one night, [hero.name]!"
                "I look disappointed at that, but Sasha shakes her head and smiles."
                sasha.say "Don't look so downhearted, man - it was your first time, you're allowed to be a bit overwhelmed!"
            else:
                hero.say "Don't just lie there panting like a bitch on heat!"
                hero.say "We're not done until I tell you we're done!"
                "Sasha keeps on playing the part of the submissive, but I can see the spark in her eye at the thought of there being more ahead."
        "Don't cum" if hero.fitness >= 50:
            "I could easily give in and lose it here and now."
            "But the thought of just how aroused and biddable Sasha seems to be keeps me from letting go."
            hide sasha
            show sasha rope
            "With a massive dose of willpower, I manage to hold on and pull my dick out from between Sasha's eager lips."
    "Both of us are panting now, red-faced and overcome by the excitement of what we've just done."
    "As Sasha waits obediently on the bed before me, I take a moment to plan my next move."
    menu:
        "Use protection" if hero.has_condom():
            $ CONDOM = True
            $ hero.lose_condom()
            "Snatching up a condom from the bedside table, I roll it on as Sasha eyes my dick in barely concealed anticipation."
        "Do not use a condom":
            $ CONDOM = False
            "I glance at the condoms on the bedside table, but they feel out of keeping with the whole bondage vibe, so I decide to push on bareback instead."
    "I motion for Sasha to come closer as I decide what's in store for her."
    "She crawls towards the edge of the bed, clearly eager to see what fate awaits her."
    menu:
        "Standing":
            $ P = "s"
            scene bg bedroom1
            show sasha stand rope
            "Remembering the way Sasha looked at herself in the full-length mirror, I pull her off of the bed and onto her feet."
            "She offers no resistance as I take hold of her arms behind her back and bend her over until her face is almost touching the glass."
            show sasha stand rope dickin
            "Sasha moans deeply as I position myself just right and then pull her bodily backwards."
            "Impaled on my awaiting dick, she stares at her own reflection as I sink into her."
            "I thrust forwards almost with a rowing motion, before loosening my grip and allowing her to sag forwards."
            "Sasha is almost screaming now, each one coming in time with my own movements."











        "Missionary" if not "anal beads" in hero.inventory.keys() and sasha.love >= 180 and not CONDOM:
            $ P = "m"
            scene bg bedroom1
            show sasha missionary rope
            "I push Sasha roughly backwards without a moment's hesitation, sending tumbling onto the bed."
            "Following a step behind, I pin her shoulders with my hands even as I use my legs to part her thighs."
            show sasha stand rope fuck
            "I see no sense in waiting for a moment, so I simply steer myself between Sasha's legs and into her waiting lips."
            "She gives a slight whimper of arousal as I push as far as I am able into her, and then I pause perhaps an inch from her."
            show sasha stand rope sashacum
            "I can feel the rope rubbing against the sides of my dick as I start to move, adding to the feel of her contrastingly soft folds."
            "All the while Sasha simply lays back and takes whatever I have to give her, clearly enjoying the submissive role into which she has been forced."
        "Missionary" if "anal beads" in hero.inventory.keys() and sasha.love >= 180 and not CONDOM:
            $ P = "m"
            scene bg bedroom1
            show sasha missionary rope
            "With one hand I push Sasha down onto the bed and snatch up the anal beads I hid on the bedside table."
            "Sasha's face registers surprise as I lean over her with them in my hand, using my weight to pin her beneath me."
            show sasha stand rope fuck
            "As the head of my dick pushes into her lips, I reach under her and use a finger to also insert the first of the beads in her ass."
            "I time my short thrusts forwards to the insertion of each subsequent bead, not pushing all the way into her until the entire string is inside."
            show sasha stand rope sashacum
            "Only then do I start to move more rapidly inside of Sasha, enjoying the still startled look on her face."
            "It feels empowering to have shocked her at her own game, and I feel the pleasure of her body all the more because of it."
        "Doggy style" if not "anal beads" in hero.inventory.keys() and sasha.sub >= 90:
            $ P = "d"
            scene bg bedroom1
            show sasha doggy rope
            "Liking the sight of Sasha submissive on her hands and knees, I'm not about to let her up again."
            "Instead I turn her around so that she's facing away from me and push her shoulders down to the mattress."
            "This leaves me staring down at her rounded ass, and I can't resist pulling back my hand and slapping both buttocks sharply."
            "Sasha squeals in shock and pain as her skin reddens, and I choose that exact moment to pull her backwards and onto my dick."
            "She must be feeling a mingling of pain and pleasure, as my entering her elicits more squeals and yelps, almost like a scolded dog."
            "I can't resist squeezing and pinching her already ruddy buttocks, her flinching and crying serving to arouse me all the more."
        "Doggy style" if "anal beads" in hero.inventory.keys() and sasha.sub >= 90:
            $ P = "d"
            scene bg bedroom1
            show sasha doggy rope
            "Sasha makes a move to rise, but I take her by the shoulders and forced her back down onto the bed again."
            "She glances back over her shoulder at me, eyes widening, as I pick up the anal beads."
            show sasha doggy rope beads3
            "I make a point of parting her buttocks and inserting one bead after another, enjoying the way her body twitches as she takes them into her ass."
            show sasha doggy rope beads1
            "Only when the last one is inserted to I quickly thrust my dick into her already slick lips."
            show sasha doggy rope beads1 fuck pussy
            "Reeling from the sensation of the beads, I can't tell if Sasha actually knows that I'm inside of her as well now."
            show sasha doggy rope beads1 fuck pussy ahegao
            "Not that it bothers me in the slightest, as I find that her state of flustered confusion just makes me that much more aroused."
    "I have no idea if it's the thrill I'm getting from the bondage or from seeing Sasha react to it, but I can't keep this up much longer."
    menu:
        "Cum inside" if not "anal beads" in hero.inventory.keys() and CONDOM:
            $ sasha.sub += 1
            "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
        "Cum inside" if "anal beads" in hero.inventory.keys() and CONDOM:
            $ sasha.sub += 2
            "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
            "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
        "Cum inside" if (not "anal beads" in hero.inventory.keys() and not CONDOM) or p == "s":
            $ sasha.sub += 2
            "I might have normally pulled out at that moment, but something about the bondage aspect makes me want to dominate Sasha still further."
            if P == "s":
                show sasha stand rope dickin cum
            elif P == "m":
                show sasha missionary fuck cumshot rope
            elif P == "d":
                show sasha doggy rope mike pussy ahegao cum
            "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
        "Cum inside" if "anal beads" in hero.inventory.keys() and not CONDOM and p != "s":
            $ sasha.sub += 3
            if P == "s":
                show sasha stand rope dickin cum
            elif P == "m":
                show sasha missionary fuck cumshot rope
            elif P == "d":
                show sasha doggy beads1 rope mike pussy ahegao cum
            "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
            if P == "d":
                show sasha doggy anusopen rope mike pussy ahegao cum
            "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
        "Pull out" if not "anal beads" in hero.inventory.keys() and not CONDOM:
            if P == "s":
                show sasha stand rope dickout cum
            elif P == "m":
                show sasha missionary out cumshot rope
            elif P == "d":
                show sasha doggy rope mike dickout cum
            "At the very last moment I manage to somehow drag my dick out of Sasha, sparing her from taking me as I cum."
            "As she moans from the sensation of the sudden withdrawal, I just pant from sheer exhaustion."
        "Pull out" if "anal beads" in hero.inventory.keys() and not CONDOM:
            $ sasha.sub += 1
            if P == "s":
                show sasha stand rope dickout cum
            elif P == "m":
                show sasha missionary out cumshot rope
            elif P == "d":
                show sasha doggy beads3 rope mike dickout cum
            "I hear Sasha almost moan in disappointment as I pull out of her before I cum."
            if P == "d":
                show sasha doggy anusopen rope mike dickout ahegao cum
            "But then I take hold of the beads and virtually rip them out of her ass, making her breathless at the sensation."
    "No one speaks as we lie there, drenched in each other's sweat and utterly exhausted."
    "I survived my first experience of bondage, and I can't say that I didn't like the vast majority of it."
    "The cheesy power ballad says that love's a battlefield."
    "And it certainnly feels that way when there's a heavy dose of BDSM involved."
    return

label sasha_shower_BJ:
    show sasha
    if not game.get_flag_value("homeharem"):
        "I have no idea whatsoever how Bree would react to the idea that Sasha and I were getting up to something intimate under the same roof as her."
        "But all the same, it's certainly more than a little enjoyable to play along and believe that we're sneaking around and trying to keep from being caught."
    "Sasha reaches into the shower cubicle and turns on the water so that steam begins to rise and fog the glass of the door."
    "And then she turns to face me, already beginning to strip off the few clothes that she's wearing."
    "I stand there for a moment, quite happy to be watching Sasha as she reveals her body to me."
    "But then she makes a point of looking me up and down with a sense of amused urgency in her eyes, shaking her head at the same time."
    "It's at this moment that I realise I'm just standing there, not bothering to follow her example."
    "I make an apologetic gesture and scrabble to pull of my own clothes whilst still trying to keep most of my attention on Sasha, who by now is completely naked."
    "Still shaking her head at my tardiness, she opens the shower door and slips inside."
    "As I pull off the last of my clothes, I look up just in time to see her arm beckoning to me through the crack in the door."
    "Hurrying to follow, I almost blunder into the shower, expecting to find her waiting for me just inside."
    "But all I find once I'm inside is a wall of steam to greet me."
    "The shower cubicle can't be more than a couple of feet wide, but still Sasha's somehow managed to hide from me in here!"
    "I can just about hear her laughing at my expense over the sound of the water, but still I can't quite work out exactly where she is."
    "Putting my hands out in front of me, I grope for her in the confined space."
    "For a moment the tips of my fingers brush something soft and slick, and then it slips past me and I lose it once more."
    "Sasha's laughing even more now, so much so that I swear I can tell just where she must be."
    "I make another lunge for her, and this time almost manage to grasp what felt like part of a thigh or buttock."
    "This near miss wins me a whooping cry from Sasha, who clearly thought that she had eluded me as easily as the first time."
    "But then the possibility occurs to me that she might not be trying as hard as I thought, and maybe she actually wants to get caught."
    "My suspicions are all but confirmed when I feel the palms of her open hands press against my own, fingers twining between mine."
    "Chasing her has made me all the more eager to have her, and I immediately pull Sasha against me."
    "She feels incredible from the moment that we come together, skin to skin, her slippery belly and breasts sliding in a delightful manner."
    "I try to kiss her, but all that Sasha will allow me is the briefest of contact between our lips before she pulls away."
    "Before I can make my disappointment known, I feel her hand as it reaches down to stroke my cock and then gently squeeze my balls."
    "I could object, but sometimes, when they say that you really don't know what you want until you get it, they're telling the absolute truth."
    hide sasha
    show shower 2bj sasha
    "Sasha keeps on playing with my now stiffening cock as she gets down on her knees before me."
    "And by the time she's able to look me in the groin, there's no more teasing required for what she has in mind to do next."
    "The only reason that I can see what's going on down there is on account of Sasha's jet black hair and the heavy make-up of the same colour that she's wearing."
    "But even this is beginning to streak and run down her face as the water of the shower cascades down upon her."
    "All that seems impervious to this gradual washing away is the black lipstick that she's wearing."
    show shower 2bj sashamouth
    "And I note this as I see the shape of her lips outlined in that way, closing gently over the head of my cock."
    "I'm grateful for the fact that Sasha seems to want to go slowly, taking me into her mouth a little at a time."
    "What with the heat and confined space in the shower, the last thing I need is to get over-excited and end up passing out!"
    "The care that she's taking also means that I can feel every single twist and turn that her tongue and lips make on the shaft too."
    "But that's not to say Sasha doesn't sprinkle a little pain in with the pleasure as well."
    "More than once I find myself gasping in a moment of discomfort as she sinks her teeth in, just enough to get such a reaction out of me."
    "I only realise just how deep Sasha seems intent on taking me when I look down and see how close her lips are getting to the base of my cock."
    "Maybe the shower starting to feel more like a sauna has loosened her throat up, or maybe she's just determined to deep throat me."
    "Either way, she surely can't take any more of it in there without being in danger of choking."
    "And yet that's exactly what she does, as I feel the muscles at the top of her throat begin to squeeze at me when they go into spasm."
    "While the heat wasn't getting to me before now, the sheer intensity of what Sasha's doing to me seems to be making me all the more susceptible."
    "For the first time I can feel my head starting to reel and my legs becoming weaker."
    "Not knowing what else to do, I put my hands on the side of Sasha's head and try to pull her off of my cock before I can faint away and end up hurting us both."
    "Needless to say, she's not exactly ready for this, and her already twitching throat muscles clamp down all the harder on my cock as a result."
    hide shower 2bj
    show shower 2bj sasha
    "This means that by the time I finally manage to drag my cock out of her Sasha is coughing and wheezing in order to catch her breath."
    show shower 2bj sasha shoot
    "Unable to hold it in or else turn away from her, I cum a mere few seconds later."
    show shower 2bj sasha shoot facial
    "Still fighting for air, Sasha takes the entire thing square in the face."
    "The streamers of cum stripe her cheeks and forehead, but those that hit her mouth are immediately drawn in and swallowed."
    "Leaning against the wall, I find myself gasping for breath in a similar manner."
    "And I can't for the life of me tell if it's more from the heat of the shower or the sensation of release."
    return

label sasha_piss_off:
    show sasha wtf
    sasha.say "Piss off!"
    $ sasha.love -= 1
    $ hero.activity.set_flag("canceled",True)
    hide sasha
    return

label sasha_nightclub_showdown:
    "Despite my nerves, the night seems to be going pretty well, what with this being the first time that Sasha and I have hit a nightclub together as an official item."
    "We found a club where the music was agreeable to the both of us, grabbed a couple of drinks and just took it from there."
    "Maybe it's the fact that the sheer volume of the place makes holding a conversation almost impossible, meaning I can't put my foot in it that way."
    "But then again, perhaps I'm just being too pessimistic, and we're actually getting along so well because we have genuine chemistry."
    "Eventually a track that Sasha can't resist gets played, and she drags me onto the dancefloor, refusing to take no for an answer."
    "I try not to look as though my protests are too phoney as I allow myself to be pulled along in her wake."
    "But all the while I'm eager to spend any amount of time pressed up close to Sasha while she gets hot and sweaty..."
    "Before too long, I can feel a willing body pressed against me, fulfilling the possibilities that are filling my mind."
    "The only problem is that it takes me almost a full minute to realise that Sasha is still standing a little way off, her mouth hanging open in surprise."
    "Trying to shake myself back into awareness, I look down and see Audrey, a broad smile on her face as she grinds herself against me."
    audrey.say "Hey there - I didn't know you were a regular here!"
    "You know those times when you really do wish that the ground would open under your feet and swallow you up?"
    "Before I even manage to even think about reacting, Sasha's expression has already turned dark and thunderous."
    "She shakes her head in apparent disgust, turns around and then storms off the dancefloor without as much as a single word."
    "At the same time, Audrey has begun to frown at my frigid reaction to her attentions."
    "And why wouldn't she?"
    "Especially when I was so eager to return them the last time we met!"
    "But as I keep looking after Sasha and trying to escape her grip, she soon figures out what's going on."
    audrey.say "Don't tell me - you were here with that other girl over there?"
    "I nod desperately, still trying to free myself from her grasp."
    audrey.say "Ooh...awkward!"
    audrey.say "Well, don't mind me - I think you've already got enough problems on your hands!"
    "With that, she steps to one side, allowing me to hurry after Sasha."
    "Part of me wants to say something sarcastic in response."
    "But I'm too desperate to catch up to Sasha for my brain to fire anything off quickly enough without making myself look even more stupid than I already do right now."
    "Of course, I was also pretty damn stupid to think that I could have some fun with Audrey behind Sasha's back without her finding out."
    "I manage to catch up to her just before she reaches the exit."
    hero.say "Sasha...wait...please!"
    "I grab hold of her arm, more out of sheer desperation than any desire to manhandle her."
    "Sasha spins around and twists her way out of my grip, her face still showing her evident distaste for my presence."
    "At the sight of our struggle, one of the doormen starts to walk over."
    "But Sasha shakes her in his direction, causing him to shrug and turn away again."
    hero.say "Sasha...that wasn't what it looked like!"
    hero.say "I can explain..."
    show sasha angry
    sasha.say "Can you really?"
    sasha.say "Because right now, all I hear are bullshit cliches!"
    menu:
        "Admit cheating":
            $ sasha.love -= 10
            "Maybe the only way that I can hope to make this right is to tell Sasha the truth?"
            "Honesty might show her that I'm seriously sorry for going behind her back."
            "But even if it doesn't, she's still too special for me to want to lie to her..."
            hero.say "Yes...that was what it looked like."
            hero.say "We hooked up once, back when you and I got together."
            hero.say "I didn't tell you at the time, because I didn't know if we'd get serious."
            "At this last admission, her eyes go wide with irritation."
            hero.say "I...I know that was a mistake now."
            hero.say "I'm sorry, Sasha - really I am."
            "For a while, she says nothing, just stares at me in silence."
            "I can see that she's sizing up my explanation, dissecting it for what it's worth."
            sasha.say "What were you doing?"
            sasha.say "Hedging your bets, huh?"
            hero.say "No, Sasha - it wasn't like that at all!"
            hero.say "You have to believe me!"
            "Sasha snorted and shook her head in apparent disbelief."
            sasha.say "No, [hero.name], I think you'll find that I don't."
            sasha.say "In fact, I think that if you want me to buy your story, then you're the one that's got to convince me."
            "And with that, she turns her back on me for a second time and walks out of the nightclub."
            "But this time, I make no effort to follow."
            "Instead I just stand there, cursing myself for a fool and trying to think up some way to win her over once again."
        "Deny cheating":
            $ sasha.love -= 20
            "I want to be honest with Sasha, really I do."
            "But there's such a thing as too much honesty."
            "If she knew every grisly detail about my life, I'm sure Sasha would never be able to look me in the face again!"
            hero.say "Okay, okay...I do know that girl."
            hero.say "But she's an old flame, back from well before we were ever an item."
            "Sasha narrows her eyes, scrutinising my words for all they're worth."
            "But all the same, I can see a glimmer in her eyes that I choose to interpret as her wanting to believe me."
            "Whether my hunch right or not, I choose to seize on the one chance that I can see before me right now."
            show sasha normal
            sasha.say "You really mean that?"
            sasha.say "Because she seemed REALLY familiar with you?"
            "I can feel a cold sweat running down the back of my neck as she waits for my answer."
            "But I've committed myself to the lie, and I can't take it back now."
            hero.say "Of course I do, Sasha!"
            hero.say "Didn't you hear how surprised she was to see me here?"
            hero.say "I don't think I've seen her since we were last together."
            hero.say "And well...we kind of never broke it off - at least not formally."
            "Sasha nods slowly, as though she's not totally satisfied with this explanation, but willing to buy it all the same."
            sasha.say "Okay...well...I'm going home now."
            sasha.say "I don't feel like doing this anymore tonight."
            sasha.say "Would you mind getting a taxi home without me?"
            sasha.say "I need some time to think..."
            "And with that, she turns her back on me for a second time and walks out of the nightclub."
            "But this time, I make no effort to follow."
            "Instead I just stand there, cursing myself for a fool and trying to think up some way to win her over once again."
    $ sasha.set_flag("nodate")
    $ sasha.set_flag("nokiss")
    $ sasha.set_flag("cheated")
    $ date_stay = False
    return

label sasha_ending:
    $ game.hour = 16
    if bree.get_flag_value("engagedmike") and game.get_flag_value("homeharem"):
        jump sasha_bree_ending
    show bg church
    "If you'd asked me to guess where my life would take me even a couple of months before today, I doubt that I'd have been able to predict anything as crazy or wonderful as what I'm doing right now."
    "I'm standing before the altar of an old church, in front of dozens of people who are all in gothic dress, while harps and lyres play in the background."
    "I ask you - who else could I be waiting for, but Sasha?"
    "It really doesn't matter to me that I can't identify most of the guests that are sitting behind me."
    "They could all be strangers or a mass gathering of professional wedding-crashers for all I care."
    "I've seen all of their names on the guest-list that we put together and heard an explanation of just who they are in relation to Sasha."
    "But in reality, she's the only person that I want to see."
    "I'd have been happy if it were just the two of us and the priest performing the ceremony."
    "Actually, we almost did just that - disappearing together with the intention of getting married in secret."
    "But in the end we decided that this was something that we wanted people to see and remember."
    "Suddenly the music changes from the sedate background noise we chose for while people were filing into the church to the piece for Sasha's procession down the aisle."
    "I take a deep breath, waiting for my first glimpse of her in the dress that she's been keeping under wraps until today."
    "Sasha's been careful to tell me nothing about the look she's chosen, not even dropping as much as a hint."
    "There's no prize for guessing that it'll most likely be something in keeping with the gothic theme that we've gone with for the entire wedding."
    "But still, this is her wedding dress, and even a girl as unique as Sasha is going to want to make an impression when she walks down the aisle."
    show sasha wedding blush
    "And the moment that I see her enter the church, I can see that's just what she's managed to do..."
    if not sasha.get_flag_value("pregnant") >= 9:
        "Sasha sweeps into the church, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red above flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebon hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
        "And since I've grown to love her, so do I."
        "When I said she was a vision, I meant it."
    else:
        "Sasha sweeps into the church, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red, cut to be sympathetic to the curve of her swelling belly."
        "Below are flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebon hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
        "And since I've grown to love her, so do I."
        "When I said she was a vision, I meant it."
    "As much as she's an alternative kind of girl that doesn't define herself solely on her looks, I can still see that Sasha's enjoying the attention she's getting."
    "Joining me at the altar, even the veil that she's wearing can't do much to hide the smile on her face."
    "Though I'm sure that a good part of the reason for that smile is also on account of the fact that we're finally about to go through with it and tie the knot."
    "With Sasha finally standing by my side, the priest gives us a nod and a smile, letting us know that he's ready to start the ceremony proper."
    "You'd be wrong if you were thinking that we'd gone and composes long, dramatic passages of gothic verse for the purpose of our vows."
    "In reality, they're very simple and honest, uncomplicated sentiments that we feel for each other and want to be the basis of our union."
    "I can almost feel my hands shaking as we exchange rings."
    "And then the time comes for me to lift the veil from Sasha's face."
    "Now there's no illusions involved - I can definitely feel my hands shaking from the pressure and the emotions passing through me."
    "As crazy as it sounds, I feel as though I'm looking on that so familiar face in a totally new way, now that we're husband and wife."
    "The same eyes that I've looked into countless times as we made our way from housemates to friends and then lovers, seem somehow different to me now."
    "I look into them and Sasha looks back at me with the knowledge that we've just made a vow to spend the rest of our lives together."
    "And those new lives start right here and now."
    priest_say "You may kiss the bride..."
    show sasha kiss wedding
    "Sasha wraps her arms around me as I pull her into a gentle embrace and kiss her full on the lips."
    "It feels as wonderful now as it did the very first time."
    "Outside, on the church steps, the guests toss confetti - which, of course, is black."
    "And then Sasha tosses her bouquet to the crowd, who mill around in anticipation."
    "But whoever catches it, I have no idea, as I only have eyes for her."
    "And I seriously hope that I always will."
    scene bg park
    show bree ending sasha
    with fade
    sasha.say "So, after we tied the knot, we saved up enough to put down a deposit on a ruined gothic castle in Transylvania."
    sasha.say "And now we live our lives in imitation of the most iconic vampires from the silver screen and the pages of classic horror literature."
    sasha.say "The end..."
    sasha.say "Hah, nope - but I had you fooled for a moment there, didn't I?"
    sasha.say "I guess if I were to compare meeting [hero.name] to anything, it'd be picking up a book with a goofy-looking cover."
    sasha.say "In that situation, you have one of two choices."
    sasha.say "Firstly, you can go with your gut reaction and assume that what's on the inside is going to be just as goofy and toss it aside."
    sasha.say "Or secondly, you can have a glance at the blurb on the back, maybe even read a couple of pages and see how it grabs you."
    sasha.say "That's how [hero.name] seemed to me when we first met - a paperback that looked like it could be fun, but with a cover that you just had to get past or not."
    sasha.say "And I'm glad that I did read those first couple of pages, because the story just seemed to get better and better as it went on."
    sasha.say "First I found out that he was pretty funny and charming."
    sasha.say "Then that he was into the same kind of stuff as me."
    sasha.say "Next I began to realise just how much I liked his company."
    sasha.say "And finally I discovered that the itch inside of me was for us to be more than just friends."
    sasha.say "Sure, he's a pretty typical guy sometimes - childish, with a short attention span and his mind on only one thing."
    sasha.say "But I know that I can be no bed of roses myself, and we both know when to give each other the space we need."
    sasha.say "It's funny, how I'd always sworn that I'd never be a wife with a home in the suburbs."
    sasha.say "But now that's exactly what I am, it's not all that bad after all."
    sasha.say "No one's chained me to the sink or made me behave like a Stepford Wife - at least so far..."
    if not sasha.get_flag_value("pregnant"):
        sasha.say "The only real fly in the ointment when we got back from the honeymoon was how the atmosphere in the house changed."
        sasha.say "I guess that [hero.name] and I being a couple kind of ruined the dynamic for Bree."
        sasha.say "She started spending less time around us and more in her room, until she upped and told us she was moving out."
        sasha.say "Sure, it was sad - but she keeps in touch and seems to be doing well in her new place."
    else:
        sasha.say "The only real fly in the ointment when we got back from the honeymoon was how the atmosphere in the house changed."
        sasha.say "I guess that [hero.name] and I being a couple kind of ruined the dynamic for Bree."
        sasha.say "And then when Dahlia came along, it must have felt like she was intruding on our little family the whole time."
        sasha.say "She started spending less time around us and more in her room, until she upped and told us she was moving out."
        sasha.say "Sure, it was sad - but she keeps in touch and seems to be doing well in her new place."
    sasha.say "I don't think marriage has changed us all that much though."
    sasha.say "We still have the band, go to gigs and see a movie every now and then."
    sasha.say "If you thought that I was going to paint the whole house black and fill the yard with tombstones, then I'm sorry to disappoint you."
    sasha.say "Maybe we do put out Halloween decorations up a little earlier than the rest of the neighbourhood and take them down later."
    sasha.say "But we do normal folks stuff as well, more often than you might think, too."
    sasha.say "We have BBQs and parties, swim in the pool and go to the beach."
    sasha.say "Well, maybe not the last one - you don't stay this pale by getting too much sun!"
    sasha.say "In fact, you want proof of just how normal we can be?"
    sasha.say "Then here we are, walking through the park on a nice, sunny day."
    sasha.say "Look at us, smiling and laughing like we don't have a care in the world."
    sasha.say "As far as anyone can tell, we're just another, normal couple leading normal lives."
    sasha.say "And no one needs to know the truth of just how different we are under the surface - or what goes on behind closed doors!"
    $ renpy.full_restart()

label shower_ffm_female:
    $ sasha.set_flag("sex",1,"permanent","+")
    $ mike.set_flag("sex",1,"permanent","+")
    scene bg bathroom
    show sasha naked at left
    show mike naked at right
    "Neither of us as much as touched him to begin with, instead making a show of stripping each other off as he watched."
    "He was still too surprised to have done anything all the same, and so he just stood there, eyes following every piece of clothing that we removed."
    "But even if he was not making any conscious moves, I couldn't help smiling at the sight of his cock beginning to stir the whole time."
    "Once we're all naked, Sasha skips ahead of me, stepping into the shower and beckoning for us both to follow."
    "I can't help smiling as I reach out and take hold of Mike by his now well and truly erect cock, using it to lead him into the cubicle."
    "Even when we get into the shower, he still seems to be hesitant, not making any move to assert himself."
    hide mike
    hide sasha
    show gog
    "Reasoning that he needs some more motivation in order to shake off his inaction, I lean against one of the tiled walls and pull Sasha into a close embrace."
    "As my hands begin to explore her smooth skin, made slippery by the water raining down from above, I can already feel Sasha returning the favour with equal enthusiasm."
    "I feel her weight lean into me perhaps a second before her questing lips find my own, her tongue immediately seeking a way between them and finding it with ease."
    "Sasha's breasts brush roughly against me as she presses herself atop me, slipping over my chest and making it hard to tell where one pair ends and the other begins."
    "Already I want to reach down between my legs, fingers anticipating the feeling of my pussy."
    "But still Mike seems to be holding back, not ready to commit himself to what we're doing together."
    "I'm certain that he's not reticent because of shyness, and so that can only mean that we've been giving him too good of a show to tear himself away from."
    "Reluctantly I break the kiss with Sasha, leading her to fall to kissing and almost biting at my neck as I do so."
    "Making sure that I have Mike's attention, I begin to run my hands up and down the small of Sasha's back, massaging and kneading at her buttocks."
    "Sasha herself can't help moaning at the pleasure that this gives her, bending down and stretching her backside towards him as she does so."
    "Though I can't see her from Mike's point of view, I know enough about my own anatomy to be sure that he must have a rather inviting view from that angle."
    "I see him lick his lips, and then he's snared, stepping forwards to close the small distance between them."
    "He doesn't take time for teasing or foreplay of any kind, instead just taking hold of Sasha's left buttock in one hand and using the other to guide himself home."
    hide gog
    show shower ffm
    "I have no idea whether he's chosen to push his way into Sasha's pussy or take her up the ass, but the effect is still quite something from where I'm standing."
    "Sasha doesn't protest or object in the slightest, only letting out a muffled moan as begins to kiss me again in earnest."
    "Mike pushes in as far as he can possibly go, holding himself there for an lingering moment."
    "In response she probes just as deeply into my mouth with her tongue, almost too deep for me to handle."
    "But thankfully, as Mike begins to lessen the degree to which he's pressed into her, starting to move back and forth, Sasha too settles into a more tolerable rhythm."
    "Though she's the one that's actually getting fucked, I feel strangely as though Sasha's becoming nothing but a bridge between Mike and myself."
    "I open my eyes as Sasha kisses me, and see that he's looking straight at me, rather than down at her as she takes his cock from behind."
    "It's almost like I can feel every thrust of his dick inside of her, as it translates into the way in which she kisses me."
    "As it writhes and twists in my mouth, Sasha's tongue feels like nothing more than an extension of Mike's cock."
    "Before I know it, my fingers are sliding between my legs and stroking the outer lips of my pussy."
    "Wet as I may be from the water of the shower, I know the difference between it and the slick sensation of my own body."
    "Stroking in the right places in just the right way means that I can't help but come alive to the pleasure of what we're doing all over again."
    "Sure, Mike might be inside of Sasha right now, but what she's doing to me is thanks to what he's doing to her."
    "And what I'm doing to myself is likewise the end of a sensual chain that started when his cock entered her body."
    "I can already sense that I'm zoning out thanks to the sensations that I'm feeling and the heat in the shower cubicle."
    "How close Sasha and Mike are to cuming I have no idea, but I can feel mine coming over me right then and there."
    "Breaking Sasha's kiss for the second time, I lean my head against the wall and can't keep from letting out a strained cry as I cum."
    "Perhaps it's the sight of this that spurs him on, but for a second, it looks like Mike is about to cum too, and while he's deep inside of Sasha."
    show shower 2bj bree sasha
    "Don't ask me how, but Mike actually manages to hold it in, pulling out before it's too late and urgently forcing the both of us to kneel in the bottom of the shower before him."
    "I can't help wondering if his desperation to pull out was because he was doing Sasha in the pussy, but there's no time to contemplate such things right now."
    show shower 2bj bree sasha shoot
    "Instead we sit on our haunches, looking up at him in obvious anticipation as he strokes his cock in the last moments before his climax finally takes him."
    "Sasha and I jostle and push playfully for the best position, and I find that I have to keep myself from actually pushing her aside for real."
    "There's still a part of me that's unreasonably jealous that she was the one to get Mike's cock inside of her, and wants to claim the largest portion of his cum as compensation."
    show shower 2bj bree sasha shoot facial
    "The point becomes moot only a second later, when he finally cums and gives us a shower inside of a shower."
    "I can't hope to tell just which one of us actually gets the most of it, but I feel the warm cum streak my forehead and cheeks, as well as landing inside of my wide-open mouth."
    "Swallowing what I managed to catch and then licking greedily with my lips for whatever else I can find on my face, I'm too satisfied to be jealous of Sasha any longer."
    "All I have the will and energy to do is sit there, as the continued pattering of the water washes the three of us clean."
    return

label shower_ffm:
    scene bg bathroom
    show bree at left
    show sasha at right
    if bree.get_flag_value("collared") and sasha.get_flag_value("collared") and sasha.sub >= 50 and bree.sub >= 50:
        hero.say "The shower's ready for us all to hop in there together."
        hero.say "But first I'm going to need the pair of you to strip off my clothes."
        hero.say "So get to it and be sure to fold them neatly as well."
        "Without so much as a question or complaint, Bree and Sasha set to their task."
        "Together they strip me from top to bottom, folding each and every piece of clothing they remove."
        "But while they remain silent throughout, I can see them eyeing up what they reveal."
        "And when they come to removing my pants and underwear, their interest becomes all the more intense."
        "Neither of them falls to the temptation to touch my cock, yet I can tell that they both want to."
        "And it's the knowledge of just how much they're having to hold back that begins to get me hard."
        "Of course this also means that their eyes are drawn back to it all the more."
        "Which, in turn, makes me that much harder."
        hero.say "Okay, into the shower you go."
        hero.say "And I want you to show me that you can share!"
    else:
        sasha.say "Doesn't he look nervous, Bree?"
        bree.say "Yeah, like a deer in the headlights!"
        "They saunter over to where I'm standing, smiling in a way that I should find a massive turn-on."
        "But instead I feel instantly paranoid and like I'm being sized up by a pair of hungry she-wolves."
        bree.say "You know, it is hot in here - maybe he's feeling it?"
        sasha.say "I remember what they told me in first aid class about heatstroke."
        sasha.say "You gotta remove a layer of clothing to cool the victim down."
        bree.say "Hmm...I think we should take off all of his clothes, just to be sure!"
        "Together they begin to strip off my clothes, brooking no objections and putting a finger to my lips whenever I try to speak up."
        "Pretty soon I'm naked too, and the girls stand back to admire their handiwork."
        bree.say "That's better...but he still looks nervous, the poor lamb!"
        sasha.say "We could try to breathe some life back into him?"
        "Bree shakes her head."
        bree.say "No - I say we BLOW some life back into him instead!"
        "With that, they each grab one of my hands and pull me into the steaming shower."
    show shower 2bj bree sasha
    "Once we're all standing in the shower together, Bree and Sasha sink to their knees before me without needing any encouragement."
    "They work so well as a team that I can't help but wonder if they've taken the time to plan all of this out beforehand."
    "Bree takes the lead, beginning to stroke the shaft of my cock with one hand and teasing the tip with her tongue."
    "While Sasha cups my balls and starts to lick them slowly, sucking one into her mouth at a time."
    show shower 2bj breemouth
    "Bree looks up at me as she finally takes my cock into her mouth, holding my eye the whole while."
    "It's like she wants me to see the effect that it's having on her at the same moment that I feel the sensations myself."
    "Just as I think Bree can't swallow me any further and that she must be about to choke, she slides my cock out of her mouth again."
    "Only her lips linger on the very tip, and I'm clueless as to what she's doing until Sasha's lips appear on the other side."
    "As smoothly as it's possible to imagine, Bree surrenders my cock to Sasha's intentions, while she takes over caressing my balls."
    show shower 2bj sashamouth
    "But where Bree was attentive and fairly meek, Sasha instantly sets a different tone."
    "She smiles impishly as she uses her teeth almost as much as her lips and tongue."
    "When she takes me into her own mouth, it's like being pleasured by a predatory animal."
    "And where Bree stroked my shaft, I can already feel Sasha's nails, sharp and sensual against my tautly stretched skin."
    "If asked to choose, I couldn't honestly say that I could pick Bree's warm gentleness over Sasha's exquisite pain."
    "But what I do know is that if this keeps up for much longer, I'm going to cum!"
    if bree.get_flag_value("collared") and sasha.get_flag_value("collared") and sasha.sub >= 50 and bree.sub >= 50:
        "As nice as the attention that I'm getting from the mouths of my bitches might be, I want to shoot my load into a more intimate hole."
        "A short tug on each of their leads lets Sasha and Bree know that I've had enough of what they're doing and that it's time for a change."
        "But as we're building up towards a peak and not about to slacken off any time soon, they don't need to be told what it is that I want next."
        "Both of them kneel before me, looking up with smiles on their faces and appeals to be picked in their eyes."
        "On a whim, I give Sasha's lead a second tug, and watch as she happily gets to her feet in anticipation of what's to come next."
        "Bree looks disappointed, but she's well-trained enough to know that she shouldn't complain."
        "As soon as I have Sasha's buttocks within easy reach, it's time to begin."
    else:
        hero.say "Ah...ah...I'm gonna..."
        "Bree and Sasha don't even need me to finish the sentence to know what's up."
        "They exchange knowing glances, even as Sasha lets my cock slip out of her mouth."
        "Still kneeling in the bottom of the shower cubicle, they begin to play what looks like a game of Rock, Paper, Scissors."
        "Bree goes first, revealing scisors, but a split second later, Sasha has rock."
        "Showing good grace even when losing, Bree shrugs and backs off a little, letting Sasha claim her prize."
        "I have no idea of just what that could be, until she rises to her feet and turns her back on me."
        "Sasha glances over her shoulder, giving me an inviting smile and shaking her buttocks just enough so that the message can't be misinterpreted."
    show shower ffm
    "The combination of the warm water showering down on all three of us and the games that we've already been playing mean that Sasha is enticingly soft and compliant."
    "I take a firm hold of her buttocks, enjoying the sensation of just how slippery they feel as the water cascades over them."
    "Sasha makes no protest whatsoever as I part them and then pull her smoothly back and onto me in one movement."
    "But if her skin is soft and yielding, then the inside of her pussy is suddenly tight and willing to put up more of a fight."
    "I begin to thrust into Sasha with ever more enthusiasm, feeling her quiver and shake in response to my efforts."
    "Looking up, I see that Bree is leant against the tiled wall of the shower, her arms crossed as she watches us."
    "She's trying to look resigned to the way things have played out, but it still feels wrong for her to be just watching."





    "Soon, though I'm vigorously pounding away on Sasha, I'm getting off as much on watching her and Bree as anything else."
    "Her hands are playing all over her body in response to Sasha's attentions."
    "Stroking her thighs and squeezing her breasts to exorcise some of the feelings overtaking her senses."
    "When Bree's own hands reach down for her pussy too, probing the folds and creases that Sasha neglects as she probes deeper, I feel like I can't go on much longer."
    "Even as Bree begins to stroke herself towards an orgasm, I'm losing myself inside of Sasha."

    "Afterwards, all three of us stand beneath the still falling water, letting it wash away the sweat and other things that have accumulated."
    "All that can be heard over the pounding of the droplets is the sound of our own breath as it comes in ragged gasps."
    return

label sasha_threesome_request:
    show sasha
    "Sasha keep looking over at me, keeping her eyes on me for a couple of seconds and then turning away before doing the whole thing all over again."
    "I try to ignore it as best I can, but it's like her gaze is boring into me every time she does it, and it's starting to get under my skin."
    "Every time she seems to be on the verge of saying something, and then chickens out at the very last minute."
    "Finally, when I feel as though it's going to end with me screaming and running away in a state of sheer insanity, I decide to call her bluff."
    hero.say "Okay, Sasha - out with it!"
    sasha.say "Huh, out with what?"
    "I groan and roll my eyes in frustration."
    hero.say "Sasha, your eyes have been burning a hole in the side of my head for an age now."
    hero.say "What is it that you keep trying to pluck up the courage to ask me all this time?"
    "For a moment, Sasha's face seems to say that she's going to try and argue the point."
    "But then she shrugs in apparent surrender."
    show sasha blush
    sasha.say "Okay, okay...I'll say it."
    sasha.say "But I'm not sure how receptive you're gonna be."
    sasha.say "So you've been warned, yeah?"
    "I nod, more for the sake of getting Sasha to finally spill her guts than actually wanting to know what it is she's been stewing on the entire time."
    hero.say "Go ahead, Sasha, surprise me!"
    "Sasha takes a deep breath before she obliges."
    sasha.say "Well...thing was...I was was kinda wondering if you'be up for...maybe trying a threesome sometime soon?"
    "Well, let's just say that while I'm not surprised, I am greatly intrigued!"
    hero.say "That sounds like a great idea, Sasha."
    hero.say "Why in the hell would you be hesitant to ask me that?"
    sasha.say "Ah...you can be kind of vanilla sometimes, you know?"
    sasha.say "I find it hard to guess what you'll be up for and what you wont most of the time..."
    "'Vanilla' - what does she mean by that?!?"
    "Maybe she needs to be reminded of just how adventurous and outrageous I can be when the mood takes me!"
    hero.say "I'm up for this, I can tell you that."
    "Sasha's mood suddenly picks up visibly and a wide smile spreads across her face at my declaration."
    sasha.say "Really?"
    sasha.say "That's great, really great."
    sasha.say "And don't you worry, the guy that I have in mind is perfect for this kind of thing."
    sasha.say "You'll get on so well with him, I promise!"
    "Wait a minute - did she just say 'guy'?!?"
    menu:
        "Change your mind":
            $ sasha.love -= 10
            hero.say "Whoa, whoa, whoa...Sasha - what do you mean you have a GUY in mind?"
            "Sasha looks at me oddly, as if she doesn't really understand my objection."
            "Then she puts her hand to her mouth to stifle a laugh she can't quite keep from bursting out."
            show sasha happy
            sasha.say "Oh, [hero.name] - did you just freak out because I wanted to invite another guy along for sex?"
            sasha.say "Aww, that's so cute and twentieth-century of you - to just automatically assume I'd be hooking us up with a girl!"
            "Before I was feeling uneasy and threatened about some other guy's cock waving about in my immediate vicinity."
            "But now I'm also burning up with embarrassment at Sasha calling me some kind of sexual throwback."
            sasha.say "Like I said before, don't worry."
            sasha.say "He really is perfect for this kind of thing, [hero.name]."
            sasha.say "You know, great body and a fucking massive..."
            hero.say "SASHA...this is not helping to sell me on the idea!"
            sasha.say "It'll be fine - I'll be there to look after you..."
            sasha.say "We can even make it clear before we get started that, under no circumstances, is he to put his cock up your ass."
            hero.say "No, Sasha...N...O...No - do you understand me?"
            show sasha sad
            "Sasha sighs in resentment, starting almost instantly to go into a pout."
            sasha.say "Urgh...whatever, [hero.name]."
            sasha.say "It would have been fun too - if someone not a million miles from here wasn't so sexually repressed..."
        "Stick with it":
            sasha.say "His name's Scottie, and he's an old friend of mine..."
            "That name sounds oddly familiar to me, like Sasha's mentioned it before."
            hero.say "'Scottie'...where do I recognise that name from, Sasha?"
            "Sasha pauses, clearly knocked off of her stride by the question."
            sasha.say "I might have told you about him already - he and I used to date."
            sasha.say "But that was before I moved in with you and Bree."
            sasha.say "It's well over now, and we're just good friends."
            "That's it, he's one of Sasha's former boyfriends."
            "And from the sound of it, she wants him to be a friend with benefits too!"
            "Whatever I might think about the reality of getting into a threesome with Sasha and another guy, I'm not about to let this guy make me look bad by comparison."
            hero.say "Sure, Sasha, sign me up."
            show sasha happy
            $ sasha.love += 5
            sasha.say "You mean it - you're up for this?"
            hero.say "Yeah, of course - it's the twenty-first century, Sasha."
            hero.say "What did you think, that I was backwards enough to just assume you wanted to bring along another girl?"
            hero.say "This is supposed to be sex between three equal, consenting adults, after all."
            hero.say "Not some sad little adolescent male wank fantasy!"
            "Sasha grins at me, clearly feeling pleasantly surprised at how liberated I've turned out to be."
            "I smile too, but it's more a rictus of worry that I might not be able to live up to the hype that I've created for myself."
            $ sasha.set_flag("scottiethreesome",1)
    "Once the discussion dies down, we both become silent for a short while."
    "But I can bet that Sasha's mind is on nothing but the matter of the threesome."
    "Because I know that's what is on my mind as well."
    return

label bree_sasha_bitches_1:
    $ hero.activity.set_flag("canceled")
    show tv bree sasha
    "It's weird how things can change so much and how stuff that was crazy at first can come to be pretty much the norm with time."
    "Take my domestic arrangements, for example."
    "Just a couple of months ago, I was adjusting to having two brand new and very different female room-mates move in with me."
    "And before I could get my head all the way around that, things changed all over again."
    "Now I'm living with them both in a three-way relationship that involves them both being basically my obedient slaves."
    "So kids at home, the lesson is that, while things always change, some changes are better than others."
    "Tonight's a good example of how normal things can be, and yet how weird at the same time."
    "Bree, Sasha and myself are just sitting on the sofa together, binging on a box-set and eating popcorn."
    "Sounds pretty innocent, right?"
    "Well, not if you could actually see us doing it."
    if bree.get_flag_value("pregnant") >= 9 and sasha.get_flag_value("pregnant") >= 9:
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around Bree's neck to my left."
        "Save for the collars, both of them are naked, their heavily pregnant bellies plain to see."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, Bree simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif sasha.get_flag_value("pregnant") >= 9:
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around Bree's neck to my left."
        "Save for the collars, both of them are naked, but Sasha's pregnant belly is plain to see."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, Bree simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif bree.get_flag_value("pregnant") >= 9:
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around Bree's neck to my left."
        "Save for the collars, both of them are naked but Bree's pregnant belly is plain to see."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, Bree simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif not sasha.get_flag_value("boobjob") and not sasha.get_flag_value("haircut"):
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around Bree's neck to my left."
        "Save for the collars, both of them are naked."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, Bree simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif sasha.get_flag_value("boobjob") and not sasha.get_flag_value("haircut"):
        "I guess I could pass for normal, with my popcorn - but not while holding two leather leads in my other hand."
        "Bree is on the end of the pink one, naked save for a pink collar."
        "And Sasha is on my right, tethered by a black collar, also naked, with nothing to conceal her surgically enlarged breasts."
        "Written on both collars in capital letters is the word 'SLAVE'."
        "But apart from that, both are sitting with their attention focussed totally on the TV."
        "Sasha leaning forward intently and Bree sitting cross-legged as she eats her own bowl of popcorn."
        "Together, I think we make quite the picture of domestic harmony and bliss."
    elif not sasha.get_flag_value("boobjob") and sasha.get_flag_value("haircut"):
        "I guess I could pass for normal, with my popcorn - but not while holding two leather leads in my other hand."
        "Bree is on the end of the pink one, naked save for a pink collar."
        "And Sasha is on my right, tethered by a black collar, also naked, contrasting vividly with her bleached blonde hair."
        "Written on both collars in capital letters is the word 'SLAVE'."
        "But apart from that, both are sitting with their attention focussed totally on the TV."
        "Sasha leaning forward intently and Bree sitting cross-legged as she eats her own bowl of popcorn."
        "Together, I think we make quite the picture of domestic harmony and bliss."
    else:
        "I guess I could pass for normal, with my popcorn - but not while holding two leather leads in my other hand."
        "Bree is on the end of the pink one, naked save for a pink collar."
        "And Sasha is on my right, tethered by a black collar, also naked, with nothing to conceal her surgically enlarged breasts, not even her bleached blonde hair."
        "Written on both collars in capital letters is the word 'SLAVE'."
        "But apart from that, both are sitting with their attention focussed totally on the TV."
        "Sasha leaning forward intently and Bree sitting cross-legged as she eats her own bowl of popcorn."
        "Together, I think we make quite the picture of domestic harmony and bliss."
    "It's been one of those lazy, quiet nights, the kind where no one really needs to speak to be aware that everyone else is happy and at ease."
    "Even though both of the girls are quite comfortable with the arrangement of needing to ask permission if they want to speak, it's been almost an hour since anyone actually has."
    "I've totally lost track of the time when Sasha finally sits up and raises her hand, wanting to speak."
    hero.say "Yes, Sasha - what is it?"
    sasha.say "Mmm...Master, I need to use the bathroom - may I be excused?"
    "Sasha's yawn and the sound of her tired voice seems to have roused Bree into wakefulness too."
    "She now raises her hand in the same manner."
    "I nod, giving her permission to speak as well."
    bree.say "I'd like to use the bathroom too, Master..."
    menu:
        "Remove their leashes":
            hero.say "Okay, but you two are to come straight back here when you're done, you hear?"
            "Sasha and Bree, both sitting up on their haunches now, are quick to nod in agreement."
            "I unclip their leashes and watch as they hurry off upstairs together eagerly."
            "After a short while, they come back down the stairs at a much more leisurely pace."
            "They walk around the sofa and kneel in front of me, waiting to be put back on their leads."
            "That done, they clamber back on the sofa, snuggling down against me, one on either side."
            "And we get back to watching the TV once more."
        "Take them out for a walk":
            $ game.set_flag("BreeSashaPet",1)
            hero.say "Okay, let's get you two a little fresh air."
            "Bree and Sasha look at each other in confusion as I stand up."
            hide tv
            "But a gentle yet firm tug on their leads convinces them to follow suit."
            show bree naked leash at left
            show sasha naked leash at right
            "I walk them to the front door and open it wide, then gesture for them to step outside."
            hero.say "There you go - what are you waiting for?"
            "Bree raises a tentative hand."
            hero.say "Speak."
            bree.say "Please, Master...we don't understand..."
            hero.say "What's not to understand?"
            hero.say "You're my bitches, you're wearing collars, and you need the bathroom."
            "Bree still looks confused, but I see recognition appear in Sasha's eyes."
            "Without needing to be told, she drops onto all fours and pulls eagerly on her leash, whining to be allowed outside."
            "Bree doesn't seem to get what she's doing at first, but then she truly thinks about it, and a bashful grin spreads across her face."
            "She copies Sasha, and is soon straining by her side, making whining sounds of her own that are quite something to hear."
            "Shit - they're actually going to do this!"
            hide bree
            hide sasha
            show bitches walk
            "Not willing to be outdone by them, I walk the girls out of the front door and down the street to the local park."
            "Luckily for us, there aren't many street lights and the place is totally deserted when we arrive."
            "That means that only I get to see the spectacle of first Sasha and then Bree hunting on their hands and knees for an agreeable spot amongst the borders and flowerbeds."
            show bitches blowjob sashapee
            "Sasha pees for longer, seeming to enjoy having my eyes on her."
            hide bitches
            show bitches blowjob breepee
            "But Bree quickly relieve herself too."
            hero.say "Both finished?"
            "Sasha and Bree nod happily, not fazed in the least by the experience."
            "Shaking my head, and more than a little turned-on, I lead them back along the street to the house, usher them inside and lock the door."
    $ game.pass_time(2)
    return

label bree_sasha_bitches_2:
    $ hero.activity.set_flag("canceled")
    show tv bree sasha
    "It's just an average night of the week for Brie, Sasha and myself."
    "Sitting in front of the TV and watching any old thing we can find to kill time before turning in for the evening."
    "But then of course, the two girls being stark naked and wearing collars and leashes that I clutch in one hand might look odd to an outsider."
    "Though it's become the accepted norm for myself and my two eager and very willing slaves."
    "I'd say that nothing out of the ordinary happened throughout most of the evening."
    "But there's already the image of Bree and Sasha in their cute little collars and nothing else to make that sound strange in of itself!"
    "It's normal for us, okay?"
    "We're not watching anything in particular, no one's enjoying a drink at the end of the day, and there are no illicit drugs going around."
    "For a master and slaves, I guess we're pretty domesticated."
    "Though there is one thing that's been bugging me for the past hour or so."
    "Both Bree and Sasha have been drinking a lot more fluids than they normally seem to on a typical evening."
    "In fact, come to think of it, I haven't seen either of them without their noses in their water bowls every fifteen minutes or so for hours."
    "Yet both of them have only crawled off of the sofa and across the room to where their bowls (inscribed with their names and in colours matching their respective collars too) are kept."
    "On top of that, they seem to have developed individual nervous ticks that weren't there before."
    "Sasha keeps twitching her leg, almost like a dog moving in it's sleep."
    "And Bree is constantly chewing on her lip, as if she's trying to relieve some unseen urge."
    "I have no idea what's going on, and it's beneath the dignity of a master to ask such a thing of his slaves anyway."
    "So I just sit back and watch as the ticks seem to become ever more pronounced as time slowly passes."
    "But eventually, I can only think of one way to call their bluff without losing face."
    "I yawn in what I hope is a convincing manner and begin to rise from the sofa."
    $ game.pass_time(1)
    scene bg livingroom
    hero.say "Okay, time for bed!"
    hero.say "The pair of you, upstairs and into my bed!"
    "Both the girls begin to whine and pout, and at first I think they're actually protesting about being sent to bed."
    show bree naked at right
    show sasha naked at left
    "But then they crawl on all fours towards the hallway, in the direction of the front door."
    "I could order them back, and they'd doubtless obey."
    "But something's going on here, and I want to get to the bottom of it."
    "So I follow them into the hallway, giving them enough slack on their leads to reach their intended destination."
    "They stop by the closed front door, sitting up on their haunches to scratch it with their fingernails."
    "Ah, now it all begins to make some kind of sense!"
    "The other night, when they both wanted to pee at the same time, I called their bluff and walked them to the park to do it, just like a pair of bitches."
    "Well, it seems like they really got off on the exhibitionism and danger that the little late night stroll involved and want to repeat it."
    "They even went to the trouble of making sure they were desperate to pee for added effect!"
    "I shrug and then nod."
    "Why the hell not?"
    "It's not too far from the time we went out the last time, and there was no one around on that occasion."
    "Chances are we won't bump into anyone tonight either."
    "The day has been fairly warm, but there's usually a chill breeze at night right now, so I make sure to grab myself a jacket."
    show bree naked leash
    show sasha naked leash
    "Bree and Sasha don't get any such consideration though, as after all, they're just a pair of bitches."
    "And whoever heard of bitches complaining about the cold or asking for a coat?"
    "I open the door to a chorus of appreciative panting and other sounds of happiness from Bree and Sasha."
    scene bg house
    show sasha naked leash at right
    show bree naked leash at left
    "They eagerly walk out onto the sidewalk on all fours, and I almost forget to scan the street for signs of anyone watching."
    scene bg street
    show sasha naked leash at right
    show bree naked leash at left
    "So hypnotic is the sight of their naked backsides in motion and the occasional hint of breasts, swaying from side to side."
    hide bree
    hide sasha
    show bitches walk
    "Several times before we reach the gates of the park, I'm almost half sure that I can see hints of light as people jerk curtains."
    "It's the way I can't be sure if we're being watched or not that makes the thought so thrilling for me."
    "But if anyone is peeping through their drapes at me walking my most unusual pets tonight, they're not making a point of coming out to confront me about it."
    "It's too late for mundane dog-walkers as we finally walk off of the street and into the park."
    "Though I can hear the occasional noise that I'm sure can't be an animal every now and then."
    "There are no street lights in the park, and we seem to be insulated in our own little world of darkness as we find our way to a stand of trees."
    "Just then I hear the unmistakable sound of footsteps approaching quickly."
    "I glance over my shoulder in time to see a jogger pounding her way up the path towards where I'm standing."
    "I step neatly out of the way as she passes, giving her a polite smile."
    "But all the time I'm silently panicking, trying to resist the urge to glance over at Bree and Sasha for fear of drawing the eye of the jogger as well."
    "She gives me a brief glance and a smile, before she passes me and jogs off until she's out of sight."
    "Finally I can breathe out and look over towards where I last saw my bitches."
    "Shaken by the experience, but not wanting to show it to Bree and Sasha, I walk into the stand of trees and call for them to come to me."
    "They obey eagerly, making me think that either they missed the passing of the jogger entirely, or else did not and enjoyed the thrill of coming so close to being seen."
    show bitches blowjob
    "It's then that I look up to see that they both have a hand raised, asking permission to speak."
    menu:
        "Allow Bree to speak":
            hero.say "Alright, Bree - what do you have to say?"
            bree.say "Now that we've had our exercise and fun..."
            bree.say "Would Master allow me to do something nice and fun for him?"
            "Sasha looks disappointed that Bree got to speak first, but she obediently stares at the ground all the same."
            "I look at Bree's smile and her wide, innocent-seeming eyes."
            "Why shouldn't I indulge her?"
            "We've only seen one other person the entire time we've been out here, and now we're well and truly standing in amongst the trees"
            "Also, my nerves are getting pretty frayed around the edges."
            "I could do with something enjoyable to calm me down before we head back home."
            "I smile indulgently at Bree and nod my assent."
            "In response, she claps her hands together and happily shuffles forwards until she's kneeling before me."
            "Bree sets about unzipping my flies and pulling out my cock, making small, excited noise as she does so."
            "It's cold in the spot where we're standing, and that breeze returns now with a vengeance."
            show bitches blowjob breesuck
            "But as if she can sense the way in which the cold is making me a little uncomfortabele, Bree wastes no time in wrapping her lips around my dick."
            "I'm not yet fully aroused, but the wet, warm sensation of her tongue soon fixes that problem."
            "Watching Bree's face as she literally coaxes my cock to being fully erect is an experience in of itself."
            "As it grows, she's forced to manoeuver around it and struggle to keep the entire thing inside of her mouth as much as possible."
            "Her almost stubborn determination to keep it from escaping her is almost as arousing as the feeling of the blow-job she's giving me at the same time."
            "Indeed, Bree whines and pines whenever it looks like my dick is going to slip from between her lips."






            show bitches blowjob breesuck breemouth




            "I lose myself in Bree's mouth, a trickle of my cum begins to seep from the corner of her mouth."
        "Allow Sasha to speak":
            hero.say "Yes, Sasha - you may speak."
            sasha.say "Master...are you quite okay?"
            sasha.say "You seem a little pale...what can we do to make you feel better?"
            "Bree looks down, obviously somewhat ashamed not to have noticed the same change in her Master as Sasha has."
            hero.say "I don't know, Sasha - what did you have in mind?"
            "Sasha shuffles forward, looking meek and demure as she does so."
            "But then she begins to paw at my crotch, her tongue hanging out as she does so."
            "Sasha adds to the effect by whining a little pathetically and looking up at me with huge, appealing eyes."
            "I nod in approval, and her expression immediately transforms into one of open anticipation."
            show bitches blowjob dick
            "Sasha slowly opens my flies and reaches inside with her fingers to take hold of my cock."
            "She doesn't pull it out immediately, and instead spends some time stroking and rubbing it in very pleasant manner."
            "This means that not only am I almost erect by the time she actually does pull out my dick."
            "But it's also had the last traces of the cold massaged out of it and I hardly feel the chill of the breeze at all."
            show bitches blowjob sashasuck
            "Only now does Sasha begin to inch my dick into her mouth, taking a little more in with each lick and caress of her lips and tongue."
            "She works quickly, rather than dragging it out as she might have had we been in a more private setting."
            "But the effect only serves to intensify the feelings of pleasure that her ministrations are giving me."
            "Soon Sasha is taking my dick so deeply into her mouth and with such determined speed that I begin to worry about her over-facing herself."
            "But she never gags or chokes once, and the deeper that she takes me the more enjoyable the experience becomes as a result."





            "Soon I'm on the brink of cuming, and there's nothing more that either of the bitches can do to prolong the experience."
            show bitches blowjob sashasuck sashamouth
            "I cum in Sasha's mouth, and the depth that she's taken me in means that she has to swallow without thinking about it."
            "She does so as I pull out, gasping for air in the hope of making it easier for herself."
            hide bitches
            show bitches blowjob sashafacial
            "But in doing so triggers a few aftershots of my cum, splattering on her face."


    hide bitches
    show bitches blowjob
    "I stand still and allow the bitches to push my cock back into my pants and zip them up between them."
    show bitches walk
    "With their leads firmly back in my hand, I give them a firm but gentle tug, making them trot along almost perfectly at heel."
    "It doesn't take us long to walk the short distance back home, and there are even fewer signs of life along the way than there were earlier in the evening."
    "Once we're back in the house, I lock the front door and turn to face my pair of bitches."
    hero.say "Right...NOW it's upstairs and into my bed!"
    "Without a hint of protest, both Bree and Sasha turn and dash eagerly up the stairs."
    "I follow silently, astonished that they still have so much energy left."
    $ game.pass_time(1)
    return

label sasha_likes_blondes_3:
    $ sasha.set_flag("haircut", False)
    return

label sasha_likes_blondes_2:
    $ sasha.set_flag("haircut", True)
    scene bg livingroom
    "I admit that I have a habit of getting home and collapsing in front of the TV at the end of the day, zoning out and being hard to reach."
    "But in my defence, I have a tough job, my boss is an asshole of the highest order, and my personal life isn't exactly serene at the moment either."
    show sasha
    "So when someone walks confidently into the living room and almost seems to present themselves for an inspection, it takes me a couple of seconds to snap out of it."
    "Almost immediately I know that this is the wrong decision, as the first thing I realise is that the person standing in front of me is female, and demanding attention."
    "The second thing I realise is that the body and face belong to Sasha, but there's something bugging me about what I see."
    "Luckily for me, my TV-addled brain is stirring rapidly from its former sluggishness."
    "This means I can make a vague connection between the fact that something's different about Sasha's appearance and the fact that she's almost demanding that I look her up and down."
    "My astute deduction, therefore, is that she's changed something, and now she wants a suitably genuine and spontaneous-sounding compliment on whatever that change is."
    sasha.say "Well, what do you think?"
    "I make as quick of an appraisal of her as I can manage, searching for the elusive change."
    "Her face and make-up look no different from the usual, no help there."
    "Clothes are the same band T-shirt and shorts, another blank."
    "Sasha looks increasingly impatient as I struggle to locate whatever it is I should instantly have noticed."
    "What else is there to see?"
    "What else can girl chance on a whim?"
    "Hair, that's it!"
    "Now that I'm actually fully awake and paying attention, I can see that it should have been obvious."
    "Sasha's hair is no longer its characteristic black, but instead a shockingly platinum blonde instead."
    "All that remains of the former colour is a hint of darkness around the roots."
    hero.say "Wow...that's really quite a...quite a change!"
    "Sasha instantly looks frustrated at the bland and noncommital nature of my comment."
    sasha.say "Really, [hero.name]?"
    sasha.say "Is that all you can summon up to say?"
    sasha.say "I was hoping for a 'fucking hell' or something like that, at the very least!"
    hero.say "Sorry...it's just a bit of a surprise, that's all."
    sasha.say "Well?"
    hero.say "Well what?"
    sasha.say "Well now that you've had a chance to let this crazy news sink in - do you like it or not?"
    menu:
        "I don't like it":
            hero.say "Erm...well...not really."
            $ sasha.love -= 10
            sasha.say "WHAT?!?"
            hero.say "Ah...I'm going to guess that wasn't exactly what you wanted to hear...and that it's too late to change my answer."
            "Sasha puts her hands to her forehead in a gesture of frustration, then runs her fingers through her hair."
            "This only seems to make things worse, as she glances down to see the now blonde locks between her fingers."
            sasha.say "But the other night, when we were getting takeout with Bree - you told me that you preferred blondes!"
            "Oh dear - it seems Sasha read far too much into a comment I made in the hope of covering the fact I was actually staring at Bree's ass."
            hero.say "Yeah, Sasha - I remember what I said at the time."
            hero.say "But I never actually said that you should go out and do something this drastic just to please me either!"
            "Sasha's anger seems to be simmering down into irritated resentment, as she mulls over this important fact."
            sasha.say "I...I just thought that you'd like it...that it'd make me more your type."
            hero.say "Sasha, it doesn't work like that - not with me, anyway."
            hero.say "Just because I like blondes doesn't mean that I can't be with you if you've got black hair."
            hero.say "Hell, Sasha - I love cheeseburgers, but I don't want to eat them at every meal."
            "Sasha looks at me sideways, trying to make sense of my last comment."
            hero.say "Maybe that's a bad metaphor...but what I'm trying to say is that I don't need you to change in order to keep me interested in you."
            sasha.say "You might have been more specific about that."
            sasha.say "Jesus...this shit is going to take months to grow out!"
            "A sudden flash of inspiration crosses Sasha's face."
            sasha.say "Unless I shave my head and start from scratch!"
            sasha.say "[hero.name], what do you think about girls with shaven heads?"
            "Her tone and expression are so sincere that I must look genuinely shocked at the question."
            sasha.say "Joking!"
            sasha.say "Don't worry, I'll just have to grow it out, I guess."
            $ game.set_flag("LikesBlondes",False)
            $ game.set_flag("LikesBlondesDelay",True,duration=7)
        "I love it":
            $ sasha.love += 5
            hero.say "I like it, Sasha...I like it a lot!"
            "Sasha doesn't say a word, but her face shows a genuine delight which makes the impact all the more impressive."
            hero.say "I think I didn't notice it at first because it looks so good."
            hero.say "Maybe this is how I always pictured you, and it took me a second to realise I wasn't imagining it?"
            "Cheesy line, I know."
            "But in my experience, girls don't really pick up on that kind of thing when they want to be flattered and you're obliging them."
            sasha.say "You really think so?"
            "Sasha's blushing now, drinking in the compliments eagerly."
            "I nod, and not out of a desire to simply make her feel good about herself and validate her decision."
            "I've always found dyed hair a big turn-on, and what with the black still showing at the roots, Sasha's platinum blonde locks are really doing it for me."
            "The combination of the two makes her normally dark look feel instantly more edgy and trashy somehow."
            "All I can think about is getting up to the kind of kinky shit that I already know Sasha likes in the bedroom."
            "But now I keep imagining those dirty blonde locks hanging over me or grabbing them firmly in one hand."
            sasha.say "I really wasn't sure if I should risk it."
            sasha.say "But after you complimented Bree on her hair, I thought you'd like it if I were blonde too."
            "I have to call that a win - trying to cover up checking out another girl's backside and ending up with the one I'm fucking making changes I love thanks to my lame excuse at the time!"
            hero.say "You were right!"
            hero.say "But yours is better, much better."
            sasha.say "How so?"
            hero.say "Bree's is natural, so I guess it looks all sweet and innocent on her."
            hero.say "Yours is more down and dirty, you know?"
            "I know Sasha's kinks pretty well, and I'm not surprised that being described in such terms elicits a sly smile."
            hero.say "I suppose I'm trying to say it's more punk rock than pop - more Joan Jett than Joan Rivers."
            hero.say "Does...does it make you feel different?"
            hero.say "Does it make you feel more dirty, Sasha?"
            sasha.say "I don't know...but maybe there's a way we could find out?"
    "Seemingly satisfied with what I've said on the subject, Sasha walks out of the room and leaves me alone once more."
    "I'm left reflecting that, though you can never see either coming, there are definitely good and bad surprises to be had in life."
    "But I'm still not entirely sure which kind just popped up in my own."
    return

label sasha_likes_blondes_1:
    scene bg livingroom
    show sasha
    "It's one of those evenings when no one needs to spell it out, everyone just knows that you're all dog-tired and wanting to chill out in front of the TV."
    "To begin with, it's just Sasha and me, so there are lazy embraces and maybe a few more relaxed possibilities on the cards."
    hide sasha
    show sasha at left
    show bree at right
    "But then Bree joins us, and the mood becomes altogether more focussed on simply filling the remaining hours of the day with laziness and inactivity."
    "At some point, one of us thinks to order pizza, but I'm so tired and unfocussed that I really can't recall who."
    "Maybe it was Bree, as she's the first up and making for the door when the food arrives."
    "On her way back in, she bends over to put the boxes down on the coffee table, and I get an unexpected chance to check out her ass as she does so."
    "I wasn't looking to ogle Bree in particular."
    "But as she's wearing yoga pants and her backside is no more than a metre from my face, I kind of can't help getting an eyeful."
    "Sasha elbows me in the ribs, snapping me out of my reverie and letting me know that she can see what I'm doing."
    "As Bree stands up, I feel the need to lessen the severity of my transgression somehow."
    hero.say "Did you do something to your hair, Bree?"
    bree.say "Erm, no...just washed it like I always do for a night in."
    hero.say "Well, whatever you did...it looks pretty good."
    bree.say "Okay...thanks, [hero.name]...I guess."
    "In the awkward silence that follows, have no idea whether my clumsy attempt to cover my tracks has worked or actually made things worse."
    "We eventually get back to making meaningless small-talk and watching the TV as the pizzas are slowly devoured."
    "Bree yawns a little later, starting everyone else off doing the same."
    bree.say "Okay...I'm turning in, before I fall asleep right here on the couch!"
    "Sasha and I make our excuses and say that we're staying up still later."
    hide bree
    hide sasha
    show sasha
    "But even as I do so, I'm already worried that Sasha's going to chew me out for staring at Bree's backside."
    "To her credit, Sasha waits almost a full five minutes before making what's supposed to be an innocent comment."
    sasha.say "[hero.name]...I heard you complimenting Bree on her hair before."
    hero.say "Ah...yeah?"
    "How could she have failed to hear me?"
    "She was sitting right there next to me at the time!"
    sasha.say "This is gonna sound pretty dumb...but do you prefer blondes, or something?"
    sasha.say "I mean, you never complimented me like that."
    "Although I'm relieved to not be answering the more dangerous question involving Bree's ass, this could still be a potential minefield in its own right."
    "I can see Sasha's looking at me like she expects an answer, and I can't think up a credible way out of giving her one."
    menu:
        "I prefer blondes":
            hero.say "Well, it's not that I PREFER blondes in any official capacity."
            hero.say "You know, I don't have a membership card for the 'International I Love Blondes Society' in my wallet next to my credit cards."
            sasha.say "But you do like them, don't you?"
            hero.say "Of course I like them, Sasha - I like women with all different colours of hair."
            hero.say "It's just that..."
            $ sasha.love -= 10
            sasha.say "It's just that what?"
            "I can feel myself clutching at straws as I stumble over my words."
            hero.say "It's just that you kinda get it drummed into you that blonde is best, you know?"
            hero.say "TV, magazines, movies - they're all full of blondes."
            hero.say "Even when someone's not blonde, there are ads all over the place for stuff to dye your hair blonde."
            hero.say "You get to the point where you're indoctrinated."
            "Sasha nods a little."
            sasha.say "You want to try being a non-blonde...that's pretty tough sometimes too."
            hero.say "So yes...I guess that I do like blondes."
            hero.say "But it's never been a deal-breaker for me either."
            $ game.set_flag("LikesBlondes",True)
        "I don't prefer blondes":
            hero.say "Me, prefer blondes?"
            hero.say "Hell no!"
            sasha.say "Really?"
            hero.say "Yes, really - I always hated the way that they're shoved down your throat."
            hero.say "Whenever you turn on the TV or open a magazine, it's just blondes, blondes, blondes."
            hero.say "They turn into 'blands' pretty quickly, if you know what I mean?"
            "Sasha nods and laughs at the lame joke, seeming pleased with the answer."
            $ sasha.love += 5
            sasha.say "That's a relief to hear."
            sasha.say "I was thinking that you might have wanted me to go do something crazy, like bleach my hair!"
            hero.say "Nah, I like it just how you have it now."
            hero.say "Don't go changing it on my account."
            "Sasha screws up her face in mock horror."
            sasha.say "But if you weren't into Bree's hair...you must have been checking out her butt!"
            hero.say "Sasha, I couldn't help it!"
            hero.say "It was like an inch from my face!"
            "Sasha laughs and waves away my protests."
            sasha.say "Relax, [hero.name] - you're only human, and it's a nice butt!"
    "That's the last either of us has to say on the matter for the rest of the night."
    "I find myself hoping that it's nothing more than an idle conversation that Sasha will soon forget all about."
    "But then I remember how deep and emotional she can be, and I wonder, not for the first time, if what I've said will end up coming back to haunt me."
    return

label sasha_breast_complex_5:
    scene bg livingroom
    $ HIDDEN.remove("sasha")
    $ sasha.set_flag("boobjob",True)
    show sasha casual
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        sasha.say "Hello, master...I'm back."
    else:
        sasha.say "Hi."
    sasha.say "I hope that you're pleased to see me..."
    "Of course, today is Saturday, more than a week since Sasha left for the appointment at the clinic."
    "Specifically the appointment for her breast augmentation surgery."



    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        "If she weren't so happily subservient to my will, I'd say she was trying to tease me."
        "But as it is, I think she's far more likely presenting me with an opportunity to exercise my control over her."
        hero.say "I'm definitely pleased to have a piece of my property back."
        hero.say "It means I have the chance to inspect the work that I've had done to it."
        "Sasha's pale cheeks colour a little at my speaking of her in such abstract terms."
    "I'm fully aware of just how intrusive, potentially painful and life-changing the enlargement of her breasts must have been."
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        "But I also know how arousing she finds my treating her like an object."
        "And the two in combination must be almost impossible to keep from turning her on to a great degree."
        "I make a vague gesture for Sasha to come and stand before me, winding an index finger in a circle at the same time."
        "She nods and, not needing to be told any more, walks obediently forwards until she stands perhaps two feet in front of me."
    else:
        "Sasha walks towards me."
    hero.say "Well, what are you waiting for?"
    hero.say "Strip."
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        "Sasha nods curtly, clearly enjoying being given orders by me once more."
    show sasha naked
    "She slowly peels off her clothes, easing it down over her arms."






    "As she raises her arms to drag it over her head, I'm treated to a truly magnificent view."
    "First they rise in sympathy with her arms and shoulders, spreading out and then jiggling with the jerking of her muscles."
    "And then they descend in the same manner, settling onto her chest as gravity returns them to their normal position."
    "Sasha proceeds to then caress them, weighing them in the palms of her hands and even gently squeezing their heavy, fleshy masses."
    "If I'd been expecting the operation to leave Sasha with the god-awful kind of implants that make breasts look like soccer balls stuffed under the skin, I was dead wrong."
    "Clearly she'd been very wise when it came to choosing the clinic, as while they were clearly out of proportion to her petite figure, they still looked natural and very alluring."
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        sasha.say "Well, master...will I do?"
        "I gave a grin that was almost a leer, and pointed to the floor right before me."
        hero.say "They look the part, but I want to take them for a test-drive, before I sign off on them."
        "Sasha again nods in obedience and kneels on the floor in front of me."
    else:
        sasha.say "Do you like them?"
        hero.say "I do."
        sasha.say "I am pretty sure you'll like them even more in a few minutes."
    "She shuffles forwards on her knees, making her newly enlarged breasts sway back and forth as she comes."
    "I don't see where she produces the lube from, but nevertheless, it appears in her hands."
    "Sasha makes a great show of slowly rubbing the transparent liquid onto her breasts."
    "She once more massages and caresses them as she does so, spreading the lube between them and then over their entire mass."
    "Sasha pinches her enlarged nipples as she sweeps her hands over them, the darkened skin puckering as they become suddenly erect."
    "There's little to do for my sake once she opens my flies and reaches in to pull out my dick."
    hide sasha
    show sasha tittyfuck
    "Placing the tip just beneath her now slick breasts, Sasha moves downwards so that it travels straight up and between them."
    "She makes perhaps a half-dozen more such passes, and then suddenly presses them together so that my dick is caught in the middle."
    "The unexpected pressure makes me gasp audibly as the head emerges, from the cleft."
    "Sasha's breasts are baffling mixture of softness and substance, both cushioning and squeezing at the same time."
    "She works me in that same way now, keeping the pressure up as she slides my dick between her breasts."
    "The way that her hands cause them to push together and then return to their resting shape is almost hypnotic to watch."
    "Sasha's new chest seems to almost possess a life of its own as she uses it to tease my and caress me all at the same time."
    "All the while, Sasha pants and moans, as if the feeling of my dick is arousing her in the same manner as her breasts are me."
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        sasha.say "Uh...uh, master...please...may I..."
        hero.say "Speak up!"
        sasha.say "Master...please...may I...touch myself?"
        "I nod, trying not to look too turned on my her desperate desire to masturbate right in front of me."
    "Sasha wraps her breasts with one arm to keep them around my dick, while her free hand almost darts for her denim shorts."
    "I might not be able to see what she's doing, but soon I can feel the results."
    "Sasha's pants and moans become all the more pronounced, and she begins to move in time with her ministrations to herself."
    "The rhythm this creates is immediate and intense, as she's effectively stimulating herself and then me in turn as she moves in sympathy."
    "Sasha's lips are now puckering and parting, her tongue curling with the increasing pleasure she's feeling."
    "She's in serious danger of finishing me off any moment, but now I can't take my eyes of the appealing sight of her open, gasping lips."
    hero.say "Sasha, take me in your mouth...now."
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        sasha.say "Uhh...yes, yes...master!"
    show sasha tittyfuck blow
    "Hurrying to obey, she wastes no time with kissing or caressing the head of my dick."
    "Instead she simply wraps her lips around it and eagerly swallows as much as she can without either gagging or choking."
    "Still with her own fingers inside of herself, Sasha sucks away at the same intensifying rhythm."
    "I could swear I can feel the very emanations spreading out from her pussy and through her entire body."
    show sasha tittyfuck blow mouth
    "I cum mere seconds later, and Sasha struggles to take it all, keeping it in her mouth and not following her instinct to swallow."
    "A wave of my hand lets her know that she can release me, and she does so, keeping her eyes on me at the same time."
    if "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        hide sasha
        show sasha tittyfuck swallow
        hero.say "Open wide - let me see it."
        "Sasha obliges me by opening her mouth wide, letting me see the cum still upon her tongue."
        hero.say "Very good...you may swallow it now."
        "She nods demurely as she complies."
        sasha.say "Thank you, master."
    hide sasha
    "I pat the sofa beside me, and Sasha crawls up to curl herself beside me, almost like an oversized house-cat."
    "She makes no effort to cover up her breasts, still soaked in a mixture of sweat and lube."
    "I amuse myself by idly playing with her stiff nipples and listening to the soft moans this arouses from her."
    "Neither of us speaks, but I'm already thinking of the new possibilities where my submissive pet's new assests are concerned."
    return

label sasha_breast_complex_4:
    show sasha
    hero.say "What's up?"
    "Sasha walks over and sits down next to me on the bed."
    sasha.say "Well, first of all I wanted to say sorry for being all weird and angry with you the past couple of days."
    hero.say "Ah, I see...you mean about..."
    sasha.say "Yeah, yeah...about my breast size."
    hero.say "Apology accepted."
    "Sasha smiles wanly at my response, clearly pleased to know that she's back in good graces with me."
    sasha.say "I just got to thinking of how selfish and unfair I'd been about all of this, you know?"
    hero.say "I did feel a bit like you bit my head off, Sasha."
    hero.say "Especially when it was you who asked me to be honest!"
    sasha.say "I know...I'm sorry I was so unreasonable."
    sasha.say "I've come to realise that it's my problem, not yours."
    sasha.say "I've always been really insecure about the size of my breasts."
    sasha.say "But that's my fault, and I've been taking it out on you."
    sasha.say "I was so full of that feminist idea that my body was mine alone, that I totally forgot that you have rights too."
    "I just keep nodding, allowing her to say her piece."
    "But all the time I'm wondering where this is ultimately going."
    sasha.say "That's why I've given it some serious thought, and I've decided to have my breasts enlarged."
    "Of all the things she could have said, I wasn't expecting that."
    sasha.say "After all, I'd only be doing it to make myself more attractive to you."
    sasha.say "And if you want me more, then we both get something we want out of it."
    sasha.say "Don't we?"
    menu:
        "I'll help you pay for it" if hero.money >= 500:
            hero.say "Wow, Sasha - I'm such a lucky guy to have a girl that'd go to such lengths for me!"
            "Sasha's face positively lights up with delight at my approval."
            sasha.say "Okay - I've done some research on clinics with a good record in the city."
            sasha.say "And I think that I've come up with a way I can pay..."
            hero.say "Oh no, you're not paying for it - I am."
            $ sasha.love += 10
            $ sasha.sub += 10
            show sasha blush
            "Sasha looks at me in genuine surprise."
            hero.say "I'm the one that wanted you to have bigger breasts, so the least I can do is pay for them."
            hero.say "Think of them as a gift that'll keep on giving for the both of us."
            hero.say "I know I'm already thinking of how to repay you after the surgery's over!"
            $ game.set_flag("BreastComplexDelay",1,duration=7)
            $ HIDDEN.append("sasha")
        "That's a great idea":
            hero.say "We sure do!"
            hero.say "I can almost imagine them already!"
            "I cup Sasha's petite breasts in my hands without asking for permission, massaging them as I think of them massively increased in size."
            sasha.say "So you're okay with me getting it done?"
            "Sasha's cheeks have flushed as I continue to play with her nipples."
            "I can hear a question in her tone, but I'm more interested in pinching her now stiffening nipples than seeking it out."
            sasha.say "[hero.name]...it's just that...ah...I was...ah...wondering if you could...help me out...with the cost?"
            hero.say "Woah, Sasha - that's pretty manipulative of you, don't you think?"
            $ sasha.love -= 10
            $ sasha.sub -= 10
            show sasha sad
            sasha.say "Huh?"
            hero.say "I mean - you come in here, all apologetic and demure to start with."
            hero.say "Then you tease me with your boobs and try to milk me for money!"
            sasha.say "I...no...that's not it!"
            hero.say "The least you could do is pony up the cash yourself."
            hero.say "That'd show me you were REALLY sorry."
            sasha.say "Uh..well...I guess so."
            $ game.set_flag("BreastComplexDelay",1,duration=7)
            $ HIDDEN.append("sasha")
        "You should not do it":
            hero.say "You're serious?"
            sasha.say "Of course I am!"
            hero.say "Look, Sasha - I've been thinking too, and I don't really want you to have the surgery."
            show sasha happy
            "Sasha's expression shows surprise at my confession, but also not a little relief too."
            sasha.say "But...but I thought you said you liked bigger breasts than mine?"
            hero.say "What I meant was that I like bigger breasts on girls with bigger breasts."
            hero.say "And I like your breasts on you!"
            sasha.say "Really?"
            hero.say "Yes...how could an over-sized pair of dumplings stand to attention like yours are right now?"
            "Sasha giggles and instinctively covers her breasts with her hands."
            "But I can see that she's flattered and more than a little aroused by the praise I've just heaped on her petite chest."
            $ sasha.set_flag("BreastComplex",0)
    "Once we're done talking about the subject, I feel much better, like the air has finally been cleared between us."
    "Sasha plants a kiss on my lips and scurries away to her own room, not saying another word."
    "Little by little, I think we're coming to understand each other so much better than before."
    return

label sasha_preg_talk:
    show sasha
    sasha.say "I kinda have something I need to tell you."
    "I give her the same raised eyebrows, not letting on that I've already seen this coming."
    sasha.say "Well...you know how we've 'forgotten' to use protection a hell of a lot recently?"
    "Even though I've been trying to play it cool, I can't keep my eyes from widening."
    hero.say "Do you mean what I think you mean?"
    sasha.say "Depends on whether or not you think I mean that I'm pregnant!"
    "We both fall silent from the enormity of what Sasha just admitted."
    "But we can't stay silent forever, not with something of that magnitude hanging over the both of us."
    "Eventually, it looks as though Sasha is going to be the one to break the silence for the second time."
    if sasha.sub <= 50:
        "Sasha coughs loudly, taking control of the conversation."
        if sasha.love >= 180:
            sasha.say "We both had a hand in making this happen, so I think we both need to step up and take ownership of it as well."
            hero.say "Erm...you mean like, stepping up and being a man?"
            sasha.say "Geez, you make it sound like it's the scariest thing that you could imagine."
            hero.say "Well...it is kind of scary."
            sasha.say "How about you take it a step at a time?"
            sasha.say "Maybe try being a dad first, then step it up to a fully-fledged man at a later date, eh?"
            $ sasha.set_flag("toldpreg")
        else:
            sasha.say "I can't raise a child on my own, and I can see from your face that you'd be no use to me either."
            "I open my mouth to speak, but Sasha's blunt appraisal of me means that my lips move and nothing comes out."
            sasha.say "Yeah, you see now would have been the time to speak up and prove me wrong."
            sasha.say "But all you can manage is a lousy impression of a goldfish."
            sasha.say "That's why I'm having a termination - the timing's just not right."
            hero.say "Erm...well...if you think that's what'd be best..."
            $ sasha.set_flag("pregnant",0)
    else:







        "Sasha looks at me imploringly, clearly waiting for me to tell her what we're going to do."
        menu:
            "Let's keep the baby":
                $ sasha.love += 10
                hero.say "Well, I can't say that I was expecting you to say that."
                sasha.say "You're...you're not mad, are you?"
                hero.say "No, I'm not mad - you'd know if I was mad."
                sasha.say "Okay...but what are we going to do?"
                hero.say "We're going to keep it, that's what we're going to do."
                sasha.say "Really - you think that's for the best?"
                hero.say "I do, so just do as I say and it'll be fine - you'll see."
                $ sasha.set_flag("toldpreg")
            "Tell her to abort":
                $ sasha.love -= 25
                hero.say "We can't have a kid, Sasha - you know that as well as I do."
                show sasha sad
                sasha.say "But...but I'm pregnant, the test was positive!"
                hero.say "Well we'll just have to fix that then, won't we?"
                sasha.say "You mean...you want me to have an abortion?"
                hero.say "Who said anything about wanting - you're having one, and that's all there is to it!"
                "Sasha looks down at her lap as any thoughts of doing otherwise fade from her mind."
                sasha.say "Okay...I suppose you know what's best."
                $ sasha.set_flag("pregnant",0)
            "Dump Sasha":
                "I sigh and begin to rub my forehead with one hand, my frustration at the unexpected news clearly evident."
                sasha.say "What's wrong, [hero.name] - are you mad at me?"
                show sasha sad
                hero.say "Goddamn it, Sasha - of course I'm fucking mad at you!"
                "Sasha flinches back at the anger evident in my voice."
                hero.say "Jesus, how in the hell could you let this happen - how could you be so stupid?!?"
                sasha.say "But...but we both didn't remember to use..."
                hero.say "Shut up, Sasha - don't go trying to pin this one on me!"
                hero.say "You're the one that's pregnant, and it's your problem -don't expect me to bail you out now!"
                sasha.say "[hero.name], what are you saying?"
                hero.say "Oh I think you know, but I'll spell it out for you, just to be sure - you're dumped, Sasha!"
                $ sasha.set_flag("toldpreg")
                $ sasha.love -= 100
    return

label sasha_pregnant_flag:
    $ sasha.set_flag("pregnant",1,mod="+")
    return

label sasha_kiss_me:
    call sasha_greet from _call_sasha_greet_5
    show sasha
    if not sasha.get_flag_value("kiss"):
        "Sasha walks towards me with a decided look in her eyes."
        "She seems to hesitate a little, then leans toward me, she obviously tries to kiss me."
        $ result = renpy.display_menu([("Kiss her",1),("Don't kiss her",2)])
        if result == 1:
            hide sasha
            show expression "sasha kiss "+sasha.get_clothes()
            "Sasha kisses me with passion and lust."
            "After some time (I couldn't tell how long), we part."
            if sasha.love() >= 60 - hero.charm()/2:
                hero.say "What's the occasion ?"
                sasha.say "I felt like giving myself a treat."
                hero.say "Feel free to indulge yourself whenever you feel the need."
            else:
                sasha.say "I shouldn't have done that..."
            $ sasha.set_flag("kiss",1,"permanent","+")
            $ sasha.love += 1
            hide expression "sasha kiss "+sasha.get_clothes()
        elif result == 2:
            "Sasha looks hurt when I push her away."
            $ sasha.love -= 1
    elif "sasha_sub_event_1" in DONE and sasha.sub >= 75:
        "Sasha looks at me meekly..."
        sasha.say "Could your cute little slave ask for a kiss master?"
        menu:
            "No":
                hero.say "You haven't been a good enough slave."
                $ sasha.sub += 1
            "Yes":
                show expression "sasha kiss "+sasha.get_clothes()
                "I lean and kiss Sasha passionately."
                hide expression "sasha kiss "+sasha.get_clothes()
                show sasha
                sasha.say "Thank you master."
                $ sasha.love += 1
    else:
        "Sasha walks toward me..."
        show expression "sasha kiss "+sasha.get_clothes()
        "...and kisses me deeply."
        hide expression "sasha kiss "+sasha.get_clothes()
        show sasha
        if sasha.love() >= 60 - hero.charm()/2:
            hero.say "What's the occasion ?"
            sasha.say "I felt like giving myself a treat."
            hero.say "Feel free to indulge yourself whenever you feel the need."
        else:
            sasha.say "I shouldn't have done that..."
        $ sasha.love += 1
    hide sasha
    return

label kleioannafoursome2:
    "Maybe it's just me, but since we took the leap of becoming a foursome, the band just seems to gel so much better than before."
    "Even when we're only practising, it's as if we know what each other's going to do before we do it, like we're all of one mind."
    "So much so that after the first practice session following our initial four-way dance, the atmosphere in the small space is crazily charged."
    "While I'm playing like a prodigy, I still can't keep from picturing the girls in various compromising positions."
    "And they must be in a similar state, as glances are shooting between all of us, along with lingering stares when someone thinks on one else is looking."
    "When we finally call it a night, it's fairly obvious that no one really wants to call it a night."
    hero.say "Erm...do any of you guys fancy coming back to my place?"
    hero.say "We can...watch something on Netflix, maybe?"
    show kleio
    kleio.say "Why don't you just ask us to come round and look at your damn etchings?!?"
    show sasha behind kleio at left
    sasha.say "Are you trying to ask us all round for a fuck?"
    hero.say "Well...now that you mention it..."
    show anna behind kleio at right
    anna.say "That sounds really good to me - otherwise I'd just end up going home and playing with myself until I fall asleep again!"
    "Well, I guess that decides the matter."
    scene bg bedroom1
    "Almost before I can get my head in gear, we're back at the house and in my bedroom, all four of us eagerly stripping off our clothes."
    "Kleio seems to be the most tired of all, reclining against the headboard in a languid manner."
    "Sasha drapes herself on the side of the bed, her dark eyes open, yet with a sleepiness that only adds to her appeal."
    "In contrast, Anna is the most eager and alert, almost hopping into the middle of the bed like an excitable puppy."
    show band foursome2 kleio sasha
    "Knowing smiles pass between Sasha, Kleio and myself, each of us turned on and woken-up by Anna's seemingly boundless energy."
    kleio.say "Whoa, down girl!"
    "As if sensing that she's putting us in mind of an eager canine, Anna grins and gets onto all fours."
    show band foursome2 kleio sasha pussylick
    "She sticks her tongue out and leans in to lick at Kleio's exposed pussy, earning an aroused chuckle for her efforts."
    hide band
    show band foursome2 kleio sasha
    "A second later, she looks over her shoulder at me, wiggling her ass as if she had a tail to show off."
    "When she sees the effect she's having on my dick, she grins, beginning to pant and whine."
    "I'm about to literally pounce on Anna's ass, when Sasha rests an elbow upon it and catches my eye."
    "She smiles slowly, reaching out with one hand to caress the underside of my dick, clearly offering me an another choice altogether."
    show band foursome2 pussylick kleio sasha
    $ CONDOM = False
    menu:
        "Fuck Anna's pussy" if CONDOM:
            "As good as Sasha's lips look right now, I only have eyes for the ones between Anna's legs."
            "I hastily snatch up a condom from the bedside table and put it on, parting Anna's buttock still further with my hands once I'm ready."
            show band foursome2 kleio sasha vaginal condom
            "There's no need to play around, as Anna's already more than in the mood, and so I sink into her slowly yet surely."
            show band foursome2 kleio sasha vaginal condom asslick
            "Undeterred by the minor snub, Sasha leans in and begins to use her tongue on Anna's exposed ass, while Anna herself continues to lick at Kleio's pussy."
            "Sasha and I find ourselves gazing at Kleio, as she registers the pleasure from Anna's tongue, as if we're passing it through the petite girl and into her body."
            "Maybe that's why, as soon as I show signs of peaking and Anna begins to cry out in turn, Kleio begins to clamber up the headboard as her own climax builds as well."
            "I'm all but pounding at Anna's pussy when I finally cum, her buttocks quivering with each thrust."
            "The condom catches everything as it's supposed to, but the force of it tips Anna over the edge as well."
            "She gives up on licking at Kleio's pussy to let out a desperate cry as she succumbs to her orgasm."
        "Fuck Anna's pussy" if not CONDOM:
            "What can I say - Anna's pussy is calling to me, and so I answer in kind."
            show band foursome2 kleio sasha vaginal
            "It only takes a matter of seconds to push into Anna, as she's already slick and welcoming."
            show band foursome2 kleio sasha vaginal asslick
            "As I begin to thrust into her, Sasha leans over the other girl's buttocks and starts to lick at her taught ass."
            "Anna herself has not stopped doing the same to Kleio's pussy, and now all four of us are coming together as one mass of heads, limbs and holes that are begging to be filled."
            "It's Kleio that seems to begin cumming first, throwing her back against the wall and moaning deeply."
            "Then the same reaction almost cascades through us, first with Anna quivering, and then the feeling that I'm about to cum seconds later."
            "Anna fits me like a glove, squeezing me so tightly that I can't imagine there's room inside of her for anything else at all."
            "But when I finally lose myself and burst in that same exquisite place, the result is explosive."
            "Anna shrieks in helpless arousal as she too now begins to cum, the inside of her pussy squeezing me like a clenching hand."
        "Show Sasha who's the boss" if sasha.sub > 75:
            "I can see both the lips of Anna's pussy and the black-painted lips of Sasha's mouth, both slick, appealing and within reach."
            "It's so hard to choose between them, that I decide I won't."
            show band foursome2 kleio sasha anal
            "Firstly I sieze Anna's pert buttocks and thrust into her as deeply as I can."
            "She squeals with pleasure, and I watch disappointment cross Sasha's face at being overlooked."
            show band foursome2 kleio sasha blowjob
            "But after only a handful of thrusts, I pull out without warning and force Sahsa's lips around my cock."
            "She chokes in surprise for a moment, but obliges, rather than suffocate, and is soon pleasuring me with some enthusiasm."
            show band foursome2 kleio sasha anal
            "Before she can make me cum, I pull away from her and without warning stick my dick back into Anna's ass."
            "Her exhausted panting once again becomes a more intense squeal of pleasure."
            "Sasha watches me from where she's laid, saliva dripping down her chin."
            "I can see confusion on her face, her cheeks flushed red, but her hand already sliding towards her pussy in arousal."
            if randint(1,2) == 1:
                "I already know how much Anna loves being taken up the ass, and that turns me on all the more."
                "I can't help but keep on thrusting myself ever harder into Anna's pert little ass, and all too soon I feel myself cumming."
                show band foursome2 kleio sasha anal cum
                "I don't think that I could pull out if I tried, and I listen to her cries of arousal as I release myself into her without pause."
            else:
                "But a second later, I realise that I'm on the brink of cumming too."
                "I decide that Sasha should be rewarded..."
                menu:
                    "Cum in Sasha's mouth":
                        "I seize the sides of her head with my hands, pushing her down as my orgasm finally hits."
                        show band foursome2 kleio sasha blowjob cum
                        "As I hear Sasha gag and splutter with her mouth full of cock and cum alike, I just hope she remembered to breathe through her nose."
                    "Cum on Sasha's face" if False:
                        "I decide to pull my dick out of Anna's ass."
                        show band foursome2 kleio sasha out cum
                        "Still slick with juices, it nods for a moment before Sasha's face, and then releases itself in a sudden fountain."
                        show band foursome2 kleio sasha out facial
                        "Her mouth open in shock, Sasha is splattered with the sticky, white mass, making me feel a little like an animal marking its territory."
        "Fuck Anna's ass" if sasha.sub <= 75:
            "All I can see is Anna's ass, shaking from side to side, and in that moment I want it more than anything I can imagine."
            show band foursome2 kleio sasha anal
            "Taking a buttock in each hand, I mercilessly thrust myself into her anus, pushing until I'm as deep as I can get."
            "Anna's squeal of surprise serves only to turn me on all the more, making me start pumping away in the hope of eliciting more."
            show band foursome2 kleio sasha anal asslick
            "As I begin to thrust into her, Sasha leans over the other girl's buttocks and starts to lick at her taught ass and my shaft at the same time."
            "It takes all of Anna's willpower to keep on doing the same to Kleio, as she finds herself being pleasured from two angles at once."
            "As we all begin to build to an inevitable climax, I can't help wondering if we're turned on by Anna's cries just because we're aroused her."
            "Or because she sounds like a wounded, helpless animal and we're all suddenly on the hunt."
            "I already know how much Anna loves being taken up the ass, and that turns me on all the more."
            show band foursome2 kleio sasha anal asslick cum
            "I can't help but keep on thrusting myself ever harder into Anna's pert little ass, and all too soon I feel myself cumming."
            "I don't think that I could pull out if I tried, and I listen to her cries of arousal as I release myself into her without pause."
        "Fuck Sasha's mouth" if sasha.sub <= 75:
            "Anna's lips look appealing, but not as much as Sasha's, black-painted and currently being licked provocatively by her tongue."
            "I turn my dick to face Sasha, suddenly forgetting about Anna's proffered ass."
            show band foursome2 kleio sasha blowjob
            "Sasha looks more than a little truimphant as she begins to kiss and lick the tip of my dick."
            "Before too long she opens her lips wider and slowly slides the head into her mouth, then as much of the shaft as she can take."
            "In that moment, I forget that there are two other girls in the room, being inside Sasha's mouth feels that damn good."
            "Anna and Kleio must have kept on with whatever they were doing, as I can hear moaning that's not me and simply can't be Sasha."
            "But a second later, I realise that I'm on the brink of cumming too."
            menu:
                "Cum in Sasha's mouth":
                    "I don't know if Sasha is planning on releasing me before I cum, but that's not what I want to happen."
                    show band foursome2 kleio sasha blowjob cum
                    "Instead I seize the sides of her head with my hands, holding her down as my orgasm finally hits."
                    "As I hear Sasha gag and splutter with her mouth full of cock and cum alike, I just hope she remembered to breathe through her nose."
                "Cum on Sasha's face" if False:
                    "Before Sasha can make the decision for me, I pull my dick out of her mouth."
                    show band foursome2 kleio sasha blowjob facial
                    "Still slick with her spit, it nods for a moment before her face, and then releases itself in a sudden fountain."
                    "Her mouth open in shock, Sasha is splattered with the sticky, white mass, making me feel a little like an animal marking its territory."
    hide band
    "It seems as though everyone has used up the very last of the energy they had left over after the practice session, pushing themselves to the point of orgasm."
    "Even Kleio, who was mostly immobile during the four-way love-making session, is all but ready to collapse into unconsciousness."
    "I'm not sure if I should be calling ubers for people or else offering to put them up for the night."
    "But the sound of Anna's loud snoring puts paid to any question of kicking the girls out before morning."
    "I count myself lucky for having bought a bed almost large enough for all four of us to sleep comfortably in."
    "But more lucky to be able to share it with three women the likes of Sasha, Kleio and Anna."
    call sleep from _call_sleep_4
    $ game.room = "bedroom1"
    return

label sasha_breast_complex_3:
    "I push the door to the bathroom open and walk in while still feeling half asleep, and then jump at the sound of someone telling me off."
    show sasha naked angry
    sasha.say "HEY - did you never hear of actually fucking knocking on a door?"
    hero.say "What...huh...oh, sorry...I guess I should have knocked, you're right."
    show sasha naked normal
    "Seeing that it's me and not Bree that barged in on her, Sasha's expression softens a little and she stops reaching desperately for a towel."
    "It's kind of weird to be so prudish about being nude around someone that's gotten up to what we have, after all."
    "Even though I'm still not awake and I just got a little chewed out for my trouble, I still can't help looking Sasha up and down admiringly."
    "She's fresh out of the shower, hair hanging in wet tresses and skin pink from the warmth of the water."
    "Though she has her back to me, I can tell she's watching me in the mirror above the sink."
    "And her expression isn't long in softening as she realises that she's being admired."
    "I catch her smile in the mirror and she shakes her head at my interest."
    "A moment later she hops around, leans forward and waggles her petite breasts at me."
    "Then she hops back the other way, adding a last wriggle of her buttocks just to tease me."
    sasha.say "That's all you're getting right now - I have plans for this morning, and they don't involve your dirty imagination!"
    "Smiling at the little show for my sole benefit, I nod in agreement and go back to eyeing up her buttocks."
    "Sasha pauses in the middle of brushing her teeth, the brush still in her mouth as she speaks."
    sasha.say "Not meaning to be weird, but why do your eyes always seem to be drawn specifically to my ass?"
    hero.say "Erm...because I'm a guy, and you have a great ass?"
    sasha.say "No, really - you can take it all in, but you always end up looking at my ass."
    "I don't really have an answer for that."
    "I haven't spent much time analysing my hierarchy of preferences when it comes to admiring Sasha's body."
    "I suppose that I'm too busy actually doing it to care very much."
    sasha.say "I guess what I mean is...don't you like my breasts?"
    "The question seems so odd that I can't answer it either."
    sasha.say "I know most guys are supposed to like bigger ones, but I thought maybe you liked mine...even though they're pretty small?"
    menu:
        "I like them small":
            hero.say "Sasha, your breasts are fucking amazing...they make me want to touch them whenever I set eyes on them."
            sasha.say "Really?"
            sasha.say "You never said so!"
            hero.say "Sasha, this is the twenty-first century, you know?!?"
            hero.say "Most guys think saying something like that'll get them strung up, never mind dumped!"
            sasha.say "Most guys are idiots."
            hero.say "Okay, for the sake of not being one of them, and for the record."
            hero.say "Sasha, I hereby state that I not only love your breasts, I also cherish, worship and adore them."
            hero.say "I love the fact that I can fit them into the palms of my hands."
            hero.say "I love the way they stand up and beg for attention."
            hero.say "And I love the way they bounce when you're on top of me."
            $ sasha.love += 1
            "Sasha screws up her face at the gushing praise I'm heaping upon her chest."
            sasha.say "Geez, lighten up there, Mr Shakespeare!"
            "She shakes her head to underline how she thinks I'm being over the top."
            "But as she wraps herself in a towel and walks out, she has a glint in her eye and a twitch of a smile."
            "That makes me think she's not totally embarrassed by my proclamations."
        "I like them big":
            hero.say "They're great, Sasha - but..."
            sasha.say "But what?"
            hero.say "Well, don't take this the wrong way, but you wanted me to be honest, right?"
            sasha.say "Yeah...I suppose so."
            hero.say "The thing is that, while they're great, I do kinda more like larger breasts...usually."
            sasha.say "Oh...so you think mine are...too small?"
            hero.say "No, no, that's not what I'm saying...well, kind of it is, but not...if you follow me?"
            sasha.say "I'm not sure that I do."
            hero.say "I just like bigger ones, but yours are great too."
            show sasha naked sad
            "The look of disappointment and confusion on Sasha's face tells me that I'm in trouble here."
            "I open my mouth to go on, but she holds up a hand to cut me off."
            $ sasha.love -= 5
            $ sasha.sub += 5
            $ sasha.set_flag("BreastComplex",1)
            $ game.set_flag("BreastComplexDelay",1,duration=3)
            sasha.say "It's okay, I get it."
            show sasha towel sad
            "She wraps herself up in a towel and stalks out of the bathroom without another word."
            "And I'm left thinking that I pretty much fouled that one up completely."
    "Now that I have the bathroom to myself, I can't honestly remember what I came in here for in the first place."
    "The only thing on my mind now are Sasha and her breasts."
    "But I suppose there are far worse things to be obsessed with."
    return

label sasha_breast_complex_2:
    show bree
    "Seeing as how it was the weekend and the weather was fine, the pool was the natural place I found myself relaxing."
    "But it took me a full twenty minutes to sit up and realise what was actually happening when Bree announced that she was doing the same."
    "I felt like one of those guys living the fantasies I'd dreamed up as a pathetic teenager."
    "I try to stay relaxed and unmoved when Bree strolls out in a white swimsuit and begins to tentatively dip her toes in the water."
    "I feel that she's basically doing the same thing."
    "But it's like she's just too naturally hot to be able to keep from making whatever she does seductive and arousing."
    hide bree
    if sasha.get_clothes() != "swimsuit":
        show sasha casual
    else:
        show sasha
    sasha.say "Hey, [hero.name] - you want some company out here..."
    "I look up guiltily to see Sasha standing by my lounger, clearly thinking of joining me."
    "Or at least she was, until she realised that I was just getting a load of Bree in her swimsuit, sporting in the pool."
    hero.say "Sure, Sasha...erm, it looks like Bree's staying in the water, so I could use someone to talk to."
    "My line sounds lame, mainly because it is."
    sasha.say "Now you come to mention it, the water does look really good this morning."
    if sasha.get_clothes() != "swimsuit":
        sasha.say "Don't go anywhere, I'll be right back."
        hide sasha
        show bree
        "I sit there feeling more than a little puzzled, but another glance at Bree soon cures me of that."
        "She's doing a backstroke, and I can't help being hypnotised by her motions in the water."
        "Her glistening blonde locks and the way her swimsuit clings to her breasts make me think what she'd look like as a mermaid."
        hide bree
        show sasha swimsuit
        "But before I can imagine Bree wearing nothing save for clamshells and a tail, another sight to distract me sasha comes into view."
        "Sasha must have hastily changed and come back to the side of the pool."
        if not sasha.get_flag_value("sexyswimsuit"):
            "As she's now wearing nothing save for a black bikini."
        else:
            "As she's now wearing nothing save for a red bikini."
    "She seems to take one quick glance over her shoulder, almost as if checking that I'm watching."
    "And then she slips off into the water."
    show sasha swimsuit at left
    show bree at right
    "Watching both girls swim, I could almost believe Bree having a halo and feathery wings, and Sasha sprouting horns and bat wings herself."
    "The pair of them are so different, and yet both so sexy in their own way, it's hard to choose which one to watch at any given moment."
    "Eventually Sasha emerges from the pool and comes to lie on the lounger next to mine."
    "She reclines for a while without saying a word, simply enjoying the sensation of the sun upon her skin."
    hide bree
    hide sasha
    show sasha swimsuit
    "While she's silent, I suddenly know which one of them that I want to watch."
    "I can't take my eyes of the pale skin of Sasha's body and how it contrasts so strikingly with her jet-black hair."
    "Her breasts are more petite than Bree's, for sure."
    "But that only means that they stand more erect and proud on her chest, nipples stiff beneath her bikini top."
    "I start to think what it would be like to caress Sasha's little round breasts, to have one in each hand."
    "I realise that I could cover them, hold them entirely, as if my hands were some kind of living bra..."
    sasha.say "[hero.name]...be honest with me, okay?"
    "Sasha keeps her eyes closed as she speaks, but her words don't instantly put me at ease."
    sasha.say "Does Bree look good in that swimsuit she's wearing?"
    "Oh great, one attractive woman asking me in a roundabout way if I think another attractive woman is at all attractive."
    "No hidden traps or pitfalls there then!"
    hero.say "It looks good, I guess...on her."
    sasha.say "What does that mean?"
    hero.say "I suppose it means that I think she's got the figure to pull it off."
    sasha.say "Do I have the figure to pull it off?"
    "Careful now!"
    hero.say "I don't know about that...but she definitely couldn't pull it off the other way round."
    sasha.say "How so?"
    hero.say "Well, don't think I'm being mean, but I think there are times when you need ripe peaches, rather than over-sized melons."
    "Sasha opens her eyes wide at the same moment she opens her mouth in what I take as a scandalised and yet still very much amused grin."
    "I must have said something right, because Sasha's body-language becomes more open and she leans visibly towards me."
    "I should say more, but the fact her rapidly-drying breasts are coming closer makes me clam up and simply stare at them some more."
    hide sasha
    return

label sasha_breast_complex_1:
    "I barely make it to the sofa before I collapse and let out a groan of utter exhaustion."
    "I'm so tired that I can't even be bothered to turn on the TV, so I just grab the first thing within reach to read."
    "It's a glossy women's lifestyle magazine, the kind of thing that Sam used to leave scattered around the house all the time."
    "Not ideal reading material, but there's usually at least one article or photoshoot that classes as VERY softcore titillation."
    "That could be just what I need right now, as anything more stimulating might render me unconscious with a mere glance."
    "I've been flicking through the pages for what feels like a couple of minutes before I get the feeling of being watched."
    show sasha
    "Glancing up blearily, I see Sasha, leaning in the doorway and grinning evilly in my direction."
    sasha.say "Getting in touch with your feminine side, eh?"
    "I take a while to answer, as in addition to being worn out, I'm also too busy checking Sasha out too."
    if sasha.get_clothes() == "sleep":
        "She's clearly winding down for bed, wearing nothing save for a pair of tight shorts and a cut-off band T-shirt."
        "Even without make-up, her mocking features are filled with wicked allure."
    hero.say "Huh?"
    hero.say "Oh...this?"
    "I hold up the magazine, trying to sound nonchalant."
    hero.say "Nah, it's just Sam's, she must have forgotten it...I was looking at the pictures, that's all."
    sasha.say "Why, you too much of a pussy to look at actual porn?"
    hero.say "No...it's just that there are actually some interesting and informative articles in here."
    "Sasha raises her eyebrows in questioning amusement."
    hero.say "Really, there are...like this one here 'Is Your Undersized Bra Causing You Harm?'"
    "Sasha keeps on staring at me, evidently enjoying watching me squirm and dig myself into a hole."
    hero.say "Well...not that the last one would be of interest to you..."
    show sasha wtf
    $ sasha.love -= 5
    sasha.say "WHAT THE HELL?!?"
    hero.say "Erm...I'm sorry?"
    sasha.say "What in the hell is that supposed to mean?!?"
    "For a moment I'm wrong-footed and lost for words."
    "I genuinely can't fathom what I've said to take Sasha from zero to fuming in so short of a time."
    "But then I glimpse her hands going instinctively towards her breasts, as if she's trying to cover them up or hide them from sight."
    "Suddenly it all makes sense, and I realise that Sasha's secretly quite insecure about her breast size."
    "And I just went and made a comment that could be taken as meaning I think her's are too small to ever have an undersized bra."
    "Hooray for me."
    hero.say "Sasha I'm..."
    sasha.say "Ah, shut up - just keep on wanking over women with fake tits as full of air as your big, dumb head and leave me out of it!"
    "With that, she storms out of the room and I can hear her stomping footsteps all the way to her room."
    "When the sound of the door slamming reaches my ear, I'm left alone with the magazine still clutched in my hand."
    "I wonder if I just put my foot in it because I'm dead tired."
    "Or if I could have been so blundering and insensitive after a good night's rest."
    "Either way, I just discovered one of Sasha's flashpoints in perhaps the worst way imaginable."
    hide sasha
    return

label sasha_init:
    python:
        sasha.set_flag("story",1)
    return

label kleioannafoursome:
    $ game.set_flag("bandharem",2)
    scene bg livingroom
    "Anna and Kleio eagerly agreed to come over to my place that evening, no doubt expecting to resume our group activities."
    "I couldn't share their enthusiasm, as I was already feeling my stomach churn at the prospect of telling them about Sasha."
    "Being involved with two girls was dizzying enough, but now I had to ask them to let another one into our already unusual relationship."
    show kleio date at right
    "Kleio arrived first, giving me a typically dirty and lingering kiss before throwing herself down on the sofa."
    show anna casual at left
    "Anna turned up a few minutes later, hugging me with her usual childish glee and then perching on the edge of the sofa beside Kleio."
    hero.say "Have you eaten, can I get you both a drink?"
    anna.say "Oh, erm...I didn't think you'd ask me that!"
    kleio.say "Maybe later - I'm hungry for something else right now!"
    hero.say "Oh, yeah, of course...me too."
    hero.say "I just thought it might be nice to chat for a bit before we...you know."
    hero.say "It can't all be about the sex, can it?"
    kleio.say "I don't see why not!"
    anna.say "I know - maybe we can talk dirty?"
    "I've begun to fiddle with my collar by now, probably looking like a picture of panic and evasion."
    kleio.say "Something's up with loverboy...come on, man - spill your guts."
    "I try not to stammer or trip over my words, aware that Sasha is waiting in her room to hear the outcome of my pitch on her behalf."
    hero.say "Well, the thing is...I was out for a drink with Sasha the other night."
    hero.say "And she, well...she kind of figured out what's going on between us all."
    "Anna's expression is one of incomprehension, and then shock."
    "Kleio surprises me by looking amused, rather than annoyed."
    kleio.say "You told her all about it?"
    hero.say "No, I swear - she thought we were spending time together without her because we were planning on kicking her out of the band."
    hero.say "When I told her we weren't, she's smart, so she guessed what it really was."
    kleio.say "So what - is she mad, jealous, or a bit of both?"
    anna.say "Ooh, if she is mad, I hope she's not too mad."
    "I try to steel myself as the moment of truth arrives."
    hero.say "She's definitely not mad, but you could say she's jealous."
    hero.say "She asked me to ask you...if she could make what we have into a foursome?"
    kleio.say "Does she now?!?"
    hero.say "Is that a yes, or a no?"
    kleio.say "I'm no prude, so it's a yes - if we can have a threesome, why not a foursome?"
    hero.say "What about you, Anna?"
    "Anna blushes, clearly intrigued by the idea and yet embarassed to be put on the spot."
    anna.say "I always had kind of a girl-crush on Sasha, so I say let's do it!"
    "Two votes of yes, and I guess I'd already said the same when I agreed to bring it up with Kleio and Anna, which makes it a clean sweep."
    scene bg secondfloor
    "I nod quickly, letting out a nervous sigh as I get up and start to walk towards the hallway and Sasha's bedroom door, perparing to deliver the news personally."
    "I have no idea why, but I try to make as little sound as possible as I creep towards Sasha's bedroom door and knock quietly."
    show kleio date at right
    show anna casual at left
    "Behind me, Kleio and Anna are making no such effort."
    "Kleio seems to be stalking after me like a cat hunting down a helpless bird with a broken wing."
    "And Anna can't keep from breaking out into what I suspect are nervous bouts of giggles at the prospect of what lies ahead."
    "I turn my head, intending to tell them to shut up, but a voice from the other side of the door stops me before I can speak."
    sasha.say "Who is it?"
    "I realise that she must have been sitting there in silence, just waiting to hear the outcome of my proposal to the other girls."
    hero.say "It's me...can I come in?"
    sasha.say "I guess so."
    scene bg bedroom3
    show sasha sleep
    "I make as serious a gesture for Kleio and Anna to keep quiet and wait in the hallway as I can manage, and then open the door to slip into Sasha's bedroom."
    "Sasha has the lights down low, save for a lamp by the bedside, and an open book beside it suggests she's been trying to distract herself without success."
    "But I soon forget those details, as she's sitting up on the bed, wearing only a vest and some shorts, a hopeful look on her face."
    "I should be saying something to her, but all I can do is stare at Sasha and think of what new possibilities she opens up for Kleio, Anna and myself."
    sasha.say "Well...what's the verdict?"
    hero.say "I asked them both, and...and..."
    "Before I can finish the sentence, I feel the door being rudely barged open from behind, pushing me further into the room."
    hide sasha
    show kleio date at left
    show anna casual at right
    "Kleio and Anna burst in, both giggling now and looking at Sasha in a manner that suggests they're thinking the exact same thing as me."
    kleio.say "We said YES!"
    "Anna and I both nod, hoping not to be left behind by Kleio's brash entrance."
    kleio.say "If we waited for loverboy here to tell you, we'd be cleaning cobwebs out of our clits before he got round to it!"
    anna.say "[hero.name] and I aren't as forward as Kleio, but we're both super excited to be letting you in on this, aren't we?"
    hero.say "Yeah...yeah, it's like being on a roller-coaster...you know, thrilling and a little scary, but in a good way."
    "All three of us have sat down on the bed and around Sasha by this point."
    "She smiles and tries to look confident, but she must feel like she's being initiated into some kind of wierd, kinky cult right now."
    hide kleio
    hide anna
    show sasha sleep
    sasha.say "So that's how you guys want it to be, eh?"
    sasha.say "You want to treat me like some kind of fairground ride that's for cheap thrills?"
    hide sasha
    show kleio date at left
    show anna casual at right
    kleio.say "Nah, you're the noob - so you get to ride us."
    hide kleio
    hide anna
    show sasha sleep
    "Sasha shows a little colour in her cheeks at Kleio's statement, obviously trying to picture what she has in mind."
    "I find that I can tune into what Kleio must be thinking, remembering that she, Anna and I are already used to indulging ourselves as a threesome."
    "If we want to bring Sasha into the fold, then perhaps we should take her by the hand and show her the way."
    hide sasha
    "Without asking permission, I reach over and pull Anna's tight t-shirt up and over her head."
    "Anna makes no effort to stop me, giggling even more as her large breasts are revealed."
    "Sasha reaches out tentatively with one hand, and Anna gently takes hold of her wrist, guiding her to cup one of her breasts."
    "At the same time, Anna moves closer, beginning to slide alongside Sasha, and slips one hand under her vest and the other into the waistband of her shorts."
    "Kleio chooses that moment to crawl into my lap, unzipping my flies, fingers stroking my dick."
    "She purrs in approval as I return the favour, lifting her skirt with one hand to caress her beneath her knickers as the other pulls off her top and spills her breasts."
    "We each undress the other as we explore each other's bodies, Kleio and I in one pair and Anna and Sasha and Anna the other."
    "Sasha's eyes are as much drawn to watching myself and Kleio as they are to Anna's attentions to her own body."
    "At one point we catch each other's gaze, and wonder if she's as amazed by the situation as I am."
    "Neither of us could have known, when she walked into my apartment or introduced me to her bandmates for the first time, that we would end up here."
    "It isn't long before everyone is undressed, four naked bodies coming together in the middle of the bed."
    "Sasha tries not to stare at my now very much hard and erect dick, but she can't help herself, and the others are not slow to notice either."
    kleio.say "Not a bad specimen, is it?"
    anna.say "I can personally recommend it, in either hole down there...very nice indeed!"
    "Sasha laughs nervously, not knowing what should happen next."
    kleio.say "Thing is, it's the only one we got."
    anna.say "So you have to be fair, you have to agree to share it."
    kleio.say "Yeah, Sasha - no hogging loverboy's dick!"
    "Sasha looks at me, probably wondering why I'm not a part of the conversation."
    kleio.say "But, you do get new-girl's privilege."
    anna.say "Yeah, you get to ride it as it's your first time!"
    "Part of me is pissed off that Kleio and Anna are talking about me like a piece of meat, despite all the talk of equality in the band."
    "But I have to admit that there's a real thrill to being used in this way, especially when they're debating who should get to have it inside of them."
    "I get no chance to speak before Anna starts pushing me down onto the bed, massaging my dick at the same time."
    "Together, she and Kleio push Sasha backwards, as she gets ever closer to my erection."
    show band foursome
    "Anna begins to help guide Sasha, who glances over her shoulder as she approaches."
    "It's only at this moment I realise that I'm in total control of just where my dick goes."
    "And in those few seconds, I put my hands on Sasha's hips and make my decision."
    menu:
        "Fuck Sasha's pussy":
            "I figure that, as it's Sasha's first time, I should keep things pretty traditional."
            "I pull her down slowly, so that my dick slides up and between the lips of her pussy."
            show band foursome pussy
            "Sasha's already quite slick, and so she can offer little resistance as she sits down on me."
            "Gravity makes her take the entire length until there's nothing left that's not inside of her."
            show band foursome pussy anna kleio
            "At the same time, Kleio is alternatively kissing one of her exposed nipples while squeezing and pinching the other."
            show band foursome pussy anna kleio lick
            "Anna busies herself by licking one moment at Sasha's lower lips, and then doing the same to the base of my shaft."
            "Sasha instinctively tries to shift her position, but she is being pleasured from three different angles at once."
            "Any attempt to move merely serves to intensify the sensations that are clearly coming close to overwhelming her."
        "Fuck Sasha's ass":
            "I might have been tempted to do Sasha in the traditional manner, but why be conservative in the middle of a foursome?"
            show band foursome ass
            "I angle Sasha forward a little, and push my dick between her buttocks and into her unsuspecting ass."
            "Sasha yelps in surprise as she sinks down on my dick, feeling it probe her ass."
            show band foursome pussy anna lick
            "But then she moans long and loudly as Anna's tongue begins to explore the folds of her pussy."
            show band foursome pussy anna kleio lick
            "Kleio soon joins in, kissing, nibbling and squeezing Anna's stiffened nipples without pause."
            "I can't honestly think of any more that we could be doing to stimulate Anna at that moment in time."
            "And she soon rises towards her climax, body twitching and flinching as the three of us play her like she was one of our instruments."
        "Fuck Anna's mouth":
            "I don't know what makes me go against the flow, maybe the closeness of Anna's heavy breasts and plump lips."
            "But whatever the reason, I decide to throw a curve-ball at Sasha, and reach around to sieze Anna's head."
            show band foursome mouth anna
            "At the same time, I push my groin upwards so that my dick slips into her mouth, just as she opens it to ask what I'm doing."
            "Not needing any more explanation, Anna begins to slide her tongue around my shaft, expertly exciting me with each and every movement."
            show band foursome mouth anna kleio
            "Sasha looks disappointed, but her attention is soon diverted when Kleio begins to kiss and lick at her now stiffening nipples."
            "With my hands free, I reach down and stroke Sasha's pussy until I can work my fingers inside of her."
            "Soon Sasha seems to have forgotten the fact that I denied her my dick, and is siging more loudly with each moment that passes."
            "As she arches her back and prepares to climax, I realise she's not the only one about to cum."
    "I have perhaps five seconds to decide where exactly I want to be before I lose it."
    menu:
        "Cum in Sasha's pussy":
            "Determined to make Sasha the centre of attention during her first time together with us, I push as deep into her as I can."
            show band foursome pussy anna kleio lick cum
            "When I can't hold on any longer, I let go and feel the sensation of my own climax pushing her over the edge."
            "Sasha cries out and stiffens, as while My motions have stopped, Kleio and Anna show no signs of doing the same."
            "Still riding me and being held up by the other two girls, she remains suspended upright, feeling the full effects without release."
        "Cum in Sasha's ass":
            "Kleio's playing with her nipples and Anna licking at her pussy seems to be enough to finally bring Sasha to an orgasm."
            show band foursome ass anna kleio lick cum
            "As I feel the sensation rippling through her taught body, she sets me off as well, my dick getting every twinge and tick while up her ass."
            "Adding the sudden pressure of me cuming inside of her makes Sasha arch her back and cry out with unexpected volume."
            "I watch as she takes every single moment of the climax, impaled on my dick and trapped where she sits."
        "Cum in Anna's mouth":
            "With my fingers inside of Sasha and my dick in Anna's mouth, I can't tell which one of us starts to cum first."
            show band foursome mouth anna kleio lick cum
            "But once the ripples of an orgasm start to spread, it pushes us both over the edge."
            "Seconds later I feel the release while my dick is still surrounded by the soft warmth of Anna's mouth."
            "Luckily, she's ready for it, and keeps from choking as she gasps and swallows, which only adds to me own sensations of pleasure."






    hide band foursome
    "Though only Sasha and myself have actually cum, everyone sags onto the bed, like a troupe of puppets who's strings had been suddenly severed."
    "No one speaks, but we can all feel that something pretty amazing and life-changing has just happened to us all."
    "Not only are we all bandmates, we're all lovers now as well."
    return

label sasha_threesome_confrontation:
    show sasha
    hero.say "I'm not psychic, Sasha, but it feels like something's bugging you."
    sasha.say "What - no, I just wanted to talk, that's all."
    "My heckles are immediately up at this, but I try to play innocent."
    hero.say "Talk about what, exactly?"
    sasha.say "Oh, just stuff in general...I feel like we somehow talk less, even though you're in the band now."
    sasha.say "Wierd, yeah?"
    "I nod, noticing that she's already the one doing most of the talking."
    sasha.say "You guys were on fire tonight, by the way."
    hero.say "Thanks, Sasha - you were great too."
    sasha.say "Nah, I was a mess."
    sasha.say "But you, Anna and Kleio - I don't know, it's kinda like you've just clicked, all three of you all of a sudden."
    "I try to look like I'm smiling at the compliment, but I'm already worried Sasha has figured out that Kleio, Anna and I are now a threesome."
    sasha.say "Look, we're supposed to be a band, a four-piece, and I think we can be honest with each other - don't you?"
    "I nod, preparing myself for the worst."
    show sasha sad
    sasha.say "Just tell me - have the three of you been practising behind my back?"
    sasha.say "Are you gonna kick me out of the band, or just all quit and reform without me?"
    "The look of surprise and then relief on my face must be plain to see."
    "Sasha reads instantly that I'm taken aback by the idea."
    "But she's no fool, and soon senses that there's something else behind my reaction."
    show sasha normal
    sasha.say "Wait a minute...it's not that you want rid of me - but there's something going on here, isn't there?"
    "I start trying to speak, but Sasha cuts me off."
    sasha.say "I got suspicious when you all showed up within neat little five minute intervals."
    sasha.say "Normally Kleio's early, Anna's late and we go to the practise room together."
    "I can almost see the wheels and cogs turning in Sasha's brain as she works it out for herself."
    sasha.say "If you're all into something together, something that's making you so in tune with each other, something you're not telling me about..."
    "And there it is, I see the moment her face registers what's going on between Kleio, Anna and myself."
    hero.say "I don't know what to tell you, Sasha."
    hero.say "It just kind of happened - no one's more surprised than me!"
    if sasha.love <= 150 and sasha.get_flag_value("lesbian") <= 10:
        show sasha wtf
        "Sasha wrinkles her features as though she's smelled something nasty."
        sasha.say "Eww...all three of you, together, at once?!?"
        hero.say "It didn't start out that way, honestly!"
        hero.say "I was seeing them seperately and they kinda found out about each other."
        sasha.say "And that makes it better how?"
        "I realise how bad that explanation sounds only after I've said it."
        sasha.say "Jesus, why am I exploding all over you when you're all in it together and loving the whole thing?"
        hero.say "I'm sorry, for what it's worth."
        hero.say "I couldn't help falling for two women that wanted me...I thought you were different enough to be okay with something like that."
        sasha.say "Huh...maybe I'm more traditional than either of us thought."
        $ sasha_love_max = 0
        $ sasha.set_flag("nodate")
        $ sasha.set_flag("nokiss")
        $ sasha.set_flag("nosex")
    elif sasha.love <= 150 or sasha.get_flag_value("lesbian") <= 10:
        "Sasha shakes her head and whistles in what I take to be a show of grudging admiration."
        sasha.say "Well, aren't we the dark horse?"
        hero.say "It really didn't happen like that!"
        sasha.say "No, I suppose you all just tripped and fell into bed together while you were naked?"
        hero.say "More like I was kind of seeing them both and they found out."
        sasha.say "You're lucky they wanted to share their toys!"
        hero.say "Look, I'm sorry no one told you, Sasha."
        sasha.say "Hey, you're telling me now, aren't you?"
        "Sasha gives me a knowing wink."
        sasha.say "Just don't leave me to jump to the wrong conclusion next time you've got a juciy secret like that!"
    else:
        show sasha blush
        "Sasha looks awkward, blushing and struggling to look me in the eye."
        hero.say "Shit, Sasha...I'm sorry if I've shocked you or pissed you off with all of this."
        sasha.say "No...no, it's nothing like that."
        "I'm struggling to guess what Sasha means, when she puts her hands on mine atop the table."
        sasha.say "This is tough for me to admit, but I've always had kind of a crush on Kleio and Anna...and you too, if I'm honest."
        hero.say "It's not wierd, Sasha - a lot of people think their friends are pretty cute, and we're all really close because of the band."
        sasha.say "Okay, I'll spell it out for you - I feel like I'm missing out on something fun, and I want in!"
        "My mouth moves, but no words come out."
        sasha.say "That's a pretty good impression of a goldfish, but it doesn't give me an answer."
        hero.say "Sasha...I'm already reeling from being in a relationship with two women, let alone three!"
        sasha.say "Can't be that big of a leap, from a threesome to a foursome, surely?"
        hero.say "Well, when you put it like that..."
        sasha.say "Look, I'm just asking - maybe put in a good word for me, huh?"
        "I nod, trying to keep the thoughts of what possibilities this promises off my mind for the moment."
        $ sasha.set_flag("kleioannafoursome",True)
    "We finish our beers and leave in silence."
    "Both of us are too preoccupied with the ramifications of all that's just come out to be able to talk."
    "Whatever happens from here on in, it's sure to change somethings forever."
    return

label sasha_scottie_talk:
    show sasha
    "I can tell that something's bugging Sasha the moment that I see her."
    "She looks preoccupied and isn't really paying attention to anything or anyone around her."
    "I could just leave it alone, as whatever's bothering her is probably none of my business and she's not volunteering any information either."
    "But I get the irresistible urge to play the part of the understanding housemate, and I hope, maybe even friend."
    "And right now, it seems to me that Sasha could probably do with a sympathetic ear for her problems."
    hero.say "Penny for your thoughts, Sasha?"
    sasha.say "Huh...what was that, [hero.name]?"
    hero.say "I just thought that you looked like you had a something on your mind."
    hero.say "If you want to talk about it, I'm all ears..."
    "Sasha smiles at me in a way that makes me wonder if I want to limit my ambitions to being just a friend after all."
    sasha.say "That's sweet, [hero.name], thanks for the offer."
    sasha.say "Normally, I'd say no...but it's got to do with guy problems."
    sasha.say "So maybe you could give me some advice from the other side of the gender divide?"
    "Guy problems?"
    "Is this a chance to get a glimpse into Sasha's personal life?"
    hero.say "Sure, Sasha...if you think that'd help."
    "She smiles, the gratitude clear to see in her eyes, and puts a hand atop mine."
    sasha.say "Thanks, [hero.name] - you're a real friend to me."
    sasha.say "Most guys are only interested in getting into my knickers, but you're one of the good ones."
    "I almost blush at the fact that I was thinking about that very thing only a couple of seconds beforehand."
    hero.say "Anyway, you were going to tell me all about this problem that you have with a guy?"
    "What a smooth recovery!"
    sasha.say "Yeah, of course."
    sasha.say "Well, it's kind of one of those situations where you date someone for a while, and it's pretty okay."
    sasha.say "But then you break up for whatever reason, and you forget about all of the stuff that bugged you about them."
    "Sasha looks at me to check that I'm still following her, and I nod for her to continue."
    sasha.say "And then, when they inevitably call you up out of the blue, you're torn."
    sasha.say "Because all you can really remember is the good stuff, but you know that there was enough bad stuff to end it the first time."
    sasha.say "You know what I mean?"
    "Not really, as I don't have a string of former girlfriends calling me up all the time, trying to win me back!"
    "But I nod anyway, just to keep the conversation going and for the sake of feeling useful."
    hero.say "Sounds like there's more to it than that, Sasha."
    hero.say "Who is this guy, and what is it about him that's got you so tied up in a knot?"
    "Sasha sighs and nods her head, before she going on."
    sasha.say "His name's Scottie, and he's not as bad as all that."
    "Even with those few words on the subject, I instantly come to the conclusion that, in reality, he's probably much worse than all that."
    sasha.say "I mean, he could be really sweet when he was in the mood."
    sasha.say "And that body..."
    "At that, Sasha seems to stare into space for a moment, as if the image it summons from her memory is just that impressive."
    hero.say "Ahem...maybe if we try to focus on the negatives that you mentioned, rather than the positives, Sasha?"
    hero.say "Like...what was the actual reason that you broke up with this Scottie?"
    "Sasha shakes her head, which seems to bring her back to reality, and then shrugs."
    sasha.say "I don't know...I guess he was just such an insensitive meat-head at times, you know - thick as fuck."
    "This guy sounds like a text-book case - a million dollar body and a ten cent brain."
    sasha.say "So, as a guy, what do you think I should do?"
    menu:
        "You should give him a second chance":
            $ sasha.love += 5
            "I could just dump on the guy, tell Sasha that he sounds like a complete asshole - which he kind of does."
            "But would that really make me any better than him in the long run?"
            "I mean, at least some of my motivation for trying to turn Sasha off the idea would be on account of my own jealousy."
            hero.say "I don't think you'd be even considering taking this guy back if you didn't like his good points more than his bad ones."
            "Sasha nods at this, her face taking on a thoughtful look as she ponders my reasoning."
            sasha.say "Huh, I suppose you're right!"
            sasha.say "Maybe he's realised what bugged me when we were together and wants to tell me he's really changed?"
            "I think it's more likely that he's sprouted a second head in the time they were apart."
            "But I nod all the same."
            sasha.say "And if not, I can always work really hard on changing him myself!"
            "I have to try real hard to keep from rolling my eyes and groaning at that old cliche."
            hero.say "Stranger things have happened..."
            "Sasha seems pleased with the way the conversations gone, relaxing noticeably for the first time since the subject came up."
            "Whatever kind of disaster this whole thing turns into, I think I deserve a ton of karma for the way I just handled it!"
        "Don't bother with the dude":
            $ sasha.sub += 5
            "Jesus - this guy sounds like a bloody pain in the arse!"
            "I may be jealous of someone else having a chance with a girl as cute as Sasha."
            "But the way I see it, if she starts seeing this wanker again, then he'll be hanging around here all the time too."
            "So I'm not just against this for Sasha's sake, but for mine and Bree's as well!"
            hero.say "It's really great of you to think of giving this Scottie another chance, Sasha."
            hero.say "But he sounds to me like one of those guys that never really changes."
            "Sasha looks at me a little quizzically, as if not too sure of my sweeping statement."
            sasha.say "Really, becasue he sounded so sincere when we last spoke?"
            sasha.say "I was so sure of what he said that I was teetering towards taking him back."
            "I shake my head and give her hand a little squeeze, just enough to reassure her of my sincerity."
            hero.say "Sasha, I think you can trust my judgement on this kind of thing."
            hero.say "The only motivation I have for saying this is my own experience and the fact that we're friends."
            hero.say "If you've been hurt by this guy in the past, then the healthiest thing would be to make a clean break of it."
            hero.say "Try seeing someone new, or don't..."
            "Wait a minute, that sounds even better!"
            hero.say "You know, a stint of celibacy might be just what the doctor ordered..."
            "And all the while, I can be working on my chances of getting in there myself!"
            "Sasha nods at this, looking as though she's becoming more open to the idea the more she thinks about it."
    "With that issue addressed, the conversation returns to more normal and neutral subjects."
    "I find myself hoping that I've made the right decision in terms of my advice to Sasha."
    "But I can still feel the shadow of this Scottie guy hanging over me, like an oppressive presence lurking in my immediate future."
    $ sasha.set_flag("scottieDelay", True, 7)
    return

label scottie_appears:
    scene bg livingroom
    "I’m about to open the door when a knock on the other side of it startles me to a halt."
    "Actually, ‘knock’ is too passive -- someone’s pounding on the door with their fist, impatient and demanding."
    "I draw my hand back from the doorknob, frowning. Who could that possibly be?"
    scottie_say "Open up! Hey! I know you’re in there, you black-hearted bitch!"
    "Oh. That’s… not for me."
    "I hear a groan from somewhere down the hallway, and then footsteps as the ‘bitch’ herself makes her way to the living room, propping her hands on her hips."
    show sasha
    sasha.say "That’s mine, I guess."
    "I give a nervous sort of chuckle and step aside, giving a sweeping gesture to the door that tells her: it’s all yours."
    "But she doesn’t seem to think that’s how this goes, giving her head a short shake before folding her arms and tilting her head toward the door."
    sasha.say "Nuh uh. You answer it. I need a meat shield so his dumb ass doesn’t try to barge inside."
    "I don’t think I signed up for this. But it feels a little too pathetic, suddenly, to decline her while she’s got those dark eyes locked on me like that."
    "If my masculinity is at stake, I guess I’ll play the hero."
    scene bg house
    show scottie teaser
    "The door hasn’t stopped rattling in its frame under the assault for the duration of our brief exchange, and I make my way over to it and flip open the lock, pulling it ajar."
    "Seemingly surprised by this, the beefhead on the other side knocks the suddenly open air once before clearing his throat and composing himself, puffing himself up and setting a hateful scowl onto his face."
    scottie_say "Who the hell’s this doofus? Where’s Sasha?"
    scene bg livingroom
    show sasha
    sasha.say "I’m right here, genius..."
    "Sasha speaks from behind me, sounding exasperated already."
    sasha.say "How the hell’d you get this address?"
    hide sasha
    show scottie teaser
    scottie_say "I have my ways."
    "The bulky blonde in front of me answers, trying to sound gruff and mysterious, I’m sure."
    "I get the impression that he just stalked her social media, though, and it’s not that deep."
    "I hear Sasha scoff behind me and step forward, stopping just behind my shoulder to address our uninvited guest."
    hide scottie teaser
    show sasha
    sasha.say "Cry about whatever you came to cry about, then, and piss off."
    "The dude’s face screws up a little more, and for a second I think he is about to cry."
    "But then he puffs up a little bit more instead, seeming to regain himself, and turns up his volume instead."
    hide sasha
    show scottie teaser
    scottie_say "I want answers, you cheating whore!"
    "Sasha sighs, as though this song and dance isn’t new."
    hide scottie teaser
    show sasha
    sasha.say "I didn’t cheat on you, Scottie."
    hide sasha
    show scottie teaser
    scottie_say "Yeah, right! Why else would you have left something like this?"
    "He flexes stupidly in front of our doorway, and I have to bite my tongue to stifle a laugh. What an embarrassment."
    "I turn a bit to glance back at Sasha, who’s pinching the bridge of her nose."
    "She must be thinking the exact thing I’m thinking: how the hell did she ever date someone like this?"
    hide scottie teaser
    show sasha
    sasha.say "Maybe because you’re the kind of jackass who comes pounding on my door uninvited."
    "He seems to completely miss this, or just not care. His eyes are fixed on me now, sizing me up."
    hide sasha
    show scottie teaser
    scottie_say "Who’s this wimpunk? Huh? This what you’re bangin’ now? Your standards are low, Sasha."
    "She only grunts out a sound of exasperated disgust behind me, and I see her shift her weight and fold her arms from my peripheral."
    "Maybe she’s tired of communicating with him already, but a beat of silence falls between them that’s a little too long. It feels like my job to fill it."
    menu:
        "Not as low as they were.":
            $ sasha.love += 2
            "I straighten myself and turn back to face ‘Scottie’ fully, my expression smug."
            hero.say "It’d be hard to downgrade from someone like you."
            "Scottie tenses up and clenches his jaw, and I feel like I can almost see him physically boiling like some old cartoon."
            scottie_say "Big talk for someone your size, punk! Take it outside and I’ll grind you into the pavement!"
            sasha.say "Alright, Scott, knock it off,"
            "Sasha snaps, seemingly losing her already thin patience."
            sasha.say "Get out of here before I call your mom and tell her you’re still picking fights."
            "This time I don’t hide my amusement, snickering openly at the idea that she was going to call his mommy like a middle schooler, and even more so at how quickly he seems to cower from the idea."
            scottie_say "That’s low, Sash."
            "His voice is a wounded mumble, now, a dog scolded."
            scottie_say "We had something special."
            sasha.say "It’s hard to believe that’s even true."
            "He looks even more hurt by this, and I think if he didn’t storm up acting like such a dick I’d almost feel bad about how he turns away, drooping as he makes his way back down the hall."
        "You’re right. Sasha’s a goddess." if sasha.love >= 50:
            $ sasha.sub -= 5
            "I pull a crooked smile and lean an elbow against the doorframe, making sure ‘Scottie’ has a good view of the babe standing behind me, in my apartment, on my side of the door."
            hero.say "She’s out of my league,"
            "I speak cooly, buttering her up as much as I’m taunting this meathead."
            hero.say "but I’d say my chances are still pretty good, if she ever settled for a monkey like you."
            "Sasha gives a sort of soft chuckle behind me, and Scottie goes red in the face, tensing up like he’s about to burst in front of me like a balloon."
            scottie_say "Say that to my face!"
            "Sasha sighs."
            sasha.say "He just did."
            scottie_say "Yeah, w-well--!"
            "Scottie stammers a bit, then clenches his beefy hands into fists, and I think, for a moment, he’s planning on pummeling me in the doorway."
            "But Sasha steps back in before he can, stepping forward until she’s nearly beside me and speaking in a low and serious tone."
            sasha.say "Enough, Scott. Get out of here before I call the cops."
            "He seems to teeter a moment on the idea of risking it to punch my teeth out, then deflates with a heavy, childish sigh, spinning back sharply and stomping his way down the hallway."
            scottie_say "This isn’t over, you piss-soaked ramen noodle! You better hope I never catch you on the street!"
            "Though he’s not the sharpest pencil in the box, I kind of do hope he never does. I could probably talk circles around him, but I don’t know what he can do with those muscles if he goes into some kind of toddler hissy fit."
            "I guess I just hope I never bump into him in a back alley or something."
        "She’ll be mine soon enough." if sasha.love >= 50:
            $ sasha.sub += 5
            "I let a cocky smirk cross my face and lean myself against the doorframe, making sure ‘Scottie’ has a clear view of his ex behind me while I speak."
            hero.say "Let it go, beefcake. She’s in much better hands now."
            "Scottie sets his jaw, and I see his shoulders tense up, like he’s ready to start swinging."
            scottie_say "What, yours? You probably couldn’t lift her if she was begging for it!"
            hero.say "I guess I’ll just have to test that out later."
            "Scottie starts going red in the face, almost visibly broiling, like some old-timey cartoon."
            scottie_say "Like hell you will!"
            sasha.say "Alright."
            "Sasha raises her voice over both of us, stepping forward until she’s almost beside me and giving me a slight shove on my shoulder, as if to say I’m being just as bad."
            sasha.say "Both of you knock it off."
            scottie_say "Fight me for her, then, pipsqueak!"
            "Scottie nearly roars, disregarding her and clenching his big hands into fists."
            scottie_say "We’ll see who’s hands are better… hands!"
            sasha.say "Scottie!"
            "This time her voice is a sharp bark, and like an obedient dog he deflates a little under the sound. It must be a tone he’s learned means he’s crossed a line."
            sasha.say "I said that’s enough! Get out of here before I call your mother again."
            "I laugh openly at how he cowers from this threat, and the implication that it’s come to that before. He seems to unwind, his taut muscles relaxing as he steps back from the door."
            scottie_say "Come on, Sash… that’s not fair."
            "Sasha jabbed a finger down the hallway, her own jaw set."
            "Sighing, defeated, Scottie obeyed… but not without shooting me a death glance over his shoulder, that said: this isn’t over yet."
            "That’s fine. If it comes down to proving I can pin Sasha back against the wall and have my way with her any day, I’ll fight any fights I need to."
    "She gave another exhausted, exasperated groan from behind me, and I stepped back from the doorway, allowing her to close it quietly behind me."
    sasha.say "Sorry about that…"
    hero.say "An ex, I take it?"
    "She rolls her eyes and folds her arms beneath her breasts, shaking her head slightly in disapproval."
    sasha.say "Unfortunately."
    "I can’t help but snort an amused laugh, quirking a brow."
    hero.say "I wouldn’t have pegged him as your type."
    sasha.say "Yeah, well."
    "She steps by me, a mysterious, catlike glimmer flashing in her eyes as she pass."
    sasha.say "Maybe you’d be surprised by what I’m into."
    "Ooh."
    "Something thrills through me as she purrs these words and moves past me back to her bedroom, and I turn and let my gaze follow her as she does."
    "My eyes linger, shamelessly, on the pert motion beneath her cutoff shorts before I draw in a deep breath and turn back away, a helpless smile crossing my face from ear to ear."
    $ sasha.set_flag("scottieDelay", True, 7)
    return

label sasha_practice_01:
    "With the battle of the bands getting closer every day, we were practicing in every moment of free time that we had."
    "I thought we were sounding better than ever, but Sasha and Kleio seemed to be getting more frustrated with the smallest of details."
    "Anna and I tried to keep out of their frequent outbursts of emotion, but occasionally they were too much to ignore."
    show sasha angry
    sasha.say "FUCK...FUCK...FUCK!"
    show kleio angry
    kleio.say "Jeez, hold it together, Sasha!"
    show anna
    anna.say "Wow...Sasha, are you okay?"
    show sasha
    sasha.say "I just can't get this chord out of my head and onto the damn bass."
    sasha.say "I feel like I've got flaccid dicks for fingers!"
    "I offer Sasha an understanding smile while trying to keep such a weird mental image out of my mind."
    "She sees the gesture and smiles back, seeming to get more reassurance from my silent show of support than the words of the other girls."
    sasha.say "Let's have a break...I'm just gonna have some me time in the bathroom."
    "The other girls nod as we all set down our instruments, but as she passes me, Sasha beckons me with a finger."
    hide sasha
    "It's clear that she wants me to follow her into the bathroom for some reason."
    "But I'm not sure if I should follow on her heels, or give it a few seconds to keep from drawing Kleio and Anna's attention."
    hide kleio
    hide anna
    menu:
        "Follow Sasha immediately":
            "I arrive in the small bathroom almost literally right behind Sasha."
            "She turns and smiles broadly at the sight of me, clearly delighted that I read her so well."
            hero.say "Hey, Sasha - are you okay?"
            sasha.say "Yeah, just tense as hell...like we all are."
            sasha.say "I need to let off some steam - and let's just say I didn't mention dicks back there by accident, either!"
            $ sasha.love += 5
        "Follow Sasha after a minute":
            "I give it about a minute, then follow Sasha into the bathroom."
            "She looks over her shoulder at me, her mood improving at seeing me turn up."
            hero.say "Just wanted to see if you were doing okay?"
            sasha.say "Better than I was...I thought you weren't going to come see me for a moment."
            hero.say "Sorry...I just thought you'd appreciate a few seconds alone, after being cooped up with all of us for so long."
            sasha.say "Trust me, it's different when it's just the two of us."
        "Follow Sasha after five minutes":
            $ sasha.love -= 5
            "I wait a full five minutes, checking the time before I follow Sasha into the bathroom."
            "She's sitting cross-legged on the toilet, arms folded over her chest and looking pretty annoyed."
            hero.say "Are you feeling any calmer, Sasha?"
            sasha.say "Nope, but at least now I'm pissed for sitting here on my own in a damn bathroom for ages, so that's a change at least!"
            hero.say "Wait a minute...you wanted me to come quicker?"
            hero.say "Geez, sorry...guess I misread the situation."
            sasha.say "Yeah - same here!"
    "She stretches and lets out a long breath, which means getting even closer to me in the small space of the bathroom."
    sasha.say "Help me out here - teach me some way to squeeze a little of the stress out of me?"
    "Sasha's so close now that I can see the tension in her muscles, the tightness of the dog-collar that she wears around her neck, and her breathing is all I can hear."
    menu:
        "Tighten the dog collar round Sasha's neck":
            "Without speaking, I turn Sasha around and take hold of the leather collar she's wearing."
            "She gasps in surprise, but thanks to her delight in such things, doesn't object in the slightest."
            "I tighten it slowly and gently, allowing her to feel the gradual progression of its grip on her neck."
            "Sasha gasps, instinctively pressing herself against me, so that her ass is nestled in my lap."
            "I don't keep it up for too long, just enough time for her to lose herself, and then I loosen my grip once more."
            $ sasha.sub += 5
        "Massage Sasha's tense muscles":
            hero.say "You're wound up tighter than the strings on your own Bass!"
            "I begin to knead and massage the muscles of Sasha's shoulders, not being at all gentle with the knots and kinks that I find."
            "She makes no effort to protest, and pretty soon her expression begins mellow as she lets herself feel the benefit."
            sasha.say "Don't we have magic hands...now do the back as well."
            "She turns to allow me to massage her back, but surprises me by stripping off her t-shirt as she does so."
            "Before I can begin, her hands caputure mine and guide them to her petite breasts."
            "Too turned on to argue, I massage them instead, enjoying the sensation of her nipples as they stiffen under my touch."
            $ sasha.sub -= 5
        "Teach Sasha a breathing exercise":
            hero.say "I got sent on a stress-relief course by work last year, they taught me a breathing exercise that always works."
            "I talk Sasha through the exercise, trying to ignore the fact that she's almost looking daggers at me the whole time."
            "I guess she was hoping for something a little more tactile and impactful, but she grits her teeth and copies my actions."
            "After a couple of minutes pass, she's actually visibly calmer than before."
            sasha.say "I guess you were right...that has helped calm me down."
            $ sasha.love += 5
    sasha.say "Thanks for that...it seems to have done the trick."
    hero.say "Happy to be of help."
    "We walk back into the practice room, neither of us wanting to admit to what just happened in the bathroom, but its implications already running through our minds."
    "Kleio and Anna try to look nonchalant and disinterested, but they both clearly want to know why we just spent so long in there together."
    sasha.say "What are we waiting for, the start of the next fucking ice age?"
    sasha.say "Let's get back to it, people!"
    hide sasha
    return

label massage_book:
    "I read about massages in Sasha's book."
    $ game.pass_time(2)
    if not "massage" in hero.skills:
        $ hero.skills.append("massage")
    return

label sasha_give:
    if not "Massage book" in hero.inventory.keys() and sasha.sub <= 25 and not "massage" in hero.skills:
        $ gift = Consumable("Massage book", money_cost = 1000, label = ["massage_book"])
        "She hands me a pretty large book."
        hero.say "Wow !\nIs that a book about massages?"
        sasha.say "It sure is..."
        hero.say "Thank you so much."
    elif not "dildo" in hero.inventory.keys() and sasha.love >= 50:
        $ gift = Item("dildo",money_cost = 200)
        "She hands me a small box."
        hero.say "A dildo?"
        sasha.say "I am pretty sure you know how to use it."
        hero.say "Thank you I guess."
    elif not "anal beads" in hero.inventory.keys() and sasha.sub >= 25 and sasha.love >= 25:
        $ gift = Item("anal beads",money_cost = 200)
        "She hands me a small box."
        hero.say "Anal beads?"
        sasha.say "It goes in the butt, if you wonder."
        hero.say "Thank you I guess."
    elif not "handcuffs" in hero.inventory.keys() and sasha.sub >= 25:
        $ gift = Item("handcuffs",money_cost = 200)
        "She hands me a small box."
        hero.say "Handcuffs?"
        sasha.say "So you can play cops."
        hero.say "Thank you I guess."
    elif not "bondage ropes" in hero.inventory.keys() and sasha.sub >= 50:
        $ gift = Item("bondage ropes",money_cost = 200)
        "She hands me a small box."
        hero.say "Ropes?"
        sasha.say "They are made to tie up girls, willing ones preferably."
        hero.say "Thank you I guess."
    else:
        $ gift = Consumable("cake", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
        "She hands me box, obviously from a pastry shop."
        hero.say "Thanks."
    $ hero.gain_item(gift)
    return

label sasha_give_valentine:
    show sasha
    "Sasha walks confidently towards me."
    call sasha_greet from _call_sasha_greet_3
    show sasha blush
    sasha.say "Happy valentine's day [hero.name]..."
    call sasha_give from _call_sasha_give
    return

label sasha_give_birthday:
    show sasha
    "Sasha walks towards me."
    call sasha_greet from _call_sasha_greet_4
    show sasha happy
    sasha.say "Happy birthday [hero.name]!"
    call sasha_give from _call_sasha_give_2
    return

label sasha_give_christmas:
    show sasha
    "Sasha walks towards me."
    call sasha_greet from _call_sasha_greet_6
    show sasha happy
    sasha.say "Merry christmas [hero.name]."
    call sasha_give from _call_sasha_give_1
    return

label sasha_get_out:
    if game.from_room != "bathroom":
        show sasha angry
        $ sasha.set_flag("greeting",True,1)
        if sasha.activity["clothes"] == "underwear":
            sasha.say "Please can you step out ?"
        else:
            sasha.say "I am naked. Please can you step out ?"
        $ sasha.set_flag("peeping_tom",1, "day", mod ="+")
        $ peep = sasha.get_flag_value("peeping_tom")
        $ sasha.love -= peep
        hide sasha
    else:
        "I hear a voice through the door."
        if game.room == "bathroom":
            if hero.check_skill("hung"):
                $ sasha.love += 1
            sasha.say "[hero.name] I need the bathroom, get out."
        else:
            sasha.say "[hero.name], get out."
        hero.say "Sure."
    $ game.room = "secondfloor"
    return

label sasha_not_get_out:
    $ sasha.set_flag("greeting",True,1)
    show sasha
    "Sasha is naked..."
    hero.say "Sorry, Sasha I didn't know you would be here."
    sasha.say "You know..., I don't mind if you come in..."
    hide sasha
    return

label sasha_not_get_out_2:
    $ sasha.set_flag("greeting",True,1)
    show sasha
    if sasha.get_clothes() == "underwear":
        "Sasha is in her undies..."
    else:
        "Sasha is only wearing a towel..."
    hero.say "Sorry, Sasha I didn't know you would be here."
    sasha.say "Stop it, we know each other well enough not to be bothered by that..."
    hide sasha
    return

label sasha_band_event_02:
    $ game.set_flag("performance",2)
    show anna teaser normal
    "As I nurse my drink at the bar, smiling softly at the people as they slowly fill up the venue, I’m suddenly startled by a small, pink-haired woman, smiling broadly as she comes up to me."
    if hero.charm >= 25:
        "I look down at this small, pixie-like woman, trying to contain my laughter."
        hero.say "Hey there, little fairy. Did you get lost on the way to pixie hollow?"
        "The woman seems unfazed by my joke, simply shaking her head."
        anna_say "Sasha said you’d be an asshole."
        anna_say "Come on—she sent me to get you."
        anna_say "Apparently we’re in need of your ‘big strong arms.’ Looking at you now, though, I don’t really know what she was talking about."
        "Hiding a grin, I realize this small woman has just as much power to dish it out as she does to take it."
        "Sticking out my hand, I offer it to her to shake."
        hero.say "I’ll come, don’t worry. But, first—what’s your name?"
        "She smiles up at me as I get to my feet, anxious to return me to Sasha."
        anna_say "I’m Anna. Nice to meet you."
    else:
        "This woman, although small, immediately captivates my attention."
        "She’s absolutely beautiful—built like a model, with curves for miles—and her breasts, despite her small frame, are huge."
        "I don’t even attempt to hide my staring, unable to break my gaze until she finally speaks to me."
        anna_say "Uh, hi. Are you [hero.name]?"
        "My heart flutters in my chest as I realize, somehow, that this small sexy woman already knows my name."
        hero.say "Yeah, I am. What’s up?"
        show anna teaser happy
        anna_say "Sasha sent me to come get you. And, boy, am I glad she did. I’m Anna, and it is so, so nice to meet you."
        "Realizing her eyes were raking me up and down as much as mine were hers, I almost seem to drift to my feet beside her, not asking any more questions than I need to."
    show anna teaser normal
    "Before I get a chance to say anything more, Anna begins to lead me towards the back of the bar, to the service door."
    "With a slight wink at the security guard, she gestures me inside."
    "The brightly lit hallway is a direct contrast to the dark mood lighting of the bar, and I find myself reaching for Anna to guide me as my eyes adjust."
    "She does so happily, her fingers sliding and playing with mine as she weaves me through the small hallways to where the band is setting up."
    "My eyes have just adjusted to the light when I finally see Sasha, a wave of relief crashing over her as soon as she sees me."
    hide anna
    show sasha casual2
    sasha.say "Oh, thank God, you found him. Thank you, Anna."
    hide sasha
    show anna teaser normal
    "Anna grins up at me, refusing to leave my side."
    anna_say "No, no, thank YOU, Sasha. [hero.name] is awesome."
    "She looks up at me again, fluttering her long, beautiful eyelashes, and I feel my knees get weak."
    hide anna
    show sasha casual2
    "Sasha notices Anna’s flirting, and unceremoniously pushes her aside to the other woman in the room."
    hide sasha
    show kleio teaser annoyed
    "She’s looks much more stoic, and appears much more annoyed with my presence."
    kleio_say "This is ridiculous, Sasha—we don’t need him to do this."
    kleio_say "We are more than capable on our own, or, worst comes to worst, we can borrow some security guards."
    kleio_say "Why do we need your friend back her."
    hide kleio
    show sasha casual2
    "Sasha shakes her head, completely disregarding her bandmate’s words."
    sasha.say "Ignore her, please. That’s Kleio, and she’s a big believer in woman’s rights."
    sasha.say "I am too, but I’m also a realist, and I realize, unlike some people, that were are incapable of lifting our two huge amps out onto the stage on our own."
    sasha.say "Even if we were, we don’t need to risk breaking bones right before a show."
    "Kleio rolls her eyes, scoffing at Sasha’s words, but says nothing more, clearly realizing that this is an argument not worth fighting."
    sasha.say "So, [hero.name] I know it’s a lot to ask, but could you help us? We’d really appreciate it."
    menu:
        "Sure":
            hero.say "Uh, I mean, yeah, of course I can try. I don’t know how much help I’ll be, but I can try it."
            hide sasha
            show anna teaser happy
            "Sasha smiles, and Anna dashes across the room, breaking from Kleio’s side, to tackle me into a hug."
            anna_say "Thank you so much, [hero.name]! You’ve saved us!"
            hide anna
            show sasha casual2
            sasha.say "That might be a little extreme, Anna, but, yes, thank you so much, [hero.name]."
            sasha.say "This means a lot to us."
            "I smile at them, but I’m unable to ignore Kleio’s sulking in the corner. She snorts as the two other girls fawn over me, rolling her eyes as Anna refuses to let go of my body."
            hide sasha
            show anna teaser happy
            anna_say "Here, I’ll take him to where the amps are, okay?"
            "Before anyone has a chance to agree, Anna grabs my arm, and drags me out of the room."
            "Her tiny body clings hard against mine, her breasts pressed against my arm as she took her time leading me to the room."
            "When we finally reach our destination, I can’t help but notice that she looks almost disappointed."
            "She scuffs her feet against the ground as we talk, stalling our goodbye for as long as she can."
            anna_say "Well, here we are."
            hero.say "Yep. So the amps are just in here, then?"
            anna_say "Yeah, they are. The stage doors are two large loading docks, and it should take you right to the stage."
            anna_say "Just place them on the lip, and we can handle the rest."
            hero.say "Alright, got it. Thank you, Anna. I appreciate your help."
            "Anna’s eyes got wide again, and I swear, I could hear her heart fluttering wildly in her chest."
            anna_say "No, no—thank you! We couldn’t even be doing this show without you. Thank you so much."
            "I smile, taking in her small, voluptuous body one last time before finally turning to the door."
            "With one last wave at Anna, I make my way into the room."
            hide anna
            if hero.fitness >= 25:
                "I make quicker work of my job than I expected to; the amps were heavy, and I could see why the girls needed help, but it was nothing I couldn’t handle on my own."
                "By the time I finish, it was almost time for the show to start, so I slip down from the stage, returning to the bar for one more drink to settle my aching muscles before their set begins."
            else:
                "The amps are much larger and heavier than I thought they would be, and it takes me forever to drag their large bodies out onto the stage."
                "Embarrassingly, I have to go get one of the security guards to help me move the largest one, which he does without a second thought."
                "Embarrassed, by the time I finish the excruciating task, the show is mere minutes from starting, so, in a rush, I jump down from the ledge and rush to the bar, hoping to drink away my shame and ease my weary muscles before the show begins."
        "No":
            hero.say "Uh, I mean, I would, but, like, I think Kleio is right."
            "The security guards here are probably ten times stronger than I am, and I just feel like that would be a better option. Sorry."
            "Sasha’s face twists, and she takes a step back from me, and, even though I’m tipsy, I can tell I hurt her feelings."
            "Kleio, though, looks up at me, a small smile on her face as, for the first time, I think she takes me in."
            "Nodding a small approval, she looks down again before Sasha notices her noticing."
            sasha.say "Oh, well, okay then. I guess you’re right. Anna, you can take [hero.name] back out to the bar, and, while you’re at it, you’ll get a security guard, won’t you?"
            "Looking kind of sad, Anna nods, coming up again to take my arm."
            hide sasha
            show anna teaser normal
            anna_say "Come on, [hero.name]. I’ll take you back out to the bar."
            "Allowing myself one more glance at Kleio, Anna slowly leads me out of the green room and back down the hallways we came."
            "When we reach the door that leads back to the main bar, Anna lingers by my side, clearly stalling. She shifts from foot to foot, thinking of something to say."
            anna_say "Well, thanks for trying to help, anyways. We appreciate it."
            hero.say "Yeah! Yeah, anytime, Anna. Sorry I coudn’t be of any more help."
            anna_say "It’s okay! Don’t worry about it, honestly."
            hero.say "Yeah. Well, hey, good luck tonight. You guys are gonna sound amazing."
            show anna teaser happy
            "Anna brightens up at these words, grinning widely at me once again."
            anna_say "I sure do hope so! Speaking of, I’d better get back. Once we get those amps out, I think we’re gonna start the set."
            anna_say "You’d better grab a drink and grab a spot quickly—we’re hoping to back the house!"
            hide anna
            "Her enthusiasm was infectious; I find myself grinning wider and wider as she rambles."
            "Giving her a wave goodbye as she finally sets her eye on a guard that she needs, our eyes linger on each other for one more energetic moment, before she’s whisked away down the hall, and I make my way over to the bar."
            "By the time I get my drink in my hand, I realize that Anna wasn’t lying—the house was packed already."
            "Shuffling my way towards the front, I manage to get a pretty good seat just as the set begins."
    "The girls come out on stage, looking electrified, Sasha leaning close to the microphone, speaking in a low, breathy voice I hadn’t yet heard from her."
    "The other girls look empowered, punkish, and, despite the stereotype, ready to rock ’n’ roll."
    sasha.say "Thank you all for coming out to our show tonight."
    sasha.say "We are Deathless Harpies, and we aren’t sorry about it."
    play music "music/TeknoAXE/simple_metal.mp3" loop
    "Their music was loud, angry, and the antithesis of everything I usually listened to—and yet, I could not drag my attention away."
    "Despite them being missing a member, they did not seem to be missing anything, their presence swelling and filling the small room to the brim."
    "The drunk bodies around me swung and swayed to the music, enthralled with the punk sound of electric guitar and the heartbeat from Anna’s drums."
    "Their music was electrifying, and I never wanted it to end."
    "By the end of their set, I found myself almost completely out of breath, so drawn into their performance that when their encore finally finished I felt as though I was missing an integral part of me."
    play music "music/TRG_Banks/the_night_bus.mp3" loop
    "With one more grin at her bandmates, Sasha and her friends begin what was probably one of the greatest local concerts of my life."
    "My face flushed, my eyes wild, I didn’t even hold myself back from rushing back into the green room to see Sasha and the band again—with one flash of my card at the guard, he allowed my stumbling body back, me scrambling wildly through the halls until I found the door again."
    "Busting inside, I find all three bandmates, nursing small mixed drinks, smiling and laughing, clearly high off the success of their set."
    show sasha casual2
    hero.say "Holy shit, you guys—that was amazing! Sasha, you didn’t tell me you guys were that good!"
    "Sasha smiles, but it’s clear that she’s trying to be modest. She nods slightly to me, hiding a slight blush before responding."
    sasha.say "I’m glad you liked it, [hero.name]. We’ve come really far, but we still have a ways to go."
    hero.say "Liked it? I loved it! It was fucking fantastic! You need to do this for a living, all of you do—holy shit, that was amazing."
    hide sasha
    show anna teaser blush
    "Anna looks up at me, almost vibrating with excitement and the rush of the set and my praise."
    "As though she couldn’t contain herself any longer, she rushes across the room, tackling me into a warm, tipsy hug."
    anna_say "Thank you so much, [hero.name]! You’re the best! You’re welcome here with us, anytime!"
    hide anna
    show kleio teaser annoyed
    "Kleio, the quietest one by far, looks up at this statement, looking slightly annoyed by Anna’s words."
    kleio_say "Seriously?"
    hide kleio
    show anna teaser happy
    "Anna spins around to meet her bandmate, not letting go of my waist as she speaks."
    anna_say "Don’t be such a downer, Kleio!"
    anna_say "Of course [hero.name] is welcome!"
    anna_say "He’s Sasha’s roommate, after all, and he’s so damn sweet—it’d be, like, cruelty to not let him hang out with us!"
    hide anna
    show kleio teaser annoyed
    "Kleio rolls her eyes but drops the subject, continuing to quietly nurse her drink, pleased with herself and satisfied with that praise alone."
    "I got the vibe that she was very independent, very uncaring of what others thought about her, and, despite her nasty attitude, I could see the allure very, very clearly."
    hide kleio
    show anna teaser happy
    "Anna, though, brought me back to focus."
    "She seems ridiculously hyper, almost bouncing off the walls, and, despite its seeming childishness, I can’t help but find something sexy about her."
    "We all talk for what seems like hours, with even Kleio jumping in to the conversation at times, the energy of the girls so overwhelmingly infectious."
    "We all drink and laugh, except for Sasha, who just laughs, enjoying each other’s presence and the overwhelming high from the performance."
    "As time goes on, though, the exhaustion from the night begins to creep in—slowly, carefully—and we find ourselves holding back yawns more and more as the night continues."
    "Finally, Sasha says what we’ve all been thinking—that it’s time to go home and get some rest."
    "Anna is resting in my lap at this point, holding onto my neck tightly, nuzzling her face into my chest."
    anna_say "Oh, come on Sasha, just five more minutes. We’re having so much fun..."
    "Despite her words, I can feel Anna dozing off beside me, and I hide a smile, knowing she just doesn’t want the night to end."
    "Sighing, Kleio gets to her feet, gently taking Anna from me into her arms, righting her on the floor, allowing her small body to rest against her own, slowly guiding her towards the door."
    hide anna
    show kleio teaser normal
    kleio_say "Come on, girls. Let’s get some well-deserved rest. We did well today—let’s try and reward ourselves."
    "Smiling, I gently lean on Sasha, allowing her to guide me to the door and out to our cars."
    "With one last wave at the girls, and a tight hug from Anna, we leave the bar, the car ride an exhausted, drunken blur."
    hide kleio
    "By the time we get home, I barely realize that any time has passed at all, with Sasha gently helping me into my room and taking off my nice clothes before leaving me to sleep."
    "I lay down on my bed and pass out almost immediately, my head filled with images of beautiful, punk girls and the endless, beautiful sounds of their hard rock ’n’ roll band."
    if not "kleio" in GIRLS:
        show screen message(title="Patreon Edition",what="Kleio & Anna are only available in the Patreon Edition of the game.\nVisit {a=https://www.patreon.com/Andrealphus}patreon.com/Andrealphus{/a} to become a patron and get to know them better.")
        pause
        hide screen message
    return

label sasha_b_event_01:
    $ sasha_love_max = 30
    $ sasha.set_flag("story",1)
    scene bg livingroom
    "The sound of keys rattling gets my attention; it is too early for Bree to have gone anywhere --unless she was coming home from the night before-- so it means that Sasha must be here!"
    if game.room == "kitchen":
        "I ignore the toast that pops up from the toaster and go to open the door, since by the sound of those keys she's having trouble with it."
    show sasha box normal
    "When I open the door, all I see is a stack of boxes with a pair of long, bare legs sticking out from underneath them; the brown cardboard cartons are above the level of the girl's head."
    menu:
        "Invite her in":
            show sasha box angry
            hero.say "Come on in, Sasha."
            "I move out of her way so she has room to haul her stuff inside, then follow, watching from the hallway."
            "When she comes back out of the room, I say hello."
        "Help her":
            hero.say "Oh jeez, let me help you with those."
            "I take the top two boxes carefully, and see a very pretty face framed by black hair, smiling at me."
            show sasha box happy
            "I lead the way to her room and deposit her stuff just inside the door, then step out into the hallway, turning to say hello when she comes out."
            $ sasha.love += 3
        "Take the boxes from her" if hero.fitness() >= 5:
            hero.say "Here, give me those."
            "I take the boxes without waiting for her to respond, lifting them easily, and turn to take them to her new room."
            "When I come back out, she's standing in the hallway and I go to say hello."
            $ sasha.love += 3
        "Go grab more boxes outside":
            hero.say "Oh hey! Yours is the first door on the left down the hall; I'll go out and grab another load for you, okay?"
            show sasha box happy
            "A muffled 'mm-hmm' comes from behind the boxes and I step aside so she has plenty of room to navigate. Heading out the door, I go up to her car, a small black two-door."
            "It has bumper stickers for metal and goth bands plastered all over the back of it, and a pair of little black rubber bats hangs from the rearview mirror where some people would hang fuzzy dice."
            "I grab a load of her stuff from the back seat and head back into the house, taking them into her room and setting them down. When I turn to head back out, she's standing in the hallway and I go to say hello."
            $ sasha.love += 2
    hide sasha
    scene bg livingroom with fade
    show sasha casual2
    hero.say "Hey, welcome to the house... Sasha ..?"
    "I’m fairly sure that’s the right name; I’ve only met her once briefly."
    "I stick out my hand and she gives it a shake with a firm and confident grip, and I notice her nails are painted black."
    "She smirks, which actually looks pretty on her face, and pushes long inky hair back."
    sasha.say "I must be, since it'd be pretty funky if some other random girl just wandered in here with a stack of boxes,"
    "she responds with a touch of surprisingly appealing sass."
    menu:
        "Joke" if hero.charm() >= 8:
            hero.say "Nah, I get strange girls coming and going here all the time. Just usually not so early in the morning!"
            show sasha happy
            "I grin a little to show her I'm joking and she chuckles and shakes her head."
            sasha.say "In that case, I better sound-proof my room,"
            "she retorts, surprising me into a startled laugh."
            $ sasha.love += 2
        "Laugh" if hero.charm() >= 4:
            "I roll my eyes a little, but chuckle; if Sasha's always like this, it will add some amusing sarcasm to the house, though she probably won't get on all that well with Bree at first."
            hero.say "Let's go get the rest of your stuff, non-random girl who wandered in here."
        "Be awkward":
            hero.say "Guess it would be, huh?"
            "I shuffle my feet a little and glance down with a small smile."
            hero.say "Want me to go get some more of your stuff, Sasha?"
            $ sasha.sub -= 5
    "Together, we manage to haul most of her stuff into her bedroom, where Sasha can sort it from there; she says she's going to come by with a U-Haul later today with her furniture."
    "I've got to go now. I'll see you when I get home; welcome to the house, Sasha."
    hide sasha
    return

label sasha_b_event_02:
    $ sasha_love_max = 40
    $ sasha.set_flag("story",2)
    show bg secondfloor
    if not game.get_flag_value("female"):
        "I walk in to the sound of boxes toppling over and some grade-A creative cursing."
        "Sounds like Sasha is trying to get things unpacked!"
    else:
        "I hear Sasha cursing in her bedroom..."
    "I walk down the hallway and peer into her room; she's managed to muscle a dresser and a bookshelf into the room by herself, but the U-haul is still outside with her bed and a little more furniture in it."
    scene bg bedroom3
    show sasha angry
    "Several boxes lay on the floor, a few with books and clothing tumbled out of them; they must have been stacked and fallen over."
    "Sasha looks frustrated enough to throw something."
    menu:
        "Tell her to keep it quiet":
            hero.say "Hey, I get that this is frustrating, but can you try to keep it down?"
            "She slams the door shut after glaring at me.."
            $ sasha.love -= 5
            return
        "Offer to help":
            show sasha normal
            hero.say "Hey, looks like you've got a lot going on here; need some help with unpacking?"
            $ sasha.love += 2
            if not game.get_flag_value("female"):
                sasha.say "What I really need is some muscle to help move the furniture in. You game?"
            else:
                sasha.say "A second pair of arms would be perfect."
            menu:
                "Accept" if hero.energy > 2:
                    hero.say "Sure, let's get these boxes out of the way and we'll get started!"
                    $ sasha.love += 2
                "refuse":
                    hero.say "Sorry, I don't have time right now."
                    $ sasha.love -= 2
                    return

    if not game.get_flag_value("female"):
        hide sasha
        scene bg house car with fade
        "Sitting in the U-Haul are a full-size bed, a small computer desk, a beat-up green recliner, and a pair of nightstands."
        "On the lawn are a stand lamp and a desk lamp, along with a few stray boxes."
        show sasha
        sasha.say "Let's get started with the bed,"
        "Sasha says to me with a small grin."
        menu:
            "Joke and agree" if hero.charm() >= 10:
                hero.say "Already? That's quick,"
                "I respond with a wink to show I'm just teasing."
                show sasha happy
                sasha.say "Yeah, well, no point in waiting. It's got to happen eventually, right?"
                "Sasha smirks."
                "I chuckle at her response, and we get started hauling the furniture in, too busy to converse much further for the moment."
                $ sasha.love += 1
            "Just agree":
                hero.say "Whatever you say,"
                "I reply, moving to the split box-spring to take an end of it while she takes the other."
                hero.say "You're the boss, boss."
                sasha.say "Heh. Damn right I am,"
                "she answers, taking her own end so we can start lugging it inside."
                $ sasha.love += 1
    scene bg bedroom3
    show sasha
    sasha.say "You wanna help me get these boxes empty?"
    sasha.say "I'll be able to sort everything out and get stuff where it belongs way easier if I can just see everything."
    if not game.get_flag_value("female"):
        "Sasha watches me with those pretty, dark eyes and a small half-smile."
    menu:
        "refuse":
            hero.say "Sorry, I don't have time tonight."
            "I've got to get a good night of sleep so I can keep pushing for that promotion at work."
            $ sasha.love -= 1
            return
        "accept" if hero.energy > 5:
            hero.say "Sure, let me get the box cutter."
            $ sasha.love += 1
    "I help her get her bed and the furniture placed just where she wants them and then get started opening up the slew of boxes she's got scattered through the room."
    "Sasha has a lot of books!"
    "All sorts of topics, with a lot of fantasy and science fiction."
    "Plenty of music too; her CD tower is going to be full before they're all unpacked."
    "She's got a nice stereo set up on the big book shelf, and I prepare myself to deal with some loud music now and then."
    "I sit on the edge of the bed and slit the flaps open on a smallish box, then open it up and blink in surprise."
    "It's full of toys, and not the kind kids play with!"
    hero.say "Wow,"
    "I murmur softly before I can stop myself."
    "Sasha turns and looks at me with a brow raised, then grins as she sees the box I've opened."
    "She shows no shame at all, no shyness or embarrassment; this woman is confident!"
    show sasha happy
    sasha.say "What, you've never seen sex toys before?"
    menu:
        "No":
            hero.say "Well... no,"
            "I say a little defensively, suddenly feeling shy under her frank gaze."
            $ sasha.love += 1
            show sasha normal
            sasha.say "Aww,"
            "Sasha coos with a little smile."
            sasha.say "Well, take a good look and get an education!"
            menu:
                "Don't look at the toys":
                    hero.say "No, it seems sort of private to me. I'll leave it on your nightstand."
                    $ sasha.love -= 1
                    hide sasha
                    $ HIDE_UI = True
                    scene bg black with fade
                    $ renpy.pause(0.1)
                    scene bg bedroom3
                    $ HIDE_UI = False
                    show sasha
                    "Job done, I tuck the box-cutter back in my pocket."
                    hero.say "That's the last of them!"
                    menu:
                        "Offer more help" if hero.energy > 7:
                            hero.say "Do you need any more help?"
                            "Sasha shakes her head."
                            if not game.get_flag_value("female"):
                                sasha.say "Nah, thanks. You've done your Big Strong Man deed for the day."
                            else:
                                sasha.say "You already have been more help than most of my friends."
                            $ sasha.love += 1
                        "Stop helping":
                            hero.say "That's it for me. Good luck with your unpacking!"
                    sasha.say "Thanks for the help. Catch you later,"
                    "She then moves to the next box of stuff."
                    return
                "Look at the toys":
                    pass
                "Joke" if hero.charm() >= 10:
                    hero.say "Planning on a demonstrations?"
                    "I ask with a snicker. Sasha laughs and wags her finger mock-scoldingly at me, then goes back to putting her books on the shelf."
                    $ sasha.love += 1
            hide sasha
            "I start sorting through the box, which has several dildos of various sizes --including one that sort of astounds me-- a few of which have control knobs for vibration."
            "A box of ribbed condoms is in here as well, along with what looks like a leather thong!"
            "I pull the thong out and realize what it is by the circular opening at the front; a strap on!"
            hero.say "So, you're into girls?"
            show sasha
            "Sasha smirks at me."
            sasha.say "And boys. Never know what you'll like until you try it!"
            menu:
                "Be surprised" if hero.charm < 10:
                    hero.say "You use this on guys?"
                    if not game.get_flag_value("female"):
                        "I cringe a little at the thought and shake my head; no way I'd let a girl use one of these on me, no matter how hot she is!"
                        "Sasha shrugs, seeming disinterested suddenly and returns to putting away her books."
                        sasha.say "Everybody has their kinks,"
                        sasha.say "Go ahead and leave the box on the nightstand; I'll put that stuff away later."
                        "I put the strap-on back in the box and resume the process of getting all the other boxes open, wondering if there are more surprises in store."
                        $ sasha.love -= 1
                    else:
                        sasha.say "You would not believe how many macho looking guys gets off being pegged by a sexy lady."
                "Be surprised" if hero.charm >= 15:
                    hero.say "You use this on guys?"
                    if not game.get_flag_value("female"):
                        "I look at it with even more curiosity, wondering how that would feel."
                        "I've heard that it can feel really good, but I've never given it much thought before."
                        "Seeing the equipment that would let a girl do it, now I'm curious."
                    "Sasha smiles a little and shrugs."
                    sasha.say "Sure. Some guys really love it. Especially the submissive ones. And I like being in control,"
                    "she adds with a grin."
                    sasha.say "Go ahead and leave the box on the nightstand."
                    $ sasha.love += 1
                "Be intersested":
                    hero.say "Wow.. that.. seems kinda hot."
                    if not game.get_flag_value("female"):
                        "I wonder how it would feel, and I peer in the box at the various dildos that might fit into the strap-on with curiosity."
                    show sasha happy
                    "Sasha grins wickedly at me."
                    sasha.say "Oh, believe me, it's hot. Go ahead and leave the box on the nightstand."
                    $ sasha.love += 2
        "Yes":
            hero.say "Sure I've seen sex toys before, but not this many unless I was in a sex shop!"
            "I grin at her, making sure my tone is teasing so she won't get offended."
            sasha.say "Spend much time in sex shops, do you?"
            "She smirks at me."
            menu:
                "Yes":
                    hero.say "Hey, everybody needs a little spice in the bedroom, right?"
                    "Sasha grins."
                    sasha.say "Absolutely. The spicier, the better! Go ahead and put that on the nightstand; I'll unpack it later."
                    $ sasha.love += 2
                "No":
                    if not game.get_flag_value("female"):
                        hero.say "Ha! No, I don't need any help in that department."
                    else:
                        hero.say "No I was always too shy..."
                    "Sasha grins."
                    sasha.say "Don't know what you're missing. Go ahead and put that on the nightstand; I'll unpack it later."
    hide sasha
    "The Naughty Box set aside on the nightstand, I open up the rest of the boxes so she can see what stuff she's got where."
    "Job done, I tuck the box-cutter back in my pocket."
    show sasha
    hero.say "That's the last of them!"
    menu:
        "Offer more help" if hero.energy > 7:
            hero.say "Do you need any more help?"
            "Sasha shakes her head."
            if not game.get_flag_value("female"):
                sasha.say "Nah, thanks. You've done your Big Strong Man deed for the day."
            $ sasha.love += 1
        "Stop helping":
            hero.say "That's it for me. Good luck with your unpacking!"
    sasha.say "Thanks for the help. Catch you later,"
    "She then moves to the next box of stuff."
    return

label sasha_b_event_03:
    if not game.get_flag_value("female"):
        $ sasha_love_max = 60
    else:
        $ sasha_love_max = 200
    $ sasha.set_flag("story",3)
    if not game.get_flag_value("female"):
        "The Winchester is a little better lit than most bars, and the music --a local Classic Rock station-- is played low enough to not make people have to shout over it; it's my favorite place to grab a drink and maybe some good Pub food after work."
        "I go in and look over the tables, and see that there are plenty of little round two-seaters free before I glance toward the back of the room at the pool tables, and there I see a pair of familiar and very lovely legs."
    show sasha play pool
    "Sasha is bent over the pool table, queue in hand, getting ready to take a shot."
    if not game.get_flag_value("female"):
        "Her little pert ass looks fantastic in those cut-off jean-shorts and I indulge myself a moment staring at her; that position is extremely sexy and distracting."
        "It's distracting to the other guys around the pool table too; she's got several pairs of eyes on that ass."
    menu:
        "Talk to her":
            "I ignore the bar and tables for the moment and walk up to stand beside Sasha."
            hide sasha
            show sasha
            "She straightens up with a little bit of surprise in her big dark eyes, then flashes me a grin."
            sasha.say "Well well, fancy meeting you here. Care to lose some money?"
            menu:
                "No":
                    if not game.get_flag_value("female"):
                        hero.say "Pass, but I'll buy you a drink."
                        "I'm pleased when Sasha agrees and I go to the bar, bringing back her rum and cola along with my mug of beer."
                        "I enjoy the view of her taking those difficult shots leaned over the pool table, and she notices me looking, but I just flash her a grin."
                    else:
                        hero.say "No, but we can have a drink together if you want."
                        "I'm pleased when Sasha agrees and I go to the bar, bringing back her rum and cola along with my own."
                    $ sasha.love += 1
                "Yes":
                    hero.say "Nah, but I'm down for winning some,"
                    "I say as I grab a queue off of the wall and the triangle to rack the balls back up."
                    hide sasha
                    show sasha play pool
                    if not game.get_flag_value("female"):
                        "I'm good at pool, but so is she, and damned if she isn't distracting as hell the way she takes those shots in those tiny shorts."
                        "And she knows it too, flashing me a bit of a grin when she catches me looking."
                    hide sasha
                    show sasha
                    if randint(0,1) == 1:
                        if hero.money >= 10:
                            $ hero.money -= 10
                        else:
                            $ hero.money = 0
                        if not game.get_flag_value("female"):
                            sasha.say "Good thing we were only betting a buck. A guy like you could lose his shirt to a gal like me."
                        else:
                            sasha.say "Good thing we were only betting a buck. I need you to pay your share of the rent."
                        if not game.get_flag_value("female"):
                            if randint(0,1) == 1:
                                hero.say "Oh, you want me shirtless already?"
                                "I smile innocently as I ask the question, arching a brow, and she starts laughing good-naturedly."
                                $ sasha.love += 1
                            else:
                                hero.say "If we're betting shirts, I think the folks around here would prefer you lose!"
                                "I grin at her and she snickers, glancing around at the guys paying attention to the way she moves."
                                $ sasha.love += 2
                        else:
                            sasha.say "You're pretty good! I haven't had that much fun playing pool in a while."
                    else:
                        sasha.say "You're pretty good! I haven't had that much fun playing pool in a while."
                        $ sasha.love += 2
                    if not game.get_flag_value("female"):
                        hero.say "You know, it's a little unfair playing with someone that gets so distracting taking those tough-angle shots,"
                    $ sasha.love += 1
            hide sasha
            if not game.get_flag_value("female"):
                "We go to the bar and I order a beer when the waitress comes over."
            else:
                "After the game we move on to the bar."
        "Leave her alone":
            hide sasha
            show hero
            if not game.get_flag_value("female"):
                "I go to the bar and order a beer when the waitress comes over."
            else:
                "I go sit at the bar."
            "When Sasha finishes her game, taking a couple of bucks bet by a guy who was too distracted by her legs to play well, she turns and sees me."
            "I raise my hand in a friendly wave, and she saunters over after putting her pool queue back."
            hide hero
    show sasha
    sasha.say "Come here often?"
    if not game.get_flag_value("female"):
        hero.say "Often enough,"
        hero.say "See you found the local hang-out easy enough. How's the moving going?"
    else:
        hero.say "How's the moving going?"
    if game.days_played < 7:
        sasha.say "Slow. Most of my boxes are in, but I'm gonna need help with the furniture."
        if not game.get_flag_value("female"):
            sasha.say "Care to be my hero?"
        menu:
            "Yes, later":
                hero.say "Why not? But for now, let's have dinner."
                menu:
                    "Invite her" if hero.money >= 50 and hero.energy > 3:
                        $ hero.money -= 50
                        hero.say "I'll buy, it's my duty to show my new roommate a warm welcome."
                        "Sasha smiles and agrees."
                        "She scoots the chair to sit beside me to look over the menu and get food suggestions, and we make small-talk over dinner before heading back to the house."
                        $ sasha.love += 1
                    "Order food":
                        if not game.get_flag_value("female"):
                            "Sasha agrees, asking for food recommendations since she's never been here before, and we make a little small-talk over the meal before heading back to the house."
                        else:
                            "Sasha agrees, and we make a little small-talk over the meal before heading back to the house."
                $ game.pass_time(1)
            "Yes, now" if hero.energy > 5:
                hero.say "I'd love to help. Do you want to go now?"
                "Sasha nods and gets up; she follows me home, and we get to work moving furniture."
                $ sasha.love += 2
                $ game.pass_time(1)
            "No":
                hero.say "Sorry, I don't really have the time"
                $ sasha.love -= 1
    else:
        sasha.say "It's over already, but thanks for asking"
        "We chat a little before going back home."
    hide sasha
    show bg black with fade
    return


label sasha_b_event_04:
    $ sasha_love_max = 200
    $ sasha.set_flag("story",4)
    scene bg secondfloor
    "I walk down the hall and stand outside of Sasha's door, listening, and it turns out I was right: it's the sound of a bass guitar, playing the bass line from Violent Femme's Blister in the Sun."
    "And just the bass line, which meant someone had very esoteric taste in music, or someone was actually playing the instrument."
    menu:
        "Leave":
            "Never had a musician for a room mate before."
            "I hope she doesn't play too late at night!"
            "I head back toward the kitchen, leaving Sasha alone to practice."
            return
        "Open the door":
            scene bg bedroom3
            show sasha sleep
            "Curious, I open the door and peak inside to see Sasha sitting on the edge of her bed."
            "I'm lucky; her back is towards me so she won't catch me snooping."
            "Can't see the instrument, but I can enjoy the sound for a bit."
            "I finaly decide to call out to her and she abruptly stops playing."
        "Knock on the door":
            scene bg bedroom3
            "Curious, I knock lightly on her door and the music abruptly stops."
            "Yep, definitely Sasha as the musician."
            show sasha sleep
            "A moment later and the door opens, revealing Sasha still in her PJs: super short shorts and a snug shirt, both in dark colors (surprise, surprise.)"
    hero.say "Hey, Sasha. I didn't know you played music."
    "I glance over at the bass guitar sitting on its stand. Jet black with silver spiderweb patterns; yes, that fits Sasha."
    show sasha sleep happy
    sasha.say "Oh, yeah! Been playing for about five years now."
    sasha.say "Even got a band, mostly goth-punk stuff, some covers."
    menu:
        "Don't play too late.":
            "Sasha sounds excited to talk about this topic, but it's not really my thing."
            hero.say "That's cool. Just don't play too late, huh?"
            show sasha sleep angry
            "I wonder why she closes the door so sharply."
            $ sasha.love -= 5
            return
        "That's great." if not "guitar" in hero.skills:
            hero.say "Very cool!"
            "I do enjoy music, especially live shows."
            hero.say "Where do you play? Maybe I could catch a show some time."
            "Sasha gets an excited look in those pretty eyes."
            "It seems she likes the idea of having someone be enthusiastic about her music with her."
            sasha.say "We usually play down at the Black Box."
            "I've driven past the place before; cube-shaped black building, hence the name, usually catering to teens-20 somethings and playing alternative, goth, and punk music."
            "Some of that stuff is pretty good."
            hero.say "I know where it is. When's the next performance?"
            "She grins and saunters over to grab her bass by the neck, sitting on the bed as she most likely had been before I knocked."
            sasha.say "Pretty soon, I'll tell you when I know exactly. You should absolutely come; you'll have a blast. Plus, cheap drinks!"
            "I flash her a grin."
            hero.say "You had me at 'got a band'."
            "Sasha grins right back at me, starting to pluck the bass strings again."
            "I close the door to give her better acoustics for practicing."
            "Looks like I'll be hitting the bar pretty soon!"
            $ sasha.love += 1
            $ game.set_flag("performance",1)
            return
        "That's great." if "guitar" in hero.skills:
            "How cool! I was living with another musician."
            hero.say "Really? Hey, I play guitar. Maybe we could play together some time."
            "It would be a good way to bond with her."
            sasha.say "I'll do you one better! We're practicing every Friday at 8pm; wanna come hang and maybe jam with us after?"
            "That's the best offer I've had all week; I rarely get to play music with anyone else these days."
            "My old garage band days were over, though I suspected that attending this practice would put me in a garage again. Fine with me."
            hero.say "I'd love to! Gonna perform soon?"
            sasha.say "Yeah, we've got a gig at the Black Box on pretty soon."
            sasha.say "They do pretty good shows there, and the booze is cheap."
            sasha.say "Feel free to swing by if you're in the mood for goth or punk music."
            "Sometimes I was in the mood for punk music."
            "I didn't know much goth stuff, but maybe she'd wind up getting me into it."
            "Could be fun."
            hero.say "Make sure to give me the date and time when you have it."
            "I walked into the bedroom and we both sat on the edge of the bed."
            $ sasha.love += 2
            $ game.set_flag("band",1)
            return

label sasha_band_event_01:
    $ game.set_flag("band",2)
    if "studio" in HIDDEN:
        $ HIDDEN.remove("studio")
    play music "music/TRG_Banks/the_night_bus.mp3" loop
    scene bg map
    show sasha casual
    "Sasha is waiting for me in front of the studio."
    sasha.say "Hurry up,"
    sasha.say "We’re already late.."
    sasha.say "This practice is ridiculously important."
    sasha.say "Battle of the Bands is pretty soon, and we only have a few rehearsals left before we have to perform."
    sasha.say "This could be our big break"
    "I sigh, but follow her dutifully, not wanting to argue when she’s in this kind of mood."
    "Besides I don’t want her to kick me out when I haven’t even heard her play yet; her boasts about her musical prowess without any proof to back them up have gotten rather annoying, and I want to see, and hear this band for myself."
    scene bg studio
    "We enter the small studio, and I follow her as she weaves through the tight hallways to the back."
    "She enters through the last door on the left, and beckons me to follow."
    hide sasha
    show anna teaser normal at left
    show kleio teaser annoyed at right
    "Inside stand two girls, one more edgy than the other, hesitantly tuning their instruments."
    "The first is blonde, arms covered in tattoos, her frame almost boyish that if not for her massive breasts, I would’ve thought she was a boy. "
    "The second is smaller, almost girlish, her hair short and pink and her body wonderfully curvy despite her small frame."
    "Their heads snap up when they hear Sasha, but their eyes quickly fall on me instead."
    "The smaller girl, with the pink hair, speaks up first."
    show anna teaser normal
    hide kleio
    anna_say "Who’s the boy? Did you bring him?"
    anna_say "Is he that roommate you talked about?"
    "Sasha, scanning the room, cuts off her questions."
    hide anna
    show sasha casual angry
    sasha.say "Doesn’t matter Anna. Where the hell is Jade?"
    "Despite Sasha’s clear distraction, I take notice of what Anna said."
    "Was she talking about me?"
    hide sasha
    show kleio teaser annoyed
    "The other girl, the one with the short, blonde, almost boyish hair, shrugs, distracting me from my revelation."
    kleio_say "No idea. We’ve been calling and texting her, and she hasn’t responded at all."
    "Anna pipes in, sounding too positive for such a shitty situation."
    show anna teaser normal at left
    show kleio teaser annoyed at right
    anna_say "We think she bailed."
    hide anna
    hide kleio
    show sasha casual angry
    "Sasha’s body stiffen and her fists clench as she turn on the girl."
    sasha.say "Anna, what do you mean, ‘you think she bailed.’ "
    sasha.say "She’s our lead guitarist--she can’t fucking bail!"
    hide sasha
    show kleio teaser annoyed
    "The first girl rolled her eyes at Sasha’s anger, clearly not phased."
    kleio_say "Chill out, Sasha. We’ll find someone else. It may just take a while."
    "Anna pipes up again, not phased by Sasha’s scathing tongue."
    show anna teaser normal at left
    show kleio teaser annoyed at right
    anna_say "We think she was never really going to join in the first place."
    anna_say "Kleio said she probably just wanted to pick up chicks."
    show anna teaser normal
    hide kleio
    "After a moment, she shrugs."
    anna_say "At least, it makes more sense as to why she’s not calling us after she slept with me."
    "It’s clear to me, and the other girls, and anyone who might take a passing glance at Sasha, that she’s seething mad and doesn’t want to take this for an answer, nor does she even want to comment on Anna’s love life."
    hide anna
    show sasha casual angry
    sasha.say "We’ll never find someone, especially not in time for Battle of the Bands. It’s hopeless."
    "She slumps back in the chair, crossing her arms, staring angrily at the wall."
    hide sasha
    menu:
        "I can play guitar":
            "Um, well, you know, Sasha, I can play guitar?"
            show sasha casual
            "Sasha rolls her eyes, dismissing me entirely."
            sasha.say "I’m sure you can, [hero.name]."
            sasha.say "You and every other boy on this planet."
            sasha.say "You’ll be no help, we’re doomed."
            hide sasha
            show anna teaser normal
            "Anna, glares at Sasha."
            anna_say "No need to be so cruel, Sasha."
            anna_say "He clearly wants to help."
            anna_say "Why not let him? What have we got to lose?"
            hide anna
            show sasha casual
            "Sasha sighs, clearly annoyed, but she concedes, knowing she was out a guitar player, and—as far as I was aware—out of options."
            sasha.say "Whatever.."
            "Kleio and Sasha step aside to sulk, scrolling through their phones, clearly looking for a replacement guitarist, but Anna smiles at me, gesturing to the guitar before stepping aside to turn on my mic."
            "I take a hesitant breath, before I carefully pick up the guitar."
            hero.say "Step aside, ladies. Hand me that guitar, let me show you what I can do."
            "Sasha’s head snaps up, and, before I know it, she’s laughing at me, her whole body consumed in convulsions before I can even say anything more."
            sasha.say "[hero.name], I highly doubt you can do anything that would be good enough for us, but if you want to embarrass yourself, be my fucking guest."
            hide sasha
            "Annoyed by her words, I confidently stride forward, grabbing the neck of the guitar and yanking it into my arms."
        "Say nothing":
            "I stay silent, trying to fade into the background, but it’s hopeless."
            show anna teaser normal
            anna_say "Hey, [hero.name], can you play guitar?"
            hide anna
            show sasha casual
            sasha.say "Are you kidding me, Anna? You want to try [hero.name]? We are an all female band!"
            "After a moment though, she sighs."
            sasha.say "But if you really want to try, then be my fucking guest."
            hide sasha
            "The first girl steps aside to join Sasha, not paying me any attention at all as Anna gathers the guitar for me."
            show anna teaser normal
            "She smiles at me, clearly curious and excited for me, before stepping aside to adjust my mic."
            "Embarrassed, I fumble with the guitar, hoping I can at least get some of this right."
    "I tune the guitar quietly, watching the first girl and Sasha more than I watch Anna."
    "It’s clear she’s already sold—either that, or she’s just attracted to me—but it’s them, especially Sasha, that I want to impress. I want to show her what I can do."
    play music "music/TeknoAXE/simple_metal.mp3" loop
    "With one more inhale, and one more strum to test the guitar, I begin to play."
    "The music is louder than I expected it to be, the studio rather conducive to the sound of music."
    "It sounds even better than I thought it would, and, by the looks on their faces, it’s clear Sasha and her bandmate are thinking the same way."
    show anna teaser happy
    "Across the room, Anna is beaming, clearly smug as she watches me play. Her body language screams, I told you so."
    "I can’t help but smile before I open my mouth to sing."
    "At that point, Anna becomes so pleased that she rushes to the booth, slamming on an old recording of theirs on top of my voice."
    "I quickly adjust to their record, mixing my voice in with their sounds."
    "Kleio and Sasha both roll their eyes, pretending to not be impressed, but it’s clear that it’s only their pride in their way."
    "I have them sold."
    "When the recording finally comes to an end, I finish out my guitar, holding the last note until my breath gives out, turning to the girls for their approval."
    play music "music/TRG_Banks/the_night_bus.mp3" loop
    "I can’t hold back the cocky grin on my face as I look at them. "
    hero.say "So, what do you think?"
    "Anna rushes out of the booth, nearly tackling me with her hug."
    anna_say "Oh my gosh, [hero.name]! You did amazing! Kleio, Sasha, he has to join us."
    anna_say "You guys would be so, so stupid not to let him in!"
    hide anna
    show kleio teaser annoyed
    "The first girl, Kleio, rolls her eyes at her friend’s enthusiasm"
    kleio_say "He’s good, but not great, and his attitude needs some serious adjustment."
    kleio_say "I vote no."
    kleio_say "We can find someone way better. Preferably a girl."
    kleio_say "I’m not a fan of all this testosterone, anyway."
    show anna teaser happy at left
    show kleio teaser annoyed at right
    "Anna pouts, clearly protective of my words, before turning desperately to Sasha."
    anna_say "Sasha, come on!"
    anna_say "You can’t deny that what you just heard was good."
    anna_say "He simply has to join us."
    anna_say "It’s for the good of the band."
    anna_say "Come on!"
    hide kleio
    hide anna
    show sasha casual
    "Sasha wavers, clearly wondering if she wants her pride to win, or her band."
    "Proud of myself, but still hesitant, unsure of these girls, I find myself wavering slightly."
    "After a long, pregnant pause, Sasha finally opens her mouth."
    sasha.say "What if we just let him in, just for Battle of the Bands? If he proves himself worthy, he can stay after that."
    sasha.say "If not, we’re booting him, no if’s, and’s, or but’s, alright?"
    hide sasha
    show anna teaser happy
    "Anna seems to ignore the second bit, simply squealing and jumping over to hug Sasha."
    anna_say "Sasha, you’re the best!"
    anna_say "You won’t regret it, I can tell he’s going to be great for us!"
    show anna teaser happy at left
    show kleio teaser annoyed at right
    "Kleio scoffs, before crossing her arms and turning to me."
    kleio_say "Chill out, Anna."
    kleio_say "Jesus Christ."
    kleio_say "Sasha didn’t even ask him if he really wanted to join."
    kleio_say "He just played guitar—that’s all."
    "That observation seemed to make Anna falter, and she turned to me, eyes wide."
    anna_say "Well, you will join, won’t you?"
    menu:
        "Yes":
            "I barely even have to consider it."
            "A grin overtakes my face as I find myself agreeing."
            hero.say "‘Course I will. Seems like you guys need me, anyway."
            "Anna grins and hugs me again, her gratitude clearly abundant."
            anna_say "Oh, thank you so much, [hero.name]! You’ve saved us."
            "Her enthusiasm is infectious, and I can’t help but smile, looking down at this woman as she grins up at me."
            "She’s rather cute too, and I’d be lying if I said I didn’t notice her breasts shoved up against my arm."
            "With a smug grin on my face, I realize that joining this band was the best idea I’ve had in a long time."
        "No":
            "It takes me a moment to really process what she’s asking."
            "Joining a band would be super cool, and I’d definitely be lying if I said that I didn’t want to spend more time with these insanely hot women, but joining a band is an insane time commitment, and one that I’m not sure I want."
            "Plus, it’s clear that over half the band doesn’t really want me here, and I’d be crazy to think that a band full of people who dislike one another would work."
            "I find myself opening my mouth to backpedal my way out of the situation, scrutinized under Kleio’s annoyed gaze, when I catch sight of Anna again."
            "Her eyes are so full of hope and desperation that I falter again, wanting nothing more than to make her happy."
            "She’s really cute when she’s happy, and I wouldn’t mind being able to make her happy, again and again and again..."
            "My mind is so lost in thoughts about fucking Anna that it barely even registers that I’ve opened my mouth to agree until it’s already happened. "
            hero.say "Yeah."
            "My gaze is still locked on Anna."
            hero.say "Yeah, I’ll join."
            "Anna grins so wide I think it might break her face, and, ignoring Kleio and Sasha’s annoyed glares, she rushes over to me and tackles me into a hug."
            "Although I’m uncomfortable, it’s really hard to not smile when there’s a cute girl basically straddling your arm."
            "As I look down at her grinning face, I hesitantly think that maybe joining a band wasn’t such a bad idea after all, if it means I get to spend more time with her."
    "Kleio shatters my moment, scoffing as she turns aside to pluck at her guitar."
    kleio_say "You’re ridiculous, Anna, honestly."
    "She tosses a scathing glance my way."
    kleio_say "You’d better be good."
    "For a moment, I watch Kleio, wondering what her problem was."
    "She stays silent for a moment, before turning to me with a devious glance."
    kleio_say "[hero.name], you can join our band, but you know, before you joined, it was an all-female band."
    kleio_say "If you want to stay, you’ll have to crossdress."
    menu:
        "Ok":
            $ game.set_flag("bandcrossdress",True)
            "I shrug, grabbing up the guitar before glancing to Sasha for guidance."
            "She’s hiding a slight grin, the first time this whole practice I’ve seen her smile. Anna stifles some laughter, too."
            "Clearly, they think this idea is hilarious."
            "I decide to play along."
            hero.say "Sure."
            hero.say "Of all the embarrassing things I’ve done, crossdressing is probably the least of my worries."
            hero.say "Show me a dress and buy me heels and I’m yours."
            "Kleio’s eyes widen, and all three girls burst into laughter. I can’t help but join in with them."
            "For a moment, we simply all laugh, but by the mischievous glint in Kleio’s eyes, I can tell she’s more serious than I thought. Or, at the very least, she’s going to have a lot of fun embarrassing me."
            "As the laughter dies down, we get serious again, and Kleio turns to Sasha, waiting for her to begin the rehearsal."
        "No way":
            "My eyes widen, and I try to hide my disbelief."
            "Crossdressing? She has got to be kidding."
            "I try not to offend her, but also desperately trying to turn her down."
            hero.say "Uhh..."
            "Luckily, Anna comes to my rescue."
            anna_say "Lay off him, Kleio. He doesn’t have to crossdress. Just because we were an all-girl band before doesn’t mean we can’t have a boy now."
            "I could kiss Anna I’m so happy. Luck for me, Kleio doesn’t push the point anymore, just rolls her eyes and looks to Sasha for her to begin rehearsal."
    "Rolling her eyes, Sasha stands up, crossing the room, gathering her guitar and turning to me."
    kleio_say "Take us away, [hero.name]."
    "With a small grin, I begin to play."
    "Time moves fast for all of us, and although, by the end of it, Sasha and Kleio are still hesitant, it’s obvious that they’re a lot less stingy than they were when we started."
    "I even caught Kleio smiling at me once or twice when she thought I wasn’t looking."
    "Overall, it was a pretty good practice."
    "Eventually, though, we all crashed, exhausted, and we all unanimously decided to take a break."
    "Sipping on a Coke the girls had set aside, I find myself making casual conversation."
    hero.say "So, Anna, tell me about yourself."
    show anna teaser blush at left
    "Anna blushes, clearly embarrassed to be called out directly, but not unwilling to share."
    anna_say "Well, I go to University around here, actually. I moved here from Virginia just to go."
    "My eyebrows shoot up, unable to contain my surprise. I didn’t peg her as a university girl."
    hero.say "Oh really? That’s awesome. What are you studying?"
    anna_say "Biology."
    "She can’t contain her massive grin as she speaks."
    anna_say "I want to be a scientist, actually. I know it’s a little silly—I don’t exactly look like a scientist—but hey, a girl can dream, right?"
    menu:
        "Yes":
            "I nod. Although I’m a little skeptical, I try not to show it."
            hero.say "Definitely. It’s good that you’re pursuing your dreams."
        "No":
            hero.say "I guess, but you may be just slightly off the mark there. You seem to be better suited here."
            "Although she seems hurt, she lets it slide."
    hero.say "Anyway, what brings you here?"
    anna_say "To the band, you mean?"
    hero.say "Yeah."
    anna_say "Oh! Well, I met Sasha at the store I go to at the mall all the time, because that’s where she works, you know?"
    anna_say "And one day we got to talking, and I happened to mention that I played the drums. She brought up she had a band, and, well, from there, it’s history."
    "She grins, glancing over at Sasha."
    anna_say "Isn’t that right, Sasha?"
    hero.say "Kleio, right?"
    "Kleio glances over at me, almost startled as though I’m talking to her and not Anna, who had been soaking up my energy all afternoon."
    kleio_say "Yeah? What about it?"
    hero.say "Nothing, I was just trying to get to know my fellow bandmates better."
    kleio_say "Ah."
    "There was a pause."
    "I try again, unwilling to let this conversation fall flat just yet."
    hero.say "That a really cool name."
    kleio_say "Thanks. I picked it myself."
    "I blink, a little startled but trying not to show it. "
    hero.say "Oh, really? Is it a nickname?"
    "She nods, and then, almost as though she senses how much I was trying, she tosses me a bone."
    kleio_say "Sasha sorta helped me pick it out when we first met, isn’t that right, Sasha?"
    "I sigh, turning towards Sasha, giving up on trying to interact with someone who clearly wants nothing to do with me."
    hide anna
    hide kleio
    show sasha casual
    "I turn to Sasha, a little overwhelmed by these new girls, unwilling to branch out yet."
    hero.say "What made you decide to start a band?"
    "She looks a little caught off guard, but for once, decides to answer honestly, and without a hint of her usual sarcasm."
    sasha.say "Well, I’ve known Kleio for a while, and her and I always used to joke about starting a band."
    sasha.say "But when I met Anna in the mall that day—I don’t know, it just all ended up working out."
    sasha.say "We all pooled our money, and we got this studio for a few weeks."
    sasha.say "But if we don’t make it back at Battle of the Bands, then we’re through."
    "I give her a hopeful grin."
    hero.say "I’m sure we’ll get there, I can feel it."
    "Seemingly stunned by my sincerity and unwavering optimism, Sasha gives me a rare smile."
    sasha.say "Thanks, [hero.name]."
    hide sasha
    if not "kleio" in GIRLS:
        show screen message(title="Patreon Edition",what="Kleio & Anna are only available in the Patreon Edition of the game.\nVisit {a=https://www.patreon.com/Andrealphus}patreon.com/Andrealphus{/a} to become a patron and get to know them better.")
        pause
        hide screen message
    return

label sasha_event_01:
    scene bg bedroom1
    "I hear a sound outside, and look out my window."
    show sasha swimsuit
    "I see Sasha, lounging by the pool."
    sasha.say "[hero.name]! Come on down!"
    scene bg bedroom1
    hide sasha
    "I have got nothing to do, so..."
    scene bg pool
    show sasha swimsuit happy
    if not sasha.get_flag_value("greeting"):
        sasha.say "Hi, [hero.name]!"
        hero.say "Hi, Sasha."
        $ sasha.set_flag("greeting",True,1)
    "I stop and I can’t help but stare at Sasha lounging there in nothing but her tiny bikini, her naked skin gleaming in the sun..."
    sasha.say "Come on over here and sit with me!"
    menu:
        "No, thank you.":
            hero.say "No, thank you."
            show sasha angry
            $ sasha.love -= 1
            "I stand there awkwardly, not knowing what else to do; Sasha looks disappointed."
            return
        "If that is what you want, then yes!":
            hero.say "If that is what you want, then yes!"
            $ sasha.sub -=1
            "I approach Sasha, and then sit at her feet and look up at her, waiting expectaqntly for what she might say."
            hero.say "So, Sasha, what can I do for you?"
        "Okay.":
            hero.say "Okay."
            show sasha swimsuit happy
            $ sasha.love +=1
            "I walk over and sit beside Sasha, giving her a smile as I sit down beside her."
            hero.say "So, Sasha, how are you?"
        "Well, I like that!":
            hero.say "Well, I like that!"
            $ sasha.sub +=1
            show sasha blush
            "I give her a smile, then walk over and sit by her shoulder on the chair, looking down at her friendly face. Struck by an impulse, I reach down and toy with her hair a bit."
    hero.say "So, Sasha... what is it you wanted to talk to me about?"
    show sasha swimsuit happy
    "She looks up at me with a wide smile, her eyes alight and eager."
    sasha.say "Well, [hero.name], how are you doing?"
    hero.say "Oh, I’m fine. How are you?"
    show sasha swimsuit sad
    "She shrugs, looking a little lost, as if she is looking for something, something to make a difference, to change things."
    hero.say "Hey, is there something wrong?"
    sasha.say "No, no. Nothing’s wrong."
    "Somehow, the way she said that, I thought there must have been a ‘but’ just waiting to be said."
    hero.say "Well, than, is there something that could be better?"
    show sasha swimsuit normal
    "She hesitates, as if startled, then put off, then she starts really thinking about the question, her face scrunched up ina cute way, her brows furrowed, clearly she is taking the question very seriously."
    sasha.say "Well... I- that is, sometimes I get the feeling that there should be more, more going on, I mean, something happening to change things, to move life forward."
    hero.say "Oh, come one- you’re here, Sasha! That makes a big change!"
    show sasha swimsuit happy
    "She laughs cheerfully, and I can’t help but admire the curve of her jaw, and the way her breasts move with her laughter."
    hero.say "So- do you have anything going on? If you need something to make something happen, I’d be happy to help!"
    sasha.say "No, not much at all is going on, [hero.name] - but..."
    "She stops, looking a little anxious."
    sasha.say "But, if you want to - that is, in fact, I was hoping that maybe you could suggest something to do!"
    "Well, I think to myself, how can I respond to that?"
    menu:
        "I’m sure you can think of something to do.":
            hero.say "I’m sure you can think of something to do."
            show sasha swimsuit normal
            $ sasha.love -= 1
            "She looks up at me, and sits still for a long moment, then smiles."
            sasha.say "Yes, I’m sure, too."
        "I can think of games we could play.":
            "I reach down and coil a finger in her hair, staring down into her eyes with a tight smile."
            hero.say "I can think of some games we could play."
            show sasha swimsuit blush
            $ sasha.sub +=1
            "She looks up, meetiong my eyes; she is silent for a long moment, then smiles, her eyes shining."
            sasha.say "Sure, I’d love to play some games with you."
        "I would love to do whatever you want.":
            hero.say "I would love to do whatever you want."
            $ sasha.sub -= 1
            "I look at her expectantly, waiting for whatever she wants - Sasha looks at me with a dark, thoughtful eyes. She cocks an eyebrow, and smiles."
        "Sure, I can think of things we could do together.":
            hero.say "Sure, I can think of things we could do together."
            show sasha swimsuit blush
            $ sasha.love += 1
            "I reach down and take her hand, and hold it with a smile. Sasha looks down at my hand in hers, then looks to meet my smile with one of her own."
    sasha.say "Well, maybe we can do something together, go somewhere - are there any good places to go around here?"
    hero.say "Yeah, there are some good places to go, but actually..."
    "I stop, not sure how to go on, how to say this. I feel a strong desire, an undeniable urge, but I am not sure how to say it, to talk about it."
    hero.say "...but, actually, I would like to spend some time with you here, not going anywhere, just getting to know each other."
    "I watched her eyes light up eagerly, and I felt something like- like I needed to be careful, because I could make her happy, or I might make her sad, and I should be careful."
    sasha.say "Oh, that would be great!"
    hero.say "How about we go inside?"
    sasha.say "Oh, yeah, that would be great!"
    scene bg livingroom
    show sasha normal
    sasha.say "So, [hero.name] what places are there to go around here?"
    hero.say "Well, let’s see, there’s- uh... a movie theater and a pub, there’s a bakery if you like things fresh; a bookstore, coffeeshop and an arcade at the mall..."
    sasha.say "*giggle!* So there’s plenty of things to do around here; there are lots of options!"
    hero.say "Yeah, that’s right."
    sasha.say "Well, would you take me out and show me some of them? Maybe we could go out and do something together?"
    menu:
        "Nah, that doesn’t sound like a good idea.":
            hero.say "Nah, that doesn’t sound like a good idea."
            show sasha swimsuit sad
            $ sasha.love -= 1
            "The moment I said the words, I could see the affect of them. Her smile falters a little, her shoulders slump."
            sasha.say "Well, all right, if you don’t think that would be a good idea..."
            return
        "I want you to come and do it with me.":
            hero.say "I want you to come and do it with me."
            $ sasha.sub +=1
            show sasha swimsuit blush
            "She giggled, and almost dropped into a curtsy, looking up at me playfully."
            sasha.say "Alright, if that’s what you want!"
        "Whatever you want to do is just fine with me.":
            hero.say "Whatever you want to do is just fine with me."
            $ sasha.sub -= 1
            "I lower my head, glancing up at her form under my brows, waiting for the answer she would give; Sasha seems to almost puff up, looking at me with a superior smile."
            sasha.say "Very good, I’m glad to hear that!"
        "Yeah, I’d love to do something together with you.":
            hero.say "Yeah, I’d love to do something together with you."
            show sasha swimsuit happy
            $ sasha.love += 1
            "I look at Sasha and smile as I say it; she meets my gaze with a smile of her own."
            sasha.say "Yeah, I think it would be great to do things together!"
    hide sasha
    return

label sasha_event_coffee:
    scene bg coffeeshop
    show sasha
    sasha.say "Gee, [hero.name] thanks for suggesting we go here! It looks like a great place, and the coffee’s real good, too!"
    menu:
        "Nah, it’s not that good.":
            hero.say "Nah, it’s not that good."
            $ sasha.love -= 1
            "Sasha smiles weakly, and takes another sip of her coffee."
            sasha.say "Well, okay, if you say so."
        "Very good, you should have some of the pastries too, you will like them." if sasha.sub > 25:
            hero.say "Very good, you should have some of the pastries too, you will like them."
            show sasha blush
            $ sasha.sub += 5
            "Sasha smiles and ducks her head, meeting my eyes for a moment, then looking down with a little smile."
            sasha.say "Okay, I will, thank you."
        "I’m so happy that it pleases you." if sasha.sub < -25:
            hero.say "I’m so happy that it pleases you."
            show sasha normal
            $ sasha.sub -= 5
            "Sasha takes anothe sip of her cooffee, looking at me from under her eyebrows with a knowing look and a little satisfied smile, pleased with my response."
            sasha.say "Very good, I’m glad to hear that!"
        "Good, I’m glad you like it." if -25 <= sasha.sub <= 25:
            hero.say "Good, I’m glad you like it."
            $ sasha.love += 1
            "I meet Sasha’s eye and smile as I say it; she meets my gaze with a smile of her own, then takes another sip of her coffee."
    sasha.say "So, [hero.name] do you come here often?"
    hero.say "Well, maybe not as often as I would like to."
    sasha.say "Oh? What does that mean?"
    hero.say "Well, I don’t have many people I can take here, so I haven’t had a good reason to come here."
    "Sasha laughs, and I watch her hair play as she tosses her head back. It makes me smile."
    sasha.say "Hey, maybe I could be your reason to come here."
    menu:
        "You and I will come her again very soon." if sasha.sub >= 25:
            "I fix her with a commanding eye and smile."
            show sasha blush
            "You and I will come her again very soon."
            $ sasha.sub += 5
            hero.say "You and I will come her again very soon."
            "Sasha giggles, her eyes alight."
            sasha.say "Yes."
        "I would love to do that; anything you want." if sasha.sub <= -25:
            "I smile and nod my head."
            show sasha normal
            hero.say "I would love to do that; anything you want."
            $ sasha.sub -= 5
            "Sasha looks at me with, her hands clasped on the table before her, and she smiles, her eyes piercing into mine."
        "Actually... I don’t know that I have time for that, really. Sorry.":
            hero.say "Actually... I don’t know that I have time for that, really. Sorry."
            show sasha normal
            $ sasha.love -= 5
            "I shrug helplessly, not knowing what else I can say. Sasha stares at me in silence for a moment, and then she shrugs in return."
        "Is that a come-on?" if -25 <= sasha.sub <= 25:
            hero.say "Is that a come-on?"
            $ sasha.love += 1
            "I raise an eyebrow, giving Sasha a surprised smile. She grins back at me."
            sasha.say "What do you think?"
    hide sasha
    return

label sasha_event_03:
    "We walked home together, looking around at things as we went, not looking at anything in particular, just looking."
    "We talked as we walked, again, not about anything in particular. Just talking."
    "When we reach the house, Sasha stops and turns and leans her back against the wall, looking up at me with a smile."
    sasha.say "I had a lovely time tonight."
    if sasha.sub <= -10:
        hero.say "Good, I’m happy I was able to entertain you."
        $ sasha.sub -= 1
        "I stand quiet, waiting for her response; Sasha stares at me for a long moment, then smiles. She reaches up and caresses my cheek affectionately."
        sasha.say "Good boy."
        "She smiles at me with a strange fiery glint in her eyes that makes my stomach tremble, but a heat rises in my cheeks, and I find myself smiling back."
        "She pats my cheek again, then turns and strides in pausing in the doorway to glance expectantly over her shoulder at me, then turns and goes in."
        "My heart hammering, my mouth dry, I hurry after her."
    elif sasha.sub >= 10:
        hero.say "Good. I will take you out again."
        $ sasha.sub += 1
        "As I say it, I look down at Sasha, and she stares up at me, her eyes wide at my pronouncement. I raise my hand and clench her jaw in a gentle grip."
        "She smiles, closing her eyes as I caress her delicate jaw. Sasha moans softly, almost nuzzling my hand."
        show sasha kiss
        "I raise her chin as I lean down to press my lips to hers in a long soft, gentle kiss."
        "Sasha surrenders to me, kissing me back, moaning softly into my lips as i taste her, as I take her."
        "I break it off, and look her closely as she slowly opens her eyes to look up into mine."
        hero.say "Come on inside."
        "I take her by the hand and lead her inside with me."
    elif sasha.love >= 50:
        hero.say "I’m glad you did."
        $ sasha.love += 1
        "I smile as I say it, and she smiles back at me, the moonlight shining on her cheek."
        "She reaches up and cups my cheek with her hand, going up on her toes to reach up and kiss me on the cheek."
        "She looks me in the eye, her smile turning slightly sultry."
        " walk up to join her, and take her hand in mine. She looks up at me, and I look down at her, then we walk in together."
    else:
        hero.say "Good."
        $ sasha.love -= 1
        "I nod absently as I say it, and Sasha looks at me quietly for a moment, then nods herself, then she turns and walks in, and I walk in behind her."
    hide sasha
    return

label sasha_event_04:
    scene bg livingroom
    show sasha
    "Sasha is sitting on the couch."
    sasha.say "So, [hero.name], do you have any family around here? Anyone you could call on if you needed help."
    menu:
        "Nope. Just you!":
            hero.say "Nope. Just you!"
            $ sasha.love += 1
            "I grin as I say it, trying to make a joke out of it, but also perhaps thinking that she might take it well."
            "Sasha grins back at me, then leans over the arm of her chair toward me."
            sasha.say "Well, if you're ever in need, just call on me!"
        "I'm more of the giving help and taking care type; I've never needed help.":
            hero.say "I'm more of the giving help and taking care type; I've never needed help."
            $ sasha.sub += 1
            "I say it with a tight, controlled smile, watching Sasha carefully to gauge her reaction."
            "Sasha smiles and looks down, then raises her eyes to glance up at me."
            sasha.say "Well, if I ever need help then, I know who to ask for it."
        "Yes, which is good for me, because I sometimes really need help.":
            hero.say "Yes, which is good for me, because I sometimes really need help."
            $ sasha.sub -= 1
            "Sasha leans back in her chair, looking at me with a long, quiet, thoughtful look and gives me a tight smile."
            sasha.say "Well, if you ever need help, I'll be there to give it to you."
        "No, but that's okay, because I don't need anyone to be there for me.":
            hero.say "No, but that's okay, because I don't need anyone to be there for me."
            $ sasha.love -= 1
            "Sasha nods, her expression blank."
            sasha.say "Okay, fine. Good for you."
    hide sasha
    return

label sasha_event_05:
    scene bg kitchen
    show sasha
    hero.say "Do you want something to drink? Some coffee or tea or something?"
    sasha.say "Sure, I'd love some juice."
    "I pour Sasha some juice."
    sasha.say "So how come you've never made a move on me before?"
    menu:
        "I never wanted to before, but now...":
            hero.say "I never wanted to before, but now..."
            $ sasha.love += 1
            "I cock my head to the side and say it with a smile, and Sasha returns it with a smile of her own."
            "She raises her glass to her lips and takes a drink, her sultry eyes glancin at me over the rim."
        "It didn't seem important to me.":
            hero.say "It didn't seem important to me."
            $ sasha.love -= 1
            sasha.say "Mhmm."
            "Sasha nods, then takes a drink from her juice, throwing her head back, then turning away as she lowers her glass."
        "I was waiting for a time of my choosing.":
            hero.say "I was waiting for a time of my choosing."
            $ sasha.sub += 1
            "I say it with a tight smile, staring intently into her eyes as I say the words, low and clear."
            "Sasha smiles, a little anxiously, a flush rising in her cheeks, and she raises the glass and takes a drink to cover herself, but she can't quite tear her eyes away from mine."
        "I didn't want to offend you; I thought if you wanted it, you would make the first move.":
            hero.say "I didn't want to offend you; I thought if you wanted it, you would make the first move."
            $ sasha.sub -= 1
            "Sasha smiles as I say it, her piercing eyes staring intensely into mine."
            "Her lips curved in an arch smile, she raises the glass to her lips and takes a modest sip, never taking her eyes from mine."
            sasha.say "Smart boy."
    hide sasha
    return

label sasha_sub_event_1:
    scene bg kitchen
    show sasha
    "I take a long step closer to Sasha, then I reach out and put my hand on her arm, leaning close, I lower my face to hers-"
    sasha.say "Wait."
    "She raises her hand, pressing a finger to my lips."
    sasha.say "What is it you want, exactly?"
    "I smile down at her, my eyes staring into hers."
    hero.say "I want you."
    "I can feel my heart pounding in my chest as I tighten my grip on her, not to let her escape."
    hero.say "I want to have you, to hold you, to take you and pleasure you and use you, and make you happy."
    show sasha happy
    sasha.say "Why- that’s-"
    hide sasha
    show expression "sasha kiss "+sasha.get_clothes()
    "I cut off her words with a kiss, holding her against me, I press my lips to hers in a hot fiery passion, lips and tongue working at her- she freezes, then melts against me, going from cold to hot in my arms, her breasts pressed against me, her lips and tongue working at mine."
    "She moans as I run my hands over her, brushing her breasts, her hips and ass, caressing her hot body, pinching and squeezing her in all the right places."
    "We break apart, and I look down into her face. Then she opens her eyes to meet mine."
    hide expression "sasha kiss "+sasha.get_clothes()
    show sasha blush
    sasha.say "So what do you want from me?"
    "I smile, knowing that she is now mine."
    hero.say "I want you to kneel for me, Sasha."
    "I lay my hand on her chin and raise her head to look up at me; she stares almost worshipfully at me, waiting patiently, submissively, for whatever I choose."
    hero.say "You are mine, now, Sasha. my slave, my servant. I claim you."
    hero.say "Your body is mine, your soul is mine; I will use you and toy with you and tease you and pleasure you."
    sasha.say "These are yours. . . Master. I give them to you, I surrender to you. Take me!"
    "I reach down and grab her breasts, squeezing and kneading them, - Sasha moans as my fingers sink into her soft flesh, her face growing red, her breath coming faster while her nipples grow hard."
    "I lean down further and kiss her again as I slip a hand lowers, down into her panties."
    "She moans as I caress her, running my fingers over her tight little pussy; she trembles as I take her in my arms and raise her up, then turn toward the bedroom, carrying her away."
    hide sasha
    scene bg bedroom1 with fade
    call sasha_normal_fuck from _call_sasha_normal_fuck_1
    return








label sasha_event_bree_shower:
    "I'm lying in bed, just scrolling through some mindless crap on my phone when I hear the first of the hushed giggles coming from outside the door."
    "Unable to tell if it's Bree or Sasha that's finding something so funny that she just can't keep it in, I slide off the bed and sneak to my door and open it just enough to glance out."
    "My reward is to catch a fleeting glimpse of Sasha as she flits into the bathroom and then looks back over her shoulder."
    "She beckons with a crook of her finger to someone still unseen, and then Bree appears, apparently answering the summons."
    "There are more giggles, slightly nervous in tone from Bree and downright wicked from Sasha."
    "And then they disappear behind the closed bathroom door, leaving me more than a little intrigued as to just what's going on in there."
    "Now I find myself in a terrible dilemma, as I know that you could argue I have absoloutely no right to see whatever the girls are up to."
    "But on the other hand, I do live in this house too, and I have a right to know if the dynamics between us are about to change in a significant manner."
    "In the end, I tell myself that we're a pretty open and honest household, sharing things like groceries and splitting the bills three ways."
    "So they'd probably be okay with me knowing what's going on in one of the communal areas of the house, right?"
    "Before my conscience has a chance to protest at the shakiness of my logic, I sneak out of my bedroom and across the hallway to the bathroom door."
    show bg secondfloor
    "Crouching down and trying to keep as quiet as I can, it seems that I'm in luck, as the bathroom door isn't fully shut."
    "There's just enough of a gap for me to be able to peek inside and get a fairly good look at what Bree and Sasha are up to in there."
    show bg bathroom
    "I can hear the sound of water running in the background and see the steam fogging both the mirror on the wall and the glass of the shower cubicle."
    "But the sight of Bree and Sasha stripping the last few items of clothing off of each other is more than enough to make all else seem unimportant right now."
    show gog
    "Sasha seems to be taking the lead, grinning in delight as she pulls down Bree's panties."
    "Bree herself looks more shy and embarrassed at what they're doing, her cheeks flushed from more than the heat rapidly building up in the bathroom."
    "A part of me can't believe what I'm actually seeing here."
    "The two incredibly hot girls that I'm sharing a house with are genuinely sneaking around to take a shower together!"
    "And what's more, I'm about to get a front row seat to watch the whole thing!"
    "Just as I'm congratulating myself on not only seeing Bree and Sasha naked, but also the prospect of watching them soap each other up, everything changes in an instant."
    "Sasha's smile changes from wicked to something visibly more tender, and she cranes her neck forward to kiss Bree gently."
    "The other girl shivers a little at first, but then begins to return the kiss with a growing measure of passion."
    "Still with their lips locked together, Sasha puts her hands on Bree's hips, walking her backwards into the falling water of the shower."
    "I feel my mouth grow suddenly dry, realising that I'm seeing something that most guys could only dream about witnessing."
    "Luckily for me, Bree and Sasha are both far too engrossed in what they're doing to even think about closing the door of the shower cubicle."
    "And the steam rising as the water falls only serves to cover their naked bodies in a film of moisture that makes the whole thing that much more enjoyable to watch."
    "Their passionate kiss endures until Sasha runs her hand over Bree's body, down her belly and then between her slick thighs."
    "A moment later, Bree breaks the kiss as she tilts her head back and begins to moan audibly at what Sasha's doing to her down there."
    "Though I can't see her fingers for Bree's thighs, it's clear to see that Sasha is engaged in the act of stroking, rubbing and probing to great effect."
    "Bree sinks back against the wall as Sasha teases her more with each second that passes."
    "But then she arches her back and pushes herself away again upon her elbows."
    "And from the expression on her face, I can only guess that one or more of Sasha's fingers is now deep inside of her."
    "Bree begins to almost jump on the spot, as though she can't take the sensations that she's feeling right now."
    "This sets her chest to bobbing up and down in sympathy, the sight made all the more impressive by the way the water rushes over them and covers them with droplets."
    "I can't see Sasha's face as well as I can Bree's, though I can clearly see that she's every bit as turned on by her own actions as is the girl receiving them."
    "Denied the chance to kiss Bree's lips for a second time by the way her head is cast back, Sasha bows down and begins to lick at her nipples instead."
    "Rather than causing Bree's chest to move less than before, this only serves to make her writhe and thrash as Sasha even takes her nipples between her teeth and nips at them hungrily."
    "Finally, Sasha goes lower still, sliding downwards until she's kneeling in front of Bree in the bottom of the shower cubicle."
    "She doesn't allow enough time for the other girl to regain even a small amount of her composure."
    "Instead she leans quickly forward, and I see the briefest glimpse of her tongue as it darts towards Bree's already much aroused pussy."
    "Honestly, I don't know which one of the girls is turning me on more, as I feel my cock straining against my shorts at the sight of all this."
    "Bree's show of arousal and her naked body being shown off in all of its glory is a memory that'll stay with me for a long, long time."
    "But the sheer tenacity and technique that Sasha's putting into producing all of that arousal makes me long for the same treatment myself."
    "I'm pretty sure that from the way she's shaking and biting her bottom lip, Bree won't be able to hang on in there much longer."
    "And I'm proven right just a few moments later, as she literally gasps and clasps the side of Sasha's head with both of her hands."
    "Still yelping and twitching from the strength of her orgasm, Bree only just manages to guide Sasha's head away from her groin with shaking arms."
    "Now that the whole thing is over, the spell that it momentarily cast over me seems to vanish."
    "I realise that I'm only a couple of metres away from Bree and Sasha, watching this intimate moment without a shred of excuse or permission."
    "This sends me darting back to my bedroom and hopping under the covers, all too aware of my still painfully erect cock."
    "Taking it in the palm of my hand, I close my eyes and try to summon a mental image of what I've just seen."
    "But I already know that whatever I can pull out of my memory, it won't even come close to the sight of the real thing just now."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
