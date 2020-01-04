init python:

    Event(**{
        "name":"palla_init",
        "label": ["palla_init"],
        "girls_conditions": {"palla":{"flag_story":False}},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name":"palla_start",
        "label": ["palla_start"],
        "girls_conditions": {"palla":{"flag_story":False}},
        "game_conditions": {"done":["palla_event_02","palla_init"]},
        "priority": 1000,
        "do_once": True,
        "quit": False,
        })

    Event(**{
        "name": "palla_give_christmas",
        "label": ["palla_give_christmas"],
        "duration": 0,
        "game_conditions":{"date":"christmas"},
        "girls_conditions": {"palla":{"min_love":50,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "palla_give_birthday",
        "label": ["palla_give_birthday"],
        "duration": 0,
        "game_conditions":{"date":"birthday"},
        "girls_conditions": {"palla":{"min_love":40,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "palla_give_valentine",
        "label": ["palla_give_valentine"],
        "duration": 0,
        "max_girls": 1,
        "game_conditions":{"date":"valentine"},
        "girls_conditions": {"palla":{"min_love":100,"present":True, "flag_female":0, "valid":True}},
        "once_day": True,
        "do_once":False,
        "quit": False
        })

    Event(**{
        "name": "palla_event_02",
        "label": ["palla_event_02"],
        "duration": 1,
        "game_conditions":{"room":["clothesshop"], "min_charm":50, "done":'palla_event_01', "flag_female":0},
        "do_once": True,
        "quit": True
        })

    Event(**{
        "name": "palla_event_03",
        "label": ["palla_event_03"],
        "duration": 1,
        "girls_conditions": {"palla":{"min_love":40}},
        "game_conditions": {"room": ["coffeeshop"], "done": 'palla_event_02'},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_04",
        "label": ["palla_event_04"],
        "duration": 0,
        "girls_conditions": {"palla":{"min_love":80, "contact": True, "present": False}},
        "game_conditions": {"hours":(0, 1), "done": 'palla_event_03', "flag_dateinprogress":0},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_05",
        "label": ["palla_event_05"],
        "duration": 0,
        "girls_conditions": {"palla":{"flag_nokiss":False, "present":True}},
        "game_conditions": {"done": 'palla_event_04', "flag_dateinprogress":0},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_06",
        "label": ["palla_event_06"],
        "duration": 0,
        "girls_conditions": {"palla":{"gaveflowers":True, 'gavesweets': True, "min_love": 120, "flag_nodate": True, "flagmax_datetries": 3, "present":False, "flag_event6done": False}},
        "game_conditions": {"done": 'palla_event_05', "hours":(23, 24), "flag_dateinprogress":0},
        "do_once": False,
        "quit": True
    })

    Event(**{
        "name": "palla_event_07",
        "label": ["palla_event_07"],
        "duration": 0,
        "girls_conditions": {"palla":{"flag_talksex":True, 'present': True}},
        "game_conditions": {"flag_dateinprogress":0},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_08",
        "label": ["palla_event_08"],
        "duration": 0,
        "girls_conditions": {"palla":{"min_sub":70, "min_love": 200, 'present': False}},
        "game_conditions": {"hours":(0, 1), "done": 'palla_event_07', "flag_dateinprogress":0},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_09",
        "label": ["palla_event_09"],
        "duration": 0,
        "girls_conditions": {"palla":{'present': False}},
        "game_conditions": {"days": "1245", "hours":(0, 4), "done": 'palla_event_08', "flag_dateinprogress":0, "room": ["nightclub"]},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_10",
        "label": ["palla_event_10"],
        "duration": 0,
        "girls_conditions": {"palla":{'present': False}},
        "game_conditions": {"done": 'palla_event_09', "flag_dateinprogress":0, "room": ["electronic"]},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_11",
        "label": ["palla_event_11"],
        "duration": 0,
        "girls_conditions": {"palla":{'present': False, "countermin_shawnencounter": 2}},
        "game_conditions": {"hours": (20, 24), "done": 'palla_event_09', "flag_dateinprogress":0, "room": ["map"]},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_12",
        "label": ["palla_event_12"],
        "duration": 0,
        "girls_conditions": {"palla":{'present': False, "countermin_pallavisit12": 7}},
        "game_conditions": {"hours": (20, 24), "done": 'palla_event_11', "flag_dateinprogress":0, "room":['livingroom']},
        "do_once": True,
        "quit": True
    })

    Event(**{
        "name": "palla_event_12_fix",
        "label": ["palla_event_12_fix"],
        "duration": 0,
        "game_conditions": {'done': 'palla_event_12'},
        "do_once": True,
        "quit": False
    })

    Event(**{
        "name": "palla_mall_date_fuck",
        "label": ["palla_mall_date_fuck"],
        "priority": 500,
        "duration": 0,
        "girls_conditions": {"palla":{"present":True, "flagmin_sex": 2}},
        "game_conditions":{"activity":"date_go_shopping", "room":["date_mall"]},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "palla_mall_date_fuck_02",
        "label": ["palla_mall_date_fuck_02"],
        "priority": 500,
        "duration": 0,
        "girls_conditions": {"palla":{"present":True, "flagmin_sex": 2}},
        "game_conditions":{"activity":"date_go_shopping", "room":["date_mall"], 'done':['palla_mall_date_fuck']},
        "do_once":False,
        "quit": True
        })

    Event(**{
        "name": "palla_audrey_date",
        "label": ["palla_audrey_date"],
        "priority": 500,
        "duration": 0,
        "girls_conditions": {"palla":{"present":True, "min_love":160, "flagmin_lesbian":10}, "audrey": {"min_love": 140, "flagmin_sex": 1, "flagmin_lesbian":10}},
        "game_conditions":{"activity":"date_eat_restaurant", "room":["date_highclassrestaurant"], "done": ['palla_event_08']},
        "do_once":True,
        "quit": True
        })

    Event(**{
        "name": "palla_fix",
        "label": ["palla_fix"],
        "game_conditions": {},
        "do_once": True,
        "quit": False,
    })
    Event(**{
        "name": "palla_event6_fix",
        "label": ["palla_event6_fix"],
        "conditions": ["'palla_event_06' in DONE", 'palla_love_max >= 160', 'not palla.get_flag_value("event6done")'],
        "priority": 1000,
        "do_once": True,
        "quit": False,
    })

label palla_event6_fix:
    $ palla.set_flag('event6done')
    return

label palla_fix:
    python:
        palla_love = 0
        palla_sub = 0
        palla.set_flag('lesbian', 0)
        palla.set_flag('kiss', 0)
        palla.set_flag('pregnant', 0)
        palla.set_flag('sex', 0)
        palla.set_flag('birthdayknown', False)
        palla.set_flag('nodate', True)
        palla.set_flag('nokiss', True)
        if 'palla' in hero.smartphone_contacts:
            hero.smartphone_contacts.remove('palla')
        piercings = palla.get_piercings()
        for type in ['nose', 'clit', 'nipples']:
            piercings[type]['pierced'] = False
        reset_events = ['palla_event_01', 'palla_event_02', 'palla_init', 'palla_start']
        for event_name in reset_events:
            if event_name in DONE:
                DONE.remove(event_name)
    return

label palla_start:
    $ palla_love_max = 40
    $ palla_sub_max = 60
    $ palla.set_flag('pill', True)
    if "palla" in HIDDEN:
        $ HIDDEN.remove("palla")
    return

label palla_event_02:
    "While I do my shopping, I hear a somewhat familiar voice."
    unknown_girl_say "Hey, [hero.name], if you’re here, you must have some taste, after all."
    "I can’t quite place it, so I turn around, and there is Palla, standing there, looking over a few outfits."
    show palla teaser
    palla_say "Think you could do me a favor? This dress would work perfectly with the shoes I just got."
    palla_say "Since you and Audrey work together, I know you have the money to help a girl out."
    hero.say "Wait, are you, asking me to pay for your clothes for you?"
    palla_say "What? Are you not a gentleman? I guess I could just tell Audrey what an ass you are, for not helping out a girl in need."
    menu:
        "Pay" if hero.money >= 100:
            "Looking at the price, it’s not that bad. And besides, getting on Palla’s good side might actually be a bonus."
            hero.say "Who says I’m not a generous gentleman? Sure, I’ll pay for you. Anything for a friend."
            palla_say "Oh, are we friends, now? I think I’ll go change into this and see how it goes."
            palla_say "Just go over there and pay for it, but don’t you dare go sneaking into the dressing room."
            palla_say "This place has terrible security, you know. No one would ever know."
            hide palla
            "She walks off towards the back and to the dressing rooms."
            "It’s a quick transaction as I tell the cashier what I want."
            "She looks totally bored out of her mind and has her face buried in her phone."
            "Wow, Palla was right."
            "Security here is really lax, and even though I was so nice to her, she was still being a bitch."
            $ hero.money -= 100
            $ palla.set_flag('storepaid', True)
            $ pay = True
        "Don’t Pay":
            hero.say "What the hell? You want me to pay for your clothes?"
            palla_say "Of course, you are a gentleman, aren’t you?"
            hero.say "That doesn’t mean I’m going to give you free clothes, you cheapskate!"
            "Palla sighs and turns away from me, only to give me a glance over her shoulder for a narrow, smouldering eyes."
            palla_say "Well, I’m just going to the dressing room now, and take a look at myself in this dress."
            palla_say "You’d better not take advantage of the store’s terrible security and follow me in there, you creep!"
            hide palla
            "With that, she storms off, leaving me dumbfounded for a moment. Did she… did she actually want me to go in?"
            $ pay = False
            $ palla.set_flag('storepaid', False)

    menu:
        "Leave":
            "What the hell is that woman’s deal?"
            "She’s totally ruined my mood with her bitchiness."
            "Might as well head home."
            "There’s no way I can think straight while she’s around here..."
            return
        "Go in":
            if pay:
                "Well, I’ve paid for the dress, right? I suppose its only fair I get to see her in it."
                "I slip casually away from the cashier and make my way to the dressing rooms, grabbing a random pair of pants along the way to avoid suspicion."
            else:
                "That uptight fashionista thinks she can get away with bossing me around, does she?"
                "Well, I’ve gone too high up the corporate ladder to be someone’s lackey. Seems I need to teach her a lesson."
                "I storm off towards the dressing room, yanking off a random pair of pants, though my annoyance is probably clear to anyone who might be watching."
                "Here’s hoping security is as bad as Palla claimed it was..."
            "Once inside, I can clearly see that there is only one unit occupied."
            "That’s my target."
            "The door pushes open with no lock, and on the other side is Palla, staring wide-eyed at me, still wearing her glasses, but otherwise stripped down to stylish underwear."
            "She holds the dress up against her, as if trying to hide from me, yet drops it immediately."
            palla_say "W… what are you doing? You can’t be in here!"
            hero.say "Are you complaining?"
            palla_say "Of course I am, you ass!"
            hero.say "Then, go on, raise your voice if you don’t want me in here."
            "She stares at me a moment, her eyes catching onto my own. For a brief moment, she even bites her lip."
            palla_say "Don’t you dare force me against the wall and fuck my ass, you sicko!"
            hero.say "Oh, alright, I guess I’ll just leave, then."
            "Her eyes widen at that, her jaw dropping."
            palla_say "Hey, what are you-?"
            "I need to get rid of this frustration, and it seems she really wants me frustrated, so I grab her head and push her up against the mirror, her glasses sliding awkwardly off her face and her cheek squished against the glass."
            hero.say "Last chance to back out, if you don’t really want this,"
            palla_say "Fuck you, asshole. Don’t you dare do it!"
            show palla stand
            "I unzip my pants with my free hand, and she stares at my reflection as I hold her down."
            "Obviously, she could push against me, fight back, and call for help."
            "I do everything I can to make sure I’m not really harming her."
            "She’s a bitch, but I’m not a monster."
            "I could just as easily get my rocks off at home as with her."
            "No, I have to make sure she wants it."
            "It’ll make it all the sweeter."
            "I let go of her head, and she holds onto the wall, not pushing away."
            "Her ass sticks out for me, and I take my now free hands and run them down along her sides, hooking my thumbs in the hem of her underwear, and I pull them down."
            "Already, there’s a bit of sticky wetness on them."
            hero.say "And you’re the one who called me an asshole,"
            hero.say "You know, I’d love to fuck you right now, but you’d want that, wouldn’t you?"
            hero.say "No, I think I’ll take what you said you don’t want."
            "She remains against the window as I grip her cheeks, pulling them apart, and giving myself a great view of her asshole."
            palla_say "Whatever you do... please, please, don’t fuck my ass."


            "I then slide my cock over her, the head pressing against her tight hole."
            "Her eyes roll back, certainly not the signs of a woman who really didn’t want this to happen, but I wasn’t going to get rid of her illusion."

            "That only adds to the excitement as I spread her apart with my dick, thrusting into her and grunting with each little bit I go deeper into her."

            palla_say "Y-you call this assault? You’re-You’re not very good at this, are you!?"

            show palla stand wet
            "Her pussy drips with desire as my cock disappears into her ass with each thrust forward."
            "She stares, transfixed at the situation before her, and bites her lip as she watches, a deep blush going over her face."
            "She grunts with each thrust, her fingers curling against the mirror, nails scratching at the surface."
            palla_say "C… Come on… you you! Can! Do! More! Than! That!"
            "I pick up the pace as she taunts me, closing my eyes shut and gritting my teeth as I bury my face against her back."
            "I plow into her, and she smashes against the window again, our fucking thumping against the mirror, making the flimsy walls of the dressing room quake underneath of rough ride."
            show palla stand wet pleasure
            "She bites her lip as she holds back her groan of pleasure, and I feel the spasms around me as she reaches her climax."
            "I too unleash into her, filling her with my cum."
            "I pull out, and she dribbles down onto the floor, falling against the mirror and gasping for breath."
            show palla stand wet smile
            palla_say "F… fuck… [hero.name], you’re an animal. But you’d better get out of here."
            "She pulls her pants up."
            palla_say "If they discover what we did, we won’t be allowed back in the store…!"
            $ palla.set_flag('storeanal', True)
            $ palla.sub += 2
    return

label palla_event_03:
    "When I walk in, I see Palla just stepping away from the counter, fresh coffee in hand. She looks at me and narrows her eyes."
    show palla normal casual
    if palla.get_flag_value('storeanal'):
        palla_say "Hey asshole, we need to talk."
        show palla angry
        "She looks angry, but there is also something else."
        hero.say "Fine."
        "We walk over to a table and she sits across from me. I feign ignorance and put on my best poker face."
        hero.say "What do you want to talk about?"
        palla_say "Don't give me that, asshole. You know what I want to talk about."
        if palla.get_flag_value('storepaid'):
            hero.say "Um, you want to thank me for buying that dress?"
            "Palla shifts a bit and actually looks a little flustered, but recovers herself."
            palla_say "No, I think I you already got thanked for that. Asshole."
            "I think she smiled just a little as she said \"Asshole\"."
        hero.say "Ah, you want to talk about your asshole?"
        show palla blush
        palla_say "No! I mean, actually, kind of. What you did to it!"
        "I smile a little and lean forward. "
        hero.say "Oh, you mean when I made you scream for more?"
        "I didn't think she could blush more, but she does. I actually think she's turned on just talking about it."
        palla_say "No! I mean, ugh, you're such a dick. You should apologize."
        menu:
            "Apologize":
                hero.say "You want me to apologize for giving you exactly what you asked for?"
                palla_say "I didn't ask for it, and yes."
                "I sigh."
                hero.say "Fine. I'm sorry I fucked you in the ass. I promise I won't do it again. Unless you ask for it."
                show palla happy
                palla_say "See, that wasn't so bad!"
                "Is she serious? That was the weakest sarcastic apology I could think of."
                "She blows me a kiss and leaves the the table."
                $ palla.love += 3
            "Not a chance":
                hero.say "Not a chance, bitch! You had every opportunity. I made sure you wanted it, and trust me, you wanted it. I have nothing to apologize for. You're the one who should be apologizing to me!"
                show palla angry
                palla_say "Me, apologize to you? What the hell for?"
                hero.say "For not just asking for what you so obviously wanted!"
                "She leans over the table and points a finger at me, practically stabbing me in the nose with it."
                palla_say "If you ever do anything that again, I'll, I'll…"
                hero.say "Again? Oh that sounds kind of fun."
                show palla blush
                "She is now completely speechless and blushing furiously."
                hero.say "Sorry I interrupted you. If I do this again, you'll do what now? Get on your knees and scream for more again?"
                "Clearly at a loss for words, she gets up from the table and storms off, leaving her coffee behind."
                $ palla.sub += 3
    elif palla.get_flag_value('storepaid'):
        palla_say "Hey [hero.name], let me pay you back for that dress."
        hero.say "Oh great, thanks! It was a hundred bucks."
        show palla blush
        palla_say "Oh that's not what I meant."
        hero.say "What did you mean, then?"
        show palla normal casual
        "Palla hesitates and then mumbles,"
        palla.say "Um, something else."
        "That was weird. And I guess she did kind of suggest she wanted me to follow her in, in a kind of \"Don't throw me in that briar patch\" kind of way. I decided to press and see."
        hero.say "What, like a blow job or something?"
        show palla blush
        "She sounds angry, but she doesn't LOOK angry. In fact she looks kind of turned on."
        palla.say "No! Ew no, gross! Nothing like that! I was thinking I'd let you buy me coffee."
        hero.say "I don't see how that's paying me back."
        show palla normal casual
        palla_say "Well, I'm a famous model, and you could be seen. With me."
        "She waves a hand at the substantial crowd."
        palla_say "They'd all think you're important."
        menu:
            "I'd rather get the BJ.":
                hero.say "Yeah no, pass. I'd rather have the BJ."
                show palla blush
                if hero.grooming < 4:
                    palla_say "Ugh no! Gross! You smell like you haven't showered in a week!"
                    hero.say "Oh, is that all? What if I went and took a shower, right now?"
                    "She hesitates, just for a second."
                    palla.say "Uh, still no."
                    "She's really not convincing."
                else:
                    palla_say "Gross! No, I'm not a fucking whore!"
                    hero.say "Oh yeah? Is that why you practically begged me to follow you into the dressing room?"
                    show palla angry
                    palla_say "I told you NOT to do that!"
                    hero.say "Yeah, and why would you tell me not to do that? It's not something you'd normally expect."
                    "Palla stammered."
                    hero.say "I bet if I'd followed you in I would have gotten a lot more than a blow job!"
                    show palla blush
                    palla_say "Ugh!"
                menu:
                    "What if I said please?":
                        hero.say "What if I said please?"
                        palla_say "Still no! Asshole!"
                        hero.say "Pretty please? With sugar on top?"
                        "She rolls her eyes."
                        palla.say "Oh fuck off already."
                        "And with that she heads to the exit, but strangely she doesn't really seem angry. She gives me a look over her shoulder as she walks out, and I swear she gave me a wink just as she turned away."
                        $ palla.love += 3
                        $ palla.sub += 1
                    "Get on your knees, bitch!":
                        hero.say "Get down on your knees, bitch!"
                        show palla angry
                        palla_say "What?! Here, in public? Christ you're a fucking asshole."
                        "She gets up and storms off, leaving her coffee. But just as she's at the doorway, she looks back over her shoulder and I swear she looked at me with a mix of hunger and hate in her eyes. Then she's gone."
                        hero.say "Serves that bitch right!"
                        $ palla.love -= 1
                        $ palla.sub += 5
                    "Drop it":
                        hero.say "Fine, never mind. Are we done here?"
                        show palla sad
                        "She actually looks a mixture of embarrassed and disappointed. She mumbles something that sounds like half apology and half a curse, then gets up and leaves."
                        $ palla.love += 1
                $ palla.set_flag('owesbj', True)
            "I'd rather see more of the famous model.":
                hero.say "I'd rather see more of the famous model."
                palla_say "What do you mean?"
                hero.say "Ever done any nude modeling?"
                show palla angry
                palla_say "No! I do high fashion, catalog stuff, not pornography!"
                hero.say "Ahh, too bad. You're kind of hot, and that would totally make up for the dress."
                "She looks at me, a strange mix of intrigued and repelled on her face."
                palla_say "So what you're saying is if I give you some nudie pics, we're even?"
                hero.say "Sure!"
                "Palla shifts around uncomfortably."
                palla_say "I don't know. Are you sure you wouldn't rather have the coffee with me?"
                menu:
                    "Nope!":
                        hero.say "Nah, the pics sound a whole lot better."
                        palla_say "Uh no, no I don't think so."
                        "Palla turns to leave. As she reaches the doorway she turns and looks back at me over her shoulder. When she sees me watching her, she turns away again, embarrassed. Then she's gone."
                        $ palla.love += 2
                    "You could model in person instead, if you like":
                        hero.say "You could model in person instead, if you like!"
                        show palla angry
                        palla_say "Oh sure, first pictures, then you want me to model for you personally. Let me guess, at your place? And then what, you're going to ask to tie me up and fuck me in the ass?"
                        "Wow, where did THAT come from! She looks angry but that one came out of nowhere. Still, it sounds intriguing so I figure I ought to follow it up."
                        hero.say "Wow, that sounds hot! You'd do that? For a dress?"
                        show palla blush
                        "What? No I wasn't sugg…I mean I wasn't off…oh fuck."
                        "And then she turns and practically runs out of the store."
                        $ palla.sub += 5
                $ palla.set_flag('owesnudie', True)
            "Forget it":
                hero.say "Forget it, it's not necessary. And I'm not interested."
                show palla sad
                "Palla looks disappointed."
                palla.say "Fine."
                "And she leaves."
                $ palla.love -= 3
    else:
        palla_say "Hey [hero.name], sorry about the thing with the dress. Can I make it up to you?"
        hero.say "That depends, did you tell actually Audrey I'm an ass?"
        "She smiles a little bit, and I can't help but wonder what she's got up her sleeve."
        palla_say "Not yet, but the day isn't over."
        hero.say "Oh, so you're going to make it up to me by threatening me again? Or are you just going to call me a creep and maybe hope I follow you somewhere private and…I don't know what you expected."
        show palla blush
        "Her eyes widen a little and she starts stammering."
        palla_say "No no no that's not what I--"
        "I can't help myself, but she just got so flustered I had to take a little pity on her. Just a little."
        hero.say "Relax, Palla. What did you have in mind, then?"
        show palla casual normal
        "She takes a deep breath."
        palla_say "Well, I guess I thought I'd buy you a coffee and, um, you know, apologize."
        "I swear, it seems like she's two different people right now. On one hand, she clearly has a high opinion of herself and a low opinion of nearly everyone around her. On the other hand, she's actually decided she wants to apologize to me over something I've frankly almost forgotten."
        hero.say "Apologize for which part? Threatening me or assuming I was going to follow you into the dressing room and try to get a look at you changing into that dress?"
        show palla angry
        palla_say "Hey! Don't be an ass!"
        hero.say "Or now you could be apologizing for calling me an ass?"
        "I honestly can't tell if she's angry or aroused right now, or maybe both."
        palla_say "Oh fuck, why am I bothering with the likes of you anyway?"
        "Damn but she knows how to get under my skin. Still, I try to project the calmest demeanor I can."
        hero.say "I don't know, Palla, why are you bothering with \"the likes of me\"?"
        show palla casual normal
        "She suddenly starts talking about a mile a minute, not even taking a breath between sentences."
        palla_say "I guess because Audrey won't stop going on and on about how awesome you are and I thought I'd see what it was all about and I thought I should see what she's going on about and I don't have many friends except Audrey--"
        palla_say "--and she's always talking about you and I hate it and oh you don't care about any of this and I'm really sorry I'm bothering you oh god damn it!"
        "She turns to race off, but hesitates, just a second, leaving an opening."
        menu:
            "Grab her wrist and stop her":
                show palla angry
                "As she turns I grab her wrist, preventing her from easily taking more than a step. She turns and looks at me, anger in her eyes, but something else. She tries to pull her wrist away, but I maintain a grip that isn't tight enough to hurt her, but will require her to pull pretty hard to get away."
                "She tugs a second time, but interestingly not actually all that hard. It has the effect of forcing her to step toward me, and suddenly she is very nearly pressed up against me. She's almost as tall as I am, and I end up looking directly into her angry green eyes."
                palla_say "Let go of me, asshole!"
                "She doesn't actually pull away again, instead just letting me hold her wrist, her nose a mere couple of inches away from mine. I lower my voice; we are in public, after all, and I don't want this to be a shouting match."
                hero.say "Now, hang on a second, lady. First you threaten me, call me a creep, then say you want to get to know me, and now I'm an asshole? Which is it?"
                "She lowers her voice too, and practically whispers."
                palla_say "I…I…I just want you to let go of me."
                "I loosen my grip and let my fingers go slack, but don't actually remove them from her wrist, and then I wait to see what she does."
                show palla casual normal
                palla_say "And don't you dare try anything. If you try to kiss me, I'll scream."
                "I look down at her lips. They're trembling. She moves her wrist and it's obvious she knows she can pull away at any time, but hasn't yet. That was a dare. I want to, because this girl is hot and this whole angry act is getting me going. I'm not sure if I dare, though. We're in public. What if she really does scream?"
                menu:
                    "Kiss her":
                        show palla blush
                        "I lean in--it's not too far, she's already right in my face--and touch my lips to hers. My whole body follows, and when her chest presses up against mine, her heart is beating so hard and so fast I can feel it up against me."
                        "Her only immediate response is for her eyes to first widen, then close. The rest of her body stiffens. I wrap my free hand around her waist and pull her fully against me."
                        "After a few more seconds, her lips part and our tongues meet. I tighten my grip on her wrist again and she makes a noise in the back of her throat."
                        "In just a few seconds, this whole thing has me so turned on that my dick starts to harden as our bodies press against each other."
                        "Then, suddenly, she pushes away. I wasn't holding very tightly, so she is easily able to escape my embrace."
                        show palla angry
                        palla_say "Don't ever do that again, you fucking asshole."
                        "She turns and heads toward the exit. As she passes through it, she throws me a look over her shoulder, her eyes smoldering. With rage? With desire? Some of both? It's hard to tell."
                        "And with that, she's gone. I think maybe she wants me to follow her, but I don't think I want to play that game right here."
                        $ palla.love += 5
                        $ palla.sub += 5
                    "Don't kiss her":
                        hero.say "You keep telling me not to do things that I think you want me to do."
                        show palla blush
                        hero.say "But I don't think so, not here, not now anyway. Maybe another time, somewhere else."
                        "Palla stammers and her wrist pulls easily out out of my loose grip."
                        palla_say "How dare…you fu…you creep! Asshole!"
                        hero.say "Don't forget dick, you haven't called me a dick yet. Or a bastard."
                        show palla angry
                        "For a minute, I actually think she's going to slap me, right there in front of the crowd. But she doesn't, she just scowls at me and, apparently having run out of nasty words for me, turns on her heel and leaves. She looks frustrated. Frankly, so am I."
                        $ palla.sub += 2
                        $ palla.love += 2
            "Let her go":
                "I just watch her leave, without saying anything. When she looks back I actually think she might have been crying a little, but it was just a quick glance. Maybe I was imagining it, but it makes me wonder if I did the right thing."
                $ palla.love -= 10
    $ palla_love_max = 80
    return

label palla_event_04:
    play sound "sd/cell_vibrate.mp3"
    "My phone goes off, very much to my surprise. I look at the caller ID, and it's Palla. What could she want at this time of night? I'm not sure if it's a good idea or not, but I decide to answer it."
    hero.say "Hey, Palla. What's up?"
    palla_say "Hey [hero.name], I want to to the club and dance with someone. Take me."
    "Wow, she's got some nerve, bossing me around like that! And in the middle of the night!"
    hero.say "[[mocking] Oh hey [hero.name], sorry to call so late. How you doing? I'm kind of lonely, can we go out?"
    palla_say "Yeah, fuck you too. Are you going to take me or not?"
    hero.say "I don't think I'm in the mood to take shit from you tonight, Palla."
    palla_say "[hero.name], Hi. I'm a hot, horny, lonely redhead, and I want to fucking dance. With you. If you ever want to kiss me, or anything else to me, ever, you'll get your sexy ass over to the club and fucking dance with me."
    "Then her voice softens, and turns super sexy."
    palla_say "…And I'll make it worth your while."
    "Well, damn. Is she really offering some sexy time? With that bitch, who knows."
    menu:
        "Pass":
            palla_say "Fine, your loss."
            "There is an audible click as she disconnects the call."
            $ palla_love_max = 40
            $ palla.love -= 40
            $ palla_sub = 0
            $ palla_sub_max = 0
            return
        "Fine, I'll meet you there":
            "I agree to meet her, though I don't know if it'll be worth it. On the way over, I realize that she sounded a little drunk."
    $ game.room = 'nightclub'
    scene bg nightclub with fade
    show palla date happy
    "When I get to the club, Palla is out on the dance floor. I have to admit, the girl has some moves! She is completely lost in the beat, moving and shifting in rhythm. I'm almost entranced. I've never actually seen her like this. The more I watch, the more I realize that she could be a professional dancer."
    "When the song ends, she slides gracefully off the dance floor and comes up to me. Damn, but she is hot in that dress!"
    "To my surprise, she wraps her arms around me in a tight, slightly sweaty hug, the wallet in her hand pressing into the small of my back."
    if hero.grooming < 4:

        show palla angry date
        palla_say "Damn, [hero.name], when was the last time you showered? Gross!"
        $ palla.love -= 1
        palla_say "Seriously if you expect to kiss me, take a shower first next time!"
    "After just a second, she steps back and grabs a passing waiter."
    palla_say "I want a Long Island Iced Tea, and whatever he's having. Oh, he's buying."
    "I mumble an order at the waiter, who quickly disappears. Before he is even gone, she drags me out to the dance floor."
    palla_say "[hero.name], now is the time for dancing!"
    if hero.check_skill("dance"):
        "It's easy to get lost in the dance. She is smooth, moving sinuously and sexily, against me and way from me as the music demands."
        $ palla.love += 2
        palla_say "I had no idea you could dance, [hero.name]! You're pretty good at this!"
        hero.say "Yeah, and you're fucking amazing at this!"
        $ hero.fun += 2
        $ hero.energy -= 2
    else:
        "Palla is a far, far better dancer than I am, and I get lost in her twists and turns. I try to keep up, but she seems to lose patience quickly."
        palla_say "[hero.name], if you want to kiss me, you'd better learn how to dance like a fucking man."
        hero.say "I guess you'll just have to teach me!"
        palla_say "Maybe. I'm not sure you're worth it yet."
        hero.say "Oh yeah? And what makes you think you're worth it to me?"
        "Palla thrusts out her sweaty chest and motions to her presented breasts with both hands. In that dress, she may be right; those tits just might be worth it."
        $ hero.energy -= 1
        $ palla.sub += 1
    "After an hour or two of moving and swaying, we both come off the floor again, exhausted and out of breath. Our forgotten drinks are sitting on the little table where the waiter left them, the ice already melted."
    $ game.pass_time(2)
    palla_say "Well, fuck, now I need a fresh drink. Hey waiter!"
    "She flags down the waiter and gets a replacement, while I just watch her heaving breasts, glistening where the dress reveals the skin. She notices me watching."
    show palla normal date
    palla_say "Don't get any ideas, creep."
    hero.say "Ideas? You're the one who planted the idea in my head when you called me. At midnight, remember?"
    "She just shrugs. Damn one minute she's sexy as hell, and the next she's an uber bitch. It really makes me want to put her in her place."
    hero.say "In fact, you promised me a kiss."
    palla_say "I did no such thing."
    hero.say "Yeah you did. Your exact words were that you'd make it worth my while."
    palla_say "I did! This dress, that dancing? You can't tell me that wasn't worth your while!"
    if hero.check_skill("dance"):
        palla_say "Seriously, that was some of the most fun I've had in months."
    else:
        palla_say "Even if you can't dance for shit, it was still awesome."
    hero.say "That was fun for {b}you{/b}, you said you'd make it worth {b}my{/b} while."
    "Palla shrugs and looks at me over the rim of her glass as she drains her Long Island Iced Tea."
    palla_say "Well, that's what you get. Sorry."
    hero.say "Wow, yeah, totally worth it."
    palla_say "Yes, yes it was. Thanks for admitting it. And fuck, I have to go the bathroom. Don't you dare follow me, creep."
    if palla.get_flag_value('storeanal'):
        "There she goes again, daring me to follow her. Of course, last time I got some nice booty. Maybe that's what this is all about? Does she just want to feel...used?"
    else:
        "There she goes again, daring me to follow her. What the fuck is up with that?"
    menu:
        "Follow her":
            scene bg publicbathroom with dissolve
            "I wait a couple of minutes, and then follow Palla into the bathroom, hoping she's the only one in there."
            "When I get there, she's looking into the mirror, adjusting her makeup. I see her eyes catch my reflection in the mirror, but she pretends not to see me."
            "Fine, if this is what she wants. I walk up behind her and grab her ponytail with one hand. The other I put on her shoulder and turn her."
            show palla date blush
            "This causes her neck to be wrenched when she spins around, and she gives a little shriek -- of delight!"
            "Encouraged by this, I slip my arm completely around her and pull her into an embrace, still pulling on her hair, though not hard enough to hurt. Much."
            "I press my lips to hers, which pushes her ass back into the sink. She makes a muffled noise into me as I kiss her, hungrily."
            "Still holding her hair, and with my lips still hungrily taking hers, I bring my arm around front and pull her dress aside to fondle those beautiful tits."
            "Her nipple is as hard as a diamond when my palm comes across it, and she makes a muffled moan. Her arms wrap around my shoulders and grip me tight."
            "I am just about to pull her dress up and really go for it when I hear the door slam. I hear a woman practically shout,"
            unknown_girl_say "Oh go make out somewhere else, you perverts!"
            "I take a step back from Palla, and she looks thoroughly embarrassed. She grabs her purse and runs out through the door."
            hide palla
            "I don't know what to say to the stranger so I shrug kind of awkwardly."
            unknown_girl_say "Just get the fuck out of here so I can pee!"
            "Right, then. I head out the door looking to follow Palla, but when I get out, she's nowhere to be seen."
            "And when I get back to the table, the bill she stuck me with turns out to be 200 bucks!"
            $ palla.set_flag('nokiss', False)
            $ palla_love_max = 120
            $ game.pass_time(1)
            $ hero.energy -= 1
            $ hero.fun += 1
        "Enough of her crap, I'm going home":
            "I wait for a moment, but she doesn't immediately come back. When the waiter brings the bill, my eyes almost bug out. 200 bucks!"
            $ palla.love -= 20
            $ palla_love_max -= 20

    if (hero.money > 200):
        "I have it though, so I pay the bill anyway, and then I head home."
        $ hero.money -= 200
    else:
        "I don't have that kind of money right now, so I wait until the water isn't looking and sneak out."


    $ game.room = 'livingroom'
    return

label palla_event_05:
    palla.say "Hey, [hero.name]. You got a second to chat?"
    "Uh oh, how much abuse am I going to get now?"
    hero.say "Um sure, I got a sec. I guess."
    show palla sad
    palla.say "You don't sound enthusiastic."
    hero.say "Well, you do tell me I'm an asshole and a creep a lot, I'm not sure I'm ready for that just now."
    show palla normal
    palla.say "Okay, fair, I do. But I didn't call you asshole."
    hero.say "Yet."
    palla.say "Anyway, I wanted to talk about the club."
    hero.say "The dancing or the part where you ran off and disappeared just as it was getting good."
    show palla happy
    palla.say "Oh, so it was getting good?"
    hero.say "Are you trying to get me to say you're a good kisser?"
    palla.say "I already know I'm a good kisser, I don't need you to tell me that."
    hero.say "Uh huh."
    palla.say "So yeah, I'm sorry, I ran off. And I wanted to thank you for coming and seeing me. I really needed someone, and you were there for me."
    hero.say "You made it pretty clear we'd be done if I didn't go."
    "Her expression changes, and I can't quite read it; it's like her lips are smiling and her eyes are sad. It doesn't make any sense to me."
    palla.say "But you did, and you were there for me. So, I just want..."
    "Without warning, she steps up to me and wraps her arms around my waist, pressing the length of her body up against mine. When she speaks the air from her words blows gently across my nose."
    "I can smell slightly minty, fresh scent. Did she take a breath mint when she saw me?"
    palla.say "...to thank you."
    "Her eyes are locked to mine. I thought for a minute she was going to kiss me, but she doesn't. But she also doesn't look away."
    "Screw it, she keeps acting like I should take what I want, so I put my arms around her shoulders and pull her close, pressing my lips against hers."
    "Not a hint of resistance! She practically melts in my arms, and it's a real, genuine kiss. Her lips part and she offers her tongue, following my lead."
    "After a moment she tries to pull away."
    menu:
        "Let her":
            show palla happy
            "I let her leave my embrace. She takes a step back and this may be the first time I've ever seen her genuinely smile."
            palla.say "Huh, that wasn't as bad as I thought. Maybe I'll let you do that again."
            $ palla.love += 10
        "Don't let her":
            show palla blush
            "No, she's made it clear she wants me to be firm with her, whenever we're together. So when she tries to pull back, I don't let her."
            "I figure if she really tries, I'll let her go, but certainly not the first time."
            "And indeed, as our lips are locked together, she tries to pull away a second time, but this time clearly not actually putting anything into it."
            "So I reach up with my left hand and grab her pony tail. I yank just a little, which pulls her lips away from mine."
            hero.say "This kiss is over when I say it's over."
            "Palla squeaks, but doesn't say anything. So I let go of her hair and put my hand on her neck, pressing her face back into mine."
            "This time, the kiss is full of fire and passion. If we weren't in a public place, I swear we we'd do the nasty right there."
            "But these things can't last forever, and after another moment I relax my arms."
            "She doesn't pull away immediately, either."
            "When she does pull away, her eyes are a bit glazed over, like she's high."
            palla.say "Oh, fuck, [hero.name]."
            "I guess she doesn't have any other words for that. And frankly neither do I."
            $ palla.sub += 10
            $ palla.love += 3
    show palla happy
    "When it's all done, Palla smiles brightly."
    hero.say "So, you want to go out sometime?"
    palla.say "Nope!"
    "Well that takes me by surprise. What the fuck? After that?"
    "Seeing my distress, Palla laughs."
    palla.say "But! But but but! Keep that up and I'll let you earn it. I just...I just need to know something first."
    hero.say "What's that?"
    palla.say "That's a secret. Don't worry, I won't keep you hanging for too long."
    hero.say "You better not!"
    palla.say "Unless you're an asshole. Which you are always an asshole so maybe I will."
    hero.say "Okay you can stop playing bitch now."
    "Palla laughs and walks away. As she turns she makes a show of her ass and gives me the full sexy model walk."
    "Yeah. Her ass really is all that, too. There's a reason she gets paid for this."
    return

label palla_event_06:
    play sound "sd/cell_vibrate.mp3"
    "When my phone vibrates, the caller ID shows another late night call from Palla. The last time she did this, it ended up mostly fun. Maybe she's done keeping me hanging?"
    hero.say "Hey, Palla!"
    palla.say "Hey, Handsome. You free?"
    menu:
        "Sorry, no":
            hero.say "Damn, and you called me handsome too. But I can't right now. Try me again later?"
            $ palla.set_flag('datetries', 1, mod="+")
            if palla.get_flag_value('datetries') == 1:
                palla.say "Okay, next time. But you'd better be available then, this is a limited time offer!"
            elif palla.get_flag_value('datetries') == 2:
                palla.say "You put me off last time, you'd better not put me off again. I'm not kidding!"
            else:
                palla.say "That's it, you lost your chance with me."
                "She hangs up. I try to call her back, but my number is blocked. Well, I guess that's over with."
                $ HIDDEN.append("palla")
            return
        "Yes!":
            hero.say "Only if you promise not to call me an asshole."
            palla.say "Oooh, that's asking a lot."
            hero.say "Promise me!"
            palla.say "But what if you act like an asshole?"
            hero.say "I know it'd be a new experience for you, but just this once, try biting your tongue."
            palla.say "Maybe I'll bite something else instead. Anyway, I'll meet you at the restaurant. Oh and [hero.name] don't embarrass me. Dress nice. And shower first! I don't want you to be gross."
    if hero.grooming < 6:
        menu:
            "Take a shower":
                "After she hangs up, I smell my pits. She's right, I do need a shower, so I take one."
                $ hero.grooming += 8
            "I don't smell THAT bad":
                "I'm getting a little tired of that bitch telling me what to do, so fuck the shower."
    else:
        "After she hangs up, I decide that since I already showered today, I don't feel like I need another one."

    $ palla_love_max = 160
    $ palla.set_flag('event6done')
    "I take my time getting to the restaurant. It's not that I'm not looking forward to this; she's dropped enough hints that I think this really is the night."
    "But she's so damn bossy that I really feel like she needs to be kept waiting."
    "Of course, that runs the risk of her being angry when I get there, but I have a plan for that. I hope it works."
    "When I get there, she's already at a table, and I take my time walking up to it."
    scene bg highclassrestaurant with fade
    show palla date angry
    palla.say "Fuck, [hero.name], did you walk here by way of Cuba?"
    hero.say "No, I just walked slowly to let you think about me for awhile."
    palla.say "What, the fuck, a--"
    hero.say "Hey! You promised!"
    "Palla purses her lips, but the word doesn't actually leave her mouth."
    hero.say "Okay, you want the real answer?"
    palla.say "It better be good, or I swear I'll nail your cock to the table."
    "The answer I had prepared almost disappears from my head at that image. Ow. But after a second I recover."
    hero.say "Palla, you're fucking hot when you're angry, and I wanted to start the night out with a hot, sexy bitch on my arm."
    show palla date normal
    palla.say "Yeah, you have to work on that one, [hero.name]."
    "Damn. Well, at least she doesn't look angry any more."
    "Palla sighs."
    palla.say "If you know what's good for you, *[hero.name]*, you'll knock that shit off right now. Or you won't get what I brought for you."
    "I admit, that gets me curious. She doesn't have room to hide much of anything in that dress, and that wallet couldn't hold much more than a card or two."
    hero.say "Okay, you got me. What did you bring me?"
    palla.say "First, did you shower?"
    if hero.grooming < 6:
        hero.say "Nope, you can take me as I am."
        "Palla sighs, and seriously looks disappointed. I mean, maybe I should've given her that one, but she has to stop bossing me around."
        palla.say "I sure hope. Ugh. Gross dude, just gross."
        $ palla.love -= 5
    else:
        hero.say "Can't you tell, my hair's still wet."
        palla.say "Hmm, and I can't smell you from here."
        $ palla.love += 5
    "Palla takes a deep breath, and then turns on her modelling charm. She looks at me and suddenly I'm the camera. And she knows how to work the camera."
    palla.say "Say something nice about me."
    menu:
        "Humor her":
            hero.say "You, uh, you've got a devastating smile?"
            show palla date normal
            palla.say "Seriously, is that all you got?"
            hero.say "No, it's just I'm stunned by your sudden model pose and all the words have been chased from my head by your beautiousness."
            "It wasn't too far from the truth, though really it's stunned by her rapid changes from bitchy to delicious and back again."
            palla.say "On a scale of 1 to 10 I'm going to give that one a 3, but at least, and work with me here..."
            palla.say "You're not being an asshole."
            "Palla leans across the table, giving me a nice view down her dress."
            palla.say "Now, tell me I'm beautiful again."
            hero.say "Okay, Palla, you're beautiful."
            palla.say "Keep going."
            hero.say "Well for one, your body is amazing. Your breasts make me want to grab them and hold them all night."
            show palla date happy
            "I figure if she's not offended by that, I'd go ahead and pursue it."
            hero.say "Your legs, well, when you do that catwalk turn, they make me want to just push you onto a bed, spread them out and dive right in."
            hero.say "And your lips. You really do have the most amazing smile. But I most want to see those lips, wrapped around my cock, sliding back and forth while you finger yourself."
            "I stop and wait for Palla's reaction, which I hope isn't a giant slap in the face."
            $ palla.love += 5
        "Fuck that noise":
            hero.say "Palla, you're gorgeous, but you're being a bossy bitch tonight, and I've just about had enough."
            show palla sad date
            palla.say "Damn it, [hero.name], I'm trying to be good. I really am. Look, I like you, okay? I want you, and I'm trying to give you a chance to earn the right."
            hero.say "The right to what, exactly?"
            palla.say "Jesus, [hero.name], do I have to spell it out? Are you the densest motherfucker in this town, or are we doing this dance because you want to fuck with me?"
            "I sigh, softly, and take a second to compose my words."
            hero.say "Palla, I don't know how to deal with you. One minute you're sweet, one minute you're the world's biggest bitch, and I really don't know how to cope with any of that."
            if hero.grooming < 6:
                show palla sad date
                palla.say "Okay, fine, you win. I thought you would be the one, even as much of an asshole as you are, but you're just not, and you're not going to be. I get it. I'm sorry."
                palla.say "This whole thing was a bad idea. Never mind. I'll leave you alone now."
                "Palla pushes away from the table and gets up. As she turns and storms away, I can see tears streaming down her face."
                "I really wish I understood her, but I don't. Maybe if I'd given in a little more to her whims something could've happened?"
                "But maybe I'm better off not having to deal with that crap."
                $ HIDDEN.append("palla")
                return
            else:
                show palla sad date
                palla.say "Okay, at least you showered for me. That's something. Maybe this won't be so bad."
                hero.say "Maybe WHAT won't be so bad?"
                palla.say "You really don't know why you're here?"
                hero.say "I'm here because a crazy but hot woman calls me up in the middle of the night when she's lonely. She teases me but won't ever admit what she actually wants."
                hero.say "I'm here because apparently I'm a masochist who puts up with this crap in the hopes that if I can get past your bitchiness, the sweet, sexy woman will come out."
                show palla normal date
                hero.say "I'm here maybe because I'm stupid or maybe because I'm hopeful. Very possibly it's both."
                hero.say "And mostly I'm here because I'm curious, curious enough to weather your scorn to see what comes out the other side."
                palla.say "Okay. Okay. Okay, maybe I can do this, then."
    hide palla
    "Palla slides forward and disappears under the table."
    "I feel her hands on my knees, which she pushes apart, not entirely gently. Her entire body pushes forward and then I see her red hair peeking out from under the table, in my lap."
    hero.say "Wait, what are you doing?"
    palla.say "When the waiter shows up, tell him I went to powder my nose and order a salad for me."
    show palla restaurantbj
    "Palla unzips my pants and sure enough as soon as her fingers brush against my cock, it responds and springs to attention in her fingers."
    "She brushes her tongue against the very tip."
    if hero.grooming < 6:
        palla.say "I really, really wish you'd showered, this would be a lot less stinky down here."
        hero.say "Um, uh, yeah, next time I guess."
    palla.say "Pretend like nothing's going on. Get your phone out and stare at it. If you say anything or give me up I swear I'll bite."
    "That threat should bother me, but it just turns me on even more."
    show palla restaurantbj suckdick
    "Her lips slide around my penis, taking just the tip of my head into her mouth. She uses her tongue the way only someone who's got some experience at this can do."
    "I pull out my phone, like she said, and pretend to look at it. It turns out to be really, really hard not to make a sound, because she's {b}good{/b} at this."
    "After a few strokes, she starts taking me deeper, bit by bit, until I can start to feel the tip of my cock bumping against the back of her throat."
    "I slip one hand under the table, putting it on the back of her neck. She resists my attempts to speed her up."
    "That's probably just as well, there's no way no one would notice that."
    menu:
        "Make her deep throat":
            "But she's down there, and she's liked it every time I've taken charge. So instead of trying to speed her up, I slow her down."
            "When she tries to pull back, I hold her head right where it is, with my cock just touching her tonsils."
            "And carefully I push her down further, until she's all the way down to the base, and hold her there."
            "I can hear her making a gagging noise, but it doesn't seem too serious, and she isn't fighting me at all."
            "So I let her go back up to just the head, and then down a few more times, each time holding myself all the way in."
            show palla restaurantbj suckdick dick
            "It doesn't take long before I cum all down her throat, and this one feels like it goes on forever."
            "But just because I've cummed, that doesn't mean she can be done."
            "I keep holding her down there until I'm fully limp, which takes another five or six minutes. She makes a little play at trying to get up, but doesn't try too hard."
            show palla restaurantbj kissdick face
            "Once I'm done, I release my grip on her neck."
            show palla restaurantbj kissfeet
            "She kisses all the way down my thighs, past my knees, and down to my feet."
            "I've never had a girl kiss my feet after a blow job before, and I think I kind of like it!"
            $ palla.sub += 10
        "Let her control the pace":
            "I leave my hand slack on her neck, letting her control the pace."
            "It doesn't take her too long, either; like I said, she's good at this. Not a hint of teeth and expert use of her tongue."
            show palla restaurantbj suckdick dick
            "I fill her mouth up with my cum, which goes on a lot longer than I would have expected."
            show palla restaurantbj kissdick face
            "I hear her swallow, and then she gives me little kisses all along my belt line and around the insides of my thighs, before backing out from between my legs."
            $ palla.love += 5
    show palla date happy
    "Palla slips back up out from under the table, and the conversation at the table next to us suddenly goes stone quiet. I guess someone noticed her."
    "But she doesn't seem to mind. She flashes me a bright smile, with just a little bit of my cum dripping from one corner of her mouth."
    palla.say "Oh look, you came before the food did."
    hero.say "Well, damn, I guess I did."
    "And then Palla continues the date, pretending that didn't happen."
    "When the waiter brings our meal, she goes on with her normal erratic behavior, alternately telling me I'm handsome and finding something I did, or said or just smelled to be annoyed about."
    "Somehow after that orgasm, it's all a little easier to take, though."
    "When the meal is over, and we're on the way out of the restaurant, I invite her back to the house."
    palla.say "Nope, you still haven't earned that one. Yet. But I'll think about it next time, okay?"
    hero.say "Next time?"
    palla.say "There better be a next time."
    hero.say "You know, that's historically been more up to you than me."
    palla.say "Well, ask me again tomorrow and I guess you'll just have to roll the dice."
    "And before I can answer, she gives me a deep, long kiss. Then she strides away, giving me that model hip sway. I do like that model hip sway."
    $ palla.set_flag('nodate', False)
    $ game.pass_time(4)
    $ hero.fun += 3
    $ hero.energy -= 4
    $ game.room = 'livingroom'
    return

label palla_event_07:
    $ palla.set_flag("talksex", False)
    "I see Palla and she immediately walks up to me."
    show palla angry
    "After our last date, I honestly have no idea what she's going to say or do. On one hand, she clearly enjoyed it."
    "On the other hand, she's always berating me for something."
    "And maybe for her this was a one night stand, but I've always felt like she was looking for something more, even if she never says it."
    palla.say "[hero.name], we have to talk."
    "Ah, it's going to be like that, is it."
    hero.say "Sure, Palla. What's up?"
    palla.say "I...ugh, I don't really know how to start. I just. Are you going to dump me now?"
    "Okay, so even not knowing what to expect, I didn't expect that."
    hero.say "Dump you? I don't...it's not like we had any kind of agreements."
    palla.say "It's not that, [hero.name], it's just that...ugh, MEN."
    hero.say "Palla, you're not making any sense."
    palla.say "Just give me the speech. Tell me it was fun and you're done with me."
    menu:
        "I'm done with you":
            hero.say "Fine, if that's what you want to hear. We had our fun, and now we're done."
            show palla sad
            "Palla looks at me, tears welling up in her eyes."
            palla.say "Okay. Thanks for at least being a man."
            "As she turns, I can hear a sob. It makes me briefly wonder if I've done the right thing."
            $ HIDDEN.append('palla')
            hide palla
            return
        "It was fun, I'm not done":
            $ palla_love_max = 200
            $ palla.set_flag('nodate', False)
            $ palla.love += 5
            hero.say "I don't know where this is coming from, Palla. It was fun, it was a LOT of fun."
            hero.say "And I'm not done with you, not yet."
            show palla normal
            palla.say "Okay, th--wait, really?"
            hero.say "I get the feeling this is not normal for you?"
            palla.say "Men only ever want one thing, and then they're gone. But, look. I'm not looking for a boyfriend."
            hero.say "So now you're the one who's one and done?"
            palla.say "No, no. I'll go out with you. Maybe go home with you again."
            if palla.get_flag_value('anal'):
                palla.say "But no more anal! Ugh!"
            palla.say "But I don't want to be your girlfriend, and I don't need you to be my boyfriend."
            hero.say "Huh, so friends with benefits?"
            palla.say "Yeah, a bitch and an asshole who can do the horizontal dance."
            menu:
                "I'm down with that":
                    show palla happy
                    hero.say "Cool, I'm down with that."
                    palla.say "Yeah, I ho--well, yeah."
                    "Palla approaches me and gives me a hug and a quick kiss."
                    palla.say "And thanks for not being a typical guy."
                    "And then she walks off, leaving me wondering where this is going to go."
                    $ palla.set_room(None)
                    hide palla
                    return
                "What if I want more?":
                    hero.say "But what if I want a girlfriend, Palla? What if I want more than a fuck friend?"
                    show palla happy
                    $ palla.love += 5
                    palla.say "Should I care what you want?"
                    hero.say "That's...ugh, that's you telling me why I shouldn't want you as a girlfriend."
                    palla.say "You're catching on."
                    hero.say "Fine, but. Will you at least think about it?"
                    palla.say "Sure, I'll think about it."
                    "..."
                    palla.say "And I've thought about it, and no. But you get to have these on the regular, right?"
                    "She cups her hands under her breasts and displays them. They're easy to admire."
                    hero.say "Yeah, but..."
                    palla.say "And I don't have to care who you fuck or when you fuck, as long as you throw me a bone now and then. So to speak."
                    hero.say "Okay, fine."
                    palla.say "You don't sound convinced. Fine. Prove it to me, for real, and I'll think about it. For real."
                    hero.say "Prove what?"
                    palla.say "That you're man enough for me. I need...a lot of man. Well, a lot of men, usually. But if you can keep up with me, maybe."
                    hero.say "Okay, it's a deal. I'll prove it."
                    "She gives me a wink and walks away."
                "I want you to be mine and mine alone":
                    $ palla.set_flag('minealone', 1, mod='+')
                    hero.say "No, Palla. I want you to be mine. Mine alone."
                    show palla blush
                    if palla.sub > 50:

                        $ palla_sub_max += 10
                        "She goes quiet for just a second, taken by surprise. But also delighted, though she quickly tries to hide it."
                        palla.say "I, uh. No, no. No. I mean I mi--no. Just no."
                        hero.say "Mine. My bitch."
                        palla.say "Don't call me that."
                        hero.say "My bitch!"
                        palla.say "I'm not your bitch. You haven't earned that yet."
                        hero.say "Yet."
                        "She smiles."
                        palla.say "Yet."
                        hero.say "I will."
                        palla.say "Promise?"
                        hero.say "Cross my heart."
                        "She smiles and walks away, looking almost dazed."
                    elif palla.sub > 25:
                        show palla normal
                        palla.say "Oh please, [hero.name], don't make me laugh. I'm way too much woman for you."
                        hero.say "Way too much bitch for me, anyway."
                        palla.say "And you have no idea how to handle a bitch like me."
                        hero.say "With a firm hand and a strong word."
                        palla.say "Don't make me laugh, [hero.name], your hand just isn't that firm."
                        "Oh, she is so full of herself. It makes me want to put her into her place. I just need to find the right time, and right place."
                        palla.say "I gotta run, [hero.name]. If you want me, you know where to find me."
                    else:
                        show palla angry
                        palla.say "Fuck you, [hero.name], you aren't man enough for me. Three of you wouldn't be man enough for me."
                        palla.say "And if that's your attitude, maybe we don't get to be fuck friends."
                        hero.say "Whoa, wait a minute there, don't have a breakdown."
                        palla.say "You can't handle me. I dare you to try."
                        hero.say "I'll take that as a challenge."
                        palla.say "You better get creative, then. See you later!"
                    $ palla.sub += 5
    hide palla
    return

label palla_event_08:
    play sound "sd/cell_vibrate.mp3"
    "I guess by now I should be used to Palla ringing me up late at night. I guess I don't mind, we've always had fun."
    hero.say "Hey sexy bitch. What's up?"
    palla.say "Hey, [hero.name]. I was having trouble settling down, and...I have a weird question for you."
    hero.say "Hit me."
    if palla.get_flag_value("minealone"):
        palla.say "You told me once that you want me to be yours and yours alone."
        hero.say "I did."
        palla.say "Is that still true? Do you care who else I date?"
    else:
        palla.say "Are you still okay with me dating other people?"
        hero.say "That's kind of an odd question, coming from you."
        palla.say "I know, it's just...just answer the fucking question, okay?"
    menu:
        "I want you all to myself":
            $ palla.set_flag('slavepath', True)
            $ palla_sub_max = 100
            hero.say "Yeah, I guess I'm kind of possessive. And I like you."
            hero.say "I think I've earned it."
            palla.say "I don't know..."
            hero.say "Then why the fuck did you ask?"
            palla.say "I was just...having a bad night, I guess, and I wanted..."
            hero.say "Palla, shut up and repeat after me."
            "To my surprise, she actually shuts up."
            hero.say "\"[hero.name], I am yours and yours alone. No one but you can have me.\""
            "There is silence from the other end of the line."
            hero.say "Palla?"
            palla.say "I don't think I can--"
            hero.say "Say it! You asked, you want this. Now say it."
            "There is silence for another few seconds, but then she speaks, and I can hear her trembling."
            palla.say "Wait, [hero.name], wait. I'm not...I'm not saying I won't, but can I have some time?"
            hero.say "Some time? For what?"
            palla.say "To see what it's like. Only dating one guy. I haven't done that since high school, and it was bad."
            "I have to think about that, for a minute. I know she wants a firm hand, but I also know if I go too far, she'll resent it."
            hero.say "Okay, Palla. So you're going to stop dating anyone else?"
            palla.say "Y-yes."
            hero.say "And you'll say it?"
            palla.say "Maybe? I just need...I just need to know it will feel right this time."
            hero.say "Okay. Okay, Palla. We'll give it some time. But you are mine, now."
            palla.say "I...y-yes. I should go, [hero.name]."
            palla.say "I love you!"
            "And before I can respond, the call is disconnected."
        "I don't care else you see":
            hero.say "It's okay, Palla. I don't care who you see. I know you need space."
            "There is a pause before she answers, and she actually sounds disappointed."
            palla.say "[hero.name], I don't think anyone has ever loved me before. Before you. Do you love me?"
            hero.say "Yes, Palla. I do love you."
            palla.say "Okay, [hero.name]. I think that's what I needed to hear. And...I love you too!"
            "And before I can respond, the call is disconnected."
    return

label palla_event_09:
    "When I arrive in the nightclub, I see Palla in the back. I don't have a chance to see or greet her, though, as she and a blond guy in a black trenchcoat disappear through a door in the back."
    if palla.get_flag_value('slavepath'):
        "That's weird. She promised herself to me, and that looked like it might be some kind of a date."
    else:
        "I wonder if that's one of the other guys she's seeing."
    menu:
        "Follow her":
            "I decide I should go check that out. But as I approach the door she went through, two rather large men--I think you might call them beefy--step in my way."
            bouncer_say "The VIP Lounge is private, kid."
            hero.say "Oh, sorry. I was just going in to meet a friend."
            bouncer_say "Do you have an invitation? I don't see any punks on this list."
            "The bouncer flexes his fist menacingly."
            hero.say "I, ah, no, no."
            bouncer_say "Beat it, kid."
            "As I walk away, I can't help but wonder who that guy with her was."
        "Leave her alone":
            "Palla's business is her own business, and I should leave her alone."
    return

label palla_event_10:
    "While browsing around the electronics shop, I can't help but think the cashier looks familiar. Maybe it's because I've been here so much I recognize the employees, but I think it's something else."
    show shawn
    "And then it hits me. If he wore a trench coat, he'd could be the guy I saw with Palla the other night. Maybe I can casually figure out what was going on there without being a jerk to anyone."
    hero.say "Hey, man. Didn't I see you in the VIP Lounge the other night?"
    shawn_say "Who, me?"
    "His nametag says \"Shawn\""
    hero.say "Yeah! Shawn, right? I swear it was you, hanging out with a gorgeous redhead, right?"
    shawn_say "Oh right, yeah! I was there with Palla a few nights ago."
    "I choose my words carefully so it doesn't look like I'm prying.."
    hero.say "Good job, man, she's hot! I hope you had a good date!"
    shawn_say "Oh heck yeah, man, she's the sexiest girl I've ever met. Way out of my league, am lucky to have any kind of shot at all with her."
    hero.say "Well hey if I see you there again, I'll be sure to say hi!"
    "Shawn looks around furtively, as though to see if anyone else is watching."
    shawn_say "And if you want to, you know, buy anything...you know, to make the club more fun or something, just hit me up."
    "Buy something? Like what? Drugs?"
    hero.say "Uh, sure. I'll keep that in mind."
    "Now that I think about it, he does smell a bit like stale smoke. Huh."
    hero.say "See you around."
    return

label palla_event_11:
    $ palla.set_counter('shawnencounter', None)
    $ palla.set_counter('pallavisit12')
    show shawn shady-hands
    shawn_say "Hey! Hey you, [hero.name]!"
    "Shawn practically runs up to me and gets right up into my face. His tone is angry, and there's an undercurrent of potential violence."
    shawn_say "What the fuck did you say to Palla, huh?"
    hero.say "All I did was ask her about you."
    shawn_say "Bullshit! She was devastated, man! I've never seen her like that. What the fuck did you do to her?"
    "Shawn raises his right hand, ball curled into a fist."
    menu:
        "Hit him first":
            "The dude looks like he's ready to try to me me down, so I don't wait. I step right up and launch my best punch right into his jaw."
            "And he goes right down to the ground."
            shawn_say "You hit me! Why the fuck did you hit me?"
            hero.say "You were about to take a punch at me."
            shawn_say "I wasn't...No, I'm not that kind of guy."
            "Shawn puts one hand on his face where I decked him; it's already starting to turn a bright shade of purple."
            "Ow, man, that fucking hurt."
            hero.say "Well, don't raise your fist at a guy while yelling. I honestly thought you were coming after me."
            "Shawn picks himself up off the pavement."
            shawn_say "I'm not going to hit you, but I want to know what you did to Palla!"
        "No need for violence!":
            "I put both hands in the air and take a step backward."
            hero.say "Hey, no need for violence."
            "Shawn looks confused for a moment, then looks at his fist as though it was someone else's. Suddenly realization strikes him and he puts his hand down."
            shawn_say "Oh, sorry man. I'm not violent by nature."
            shawn_say "But fuck man, what did you do to her?"

    hero.say "I didn't do anything, man. Seriously, I asked her about you and she turned into a stone cold bitch and stormed off."
    shawn_say "For serious? That's it?"
    hero.say "I'd say that's weird, but Palla's got some issues."
    shawn_say "You're not wrong."
    shawn_say "Look, are you her boyfriend or something?"
    hero.say "We...have an arrangement, yes."
    shawn_say "Damn, you're lucky, then."
    hero.say "I'm not so sure about that, right now."
    shawn_say "Well, you need to apologize for whatever it is you said."
    hero.say "All I did was ask about you. So are you her other boyfriend?"
    shawn_say "I wish! No."
    hero.say "I thought you said you went on a date with her to the VIP Lounge."
    shawn_say "Oh, that. It was...well it was a date to me, not so much to her."
    hero.say "What was it to her, then?"
    shawn_say "She was just getting me into the VIP Lounge. See, she's still got some contacts so she can get into places like that, but I can't."
    hero.say "You don't really look like the VIP Lounge type, I have to admit. Why would you want to get in there?"
    shawn_say "Oh, my side business."
    hero.say "What's that?"
    shawn_say "Weed. Want to buy some?"
    hero.say "Not right now."
    shawn_say "Pity, I really need the money. We're not going to make rent this month."
    hero.say "We?"
    shawn_say "Yeah, me and Palla."
    hero.say "You live with Palla?"
    shawn_say "Oh. Oh fuck. She's going to murder me if she finds out I told you. I mean, seriously. Please don't tell her!"
    hero.say "{b}You live with Palla?{/b}"
    shawn_say "Yeah man, I needed a roomie to help pay the rent, and she needed a new place. Worked out for awhile but I keep having to float her the cash for her half and this month I don't have it."
    hero.say "I didn't know any of this."
    shawn_say "Some boyfriend you are."
    hero.say "How much does she owe you?"
    shawn_say "For this month, $250."
    hero.say "Total?"
    shawn_say "Um, I don't know. I think it's like five grand by now."
    hero.say "Holy shit."
    shawn_say "Look, I don't care about that. But dude, don't make her cry."
    "I can only laugh."
    hero.say "Look, there's a few things I can make Palla do or not do, but that's not on the list."
    shawn_say "Yeah man, I guess. But. If you hurt her, I'll make sure the zombies get you first."
    hero.say "The zombies?"
    shawn_say "Yeah, when the zombies come."
    hero.say "Uh okay, whatever."
    menu:
        "Offer to cover her rent" if hero.money > 250:
            hero.say "Look, I'll cover her rent this month."
            shawn_say "Oh, no, I can't do that."
            hero.say "Fine, I'll buy $250 of your weed."
            shawn_say "Deal!"
            $ palla.set_flag('rentpaid')
            $ hero.money -= 250
            $ hero.gain_item(Consumable("weed", money_cost = 100, effects = [("fun",10), ("energy",5)], limit = "day"))
            $ hero.gain_item(Consumable("weed", money_cost = 100, effects = [("fun",10), ("energy",5)], limit = "day"))
            shawn_say "If you ever need more, you know where to find me."
        "Say goodbye to this weirdo":
            hero.say "Goodbye now."
            shawn_say "Zombie food, man."
            hero.say "Ooooooooookay."
    hide shawn
    return

label palla_event_12:
    $ palla.set_counter('pallavisit12', None)
    "The doorbell rings."
    scene bg house rain

    show palla sad
    "When I open the door, Palla is standing there. Her eyes are rimmed with red; she's been crying, though despite that her makeup is still perfect."
    palla.say "Hi, [hero.name]."
    hero.say "Palla, I was starting to think I wasn't ever going to see you again."
    "Palla raises a hand like she's going to say or express something with it, but then puts it down and looks away."
    hero.say "Do you want to come in?"
    palla.say "No."
    hero.say "Oh. What do you want, then?"
    "Palla bursts into tears, as though I'd said something hurtful."
    hero.say "Palla?"
    "She starts to turn away. I know, I can tell, if I let her leave now, I'll never see her again."
    "So I step forward and put my arms around her. She tries to push away, but I don't let her. I keep a firm hold around her shoulders as I pull her to me."
    "After a few seconds of token struggle, she relaxes and puts her head on my shoulders."
    hero.say "It's okay, Palla."
    palla.say "No it's not!"
    hero.say "Fine, have it your way. Why isn't it okay?"
    palla.say "You're going to hate me."
    hero.say "I already hate you."
    "Palla hits me gently in the arm, without actually letting go of me."
    palla.say "Not funny."
    hero.say "Well, it doesn't hold a candle to holding the woman I love who's crying in the rain. But I liked it anyway."
    "Palla doesn't say anything."
    hero.say "I've missed you."
    palla.say "You have?"
    hero.say "Yeah. You're the only one who calls me an asshole and means \"I love you.\""
    "Palla squeezes me a little more tightly."
    hero.say "Now, why again am I going to hate you?"
    palla.say "Because I'm not who you think I am."
    hero.say "You mean a beautiful, willful, amazing bitch that also happens to be mine?"
    palla.say "Okay maybe I'm those things, but..."
    "I sigh. I'm getting pretty tired of her beating around the bush here, but...I'm not lying. I did miss her, and I love having her in my arms right now."
    hero.say "You're not the incredibly successful, rich model you might have been telling everyone you are."
    "She makes a squeaky noise and presses her face into my shoulder."
    hero.say "Why do you think that's going to make me hate you?"
    "She doesn't answer again, but instead just sobs into my shoulder."
    hero.say "I don't hate you. I'm a little disappointed in you for lying to me, and a lot disappointed in you for not dealing with this like an adult. But I don't hate you."
    hero.say "And I'm not going to dump you, either. I still love you."
    "She pulls her face away from my shoulder, finally, and looks up at me. Rimmed with red and exhausted, she looks incredibly vulnerable like that."
    palla.say "I love you, too."
    hero.say "If you need help with--"
    palla.say "Don't say it."
    "I sigh and give her a little squeeze."
    hero.say "Fine, I won't say it, but it's still true."
    palla.say "Thank you."
    "It clearly did not feel good for her to say that, but now that it's been said, we're past it."
    palla.say "I have to go. I'm sorry to have dumped this on you."
    hero.say "But Palla! I haven't seen you in like a week, and now you're leaving already?"
    palla.say "I have to take care of something. But I won't disappear again, I promise."
    hero.say "You'd better not."
    "She puts one hand on my chest."
    palla.say "I love you, [hero.name]. I'm so, so lucky to have you. I'm sorry I'm such a dumb bitch."
    hero.say "You're not dumb! Don't ever say that about yourself."
    show palla normal
    palla.say "Fine. I'm sorry I'm such a bitch."
    hero.say "I doubt that you're remotely sorry about that, but I'll take it anyway. See you soon?"
    palla.say "Yes! See you soon."
    $ palla.set_flag('schedule', 'default')
    hide palla
    return

label palla_event_12_fix:
    $ palla.set_flag('nodate', False)
    return

label palla_audrey_date:
    show palla date happy
    "Palla and I casually chat while we wait for our food."





    "The food has just arrived when I realize something very odd. Palla hasn't said anything bitchy about me or the other patrons or the food or the restaurant even once."
    "She also hasn't been extra needy and clingy either, and those are the only two modes I'm used to seeing her in."
    "Instead, she's been sunshine and giggles."
    "And to be honest, it's great. When Palla smiles at me, it makes me feel like I'm the only person in the restaurant."
    palla.say "[hero.name], are you even listening to me?"
    hero.say "Sort of, Palla. I mean yes, but I'm dazzled by your smile. I feel like I'm seeing a side of you I don't see a lot."

    show palla blush

    palla.say "Do you like it?"
    hero.say "I did say dazzled, right?"
    palla.say "Well yes, but you're often at a loss for words because you're dim, not because I'm beautiful."
    "I purse my lips. I guess not being bitchy couldn't last. But before I can say anything she laughs."
    palla.say "Relax, [hero.name], I'm just teasing."
    "She puts her hand in my lap."
    palla.say "And you know what? I think I'm hungry but for something not on my plate here."
    hero.say "Oh. And you're hoping I'll feed you?"
    "Her eyes twinkle, and her voice is full of mischief."
    palla.say "Well, you wouldn't let a gorgeous redhead starve to death at the table, would you?"
    "And with that she slips beneath the table. I get stiff before she even has a chance to unzip my fly."
    show palla restaurantbj
    palla.say "Now don't let anyone know I'm down here!"
    show palla restaurantbj suckdick
    "She touches her lips to the tip of my head, which responds. My eyes go half-lidded while she works me."
    "She takes her time, too, caressing me gently with my tongue. So many times she just tries to get this kind of thing over with, but this time it's like she's worshipping my phallus, and it's fucking amazing."
    "...and then I see Audrey, walking right towards my table. Well, this is awkward."
    hero.say "Shit, Palla, don't move. Audrey is coming."
    hide palla restaurantbj suckdick
    show audrey date
    audrey.say "Hey [hero.name]! Fancy meeting you here! Do you mind if I join you?"
    "Holy crap, with Palla still wrapped around my cock, I'm not sure I can actually hold a conversation."
    hero.say "I, uh..."
    "She doesn't really wait for me to answer, and instead sits in Palla's seat."


    audrey.say "It's so funny to run into you here, [hero.name]! And here I was thinking I'd have to eat by myself tonight."
    hero.say "Yeah, uh, funny."
    "Palla, who'd managed to stay still up until this point, pulls my head deeper into her mouth, which makes me groan, just slightly."


    show audrey angry
    audrey.say "What's that about? Didn't you enjoy the present I gave you last time we ate together?"
    "So, I know Palla said it's okay that I date other people, but that doesn't mean she necessarily wants to hear about it. And this is her best friend. This is getting worse by the minute."
    hero.say "Oh, sorry no, I just...had some gas. It's not you."

    show audrey date normal
    audrey.say "Oh, that's okay then. Anyway, I was thinking this time instead of just giving you a handy I might use something else. I mean, you deserve the best, right? What do you think."
    "Palla's lips clamp down tight, and I can feel her teeth just barely dig into the very sensitive skin of my cock. Not enough to really hurt, but I definitely feel it."
    hero.say "I, uh. Maybe not right now?"
    "Audrey scoots toward me and puts her hand where she expects my dick to be."


    audrey.say "What the fuck! What the fuck is going on here, [hero.name]!"
    "She looks under the table and sees the red hair that's in her hand. She scowls at me and pushes Palla down into my crotch, forcing her to take it all the way into her throat."

    "Palla makes a choking noise and tries to pull away, but Audrey doesn't release her head. With the table there, she doesn't have enough leverage to force herself away either."
    audrey.say "Are you cheating on me, [hero.name]!"
    hero.say "Uh well it's not cheating exactly."
    audrey.say "And how is getting a blowjob under the table by my best friend not exactly cheating, huh?"
    "At this point other people in the restaurant are starting to look, and a murmur takes over the entire place. All of a sudden, Audrey and I are the center of everyone's attention."
    audrey.say "Well, what do you have to say for yourself?"
    hero.say "It's not like you're my girlfriend! We never said anything about being exclusive!"
    "My mind races, trying to think of a way to defuse this situation without getting my dick bitten off, and...not a single idea comes to me, good or bad."
    audrey.say "I'm not your girlfriend? Then what am I? Just some kind of side piece for you?"
    "She lets go of Palla's head, finally, who slips off my dick and gasps a couple of times."
    audrey.say "Besides, I wanted to be the one giving you head under the table."
    "Just then the maître d' appears."
    manager_say "Excuse me, sir and madame, but is there a problem?"
    audrey.say "I'll say there's a problem!"
    manager_say "Can you please keep it down? You're disturbing the other guests."
    "Palla chooses that moment to come up from under the table, taking one of the seats."


    manager_say "Oh. Oh my. Sir, I think I'm going to have to ask you to leave now."
    audrey.say "What the hell? You're kicking us out?"
    manager_say "I'm asking you to please be considerate of the other guests, who are having their meal spoiled by your shenanigans. Please leave. Now."
    "Audrey gets up and leaves, smacking the table loudly on the way out. Meanwhile, Palla gives me a death glare."
    scene bg map
    show audrey date angry at left
    show palla date angry at right
    "As soon as we get outside, both girls start yelling at me at the same time. I can't make out any of the words, and they ignore my attempts to interrupt. So I'm forced to wait it out."
    "Finally, Audrey quiets down."
    palla.say "Well, [hero.name]? What the fuck is going on? What do you have to say for yourself."
    hero.say "Okay, first, Audrey, like I said, there were no promises. So yeah I guess that makes you just a side piece. But since you waste no opportunities to put your tits in my face in the office, that's clearly what you want. And Palla, you said you {b}like{/b} it when I'm with other women!"
    palla.say "Yeah, [hero.name], but she's my best friend!"
    "Audrey's mask of anger cracks and she looks like she's about to laugh."
    palla.say "I told you that I was afraid of dating just one guy, that it was bad the last time I did it. And this is what you do?"
    hero.say "What the fuck, Palla? Do I need you to make a list of who's off-limits? Or is the only girl in the entire world who's off limits your best friend?"
    show audrey happy
    "Audrey starts laughing. It is completely incongruous with everything else that's gone on tonight."
    hero.say "Now what?"
    "Audrey stops laughing and tries to look angry again, but it's like she can't make her face do it."
    palla.say "The only one who is off-limits is my best friend. I thought that was obvious?"
    "I look between Audrey and Palla, and I start to wonder if this is all a setup."
    hero.say "No, Palla, it wasn't fucking obvious."
    audrey.say "Oh my God, Palla, do you see the look on his face right now? I mean, that deer-in-headlights thing is the best. Just the best."
    palla.say "Really, Audrey?"
    audrey.say "So worth it. So very worth it."
    "I look between the two of them, Audrey laughing and Palla looking stern and bitchy."
    hero.say "This is a setup, isn't it?"
    audrey.say "No shit, Sherlock. Figure that out on your own, did you?"
    show palla happy
    palla.say "Oh, fine. It would've been nice if Audrey could keep character for more than 5 minutes!"
    audrey.say "Shut it, bitch."
    show palla normal
    palla.say "Don't be a cunt. And you didn't have to push my head down so hard! I almost threw up in his lap!"
    hero.say "Whoa. Whoa. What the hell?"
    "Palla and Audrey both shrug in unison. And then..."


    "Both women launch themselves at me simultaneously, and I wind up hugging them both, tightly."
    "Well that changed real fast. I can feel Palla's nipples hard against my chest. She is seriously turned on right now."
    audrey.say "You're not mad, are you [hero.name]?"
    hero.say "Not mad? Fuck yeah, I'm mad! You got us kicked out of the nicest restaurant in the city! I'll be embarrassed to ever even go back there!"
    palla.say "Oh don't be such a pussy, [hero.name]. You got a nice blowjob out of it."
    hero.say "You didn't even finish!"
    audrey.say "Well, that can be fixed."
    hero.say "After that? I'm humiliated!"
    audrey.say "You're right, we were bad girls. We deserve to be punished."
    "Palla whispers into my ear."
    palla.say "Yeah. You should punish us."
    "I have to admit, feeling four breasts smashed against my chest was going a long way toward easing my frustration over what just happened. Plus, okay, the idea of taking them both home and fucking the living crap out of them has some appeal."
    audrey.say "I promise I'll be a good girl."
    "Yeah, her promises aren't worth crap, but..."








label palla_audrey_date_threesome:
    scene bg bedroom1
    show audrey date happy at left
    show palla date happy at right
    "We go back to my place, and both girls are, once again, all smiles. Palla might even be described as giddy. I rarely see her giddy."
    "Audrey steps behind Palla and reaches around her. In a few seconds, her elegant, probably expensive dress is on the floor."
    show palla panties
    "While Palla stands still, Audrey's hands cup the redhead's breasts and display them to me. Her nipples harden visibly at the caress."
    audrey.say "You want some of this?"
    "Her hands go under Palla's bra, which is erotic but also hides my view of her nipples. But then one hand slips back out and down into Palla's crotch, while the other casually casts aside the bra."
    audrey.say "Or do you want some of this?"
    "Palla shivers exaggeratedly as two of Audrey's fingers disappear into her slit."
    show palla naked
    palla.say "Now now, Audrey. This isn't just about me."
    "Palla slips out of Audrey's embrace and turns around to face her."
    palla.say "And you, you deserve to be punished for that awful performance you put in."
    "While she speaks, Palla removes Audrey's dress."
    show audrey panties
    palla.say "Not to mention, you were the one who couldn't keep it down. You weren't supposed to get us kicked out."
    "Audrey closes her eyes while Palla works; the model's hands caress Audrey's breasts, and her nipples are as hard as if we were inside a freezer."
    audrey.say "I know."
    palla.say "We were {b}supposed{/b} to give him a BJ together, but you couldn't control yourself."
    "Audrey shrieks as Palla tweaks the brunette's nipples."
    audrey.say "Ow! That fucking hurts!"
    palla.say "Good! It's supposed to!"
    "Palla does it again. Audrey's shriek is quieter this time, a little more gutteral. And with almost a purr behind it. Audrey likes the pain."
    show audrey naked
    "Palla turns back toward me and presents Audrey, who stands there looking completely subservient."
    palla.say "So what do you want to do, [hero.name]?"


label palla_audrey_date_loop(palla_spanked=False, audrey_spanked=False):
    show audrey naked at left
    show palla naked at right
    menu:
        "Spank Audrey" if not audrey_spanked:
            hero.say "Audrey, bend over."
            "Audrey's eyes get wide. She's been wanting this, but now that she's presented with it, I think she's just a little bit afraid. But she does what she's told."
            show spank audrey bedroom naked
            "I raise my hand and bring it down on her cheeks. It makes a satisfying SLAP noise, and her ass jiggles a little when I make contact."
            "I do it again and this time she makes a soft \"Unf\" noise. Her eyes close."
            show spank audrey bedroom naked marks
            "I keep going, counting my way up to twenty smacks. None of them are very hard, but they do add up. By the time I'm done, her ass is as red as a cherry, and a single tear is coming from one eye."
            palla.say "Yeah, cunt. That's what you deserve!"
            "Audrey moans, a mix of pain and pleasure filling her throat."
            palla.say "Slap that bitch again."
            "SLAP!"
            show spank audrey bedroom naked marks wet
            audrey.say "MORE!"
            "SLAP!"
            "Another SLAP!"
            "One more SLAP!"
            audrey.say "Oh God!"
            show spank audrey bedroom naked marks wet ahegao
            hero.say "Okay, I think that's enough."
            "And if I might be worried about how much pain I'm inflicting, her pussy is completely wet and I think she'd orgasm now if I just touched it. But she has to wait for that. This {b}is{/b} punishment after all."
            $ audrey.sub += 10
            hide spank
            call palla_audrey_date_loop (palla_spanked=palla_spanked, audrey_spanked=True)
            return
        "Spank Palla" if not palla_spanked:
            if audrey_spanked:
                hero.say "Your turn, Palla!"
                palla.say "Oh, no, I think Audrey getting it is enough!"
            else:
                hero.say "You first, Palla!"
                palla.say "What?! Wait no, Audrey is the one who wants the spanking!"
            palla.say "I had...something else in mind."
            hero.say "Oh no, you set that up with her. I know she's the one who fucked it up, but now it's your turn. Bend over."
            if palla.sub == 100:
                "Palla walks up to me and comes close to whisper into my ear, presumably so Audrey doesn't hear."
                palla.say "Yes, Master, as you wish."
            else:
                "Palla looks at me with her big, blue eyes. I...please, don't."
                hero.say "Get over here and give me your ass."
                if audrey_spanked:
                    hero.say "I promise I won't spank you as hard as Audrey got."
            "She looks at me, then at Audrey, who is just watching this whole exchange with a smile. Then she bends over, as instructed."
            show spank palla bedroom naked
            "Before I start, I caress her ass. I have to say, one advantage to her being a model is that she keeps her ass in perfect shape. It's fit and trim, not too big, not too small. I kind of want to fuck it rather than spank it, but..."
            "SLAP!"
            "Palla shouts in pain."
            palla.say "Not so rough!"
            hero.say "I thought you liked it rough?"
            palla.say "Not like that!"
            show spank palla bedroom naked pussy
            "Instead of slapping her again, I move my fingers down and slip one into her cunt. She is warm and wet, ready to go."
            hero.say "Your pussy says otherwise."
            show spank palla bedroom naked wet spank
            "Palla closes her eyes as I pull my finger out and raise my hand."
            "SLAP! Not so hard this time, though."
            show spank palla bedroom naked marks wet
            audrey.say "Oh fuck."
            "I was so absorbed in what I was doing with Palla that I didn't notice Audrey. She's standing there with her hand between her legs, pleasuring herself."
            audrey.say "Hit her again!"
            palla.say "No!"
            "SLAP!"
            "Palla shouts again. Audrey straight up has an orgasm, she's so turned on by this."
            palla.say "Please, Master, stop! I'll do anything!"
            hero.say "Anything?"
            palla.say "Anything you want, Master. I'm yours. Fuck me. Fuck my ass, fuck my mouth."
            hero.say "Lick my cum out of your best friend's pussy? Let her fuck your cunt with a strapon while I fuck your ass?"
            $ palla.sub += 10
            palla.say "Yes, please! All of those things! Just...stop this!"
            hero.say "Okay, but you need to be a good girl or we'll finish this later."
            "She looks up at me, a tear running down one cheek."
            palla.say "Yes, Master! Thank you, Master!"
            call palla_audrey_date_loop (audrey_spanked=audrey_spanked, palla_spanked=True)
            hide spank palla
            return
        "Fuck them both":
            pass

    if palla_spanked and audrey_spanked:
        "I look at both girls with their red asses and admire my handiwork."
    "They're both ready, looking at me with smiles on their faces. Both of them have swollen cunt lips, ready for my cock. The question is, who should I satisfy first?"
    "And then I remember that Sasha has a huge box of toys in her room, and one of those would come in handy. I'm going to hope she's not home."
    hero.say "Wait here, you two. I'll be right back."
    scene bg secondfloor
    "I sneak up the stairs and peek into her door. She is home, but she's asleep. I just have to be quiet."
    scene bg bedroom3
    "Luckily, Sasha is a sound sleeper, and I'm able to sneak away with one of the half-dozen strap on dildos that Sasha keeps in her toybox. I hope she doesn't notice it missing!"
    scene bg bedroom1
    show audrey naked happy at left
    show palla naked happy at right
    "When I return I present the strapon to the two ladies. Palla looks honestly surprised, but Audrey looks absolutely delighted."
    audrey.say "Oh, you have the best ideas, [hero.name]!"
    "I pass the strapon to Audrey."
    hero.say "Put it on."
    show audrey strapon
    palla.say "Whoa, are you...is she going to use that on me?"
    hero.say "Well she's certainly not going to use it on {b}me{/b}."
    show palla blush
    palla.say "Oh. Oh fuck me."
    hero.say "Yes, that's the idea. Audrey, you lay down on the bed. Palla, I want you to climb aboard."
    "Audrey obeys immediately. Palla is a little slower to move, but she does so."
    show pallaAudrey threesome strapOn pallaClosed
    "Palla moans as she surrounds the dildo with her cunt, dropping her weight onto it and taking it all in one go. Any hesitation she had about this evaporated as soon as the toy entered her. Yeah, she is ready."
    show pallaAudrey threesome mike out
    "I climb up behind her and push her down so that her face is in Audrey's."
    show pallaAudrey threesome mike ass pallaOpen
    "The two of them kiss while I enter Palla's anus from behind."
    "Palla's voice is muffled by Audrey, but despite her mouth being busy, her moans are loud and sensuous. Together, Audrey and I work Palla pretty hard."
    show pallaAudrey threesome pussyJuice
    "Audrey thrusts up while I thrust down, filling Palla up completely. Audrey holds onto Palla's head, not letting her pull away; all in all, Palla is completely trapped and doesn't have much choice about what happens to her."
    show pallaAudrey threesome assCum
    "It doesn't take long before I spill my load into her ass."
    palla.say "Oh fuck, oh fuck, [hero.name] that was...that was amazing."
    audrey.say "My turn!"
    hero.say "I just unloaded, I don't think I can for a few minutes."









    hero.say "Nope, Audrey, that's your punishment. You want to finish, you gotta finish yourself."
    "Audrey scowls at me, but she can't hold it and cracks into a smile."
    audrey.say "It's okay, I came twice already anyway."
    hide pallaAudrey
    show palla naked
    "Palla slides up and over, laying on my bed next to Audrey. She pats the bed between them."
    palla.say "Come here, my love."
    "I really should be taking charge, but...I'm spent, and it looks comfortable."
    "So I crawl up between them, and the two beautiful women snuggle up to me. Huddled in their warmth, I drift right to sleep."
    $ palla.set_flag("sex",1,"permanent","+")
    $ audrey.set_flag("sex",1,"permanent","+")
    $ hero.activity.set_flag("replaced")
    $ date_stay = False
    $ game.set_flag("dateinprogress",val=False)
    $ game.set_flag("currentdate",None,"day")
    $ game.room = 'bedroom1'
    call sleep from _palla_audrey_date
    return

label palla_mall_date_fuck:
    $ hero.activity.set_flag('replaced')
    scene bg clothesshop
    show palla
    "I don't know why I thought taking Palla on a shopping spree would be a good idea. I hate shopping and the mall at the best of times, but with Palla, it's a whole new kind of annoying."
    "Normally Palla doesn't have any patience, but when it comes to clothes, she seems to want to prove it by visiting every single high-end clothes store in the mall."
    "And if I think my patience is tested by her, her treatment of the employees is condescending at best and more like outright disdain."
    "Palla makes a point of being as awkward and demanding as she can without overstepping the mark and being openly rude and abusive."
    "After what seems like hours, I find myself standing outside one of the curtained-off changing rooms in a store the name of which I can't hope to recall."
    "Palla's been inside for three seconds shy of forever, apparently trying to piss off the entire staff of the place by sending them off for endless changes in size and color of the clothes she's only thinking about being interested in buying...maybe."
    "After a while it begins to become apparent that she's succeeded, as none of the girls that she's dispatched to the shop floor seem to be returning."
    palla.say "[hero.name], where the hell are those useless little cows?"
    palla.say "The store's not that big, and the morons work here, how can they get lost?!?"
    hero.say "I don't know...maybe you finally managed to work them to death."
    hero.say "Or maybe they got buried under an avalanche of this season's most trending clothes?"
    palla.say "Ha, ha, very funny."
    palla.say "If there's one thing I hate, it's shitty customer service!"
    "She mutters and complains to herself for a few more moments, and then seems to come to a conclusion of some kind."
    palla.say "Well, if they're not coming back, you'll just have to make yourself useful and go fetch me what I need."
    "Before I can even begin to protest, she thrusts a handful of clothes around the side of the curtain."
    palla.say "I want these in a size larger, the first in fuchsia, the second in puce and the third in azure blue, NOT ultramarine blue."
    palla.say "You got all of that, huh?"
    hero.say "Yes, I got it."
    "I snatch the proffered items and take the chance to walk away for a couple of minutes."
    "What the fuck is fuchsia or puce? And how is azure blue different from...whatever the fuck she said?"
    "Out on the shop floor, I wander around pretending to look for what Palla wants, getting progressively more annoyed that this is what our date has turned into."
    "I try to recall how I dealt with it the last time -- and then it comes back to me suddenly, and I know what I'm going to do about it now too."
    "Hastily shoving the clothes rejected by Palla onto the nearest rack, I grab three more items at random, just to keep up the ruse that I'm doing as I'm asked."
    "When I get back to the cubicle, I pull the curtain aside and slip in before Palla realizes it's me."
    palla.say "Oh, [hero.name], there you are...finally!"
    show palla panties
    "She's looking over her shoulder at me, expecting me to hand her the new clothes and then leave promptly, like a good boy."
    "I don't answer straight away, as she's standing there in nothing more than her panties."
    "Stood before the mirror as she is, I have an almost perfect view of Palla's nearly naked body, reflected upon its surface."
    "It comes home to me, in that moment, that in spite of the bitching, she's simply stunning to look at."
    palla.say "Don't hang around on my account!"
    palla.say "You can just hand them to me round the curtain next time."
    palla.say "[hero.name], hello...you just run along now, okay?"
    "What I was intending to do comes flooding back to me, and I tear my eyes away from the sight of Palla's hypnotic reflection."
    "Without saying a word, I make like I'm turning to leave."
    "The moment Palla turns her back on me and begins to inspect the clothes I brought at her behest, I stop and turn back around."
    palla.say "Hey, wait a minute, these aren't what I asked--"

    show palla stand
    "Palla yelps as I step forward and press her against the cold surface of the mirror."
    "Memories of the first time we did this come flooding back to me. She told me -- with a smile -- that I was an animal. She really wanted it then. Does she want it as much now?"
    "I wrap my right hand around hers, pinning it flat against the silvered glass above her head."
    "With the left, I slide two fingers into the crotch of her panties and lightly stroke the lips of her pussy."
    "Despite her apparent surprise and the shock in her eyes, Palla's already soaking the gusset of her underwear."
    "I guess she does want it as much as the first time!"

    "I keep Palla pinned with one arm while I hastily and rather clumsily strip off my own clothes as well."
    "Her breathing comes fast and in gasps, and I can almost feel her heart beating through her back."
    "She keeps trying to look back at me, but she's too closely pressed against the mirror."
    "All she manages to do is get one cheek squashed into it, making her expression look somewhat comical, despite the situation."
    show palla stand pleasure
    "Now that I'm undressed, I can see that I'm not going to need anything in the way of foreplay."
    "Palla too seems physically ready for me, despite her probably feigned reluctance."
    "I could swear that she even spreads her feet a little wider apart as she feels the brush of my cock on her buttocks."
    show palla stand wet
    "She yelps again as I push into her as far as I can go and remain there for a moment."
    "I can see her cheeks reddening in the mirror, and she closes her eyes now, fully engaged in what's happening."
    "I begin to thrust into Palla, every movement pushing the frustration of the day into the rearview mirror."
    "Fucking her as hard as possible seems to be the best form of therapy for her particular brand of annoyance."
    "The sense of danger, the thought that, at any moment, we might get caught -- it's turning us both on."
    "All it takes is the constant view of Palla's haughty face in such an undignified position, her breasts squashed almost flat against the mirror, the feeling of pounding her deep. God she's hot, especially like this."
    "I know that I can't keep from cumming too much longer."
    "So I need to make a decision as to where she's going to have to take it."
    menu:
        "Pull out":
            "I've become so fixated on the mirror and Palla's reflection in it, that I simply have to involve it somehow."
            "I adjust my angle so that I can slide out of her pussy in one smooth motion."
            show palla stand dick wet
            "That done, I make good use of the lubricant she's thoughtfully provided, and the sweat forming between her thighs to push my cock into the tight gap."
            "Despite her curvaceous thighs and their generous circumference, the head easily emerges from between them."
            "I can feel the cold touch of the mirror and the warm embrace of Palla's thighs all at once."
            "It's an incredible sensation, and I begin to move back and forth again, enjoying this almost as much as being inside of her."
            "Palla too seems to be getting off on it, as the shaft of my cock rubs against the splayed folds of her pussy."
            "She starts to twitch and moan, letting me know that she's close to cumming herself, and that finishes me too."
            show palla stand cum smile
            "I cum whilst the head of my cock is poking out from between her thighs, splattering the mirror as well as Palla's thighs and belly."
            show palla stand cumscreen
        "Cum inside":
            "I'm having such a good time of using Palla's own pussy to purge me of the stress she causes me that I'm staying right where I am until I cum."
            "Since there's no chance of dragging this thing out and we might be rumbled at any moment, I step up my efforts."
            "Now I'm literally thrusting into Palla with as much force as I can muster without making enough noise to attract unwanted attention."
            "She too seems to be on the same wavelength, doing nothing to keep me from fucking her ever harder and everything to keep herself quiet as the same time."
            "Palla's pressed right up against the glass now, her breath steaming it up and the sweat from her body making it slick to the touch."
            "Her breasts are making a squeaking sound in time with my thrusts, like someone dragging a fingertip down a windowpane."
            "I can see her biting her lip in an effort to suppress a cry as she begins to cum."
            show palla stand cum smile
            "That pushes me over the edge, and I lose myself inside of her a second later."
            "I remain where I am, keeping Palla pinned to the mirror, even after I'm finished cumming."
            "And she's forced to ride out her own orgasm in that same position, fighting to remain silent."
            "All she manages to do is make a small mewling sound, as she twitches and writhes against me, her back slick with sweat."
    "It takes us a good few minutes to get our breath back, dress and compose ourselves, before we can walk out of the place."
    "The best part is...now we can get on with our date!"
    $ palla.set_flag("sex",1,"permanent","+")
    $ palla.sub += 2
    $ palla.love += 2
    $ game.set_flag("datescore",50,"day","+")
    if sasha.room == "clothesshop":
        $ sasha.love -= 20
        $ sasha.set_flag('pallasextalk')
    return

label palla_mall_date_fuck_02:
    "I take Palla on a shopping spree."
    $ renpy.dynamic('value')
    menu:
        "Spend $50":
            $ value = 1
        "Spend $100" if hero.money >= 100:
            $ value = 2
        "Spend $200" if hero.money >= 200:
            $ value = 3
        "Spend $400" if hero.money >= 400:
            $ value = 4
        "Spend $800" if hero.money >= 800:
            $ value = 5
        "Spend $1600" if hero.money >= 1600:
            $ value = 6

    $ hero.activity.set_flag('replaced')
    scene bg clothesshop
    show palla
    palla.say "Wait just a minute, [hero.name]. I appreciate the gesture, I do, but don't think I'm going to put out for you in the changing room again."
    if value < 4:
        hero.say "Should I just wait for you to be done, then?"
        palla.say "No, [hero.name], I want you to watch me try these things on and tell me which one makes me look the hottest. You're buying, and you want me to look good for you, right?"
        hero.say "Just tell me you're not going to try on {b}every{/b} piece of clothing in the store?"
        palla.say "Oh nonsense, most of this stuff doesn't fit me anyway."
        hero.say "That does not make me feel better."
        palla.say "No but watching these tits go in and out of sexy dresses will."
        hero.say "Does that mean I get to watch you from inside the changing room?"
        palla.say "No."
        hero.say "Then I don't see how that follows."
        palla.say "Oh, {b}fine{/b}, then. You want a show, fine. Have a show."
        show palla panties
        "I spend the next I don't know how many hours watching an endless parade of garments. In Palla's defense, yes, they're sexy, and yes, she's good at modelling them, and yes, it was entertaining, but...it's really hard to keep focus."
        $ game.pass_time(value)
    else:
        hero.say "For that much, I expect a nice thank you."
        show palla angry
        palla.say "What do you think, I'm a whore?"
        hero.say "Well..."
        "Palla's face turns bright crimson."
        palla.say "How {b}dare{/b} you!"
        "Am I a bad person? Because somehow when Palla is this angry, she's just that much hotter than I normally think she is. And, after all Palla and I have been through, I know getting angry turns her on too. I just have to direct her carefully."
        hero.say "Fine, no, I don't think you're a whore. I do think you're a serious fashionista and that your needs run into the expensive."
        palla.say "And you're a horny asshole who thinks he can buy favors from me?"
        hero.say "Can I?"
        palla.say "Fuck, [hero.name], do you have a romantic bone in your body?"
        hero.say "The question is, do I have a romantic bone in {b}your{/b} body."
        show palla normal
        "Palla stares at me. Yes, the joke was terrible, but all the anger melted from her face. Though not so much a grin."
        palla.say "Fine. Fine fine fine. But let me shop first, because I really need something pretty to make me stop thinking about how fucking smug you look right now."
        hero.say "You have an hour."
        palla.say "An hour! I'll never find something nice in an hour! And you want me in some nice lingerie, right?"
        "I cock my head to the side, pretending to think it over. I already know this is where I have to give her some rope. She has to think she's won something I wasn't prepared to give."
        hero.say "Fine, an hour and a half."
        palla.say "No way! I need two, no three--wait, you want me to hit Victoria's Secret, so four!"
        hero.say "Four? I'll be asleep, have woke up, shot myself in the head, and then gone back to sleep in four hours. You get two, and if you say another word my credit card is going back into my wallet."
        "Palla frowns."
        palla.say "Fine. Two hours. But you're helping me try things on."
        "This is the hard part. Can I really sit through two hours of watching her try on clothing? Maybe if she really does stick to the lingerie, and puts on a show."
        hero.say "You'd better give me a show."
        palla.say "Deal."
        "We're just about an hour in, when I notice that Palla's actually getting turned on by my boredom. Oh don't get me wrong, I like watching her in these outfits. Some of them are {b}very{/b} sexy and she's a hell of a woman, but I can't tell the difference between half the things."
        "But the more bored I get, the sexier her voice gets, and the more I can see hard nipples through whatever extremely thin piece of fabric she's thrown over them this time."
        "I think that means the time is about right. I make sure none of the staff is looking, and while she's changing for the (approximately) hundred thousandth time, I slip into her changing room."
        "She's facing the mirror, having just removed the latest garment and is in the process of tossing it into the pile."
        "I step right up to her and press her against the mirror."
        show palla stand
        palla.say "Hey! It's only been an hour!"
        "I decide to go rough. I can already tell she's ready."
        hero.say "Shut up, bitch. You can finish when I finish."
        palla.say "But--"
        hero.say "If you say another word I'm going to shove your panties in your mouth to shut you up."
        "Her mouth snaps shut at that. There we go, that's what I want."
        "I use the moment if silence to strip out of my own clothes."
        show palla stand wet
        menu:
            "Fuck her ass":
                if palla.get_flag_value('anal' < 3):
                    "I press the tip of my head into he waiting anus. It's so tight, though, that it won't go in."
                else:
                    "I press the tip of my head into he waiting anus. It enters freely for the first couple of inches before the tightness stops me. Palla's face contorts, and I pull back out."
                "Luckily, her pussy is flowing with lubricant. I slip myself deep into her cunt, getting myself good and wet, and then I go back to her asshole."
                "I have to work my way in over several tries, but with the fresh, natural lubricant on my cock, each gentle thrust gets me just a little bit further in, until I'm in far enough to truly feel good."
                "While I thrust into and out of her ass, her face thumps into the mirror at the end of every one. After a few moments of this, she starts to make muffled \"ow\" noises, so I slow down a bit and try not to thump her so hard."
                "Look, she likes it when I dominate her like this. It gets her off; but I don't want to hurt her!"
                "It only takes a few more thrusts and I'm ready to blow. And nothing short of gagging her would stop the screech she makes when she orgasms. At least she bites it short."
                $ palla.set_flag("anal",1,"permanent","+")
            "Fuck her pussy":
                "I slip my hard cock into her pussy; she's wet, swollen and totally ready. It goes in easily and I push it in deep."
                "She tries not to make a sound, but a muffled mmf escapes her."
                hero.say "Shut up, bitch!"
                show palla stand pleasure
                "While I thrust into and out of her cunt, her face thumps into the mirror at the end of every one. After a few moments of this, she starts to make muffled \"ow\" noises, so I slow down a bit and try not to thump her so hard."
                "Look, she likes it when I dominate her like this. It gets her off; but I don't want to hurt her!"
                "It only takes a few more thrusts and I'm ready to blow. And nothing short of gagging her would stop the screech she makes when she orgasms. At least she bites it short."
    "I know that I can't keep from cumming too much longer."
    "So I need to make a decision as to where she's going to have to take it."
    menu:
        "Pull out":
            "I've become so fixated on the mirror and Palla's reflection in it, that I simply have to involve it somehow."
            "I adjust my angle so that I can slide out of her pussy in one smooth motion."
            show palla stand dick wet
            "That done, I make good use of the lubricant she's thoughtfully provided, and the sweat forming between her thighs to push my cock into the tight gap."
            "Despite her curvaceous thighs and their generous circumference, the head easily emerges from between them."
            "I can feel the cold touch of the mirror and the warm embrace of Palla's thighs all at once."
            "It's an incredible sensation, and I begin to move back and forth again, enjoying this almost as much as being inside of her."
            "Palla too seems to be getting off on it, as the shaft of my cock rubs against the splayed folds of her pussy."
            "She starts to twitch and moan, letting me know that she's close to cumming herself, and that finishes me too."
            show palla stand cum smile
            "I cum whilst the head of my cock is poking out from between her thighs, splattering the mirror as well as Palla's thighs and belly."
            show palla stand cumscreen
        "Cum inside":
            "I'm having such a good time of using Palla's own pussy to purge me of the stress she causes me that I'm staying right where I am until I cum."
            "Since there's no chance of dragging this thing out and we might be rumbled at any moment, I step up my efforts."
            "Now I'm literally thrusting into Palla with as much force as I can muster without making enough noise to attract unwanted attention."
            "She too seems to be on the same wavelength, doing nothing to keep me from fucking her ever harder and everything to keep herself quiet as the same time."
            "Palla's pressed right up against the glass now, her breath steaming it up and the sweat from her body making it slick to the touch."
            "Her breasts are making a squeaking sound in time with my thrusts, like someone dragging a fingertip down a windowpane."
            "I can see her biting her lip in an effort to suppress a cry as she begins to cum."
            show palla stand cum smile
            "That pushes me over the edge, and I lose myself inside of her a second later."
            "I remain where I am, keeping Palla pinned to the mirror, even after I'm finished cumming."
            "And she's forced to ride out her own orgasm in that same position, fighting to remain silent."
            "All she manages to do is make a small mewling sound, as she twitches and writhes against me, her back slick with sweat."
    "It takes us a good few minutes to get our breath back, dress and compose ourselves, before we can walk out of the place."
    "I have to commend Palla for the act she puts on in handing back the unworn clothes to one of the catty sales assistants striding back into the mall."
    "None of them dare to say anything, but I think I can infer from their evil grins and the comments exchanged behind raised hands as we leave, that they at least suspect the truth of the matter."
    "Not that it really concerns me, as the whole thing has left me feeling an almost zen-like state of calm, purged of the annoyance Palla provoked in me."
    "I'd like to think that the experience might have humbled Palla a little too."
    $ palla.set_flag("sex",1,"permanent","+")
    $ palla.sub += 2
    $ palla.love += 2
    $ game.set_flag("datescore", 10 * value, 1, "+")
    $ hero.money -= 50 * 2 ** (value - 1)

    if sasha.room == "clothesshop" or randint(1, 3) == 1:
        $ sasha.love -= 20
        $ sasha.set_flag('pallasextalk')
    return


label palla_give:

    palla.say "What do you think about your present?"
    hero.say "What present?"
    palla.say "The necklace I am wearing, silly."
    hero.say "!?"
    palla.say "I bought it just so that you could see me wearing it..."
    return

label palla_give_valentine:
    show palla
    "Palla walks hesitantly towards me."
    call palla_greet from _call_palla_greet_7
    show palla blush
    palla.say "Happy valentine's day [hero.name]..."
    $ gift = Consumable("Valentine chocolates", money_cost = 25, effects = [("fun",1),("hunger",1)], limit = "day")
    "Palla hands me a box of chocolates."
    hero.say "Thank you, Palla."
    $ hero.gain_item(gift)
    hide palla
    return

label palla_give_birthday:
    show palla
    "Palla walks towards me."
    call palla_greet from _call_palla_greet_8
    show palla happy
    palla.say "Happy birthday [hero.name]!"
    call palla_give from _call_palla_give
    return

label palla_give_christmas:
    show palla
    "Palla walks towards me."
    call palla_greet from _call_palla_greet_9
    show palla happy
    palla.say "Merry christmas [hero.name]."
    call palla_give from _call_palla_give_1
    return

label palla_init:
    if "palla" not in HIDDEN:
        $ HIDDEN.append("palla")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
