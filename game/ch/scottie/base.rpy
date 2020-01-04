init -1 python:
    Event(**{
        "name":"scottie_give_phone_number",
        "label": ["give_phone_number"],
        "duration": 0,
        "girl": "scottie",
        "girls_conditions": {"scottie":{"min_love":40,"valid":True,"contact":False,"not_activity":"sleep","present":True}},
        "game_conditions":{"chances":5, "flag_female":0},
        "do_once": True,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"scottie_send_text",
        "label": ["send_text"],
        "duration": 0,
        "priority":100,
        "fun":1,
        "girl": "scottie",
        "girls_conditions": {"scottie":{"contact":"scottie","valid":True,"present":False,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"hours":(12,13),"flag_dateinprogress":0,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"scottie_auto_greet",
        "label": ["auto_greet"],
        "duration": 0,
        "girl": "scottie",
        "priority":100,
        "girls_conditions": {"scottie":{"valid":True,"flag_greeting":False,"not_activity":"sleep","present":True,"min_love":50}},
        "game_conditions": {"chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"scottie_auto_chat",
        "label": ["auto_chat"],
        "duration": 0,
        "girl": "scottie",
        "priority":100,
        "girls_conditions": {"scottie":{"valid":True,"present":True,"not_activity":"sleep","min_love":50}},
        "game_conditions": {"flag_dateinprogress":False,"chances":10, "flag_female":0},
        "do_once": False,
        "once_day": True
        })

    Event(**{
        "name":"scottie_are_you_sick",
        "label": ["are_you_sick"],
        "duration": 0,
        "girl": "scottie",
        "priority":100,
        "girls_conditions": {"scottie":{"valid":True,"present":True}},
        "game_conditions": {"flag_sick":True,"not_activity":"sleep","chances":"love_scottie_2", "flag_female":0},
        "do_once": False,
        "once_day": True,
        "quit": False
        })

    Event(**{
        "name":"scottie_ask_out",
        "label": ["ask_out"],
        "duration": 0,
        "girl": "scottie",
        "priority":100,
        "girls_conditions": {"scottie":{"valid":True,"min_love":100, "date_planned":False,"not_activity":"sleep","present":True,"flag_nodate":False}},
        "game_conditions": {"chances":5, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


    Event(**{
        "name":"scottie_time_for_our_date",
        "label": ["time_for_our_date"],
        "duration": 0,
        "priority":100,
        "girl": "scottie",
        "girls_conditions": {"scottie":{"validappointment":True,"present":True}},
        "game_conditions": {"flag_dateinprogress":False,"not_activity":"sleep","chances":50, "flag_female":0},
        "do_once": False,
        "once_day": True
        })


label smartphone_scottie_hint:
    "No hints for Scottie right now."
    return

label scottie_bye(duration=0, bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = scottie.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = scottie.get_activity(bye_hour)
    if not activity == scottie.activity:
        if day != game.week_day:
            $ scottie.set_flag("activity-"+str(day)+"-"+h,activity,2)
        else:
            $ scottie.set_flag("activity-"+str(day)+"-"+h,activity,"day")
        show expression "scottie "+bye_outfit
        if activity["activity"] == "sleep":
            scottie.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            scottie.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            scottie.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            scottie.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            scottie.say "Do you know what is on TV right now ?"
        elif activity["activity"] in ["drink"]:
            scottie.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            scottie.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            scottie.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            scottie.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            scottie.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            scottie.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            scottie.say "I ll go get dressed."
        hide expression "scottie "+bye_outfit
    return

label scottie_cheated:
    show scottie
    "I see Scottie looking at me kissing someone else with envy and lust in her eyes."
    $ scottie.love += 1
    hide scottie
    return

label scottie_greet:
    if not scottie.get_flag_value("greeted"):
        $ scottie.set_flag("greeted",True,1)
        show scottie
        $ result = randint (1,3)
        if result == 1:
            scottie.say "Hello, babe."
        elif result == 2:
            scottie.say "Hi, baby."
        elif result == 3:
            scottie.say "Hi, babe."
        else:
            if game.hour < 12:
                scottie.say "Good morning babe."
            elif game.hour < 19:
                scottie.say "Good afternoon baby."
            else:
                scottie.say "Good evening babe."
        $ result = randint (1,3)
        if result == 1:
            hero.say "Hello, Scottie."
        elif result == 2:
            hero.say "Hi."
        else:
            if game.hour < 6:
                hero.say "Hello Scottie."
            elif game.hour < 12:
                hero.say "Good morning Scottie."
            elif game.hour < 19:
                hero.say "Good afternoon Scottie."
            else:
                hero.say "Good evening Scottie."
    return

label scottie_kiss:
    scene expression "bg "+game.room
    if scottie.love() + hero.charm() < 80 and not scottie.get_status() in ["boyfriend", "sex slave"] and not game.get_flag_value("datescore") >= 75:
        show scottie
        "Scottie quickly takes a step back, and turns away."
        if scottie.love < 40:
            scottie.say "Sorry but... I don't really feel comfortable with that."
            $ scottie.sub += 1
        else:
            $ result = randint(1,2)
            if result == 1:
                scottie.say "Sorry [hero.name], but let's just not."
                $ scottie.love -= 1
            else:
                scottie.say "I'm sorry, but I have to go..."
            "Before I can react, Scottie turns and rushes away."
        hide scottie
    elif scottie.love() + hero.charm() < 60  or (game.get_flag_value("datescore") >= 75 and not scottie.love() + hero.charm() < 60):
        hide scottie
        show expression "scottie kiss "+scottie.get_clothes()
        if not scottie.get_flag_value("kiss"):
            "I watch Scottie's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide expression "scottie kiss "+scottie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != scottie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_121
            elif scottie.love >= 60:
                show scottie
                scottie.say "Um, I think we should talk about this later, alright?"
            else:
                show scottie
                scottie.say "Oh uh... I've got to go..."
                "Before I can object, Scottie begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
            $ scottie.set_flag("kiss",1,"permanent","+")
        else:
            "I take a step closer to Scottie, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide expression "scottie kiss "+scottie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != scottie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_122
        $ scottie.love += 1
    else:
        hide scottie
        show expression "scottie kiss "+scottie.get_clothes()
        if not scottie.get_flag_value("kiss"):
            "I feel my lips passing over Scottie's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Scottie with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide expression "scottie kiss "+scottie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != scottie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_123
            elif scottie.love() >= 60:
                show scottie
                scottie.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show scottie
                scottie.say "Um... I should go..."
                "Before I can object, Scottie turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(1,2) == 2:
                "Yet again I feel my lips passing over Scottie's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Scottie with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Scottie, close enough that our bodies are very nearly touching."
                "I bring one hand to Scottie's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Scottie's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide expression "scottie kiss "+scottie.get_clothes()
            $ cheated_girls = [g for g in ROOMS[game.room].get_present_girls() if (g.get_flag("kiss") or g.get_flag("sex")) and g != scottie and renpy.has_label(g.id+"_cheated")]
            if cheated_girls:
                call expression randchoice(cheated_girls).id+"_cheated" from _call_expression_124
            if hero.charm() >= 160 - scottie.love():
                show scottie
                scottie.say "Stop doing that."
        hide scottie
        $ scottie.love += 2
    return

label scottie_sleep_date_fuck:
    scene bg bedroom1
    show scottie naked
    menu:
        "You should leave":
            hero.say "I am done with you and I have to get up early tomorrow, you should leave."
            "The sex was beyond incredible."
            "Frowning a little, Scottie straightens and shrugs, then goes to collect her clothes from where she'd let it fall earlier."
            "She then heads up the stairs."
            $ scottie.love -= 1
            $ scottie.sub += 1
        "You should sleep here":
            hero.say "You can stay and sleep here."
            "I say, my voice a little shaky."
            "We curl up spooning together in bed, drifting toward sleep."
            $ scottie.love += 1
    call sleep from _call_sleep_5
    return

label scottie_fuck_date_female:
    scene bg bedroom4
    "Once we're back at my place, we spill into my room without even thinking about anything else."
    show scottie
    "After all, I'm not exactly taking Scottie out on a date for the sake of his non-existent conversation skills."
    "Luckily for me then that he's as eager as can be and doesn't need to be led by the hand."
    "Scottie wastes no time in beginning to kiss me aggressively once the door is closed behind us and almost yanking off my clothes."
    "After so many modern guys that are all gentleness and manners, it's kind of thrilling to be treated in that way."
    "Offer no resistance, returning his kisses and enjoying being roughly stripped."
    "Liking in particular when an item of clothing holds me bound for a few moments at a time."
    "Once I'm finally naked, I return the favour."
    "Scottie begins to kiss my neck and then my breasts as I struggle to pull off his clothes."
    "His body is more impressive than I thought, and I find myself wondering why Sasha ever gave all of this up."
    scottie.say "Yeah, baby - strip it all off of me!"
    scottie.say "You know it's making you crazy!"
    "Oh yeah, I remember now what it was - he's mentally mired in adolescence."
    "But, like I said, we're not here to talk."
    if scottie.sub() < 75:
        scottie.say "What are you waiting for?"
        scottie.say "Get your ass on that bed, girl."
        "I clamber to obey, eager to see what Scottie has in store for me next."
        if randint(1,100) <= 10 + scottie.get_flag_value("anal")*10:
            "Scottie guides me down onto the bed so that I'm on all fours, and then begins to gently probe my ass with one finger."
            "I've never had too much experience with anal before, and I've already seen that Scottie's not a little guy in that department."
            "Luckily for me there's a bottle of lube on the bedside table, and I hear him pumping some onto the palm of his hand."
            hide scottie
            show bree spoon bedroom2 scottie anal
            scottie.say "Open wide, Bree - here it comes!"
            "At first I don't think my ass can take the size of him, but then he pushes harder, and he's inside of me."
            "I moan, deep and low, as he slides further in, the width of him forcing my muscles to make room for him."
            if game.get_flag_value("analSkill") < 5:
                $ posi = "v"
                if scottie.get_flag_value("anal"):
                    $ scottie.set_flag("anal", 1, mod="-")
                "While my ass is stretching to take all of him in, Scottie's dick is also starting to really hurt me more with every new thrust he makes."
                bree.say "Oh...oh, Scottie...it hurts!"
                scottie.say "What...really?"
                bree.say "Yeah...you're...you're just much too big for my ass!"
                bree.say "Please...take it out and put it in my pussy...please?!?"
                hide bree
                "Disappointed to have to pull out, but his ego undoubtedly stroked at the same time, Scottie does as I ask."
                show bree spoon bedroom2 scottie out
                "I can already feel the weight of his dick as it sways against my back and the inside of my thighs."
                "I can also feel my pussy stirring in anticipation as it comes ever closer with each pass."
                scottie.say "Little Bree, little Bree...let me in!"
                if scottie.love() + randint(1,100) <= 150:
                    $ posi += "c"
                    "Scottie pauses in the middle of making for my pussy, my playing along with his game distracting him from the annoyance of stopping for a moment."
                    "He hastily fumbles for a condom from the bedside table and rolls it on."
                    show bree spoon bedroom2 scottie vaginal condom
                    "And then he's finally on me and in me, sliding inside and not stopping until all of him is buried in me."
                    "I've been with guys so terrified of screwing this up that they did just that."
                    "But Scottie's too simple to be that preoccupied, and he simply sets about pleasing himself in the most immediate way possible."
                    "Part of me feels like I'm just along for the ride."
                    "But all the same - what a ride!"
                else:
                    bree.say "What time is it, Mr Wolf?"
                    scottie.say "Time I was balls deep inside of you!"
                    "I ask you, with wit like that, how can a girl hope to resist?"
                    show bree spoon bedroom2 scottie vaginal
                    "Scottie makes good on his promise a moment later, and I feel the sensation of him filling me completely."
                    "I wrap my legs around his, almost desperately and in fear of losing an inch of him."
                    "But I needn't have feared, as he pushes as deeply into me as he's able, forcing me down onto the bed and pinning me there."
                    "There's no more words now, only the sound of him almost growling as he rides me and my own mounting cries of fast approaching climax."
                    if scottie.love() + randint(1,100) >= 200:
                        show bree spoon bedroom2 scottie vaginal creampie ahegao
                        "I start to buck and twitch as my orgasm takes me."
                        "Scottie responds in kind, holding me firmly in place as he cums."
                        "I can feel him spreading inside of me like a slow-motion firework."
                        "He pushes me onwards into a second climax, prolonging my ecstasy still further."
                    else:
                        show bree spoon bedroom2 scottie out creampie cum outside
                        "Almost the same moment that I climax, Scottie pulls out of me."
                        "The sudden and unexpected void makes my orgasm somehow less, more hollow in nature."
                        "He cums a few seconds later, spreading his load across my buttocks and lower back."
            else:
                $ posi = "a"
                $ scottie.set_flag("anal", 1, mod="+")
                if game.get_flag_value("analSkill") < 10:
                    $ game.set_flag("analVirginity",1)
                    "My ass feels like something back there is going to tear or brake at any moment, but at the same time, the sensation is phenomenal."
                    bree.say "Scottie, keep it up...break me if you have to!"
                    "I can feel the instant effect that my words have on Scottie, driving him to fuck me even harder than before."
                    scottie.say "You like that, huh?"
                    bree.say "Oh yes, Scottie...god...I feel like my ass was made for your dick!"
                    "I can feel him quicken yet again, raising the sensations from my ass almost to the level of making me want to scream."
                else:
                    if not game.get_flag_value("analVirginity"):
                        "I've never really had someone fuck me up the ass before now."
                        "Sure, I've messed around back there with fingers and toys, but never with a guy's dick!"
                        "At first I wonder if it'll be at all like being fucked in the pussy, but as soon as Scottie's cock is between by buttocks, I know that's not going to be the case."
                        $ game.set_flag("analVirginity",1)
                    "He's hard enough to make the muscles of my ass part for him, and they resist so much that every in of him feels incredible as he pushes his way into me."
                    "At the same time as I'm moaning in reaction to Scottie, I can hear him groaning from the effort and the clenching of my muscles around his dick."
                    show bree spoon bedroom2 scottie anal cum
                    bree.say "Fuck my ass harder, Scottie...please!"
                    "He struggles to oblige, the more pressure he puts on my already taught ass, the better it feels."
                    "Just when I think that something is about to break and I'm screaming in pain, I realise it's actually that I'm right on the brink of cuming."
                show bree spoon bedroom2 scottie anal ahegao ass
                "I start to buck and twitch as my orgasm takes me."
                "Scottie responds in kind, holding me firmly in place as he cums."
                "I can feel him spreading inside my ass like a slow-motion firework."
                "The feeling pushes me onwards into a second climax, prolonging my ecstasy still further."
        else:
            $ posi = "v"
            if scottie.get_flag_value("anal"):
                $ scottie.set_flag("anal", 1, mod="-")
            "Scottie pushes me suddenly backwards so that I collapse onto the bed, and almost pounces on my back."
            "He's not careful about where his weight ends up, but the feeling is like being ravished by something a little bit wild and out of control."
            show bree spoon bedroom2 scottie out
            "I can already feel the weight of his dick as it sways against my back and the inside of my thighs."
            "I can also feel my pussy stirring in anticipation as it comes ever closer with each pass."
            scottie.say "Little Bree, little Bree...let me in!"
            if scottie.love() + randint(1,100) <= 150:
                $ posi += "c"
                "Scottie pauses in the middle of making for my pussy, my playing along with his game distracting him from the annoyance of stopping for a moment."
                "He hastily fumbles for a condom from the bedside table and rolls it on."
                show bree spoon bedroom2 scottie vaginal condom
                "And then he's finally on me and in me, sliding inside and not stopping until all of him is buried in me."
                "I've been with guys so terrified of screwing this up that they did just that."
                "But Scottie's too simple to be that preoccupied, and he simply sets about pleasing himself in the most immediate way possible."
                "Part of me feels like I'm just along for the ride."
                "But all the same - what a ride!"
            else:
                bree.say "What time is it, Mr Wolf?"
                scottie.say "Time I was balls deep inside of you!"
                "I ask you, with wit like that, how can a girl hope to resist?"
                show bree spoon bedroom2 scottie vaginal
                "Scottie makes good on his promise a moment later, and I feel the sensation of him filling me completely."
                "I wrap my legs around his, almost desperately and in fear of losing an inch of him."
                "But I needn't have feared, as he pushes as deeply into me as he's able, forcing me down onto the bed and pinning me there."
                "There's no more words now, only the sound of him almost growling as he rides me and my own mounting cries of fast approaching climax."
                if scottie.love() + randint(1,100) >= 200:
                    show bree spoon bedroom2 scottie vaginal creampie ahegao
                    "I start to buck and twitch as my orgasm takes me."
                    "Scottie responds in kind, holding me firmly in place as he cums."
                    "I can feel him spreading inside of me like a slow-motion firework."
                    "He pushes me onwards into a second climax, prolonging my ecstasy still further."
                else:
                    show bree spoon bedroom2 scottie out creampie cum outside
                    "Almost the same moment that I climax, Scottie pulls out of me."
                    "The sudden and unexpected void makes my orgasm somehow less, more hollow in nature."
                    "He cums a few seconds later, spreading his load across my buttocks and lower back."
        scottie.say "Don't just lie there panting - get cleaning me up, you lazy bitch!"
        if "c" in posi:
            scottie.say "Shame to see this stuff go to waste!"
            "Scottie peels the condom off of his dick and squeezes it so that the end holding his cum bulges."
            scottie.say "Open wide, Bree!"
            "I stick out my tongue and allow Scottie to pour the contents of the condom onto it."
            "It's already cold, and I can feel it slithering over my tongue and down my throat."
        elif "v" in posi:
            menu:
                "Do it" if game.get_flag_value("morality") < 0:
                    "Scottie's dick is already drooping, but there's still a considerable amount of ground to cover."
                    "I begin to lick him clean from the base of his cock and then work my way upwards, circling the shaft as I go."
                    scottie.say "Don't skimp on the clean up, Bree - make sure you get into all the nooks and crannies!"
                    "I try my best to oblige, being sure to pay particular attention to the head and tip before I'm done."
                "Don't do it":
                    bree.say "Eww, Scottie - I'm up for this whole kinky thing, but there's a fucking limit!"
                    scottie.say "Don't talk back, bitch - do as I say, now!"
                    bree.say "Seriously, Scottie...go wash that thing in the bathroom or something."
                    bree.say "Just stop waving it in my face!"
                    "Scottie's face falls as he realises that I'm deadly serious."
                    scottie.say "Erm...oh, okay..."
        else:
            "Scottie proffers his soiled dick, fully expecting me to indulge his wishes."
            "He's already drooping by now, and the scent of him is something quite pungent."
            menu:
                "Do it" if -75 > game.get_flag_value("morality") < -25:
                    "I try as best I can to breathe through my mouth while I perform the unappealing task."
                    "But it's not easy to do so when the vast majority of it requires the use of your lips and tongue."
                    "For the most part I manage to progress with gulps of air captured at opportune moments."
                    "Though once or twice I mess up and either catch the full aroma of Scottie and my own body comingled, or else taste the same on the back of my throat."
                "Do it" if game.get_flag_value("morality") <= -75:
                    "I try to clear my mind and focus on nothing but the task at hand, shutting everything else out."
                    "But the smell and sensation of it are just too much for that to work, and I can already feel myself beginning to gag."
                    "This is possibly the single most degrading thing that I have ever agreed to do in my life."
                    "A part of me still can't understand just why I'm doing it, but another is strangely turned on by the thought that I've sunk so low."
                    "No one could possibly imagine that I'd even be capable of this if they met me under normal circumstances."
                    "But somehow, allowing myself to literally clean the filth from my own ass off of Scottie's dick after he's fucked me up it is oddly liberating."
                    "If I have the courage to do this, then surely I can do anything...or have anything done to me?"
                "Don't do it":
                    bree.say "Eww, Scottie - I'm up for this whole kinky thing, but there's a fucking limit!"
                    scottie.say "Don't talk back, bitch - do as I say, now!"
                    bree.say "Seriously, Scottie...go wash that thing in the bathroom or something."
                    bree.say "Just stop waving it in my face!"
                    "Scottie's face falls as he realises that I'm deadly serious."
                    scottie.say "Erm...oh, okay..."
    else:
        bree.say "Now you listen very closely to me, dumbass!"
        bree.say "I want everything that you've got in you, and I want it now!"
        "Scottie's face registers a mixture of trepidation and sheer excitement as we climb onto the bed together."
        menu:
            "Tell him to fuck you in the ass":
                "I turn my back on Scottie and then get down on all fours, stalking a foot or so away from him like a haughty cat."
                "Glancing back over my shoulder, I make sure he can see that I've already spread my legs in anticipation of what's to come next."
                bree.say "What do you want, a written invitation?"
                bree.say "Lube yourself up and fuck me in the ass...NOW!"
                "Scottie's cock is fully erect even before he can get a drop of lube onto it."
                "Ready to go, he practically leaps atop me and fumbles eagerly for my ass with his dick."
                show bree spoon bedroom2 scottie anal
                "Eager as he is, he still sinks in slowly, forcing the reluctant muscles of my ass to make way for him."
                if game.get_flag_value("analSkill") < 5:
                    $ posi = "v"
                    "It doesn't take me long to realise that most of what I'm feeling is actually just pain."
                    "Game as Scottie is, he's hurting me more with every moment that passes."
                    bree.say "Stop it, fuckwit!"
                    bree.say "That freakshow cock of yours is too damn big for my ass!"
                    show bree spoon bedroom2 scottie out
                    "Scottie stops suddenly and starts to pull himself out of me, looking confused and disappointed."
                    bree.say "Who the fuck said you could stop?"
                    bree.say "Stick it in my pussy, moron!"
                    menu:
                        "Tell him to wear a condom":
                            $ posi += "c"
                            bree.say "Uhh, uh...not until you put something on it!"
                            "Scottie looks visibly panicked until I point to the condoms on the bedside table and he dives hastily for them."
                            "It only takes him a moment to slip one on and lube himself up, and then he's back on me like a lion on its prey."
                            show bree spoon bedroom2 scottie vaginal condom
                            "For all that he's a hopeless idiot elsewhere, Scottie really delivers where it matters."
                            "His dick is of a very nice size, and he knows exactly how to put it to good use."
                            "I want to keep on putting him in his place, enjoying the act so much."
                            "But he feels so good inside of me that I can't keep from moaning and panting like a bitch on heat."
                        "Don't":
                            "Part of me knows that I should stop Scottie and make him use protection, but the sight of his looming cock makes me desperate to get on with business."
                            show bree spoon bedroom2 scottie out
                            "So much so that I make no protest as he covers me and I feel the head of his dick slipping between my buttocks and hunting out my already welcoming pussy."
                            show bree spoon bedroom2 scottie vaginal
                            "He sinks into me, slowly at first and then with more urgency as he reaches the limits of his length."
                            "Scottie doesn't move for a few moments, and the feeling of his dick inside of me is almost enough to make me crazy"
                            "And then he begins to pull back and thrust forwards, gaining speed with each repetition."
                            "As I start to sigh and moan, I again find myself wondering why Sasha dumped the guy, rather than simply breaking him in properly."
                            menu:
                                "Let him cum inside":
                                    bree.say "Don't stop now, I want to feel it all."
                                    show bree spoon bedroom2 scottie vaginal creampie ahegao
                                    "I don't know if Scottie was planning to pull out or not, but he won't if I have anything to do with it."
                                    "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
                                "Tell him to pull out":
                                    bree.say "Get your elephant prick out of me, asshole!"
                                    bree.say "Right NOW!"
                                    show bree spoon bedroom2 scottie out cum
                                    "Scottie struggles to do as he's told, whipping his dick out a second before I cum."
                                    "The sudden void only serves to intensify the sensations of orgasm, almost sending me into a fit of pleasure."
                                    show bree spoon bedroom2 scottie out cum outside
                                    "So much so that I hardly feel Scotties own cum raining down on my ass until it starts to cool and run down my thighs."
                else:
                    $ posi += "a"
                    $ scottie.set_flag("anal", 1, mod="+")
                    $ game.set_flag("analVirginity",1)
                    "Scottie's enthusiasm translates almost instantly into a sensation that makes me shake with delight."
                    show bree spoon bedroom2 scottie anal cum
                    "I'm no enthusiast when it comes to anal sex, but when it's done right, I simply love it."
                    "Each time he thrusts into me, I can feel the muscles inside of my ass pull and protest."
                    "The pleasure and pain are almost impossible to tell apart, and I find both pushing me dangerously closer to coming with each thrust."
                    bree.say "Good boy, keep it up...make me feel like you're still in there a week after you're done!"
                    show bree spoon bedroom2 scottie anal ahegao
                    "As Scottie struggles to obey, I hear myself begin to yelp, almost like a dog, as my orgasm comes over me."
                    bree.say "Don't stop now, I want to feel it all."
                    show bree spoon bedroom2 scottie anal ass ahegao
                    "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
            "Tell him to fuck your pussy":
                $ posi = "v"
                "I lay down on my side, making sure that he has a grand view of all my curves."
                "Scottie watches intently as I stroke a hand up and down my thigh and squeeze one breast with the other."
                bree.say "Well, what are you waiting for?"
                bree.say "Are you going to put that donkey dick of yours to good use, or what?"
                "As if I'm talking to his cock rather then Scottie himself, I see him becoming visibly more erect with each moment that passes."
                "So I figure - why not do just that?"
                bree.say "Here, boy...come on, that's right!"
                bree.say "I've got something so nice and so juicy, just waiting for you right here!"
                menu:
                    "Tell him to wear a condom":
                        $ posi += "c"
                        bree.say "Uhh, uh...not until you put something on it!"
                        "Scottie looks visibly panicked until I point to the condoms on the bedside table and he dives hastily for them."
                        "It only takes him a moment to slip one on and lube himself up, and then he's back on me like a lion on its prey."
                        show bree spoon bedroom2 scottie vaginal condom
                        "For all that he's a hopeless idiot elsewhere, Scottie really delivers where it matters."
                        "His dick is of a very nice size, and he knows exactly how to put it to good use."
                        "I want to keep on putting him in his place, enjoying the act so much."
                        "But he feels so good inside of me that I can't keep from moaning and panting like a bitch on heat."
                    "Don't":
                        "Part of me knows that I should stop Scottie and make him use protection, but the sight of his looming cock makes me desperate to get on with business."
                        show bree spoon bedroom2 scottie out
                        "So much so that I make no protest as he covers me and I feel the head of his dick slipping between my buttocks and hunting out my already welcoming pussy."
                        show bree spoon bedroom2 scottie vaginal
                        "He sinks into me, slowly at first and then with more urgency as he reaches the limits of his length."
                        "Scottie doesn't move for a few moments, and the feeling of his dick inside of me is almost enough to make me crazy"
                        "And then he begins to pull back and thrust forwards, gaining speed with each repetition."
                        "As I start to sigh and moan, I again find myself wondering why Sasha dumped the guy, rather than simply breaking him in properly."
                        menu:
                            "Let him cum inside":
                                bree.say "Don't stop now, I want to feel it all."
                                show bree spoon bedroom2 scottie vaginal creampie ahegao
                                "I don't know if Scottie was planning to pull out or not, but he won't if I have anything to do with it."
                                "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
                            "Tell him to pull out":
                                bree.say "Get your elephant prick out of me, asshole!"
                                bree.say "Right NOW!"
                                show bree spoon bedroom2 scottie out cum
                                "Scottie struggles to do as he's told, whipping his dick out a second before I cum."
                                "The sudden void only serves to intensify the sensations of orgasm, almost sending me into a fit of pleasure."
                                show bree spoon bedroom2 scottie out cum outside
                                "So much so that I hardly feel Scotties own cum raining down on my ass until it starts to cool and run down my thighs."
        if not "c" in posi:
            bree.say "No time for lounging around yet, asshole - you made a mess, so now clean it up!"
            if "v" in posi and scottie.sub < 80:
                "Scottie eagerly plucks up his underwear and begins to mop up between my thighs."
                "It's not the most erotic or romantic of gestures, but he seems to be trying to make a decent job of it all the same."
                "He works diligently, avoiding eye-contact until he feels that he's done."
                "And even then he waits patiently for me to inspect his works and nod in approval."
            elif "v" in posi:
                "Scottie doesn't need telling twice as he obliges me by lowering his head between my thighs."
                "He proceeds to clean me up by licking away at every accumulation of bodily fluids that he can find, and all without complaint."
                "All there is for me to do is lean back and allow him to do his thing."
                "Technically it might not be as hygienic as a shower, but it's certainly more enjoyable."
            elif "a" in posi and scottie.sub < 80:
                "Grabbing his discarded underwear, Scottie begins to dab away at my buttocks, rather like an inexperienced maid cleaning a valuable, yet fragile antique."
                "I've had more enjoyable post-sex experiences, but it's amusing to see a guy with that much swagger brought firmly to heel."
                bree.say "Make sure you do a good job back there - I want it so clean you could eat your dinner off of it!"
                "At that, Scottie redoubles his efforts, and I have to chuckle at the fact that he doesn't seem to have gotten the joke."
            elif "a" in posi:
                "Scottie is quick to crouch down and begin literally licking my ass clean."
                "He shows no shame whatsoever in using his tongue on my buttocks, persisting until there's no trace of cum to be found."
                "I don't think for a moment that he'll go deeper, but then I feel him gently part my cheeks and begin to probe between them too."
                "Scottie doesn't skimp either, exploring every inch until satisfied that he's done as he was told."
    hide bree
    "Scottie and I lie on the bed, exhausted and covered in sweat that's quickly cooling."
    "I make to say something, some small talk."
    "But I can already hear his snoring, loud as a chainsaw, in my ear."
    "I guess now the only decision left is to either kick him out, or else let him sleep it off here."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
